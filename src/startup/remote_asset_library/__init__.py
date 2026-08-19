import bpy


MINIMUM_VERSION = (5, 2, 0)
REMOTE_LIBRARIES = (
    (
        "O Essentials",
        "https://assets.omoolab.xyz/b52/O_Essentials/",
        None,
    ),
    (
        "O Extra",
        "https://assets.omoolab.xyz/b52/O_Extra/",
        None,
    ),
    (
        "Stanford 3D Scanning",
        "https://assets.omoolab.xyz/stanford-3d-scanning/",
        "APPEND",
    ),
)


def _normalized_url(url):
    return url.rstrip("/")


def _find_remote_library(libraries, remote_url):
    remote_url = _normalized_url(remote_url)
    return next(
        (
            library
            for library in libraries
            if _normalized_url(library.remote_url) == remote_url
        ),
        None,
    )


def register():
    if bpy.app.version < MINIMUM_VERSION:
        return

    libraries = bpy.context.preferences.filepaths.asset_libraries
    for name, remote_url, import_method in REMOTE_LIBRARIES:
        library = _find_remote_library(libraries, remote_url)
        if library is None:
            result = bpy.ops.preferences.asset_library_add(
                type="REMOTE",
                name=name,
                remote_url=remote_url,
            )
            if "FINISHED" not in result:
                raise RuntimeError(
                    f"Unable to add remote asset library: {name}"
                )
            library = _find_remote_library(libraries, remote_url)
            if library is None:
                raise RuntimeError(
                    f"Remote asset library was not created: {name}"
                )

        if import_method is not None:
            library.import_method = import_method


def unregister():
    pass
