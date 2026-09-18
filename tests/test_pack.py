import io
import tempfile
import unittest
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from tools.pack import APP_TEMPLATE_ID
from tools.pack import KEYCONFIG_ARCHIVE_NAME
from tools.pack import TEMPLATE_ROOT
from tools.pack import build_templates
from tools.pack import main
from tools.pack import read_project_version


class PackTest(unittest.TestCase):
    def test_uses_the_omoo_lab_template_id(self):
        self.assertEqual(APP_TEMPLATE_ID, "Omoo_Lab")

    def test_builds_one_installable_template_per_target(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_files = build_templates(temporary_directory)
            version = read_project_version()

            self.assertEqual(
                [archive_file.name for archive_file in archive_files],
                [
                    f"BlenderStartup.v{version}.b45.zip",
                    f"BlenderStartup.v{version}.b52.zip",
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

    def test_cli_packs_only_the_requested_target(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with redirect_stdout(io.StringIO()):
                main(["--target", "b45", "--output", temporary_directory])

            archive_files = sorted(Path(temporary_directory).glob("*.zip"))

        self.assertEqual(
            [archive_file.name for archive_file in archive_files],
            [f"BlenderStartup.v{read_project_version()}.b45.zip"],
        )

    def test_cli_rejects_an_unknown_target(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaises(SystemExit), redirect_stderr(io.StringIO()):
                main(["--target", "b99", "--output", temporary_directory])

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
        self.assertIn(f"{root}toggle_phantom/__init__.py", entries)
        self.assertFalse(any("targets/" in entry for entry in entries))
        self.assertFalse(any("blender_manifest.toml" in entry for entry in entries))
        self.assertFalse(any("\\" in entry for entry in entries))
        self.assertTrue(all(entry.startswith(root) for entry in entries))


if __name__ == "__main__":
    unittest.main()
