import ctypes
import struct
import sys
from ctypes import wintypes


CF_DIB = 8
CF_DIBV5 = 17
MAX_CLIPBOARD_IMAGE_SIZE = 512 * 1024 * 1024


class ClipboardImageError(RuntimeError):
    pass


class ClipboardImageUnavailable(ClipboardImageError):
    pass


def dib_to_bmp(dib_data):
    if len(dib_data) < 12:
        raise ClipboardImageError("Clipboard DIB data is incomplete")

    header_size = struct.unpack_from("<I", dib_data)[0]
    if header_size == 12:
        pixel_offset = _core_dib_pixel_offset(dib_data)
    elif header_size >= 40:
        pixel_offset = _info_dib_pixel_offset(dib_data, header_size)
    else:
        raise ClipboardImageError(
            f"Unsupported clipboard DIB header size: {header_size}"
        )

    # Windows 剪贴板保存的是无 BITMAPFILEHEADER 的 DIB，Blender 需要完整 BMP。
    file_size = 14 + len(dib_data)
    file_header = struct.pack(
        "<2sIHHI",
        b"BM",
        file_size,
        0,
        0,
        14 + pixel_offset,
    )
    return file_header + dib_data


def _core_dib_pixel_offset(dib_data):
    if len(dib_data) < 12:
        raise ClipboardImageError("Clipboard DIB core header is incomplete")

    bit_count = struct.unpack_from("<H", dib_data, 10)[0]
    color_count = 1 << bit_count if bit_count <= 8 else 0
    pixel_offset = 12 + color_count * 3
    _validate_pixel_offset(dib_data, pixel_offset)
    return pixel_offset


def _info_dib_pixel_offset(dib_data, header_size):
    if len(dib_data) < header_size or len(dib_data) < 40:
        raise ClipboardImageError("Clipboard DIB info header is incomplete")

    bit_count = struct.unpack_from("<H", dib_data, 14)[0]
    compression = struct.unpack_from("<I", dib_data, 16)[0]
    colors_used = struct.unpack_from("<I", dib_data, 32)[0]

    color_count = colors_used
    if color_count == 0 and bit_count <= 8:
        color_count = 1 << bit_count

    mask_size = 0
    if header_size == 40 and compression == 3:
        mask_size = 12
    if header_size == 40 and compression == 6:
        mask_size = 16

    pixel_offset = header_size + mask_size + color_count * 4
    if header_size >= 124:
        profile_offset = struct.unpack_from("<I", dib_data, 112)[0]
        profile_size = struct.unpack_from("<I", dib_data, 116)[0]
        if profile_offset and profile_size:
            pixel_offset = max(pixel_offset, profile_offset + profile_size)
    _validate_pixel_offset(dib_data, pixel_offset)
    return pixel_offset


def _validate_pixel_offset(dib_data, pixel_offset):
    if pixel_offset > len(dib_data):
        raise ClipboardImageError("Clipboard DIB pixel offset is out of range")


def read_clipboard_image():
    if sys.platform != "win32":
        raise ClipboardImageUnavailable(
            "Clipboard image paste is currently available on Windows"
        )

    user32 = ctypes.WinDLL("user32", use_last_error=True)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    _configure_windows_api(user32, kernel32)

    png_format = user32.RegisterClipboardFormatW("PNG")
    formats = (
        (png_format, ".png", False),
        (CF_DIBV5, ".bmp", True),
        (CF_DIB, ".bmp", True),
    )

    if not user32.OpenClipboard(None):
        error_code = ctypes.get_last_error()
        raise ClipboardImageError(
            f"Unable to open the Windows clipboard (error {error_code})"
        )

    try:
        for clipboard_format, suffix, is_dib in formats:
            if not clipboard_format:
                continue
            if not user32.IsClipboardFormatAvailable(clipboard_format):
                continue

            image_data = _read_windows_clipboard_data(
                user32,
                kernel32,
                clipboard_format,
            )
            if is_dib:
                image_data = dib_to_bmp(image_data)
            return image_data, suffix
    finally:
        user32.CloseClipboard()

    raise ClipboardImageUnavailable("The clipboard does not contain an image")


def _configure_windows_api(user32, kernel32):
    user32.OpenClipboard.argtypes = [wintypes.HWND]
    user32.OpenClipboard.restype = wintypes.BOOL
    user32.CloseClipboard.argtypes = []
    user32.CloseClipboard.restype = wintypes.BOOL
    user32.IsClipboardFormatAvailable.argtypes = [wintypes.UINT]
    user32.IsClipboardFormatAvailable.restype = wintypes.BOOL
    user32.GetClipboardData.argtypes = [wintypes.UINT]
    user32.GetClipboardData.restype = wintypes.HANDLE
    user32.RegisterClipboardFormatW.argtypes = [wintypes.LPCWSTR]
    user32.RegisterClipboardFormatW.restype = wintypes.UINT

    kernel32.GlobalLock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalUnlock.restype = wintypes.BOOL
    kernel32.GlobalSize.argtypes = [wintypes.HGLOBAL]
    kernel32.GlobalSize.restype = ctypes.c_size_t


def _read_windows_clipboard_data(user32, kernel32, clipboard_format):
    data_handle = user32.GetClipboardData(clipboard_format)
    if not data_handle:
        error_code = ctypes.get_last_error()
        raise ClipboardImageError(
            f"Unable to read clipboard image data (error {error_code})"
        )

    data_size = kernel32.GlobalSize(data_handle)
    if data_size <= 0:
        raise ClipboardImageError("Clipboard image data is empty")
    if data_size > MAX_CLIPBOARD_IMAGE_SIZE:
        raise ClipboardImageError("Clipboard image is larger than 512 MiB")

    data_pointer = kernel32.GlobalLock(data_handle)
    if not data_pointer:
        error_code = ctypes.get_last_error()
        raise ClipboardImageError(
            f"Unable to lock clipboard image data (error {error_code})"
        )

    try:
        return ctypes.string_at(data_pointer, data_size)
    finally:
        kernel32.GlobalUnlock(data_handle)
