"""Pack Blender Startup application templates into installable archives."""

import argparse
import os
import tempfile
import tomllib
import zipfile
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = PROJECT_ROOT / "src" / "startup"
TEMPLATE_ROOT = PROJECT_ROOT / "template"
DEFAULT_OUTPUT_DIRECTORY = PROJECT_ROOT / "dist"

APP_TEMPLATE_ID = "Omoo_Lab"
SPLASH_NAME = "splash.png"
STARTUP_PREFIX = "startup."
STARTUP_SUFFIX = ".blend"
USERPREF_PREFIX = "userpref."
USERPREF_SUFFIX = ".blend"
KEYCONFIG_ARCHIVE_NAME = "keyconfig.py"
KEYCONFIG_PREFIX = "keyconfig."
KEYCONFIG_SUFFIX = ".py"


@dataclass(frozen=True)
class TargetBundle:
    version: tuple[int, int]
    root: Path
    startup_file: Path
    userpref_file: Path
    keyconfig_file: Path
    splash_file: Path


def parse_target_version(directory_name):
    if len(directory_name) != 3 or not directory_name.startswith("b"):
        return None
    version_text = directory_name[1:]
    if not version_text.isdigit():
        return None
    return int(version_text[0]), int(version_text[1])


def target_id_from_filename(filename, prefix, suffix):
    if not filename.startswith(prefix) or not filename.endswith(suffix):
        return None
    target_id = filename[len(prefix):-len(suffix)]
    if parse_target_version(target_id) is None:
        return None
    return target_id


def find_target_ids(template_root):
    target_ids = set()
    for template_file in Path(template_root).iterdir():
        if not template_file.is_file():
            continue
        for prefix, suffix in (
            (STARTUP_PREFIX, STARTUP_SUFFIX),
            (USERPREF_PREFIX, USERPREF_SUFFIX),
            (KEYCONFIG_PREFIX, KEYCONFIG_SUFFIX),
        ):
            target_id = target_id_from_filename(
                template_file.name,
                prefix,
                suffix,
            )
            if target_id is not None:
                target_ids.add(target_id)
    return sorted(target_ids, key=parse_target_version)


def find_target_bundles(template_root=TEMPLATE_ROOT):
    template_root = Path(template_root)
    if not template_root.is_dir():
        raise RuntimeError("Template source directory was not found")

    bundles = []
    for target_id in find_target_ids(template_root):
        bundle = TargetBundle(
            version=parse_target_version(target_id),
            root=template_root,
            startup_file=(
                template_root
                / f"{STARTUP_PREFIX}{target_id}{STARTUP_SUFFIX}"
            ),
            userpref_file=(
                template_root
                / f"{USERPREF_PREFIX}{target_id}{USERPREF_SUFFIX}"
            ),
            keyconfig_file=(
                template_root
                / f"{KEYCONFIG_PREFIX}{target_id}{KEYCONFIG_SUFFIX}"
            ),
            splash_file=template_root / SPLASH_NAME,
        )
        validate_target_bundle(bundle)
        bundles.append(bundle)

    if not bundles:
        raise RuntimeError("No versioned template targets were found")
    return sorted(bundles, key=lambda bundle: bundle.version)


def validate_target_bundle(bundle):
    missing_files = [
        path
        for path in (
            bundle.startup_file,
            bundle.userpref_file,
            bundle.keyconfig_file,
            bundle.splash_file,
        )
        if not path.is_file()
    ]
    if not missing_files:
        return

    missing_text = ", ".join(str(path) for path in missing_files)
    raise RuntimeError(f"Target bundle is incomplete: {missing_text}")


def target_id(bundle):
    return f"b{bundle.version[0]}{bundle.version[1]}"


def include_common_source(relative_path):
    if any(part == "__pycache__" for part in relative_path.parts):
        return False
    if any(part.startswith(".") for part in relative_path.parts):
        return False
    return relative_path.suffix == ".py"


def collect_common_sources():
    files = []
    for source_file in SOURCE_ROOT.rglob("*"):
        if not source_file.is_file():
            continue
        relative_path = source_file.relative_to(SOURCE_ROOT)
        if include_common_source(relative_path):
            files.append((source_file, relative_path))
    return sorted(files, key=lambda item: item[1].as_posix())


