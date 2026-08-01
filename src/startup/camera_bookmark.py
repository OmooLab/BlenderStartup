import json
import os
import tempfile
import uuid
from pathlib import Path

import bpy


PREVIEW_MAX_WIDTH = 320
PREVIEW_MAX_HEIGHT = 180
PREVIEW_IMAGE_PREFIX = "O Bookmark"
SELECTOR_TILE_WIDTH = 160.0
SELECTOR_TILE_HEIGHT = 90.0
SELECTOR_TILE_GAP = 8.0
SELECTOR_MARGIN = 12.0
SELECTOR_MAX_COLUMNS = 4

CAMERA_PROPERTIES = (
    "type",
    "lens",
    "lens_unit",
    "sensor_fit",
    "sensor_width",
    "sensor_height",
    "shift_x",
    "shift_y",
    "clip_start",
    "clip_end",
    "ortho_scale",
    "panorama_type",
    "fisheye_fov",
    "fisheye_lens",
    "latitude_min",
    "latitude_max",
    "longitude_min",
    "longitude_max",
)

DOF_PROPERTIES = (
    "use_dof",
    "focus_distance",
    "aperture_fstop",
    "aperture_blades",
    "aperture_rotation",
    "aperture_ratio",
)

_registered = False
_bookmark_items_cache = []
_keymap_items = []
_selection_update_suspended = 0


def is_camera_view(context):
    area = getattr(context, "area", None)
    if area is None or getattr(area, "type", None) != "VIEW_3D":
        return False

    region_3d = getattr(context, "region_data", None)
    if region_3d is None:
        space_data = getattr(context, "space_data", None)
        region_3d = getattr(space_data, "region_3d", None)
    return (
        region_3d is not None
        and region_3d.view_perspective == "CAMERA"
    )


def active_camera(scene):
    camera = getattr(scene, "camera", None)
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        return None
    return camera


def _serializable_properties(owner, property_names):
    values = {}
    for property_name in property_names:
        if not hasattr(owner, property_name):
            continue
        value = getattr(owner, property_name)
        if isinstance(value, (bool, float, int, str)):
            values[property_name] = value
    return values


def capture_camera_state(camera):
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        raise ValueError("The scene has no active camera")

    camera_data = camera.data
    state = {
        "matrix_world": [
            [float(value) for value in row]
            for row in camera.matrix_world
        ],
        "camera": _serializable_properties(
            camera_data,
            CAMERA_PROPERTIES,
        ),
    }

    dof = getattr(camera_data, "dof", None)
    if dof is not None:
        state["dof"] = _serializable_properties(dof, DOF_PROPERTIES)
        focus_object = getattr(dof, "focus_object", None)
        if focus_object is not None:
            state["dof"]["focus_object"] = focus_object.name

    return json.dumps(state, separators=(",", ":"), sort_keys=True)


def _restore_properties(owner, values):
    for property_name, value in values.items():
        if not hasattr(owner, property_name):
            continue
        try:
            setattr(owner, property_name, value)
        except (AttributeError, TypeError, ValueError):
            continue


def restore_camera_state(camera, state_json):
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        raise ValueError("The scene has no active camera")

    try:
        state = json.loads(state_json)
        matrix_rows = state["matrix_world"]
        camera_values = state["camera"]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise ValueError("The bookmark data is invalid") from error

    if (
        len(matrix_rows) != 4
        or any(len(row) != 4 for row in matrix_rows)
    ):
        raise ValueError("The bookmark transform is invalid")

    from mathutils import Matrix

    camera.matrix_world = Matrix(matrix_rows)
    camera_data = camera.data

    camera_type = camera_values.get("type")
    if camera_type is not None:
        _restore_properties(camera_data, {"type": camera_type})
    _restore_properties(
        camera_data,
        {
            name: value
            for name, value in camera_values.items()
            if name != "type"
        },
    )

    dof_values = state.get("dof", {})
    focus_object_name = dof_values.pop("focus_object", None)
    dof = getattr(camera_data, "dof", None)
    if dof is not None:
        _restore_properties(dof, dof_values)
        if focus_object_name:
            dof.focus_object = bpy.data.objects.get(focus_object_name)
        elif hasattr(dof, "focus_object"):
            dof.focus_object = None

    camera.update_tag()
    camera_data.update_tag()


