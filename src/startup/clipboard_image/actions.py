import hashlib
import os
import tempfile

import bpy


CLIPBOARD_HASH_PROPERTY = "o_clipboard_sha256"
CLIPBOARD_TEXTURE_PROPERTY = "o_clipboard_texture"
DEFAULT_STENCIL_SIZE = 256.0
NODE_TYPES = {
    "CompositorNodeTree": "CompositorNodeImage",
    "ShaderNodeTree": "ShaderNodeTexImage",
    "GeometryNodeTree": "GeometryNodeImageTexture",
}
WORLD_TEXTURE_NODE_TYPE = "ShaderNodeTexEnvironment"

BRUSH_TEXTURE_MODES = {
    "SCULPT",
    "PAINT_TEXTURE",
    "PAINT_VERTEX",
}

WHITE_BRUSH_COLOR_MODES = {
    "PAINT_TEXTURE",
    "PAINT_VERTEX",
}

PAINT_SETTINGS_BY_MODE = {
    "SCULPT": ("sculpt",),
    "PAINT_TEXTURE": ("image_paint",),
    "PAINT_VERTEX": ("vertex_paint",),
    "PAINT_WEIGHT": ("weight_paint",),
    "PAINT_GREASE_PENCIL": ("grease_pencil_paint", "gpencil_paint"),
    "VERTEX_GREASE_PENCIL": ("gpencil_vertex_paint",),
    "SCULPT_GREASE_PENCIL": ("grease_pencil_sculpt", "gpencil_sculpt_paint"),
    "WEIGHT_GREASE_PENCIL": ("grease_pencil_weight", "gpencil_weight_paint"),
    "SCULPT_CURVES": ("curves_sculpt",),
}


class PasteTargetError(RuntimeError):
    pass


def target_for_context(context):
    area = getattr(context, "area", None)
    area_type = getattr(area, "type", None)
    if area_type == "VIEW_3D":
        if getattr(context, "mode", "OBJECT") in BRUSH_TEXTURE_MODES:
            return "TOOL_TEXTURE"
        return "PLANE"
    if area_type != "NODE_EDITOR":
        return None

    tree_type = getattr(getattr(context, "space_data", None), "tree_type", None)
    if tree_type in NODE_TYPES:
        return "NODE"
    return None


def acquire_packed_image(image_data, suffix):
    image_hash = hashlib.sha256(image_data).hexdigest()
    existing_image = _find_packed_clipboard_image(image_hash)
    if existing_image is not None:
        return existing_image, True

    file_descriptor, temporary_path = tempfile.mkstemp(
        prefix="blender-clipboard-",
        suffix=suffix,
    )
    image = None
    try:
        with os.fdopen(file_descriptor, "wb") as temporary_file:
            temporary_file.write(image_data)
        image = bpy.data.images.load(temporary_path, check_existing=False)
        image.name = "Clipboard Image"
        image.pack()
        image[CLIPBOARD_HASH_PROPERTY] = image_hash
        return image, False
    except (OSError, RuntimeError):
        if image is not None:
            bpy.data.images.remove(image)
        raise
    finally:
        try:
            os.unlink(temporary_path)
        except FileNotFoundError:
            pass


def _find_packed_clipboard_image(image_hash):
    for image in bpy.data.images:
        if image.get(CLIPBOARD_HASH_PROPERTY) != image_hash:
            continue
        if _is_image_packed(image):
            return image
    return None


def _is_image_packed(image):
    if getattr(image, "packed_file", None) is not None:
        return True
    return bool(getattr(image, "packed_files", ()))


def paste_image(
    context,
    image,
    event=None,
    subdivisions=0,
    import_as="PLANE",
    unshaded=False,
    thickness=0.0,
):
    target = target_for_context(context)
    if target == "PLANE":
        if import_as == "REFERENCE":
            return add_reference_image(context, image)
        return add_image_plane(
            context,
            image,
            subdivisions=subdivisions,
            unshaded=unshaded,
            thickness=thickness,
        )
    if target == "NODE":
        return add_image_node(context, image, event)
    if target == "TOOL_TEXTURE":
        return set_tool_texture(context, image)
    raise PasteTargetError("Paste images from a 3D View or Node Editor")


