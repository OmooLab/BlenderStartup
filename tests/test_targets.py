import tempfile
import unittest
from pathlib import Path

from tools.pack import KEYCONFIG_PREFIX
from tools.pack import KEYCONFIG_SUFFIX
from tools.pack import SPLASH_NAME
from tools.pack import STARTUP_PREFIX
from tools.pack import STARTUP_SUFFIX
from tools.pack import USERPREF_PREFIX
from tools.pack import USERPREF_SUFFIX
from tools.pack import find_target_bundles
from tools.pack import parse_target_version
from tools.pack import target_id
from tools.pack import target_id_from_filename


class TargetVersionTest(unittest.TestCase):
    def test_parse_target_version(self):
        self.assertEqual(parse_target_version("b45"), (4, 5))
        self.assertEqual(parse_target_version("b52"), (5, 2))
        self.assertIsNone(parse_target_version("4.5"))
        self.assertIsNone(parse_target_version("b5"))
        self.assertIsNone(parse_target_version("current"))

    def test_extracts_target_id_from_flat_filename(self):
        self.assertEqual(
            target_id_from_filename(
                "startup.b45.blend",
                STARTUP_PREFIX,
                STARTUP_SUFFIX,
            ),
            "b45",
        )
        self.assertIsNone(
            target_id_from_filename(
                "startup.current.blend",
                STARTUP_PREFIX,
                STARTUP_SUFFIX,
            )
        )

    def test_finds_all_complete_bundles_in_version_order(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            template_root = Path(temporary_directory)
            self.create_bundle(template_root, "b52")
            self.create_bundle(template_root, "b45")

            bundles = find_target_bundles(template_root)

            self.assertEqual(
                [bundle.version for bundle in bundles],
                [(4, 5), (5, 2)],
            )
            self.assertEqual(
                [target_id(bundle) for bundle in bundles],
                ["b45", "b52"],
            )

    def test_rejects_incomplete_bundle(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            template_root = Path(temporary_directory)
            (template_root / "startup.b45.blend").touch()
            (template_root / SPLASH_NAME).touch()

            with self.assertRaisesRegex(RuntimeError, "incomplete"):
                find_target_bundles(template_root)

    def test_rejects_missing_versioned_targets(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            template_root = Path(temporary_directory)
            (template_root / SPLASH_NAME).touch()

            with self.assertRaisesRegex(RuntimeError, "No versioned"):
                find_target_bundles(template_root)

    @staticmethod
    def create_bundle(template_root, target_id):
        (template_root / f"startup.{target_id}.blend").touch()
        (
            template_root
            / f"{USERPREF_PREFIX}{target_id}{USERPREF_SUFFIX}"
        ).touch()
        (
            template_root
            / f"keyconfig.{target_id}.py"
        ).touch()
        (template_root / SPLASH_NAME).touch()


if __name__ == "__main__":
    unittest.main()
