import os
import tempfile
import tomllib
import zipfile
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = PROJECT_ROOT / "src" / "startup"
DEFAULT_OUTPUT_DIRECTORY = PROJECT_ROOT / "dist"


def include_in_archive(relative_path):
    if any(part == "__pycache__" for part in relative_path.parts):
        return False
    if any(part.startswith(".") for part in relative_path.parts):
        return False
    return relative_path.suffix not in {".pyc", ".zip"}


def collect_source_files():
    files = []
    for source_file in SOURCE_ROOT.rglob("*"):
        if not source_file.is_file():
            continue
        relative_path = source_file.relative_to(SOURCE_ROOT)
        if include_in_archive(relative_path):
            files.append((source_file, relative_path))
    return sorted(files, key=lambda item: item[1].as_posix())


def read_manifest():
    manifest_file = SOURCE_ROOT / "blender_manifest.toml"
    return tomllib.loads(manifest_file.read_text(encoding="utf-8"))


def build_extension(output_directory=DEFAULT_OUTPUT_DIRECTORY):
    manifest = read_manifest()
    archive_name = f"{manifest['id']}-{manifest['version']}.zip"
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    archive_file = output_directory / archive_name

    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=f"{archive_name}-",
        suffix=".tmp",
        dir=output_directory,
    )
    os.close(file_descriptor)
    temporary_file = Path(temporary_name)

    try:
        write_archive(temporary_file)
        validate_archive(temporary_file)
        os.replace(temporary_file, archive_file)
    except (OSError, RuntimeError, zipfile.BadZipFile):
        temporary_file.unlink(missing_ok=True)
        raise

    return archive_file


def write_archive(archive_file):
    with zipfile.ZipFile(
        archive_file,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as extension_archive:
        for source_file, relative_path in collect_source_files():
            extension_archive.write(source_file, relative_path.as_posix())


def validate_archive(archive_file):
    required_entries = {
        "__init__.py",
        "blender_manifest.toml",
    }

    with zipfile.ZipFile(archive_file, mode="r") as extension_archive:
        archive_entries = set(extension_archive.namelist())
        corrupt_entry = extension_archive.testzip()

    missing_entries = required_entries - archive_entries
    if missing_entries:
        missing_text = ", ".join(sorted(missing_entries))
        raise RuntimeError(f"Archive is missing required entries: {missing_text}")
    if any("\\" in entry for entry in archive_entries):
        raise RuntimeError("Archive contains non-portable backslash paths")
    if corrupt_entry is not None:
        raise RuntimeError(f"Archive contains a corrupt entry: {corrupt_entry}")


def main():
    archive_file = build_extension()
    archive_size = archive_file.stat().st_size
    print(f"Packed {archive_file} ({archive_size} bytes)")


if __name__ == "__main__":
    main()