def add_image_plane(
    context,
    image,
    subdivisions=0,
    unshaded=False,
    thickness=0.0,
):
    if getattr(context, "mode", "OBJECT") != "OBJECT":
        raise PasteTargetError("Switch to Object Mode before pasting an image plane")

    width, height = image.size
    if width <= 0 or height <= 0:
        raise PasteTargetError("The clipboard image has invalid dimensions")

    half_width, half_height = _plane_half_dimensions(width, height)
    x_segments, y_segments = _subdivision_segments(
        width,
        height,
        subdivisions,
    )
    thickness = max(0.0, float(thickness))
    if thickness == 0.0:
        vertices, faces = _plane_grid(
            half_width,
            half_height,
            x_segments,
            y_segments,
        )
    else:
        # 厚度以局部 Z=0 为中心对称分布，使物体原点保持在几何中心。
        depth_segments = _depth_segments(
            half_width,
            half_height,
            thickness,
            x_segments,
            y_segments,
            subdivisions,
        )
        vertices, faces = _block_grid(
            half_width,
            half_height,
            thickness,
            x_segments,
            y_segments,
            depth_segments,
        )

    shape_name = "Plane" if thickness == 0.0 else "Block"
    mesh = bpy.data.meshes.new(f"{image.name} {shape_name}")
    mesh.from_pydata(vertices, (), faces)
    mesh.update()
    if thickness == 0.0:
        _add_plane_uv_map(mesh, x_segments, y_segments)
    else:
        _add_block_uv_map(mesh, half_width, half_height)

    material = _create_image_material(image, unshaded)
    mesh.materials.append(material)

    plane = bpy.data.objects.new(image.name, mesh)
    context.collection.objects.link(plane)
    _place_in_view(context, plane)
    _select_only(context, plane)
    return plane


def add_reference_image(context, image):
    if getattr(context, "mode", "OBJECT") != "OBJECT":
        raise PasteTargetError(
            "Switch to Object Mode before pasting a reference image"
        )

    width, height = image.size
    if width <= 0 or height <= 0:
        raise PasteTargetError("The clipboard image has invalid dimensions")

    reference = bpy.data.objects.new(image.name, None)
    reference.empty_display_type = "IMAGE"
    reference.data = image
    reference.empty_display_size = 2.0
    context.collection.objects.link(reference)
    _place_in_view(context, reference)
    _select_only(context, reference)
    return reference


def _place_in_view(context, target_object):
    target_object.location = context.scene.cursor.location
    region_data = getattr(context, "region_data", None)
    if region_data is not None:
        target_object.rotation_euler = region_data.view_rotation.to_euler()


def _plane_half_dimensions(width, height):
    if width >= height:
        return 1.0, height / width
    return width / height, 1.0


def _subdivision_segments(width, height, subdivisions):
    cuts = max(0, int(subdivisions))
    if cuts == 0:
        return 1, 1

    x_cuts = cuts
    y_cuts = cuts
    if width > height:
        x_cuts = max(cuts, int(width / height * cuts + 0.5))
    elif height > width:
        y_cuts = max(cuts, int(height / width * cuts + 0.5))
    return x_cuts + 1, y_cuts + 1


def _plane_grid(half_width, half_height, x_segments, y_segments):
    columns = x_segments + 1
    vertices = []
    for y_index in range(y_segments + 1):
        y = -half_height + 2.0 * half_height * y_index / y_segments
        for x_index in range(x_segments + 1):
            x = -half_width + 2.0 * half_width * x_index / x_segments
            vertices.append((x, y, 0.0))

    faces = []
    for y_index in range(y_segments):
        row_start = y_index * columns
        next_row_start = row_start + columns
        for x_index in range(x_segments):
            bottom_left = row_start + x_index
            bottom_right = bottom_left + 1
            top_left = next_row_start + x_index
            top_right = top_left + 1
            faces.append((bottom_left, bottom_right, top_right, top_left))
    return vertices, faces


def _depth_segments(
    half_width,
    half_height,
    thickness,
    x_segments,
    y_segments,
    subdivisions,
):
    if int(subdivisions) <= 0:
        return 1

    x_step = 2.0 * half_width / x_segments
    y_step = 2.0 * half_height / y_segments
    target_step = (x_step * y_step) ** 0.5
    return max(1, int(thickness / target_step + 0.5))


