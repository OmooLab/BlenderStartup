import tempfile
import unittest
import zipfile
from pathlib import Path

from pack import build_extension


class PackTest(unittest.TestCase):
    def test_builds_installable_extension_layout(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive_file = build_extension(temporary_directory)

            self.assertEqual(archive_file.name, "startup-0.2.19.zip")
            with zipfile.ZipFile(archive_file, mode="r") as extension_archive:
                entries = set(extension_archive.namelist())

            self.assertIn("__init__.py", entries)
            self.assertIn("blender_manifest.toml", entries)
            self.assertIn("camera_bookmarks.py", entries)
            self.assertIn("clipboard_image/__init__.py", entries)
            self.assertIn("clipboard_image/actions.py", entries)
            self.assertIn("clipboard_image/clipboard.py", entries)
            self.assertIn("phantom.py", entries)
            self.assertIn("resources/4.5/config/startup.blend", entries)
            self.assertIn("resources/5.2/config/startup.blend", entries)
            self.assertNotIn("addon.py", entries)
            self.assertFalse(any("\\" in entry for entry in entries))


if __name__ == "__main__":
    unittest.main()