def preview_dimensions(render_settings):
    percentage = max(1, render_settings.resolution_percentage) / 100
    source_width = max(1, round(render_settings.resolution_x * percentage))
    source_height = max(1, round(render_settings.resolution_y * percentage))
    scale = min(
        PREVIEW_MAX_WIDTH / source_width,
        PREVIEW_MAX_HEIGHT / source_height,
    )
    return (
        max(1, round(source_width * scale)),
        max(1, round(source_height * scale)),
    )


def selector_tile_rects(
    count,
    region_width,
    region_height,
    anchor_x,
    anchor_y,
):
    if count <= 0:
        return []

    columns = min(SELECTOR_MAX_COLUMNS, count)
    rows = (count + columns - 1) // columns
    content_width = (
        columns * SELECTOR_TILE_WIDTH
        + (columns - 1) * SELECTOR_TILE_GAP
    )
    content_height = (
        rows * SELECTOR_TILE_HEIGHT
        + (rows - 1) * SELECTOR_TILE_GAP
    )
    available_width = max(1.0, region_width - SELECTOR_MARGIN * 2.0)
    available_height = max(1.0, region_height - SELECTOR_MARGIN * 2.0)
    scale = min(
        1.0,
        available_width / content_width,
        available_height / content_height,
    )
    tile_width = SELECTOR_TILE_WIDTH * scale
    tile_height = SELECTOR_TILE_HEIGHT * scale
    gap = SELECTOR_TILE_GAP * scale
    panel_width = columns * tile_width + (columns - 1) * gap
    panel_height = rows * tile_height + (rows - 1) * gap

    left = min(
        max(SELECTOR_MARGIN, anchor_x - panel_width / 2.0),
        region_width - SELECTOR_MARGIN - panel_width,
    )
    bottom = min(
        max(SELECTOR_MARGIN, anchor_y - panel_height / 2.0),
        region_height - SELECTOR_MARGIN - panel_height,
    )

    rects = []
    for index in range(count):
        column = index % columns
        row = index // columns
        x_min = left + column * (tile_width + gap)
        y_max = bottom + panel_height - row * (tile_height + gap)
        rects.append(
            (
                x_min,
                y_max - tile_height,
                x_min + tile_width,
                y_max,
            )
        )
    return rects


def _capture_render_settings(render_settings):
    image_settings = render_settings.image_settings
    return {
        "filepath": render_settings.filepath,
        "resolution_x": render_settings.resolution_x,
        "resolution_y": render_settings.resolution_y,
        "resolution_percentage": render_settings.resolution_percentage,
        "use_file_extension": render_settings.use_file_extension,
        "file_format": image_settings.file_format,
        "color_mode": image_settings.color_mode,
        "color_depth": image_settings.color_depth,
        "compression": image_settings.compression,
    }


def _restore_render_settings(render_settings, values):
    image_settings = render_settings.image_settings
    render_settings.filepath = values["filepath"]
    render_settings.resolution_x = values["resolution_x"]
    render_settings.resolution_y = values["resolution_y"]
    render_settings.resolution_percentage = values["resolution_percentage"]
    render_settings.use_file_extension = values["use_file_extension"]
    image_settings.file_format = values["file_format"]
    image_settings.color_mode = values["color_mode"]
    image_settings.color_depth = values["color_depth"]
    image_settings.compression = values["compression"]


def create_camera_preview(scene, identifier):
    render_settings = scene.render
    previous_settings = _capture_render_settings(render_settings)
    preview_width, preview_height = preview_dimensions(render_settings)
    file_descriptor, temporary_name = tempfile.mkstemp(suffix=".png")
    os.close(file_descriptor)
    temporary_file = Path(temporary_name)
    temporary_file.unlink(missing_ok=True)

    image = None
    try:
        render_settings.filepath = str(temporary_file)
        render_settings.resolution_x = preview_width
        render_settings.resolution_y = preview_height
        render_settings.resolution_percentage = 100
        render_settings.use_file_extension = False
        render_settings.image_settings.file_format = "PNG"
        render_settings.image_settings.color_mode = "RGBA"
        render_settings.image_settings.color_depth = "8"
        render_settings.image_settings.compression = 50

        result = bpy.ops.render.opengl(
            write_still=True,
            view_context=False,
        )
        if "FINISHED" not in result or not temporary_file.is_file():
            raise RuntimeError("Blender could not render the camera preview")

        image = bpy.data.images.load(
            str(temporary_file),
            check_existing=False,
        )
        image.name = f"{PREVIEW_IMAGE_PREFIX} {identifier}"
        # 临时 PNG 只用于生成 Image，pack 后缩略图会随 .blend 保存。
        image.pack()
        image.preview_ensure()
        return image
    except Exception:
        if image is not None:
            bpy.data.images.remove(image)
        raise
    finally:
        _restore_render_settings(render_settings, previous_settings)
        temporary_file.unlink(missing_ok=True)


