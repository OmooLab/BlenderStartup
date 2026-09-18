# Blender Startup 项目规范

## 总则

**不管是代码还是文档，遵循「少就是多」的原则，以好理解为首要要求**

- 说明性内容（提交说明、文档、注释、Mermaid 等）以中文为主，专有名词和约定俗成的表达可使用英文
- 修改代码、依赖或执行方式后，
  - 不保留旧路径、转发函数、兼容层或胶水代码
  - 仅更新并运行相关测试，不主动同步文档、构建文档或打包产物
- 优先选择依赖少、直接、易验证的实现，不为尚未出现的需求提前增加抽象层
- 复用已有函数，避免重复造轮子；保留工作区中与当前任务无关的已有改动
- 确保文件名、文件夹名与内容边界一致

## 全面整理代码

当用户说「全面整理代码」时，依据本文件规范，直接执行以下整理：

- 按业务职责梳理 `src/startup/` 的结构与命名；每项功能使用独立目录，`__init__.py` 只负责导出与注册
- 沿真实调用链清理无用代码，不把仅有测试引用当作业务用途；查证动态调用和注册入口后再删除
- 精简测试，保留有效行为覆盖，使测试名称、归属与功能对应
- 同步整理 `tools/`、`docs/` 和相关引用，使名称、说明与实际实现一致
- 保留已有的其他修改和有效功能，运行全部测试并确认正常退出，检查旧引用与最终差异，简要报告调整及验证结果


## 常见命令

```bash
# 同步开发环境
uv sync

# 运行全部测试
uv run pytest

# 构建目标到 dist/，默认全部，可用 --target 限定
uv run pack

# 本地构建多版本静态页面（只提交到本地 gh-pages 分支，不推送）
uv run docs build

# 本地热更新预览当前文档
uv run docs dev

# 生成相对同版本 Blender Default 的快捷键差异参考
uv run docs keymap

# 用 pyproject.toml 中的 major.minor.x 发布文档并更新 latest
uv run docs deploy
```

## 命名规范

- 变量、函数和 Docstring 使用英文；同一概念在代码、测试和文档中使用统一表达
- Python 类使用大驼峰，不添加项目名前缀；Operator 使用动宾结构，如 `AddCameraBookmark`；Menu、Panel、AddonPreferences、PropertyGroup 使用实际类型后缀，如 `CameraBookmarksPieMenu`、`CameraBookmarksPanel`
- 项目在 Blender API 中使用缩写 `O`（取自 OmooLab），`tests/test_addon.py` 负责校验该约定
- Operator `bl_idname` 使用 `o.` 前缀，如 `o.add_camera_bookmark`；Menu 使用 `O_MT_`、Panel 使用 `O_PT_`
- 公共 Blender RNA 类型的自定义 Property 使用 `o_` 前缀，如 `o_camera_bookmarks`；Operator 自身 Property 不加项目前缀，使用业务名称
- 文件和目录名表达稳定的业务分类与模块职责，集合层用复数，单项分类用单数

## 项目与模板

- 项目和发行包统一称为 `Blender Startup`，可以包含多个 Blender Application Template；当前模板显示名是 `Omoo Lab`，内部目录与命令行 ID 固定为 `Omoo_Lab`，三者不要混用
- 构建目标使用 `b<major><minor>` 表示最低适用 Blender 版本，当前为 `b45`（Blender 4.5+）和 `b52`（Blender 5.2+）；产物命名为 `BlenderStartup.v<版本号>.b<目标>.zip`
- `template/` 保存构建素材；同一目标必须同时提供 `startup.b<目标>.blend`、`userpref.b<目标>.blend` 与 `keyconfig.b<目标>.py`，禁止跨目标复用
- 新增构建目标只需补齐同后缀的三项素材并运行 `uv run pack`；缺少任一文件时必须构建失败，不生成不完整产物

## Blender 开发规范

- `src/startup/` 只放所有构建目标共用的运行时代码，根 `__init__.py` 是唯一入口
- 每项功能使用独立目录并暴露 `register()` / `unregister()`；入口按 `FEATURE_MODULE_NAMES` 顺序注册、逆序注销，功能目录不存在时跳过
- 功能内部按职责拆分文件，如 `camera_bookmark/layout.py`、`preview.py`、`state.py`，不要把无关职责堆进 `__init__.py`
- 新增、删除或重命名功能时同步更新入口和测试；新增或修改 Blender 类型时检查注册顺序、逆序注销和重复注册行为，并补充测试
- Application Template 功能只在模板激活期间注册，切换到其他模板后必须完整注销
- Keymap Preset 可以同步到用户脚本目录，但不得未经用户选择就切换其当前 Keymap
- 不替换 Blender 默认配置目录中的 `config/startup.blend`，也不把本项目改造成 Extension 安装流程

## 文档规范

- `README.md` 面向最终用户，只说明产品定位、安装方法和功能用法；构建机制与实现细节保留在本文件或代码中
- 文档只描述当前已实现的行为；版本范围、快捷键、菜单名称、默认值和文件名必须能从代码、素材或测试中验证
- 不使用 `---` 分隔线，一级标题只在文档开头使用一次；Mermaid 节点 ID 使用英文字符，节点显示文本可用中文，流程图默认从上到下
- 文档中不写死项目版本号，安装包统一使用 `BlenderStartup.v<版本号>.b<目标>.zip` 这类占位写法
