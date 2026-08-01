import json

import bpy


CAMERA_PROPERTIES = (
    "type",
    "lens",
    "lens_unit",
    "sensor_fit",
    "sensor_width",
    "sensor_height",
    "shift_x",
    "shift_y",
    "clip_start",
    "clip_end",
    "ortho_scale",
    "panorama_type",
    "fisheye_fov",
    "fisheye_lens",
    "latitude_min",
    "latitude_max",
    "longitude_min",
    "longitude_max",
)

DOF_PROPERTIES = (
    "use_dof",
    "focus_distance",
    "aperture_fstop",
    "aperture_blades",
    "aperture_rotation",
    "aperture_ratio",
)

def is_camera_view(context):
    area = getattr(context, "area", None)
    if area is None or getattr(area, "type", None) != "VIEW_3D":
        return False

    region_3d = getattr(context, "region_data", None)
    if region_3d is None:
        space_data = getattr(context, "space_data", None)
        region_3d = getattr(space_data, "region_3d", None)
    return (
        region_3d is not None
        and region_3d.view_perspective == "CAMERA"
    )


def active_camera(scene):
    camera = getattr(scene, "camera", None)
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        return None
    return camera


def _serializable_properties(owner, property_names):
    values = {}
    for property_name in property_names:
        if not hasattr(owner, property_name):
            continue
        value = getattr(owner, property_name)
        if isinstance(value, (bool, float, int, str)):
            values[property_name] = value
    return values


def capture_camera_state(camera):
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        raise ValueError("The scene has no active camera")

    camera_data = camera.data
    state = {
        "matrix_world": [
            [float(value) for value in row]
            for row in camera.matrix_world
        ],
        "camera": _serializable_properties(
            camera_data,
            CAMERA_PROPERTIES,
        ),
    }

    dof = getattr(camera_data, "dof", None)
    if dof is not None:
        state["dof"] = _serializable_properties(dof, DOF_PROPERTIES)
        focus_object = getattr(dof, "focus_object", None)
        if focus_object is not None:
            state["dof"]["focus_object"] = focus_object.name

    return json.dumps(state, separators=(",", ":"), sort_keys=True)


def _restore_properties(owner, values):
    for property_name, value in values.items():
        if not hasattr(owner, property_name):
            continue
        try:
            setattr(owner, property_name, value)
        except (AttributeError, TypeError, ValueError):
            continue


def restore_camera_state(camera, state_json):
    if camera is None or getattr(camera, "type", None) != "CAMERA":
        raise ValueError("The scene has no active camera")

    try:
        state = json.loads(state_json)
        matrix_rows = state["matrix_world"]
        camera_values = state["camera"]
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise ValueError("The bookmark data is invalid") from error

    if (
        len(matrix_rows) != 4
        or any(len(row) != 4 for row in matrix_rows)
    ):
        raise ValueError("The bookmark transform is invalid")

    from mathutils import Matrix

    camera.matrix_world = Matrix(matrix_rows)
    camera_data = camera.data

    camera_type = camera_values.get("type")
    if camera_type is not None:
        _restore_properties(camera_data, {"type": camera_type})
    _restore_properties(
        camera_data,
        {
            name: value
            for name, value in camera_values.items()
            if name != "type"
        },
    )

    dof_values = state.get("dof", {})
    focus_object_name = dof_values.pop("focus_object", None)
    dof = getattr(camera_data, "dof", None)
    if dof is not None:
        _restore_properties(dof, dof_values)
        if focus_object_name:
            dof.focus_object = bpy.data.objects.get(focus_object_name)
        elif hasattr(dof, "focus_object"):
            dof.focus_object = None

    camera.update_tag()
    camera_data.update_tag()
