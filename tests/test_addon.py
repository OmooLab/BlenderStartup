import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))


class FakeMenu:
    callbacks = []
    registration_method = None

    @classmethod
    def append(cls, callback):
        cls.callbacks.append(callback)
        cls.registration_method = "append"

    @classmethod
    def prepend(cls, callback):
        cls.callbacks.insert(0, callback)
        cls.registration_method = "prepend"

    @classmethod
    def remove(cls, callback):
        cls.callbacks.remove(callback)


class FakeObjectContextMenu(FakeMenu):
    callbacks = []
    registration_method = None


class FakeViewPie(FakeMenu):
    callbacks = []
    registration_method = None


class FakeUtils:
    def __init__(self):
        self.registered_classes = []
        self.scripts_directory = None

    def register_class(self, operator_class):
        self.registered_classes.append(operator_class)

    def unregister_class(self, operator_class):
        self.registered_classes.remove(operator_class)

    def user_resource(self, resource_type, path="", create=False):
        if resource_type != "SCRIPTS" or self.scripts_directory is None:
            return ""

        resource_path = Path(self.scripts_directory) / path
        if create:
            resource_path.mkdir(parents=True, exist_ok=True)
        return str(resource_path)


class FakeOperator:
    def __init__(self):
        self.reports = []

    def report(self, levels, message):
        self.reports.append((levels, message))


class FakePropertyGroup:
    pass


class FakePanel:
    pass


class FakeBpyMenu:
    pass


class FakeScene:
    pass


class FakeKeyMapItems:
    def __init__(self):
        self.items = []

    def new(self, operator_id, event_type, value, **modifiers):
        keymap_item = SimpleNamespace(
            idname=operator_id,
            type=event_type,
            value=value,
            properties=SimpleNamespace(),
            **modifiers,
        )
        self.items.append(keymap_item)
        return keymap_item

    def remove(self, keymap_item):
        self.items.remove(keymap_item)


class FakeKeyMaps:
    def __init__(self):
        self.items = []

    def new(self, name, space_type):
        keymap = SimpleNamespace(
            name=name,
            space_type=space_type,
            keymap_items=FakeKeyMapItems(),
        )
        self.items.append(keymap)
        return keymap


