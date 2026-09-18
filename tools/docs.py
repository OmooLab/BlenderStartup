"""Build, preview, and publish the project documentation."""

import argparse
import subprocess
import tomllib
from pathlib import Path

from tools import keymap


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCUMENTATION_COMMANDS = {
    "build": ("mkdocs", "build", "--strict"),
    "dev": ("mkdocs", "serve"),
}


def project_version():
    """Return the documentation version declared by the project."""
    project = tomllib.loads(
        (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    )["project"]
    return project["version"]


def documentation_command(command):
    """Return the command line that runs one documentation subcommand."""
    if command == "deploy":
        return (
            "mike",
            "deploy",
            "--update-aliases",
            project_version(),
            "latest",
        )
    return DOCUMENTATION_COMMANDS[command]


def run(command):
    """Run one external command from the project root."""
    print(
        "+",
        subprocess.list2cmdline([str(part) for part in command]),
        flush=True,
    )
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Build, preview, publish, or regenerate the documentation.",
    )
    commands = parser.add_subparsers(dest="command")

    keymap_command = commands.add_parser(
        "keymap",
        help="Regenerate the Keymap reference pages",
    )
    keymap_command.add_argument(
        "--target",
        choices=("all", *keymap.TARGETS),
        default="all",
    )
    keymap_command.add_argument(
        "--baseline-directory",
        type=Path,
        help=(
            "Directory containing blender_default_b45.py and "
            "blender_default_b52.py. Official sources are downloaded when omitted."
        ),
    )

    commands.add_parser(
        "build",
        help="Build the site, treating warnings as errors",
    )
    commands.add_parser(
        "dev",
        help="Preview the site with live reload",
    )
    commands.add_parser(
        "deploy",
        help="Publish the current project version and point latest at it",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return
    if args.command == "keymap":
        keymap.generate_targets(
            keymap.requested_targets(args.target),
            args.baseline_directory,
        )
        return
    try:
        run(documentation_command(args.command))
    except KeyboardInterrupt:
        # 本地预览用 Ctrl+C 结束，不需要输出回溯。
        pass


if __name__ == "__main__":
    main()
