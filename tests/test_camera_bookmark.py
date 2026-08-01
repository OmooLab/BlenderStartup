import importlib
import json
import sys
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))


class FakeMatrix(list):
    pass


class FakeCameraData:
    def __init__(self):
        self.type = "PERSP"
        self.lens = 50.0
        self.lens_unit = "MILLIMETERS"
        self.sensor_fit = "AUTO"
        self.sensor_width = 36.0
        self.sensor_height = 24.0
        self.shift_x = 0.1
        self.shift_y = -0.2
        self.clip_start = 0.1
        self.clip_end = 1000.0
        self.ortho_scale = 6.0
        self.dof = SimpleNamespace(
            use_dof=True,
            focus_distance=8.0,
            aperture_fstop=2.8,
            aperture_blades=6,
            aperture_rotation=0.2,
            aperture_ratio=1.0,
            focus_object=None,
        )
        self.update_count = 0

    def update_tag(self):
        self.update_count += 1


class FakeCamera:
    type = "CAMERA"

    def __init__(self):
        self.data = FakeCameraData()
        self.matrix_world = FakeMatrix(
            (
                (1.0, 0.0, 0.0, 2.0),
                (0.0, 1.0, 0.0, 3.0),
                (0.0, 0.0, 1.0, 4.0),
                (0.0, 0.0, 0.0, 1.0),
            )
        )
        self.update_count = 0

    def update_tag(self):
        self.update_count += 1


class CameraBookmarksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.remove_startup_modules()
        fake_bpy = ModuleType("bpy")
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
            GizmoGroup=object,
            Image=object,
            Menu=object,
            Operator=object,
            Panel=object,
            PropertyGroup=object,
            Scene=object,
        )
        fake_bpy.data = SimpleNamespace(
            objects={},
        )
        sys.modules["bpy"] = fake_bpy
        sys.modules["mathutils"] = SimpleNamespace(Matrix=FakeMatrix)

        cls.camera_bookmarks = importlib.import_module(
            "startup.camera_bookmark"
        )

    @classmethod
    def tearDownClass(cls):
        sys.modules.pop("bpy", None)
        sys.modules.pop("mathutils", None)
        cls.remove_startup_modules()

    def test_captures_camera_transform_and_parameters(self):
        camera = FakeCamera()

        state = json.loads(
            self.camera_bookmarks.capture_camera_state(camera)
        )

        self.assertEqual(state["matrix_world"][0][3], 2.0)
        self.assertEqual(state["camera"]["lens"], 50.0)
        self.assertEqual(state["camera"]["shift_y"], -0.2)
        self.assertTrue(state["dof"]["use_dof"])
        self.assertEqual(state["dof"]["aperture_fstop"], 2.8)

    def test_restores_state_to_current_camera(self):
        source_camera = FakeCamera()
        state_json = self.camera_bookmarks.capture_camera_state(source_camera)
        target_camera = FakeCamera()
        target_camera.matrix_world = FakeMatrix(
            (
                (1.0, 0.0, 0.0, 100.0),
                (0.0, 1.0, 0.0, 3.0),
                (0.0, 0.0, 1.0, 4.0),
                (0.0, 0.0, 0.0, 1.0),
            )
        )
        target_camera.data.lens = 18.0
        target_camera.data.dof.focus_distance = 1.0

        self.camera_bookmarks.restore_camera_state(
            target_camera,
            state_json,
        )

        self.assertEqual(target_camera.matrix_world[0][3], 2.0)
        self.assertEqual(target_camera.data.lens, 50.0)
        self.assertEqual(target_camera.data.dof.focus_distance, 8.0)
        self.assertEqual(target_camera.update_count, 1)
        self.assertEqual(target_camera.data.update_count, 1)

    def test_recall_operator_targets_explicit_bookmark_identifier(self):
        source_camera = FakeCamera()
        state_json = self.camera_bookmarks.capture_camera_state(source_camera)
        target_camera = FakeCamera()
        target_camera.data.lens = 18.0
        bookmark = SimpleNamespace(
            o_identifier="camera-a",
            o_name="Camera A",
            o_state_json=state_json,
        )
        scene = SimpleNamespace(
            camera=target_camera,
            o_camera_bookmarks=[bookmark],
            o_camera_bookmark_selection="",
        )
        operator = (
            self.camera_bookmarks.RecallCameraBookmark()
        )
        operator.o_bookmark_identifier = "camera-a"
        operator.report = lambda _levels, _message: None

        result = operator.execute(SimpleNamespace(scene=scene))

        self.assertEqual(result, {"FINISHED"})
        self.assertEqual(target_camera.data.lens, 50.0)
        self.assertEqual(
            scene.o_camera_bookmark_selection,
            "camera-a",
        )

    def test_rejects_invalid_camera_state(self):
        camera = FakeCamera()

        with self.assertRaisesRegex(ValueError, "invalid"):
            self.camera_bookmarks.restore_camera_state(camera, "{}")

    def test_preview_dimensions_preserve_render_aspect_ratio(self):
        render_settings = SimpleNamespace(
            resolution_x=1920,
            resolution_y=1080,
            resolution_percentage=50,
        )

        self.assertEqual(
            self.camera_bookmarks.preview_dimensions(render_settings),
            (320, 180),
        )

        render_settings.resolution_x = 1080
        render_settings.resolution_y = 1920
        self.assertEqual(
            self.camera_bookmarks.preview_dimensions(render_settings),
            (101, 180),
        )

    def test_selector_tiles_are_centered_and_clickable_without_labels(self):
        rects = self.camera_bookmarks.selector_tile_rects(
            2,
            1000,
            800,
            500,
            400,
        )

        self.assertEqual(
            rects,
            [
                (336.0, 355.0, 496.0, 445.0),
                (504.0, 355.0, 664.0, 445.0),
            ],
        )
        selector = self.camera_bookmarks.ShowCameraBookmarks()
        selector._rects = rects
        self.assertEqual(selector._hit_test(400, 400), 0)
        self.assertEqual(selector._hit_test(600, 400), 1)
        self.assertEqual(selector._hit_test(500, 400), -1)

    def test_camera_view_controls_pie_and_view_sidebar_panel(self):
        context = SimpleNamespace(
            area=SimpleNamespace(type="VIEW_3D"),
            region_data=SimpleNamespace(view_perspective="CAMERA"),
        )

        self.assertTrue(self.camera_bookmarks.is_camera_view(context))
        self.assertTrue(
            self.camera_bookmarks.CameraBookmarksPieMenu.poll(
                context
            )
        )
        self.assertTrue(
            self.camera_bookmarks.CameraBookmarksPanel.poll(context)
        )
        self.assertEqual(
            self.camera_bookmarks.CameraBookmarksPanel.bl_category,
            "View",
        )
        self.assertEqual(
            self.camera_bookmarks.CameraBookmarksPanel.bl_order,
            0,
        )
        self.assertEqual(
            self.camera_bookmarks.CameraBookmarksPanel.bl_label,
            "Bookmarks",
        )
        self.assertEqual(
            self.camera_bookmarks.CameraBookmarksPieMenu.bl_label,
            "Bookmarks",
        )
        self.assertEqual(
            self.camera_bookmarks.AddCameraBookmark.bl_label,
            "Add Bookmark",
        )

        context.region_data.view_perspective = "PERSP"
        self.assertFalse(self.camera_bookmarks.is_camera_view(context))
        self.assertFalse(
            self.camera_bookmarks.CameraBookmarksPieMenu.poll(
                context
            )
        )
        self.assertFalse(
            self.camera_bookmarks.CameraBookmarksPanel.poll(context)
        )

    def test_sidebar_add_bookmark_uses_bookmark_icon(self):
        operator_calls = []

        class Layout:
            def row(self, **_options):
                return self

            def label(self, **_options):
                return None

            def operator(self, operator_id, *, text, icon):
                operator_calls.append((operator_id, text, icon))

        panel = self.camera_bookmarks.CameraBookmarksPanel()
        panel.layout = Layout()
        panel.draw(
            SimpleNamespace(
                scene=SimpleNamespace(
                    camera=SimpleNamespace(type="CAMERA", name="Camera"),
                    o_camera_bookmarks=[],
                )
            )
        )

        self.assertEqual(
            operator_calls,
            [
                (
                    "o.add_camera_bookmark",
                    "Add Bookmark",
                    "BOOKMARKS",
                )
            ],
        )

    def test_silent_selection_change_does_not_recall_bookmark(self):
        recalls = []
        original_restore = self.camera_bookmarks.restore_selected_bookmark
        self.camera_bookmarks.restore_selected_bookmark = (
            lambda scene: recalls.append(
                scene.o_camera_bookmark_selection
            )
        )

        camera_bookmarks = self.camera_bookmarks

        class CallbackScene:
            def __init__(self):
                self._selection = ""

            @property
            def o_camera_bookmark_selection(self):
                return self._selection

            @o_camera_bookmark_selection.setter
            def o_camera_bookmark_selection(self, value):
                self._selection = value
                camera_bookmarks.update_bookmark_selection(self, None)

            def property_unset(self, property_name):
                self.assert_property_name(property_name)
                self._selection = ""
                camera_bookmarks.update_bookmark_selection(self, None)

            @staticmethod
            def assert_property_name(property_name):
                if property_name != "o_camera_bookmark_selection":
                    raise AssertionError(property_name)

        scene = CallbackScene()
        try:
            self.camera_bookmarks.select_bookmark_without_recall(
                scene,
                "camera-b",
            )
            self.assertEqual(recalls, [])

            self.camera_bookmarks.select_bookmark_without_recall(scene, "")
            self.assertEqual(scene.o_camera_bookmark_selection, "")
            self.assertEqual(recalls, [])

            scene.o_camera_bookmark_selection = "camera-c"
            self.assertEqual(recalls, ["camera-c"])
        finally:
            self.camera_bookmarks.restore_selected_bookmark = (
                original_restore
            )

    @staticmethod
    def remove_startup_modules():
        for module_name in tuple(sys.modules):
            if module_name == "startup" or module_name.startswith("startup."):
                sys.modules.pop(module_name)


if __name__ == "__main__":
    unittest.main()
