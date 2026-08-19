import bpy


MINIMUM_VERSION = (5, 2, 0)
REMOTE_LIBRARIES = (
    (
        "O Essentials",
        "https://assets.omoolab.xyz/b52/O_Essentials/",
    ),
    (
        "O Extra",
        "https://assets.omoolab.xyz/b52/O_Extra/",
    ),
)


def _normalized_url(url):
    return url.rstrip("/")


def _has_remote_library(libraries, remote_url):
    remote_url = _normalized_url(remote_url)
    return any(
        _normalized_url(library.remote_url) == remote_url
        for library in libraries
    )


def register():
    if bpy.app.version < MINIMUM_VERSION:
        return

    libraries = bpy.context.preferences.filepaths.asset_libraries
    for name, remote_url in REMOTE_LIBRARIES:
        if _has_remote_library(libraries, remote_url):
            continue

        result = bpy.ops.preferences.asset_library_add(
            type="REMOTE",
            name=name,
            remote_url=remote_url,
        )
        if "FINISHED" not in result:
            raise RuntimeError(f"Unable to add remote asset library: {name}")


def unregister():
    pass
