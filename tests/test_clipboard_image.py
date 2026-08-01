import importlib
import struct
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import Mock


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))


class ClipboardImageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary_directory = tempfile.TemporaryDirectory()
        cls.remove_startup_modules()
        fake_bpy = ModuleType("bpy")
        fake_bpy.app = SimpleNamespace(version=(5, 1, 0))
        fake_bpy.props = SimpleNamespace(
            BoolProperty=lambda **options: options,
            CollectionProperty=lambda **options: options,
            EnumProperty=lambda **options: options,
            FloatProperty=lambda **options: options,
            IntProperty=lambda **options: options,
            PointerProperty=lambda **options: options,
            StringProperty=lambda **options: options,
        )
        fake_bpy.types = SimpleNamespace(
            AddonPreferences=object,
            GizmoGroup=object,
            Image=object,
            Menu=object,
            Operator=object,
            Panel=object,
            PropertyGroup=object,
            Scene=object,
            TOPBAR_MT_file_defaults=SimpleNamespace(),
        )
        fake_bpy.utils = SimpleNamespace()
        fake_bpy.context = SimpleNamespace(
            window_manager=SimpleNamespace(
                keyconfigs=SimpleNamespace(addon=None),
            )
        )
        fake_bpy.data = SimpleNamespace()
        sys.modules["bpy"] = fake_bpy

        cls.addon = importlib.import_module("startup")
        cls.actions = cls.addon.clipboard_image.actions
        cls.clipboard = cls.addon.clipboard_image.clipboard

    @classmethod
    def tearDownClass(cls):
        sys.modules.pop("bpy", None)
        cls.remove_startup_modules()
        cls.temporary_directory.cleanup()

    def test_routes_supported_contexts(self):
        contexts = (
            (self.make_context("VIEW_3D"), "PLANE"),
            (
                self.make_context("VIEW_3D", mode="SCULPT"),
                "TOOL_TEXTURE",
            ),
            (
                self.make_context("VIEW_3D", mode="PAINT_VERTEX"),
                "TOOL_TEXTURE",
            ),
            (
                self.make_context("VIEW_3D", mode="PAINT_TEXTURE"),
                "TOOL_TEXTURE",
            ),
            (
                self.make_context(
                    "NODE_EDITOR",
                    tree_type="ShaderNodeTree",
                ),
                "NODE",
            ),
            (
                self.make_context(
                    "NODE_EDITOR",
                    tree_type="CompositorNodeTree",
                ),
                "NODE",
            ),
            (
                self.make_context(
                    "NODE_EDITOR",
                    tree_type="GeometryNodeTree",
                ),
                "NODE",
            ),
        )

        for context, expected_target in contexts:
            with self.subTest(expected_target=expected_target):
                self.assertEqual(
                    self.actions.target_for_context(context),
                    expected_target,
                )

    def test_rejects_unsupported_node_tree(self):
        context = self.make_context(
            "NODE_EDITOR",
            tree_type="TextureNodeTree",
        )

        self.assertIsNone(self.actions.target_for_context(context))

    def test_world_shader_uses_environment_texture(self):
        world_space = SimpleNamespace(
            tree_type="ShaderNodeTree",
            shader_type="WORLD",
        )
        material_space = SimpleNamespace(
            tree_type="ShaderNodeTree",
            shader_type="OBJECT",
        )

        self.assertEqual(
            self.actions._node_type_for_space(world_space),
            "ShaderNodeTexEnvironment",
        )
        self.assertEqual(
            self.actions._node_type_for_space(material_space),
            "ShaderNodeTexImage",
        )

    def test_pinned_world_tree_uses_environment_texture(self):
        world_space = SimpleNamespace(
            tree_type="ShaderNodeTree",
            shader_type="OBJECT",
            id=SimpleNamespace(
                bl_rna=SimpleNamespace(identifier="World"),
            ),
        )

        self.assertEqual(
            self.actions._node_type_for_space(world_space),
            "ShaderNodeTexEnvironment",
        )

    def test_preference_can_disable_clipboard_image_paste(self):
        context = SimpleNamespace(
            preferences=SimpleNamespace(
                addons={
                    self.addon.clipboard_image.ADDON_ID: SimpleNamespace(
                        preferences=SimpleNamespace(
                            enable_clipboard_image=False,
                        )
                    )
                }
            )
        )

        self.assertFalse(self.addon.clipboard_image.is_enabled(context))

    def test_preserves_image_aspect_ratio_for_plane(self):
        self.assertEqual(
            self.actions._plane_half_dimensions(1920, 1080),
            (1.0, 0.5625),
        )
        self.assertEqual(
            self.actions._plane_half_dimensions(800, 1200),
            (2 / 3, 1.0),
        )

    def test_subdivision_segments_adapt_to_image_aspect_ratio(self):
        self.assertEqual(
            self.actions._subdivision_segments(3, 4, 0),
            (1, 1),
        )
        self.assertEqual(
            self.actions._subdivision_segments(3, 4, 1),
            (2, 2),
        )
        self.assertEqual(
            self.actions._subdivision_segments(1, 4, 1),
            (2, 5),
        )
        self.assertEqual(
            self.actions._subdivision_segments(4, 1, 1),
            (5, 2),
        )
        self.assertEqual(
            self.actions._subdivision_segments(3, 4, 2),
            (3, 4),
        )

    def test_plane_grid_has_expected_topology(self):
        vertices, faces = self.actions._plane_grid(0.75, 1.0, 3, 4)

        self.assertEqual(len(vertices), 20)
        self.assertEqual(len(faces), 12)
        self.assertEqual(vertices[0], (-0.75, -1.0, 0.0))
        self.assertEqual(vertices[-1], (0.75, 1.0, 0.0))
        self.assertEqual(faces[0], (0, 1, 5, 4))

    def test_block_grid_is_closed_and_subdivided_through_depth(self):
        vertices, faces = self.actions._block_grid(
            1.0,
            0.5,
            0.25,
            2,
            1,
            3,
        )

        self.assertEqual(len(vertices), 24)
        self.assertEqual(len(faces), 22)
        self.assertIn((1.0, 0.5, 0.125), vertices)
        self.assertIn((-1.0, -0.5, -0.125), vertices)
        self.assertEqual(
            min(vertex[2] for vertex in vertices),
            -max(vertex[2] for vertex in vertices),
        )

        edge_counts = {}
        for face in faces:
            for index, start in enumerate(face):
                end = face[(index + 1) % len(face)]
                edge = tuple(sorted((start, end)))
                edge_counts[edge] = edge_counts.get(edge, 0) + 1
        self.assertTrue(all(count == 2 for count in edge_counts.values()))

    def test_depth_segments_adapt_to_surface_face_size(self):
        self.assertEqual(
            self.actions._depth_segments(1.0, 0.5, 4.0, 4, 2, 0),
            1,
        )
        self.assertEqual(
            self.actions._depth_segments(1.0, 0.5, 1.2, 4, 2, 1),
            2,
        )
        self.assertEqual(
            self.actions._depth_segments(1.0, 0.5, 1.3, 4, 2, 1),
            3,
        )

    def test_block_side_uvs_stretch_image_edges_through_depth(self):
        bottom_face = [
            SimpleNamespace(x=-1.0, y=-0.5, z=0.0),
            SimpleNamespace(x=-1.0, y=-0.5, z=-1.0),
            SimpleNamespace(x=1.0, y=-0.5, z=-1.0),
            SimpleNamespace(x=1.0, y=-0.5, z=0.0),
        ]
        left_face = [
            SimpleNamespace(x=-1.0, y=-0.5, z=0.0),
            SimpleNamespace(x=-1.0, y=0.5, z=0.0),
            SimpleNamespace(x=-1.0, y=0.5, z=-1.0),
            SimpleNamespace(x=-1.0, y=-0.5, z=-1.0),
        ]

        self.assertEqual(
            self.actions._block_face_uvs(bottom_face, 1.0, 0.5),
            [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (1.0, 0.0)],
        )
        self.assertEqual(
            self.actions._block_face_uvs(left_face, 1.0, 0.5),
            [(0.0, 0.0), (0.0, 1.0), (0.0, 1.0), (0.0, 0.0)],
        )

    def test_plane_subdivide_property_defaults_to_no_cuts(self):
        options = (
            self.addon.clipboard_image.O_OT_paste_clipboard_image
            .__annotations__["subdivisions"]
        )

        self.assertEqual(options["default"], 0)
        self.assertEqual(options["min"], 0)

    def test_plane_import_defaults_to_mesh_plane(self):
        options = (
            self.addon.clipboard_image.O_OT_paste_clipboard_image
            .__annotations__["import_as"]
        )

        self.assertEqual(options["default"], "PLANE")
        self.assertEqual(
            [item[0] for item in options["items"]],
            ["PLANE", "REFERENCE"],
        )

    def test_plane_unshaded_is_disabled_by_default(self):
        options = (
            self.addon.clipboard_image.O_OT_paste_clipboard_image
            .__annotations__["unshaded"]
        )

        self.assertFalse(options["default"])

    def test_plane_thickness_defaults_to_flat(self):
        options = (
            self.addon.clipboard_image.O_OT_paste_clipboard_image
            .__annotations__["thickness"]
        )

        self.assertEqual(options["default"], 0.0)
        self.assertEqual(options["min"], 0.0)

    def test_unshaded_nodes_mix_emission_with_transparency(self):
        created_nodes = {}

        def create_node(node_type):
            node = SimpleNamespace(location=None, inputs={}, outputs={})
            if node_type == "ShaderNodeBsdfTransparent":
                node.outputs["BSDF"] = object()
            elif node_type == "ShaderNodeEmission":
                node.inputs["Color"] = object()
                node.outputs["Emission"] = object()
            else:
                node.inputs = [object(), object(), object()]
                node.outputs["Shader"] = object()
            created_nodes[node_type] = node
            return node

        nodes = SimpleNamespace(new=Mock(side_effect=create_node))
        links = SimpleNamespace(new=Mock())
        image_node = SimpleNamespace(
            outputs={"Color": object(), "Alpha": object()},
        )
        output_node = SimpleNamespace(inputs={"Surface": object()})

        self.actions._create_unshaded_nodes(
            nodes,
            links,
            image_node,
            output_node,
        )

        mix_node = created_nodes["ShaderNodeMixShader"]
        links.new.assert_any_call(image_node.outputs["Alpha"], mix_node.inputs[0])
        links.new.assert_any_call(
            created_nodes["ShaderNodeEmission"].outputs["Emission"],
            mix_node.inputs[2],
        )
        self.assertEqual(links.new.call_count, 5)

    def test_reference_import_routes_to_image_empty(self):
        context = self.make_context("VIEW_3D")
        image = object()
        expected_reference = object()
        original_add_reference_image = self.actions.add_reference_image
        self.actions.add_reference_image = (
            lambda received_context, received_image: expected_reference
            if received_context is context and received_image is image
            else None
        )
        try:
            result = self.actions.paste_image(
                context,
                image,
                import_as="REFERENCE",
            )
        finally:
            self.actions.add_reference_image = original_add_reference_image

        self.assertIs(result, expected_reference)

    def test_subdivide_is_drawn_only_for_plane_paste(self):
        operator_class = (
            self.addon.clipboard_image.O_OT_paste_clipboard_image
        )
        operator = operator_class()
        drawn_properties = []
        operator.layout = SimpleNamespace(
            prop=lambda owner, name: drawn_properties.append((owner, name)),
        )

        operator.paste_target = "PLANE"
        operator.import_as = "PLANE"
        operator.draw(None)
        operator.import_as = "REFERENCE"
        operator.draw(None)
        operator.paste_target = "NODE"
        operator.draw(None)

        self.assertEqual(
            drawn_properties,
            [
                (operator, "import_as"),
                (operator, "thickness"),
                (operator, "subdivisions"),
                (operator, "unshaded"),
                (operator, "import_as"),
            ],
        )

    def test_image_plane_requires_object_mode(self):
        context = SimpleNamespace(mode="EDIT_MESH")
        image = SimpleNamespace(size=(100, 100))

        with self.assertRaisesRegex(
            self.actions.PasteTargetError,
            "Object Mode",
        ):
            self.actions.add_image_plane(context, image)

    def test_stencil_dimensions_preserve_scale_and_image_aspect(self):
        self.assertEqual(
            self.actions._stencil_dimensions(
                (1920, 1080),
                (400.0, 200.0),
            ),
            (400.0, 225.0),
        )
        self.assertEqual(
            self.actions._stencil_dimensions(
                (800, 1200),
                (128.0, 256.0),
            ),
            (256.0 * 2 / 3, 256.0),
        )

    def test_finds_existing_packed_clipboard_image(self):
        matching_image = FakeImage(
            self.actions.CLIPBOARD_HASH_PROPERTY,
            "matching-hash",
            packed=True,
        )
        unpacked_image = FakeImage(
            self.actions.CLIPBOARD_HASH_PROPERTY,
            "unpacked-hash",
            packed=False,
        )
        original_data = self.actions.bpy.data
        self.actions.bpy.data = SimpleNamespace(
            images=[matching_image, unpacked_image],
        )
        try:
            self.assertIs(
                self.actions._find_packed_clipboard_image("matching-hash"),
                matching_image,
            )
            self.assertIsNone(
                self.actions._find_packed_clipboard_image("unpacked-hash")
            )
        finally:
            self.actions.bpy.data = original_data

    def test_sets_and_reuses_stencil_brush_texture(self):
        textures = FakeTextures()
        original_data = self.actions.bpy.data
        self.actions.bpy.data = SimpleNamespace(textures=textures)
        brush = SimpleNamespace(
            is_editable=True,
            texture=None,
            texture_slot=SimpleNamespace(
                texture=None,
                map_mode="VIEW_PLANE",
            ),
            stencil_dimension=(256.0, 256.0),
            update_tag=lambda: None,
        )
        context = SimpleNamespace(brush=brush)
        image = SimpleNamespace(name="Clipboard Image", size=(1920, 1080))
        try:
            first_texture = self.actions.set_tool_texture(context, image)
            second_texture = self.actions.set_tool_texture(context, image)
        finally:
            self.actions.bpy.data = original_data

        self.assertIs(first_texture, second_texture)
        self.assertEqual(len(textures), 1)
        self.assertIs(brush.texture, first_texture)
        self.assertIs(brush.texture_slot.texture, first_texture)
        self.assertEqual(brush.texture_slot.map_mode, "STENCIL")
        self.assertEqual(brush.stencil_dimension, (256.0, 144.0))

    def test_localizes_read_only_active_brush(self):
        local_brush = SimpleNamespace(is_editable=True, library=None)
        linked_brush = SimpleNamespace(
            is_editable=False,
            library=None,
            make_local=lambda: local_brush,
        )

        self.assertIs(
            self.actions._ensure_editable_brush(
                SimpleNamespace(),
                linked_brush,
            ),
            local_brush,
        )

    def test_copies_and_activates_runtime_library_brush(self):
        local_brush = SimpleNamespace(
            name="Paint Hard Clipboard",
            is_editable=True,
            library=None,
        )
        library_brush = SimpleNamespace(
            name="Paint Hard",
            is_editable=True,
            library=object(),
        )
        paint_settings = SimpleNamespace(brush=library_brush)
        context = SimpleNamespace(
            mode="SCULPT",
            tool_settings=SimpleNamespace(sculpt=paint_settings),
        )

        original_ops = getattr(self.actions.bpy, "ops", None)

        def save_brush_as(**options):
            self.assertEqual(
                options["asset_library_reference"],
                "LOCAL",
            )
            self.assertEqual(options["name"], "Paint Hard Clipboard")
            paint_settings.brush = local_brush
            return {"FINISHED"}

        self.actions.bpy.ops = SimpleNamespace(
            brush=SimpleNamespace(asset_save_as=save_brush_as),
        )
        try:
            result = self.actions._ensure_editable_brush(
                context,
                library_brush,
            )
        finally:
            if original_ops is None:
                del self.actions.bpy.ops
            else:
                self.actions.bpy.ops = original_ops

        self.assertIs(result, local_brush)

    def test_active_brush_prefers_current_mode_settings(self):
        correct_brush = object()
        context = SimpleNamespace(
            brush=object(),
            mode="SCULPT",
            tool_settings=SimpleNamespace(
                sculpt=SimpleNamespace(brush=correct_brush),
            ),
        )

        self.assertIs(self.actions._active_brush(context), correct_brush)

    def test_vertex_and_texture_paint_use_unbiased_white(self):
        for mode in ("PAINT_VERTEX", "PAINT_TEXTURE"):
            with self.subTest(mode=mode):
                brush = SimpleNamespace(color=(0.2, 0.4, 0.8))
                unified_settings = SimpleNamespace(color=(0.8, 0.4, 0.2))
                context = SimpleNamespace(
                    mode=mode,
                    tool_settings=SimpleNamespace(
                        **{
                            self.actions.PAINT_SETTINGS_BY_MODE[mode][0]:
                                SimpleNamespace(
                                    unified_paint_settings=unified_settings,
                                )
                        },
                    ),
                )

                self.actions._set_unbiased_paint_color(context, brush)

                self.assertEqual(brush.color, (1.0, 1.0, 1.0))
                self.assertEqual(
                    unified_settings.color,
                    (1.0, 1.0, 1.0),
                )

    def test_sculpt_keeps_brush_color(self):
        brush = SimpleNamespace(color=(0.2, 0.4, 0.8))

        self.actions._set_unbiased_paint_color(
            SimpleNamespace(mode="SCULPT"),
            brush,
        )

        self.assertEqual(brush.color, (0.2, 0.4, 0.8))

    def test_wraps_info_dib_as_bmp(self):
        dib_header = struct.pack(
            "<IiiHHIIiiII",
            40,
            1,
            1,
            1,
            24,
            0,
            4,
            0,
            0,
            0,
            0,
        )
        dib_data = dib_header + b"\x00\x00\xff\x00"

        bmp_data = self.clipboard.dib_to_bmp(dib_data)

        signature, file_size, _, _, pixel_offset = struct.unpack_from(
            "<2sIHHI",
            bmp_data,
        )
        self.assertEqual(signature, b"BM")
        self.assertEqual(file_size, len(bmp_data))
        self.assertEqual(pixel_offset, 54)
        self.assertEqual(bmp_data[14:], dib_data)

    def test_rejects_truncated_dib(self):
        with self.assertRaises(self.clipboard.ClipboardImageError):
            self.clipboard.dib_to_bmp(b"\x28\x00\x00\x00")

    @staticmethod
    def make_context(area_type, mode="OBJECT", **space_options):
        return SimpleNamespace(
            area=SimpleNamespace(type=area_type),
            mode=mode,
            region=SimpleNamespace(type="WINDOW"),
            space_data=SimpleNamespace(**space_options),
        )

    @staticmethod
    def remove_startup_modules():
        for module_name in tuple(sys.modules):
            if module_name == "startup" or module_name.startswith("startup."):
                sys.modules.pop(module_name)


class FakeImage:
    def __init__(self, property_name, image_hash, packed):
        self.properties = {property_name: image_hash}
        self.packed_file = object() if packed else None
        self.packed_files = ()

    def get(self, property_name, default=None):
        return self.properties.get(property_name, default)


class FakeTexture(dict):
    def __init__(self, name, texture_type):
        super().__init__()
        self.name = name
        self.type = texture_type
        self.image = None


class FakeTextures(list):
    def new(self, name, type):
        texture = FakeTexture(name, type)
        self.append(texture)
        return texture

    def remove(self, texture):
        super().remove(texture)


if __name__ == "__main__":
    unittest.main()
