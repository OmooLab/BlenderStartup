import tempfile
import unittest
import zipfile
from pathlib import Path

from pack import APP_TEMPLATE_ID
from pack import KEYCONFIG_ARCHIVE_NAME
from pack import TEMPLATE_ROOT
from pack import build_templates


class PackTest(unittest.TestCase):
    def test_builds_one_installable_template_per_target(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_files = build_templates(temporary_directory)

            self.assertEqual(
                [archive_file.name for archive_file in archive_files],
                [
                    "startup.v0.2.19.b45.zip",
                    "startup.v0.2.19.b52.zip",
                ],
            )
            for archive_file in archive_files:
                self.assert_template_layout(archive_file)

    def test_packages_the_matching_target_files(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_files = build_templates(temporary_directory)

            for archive_file in archive_files:
                target_id = archive_file.stem.rsplit(".", 1)[1]
                with zipfile.ZipFile(archive_file, mode="r") as archive:
                    startup_data = archive.read(
                        f"{APP_TEMPLATE_ID}/startup.blend"
                    )
                    userpref_data = archive.read(
                        f"{APP_TEMPLATE_ID}/userpref.blend"
                    )
                    keyconfig_data = archive.read(
                        f"{APP_TEMPLATE_ID}/{KEYCONFIG_ARCHIVE_NAME}"
                    )
                    splash_data = archive.read(
                        f"{APP_TEMPLATE_ID}/splash.png"
                    )

                self.assertEqual(
                    startup_data,
                    (TEMPLATE_ROOT / f"startup.{target_id}.blend").read_bytes(),
                )
                self.assertEqual(
                    userpref_data,
                    (TEMPLATE_ROOT / f"userpref.{target_id}.blend").read_bytes(),
                )
                self.assertEqual(
                    keyconfig_data,
                    (
                        TEMPLATE_ROOT
                        / f"keyconfig.{target_id}.py"
                    ).read_bytes(),
                )
                self.assertEqual(
                    splash_data,
                    (TEMPLATE_ROOT / "splash.png").read_bytes(),
                )

    def assert_template_layout(self, archive_file):
        with zipfile.ZipFile(archive_file, mode="r") as template_archive:
            entries = set(template_archive.namelist())

        root = f"{APP_TEMPLATE_ID}/"
        self.assertIn(root, entries)
        self.assertIn(f"{root}__init__.py", entries)
        self.assertIn(f"{root}startup.blend", entries)
        self.assertIn(f"{root}userpref.blend", entries)
        self.assertIn(f"{root}splash.png", entries)
        self.assertIn(f"{root}{KEYCONFIG_ARCHIVE_NAME}", entries)
        self.assertIn(f"{root}camera_bookmark/__init__.py", entries)
        self.assertIn(f"{root}camera_bookmark/layout.py", entries)
        self.assertIn(f"{root}camera_bookmark/preview.py", entries)
        self.assertIn(f"{root}camera_bookmark/state.py", entries)
        self.assertIn(f"{root}clipboard_image/__init__.py", entries)
        self.assertIn(f"{root}clipboard_image/actions.py", entries)
        self.assertIn(f"{root}clipboard_image/clipboard.py", entries)
        self.assertIn(f"{root}toggle_phantom/__init__.py", entries)
        self.assertFalse(any("targets/" in entry for entry in entries))
        self.assertFalse(any("blender_manifest.toml" in entry for entry in entries))
        self.assertFalse(any("\\" in entry for entry in entries))
        self.assertTrue(all(entry.startswith(root) for entry in entries))


if __name__ == "__main__":
    unittest.main()
