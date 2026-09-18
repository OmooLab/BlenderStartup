import re
import tomllib
import unittest
from pathlib import Path

from tools.docs import documentation_command
from tools.docs import documentation_version


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MKDOCS_FILE = PROJECT_ROOT / "mkdocs.yml"
DOCS_ROOT = PROJECT_ROOT / "docs"
VERSION_LITERAL_PATTERN = re.compile(r"\bv?\d+\.\d+\.\d+\b")
LEGACY_TEMPLATE_NAME_PATTERN = re.compile(r"O General|O_General")
HTML_TAG_PATTERN = re.compile(r"</?[A-Za-z][^>]*>")
FENCED_CODE_PATTERN = re.compile(r"^(`{3,}|~{3,}).*?^\1", re.MULTILINE | re.DOTALL)
CODE_SPAN_PATTERN = re.compile(r"`[^`\n]*`")


def markdown_body(content):
    """剔除代码块与行内代码，只保留正文，代码里的尖括号不会被当成 HTML。"""
    return CODE_SPAN_PATTERN.sub("", FENCED_CODE_PATTERN.sub("", content))


def document_body(document):
    return markdown_body(document.read_text(encoding="utf-8"))


def project_config():
    return tomllib.loads(
        (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    )


class DocsTest(unittest.TestCase):
    def test_documents_do_not_contain_html(self):
        documents = [PROJECT_ROOT / "README.md", *sorted(DOCS_ROOT.rglob("*.md"))]

        for document in documents:
            with self.subTest(document=document.relative_to(PROJECT_ROOT)):
                self.assertIsNone(HTML_TAG_PATTERN.search(document_body(document)))

    def test_code_is_not_treated_as_html(self):
        self.assertIsNone(
            HTML_TAG_PATTERN.search(markdown_body("`BlenderStartup.v<版本号>.b45.zip`"))
        )
        self.assertIsNotNone(
            HTML_TAG_PATTERN.search(markdown_body("正文里直接写 <div> 标签"))
        )

    def test_documents_do_not_use_the_legacy_template_name(self):
        documents = [PROJECT_ROOT / "README.md", *sorted(DOCS_ROOT.rglob("*.md"))]

        for document in documents:
            with self.subTest(document=document.relative_to(PROJECT_ROOT)):
                content = document.read_text(encoding="utf-8")
                self.assertIsNone(LEGACY_TEMPLATE_NAME_PATTERN.search(content))

    def test_documents_do_not_pin_concrete_versions(self):
        documents = [PROJECT_ROOT / "README.md", *sorted(DOCS_ROOT.rglob("*.md"))]

        for document in documents:
            with self.subTest(document=document.relative_to(PROJECT_ROOT)):
                content = document.read_text(encoding="utf-8")
                self.assertIsNone(VERSION_LITERAL_PATTERN.search(content))

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


class DocumentationCommandTest(unittest.TestCase):
    def test_documentation_version_omits_the_patch(self):
        project_version = project_config()["project"]["version"]
        major_minor = ".".join(project_version.split(".")[:2])

        self.assertEqual(
            documentation_version(),
            f"{major_minor}.x",
        )

    def test_build_writes_the_multi_version_site_locally(self):
        version = documentation_version()

        self.assertEqual(
            documentation_command("build"),
            ("mike", "deploy", "--update-aliases", version, "latest"),
        )
        self.assertNotIn("--push", documentation_command("build"))

    def test_dev_serves_the_current_documentation_with_hot_reload(self):
        self.assertEqual(
            documentation_command("dev"),
            ("mkdocs", "serve"),
        )

    def test_deploy_publishes_the_project_version_as_latest(self):
        version = documentation_version()

        self.assertEqual(
            documentation_command("deploy"),
            (
                "mike",
                "deploy",
                "--update-aliases",
                "--push",
                "--allow-empty",
                version,
                "latest",
            ),
        )

    def test_project_exposes_the_pack_and_docs_commands(self):
        self.assertEqual(
            project_config()["project"]["scripts"],
            {
                "pack": "tools.pack:main",
                "docs": "tools.docs:main",
            },
        )


if __name__ == "__main__":
    unittest.main()
