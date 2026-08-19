import sys

import bpy

from .actions import (
    PasteTargetError,
    acquire_packed_image,
    paste_image,
    paste_location,
    target_for_context,
)
from .clipboard import (
    ClipboardImageError,
    ClipboardImageUnavailable,
    clipboard_change_token,
    clipboard_image_supported,
    read_clipboard_image,
)


_keymap_items = []
_operator_registered = False
_native_copy_token = None


class TrackNativeCopy(bpy.types.Operator):
    bl_idname = "o.track_native_copy"
    bl_label = "Track Native Copy"
    bl_description = "Preserve Blender's native copy and paste priority"
    bl_options = {"INTERNAL"}

    def execute(self, _context):
        global _native_copy_token

        _native_copy_token = clipboard_change_token()
        return {"PASS_THROUGH"}


class PasteClipboardImage(bpy.types.Operator):
    bl_idname = "o.paste_clipboard_image"
    bl_label = "Paste Clipboard Image"
    bl_description = "Paste and pack the clipboard image for the current editor"
    bl_options = {"REGISTER", "UNDO"}

    o_subdivisions: bpy.props.IntProperty(
        name="Subdivide",
        description=(
            "Minimum cuts across the image; longer dimensions and block depth "
            "adapt to keep faces close to square"
        ),
        default=0,
        min=0,
        soft_max=64,
    )
    o_thickness: bpy.props.FloatProperty(
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
    o_import_as: bpy.props.EnumProperty(
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
        default="REFERENCE",
    )
    o_unshaded: bpy.props.BoolProperty(
        name="Unshaded",
        description=(
            "Use an Emission shader so the image is unaffected by scene lighting"
        ),
        default=False,
    )
    o_paste_target: bpy.props.StringProperty(
        options={"HIDDEN", "SKIP_SAVE"},
    )
    o_location: bpy.props.FloatVectorProperty(
        size=3,
        options={"HIDDEN", "SKIP_SAVE"},
    )
    o_location_set: bpy.props.BoolProperty(
        default=False,
        options={"HIDDEN", "SKIP_SAVE"},
    )

    @classmethod
    def poll(cls, context):
        if not clipboard_image_supported():
            return False
        return target_for_context(context) is not None

    def execute(self, context):
        return self._paste(context)

    def invoke(self, context, event):
        self.o_paste_target = target_for_context(context) or ""
        location = paste_location(context, event)
        if location is not None:
            values = tuple(location)
            self.o_location = (*values, 0.0)[:3]
            self.o_location_set = True
        return self._paste(context, event)

    def draw(self, _context):
        if self.o_paste_target != "PLANE":
            return
        self.layout.prop(self, "o_import_as")
        if self.o_import_as == "PLANE":
            self.layout.prop(self, "o_thickness")
            self.layout.prop(self, "o_subdivisions")
            self.layout.prop(self, "o_unshaded")

    def _paste(self, context, event=None):
        if _should_defer_to_native_paste():
            return {"PASS_THROUGH"}

        if not self.o_paste_target:
            self.o_paste_target = target_for_context(context) or ""

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
            location = None
            if self.o_location_set:
                location = self.o_location
                if self.o_paste_target == "NODE":
                    location = location[:2]
            paste_image(
                context,
                image,
                event,
                location=location,
                subdivisions=self.o_subdivisions,
                import_as=self.o_import_as,
                unshaded=self.o_unshaded,
                thickness=self.o_thickness,
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

    bpy.utils.register_class(TrackNativeCopy)
    bpy.utils.register_class(PasteClipboardImage)
    _operator_registered = True
    _register_keymaps()


def unregister():
    global _native_copy_token, _operator_registered

    _unregister_keymaps()
    if _operator_registered:
        bpy.utils.unregister_class(PasteClipboardImage)
        bpy.utils.unregister_class(TrackNativeCopy)
        _operator_registered = False
    _native_copy_token = None


def _should_defer_to_native_paste():
    if _native_copy_token is None:
        return False
    return clipboard_change_token() == _native_copy_token


def _register_keymaps():
    if not clipboard_image_supported():
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
        modifiers = (
            {"oskey": True}
            if sys.platform == "darwin"
            else {"ctrl": True}
        )
        keymap_item = keymap.keymap_items.new(
            PasteClipboardImage.bl_idname,
            "V",
            "PRESS",
            **modifiers,
        )
        _keymap_items.append((keymap, keymap_item))
        copy_keymap_item = keymap.keymap_items.new(
            TrackNativeCopy.bl_idname,
            "C",
            "PRESS",
            **modifiers,
        )
        _keymap_items.append((keymap, copy_keymap_item))


def _unregister_keymaps():
    for keymap, keymap_item in _keymap_items:
        keymap.keymap_items.remove(keymap_item)
    _keymap_items.clear()
