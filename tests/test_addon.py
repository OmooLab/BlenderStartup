import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace


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
        self.config_directory = None
        self.keyconfig_files = []
        self.registered_classes = []
        self.scripts_directory = None

    def keyconfig_set(self, filepath):
        self.keyconfig_files.append(filepath)
        return True

    def register_class(self, operator_class):
        self.registered_classes.append(operator_class)

    def unregister_class(self, operator_class):
        self.registered_classes.remove(operator_class)

    def user_resource(self, resource_type, path="", create=False):
        base_directory = None
        if resource_type == "CONFIG":
            base_directory = self.config_directory
        if resource_type == "SCRIPTS":
            base_directory = self.scripts_directory
        if base_directory is None:
            return ""

        resource_path = Path(base_directory) / path
        if create:
            resource_path.mkdir(parents=True, exist_ok=True)
        return str(resource_path)


class FakeOperator:
    def __init__(self):
        self.reports = []

    def report(self, levels, message):
        self.reports.append((levels, message))


class FakeAddonPreferences:
    pass


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


class AddonRegistrationTest(unittest.TestCase):
    def setUp(self):
        FakeMenu.callbacks = []
        FakeMenu.registration_method = None
        FakeObjectContextMenu.callbacks = []
        FakeObjectContextMenu.registration_method = None
        FakeViewPie.callbacks = []
        FakeViewPie.registration_method = None
        self.scripts_directory = tempfile.TemporaryDirectory()
        self.fake_bpy = self.create_fake_bpy("Blender")
        self.fake_bpy.utils.scripts_directory = Path(self.scripts_directory.name)
        sys.modules["bpy"] = self.fake_bpy
        self.remove_startup_modules()

        import startup

        self.addon = startup

    def tearDown(self):
        if self.addon._menu_registered:
            self.addon.unregister()
        sys.modules.pop("bpy", None)
        self.remove_startup_modules()
        self.scripts_directory.cleanup()

    def test_registers_menu_and_installs_compatible_preset(self):
        self.addon.register()

        self.assertEqual(len(FakeMenu.callbacks), 1)
        self.assertEqual(FakeMenu.registration_method, "prepend")
        self.assertEqual(len(self.fake_bpy.utils.registered_classes), 12)
        self.assertEqual(len(FakeObjectContextMenu.callbacks), 1)
        self.assertEqual(FakeObjectContextMenu.registration_method, "prepend")
        context_layout = FakeLayout()
        FakeObjectContextMenu.callbacks[0](
            SimpleNamespace(layout=context_layout),
            None,
        )
        self.assertEqual(context_layout.operator_id, "o.toggle_phantom")
        self.assertEqual(context_layout.operator_text, "Toggle Phantom")
        self.assertTrue(context_layout.separator_called)
        self.assertEqual(context_layout.actions, ["operator", "separator"])
        self.assertEqual(FakeViewPie.callbacks, [])
        installed_file = (
            Path(self.scripts_directory.name)
            / "presets"
            / "keyconfig"
            / "Refined Industry Compatible.py"
        )
        self.assertEqual(
            installed_file.read_bytes(),
            self.addon._resource_bundle.keyconfig_file.read_bytes(),
        )
        self.assertEqual(self.fake_bpy.utils.keyconfig_files, [])

        self.addon.unregister()
        self.assertTrue(installed_file.is_file())
        self.assertEqual(FakeObjectContextMenu.callbacks, [])
        self.assertEqual(FakeViewPie.callbacks, [])

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
            identifier="bookmark-1",
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

    @unittest.skipUnless(sys.platform == "win32", "Windows clipboard shortcut")
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
            self.assertTrue(keymap_item.ctrl)

        self.addon.unregister()
        for keymap in keymaps.items:
            self.assertEqual(keymap.keymap_items.items, [])

    def test_restores_only_previously_selected_keyconfig(self):
        self.fake_bpy.context.preferences.keymap.active_keyconfig = (
            "Refined Industry Compatible"
        )

        self.addon.register()

        self.assertEqual(len(self.fake_bpy.utils.keyconfig_files), 1)
        self.assertTrue(
            self.fake_bpy.utils.keyconfig_files[0].endswith(
                "Refined Industry Compatible.py"
            )
        )

    def test_updates_outdated_keyconfig_preset(self):
        installed_file = (
            Path(self.scripts_directory.name)
            / "presets"
            / "keyconfig"
            / "Refined Industry Compatible.py"
        )
        installed_file.parent.mkdir(parents=True)
        installed_file.write_text("outdated preset", encoding="utf-8")

        self.addon.register()

        self.assertEqual(
            installed_file.read_bytes(),
            self.addon._resource_bundle.keyconfig_file.read_bytes(),
        )

    def test_draws_startup_replacement_operator(self):
        self.addon.register()
        layout = FakeLayout()

        self.addon.draw_file_defaults(SimpleNamespace(layout=layout), None)

        self.assertTrue(layout.separator_called)
        self.assertEqual(layout.operator_id, "o.use_startup")
        self.assertEqual(layout.operator_text, "Use OmooLab Startup")
        self.assertEqual(layout.actions, ["operator", "separator"])

    def test_clipboard_image_preference_is_enabled_by_default(self):
        preference_definition = (
            self.addon.O_Preferences.__annotations__[
                "enable_clipboard_image"
            ]
        )

        self.assertTrue(preference_definition["default"])

    def test_phantom_preference_is_enabled_by_default(self):
        preference_definition = (
            self.addon.O_Preferences.__annotations__["enable_phantom"]
        )

        self.assertTrue(preference_definition["default"])

    def test_camera_bookmarks_preference_is_enabled_by_default(self):
        preference_definition = (
            self.addon.O_Preferences.__annotations__[
                "enable_camera_bookmarks"
            ]
        )

        self.assertTrue(preference_definition["default"])

    def test_draws_feature_preferences(self):
        preferences = self.addon.O_Preferences()
        preferences.layout = FakeLayout()

        preferences.draw(None)

        self.assertEqual(
            preferences.layout.properties,
            [
                (preferences, "enable_clipboard_image"),
                (preferences, "enable_phantom"),
                (preferences, "enable_camera_bookmarks"),
            ],
        )

    def test_startup_replacement_confirmation_warns_about_overwrite(self):
        confirmation = {}

        def invoke_confirm(operator, event, **options):
            confirmation.update(options)
            return {"RUNNING_MODAL"}

        context = SimpleNamespace(
            window_manager=SimpleNamespace(invoke_confirm=invoke_confirm),
        )
        operator = self.addon.O_OT_use_startup()

        result = operator.invoke(context, object())

        self.assertEqual(result, {"RUNNING_MODAL"})
        self.assertEqual(confirmation["title"], "Use OmooLab Startup")
        self.assertIn("overwrite", confirmation["message"])
        self.assertIn("config/startup.blend", confirmation["message"])
        self.assertEqual(confirmation["confirm_text"], "Overwrite Startup")

    def test_replaces_user_startup_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config_directory = Path(temporary_directory)
            target_file = config_directory / "startup.blend"
            target_file.write_bytes(b"previous startup")
            self.fake_bpy.utils.config_directory = config_directory
            self.addon.register()
            expected_content = self.addon._resource_bundle.startup_file.read_bytes()

            operator = self.addon.O_OT_use_startup()
            result = operator.execute(None)

            self.assertEqual(result, {"FINISHED"})
            self.assertEqual(target_file.read_bytes(), expected_content)
            self.assertEqual(
                [path.name for path in config_directory.iterdir()],
                ["startup.blend"],
            )

    @staticmethod
    def create_fake_bpy(active_keyconfig):
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
            AddonPreferences=FakeAddonPreferences,
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
            preferences=SimpleNamespace(
                keymap=SimpleNamespace(active_keyconfig=active_keyconfig),
            ),
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