def _remove_preview_image(image):
    if image is None:
        return
    if image.users == 0:
        bpy.data.images.remove(image)


def bookmark_items(scene, _context):
    global _bookmark_items_cache

    items = []
    for index, bookmark in enumerate(scene.o_camera_bookmarks):
        image = bookmark.preview_image
        icon_id = 0
        if image is not None:
            image.preview_ensure()
            icon_id = image.preview.icon_id
        items.append(
            (
                bookmark.identifier,
                "Bookmark",
                "Restore bookmark",
                icon_id,
                index,
            )
        )
    _bookmark_items_cache = items
    return _bookmark_items_cache


def selected_bookmark(scene):
    selected_identifier = scene.o_camera_bookmark_selection
    for bookmark in scene.o_camera_bookmarks:
        if bookmark.identifier == selected_identifier:
            return bookmark
    return None


def bookmark_by_identifier(scene, identifier):
    for bookmark in scene.o_camera_bookmarks:
        if bookmark.identifier == identifier:
            return bookmark
    return None


def restore_selected_bookmark(scene):
    bookmark = selected_bookmark(scene)
    if bookmark is None:
        raise ValueError("No bookmark is selected")

    camera = active_camera(scene)
    restore_camera_state(camera, bookmark.state_json)
    return bookmark


def update_bookmark_selection(scene, _context):
    if _selection_update_suspended:
        return
    if not scene.o_camera_bookmark_selection:
        return
    try:
        restore_selected_bookmark(scene)
    except ValueError as error:
        print(f"Bookmarks: {error}")


def select_bookmark_without_recall(scene, identifier):
    global _selection_update_suspended

    _selection_update_suspended += 1
    try:
        if identifier:
            scene.o_camera_bookmark_selection = identifier
        else:
            scene.property_unset("o_camera_bookmark_selection")
    finally:
        _selection_update_suspended -= 1


class O_PG_camera_bookmark(bpy.types.PropertyGroup):
    identifier: bpy.props.StringProperty(options={"HIDDEN"})
    name: bpy.props.StringProperty(name="Name", default="Bookmark")
    state_json: bpy.props.StringProperty(options={"HIDDEN"})
    preview_image: bpy.props.PointerProperty(type=bpy.types.Image)


class O_OT_add_camera_bookmark(bpy.types.Operator):
    bl_idname = "o.add_camera_bookmark"
    bl_label = "Add Bookmark"
    bl_description = "Add the active camera state as a bookmark with a preview"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            active_camera(context.scene) is not None
        )

    def execute(self, context):
        scene = context.scene
        camera = active_camera(scene)
        identifier = uuid.uuid4().hex

        try:
            state_json = capture_camera_state(camera)
            preview_image = create_camera_preview(scene, identifier)
        except (OSError, RuntimeError, ValueError) as error:
            self.report({"ERROR"}, f"Unable to add bookmark: {error}")
            return {"CANCELLED"}

        bookmark = scene.o_camera_bookmarks.add()
        bookmark.identifier = identifier
        bookmark.name = f"Bookmark {len(scene.o_camera_bookmarks)}"
        bookmark.state_json = state_json
        bookmark.preview_image = preview_image
        scene.o_camera_bookmark_selection = identifier
        self.report({"INFO"}, "Added bookmark")
        return {"FINISHED"}


class O_OT_update_camera_bookmark(bpy.types.Operator):
    bl_idname = "o.update_camera_bookmark"
    bl_label = "Update Bookmark"
    bl_description = "Replace the selected bookmark state and preview"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            active_camera(context.scene) is not None
            and selected_bookmark(context.scene) is not None
        )

    def execute(self, context):
        scene = context.scene
        bookmark = selected_bookmark(scene)
        camera = active_camera(scene)

        try:
            state_json = capture_camera_state(camera)
            preview_image = create_camera_preview(
                scene,
                bookmark.identifier,
            )
        except (OSError, RuntimeError, ValueError) as error:
            self.report({"ERROR"}, f"Unable to update bookmark: {error}")
            return {"CANCELLED"}

        previous_image = bookmark.preview_image
        bookmark.state_json = state_json
        bookmark.preview_image = preview_image
        if previous_image is not None:
            previous_image.name = f"{PREVIEW_IMAGE_PREFIX} Old"
        preview_image.name = f"{PREVIEW_IMAGE_PREFIX} {bookmark.identifier}"
        _remove_preview_image(previous_image)
        self.report({"INFO"}, "Updated bookmark")
        return {"FINISHED"}


