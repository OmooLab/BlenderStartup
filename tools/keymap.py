"""Generate the Keymap reference pages relative to Blender Default."""

import argparse
import ast
import runpy
import tempfile
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "b45": {
        "name": "Blender 4.5",
        "keyconfig": PROJECT_ROOT / "template" / "keyconfig.b45.py",
        "output": PROJECT_ROOT / "docs" / "reference" / "keymap-b45.md",
        "source": (
            "https://raw.githubusercontent.com/blender/blender/"
            "blender-v4.5-release/scripts/presets/keyconfig/"
            "keymap_data/blender_default.py"
        ),
    },
    "b52": {
        "name": "Blender 5.2",
        "keyconfig": PROJECT_ROOT / "template" / "keyconfig.b52.py",
        "output": PROJECT_ROOT / "docs" / "reference" / "keymap-b52.md",
        "source": (
            "https://raw.githubusercontent.com/blender/blender/"
            "blender-v5.2-release/scripts/presets/keyconfig/"
            "keymap_data/blender_default.py"
        ),
    },
}


def load_literal_assignment(path, assignment_name="keyconfig_data"):
    syntax_tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    for node in syntax_tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == assignment_name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise RuntimeError(f"{assignment_name} was not found in {path}")


def load_blender_default(path):
    namespace = runpy.run_path(str(path))
    return namespace["generate_keymaps"]()


def freeze(value):
    if isinstance(value, dict):
        return tuple(sorted((key, freeze(item)) for key, item in value.items()))
    if isinstance(value, set):
        return tuple(sorted(freeze(item) for item in value))
    if isinstance(value, (list, tuple)):
        return tuple(freeze(item) for item in value)
    if isinstance(value, float):
        return round(value, 6)
    return value


def keymap_key(keymap):
    name, context, _content = keymap
    return name, context.get("space_type"), context.get("region_type")


def group_keymaps(keymaps):
    return {keymap_key(keymap): keymap[2]["items"] for keymap in keymaps}


def item_distance(left, right):
    left_event = left[1]
    right_event = right[1]
    event_keys = set(left_event) | set(right_event)
    event_distance = sum(
        left_event.get(key) != right_event.get(key)
        for key in event_keys
    )
    property_distance = 0 if freeze(left[2]) == freeze(right[2]) else 3
    return event_distance + property_distance


def remove_exact_matches(custom_items, default_items):
    default_counts = Counter(freeze(item) for item in default_items)
    custom_remaining = []
    for item in custom_items:
        frozen_item = freeze(item)
        if default_counts[frozen_item]:
            default_counts[frozen_item] -= 1
        else:
            custom_remaining.append(item)

    custom_counts = Counter(freeze(item) for item in custom_items)
    default_remaining = []
    for item in default_items:
        frozen_item = freeze(item)
        if custom_counts[frozen_item]:
            custom_counts[frozen_item] -= 1
        else:
            default_remaining.append(item)
    return custom_remaining, default_remaining


def compare_items(custom_items, default_items):
    custom_remaining, default_remaining = remove_exact_matches(
        custom_items,
        default_items,
    )
    default_by_operator = defaultdict(list)
    for item in default_remaining:
        default_by_operator[item[0]].append(item)

    modified = []
    added = []
    for custom_item in custom_remaining:
        candidates = default_by_operator[custom_item[0]]
        if not candidates:
            added.append(custom_item)
            continue
        default_item = min(
            candidates,
            key=lambda item: item_distance(custom_item, item),
        )
        candidates.remove(default_item)
        modified.append((default_item, custom_item))

    removed = [
        item
        for candidates in default_by_operator.values()
        for item in candidates
    ]
    return modified, added, removed


def compare_keymaps(custom_keymaps, default_keymaps):
    custom_groups = group_keymaps(custom_keymaps)
    default_groups = group_keymaps(default_keymaps)
    differences = {}
    for key, custom_items in custom_groups.items():
        modified, added, removed = compare_items(
            custom_items,
            default_groups.get(key, []),
        )
        if modified or added or removed:
            differences[key] = {
                "modified": modified,
                "added": added,
                "removed": removed,
            }
    return differences


