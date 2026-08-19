import sys
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))


class FakeOperator:
    pass


class FakeObject(dict):
    def __init__(
        self,
        *,
        color=(0.2, 0.4, 0.6, 0.8),
        hide_render=False,
        show_transparent=False,
        visible_camera=True,
        visible_raycast=True,
        visible_shadow=True,
    ):
        super().__init__()
        self.color = color
        self.hide_render = hide_render
        self.show_transparent = show_transparent
        self.visible_camera = visible_camera
        self.visible_raycast = visible_raycast
        self.visible_shadow = visible_shadow


class PhantomTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fake_bpy = ModuleType("bpy")
        fake_bpy.props = SimpleNamespace(
            BoolProperty=lambda **options: options,
            CollectionProperty=lambda **options: options,
            EnumProperty=lambda **options: options,
            FloatProperty=lambda **options: options,
            FloatVectorProperty=lambda **options: options,
            IntProperty=lambda **options: options,
            PointerProperty=lambda **options: options,
            StringProperty=lambda **options: options,
        )
        fake_bpy.types = SimpleNamespace(
            GizmoGroup=object,
            Image=object,
            Menu=object,
            Operator=FakeOperator,
            Panel=object,
            PropertyGroup=object,
            Scene=object,
        )
        sys.modules["bpy"] = fake_bpy

        from startup import toggle_phantom as phantom

        cls.phantom = phantom

    @classmethod
    def tearDownClass(cls):
        sys.modules.pop("bpy", None)
        for module_name in tuple(sys.modules):
            if module_name == "startup" or module_name.startswith("startup."):
                sys.modules.pop(module_name)

    def test_enable_phantom_sets_transparency_and_render_visibility(self):
        obj = FakeObject()

        self.phantom.enable_phantom(obj)

        self.assertTrue(self.phantom.is_phantom(obj))
        self.assertEqual(obj.color, (0.2, 0.4, 0.6, 0.35))
        self.assertTrue(obj.show_transparent)
        self.assertFalse(obj.visible_camera)
        self.assertFalse(obj.visible_raycast)
        self.assertFalse(obj.visible_shadow)
        self.assertFalse(obj.hide_render)

    def test_disable_phantom_restores_previous_settings(self):
        obj = FakeObject(
            color=(0.1, 0.3, 0.5, 0.7),
            hide_render=True,
            show_transparent=True,
            visible_camera=False,
            visible_raycast=False,
            visible_shadow=False,
        )

        self.phantom.enable_phantom(obj)
        self.phantom.disable_phantom(obj)

        self.assertFalse(self.phantom.is_phantom(obj))
        self.assertEqual(obj.color, (0.1, 0.3, 0.5, 0.7))
        self.assertTrue(obj.show_transparent)
        self.assertFalse(obj.visible_camera)
        self.assertFalse(obj.visible_raycast)
        self.assertFalse(obj.visible_shadow)
        self.assertTrue(obj.hide_render)
        self.assertEqual(obj, {})

    def test_operator_toggles_context_object(self):
        obj = FakeObject()
        context = SimpleNamespace(object=obj)
        operator = self.phantom.TogglePhantom()

        self.assertEqual(operator.execute(context), {"FINISHED"})
        self.assertTrue(self.phantom.is_phantom(obj))
        self.assertEqual(operator.execute(context), {"FINISHED"})
        self.assertFalse(self.phantom.is_phantom(obj))

    def test_works_without_raycast_visibility_property(self):
        obj = FakeObject()
        del obj.visible_raycast

        self.phantom.enable_phantom(obj)
        self.phantom.disable_phantom(obj)

        self.assertFalse(self.phantom.is_phantom(obj))

    def test_operator_requires_context_object(self):
        operator = self.phantom.TogglePhantom

        self.assertFalse(operator.poll(SimpleNamespace(object=None)))
        self.assertTrue(operator.poll(SimpleNamespace(object=FakeObject())))


if __name__ == "__main__":
    unittest.main()
