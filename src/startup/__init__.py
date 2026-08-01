import filecmp
import os
import shutil
import tempfile
from pathlib import Path

import bpy

from . import camera_bookmark, clipboard_image, toggle_phantom


KEYCONFIG_NAME = "Refined Industry Compatible"
KEYCONFIG_FILE = Path(__file__).with_name("keyconfig.py")
KEYCONFIG_PRESET_FILE = "Refined_Industry_Compatible.py"

_registered = False


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
    clipboard_image.register()
    toggle_phantom.register()
    camera_bookmark.register()
    _registered = True


def unregister():
    global _registered

    if not _registered:
        return

    camera_bookmark.unregister()
    toggle_phantom.unregister()
    clipboard_image.unregister()
    _registered = False