class O_OT_recall_camera_bookmark(bpy.types.Operator):
    bl_idname = "o.recall_camera_bookmark"
    bl_label = "Recall Bookmark"
    bl_description = "Restore the selected state to the active camera"
    bl_options = {"REGISTER", "UNDO"}

    bookmark_identifier: bpy.props.StringProperty(
        options={"HIDDEN", "SKIP_SAVE"},
    )

    @classmethod
    def poll(cls, context):
        return (
            active_camera(context.scene) is not None
            and bool(context.scene.o_camera_bookmarks)
        )

    def execute(self, context):
        scene = context.scene
        bookmark = None
        if self.bookmark_identifier:
            bookmark = bookmark_by_identifier(
                scene,
                self.bookmark_identifier,
            )
        if bookmark is None:
            bookmark = selected_bookmark(scene)
        if bookmark is None:
            self.report({"ERROR"}, "No bookmark is selected")
            return {"CANCELLED"}

        try:
            restore_camera_state(active_camera(scene), bookmark.state_json)
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}

        if scene.o_camera_bookmark_selection != bookmark.identifier:
            scene.o_camera_bookmark_selection = bookmark.identifier
        self.report({"INFO"}, "Restored bookmark")
        return {"FINISHED"}


class O_OT_show_camera_bookmarks(bpy.types.Operator):
    bl_idname = "o.show_camera_bookmarks"
    bl_label = "Bookmarks"
    bl_description = "Choose a bookmark by its preview"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        area = getattr(context, "area", None)
        return (
            area is not None
            and area.type == "VIEW_3D"
            and active_camera(context.scene) is not None
            and bool(context.scene.o_camera_bookmarks)
        )

    def invoke(self, context, event):
        self._area = context.area
        self._region = context.region
        self._bookmarks = [
            (bookmark.identifier, bookmark.preview_image)
            for bookmark in context.scene.o_camera_bookmarks
        ]
        self._rects = selector_tile_rects(
            len(self._bookmarks),
            context.region.width,
            context.region.height,
            event.mouse_region_x,
            event.mouse_region_y,
        )
        self._hover_index = -1
        self._draw_handle = bpy.types.SpaceView3D.draw_handler_add(
            self._draw,
            (),
            "WINDOW",
            "POST_PIXEL",
        )
        context.window_manager.modal_handler_add(self)
        context.area.tag_redraw()
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type == "MOUSEMOVE":
            self._hover_index = self._hit_test(
                event.mouse_region_x,
                event.mouse_region_y,
            )
            context.area.tag_redraw()
            return {"RUNNING_MODAL"}

        if event.type == "LEFTMOUSE" and event.value == "PRESS":
            bookmark_index = self._hit_test(
                event.mouse_region_x,
                event.mouse_region_y,
            )
            if bookmark_index < 0:
                self._finish(context)
                return {"CANCELLED"}
            result = self._recall(context, bookmark_index)
            self._finish(context)
            return result

        should_cancel = (
            event.type == "WINDOW_DEACTIVATE"
            or (
                event.type in {"ESC", "RIGHTMOUSE"}
                and event.value == "PRESS"
            )
        )
        if should_cancel:
            self._finish(context)
            return {"CANCELLED"}

        return {"RUNNING_MODAL"}

    def cancel(self, context):
        self._finish(context)

    def _recall(self, context, bookmark_index):
        identifier, _image = self._bookmarks[bookmark_index]
        bookmark = bookmark_by_identifier(context.scene, identifier)
        if bookmark is None:
            self.report({"ERROR"}, "Bookmark no longer exists")
            return {"CANCELLED"}

        try:
            restore_camera_state(
                active_camera(context.scene),
                bookmark.state_json,
            )
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}

        context.scene.o_camera_bookmark_selection = identifier
        self.report({"INFO"}, "Restored bookmark")
        return {"FINISHED"}

    def _hit_test(self, x, y):
        for index, rect in enumerate(self._rects):
            x_min, y_min, x_max, y_max = rect
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return index
        return -1

    def _finish(self, context):
        draw_handle = getattr(self, "_draw_handle", None)
        if draw_handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(
                draw_handle,
                "WINDOW",
            )
            self._draw_handle = None
        area = getattr(self, "_area", None)
        if area is not None:
            area.tag_redraw()

    def _draw(self):
        import gpu
        from gpu_extras.batch import batch_for_shader

        color_shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        try:
            image_shader = gpu.shader.from_builtin(
                "IMAGE_SCENE_LINEAR_TO_REC709_SRGB"
            )
        except ValueError:
            image_shader = gpu.shader.from_builtin("IMAGE")
        gpu.state.blend_set("ALPHA")

        try:
            for index, ((_, image), rect) in enumerate(
                zip(self._bookmarks, self._rects)
            ):
                color = (
                    (0.16, 0.42, 0.8, 1.0)
                    if index == self._hover_index
                    else (0.08, 0.08, 0.08, 0.95)
                )
                self._draw_color_quad(
                    batch_for_shader,
                    color_shader,
                    rect,
                    color,
                )
                if image is None:
                    continue
                self._draw_image_quad(
                    gpu,
                    batch_for_shader,
                    image_shader,
                    image,
                    rect,
                )
        finally:
            gpu.state.blend_set("NONE")

    @staticmethod
    def _draw_color_quad(batch_for_shader, shader, rect, color):
        x_min, y_min, x_max, y_max = rect
        coordinates = (
            (x_min, y_min),
            (x_max, y_min),
            (x_max, y_max),
            (x_min, y_max),
        )
        batch = batch_for_shader(
            shader,
            "TRI_FAN",
            {"pos": coordinates},
        )
        shader.bind()
        shader.uniform_float("color", color)
        batch.draw(shader)

    @staticmethod
    def _draw_image_quad(
        gpu,
        batch_for_shader,
        shader,
        image,
        rect,
    ):
        inset = 3.0
        x_min, y_min, x_max, y_max = rect
        x_min += inset
        y_min += inset
        x_max -= inset
        y_max -= inset
        width = max(1, image.size[0])
        height = max(1, image.size[1])
        image_aspect = width / height
        rect_aspect = (x_max - x_min) / (y_max - y_min)
        if image_aspect > rect_aspect:
            image_height = (x_max - x_min) / image_aspect
            offset = ((y_max - y_min) - image_height) / 2.0
            y_min += offset
            y_max = y_min + image_height
        else:
            image_width = (y_max - y_min) * image_aspect
            offset = ((x_max - x_min) - image_width) / 2.0
            x_min += offset
            x_max = x_min + image_width

        coordinates = (
            (x_min, y_min),
            (x_max, y_min),
            (x_max, y_max),
            (x_min, y_max),
        )
        texture_coordinates = (
            (0.0, 0.0),
            (1.0, 0.0),
            (1.0, 1.0),
            (0.0, 1.0),
        )
        batch = batch_for_shader(
            shader,
            "TRI_FAN",
            {
                "pos": coordinates,
                "texCoord": texture_coordinates,
            },
        )
        texture = gpu.texture.from_image(image)
        shader.bind()
        shader.uniform_sampler("image", texture)
        batch.draw(shader)


