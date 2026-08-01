import filecmp
import os
import shutil
import tempfile
from pathlib import Path

import bpy

from . import camera_bookmarks, clipboard_image, phantom
from .resource_loader import KEYCONFIG_NAME, ResourceBundle, find_resource_bundle


DISPLAY_NAME = "OmooLab Startup"
RESOURCES_ROOT = Path(__file__).resolve().parent / "resources"

_resource_bundle: ResourceBundle | None = None
_menu_registered = False
_operator_registered = False
_preferences_registered = False


class O_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    enable_clipboard_image: bpy.props.BoolProperty(
        name="Paste Clipboard Images",
        description=(
            "Paste packed clipboard images as planes, image nodes, "
            "or active brush textures based on the current editor"
        ),
        default=True,
    )
    enable_phantom: bpy.props.BoolProperty(
        name="Toggle Phantom",
        description=(
            "Add Toggle Phantom to the 3D View object context menu"
        ),
        default=True,
    )
    enable_camera_bookmarks: bpy.props.BoolProperty(
        name="Bookmarks",
        description=(
            "Show bookmark controls in Camera View"
        ),
        default=True,
    )

    def draw(self, _context):
        self.layout.prop(self, "enable_clipboard_image")
        self.layout.prop(self, "enable_phantom")
        self.layout.prop(self, "enable_camera_bookmarks")


class O_OT_use_startup(bpy.types.Operator):
    bl_idname = "o.use_startup"
    bl_label = "Use OmooLab Startup"
    bl_description = "Replace this Blender version's user startup.blend"

    def execute(self, _context):
        if _resource_bundle is None:
            self.report({"ERROR"}, "No compatible O startup file is available")
            return {"CANCELLED"}

        try:
            target_file = replace_user_startup(_resource_bundle.startup_file)
        except (OSError, RuntimeError) as error:
            self.report({"ERROR"}, f"Failed to replace startup file: {error}")
            return {"CANCELLED"}

        self.report({"INFO"}, f"Replaced startup file: {target_file}")
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(
            self,
            event,
            title="Use OmooLab Startup",
            message=(
                "This will overwrite the existing config/startup.blend. "
                "This action cannot be undone."
            ),
            confirm_text="Overwrite Startup",
        )


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


def replace_user_startup(source_file):
    config_directory = bpy.utils.user_resource("CONFIG", create=True)
    if not config_directory:
        raise RuntimeError("Blender user config directory is unavailable")

    target_file = Path(config_directory) / "startup.blend"
    return copy_file_atomically(source_file, target_file)


def install_keyconfig_preset(source_file):
    preset_directory = bpy.utils.user_resource(
        "SCRIPTS",
        path=str(Path("presets") / "keyconfig"),
        create=True,
    )
    if not preset_directory:
        raise RuntimeError("Blender user scripts directory is unavailable")

    target_file = Path(preset_directory) / Path(source_file).name
    if target_file.is_file() and filecmp.cmp(
        source_file,
        target_file,
        shallow=False,
    ):
        return target_file

    return copy_file_atomically(source_file, target_file)


def draw_file_defaults(self, _context):
    if _resource_bundle is None:
        return

    self.layout.operator(
        O_OT_use_startup.bl_idname,
        text=f"Use {DISPLAY_NAME}",
    )
    self.layout.separator()


def restore_selected_keyconfig(keyconfig_file):
    selected_name = bpy.context.preferences.keymap.active_keyconfig
    if selected_name != KEYCONFIG_NAME:
        return

    active_keyconfig = bpy.context.window_manager.keyconfigs.active
    if active_keyconfig is not None and active_keyconfig.name == KEYCONFIG_NAME:
        return

    # 首次同步 preset 时 Blender 已完成 keyconfig 初始化，因此这里恢复用户之前保存的明确选择。
    if bpy.utils.keyconfig_set(str(keyconfig_file)):
        return

    print(f"{DISPLAY_NAME}: failed to restore keymap preset {KEYCONFIG_NAME!r}")


def register():
    global _menu_registered
    global _operator_registered
    global _preferences_registered
    global _resource_bundle

    resource_bundle = find_resource_bundle(
        RESOURCES_ROOT,
        bpy.app.version[:2],
    )
    keyconfig_file = install_keyconfig_preset(resource_bundle.keyconfig_file)

    bpy.utils.register_class(O_Preferences)
    _preferences_registered = True

    bpy.utils.register_class(O_OT_use_startup)
    _operator_registered = True
    clipboard_image.register()
    phantom.register()
    camera_bookmarks.register()

    _resource_bundle = resource_bundle

    bpy.types.TOPBAR_MT_file_defaults.prepend(draw_file_defaults)
    _menu_registered = True
    restore_selected_keyconfig(keyconfig_file)


def unregister():
    global _menu_registered
    global _operator_registered
    global _preferences_registered
    global _resource_bundle

    if _menu_registered:
        bpy.types.TOPBAR_MT_file_defaults.remove(draw_file_defaults)
        _menu_registered = False

    camera_bookmarks.unregister()
    phantom.unregister()
    clipboard_image.unregister()

    if _operator_registered:
        bpy.utils.unregister_class(O_OT_use_startup)
        _operator_registered = False

    if _preferences_registered:
        bpy.utils.unregister_class(O_Preferences)
        _preferences_registered = False

    _resource_bundle = None