def _block_grid(
    half_width,
    half_height,
    thickness,
    x_segments,
    y_segments,
    depth_segments,
):
    vertices = []
    vertex_indices = {}

    def vertex_index(x_index, y_index, z_index):
        key = (x_index, y_index, z_index)
        existing_index = vertex_indices.get(key)
        if existing_index is not None:
            return existing_index

        x = -half_width + 2.0 * half_width * x_index / x_segments
        y = -half_height + 2.0 * half_height * y_index / y_segments
        z = thickness * (0.5 - z_index / depth_segments)
        index = len(vertices)
        vertices.append((x, y, z))
        vertex_indices[key] = index
        return index

    faces = []

    for y_index in range(y_segments):
        for x_index in range(x_segments):
            faces.append(
                (
                    vertex_index(x_index, y_index, 0),
                    vertex_index(x_index + 1, y_index, 0),
                    vertex_index(x_index + 1, y_index + 1, 0),
                    vertex_index(x_index, y_index + 1, 0),
                )
            )
            faces.append(
                (
                    vertex_index(x_index, y_index, depth_segments),
                    vertex_index(x_index, y_index + 1, depth_segments),
                    vertex_index(x_index + 1, y_index + 1, depth_segments),
                    vertex_index(x_index + 1, y_index, depth_segments),
                )
            )

    for z_index in range(depth_segments):
        for x_index in range(x_segments):
            faces.append(
                (
                    vertex_index(x_index, 0, z_index),
                    vertex_index(x_index, 0, z_index + 1),
                    vertex_index(x_index + 1, 0, z_index + 1),
                    vertex_index(x_index + 1, 0, z_index),
                )
            )
            faces.append(
                (
                    vertex_index(x_index, y_segments, z_index),
                    vertex_index(x_index + 1, y_segments, z_index),
                    vertex_index(x_index + 1, y_segments, z_index + 1),
                    vertex_index(x_index, y_segments, z_index + 1),
                )
            )

        for y_index in range(y_segments):
            faces.append(
                (
                    vertex_index(0, y_index, z_index),
                    vertex_index(0, y_index + 1, z_index),
                    vertex_index(0, y_index + 1, z_index + 1),
                    vertex_index(0, y_index, z_index + 1),
                )
            )
            faces.append(
                (
                    vertex_index(x_segments, y_index, z_index),
                    vertex_index(x_segments, y_index, z_index + 1),
                    vertex_index(x_segments, y_index + 1, z_index + 1),
                    vertex_index(x_segments, y_index + 1, z_index),
                )
            )

    return vertices, faces


def _add_plane_uv_map(mesh, x_segments, y_segments):
    uv_layer = mesh.uv_layers.new(name="UVMap")
    columns = x_segments + 1
    for loop in mesh.loops:
        x_index = loop.vertex_index % columns
        y_index = loop.vertex_index // columns
        uv_layer.data[loop.index].uv = (
            x_index / x_segments,
            y_index / y_segments,
        )


def _add_block_uv_map(mesh, half_width, half_height):
    uv_layer = mesh.uv_layers.new(name="UVMap")
    for polygon in mesh.polygons:
        coordinates = [
            mesh.vertices[mesh.loops[loop_index].vertex_index].co
            for loop_index in polygon.loop_indices
        ]
        uvs = _block_face_uvs(coordinates, half_width, half_height)

        for loop_index, uv in zip(polygon.loop_indices, uvs):
            uv_layer.data[loop_index].uv = uv


def _block_face_uvs(coordinates, half_width, half_height):
    x_values = [coordinate.x for coordinate in coordinates]
    y_values = [coordinate.y for coordinate in coordinates]
    z_values = [coordinate.z for coordinate in coordinates]

    if max(z_values) - min(z_values) < 1e-9:
        return [
            (
                (coordinate.x + half_width) / (2.0 * half_width),
                (coordinate.y + half_height) / (2.0 * half_height),
            )
            for coordinate in coordinates
        ]

    if max(y_values) - min(y_values) < 1e-9:
        edge_v = 1.0 if y_values[0] > 0.0 else 0.0
        return [
            (
                (coordinate.x + half_width) / (2.0 * half_width),
                edge_v,
            )
            for coordinate in coordinates
        ]

    edge_u = 1.0 if x_values[0] > 0.0 else 0.0
    return [
        (
            edge_u,
            (coordinate.y + half_height) / (2.0 * half_height),
        )
        for coordinate in coordinates
    ]