class O_OT_remove_camera_bookmark(bpy.types.Operator):
    bl_idname = "o.remove_camera_bookmark"
    bl_label = "Remove Bookmark"
    bl_description = "Remove the selected bookmark and its preview"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            selected_bookmark(context.scene) is not None
        )

    def execute(self, context):
        scene = context.scene
        bookmark = selected_bookmark(scene)
        bookmark_index = next(
            index
            for index, item in enumerate(scene.o_camera_bookmarks)
            if item.identifier == bookmark.identifier
        )
        preview_image = bookmark.preview_image

        scene.o_camera_bookmarks.remove(bookmark_index)
        _remove_preview_image(preview_image)

        remaining = scene.o_camera_bookmarks
        if remaining:
            next_index = min(bookmark_index, len(remaining) - 1)
            select_bookmark_without_recall(
                scene,
                remaining[next_index].identifier,
            )
        else:
            select_bookmark_without_recall(scene, "")

        self.report({"INFO"}, "Removed bookmark")
        return {"FINISHED"}


class O_PT_camera_bookmarks(bpy.types.Panel):
    bl_idname = "O_PT_camera_bookmarks"
    bl_label = "Bookmarks"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_order = 0

    @classmethod
    def poll(cls, context):
        return is_camera_view(context)

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        camera = active_camera(scene)

        header = layout.row(align=True)
        if camera is None:
            header.label(text="No Active Camera", icon="ERROR")
        else:
            header.label(text=camera.name, icon="CAMERA_DATA")
        header.operator(
            O_OT_add_camera_bookmark.bl_idname,
            text="Add Bookmark",
            icon="BOOKMARKS",
        )

        if not scene.o_camera_bookmarks:
            layout.label(text="Add a bookmark from the active camera")
            return

        layout.template_icon_view(
            scene,
            "o_camera_bookmark_selection",
            show_labels=False,
            scale=6.0,
            scale_popup=6.0,
        )

        bookmark = selected_bookmark(scene)
        if bookmark is None:
            layout.label(text="Select a bookmark", icon="INFO")
            return

        controls = layout.row(align=True)
        controls.operator(
            O_OT_recall_camera_bookmark.bl_idname,
            text="Recall",
            icon="VIEW_CAMERA",
        )
        controls.operator(
            O_OT_update_camera_bookmark.bl_idname,
            text="Update",
            icon="FILE_REFRESH",
        )
        controls.operator(
            O_OT_remove_camera_bookmark.bl_idname,
            text="",
            icon="TRASH",
        )


