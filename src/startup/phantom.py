import bpy


ADDON_ID = __package__
PHANTOM_ALPHA = 0.35
PHANTOM_STATE_KEY = "o_phantom"
PREVIOUS_ALPHA_KEY = "o_phantom_previous_alpha"
PREVIOUS_VISIBLE_CAMERA_KEY = "o_phantom_previous_visible_camera"
PREVIOUS_VISIBLE_RAYCAST_KEY = "o_phantom_previous_visible_raycast"
PREVIOUS_VISIBLE_SHADOW_KEY = "o_phantom_previous_visible_shadow"
PREVIOUS_SHOW_TRANSPARENT_KEY = "o_phantom_previous_show_transparent"

_menu_registered = False
_operator_registered = False


def is_enabled(context):
    preferences = getattr(context, "preferences", None)
    addons = getattr(preferences, "addons", None)
    if addons is None:
        return True

    addon = addons.get(ADDON_ID)
    if addon is None:
        return True
    return getattr(addon.preferences, "enable_phantom", True)


def is_phantom(obj):
    return bool(obj.get(PHANTOM_STATE_KEY, False))


def enable_phantom(obj):
    obj[PREVIOUS_ALPHA_KEY] = obj.color[3]
    obj[PREVIOUS_VISIBLE_CAMERA_KEY] = obj.visible_camera
    obj[PREVIOUS_VISIBLE_SHADOW_KEY] = obj.visible_shadow
    obj[PREVIOUS_SHOW_TRANSPARENT_KEY] = obj.show_transparent
    if hasattr(obj, "visible_raycast"):
        obj[PREVIOUS_VISIBLE_RAYCAST_KEY] = obj.visible_raycast
    obj[PHANTOM_STATE_KEY] = True

    obj.color = (*obj.color[:3], PHANTOM_ALPHA)
    obj.show_transparent = True
    obj.visible_camera = False
    obj.visible_shadow = False
    if hasattr(obj, "visible_raycast"):
        obj.visible_raycast = False


def disable_phantom(obj):
    alpha = obj.get(PREVIOUS_ALPHA_KEY, 1.0)
    visible_camera = obj.get(PREVIOUS_VISIBLE_CAMERA_KEY, True)
    visible_shadow = obj.get(PREVIOUS_VISIBLE_SHADOW_KEY, True)
    show_transparent = obj.get(PREVIOUS_SHOW_TRANSPARENT_KEY, False)

    obj.color = (*obj.color[:3], alpha)
    obj.visible_camera = visible_camera
    obj.visible_shadow = visible_shadow
    obj.show_transparent = show_transparent
    if hasattr(obj, "visible_raycast"):
        obj.visible_raycast = obj.get(PREVIOUS_VISIBLE_RAYCAST_KEY, True)

    for property_name in (
        PHANTOM_STATE_KEY,
        PREVIOUS_ALPHA_KEY,
        PREVIOUS_VISIBLE_CAMERA_KEY,
        PREVIOUS_VISIBLE_RAYCAST_KEY,
        PREVIOUS_VISIBLE_SHADOW_KEY,
        PREVIOUS_SHOW_TRANSPARENT_KEY,
    ):
        if property_name in obj:
            del obj[property_name]


class O_OT_toggle_phantom(bpy.types.Operator):
    bl_idname = "o.toggle_phantom"
    bl_label = "Toggle Phantom"
    bl_description = (
        "Toggle transparent Solid display and rendered ray visibility"
    )
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return is_enabled(context) and context.object is not None

    def execute(self, context):
        obj = context.object
        if is_phantom(obj):
            disable_phantom(obj)
        else:
            enable_phantom(obj)
        return {"FINISHED"}


def draw_object_context_menu(self, context):
    if not is_enabled(context):
        return

    self.layout.operator(
        O_OT_toggle_phantom.bl_idname,
        text="Toggle Phantom",
    )
    self.layout.separator()


def register():
    global _menu_registered
    global _operator_registered

    bpy.utils.register_class(O_OT_toggle_phantom)
    _operator_registered = True
    bpy.types.VIEW3D_MT_object_context_menu.prepend(draw_object_context_menu)
    _menu_registered = True


def unregister():
    global _menu_registered
    global _operator_registered

    if _menu_registered:
        bpy.types.VIEW3D_MT_object_context_menu.remove(draw_object_context_menu)
        _menu_registered = False

    if _operator_registered:
        bpy.utils.unregister_class(O_OT_toggle_phantom)
        _operator_registered = False