KEY_NAMES = {
    "ACCENT_GRAVE": "GRAVE",
    "LEFTMOUSE": "LMB",
    "MIDDLEMOUSE": "MMB",
    "RIGHTMOUSE": "RMB",
    "WHEELUPMOUSE": "WHEEL UP",
    "WHEELDOWNMOUSE": "WHEEL DOWN",
    "RET": "ENTER",
    "ESC": "ESC",
    "SPACE": "SPACE",
    "PERIOD": ".",
    "COMMA": ",",
    "SLASH": "/",
}


def event_label(event):
    parts = []
    for key, label in (
        ("ctrl", "CTRL"),
        ("shift", "SHIFT"),
        ("alt", "ALT"),
        ("oskey", "CMD"),
    ):
        if event.get(key):
            parts.append(label)
    event_type = event.get("type", "Unknown")
    parts.append(KEY_NAMES.get(event_type, event_type.replace("_", " ")))
    value = event.get("value")
    if value not in (None, "PRESS"):
        parts.append(
            {
                "RELEASE": "松开",
                "CLICK": "点击",
                "DOUBLE_CLICK": "双击",
                "CLICK_DRAG": "拖动",
                "ANY": "任意事件",
            }.get(value, value.replace("_", " ").title())
        )
    if event.get("direction"):
        parts.append(event["direction"])
    if event.get("repeat"):
        parts.append("可重复")
    return " + ".join(parts)


def property_label(item):
    options = item[2] or {}
    properties = options.get("properties", [])
    labels = [f"{key}={value!r}" for key, value in properties]
    if options.get("active") is False:
        labels.append("active=False")
    return ", ".join(labels)


def markdown_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def key_markup(event):
    return f"<code>{markdown_cell(event_label(event))}</code>"


REFERENCE_CATEGORIES = (
    "视图与通用操作",
    "对象、模式与 Transform",
    "建模、雕刻与绘制",
    "节点",
    "动画",
    "图像与 UV",
    "视频、跟踪与遮罩",
    "文件、资源与 Outliner",
    "其他编辑器",
)


def reference_category(key):
    name, space_type, _region_type = key
    if "Node" in name or space_type == "NODE_EDITOR":
        return "节点"
    if any(
        word in name
        for word in ("Animation", "Dopesheet", "Graph", "NLA", "Marker")
    ):
        return "动画"
    if "UV" in name or "Image" in name or space_type == "IMAGE_EDITOR":
        return "图像与 UV"
    if any(
        word in name
        for word in ("Clip", "Mask", "Sequencer", "Preview")
    ):
        return "视频、跟踪与遮罩"
    if any(word in name for word in ("File", "Asset", "Outliner")):
        return "文件、资源与 Outliner"
    if any(
        word in name
        for word in ("Object", "Pose", "Transform Modal Map")
    ):
        return "对象、模式与 Transform"
    if any(
        word in name
        for word in (
            "Mesh",
            "Curve",
            "Armature",
            "Lattice",
            "Metaball",
            "Grease Pencil",
            "Paint",
            "Sculpt",
            "Particle",
            "Point Cloud",
            "Font",
        )
    ):
        return "建模、雕刻与绘制"
    if any(
        word in name
        for word in (
            "3D View",
            "Window",
            "Screen",
            "User Interface",
            "Frames",
            "View2D",
        )
    ):
        return "视图与通用操作"
    return "其他编辑器"


def render_item_row(status, item, detail):
    operator, event, _options = item
    properties = property_label(item)
    action = f"`{operator}`"
    if properties:
        action += f"<br><small>{markdown_cell(properties)}</small>"
    return (
        f"| {status} | {key_markup(event)} | "
        f"{action} | {detail} |"
    )