class O_MT_camera_bookmarks_pie(bpy.types.Menu):
    bl_idname = "O_MT_camera_bookmarks_pie"
    bl_label = "Bookmarks"

    @classmethod
    def poll(cls, context):
        return is_camera_view(context)

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator(
            O_OT_add_camera_bookmark.bl_idname,
            text="Add Bookmark",
            icon="BOOKMARKS",
        )
        scene = context.scene
        if not scene.o_camera_bookmarks:
            pie.operator(
                O_OT_show_camera_bookmarks.bl_idname,
                text="No Bookmarks",
                icon="BOOKMARKS",
            )
            return

        pie.operator_context = "INVOKE_DEFAULT"
        pie.operator(
            O_OT_show_camera_bookmarks.bl_idname,
            text="Bookmarks",
            icon="BOOKMARKS",
        )


CLASSES = (
    O_PG_camera_bookmark,
    O_OT_add_camera_bookmark,
    O_OT_update_camera_bookmark,
    O_OT_recall_camera_bookmark,
    O_OT_show_camera_bookmarks,
    O_OT_remove_camera_bookmark,
    O_PT_camera_bookmarks,
    O_MT_camera_bookmarks_pie,
)


def register():
    global _registered

    for class_type in CLASSES:
        bpy.utils.register_class(class_type)

    bpy.types.Scene.o_camera_bookmarks = bpy.props.CollectionProperty(
        type=O_PG_camera_bookmark,
    )
    bpy.types.Scene.o_camera_bookmark_selection = bpy.props.EnumProperty(
        name="Bookmarks",
        description="Select a bookmark to restore it to the active camera",
        items=bookmark_items,
        update=update_bookmark_selection,
    )
    register_keymap()
    _registered = True


def unregister():
    global _registered

    if not _registered:
        return

    unregister_keymap()

    del bpy.types.Scene.o_camera_bookmark_selection
    del bpy.types.Scene.o_camera_bookmarks

    for class_type in reversed(CLASSES):
        bpy.utils.unregister_class(class_type)
    _registered = False


def register_keymap():
    keyconfigs = getattr(bpy.context.window_manager, "keyconfigs", None)
    addon_keyconfig = getattr(keyconfigs, "addon", None)
    if addon_keyconfig is None:
        return

    keymap = addon_keyconfig.keymaps.new(
        name="3D View",
        space_type="VIEW_3D",
    )
    keymap_item = keymap.keymap_items.new(
        "wm.call_menu_pie",
        "ACCENT_GRAVE",
        "PRESS",
        shift=True,
    )
    keymap_item.properties.name = O_MT_camera_bookmarks_pie.bl_idname
    _keymap_items.append((keymap, keymap_item))


def unregister_keymap():
    for keymap, keymap_item in _keymap_items:
        keymap.keymap_items.remove(keymap_item)
    _keymap_items.clear()
