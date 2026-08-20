# O General 与版本差异

## 三个名称的区别

| 名称 | 含义 |
| --- | --- |
| Blender Startup | 项目与发行包 |
| O General | 用户在 Blender 中看到的 Application Template |
| `O_General` | 模板内部目录和命令行 ID |

## Application Template 的边界

O General 提供自己的 Startup File、Preferences、Keymap 素材和运行时功能。它不会替换 Blender 用户配置目录中的默认 `config/startup.blend`，也不是 Blender Extension。

运行时功能只在 O General 激活期间注册。扩展仓库、Remote Asset Library 和已经同步到用户脚本目录的 Keymap Preset 属于持久用户配置。

## 构建目标

| 目标 | 最低适用 Blender | 独立素材 |
| --- | --- | --- |
| `b45` | Blender 4.5+ | `startup.b45.blend`、`userpref.b45.blend`、`keyconfig.b45.py` |
| `b52` | Blender 5.2+ | `startup.b52.blend`、`userpref.b52.blend`、`keyconfig.b52.py` |

两个目标不会隐式复用 `.blend`、Preferences 或 Keymap。文档中的完整快捷键差异也按目标分别生成。

## 版本 0.2.22

安装包命名为：

- `Startup.v0.2.22.b45.zip`
- `Startup.v0.2.22.b52.zip`

Mike 文档使用 `0.2.22` 作为版本名，`latest` 作为稳定版别名。
