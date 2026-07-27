from dataclasses import dataclass
from pathlib import Path


KEYCONFIG_NAME = "Refined Industry Compatible"
STARTUP_RELATIVE_PATH = Path("config") / "startup.blend"
PRESET_ROOT_RELATIVE_PATH = Path("scripts")
KEYCONFIG_RELATIVE_PATH = (
    PRESET_ROOT_RELATIVE_PATH
    / "presets"
    / "keyconfig"
    / f"{KEYCONFIG_NAME}.py"
)


@dataclass(frozen=True)
class ResourceBundle:
    version: tuple[int, int]
    root: Path
    startup_file: Path
    keyconfig_file: Path


def parse_resource_version(directory_name):
    parts = directory_name.split(".")
    if len(parts) != 2:
        return None
    if not all(part.isdigit() for part in parts):
        return None
    return int(parts[0]), int(parts[1])


def find_resource_bundle(resources_root, blender_version):
    resources_root = Path(resources_root)
    current_version = tuple(blender_version[:2])
    candidates = []

    for directory in resources_root.iterdir():
        version = parse_resource_version(directory.name)
        if version is None or not directory.is_dir():
            continue
        if version <= current_version:
            candidates.append((version, directory))

    if not candidates:
        message = (
            f"No compatible resources for Blender "
            f"{current_version[0]}.{current_version[1]}"
        )
        raise RuntimeError(message)

    version, resource_root = max(candidates, key=lambda item: item[0])
    resource_bundle = ResourceBundle(
        version=version,
        root=resource_root,
        startup_file=resource_root / STARTUP_RELATIVE_PATH,
        keyconfig_file=resource_root / KEYCONFIG_RELATIVE_PATH,
    )
    validate_resource_bundle(resource_bundle)
    return resource_bundle


def validate_resource_bundle(resource_bundle):
    required_files = (
        resource_bundle.startup_file,
        resource_bundle.keyconfig_file,
    )
    missing_files = [path for path in required_files if not path.is_file()]
    if not missing_files:
        return

    missing_text = ", ".join(str(path) for path in missing_files)
    raise RuntimeError(f"Resource bundle is incomplete: {missing_text}")