def _create_image_material(image, unshaded=False):
    material = bpy.data.materials.new(name=f"{image.name} Material")
    material.use_nodes = True
    if hasattr(material, "surface_render_method"):
        material.surface_render_method = "DITHERED"

    nodes = material.node_tree.nodes
    nodes.clear()
    image_node = nodes.new("ShaderNodeTexImage")
    image_node.image = image
    image_node.location = (-620.0, 80.0)

    output_node = nodes.new("ShaderNodeOutputMaterial")
    output_node.location = (220.0, 80.0)

    links = material.node_tree.links
    if unshaded:
        _create_unshaded_nodes(nodes, links, image_node, output_node)
        return material

    shader_node = nodes.new("ShaderNodeBsdfPrincipled")
    shader_node.location = (-160.0, 80.0)
    links.new(image_node.outputs["Color"], shader_node.inputs["Base Color"])
    links.new(image_node.outputs["Alpha"], shader_node.inputs["Alpha"])
    links.new(shader_node.outputs["BSDF"], output_node.inputs["Surface"])
    return material


def _create_unshaded_nodes(nodes, links, image_node, output_node):
    transparent_node = nodes.new("ShaderNodeBsdfTransparent")
    transparent_node.location = (-360.0, -100.0)

    emission_node = nodes.new("ShaderNodeEmission")
    emission_node.location = (-360.0, 120.0)

    mix_node = nodes.new("ShaderNodeMixShader")
    mix_node.location = (-80.0, 80.0)

    links.new(image_node.outputs["Color"], emission_node.inputs["Color"])
    links.new(image_node.outputs["Alpha"], mix_node.inputs[0])
    links.new(transparent_node.outputs["BSDF"], mix_node.inputs[1])
    links.new(emission_node.outputs["Emission"], mix_node.inputs[2])
    links.new(mix_node.outputs["Shader"], output_node.inputs["Surface"])


def _select_only(context, plane):
    for selected_object in getattr(context, "selected_objects", ()):
        selected_object.select_set(False)
    plane.select_set(True)
    context.view_layer.objects.active = plane


def add_image_node(context, image, event=None):
    space = context.space_data
    node_tree = getattr(space, "edit_tree", None)
    if node_tree is None:
        node_tree = getattr(space, "node_tree", None)
    if node_tree is None:
        raise PasteTargetError("The Node Editor has no editable node tree")

    node_type = _node_type_for_space(space)
    if node_type is None:
        raise PasteTargetError(f"Unsupported node tree: {space.tree_type}")

    node = node_tree.nodes.new(node_type)
    _assign_node_image(node, image)
    node.location = _node_location(context, event)
    _select_only_node(node_tree, node)
    return node


def _node_type_for_space(space):
    if _is_world_shader_space(space):
        return WORLD_TEXTURE_NODE_TYPE
    return NODE_TYPES.get(getattr(space, "tree_type", None))


def _is_world_shader_space(space):
    if getattr(space, "tree_type", None) != "ShaderNodeTree":
        return False
    if getattr(space, "shader_type", None) == "WORLD":
        return True

    owner_id = getattr(space, "id", None)
    owner_rna = getattr(owner_id, "bl_rna", None)
    return getattr(owner_rna, "identifier", None) == "World"


def _assign_node_image(node, image):
    if hasattr(node, "image"):
        node.image = image
        return

    # Geometry Nodes 的 Image Texture 把图片存在 Image socket，而非 node.image。
    image_input = node.inputs.get("Image")
    if image_input is None or not hasattr(image_input, "default_value"):
        raise PasteTargetError("The image node has no assignable image input")
    image_input.default_value = image


def _node_location(context, event):
    if event is not None:
        region = getattr(context, "region", None)
        view2d = getattr(region, "view2d", None)
        if view2d is not None:
            return view2d.region_to_view(
                event.mouse_region_x,
                event.mouse_region_y,
            )

    cursor_location = getattr(context.space_data, "cursor_location", None)
    if cursor_location is not None:
        return cursor_location
    return (0.0, 0.0)


def _select_only_node(node_tree, node):
    for existing_node in node_tree.nodes:
        existing_node.select = False
    node.select = True
    node_tree.nodes.active = node


def set_tool_texture(context, image):
    brush = _active_brush(context)
    if brush is None:
        raise PasteTargetError("The active tool does not provide an editable brush")
    brush = _ensure_editable_brush(context, brush)

    texture, is_new = _find_or_create_image_texture(image)
    try:
        brush.texture = texture
        brush.texture_slot.texture = texture
        brush.texture_slot.map_mode = "STENCIL"
        brush.stencil_dimension = _stencil_dimensions(
            image.size,
            brush.stencil_dimension,
        )
        if brush.texture != texture or brush.texture_slot.texture != texture:
            raise PasteTargetError("Blender did not bind the texture to the active brush")
        _set_unbiased_paint_color(context, brush)
        brush.update_tag()
    except (AttributeError, TypeError, RuntimeError) as error:
        if is_new:
            bpy.data.textures.remove(texture)
        raise PasteTargetError(
            f"The active brush could not use the image texture: {error}"
        ) from error
    _redraw_area(context)
    return texture


