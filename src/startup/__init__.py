import filecmp
import importlib
import os
import shutil
import tempfile
from pathlib import Path

import bpy


KEYCONFIG_NAME = "Refined Industry Compatible"
KEYCONFIG_FILE = Path(__file__).with_name("keyconfig.py")
KEYCONFIG_PRESET_FILE = "Refined_Industry_Compatible.py"
TEMPLATE_DIRECTORY = Path(__file__).parent
FEATURE_MODULE_NAMES = (
    "extension_repo",
    "remote_asset_library",
    "clipboard_image",
    "toggle_phantom",
    "camera_bookmark",
)

_registered = False
_registered_modules = []


def load_feature_modules(module_names=FEATURE_MODULE_NAMES):
    modules = []
    for module_name in module_names:
        module_file = TEMPLATE_DIRECTORY / module_name / "__init__.py"
        if not module_file.is_file():
            continue
        modules.append(importlib.import_module(f".{module_name}", __package__))
    return tuple(modules)


_feature_modules = load_feature_modules()


def copy_file_atomically(source_file, target_file):
    target_file = Path(target_file)
    file_descriptor, temporary_name = tempfile.mkstemp(
        prefix=f"{target_file.name}-",
        suffix=".tmp",
        dir=target_file.parent,
    )
    os.close(file_descriptor)
    temporary_file = Path(temporary_name)

    try:
        shutil.copyfile(source_file, temporary_file)
        os.replace(temporary_file, target_file)
    except OSError:
        temporary_file.unlink(missing_ok=True)
        raise

    return target_file


def install_keyconfig_preset(source_file=None):
    if source_file is None:
        source_file = KEYCONFIG_FILE

    preset_directory = bpy.utils.user_resource(
        "SCRIPTS",
        path=str(Path("presets") / "keyconfig"),
        create=True,
    )
    if not preset_directory:
        raise RuntimeError("Blender user scripts directory is unavailable")

    target_file = Path(preset_directory) / KEYCONFIG_PRESET_FILE
    if target_file.is_file() and filecmp.cmp(
        source_file,
        target_file,
        shallow=False,
    ):
        return target_file

    return copy_file_atomically(source_file, target_file)


def register():
    global _registered

    if _registered:
        return

    install_keyconfig_preset()
    for feature_module in _feature_modules:
        feature_module.register()
        _registered_modules.append(feature_module)
    _registered = True


def unregister():
    global _registered

    if not _registered:
        return

    for feature_module in reversed(_registered_modules):
        feature_module.unregister()
    _registered_modules.clear()
    _registered = False