def read_project_version():
    project_file = PROJECT_ROOT / "pyproject.toml"
    project = tomllib.loads(project_file.read_text(encoding="utf-8"))
    return project["project"]["version"]


def archive_name(bundle):
    project_version = read_project_version()
    return f"Startup.v{project_version}.{target_id(bundle)}.zip"


def build_template(bundle, output_directory=DEFAULT_OUTPUT_DIRECTORY):
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    archive_file = output_directory / archive_name(bundle)

    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=f"{archive_file.name}-",
        suffix=".tmp",
        dir=output_directory,
    )
    os.close(file_descriptor)
    temporary_file = Path(temporary_name)

    try:
        write_archive(temporary_file, bundle)
        validate_archive(temporary_file)
        os.replace(temporary_file, archive_file)
    except (OSError, RuntimeError, zipfile.BadZipFile):
        temporary_file.unlink(missing_ok=True)
        raise

    return archive_file


def select_bundles(target_ids=None):
    bundles = find_target_bundles()
    if target_ids is None:
        return bundles

    selected = [bundle for bundle in bundles if target_id(bundle) in target_ids]
    missing = sorted(set(target_ids) - {target_id(bundle) for bundle in selected})
    if missing:
        raise RuntimeError(f"Unknown build targets: {', '.join(missing)}")
    return selected


def build_templates(output_directory=DEFAULT_OUTPUT_DIRECTORY, target_ids=None):
    return [
        build_template(bundle, output_directory)
        for bundle in select_bundles(target_ids)
    ]


def write_archive(archive_file, bundle):
    root = Path(APP_TEMPLATE_ID)
    with zipfile.ZipFile(
        archive_file,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as template_archive:
        # Blender 通过根目录条目识别并替换已安装的同 ID 模板。
        template_archive.writestr(f"{APP_TEMPLATE_ID}/", b"")
        for source_file, relative_path in collect_common_sources():
            template_archive.write(
                source_file,
                (root / relative_path).as_posix(),
            )
        template_archive.write(
            bundle.startup_file,
            (root / "startup.blend").as_posix(),
        )
        template_archive.write(
            bundle.userpref_file,
            (root / "userpref.blend").as_posix(),
        )
        template_archive.write(
            bundle.keyconfig_file,
            (root / KEYCONFIG_ARCHIVE_NAME).as_posix(),
        )
        template_archive.write(
            bundle.splash_file,
            (root / SPLASH_NAME).as_posix(),
        )


def validate_archive(archive_file):
    root = Path(APP_TEMPLATE_ID)
    required_entries = {
        f"{APP_TEMPLATE_ID}/",
        (root / "__init__.py").as_posix(),
        (root / "startup.blend").as_posix(),
        (root / "userpref.blend").as_posix(),
        (root / SPLASH_NAME).as_posix(),
        (root / KEYCONFIG_ARCHIVE_NAME).as_posix(),
    }

    with zipfile.ZipFile(archive_file, mode="r") as template_archive:
        archive_entries = set(template_archive.namelist())
        corrupt_entry = template_archive.testzip()

    missing_entries = required_entries - archive_entries
    if missing_entries:
        missing_text = ", ".join(sorted(missing_entries))
        raise RuntimeError(f"Archive is missing required entries: {missing_text}")
    if any("\\" in entry for entry in archive_entries):
        raise RuntimeError("Archive contains non-portable backslash paths")
    if any(
        not entry.startswith(f"{APP_TEMPLATE_ID}/")
        for entry in archive_entries
    ):
        raise RuntimeError("Archive contains files outside the template directory")
    if corrupt_entry is not None:
        raise RuntimeError(f"Archive contains a corrupt entry: {corrupt_entry}")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Pack Blender Startup application templates.",
    )
    parser.add_argument(
        "-t",
        "--target",
        action="append",
        choices=find_target_ids(TEMPLATE_ROOT),
        help="Pack one build target; repeat for several, defaults to all",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIRECTORY,
        help="Output directory, defaults to dist/",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    for archive_file in build_templates(args.output, args.target):
        archive_size = archive_file.stat().st_size
        print(f"Packed {archive_file} ({archive_size} bytes)")


if __name__ == "__main__":
    main()
