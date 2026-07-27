import importlib
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


class AddonRegistrationTest(unittest.TestCase):
    def setUp(self):
        FakeMenu.callbacks = []
        FakeMenu.registration_method = None
        self.scripts_directory = tempfile.TemporaryDirectory()
        self.fake_bpy = self.create_fake_bpy("Blender")
        self.fake_bpy.utils.scripts_directory = Path(self.scripts_directory.name)
        sys.modules["bpy"] = self.fake_bpy

        import startup

        self.addon = importlib.reload(startup)

    def tearDown(self):
        if self.addon._menu_registered:
            self.addon.unregister()
        sys.modules.pop("bpy", None)
        self.scripts_directory.cleanup()

    def test_registers_menu_and_installs_compatible_preset(self):
        self.addon.register()

        self.assertEqual(len(FakeMenu.callbacks), 1)
        self.assertEqual(FakeMenu.registration_method, "prepend")
        self.assertEqual(len(self.fake_bpy.utils.registered_classes), 1)
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
        self.assertEqual(layout.operator_id, "startup.use_omoolab_startup")
        self.assertEqual(layout.operator_text, "Use OmooLab Startup")
        self.assertEqual(layout.actions, ["operator", "separator"])

    def test_startup_replacement_confirmation_warns_about_overwrite(self):
        confirmation = {}

        def invoke_confirm(operator, event, **options):
            confirmation.update(options)
            return {"RUNNING_MODAL"}

        context = SimpleNamespace(
            window_manager=SimpleNamespace(invoke_confirm=invoke_confirm),
        )
        operator = self.addon.STARTUP_OT_use_omoolab_startup()

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

            operator = self.addon.STARTUP_OT_use_omoolab_startup()
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
        fake_bpy.types = SimpleNamespace(
            Operator=FakeOperator,
            TOPBAR_MT_file_defaults=FakeMenu,
        )
        fake_bpy.context = SimpleNamespace(
            preferences=SimpleNamespace(
                keymap=SimpleNamespace(active_keyconfig=active_keyconfig),
            ),
            window_manager=SimpleNamespace(
                keyconfigs=SimpleNamespace(
                    active=SimpleNamespace(name="Blender"),
                ),
            ),
        )
        return fake_bpy


class FakeLayout:
    def __init__(self):
        self.actions = []
        self.separator_called = False
        self.operator_id = None
        self.operator_text = None
        self.operator_properties = SimpleNamespace()

    def separator(self):
        self.actions.append("separator")
        self.separator_called = True

    def operator(self, operator_id, text):
        self.actions.append("operator")
        self.operator_id = operator_id
        self.operator_text = text
        return self.operator_properties


if __name__ == "__main__":
    unittest.main()