class TemplateRegistrationTest(unittest.TestCase):
    def setUp(self):
        FakeMenu.callbacks = []
        FakeMenu.registration_method = None
        FakeObjectContextMenu.callbacks = []
        FakeObjectContextMenu.registration_method = None
        FakeViewPie.callbacks = []
        FakeViewPie.registration_method = None
        self.template_directory = tempfile.TemporaryDirectory()
        self.scripts_directory = tempfile.TemporaryDirectory()
        self.fake_bpy = self.create_fake_bpy()
        self.fake_bpy.utils.scripts_directory = self.scripts_directory.name
        sys.modules["bpy"] = self.fake_bpy
        self.remove_startup_modules()

        import startup

        self.addon = startup
        self.addon.KEYCONFIG_FILE = (
            Path(self.template_directory.name)
            / "keyconfig.py"
        )
        self.addon.KEYCONFIG_FILE.write_text(
            "keyconfig source",
            encoding="utf-8",
        )

    def tearDown(self):
        if self.addon._registered:
            self.addon.unregister()
        sys.modules.pop("bpy", None)
        self.remove_startup_modules()
        self.scripts_directory.cleanup()
        self.template_directory.cleanup()

    def test_registers_template_features(self):
        self.addon.register()

        self.assertEqual(FakeMenu.callbacks, [])
        self.assertEqual(len(self.fake_bpy.utils.registered_classes), 10)
        self.assertEqual(len(FakeObjectContextMenu.callbacks), 1)
        self.assertEqual(FakeObjectContextMenu.registration_method, "append")
        context_layout = FakeLayout()
        FakeObjectContextMenu.callbacks[0](
            SimpleNamespace(layout=context_layout),
            None,
        )
        self.assertEqual(context_layout.operator_id, "o.toggle_phantom")
        self.assertEqual(context_layout.operator_text, "Toggle Phantom")
        self.assertTrue(context_layout.separator_called)
        self.assertEqual(context_layout.actions, ["separator", "operator"])
        self.assertEqual(FakeViewPie.callbacks, [])
        installed_keyconfig = (
            Path(self.scripts_directory.name)
            / "presets"
            / "keyconfig"
            / "Refined_Industry_Compatible.py"
        )
        self.assertEqual(
            installed_keyconfig.read_text(encoding="utf-8"),
            "keyconfig source",
        )
        self.addon.unregister()
        self.assertEqual(self.fake_bpy.utils.registered_classes, [])
        self.assertEqual(FakeObjectContextMenu.callbacks, [])
        self.assertEqual(FakeViewPie.callbacks, [])

    def test_loads_only_feature_packages_present_on_disk(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            feature_root = Path(temporary_directory)
            feature_directory = feature_root / "available_feature"
            feature_directory.mkdir()
            (feature_directory / "__init__.py").touch()

            original_directory = self.addon.TEMPLATE_DIRECTORY
            self.addon.TEMPLATE_DIRECTORY = feature_root
            loaded_module = object()
            try:
                with patch.object(
                    self.addon.importlib,
                    "import_module",
                    return_value=loaded_module,
                ) as import_module:
                    modules = self.addon.load_feature_modules(
                        ("missing_feature", "available_feature"),
                    )
            finally:
                self.addon.TEMPLATE_DIRECTORY = original_directory

        self.assertEqual(modules, (loaded_module,))
        import_module.assert_called_once_with(
            ".available_feature",
            self.addon.__package__,
        )

    def test_registered_classes_follow_project_naming_convention(self):
        self.addon.register()

        registered_classes = self.fake_bpy.utils.registered_classes
        self.assertTrue(registered_classes)
        for class_type in registered_classes:
            with self.subTest(class_name=class_type.__name__):
                self.assertRegex(class_type.__name__, r"^[A-Z][A-Za-z0-9]*$")
                annotations = getattr(class_type, "__annotations__", {})
                for property_name in annotations:
                    self.assertRegex(property_name, r"^o_[a-z][a-z0-9_]*$")

        operator_classes = [
            item for item in registered_classes
            if issubclass(item, self.fake_bpy.types.Operator)
        ]
        menu_classes = [
            item for item in registered_classes
            if issubclass(item, self.fake_bpy.types.Menu)
        ]
        panel_classes = [
            item for item in registered_classes
            if issubclass(item, self.fake_bpy.types.Panel)
        ]
        for class_type in operator_classes:
            self.assertRegex(class_type.bl_idname, r"^o\.[a-z][a-z0-9_]*$")
        for class_type in menu_classes:
            self.assertTrue(class_type.__name__.endswith("Menu"))
            self.assertRegex(class_type.bl_idname, r"^O_MT_[a-z][a-z0-9_]*$")
        for class_type in panel_classes:
            self.assertTrue(class_type.__name__.endswith("Panel"))
            self.assertRegex(class_type.bl_idname, r"^O_PT_[a-z][a-z0-9_]*$")

    def test_updates_installed_keyconfig_without_activating_it(self):
        installed_keyconfig = (
            Path(self.scripts_directory.name)
            / "presets"
            / "keyconfig"
            / "Refined_Industry_Compatible.py"
        )
        installed_keyconfig.parent.mkdir(parents=True)
        installed_keyconfig.write_text("outdated", encoding="utf-8")

        self.addon.register()

        self.assertEqual(
            installed_keyconfig.read_text(encoding="utf-8"),
            "keyconfig source",
        )

    def test_custom_camera_bookmarks_pie_draws_triggerable_actions(self):
        self.addon.register()
        layout = FakeLayout()
        menu_class = next(
            class_type
            for class_type in self.fake_bpy.utils.registered_classes
            if getattr(class_type, "bl_idname", None)
            == "O_MT_camera_bookmarks_pie"
        )
        menu = menu_class()
        menu.layout = layout
        bookmark = SimpleNamespace(
            o_identifier="bookmark-1",
        )
        scene = SimpleNamespace(
            o_camera_bookmarks=[bookmark],
            o_camera_bookmark_selection="bookmark-1",
        )
        menu.draw(SimpleNamespace(scene=scene))

        self.assertEqual(
            [action[0] for action in layout.operator_calls],
            [
                "o.add_camera_bookmark",
                "o.show_camera_bookmarks",
            ],
        )
        self.assertEqual(
            [action[1] for action in layout.operator_calls],
            ["Add Bookmark", "Bookmarks"],
        )
        self.assertEqual(
            [action[2] for action in layout.operator_calls],
            ["BOOKMARKS", "BOOKMARKS"],
        )

    def test_custom_camera_bookmarks_pie_uses_button_for_empty_state(self):
        self.addon.register()
        layout = FakeLayout()
        menu_class = next(
            class_type
            for class_type in self.fake_bpy.utils.registered_classes
            if getattr(class_type, "bl_idname", None)
            == "O_MT_camera_bookmarks_pie"
        )
        menu = menu_class()
        menu.layout = layout
        menu.draw(
            SimpleNamespace(
                scene=SimpleNamespace(o_camera_bookmarks=[]),
            )
        )

        self.assertEqual(
            layout.operator_calls,
            [
                (
                    "o.add_camera_bookmark",
                    "Add Bookmark",
                    "BOOKMARKS",
                ),
                (
                    "o.show_camera_bookmarks",
                    "No Bookmarks",
                    "BOOKMARKS",
                ),
            ],
        )

    def test_registers_and_removes_camera_bookmarks_shortcut(self):
        self.addon.register()
        keymaps = self.fake_bpy.context.window_manager.keyconfigs.addon.keymaps
        shortcut_items = [
            keymap_item
            for keymap in keymaps.items
            for keymap_item in keymap.keymap_items.items
            if keymap_item.idname == "wm.call_menu_pie"
        ]

        self.assertEqual(len(shortcut_items), 1)
        shortcut = shortcut_items[0]
        self.assertEqual(
            (shortcut.type, shortcut.value),
            ("ACCENT_GRAVE", "PRESS"),
        )
        self.assertTrue(shortcut.shift)
        self.assertEqual(
            shortcut.properties.name,
            "O_MT_camera_bookmarks_pie",
        )

        self.addon.unregister()
        self.assertNotIn(
            "wm.call_menu_pie",
            [
                item.idname
                for keymap in keymaps.items
                for item in keymap.keymap_items.items
            ],
        )

    def test_registers_and_removes_clipboard_image_shortcuts(self):
        self.addon.register()
        keymaps = self.fake_bpy.context.window_manager.keyconfigs.addon.keymaps

        clipboard_items = [
            keymap_item
            for keymap in keymaps.items
            for keymap_item in keymap.keymap_items.items
            if keymap_item.idname == "o.paste_clipboard_image"
        ]
        self.assertEqual(len(clipboard_items), 2)
        for keymap_item in clipboard_items:
            self.assertEqual(keymap_item.idname, "o.paste_clipboard_image")
            self.assertEqual((keymap_item.type, keymap_item.value), ("V", "PRESS"))
            modifier_name = "oskey" if sys.platform == "darwin" else "ctrl"
            self.assertTrue(getattr(keymap_item, modifier_name))

        self.addon.unregister()
        for keymap in keymaps.items:
            self.assertEqual(keymap.keymap_items.items, [])

    @staticmethod
    def create_fake_bpy():
        fake_bpy = ModuleType("bpy")
        fake_bpy.app = SimpleNamespace(version=(5, 1, 0))
        fake_bpy.utils = FakeUtils()
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
            Menu=FakeBpyMenu,
            Operator=FakeOperator,
            Panel=FakePanel,
            PropertyGroup=FakePropertyGroup,
            Scene=FakeScene,
            TOPBAR_MT_file_defaults=FakeMenu,
            VIEW3D_MT_view_pie=FakeViewPie,
            VIEW3D_MT_object_context_menu=FakeObjectContextMenu,
        )
        fake_bpy.context = SimpleNamespace(
            window_manager=SimpleNamespace(
                keyconfigs=SimpleNamespace(
                    active=SimpleNamespace(name="Blender"),
                    addon=SimpleNamespace(keymaps=FakeKeyMaps()),
                ),
            ),
        )
        return fake_bpy

    @staticmethod
    def remove_startup_modules():
        for module_name in tuple(sys.modules):
            if module_name == "startup" or module_name.startswith("startup."):
                sys.modules.pop(module_name)


class FakeLayout:
    def __init__(self):
        self.actions = []
        self.separator_called = False
        self.operator_id = None
        self.operator_text = None
        self.operator_properties = SimpleNamespace()
        self.operator_calls = []
        self.icon_view_calls = []
        self.template_icon_calls = []
        self.properties = []

    def separator(self):
        self.actions.append("separator")
        self.separator_called = True

    def operator(self, operator_id, text, icon=None, **_options):
        self.actions.append("operator")
        self.operator_id = operator_id
        self.operator_text = text
        self.operator_icon = icon
        self.operator_calls.append((operator_id, text, icon))
        return self.operator_properties

    def menu_pie(self):
        return self

    def column(self, **_options):
        return self

    def label(self, **_options):
        return None

    def template_icon_view(
        self,
        data,
        property_name,
        *,
        show_labels,
        scale,
        scale_popup,
    ):
        self.icon_view_calls.append(
            (
                data,
                property_name,
                show_labels,
                scale,
                scale_popup,
            )
        )

    def template_icon(self, *, icon_value, scale):
        self.template_icon_calls.append((icon_value, scale))

    def prop(self, data, property_name):
        self.properties.append((data, property_name))


if __name__ == "__main__":
    unittest.main()
