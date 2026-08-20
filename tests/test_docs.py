import tomllib
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MKDOCS_FILE = PROJECT_ROOT / "mkdocs.yml"
DOCS_ROOT = PROJECT_ROOT / "docs"


class DocsTest(unittest.TestCase):
    def test_documented_version_matches_project(self):
        project = tomllib.loads(
            (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )
        version = project["project"]["version"]

        self.assertIn(
            f"Startup.v{version}.b45.zip",
            (DOCS_ROOT / "getting-started" / "install.md").read_text(
                encoding="utf-8"
            ),
        )
        self.assertIn(
            f"Startup.v{version}.b52.zip",
            (DOCS_ROOT / "getting-started" / "install.md").read_text(
                encoding="utf-8"
            ),
        )
        self.assertIn(
            f"Startup.v{version}.b45.zip",
            (PROJECT_ROOT / "README.md").read_text(encoding="utf-8"),
        )

    def test_navigation_references_existing_markdown_files(self):
        config = MKDOCS_FILE.read_text(encoding="utf-8")
        referenced_files = []
        for line in config.splitlines():
            value = line.rsplit(":", 1)[-1].strip()
            if value.endswith(".md"):
                referenced_files.append(value)

        self.assertTrue(referenced_files)
        for relative_path in referenced_files:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((DOCS_ROOT / relative_path).is_file())

    def test_keymap_references_use_blender_default_baseline(self):
        for target_id in ("b45", "b52"):
            with self.subTest(target_id=target_id):
                content = (
                    DOCS_ROOT / "reference" / f"keymap-{target_id}.md"
                ).read_text(encoding="utf-8")
                self.assertIn("**Blender Default**", content)
                self.assertIn("Industry Compatible 不是比较基线", content)
                self.assertIn("受影响 Keymap", content)


if __name__ == "__main__":
    unittest.main()
