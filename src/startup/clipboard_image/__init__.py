import sys

import bpy

from .actions import (
    PasteTargetError,
    acquire_packed_image,
    paste_image,
    target_for_context,
)
from .clipboard import (
    ClipboardImageError,
    ClipboardImageUnavailable,
    read_clipboard_image,
)


ADDON_ID = __package__.rpartition(".")[0]
_keymap_items = []
_operator_registered = False


def is_enabled(context):
    preferences = getattr(context, "preferences", None)
    addons = getattr(preferences, "addons", None)
    if addons is None:
        return True

    addon = addons.get(ADDON_ID)
    if addon is None:
        return True
    return getattr(addon.preferences, "enable_clipboard_image", True)


class O_OT_paste_clipboard_image(bpy.types.Operator):
    bl_idname = "o.paste_clipboard_image"
    bl_label = "Paste Clipboard Image"
    bl_description = "Paste and pack the clipboard image for the current editor"
    bl_options = {"REGISTER", "UNDO"}

    subdivisions: bpy.props.IntProperty(
        name="Subdivide",
        description=(
            "Minimum cuts across the image; longer dimensions and block depth "
            "adapt to keep faces close to square"
        ),
        default=0,
        min=0,
        soft_max=64,
    )
    thickness: bpy.props.FloatProperty(
        name="Thickness",
        description=(
            "Create a centered block around the image plane; zero keeps it flat"
        ),
        default=0.0,
        min=0.0,
        soft_max=2.0,
        subtype="DISTANCE",
        unit="LENGTH",
    )
    import_as: bpy.props.EnumProperty(
        name="Import As",
        description="Choose the 3D View representation for the image",
        items=(
            (
                "PLANE",
                "Plane",
                "Create a mesh plane with an image material",
            ),
            (
                "REFERENCE",
                "Reference Image",
                "Create an image Empty like dragging an image into Blender",
            ),
        ),
        default="PLANE",
    )
    unshaded: bpy.props.BoolProperty(
        name="Unshaded",
        description=(
            "Use an Emission shader so the image is unaffected by scene lighting"
        ),
        default=False,
    )
    paste_target: bpy.props.StringProperty(
        options={"HIDDEN", "SKIP_SAVE"},
    )

    @classmethod
    def poll(cls, context):
        if sys.platform != "win32":
            return False
        return is_enabled(context) and target_for_context(context) is not None

    def execute(self, context):
        return self._paste(context)

    def invoke(self, context, event):
        self.paste_target = target_for_context(context) or ""
        return self._paste(context, event)

    def draw(self, _context):
        if self.paste_target != "PLANE":
            return
        self.layout.prop(self, "import_as")
        if self.import_as == "PLANE":
            self.layout.prop(self, "thickness")
            self.layout.prop(self, "subdivisions")
            self.layout.prop(self, "unshaded")

    def _paste(self, context, event=None):
        if not self.paste_target:
            self.paste_target = target_for_context(context) or ""

        try:
            image_data, suffix = read_clipboard_image()
        except ClipboardImageUnavailable:
            return {"PASS_THROUGH"}
        except ClipboardImageError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}

        image = None
        image_reused = False
        try:
            image, image_reused = acquire_packed_image(image_data, suffix)
            paste_image(
                context,
                image,
                event,
                subdivisions=self.subdivisions,
                import_as=self.import_as,
                unshaded=self.unshaded,
                thickness=self.thickness,
            )
        except (OSError, RuntimeError, PasteTargetError) as error:
            if image is not None and not image_reused and image.users == 0:
                bpy.data.images.remove(image)
            self.report({"ERROR"}, f"Unable to paste clipboard image: {error}")
            return {"CANCELLED"}

        self.report({"INFO"}, f"Pasted and packed {image.name}")
        return {"FINISHED"}


def register():
    global _operator_registered

    bpy.utils.register_class(O_OT_paste_clipboard_image)
    _operator_registered = True
    _register_keymaps()


def unregister():
    global _operator_registered

    _unregister_keymaps()
    if _operator_registered:
        bpy.utils.unregister_class(O_OT_paste_clipboard_image)
        _operator_registered = False


def _register_keymaps():
    if sys.platform != "win32":
        return

    keyconfigs = getattr(bpy.context.window_manager, "keyconfigs", None)
    addon_keyconfig = getattr(keyconfigs, "addon", None)
    if addon_keyconfig is None:
        return

    keymap_definitions = (
        ("3D View", "VIEW_3D"),
        ("Node Editor", "NODE_EDITOR"),
    )
    for keymap_name, space_type in keymap_definitions:
        keymap = addon_keyconfig.keymaps.new(
            name=keymap_name,
            space_type=space_type,
        )
        keymap_item = keymap.keymap_items.new(
            O_OT_paste_clipboard_image.bl_idname,
            "V",
            "PRESS",
            ctrl=True,
        )
        _keymap_items.append((keymap, keymap_item))


def _unregister_keymaps():
    for keymap, keymap_item in _keymap_items:
        keymap.keymap_items.remove(keymap_item)
    _keymap_items.clear()
