import os
import tempfile
from pathlib import Path

import bpy


PREVIEW_MAX_WIDTH = 320
PREVIEW_MAX_HEIGHT = 180
PREVIEW_IMAGE_PREFIX = "O Bookmark"


def preview_dimensions(render_settings):
    percentage = max(1, render_settings.resolution_percentage) / 100
    source_width = max(1, round(render_settings.resolution_x * percentage))
    source_height = max(1, round(render_settings.resolution_y * percentage))
    scale = min(
        PREVIEW_MAX_WIDTH / source_width,
        PREVIEW_MAX_HEIGHT / source_height,
    )
    return (
        max(1, round(source_width * scale)),
        max(1, round(source_height * scale)),
    )


def _capture_render_settings(render_settings):
    image_settings = render_settings.image_settings
    return {
        "filepath": render_settings.filepath,
        "resolution_x": render_settings.resolution_x,
        "resolution_y": render_settings.resolution_y,
        "resolution_percentage": render_settings.resolution_percentage,
        "use_file_extension": render_settings.use_file_extension,
        "file_format": image_settings.file_format,
        "color_mode": image_settings.color_mode,
        "color_depth": image_settings.color_depth,
        "compression": image_settings.compression,
    }


def _restore_render_settings(render_settings, values):
    image_settings = render_settings.image_settings
    render_settings.filepath = values["filepath"]
    render_settings.resolution_x = values["resolution_x"]
    render_settings.resolution_y = values["resolution_y"]
    render_settings.resolution_percentage = values["resolution_percentage"]
    render_settings.use_file_extension = values["use_file_extension"]
    image_settings.file_format = values["file_format"]
    image_settings.color_mode = values["color_mode"]
    image_settings.color_depth = values["color_depth"]
    image_settings.compression = values["compression"]


def create_camera_preview(scene, identifier):
    render_settings = scene.render
    previous_settings = _capture_render_settings(render_settings)
    preview_width, preview_height = preview_dimensions(render_settings)
    file_descriptor, temporary_name = tempfile.mkstemp(suffix=".png")
    os.close(file_descriptor)
    temporary_file = Path(temporary_name)
    temporary_file.unlink(missing_ok=True)

    image = None
    try:
        render_settings.filepath = str(temporary_file)
        render_settings.resolution_x = preview_width
        render_settings.resolution_y = preview_height
        render_settings.resolution_percentage = 100
        render_settings.use_file_extension = False
        render_settings.image_settings.file_format = "PNG"
        render_settings.image_settings.color_mode = "RGBA"
        render_settings.image_settings.color_depth = "8"
        render_settings.image_settings.compression = 50

        result = bpy.ops.render.opengl(
            write_still=True,
            view_context=False,
        )
        if "FINISHED" not in result or not temporary_file.is_file():
            raise RuntimeError("Blender could not render the camera preview")

        image = bpy.data.images.load(
            str(temporary_file),
            check_existing=False,
        )
        image.name = f"{PREVIEW_IMAGE_PREFIX} {identifier}"
        # 临时 PNG 只用于生成 Image，pack 后缩略图会随 .blend 保存。
        image.pack()
        image.preview_ensure()
        return image
    except Exception:
        if image is not None:
            bpy.data.images.remove(image)
        raise
    finally:
        _restore_render_settings(render_settings, previous_settings)
        temporary_file.unlink(missing_ok=True)


def _remove_preview_image(image):
    if image is None:
        return
    if image.users == 0:
        bpy.data.images.remove(image)
