import bpy


REPO_NAME = "OmooLab Extensions"
REPO_MODULE = "omoolab"
REPO_REMOTE_URL = "https://extensions.omoolab.xyz/"


def _normalized_url(url):
    return url.rstrip("/")


def _find_repo(repos):
    remote_url = _normalized_url(REPO_REMOTE_URL)
    return next(
        (
            repo
            for repo in repos
            if _normalized_url(repo.remote_url) == remote_url
        ),
        None,
    )


def _available_module(repos):
    modules = {repo.module for repo in repos}
    if REPO_MODULE not in modules:
        return REPO_MODULE

    suffix = 2
    while f"{REPO_MODULE}_{suffix}" in modules:
        suffix += 1
    return f"{REPO_MODULE}_{suffix}"


def register():
    repos = bpy.context.preferences.extensions.repos
    repo = _find_repo(repos)
    if repo is None:
        repo = repos.new(
            name=REPO_NAME,
            module=_available_module(repos),
            custom_directory="",
            remote_url=REPO_REMOTE_URL,
            source="USER",
        )
    repo.use_sync_on_startup = True


def unregister():
    pass
