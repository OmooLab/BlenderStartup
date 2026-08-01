# O General

`O General` 是一个 Blender Application Template。它提供版本化的
`startup.blend`、`Refined Industry Compatible` Keymap，以及只在模板激活期间加载的
公共 Python 功能。

模板不会替换 Blender 默认配置目录中的 `config/startup.blend`，也不需要安装或启用
Extension。

## 安装与使用

根据 Blender 版本选择构建产物：

- Blender 4.5 至 5.1：`startup.v0.2.19.b45.zip`
- Blender 5.2 及其后续兼容版本：`startup.v0.2.19.b52.zip`

在 Blender 左上角的 Blender 菜单中选择 `Install Application Template...`，安装对应
ZIP。安装同一模板的新版本时，Blender 会替换已有的 `O_General` 模板目录。

安装后可通过 Splash Screen 或 `File > New > O General` 使用。也可以从命令行
直接启动：

```bash
blender --app-template O_General
```

模板首次激活时会把对应版本的 `Refined Industry Compatible` 同步到 Blender 用户的
`scripts/presets/keyconfig`，使其出现在 Preferences 的 Keymap Preset 选项中，但不会
自动切换当前 Keymap。模板同时会注册 Python 功能；切换到其他 Application Template
时会注销这些功能。

## 功能

- 使用模板自己的 `startup.blend`，与 Blender 默认 Startup File 分离
- 添加可选的 `Refined Industry Compatible` Keymap Preset
- Camera View 书签与预览图管理
- Object Mode 的 `Toggle Phantom`
- Windows、macOS、Linux 剪贴板图片粘贴：
  - 3D View Object Mode 中创建 Plane 或 Reference Image
  - Sculpt、Vertex Paint、Texture Paint 中设置笔刷 Texture
  - Shader Editor、Compositor、Geometry Nodes 中创建对应图片节点

Camera Bookmark 数据与 packed 预览图保存在当前 `.blend`。在 Camera View 中按
`Shift + \`` 可打开书签 Pie Menu。

`Toggle Phantom` 位于 3D View 的 Object Context Menu。启用后，对象在 Solid 模式下
半透明，并关闭 Camera、Shadow 和可用时的 Raycast Visibility；再次执行会恢复原值。

剪贴板图片会先创建临时文件，载入后立即 pack 到当前 `.blend`，再删除临时文件。没有
可用图片时，原有 `Ctrl+V` 行为会继续执行。

macOS 使用系统自带的 AppKit 读取图片，并将其转换为 PNG。Linux 优先使用
`wl-paste`（Wayland），其次使用 `xclip`（X11）；需要安装 `wl-clipboard` 或 `xclip`。
macOS 使用 `Cmd+V`，Windows 与 Linux 使用 `Ctrl+V`。

## 项目结构

```text
.
├── pack.py
├── pyproject.toml
├── src/
│   └── startup/
│       ├── __init__.py
│       ├── camera_bookmark/
│       │   ├── __init__.py
│       │   ├── layout.py
│       │   ├── preview.py
│       │   └── state.py
│       ├── clipboard_image/
│       └── toggle_phantom/
├── template/
│   ├── splash.png
│   ├── startup.b45.blend
│   ├── startup.b52.blend
│   ├── userpref.b45.blend
│   ├── userpref.b52.blend
│   ├── keyconfig.b45.py
│   └── keyconfig.b52.py
└── tests/
```

`src/startup` 只包含所有构建目标共用的运行时代码。每项功能对应一个包含
`__init__.py` 的独立目录；删除整个功能目录后，根模块会跳过该功能，其他功能仍可注册。
Feature Package 内部可以继续按职责拆分多个 Python 文件。

`template` 保存 App Template 的构建
素材：`splash.png` 为所有版本共用；`startup.b<major><minor>.blend` 和
`userpref.b<major><minor>.blend`、`keyconfig.b<major><minor>.py` 通过文件名后缀区分
Blender 版本。

## 构建

使用 Git Bash：

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python pack.py
```

`pack.py` 会为每组完整的版本素材生成一个 ZIP。每个 ZIP 都符合 Blender
`Install Application Template...` 所需的目录结构：

```text
O_General/
├── __init__.py
├── startup.blend
├── userpref.blend
├── splash.png
├── keyconfig.py
├── camera_bookmark/
│   ├── __init__.py
│   ├── layout.py
│   ├── preview.py
│   └── state.py
├── clipboard_image/
└── toggle_phantom/
```

构建时，公共脚本和 `splash.png` 会写入所有 ZIP；带版本后缀的 Startup File、Preferences
和 Keymap 会分别映射为 `startup.blend`、`userpref.blend`、`keyconfig.py`。模板注册时再把 `keyconfig.py` 同步为用户
脚本目录中的 `presets/keyconfig/Refined_Industry_Compatible.py`，但不执行
`bpy.utils.keyconfig_set()`，因此不会改变当前 Keymap。ZIP 内显式保留
`O_General/` 根目录条目，以便 Blender 安装器正确识别并替换同 ID 的已有模板。

## 添加构建目标

在 `template` 下提供带相同 `b<major><minor>` 后缀的三个文件。例如 Blender 5.3 使用
`b53`：

```text
template/startup.b53.blend
template/userpref.b53.blend
template/keyconfig.b53.py
```

再次运行 `uv run python pack.py` 即会自动增加对应版本的模板 ZIP。缺少任一文件时构建
会失败，避免生成不完整模板。共用的 `template/splash.png` 会进入所有版本的 ZIP。

## Keymap 同步

模板激活时逐字节比较模板携带的 Keymap 与用户脚本目录中的同名 Preset。文件缺失或
内容不同时进行原子替换，确保模板更新后 Keymap 选项同步更新；内容相同时不写入。
模板注销时保留已同步的 Preset，使用户选择它之后，下次启动 Blender 仍能在加载模板
脚本之前恢复该 Keymap。