def _set_unbiased_paint_color(context, brush):
    if getattr(context, "mode", "") not in WHITE_BRUSH_COLOR_MODES:
        return

    white = (1.0, 1.0, 1.0)
    brush.color = white

    tool_settings = getattr(context, "tool_settings", None)
    if tool_settings is None:
        scene = getattr(context, "scene", None)
        tool_settings = getattr(scene, "tool_settings", None)

    unified_settings = None
    mode = getattr(context, "mode", "")
    for settings_name in PAINT_SETTINGS_BY_MODE.get(mode, ()):
        paint_settings = getattr(tool_settings, settings_name, None)
        unified_settings = getattr(
            paint_settings,
            "unified_paint_settings",
            None,
        )
        if unified_settings is not None:
            break
    if unified_settings is None:
        unified_settings = getattr(tool_settings, "unified_paint_settings", None)
    if unified_settings is not None:
        unified_settings.color = white


def _ensure_editable_brush(context, brush):
    brush_library = getattr(brush, "library", None)
    brush_is_editable = getattr(brush, "is_editable", True)
    if brush_library is None and brush_is_editable:
        return brush

    if brush_library is not None:
        return _copy_and_activate_library_brush(context, brush)

    make_local = getattr(brush, "make_local", None)
    if make_local is None:
        raise PasteTargetError("The active brush is read-only and cannot be localized")

    # Brush Asset 可能来自外部库；先本地化，才能引用当前 .blend 中的 Texture。
    try:
        local_brush = make_local()
    except RuntimeError as error:
        raise PasteTargetError(
            f"Unable to make the active brush local: {error}"
        ) from error

    if local_brush is None:
        local_brush = brush
    if getattr(local_brush, "library", None) is not None:
        raise PasteTargetError("The active brush still belongs to an external library")
    if not getattr(local_brush, "is_editable", False):
        raise PasteTargetError("The localized brush is still read-only")
    return local_brush


def _copy_and_activate_library_brush(context, brush):
    try:
        result = bpy.ops.brush.asset_save_as(
            name=f"{brush.name} Clipboard",
            asset_library_reference="LOCAL",
        )
    except (AttributeError, RuntimeError) as error:
        raise PasteTargetError(
            f"Unable to create a local copy of the active Brush Asset: {error}"
        ) from error

    if result != {"FINISHED"}:
        raise PasteTargetError("Unable to activate the local Brush Asset copy")

    active_brush = _active_brush(context)
    if active_brush is None or getattr(active_brush, "library", None) is not None:
        raise PasteTargetError("Blender did not activate a local Brush Asset copy")
    return active_brush


def _find_or_create_image_texture(image):
    for texture in bpy.data.textures:
        if not texture.get(CLIPBOARD_TEXTURE_PROPERTY, False):
            continue
        if texture.image == image:
            return texture, False

    texture = bpy.data.textures.new(name=f"{image.name} Texture", type="IMAGE")
    texture.image = image
    texture[CLIPBOARD_TEXTURE_PROPERTY] = True
    return texture, True


def _stencil_dimensions(image_size, current_dimensions):
    width, height = image_size
    if width <= 0 or height <= 0:
        raise PasteTargetError("The clipboard image has invalid dimensions")

    stencil_size = max(current_dimensions, default=DEFAULT_STENCIL_SIZE)
    if stencil_size <= 0:
        stencil_size = DEFAULT_STENCIL_SIZE
    if width >= height:
        return stencil_size, stencil_size * height / width
    return stencil_size * width / height, stencil_size


def _active_brush(context):
    mode = getattr(context, "mode", "")
    tool_settings = getattr(context, "tool_settings", None)
    if tool_settings is None:
        scene = getattr(context, "scene", None)
        tool_settings = getattr(scene, "tool_settings", None)

    for settings_name in PAINT_SETTINGS_BY_MODE.get(mode, ()):
        paint_settings = getattr(tool_settings, settings_name, None)
        brush = getattr(paint_settings, "brush", None)
        if brush is not None:
            return brush

    return getattr(context, "brush", None)


def _redraw_area(context):
    area = getattr(context, "area", None)
    tag_redraw = getattr(area, "tag_redraw", None)
    if tag_redraw is not None:
        tag_redraw()
