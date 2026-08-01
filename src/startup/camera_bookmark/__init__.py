import uuid

import bpy

from .layout import selector_tile_rects
from .preview import PREVIEW_IMAGE_PREFIX
from .preview import _remove_preview_image
from .preview import create_camera_preview
from .preview import preview_dimensions
from .state import active_camera
from .state import capture_camera_state
from .state import is_camera_view
from .state import restore_camera_state


_registered = False
_bookmark_items_cache = []
_keymap_items = []
_selection_update_suspended = 0


def bookmark_items(scene, _context):
    global _bookmark_items_cache

    items = []
    for index, bookmark in enumerate(scene.o_camera_bookmarks):
        image = bookmark.o_preview_image
        icon_id = 0
        if image is not None:
            image.preview_ensure()
            icon_id = image.preview.icon_id
        items.append(
            (
                bookmark.o_identifier,
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
        if bookmark.o_identifier == selected_identifier:
            return bookmark
    return None


def bookmark_by_identifier(scene, identifier):
    for bookmark in scene.o_camera_bookmarks:
        if bookmark.o_identifier == identifier:
            return bookmark
    return None


def restore_selected_bookmark(scene):
    bookmark = selected_bookmark(scene)
    if bookmark is None:
        raise ValueError("No bookmark is selected")

    camera = active_camera(scene)
    restore_camera_state(camera, bookmark.o_state_json)
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


class CameraBookmarkPropertyGroup(bpy.types.PropertyGroup):
    o_identifier: bpy.props.StringProperty(options={"HIDDEN"})
    o_name: bpy.props.StringProperty(name="Name", default="Bookmark")
    o_state_json: bpy.props.StringProperty(options={"HIDDEN"})
    o_preview_image: bpy.props.PointerProperty(type=bpy.types.Image)


class AddCameraBookmark(bpy.types.Operator):
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
        bookmark.o_identifier = identifier
        bookmark.o_name = f"Bookmark {len(scene.o_camera_bookmarks)}"
        bookmark.o_state_json = state_json
        bookmark.o_preview_image = preview_image
        scene.o_camera_bookmark_selection = identifier
        self.report({"INFO"}, "Added bookmark")
        return {"FINISHED"}


class UpdateCameraBookmark(bpy.types.Operator):
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
                bookmark.o_identifier,
            )
        except (OSError, RuntimeError, ValueError) as error:
            self.report({"ERROR"}, f"Unable to update bookmark: {error}")
            return {"CANCELLED"}

        previous_image = bookmark.o_preview_image
        bookmark.o_state_json = state_json
        bookmark.o_preview_image = preview_image
        if previous_image is not None:
            previous_image.name = f"{PREVIEW_IMAGE_PREFIX} Old"
        preview_image.name = f"{PREVIEW_IMAGE_PREFIX} {bookmark.o_identifier}"
        _remove_preview_image(previous_image)
        self.report({"INFO"}, "Updated bookmark")
        return {"FINISHED"}


class RecallCameraBookmark(bpy.types.Operator):
    bl_idname = "o.recall_camera_bookmark"
    bl_label = "Recall Bookmark"
    bl_description = "Restore the selected state to the active camera"
    bl_options = {"REGISTER", "UNDO"}

    o_bookmark_identifier: bpy.props.StringProperty(
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
        if self.o_bookmark_identifier:
            bookmark = bookmark_by_identifier(
                scene,
                self.o_bookmark_identifier,
            )
        if bookmark is None:
            bookmark = selected_bookmark(scene)
        if bookmark is None:
            self.report({"ERROR"}, "No bookmark is selected")
            return {"CANCELLED"}

        try:
            restore_camera_state(active_camera(scene), bookmark.o_state_json)
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}

        if scene.o_camera_bookmark_selection != bookmark.o_identifier:
            scene.o_camera_bookmark_selection = bookmark.o_identifier
        self.report({"INFO"}, "Restored bookmark")
        return {"FINISHED"}


class ShowCameraBookmarks(bpy.types.Operator):
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
            (bookmark.o_identifier, bookmark.o_preview_image)
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
                bookmark.o_state_json,
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


class RemoveCameraBookmark(bpy.types.Operator):
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
            if item.o_identifier == bookmark.o_identifier
        )
        preview_image = bookmark.o_preview_image

        scene.o_camera_bookmarks.remove(bookmark_index)
        _remove_preview_image(preview_image)

        remaining = scene.o_camera_bookmarks
        if remaining:
            next_index = min(bookmark_index, len(remaining) - 1)
            select_bookmark_without_recall(
                scene,
                remaining[next_index].o_identifier,
            )
        else:
            select_bookmark_without_recall(scene, "")

        self.report({"INFO"}, "Removed bookmark")
        return {"FINISHED"}


class CameraBookmarksPanel(bpy.types.Panel):
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
            AddCameraBookmark.bl_idname,
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
            RecallCameraBookmark.bl_idname,
            text="Recall",
            icon="VIEW_CAMERA",
        )
        controls.operator(
            UpdateCameraBookmark.bl_idname,
            text="Update",
            icon="FILE_REFRESH",
        )
        controls.operator(
            RemoveCameraBookmark.bl_idname,
            text="",
            icon="TRASH",
        )


class CameraBookmarksPieMenu(bpy.types.Menu):
    bl_idname = "O_MT_camera_bookmarks_pie"
    bl_label = "Bookmarks"

    @classmethod
    def poll(cls, context):
        return is_camera_view(context)

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator(
            AddCameraBookmark.bl_idname,
            text="Add Bookmark",
            icon="BOOKMARKS",
        )
        scene = context.scene
        if not scene.o_camera_bookmarks:
            pie.operator(
                ShowCameraBookmarks.bl_idname,
                text="No Bookmarks",
                icon="BOOKMARKS",
            )
            return

        pie.operator_context = "INVOKE_DEFAULT"
        pie.operator(
            ShowCameraBookmarks.bl_idname,
            text="Bookmarks",
            icon="BOOKMARKS",
        )


CLASSES = (
    CameraBookmarkPropertyGroup,
    AddCameraBookmark,
    UpdateCameraBookmark,
    RecallCameraBookmark,
    ShowCameraBookmarks,
    RemoveCameraBookmark,
    CameraBookmarksPanel,
    CameraBookmarksPieMenu,
)


def register():
    global _registered

    for class_type in CLASSES:
        bpy.utils.register_class(class_type)

    bpy.types.Scene.o_camera_bookmarks = bpy.props.CollectionProperty(
        type=CameraBookmarkPropertyGroup,
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
    keymap_item.properties.name = CameraBookmarksPieMenu.bl_idname
    _keymap_items.append((keymap, keymap_item))


def unregister_keymap():
    for keymap, keymap_item in _keymap_items:
        keymap.keymap_items.remove(keymap_item)
    _keymap_items.clear()
