import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

if "bpy" not in sys.modules:
    fake_bpy = ModuleType("bpy")
    fake_bpy.types = SimpleNamespace(Operator=object)
    sys.modules["bpy"] = fake_bpy

from startup.resource_loader import KEYCONFIG_RELATIVE_PATH  # noqa: E402
from startup.resource_loader import STARTUP_RELATIVE_PATH  # noqa: E402
from startup.resource_loader import find_resource_bundle  # noqa: E402
from startup.resource_loader import parse_resource_version  # noqa: E402


class ResourceVersionTest(unittest.TestCase):
    def test_parse_resource_version(self):
        self.assertEqual(parse_resource_version("4.5"), (4, 5))
        self.assertEqual(parse_resource_version("5.2"), (5, 2))
        self.assertIsNone(parse_resource_version("5"))
        self.assertIsNone(parse_resource_version("5.2.1"))
        self.assertIsNone(parse_resource_version("current"))

    def test_selects_highest_compatible_version(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            resources_root = Path(temporary_directory)
            self.create_bundle(resources_root, "4.5")
            self.create_bundle(resources_root, "5.2")

            expected_versions = {
                (4, 5): (4, 5),
                (4, 6): (4, 5),
                (5, 0): (4, 5),
                (5, 1): (4, 5),
                (5, 2): (5, 2),
                (5, 3): (5, 2),
                (6, 0): (5, 2),
            }

            for blender_version, expected_version in expected_versions.items():
                with self.subTest(blender_version=blender_version):
                    bundle = find_resource_bundle(
                        resources_root,
                        blender_version,
                    )
                    self.assertEqual(bundle.version, expected_version)

    def test_rejects_unsupported_version(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            resources_root = Path(temporary_directory)
            self.create_bundle(resources_root, "4.5")

            with self.assertRaisesRegex(RuntimeError, "No compatible resources"):
                find_resource_bundle(resources_root, (4, 4))

    def test_rejects_incomplete_bundle(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            resources_root = Path(temporary_directory)
            bundle_root = resources_root / "4.5"
            (bundle_root / STARTUP_RELATIVE_PATH).parent.mkdir(parents=True)
            (bundle_root / STARTUP_RELATIVE_PATH).touch()

            with self.assertRaisesRegex(RuntimeError, "incomplete"):
                find_resource_bundle(resources_root, (4, 5))

    @staticmethod
    def create_bundle(resources_root, version):
        bundle_root = resources_root / version
        startup_file = bundle_root / STARTUP_RELATIVE_PATH
        keyconfig_file = bundle_root / KEYCONFIG_RELATIVE_PATH
        startup_file.parent.mkdir(parents=True)
        keyconfig_file.parent.mkdir(parents=True)
        startup_file.touch()
        keyconfig_file.touch()


if __name__ == "__main__":
    unittest.main()