def render_reference(target_id, target, differences):
    modified_count = sum(
        len(items["modified"]) for items in differences.values()
    )
    added_count = sum(len(items["added"]) for items in differences.values())
    removed_count = sum(
        len(items["removed"]) for items in differences.values()
    )
    lines = [
        f"# {target['name']} 快捷键差异",
        "",
        "本页由当前 `Refined Industry Compatible` Keymap 与同版本的 "
        "**Blender Default** 自动比较生成。Industry Compatible 不是比较基线。",
        "",
        '<div class="keymap-summary">',
        f"<div><strong>{modified_count}</strong>修改绑定</div>",
        f"<div><strong>{added_count}</strong>新增绑定</div>",
        f"<div><strong>{removed_count}</strong>移除绑定</div>",
        f"<div><strong>{len(differences)}</strong>受影响 Keymap</div>",
        "</div>",
        "",
        "!!! note \"怎样理解差异\"",
        "",
        "    “修改”表示同一个 Blender Operator 的触发方式或属性发生变化；"
        "“新增”和“移除”表示在相同编辑器 Keymap 中只存在于一侧。"
        "Blender 在运行时生成的工具 Keymap 不会因为没有出现在导出文件中就被记为删除。",
        "",
        f"基线来源：[Blender 官方 `{target_id}` Blender Default 源文件]({target['source']})。",
        "",
    ]
    grouped_differences = defaultdict(list)
    for key, items in differences.items():
        grouped_differences[reference_category(key)].append((key, items))

    for category in REFERENCE_CATEGORIES:
        category_items = grouped_differences.get(category)
        if not category_items:
            continue
        lines.extend([f"## {category}", ""])
        for key, items in sorted(category_items):
            name, space_type, region_type = key
            context = " / ".join(
                value for value in (space_type, region_type) if value
            )
            lines.extend(
                [
                    f"### {name}",
                    "",
                    f"上下文：`{context or '通用'}`",
                    "",
                    "| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |",
                    "| --- | --- | --- | --- |",
                ]
            )
            for default_item, custom_item in items["modified"]:
                detail = f"默认：{key_markup(default_item[1])}"
                default_properties = property_label(default_item)
                if default_properties:
                    detail += f"；{markdown_cell(default_properties)}"
                lines.append(render_item_row("修改", custom_item, detail))
            for item in items["added"]:
                lines.append(
                    render_item_row(
                        "新增",
                        item,
                        "Blender Default 中没有此绑定",
                    )
                )
            for item in items["removed"]:
                detail = "当前 Keymap 中没有此 Blender Default 绑定"
                lines.append(render_item_row("移除", item, detail))
            lines.append("")
    return "\n".join(lines)


def download_source(url, directory, target_id):
    target_file = Path(directory) / f"blender_default_{target_id}.py"
    urllib.request.urlretrieve(url, target_file)
    return target_file


def generate(target_id, baseline_file):
    target = TARGETS[target_id]
    custom_keymaps = load_literal_assignment(target["keyconfig"])
    default_keymaps = load_blender_default(baseline_file)
    differences = compare_keymaps(custom_keymaps, default_keymaps)
    target["output"].parent.mkdir(parents=True, exist_ok=True)
    target["output"].write_text(
        render_reference(target_id, target, differences),
        encoding="utf-8",
    )
    return differences


def generate_targets(target_ids, baseline_directory=None):
    """Regenerate the reference page of every requested build target."""
    with tempfile.TemporaryDirectory() as temporary_directory:
        for target_id in target_ids:
            target = TARGETS[target_id]
            if baseline_directory:
                baseline_file = (
                    Path(baseline_directory)
                    / f"blender_default_{target_id}.py"
                )
            else:
                baseline_file = download_source(
                    target["source"],
                    temporary_directory,
                    target_id,
                )
            differences = generate(target_id, baseline_file)
            print(
                f"Generated {target['output']} "
                f"from {len(differences)} changed keymaps"
            )


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate Keymap docs relative to Blender Default.",
    )
    parser.add_argument(
        "--target",
        choices=("all", *TARGETS),
        default="all",
    )
    parser.add_argument(
        "--baseline-directory",
        type=Path,
        help=(
            "Directory containing blender_default_b45.py and "
            "blender_default_b52.py. Official sources are downloaded when omitted."
        ),
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    generate_targets(requested_targets(args.target), args.baseline_directory)


def requested_targets(target):
    return tuple(TARGETS) if target == "all" else (target,)


if __name__ == "__main__":
    main()
