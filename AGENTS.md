# OmooLab Startup

`O Startup` 是 OmooLab 的 Blender Application Template：提供版本化的 `startup.blend`、
`Refined Industry Compatible` Keymap，以及仅在模板激活期间加载的公共 Python 功能。
模板不替换 Blender 默认配置目录中的 `config/startup.blend`，也不以 Extension 形式安装。

## 总规范

- 说明性内容（例如提交说明、文档、注释、mermaid），以中文为主，专有名词、约定俗称可用英文

## 构建与测试

- 使用 Git Bash 执行命令；环境由 `uv` 管理，`pyproject.toml` 无运行依赖

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python pack.py
```

- 产物命名为 `Startup.v<版本号>.b<major><minor>.zip`，例如 `Startup.v0.2.20.b45.zip`
- 目前构建目标为 `b45`（Blender 4.5+）与 `b52`（Blender 5.2+）

## 项目结构

- `src/startup/` 只包含所有构建目标共用的运行时代码，`__init__.py` 是入口
- 每个功能对应一个含 `__init__.py` 的独立目录，暴露 `register()` / `unregister()`；入口按 `FEATURE_MODULE_NAMES` 顺序注册，删除整个功能目录后入口会跳过该功能，其余功能仍可注册
- 功能目录内部可继续按职责拆分多个 Python 文件，例如 `camera_bookmark/` 拆出 `layout.py`、`preview.py`、`state.py`
- `template/` 保存构建素材：`splash.png` 为所有版本共用；`startup`、`userpref`、`keyconfig` 通过 `b<major><minor>` 后缀区分 Blender 版本
- 新增构建目标：在 `template/` 下提供同 `b<major><minor>` 后缀的三个文件（`startup`、`userpref`、`keyconfig`），重新运行 `pack.py` 即自动产出对应 ZIP；缺少任一文件时构建失败

## Markdown 规范

- 不使用`---`分割器
- `# Heading` 一级标题仅用于开头
- mermaid 节点名用英文字符

## 代码规范

- 避免嵌套结构
- 特殊的、非常规的需要写注释
- 变量、函数名、Docstring 用全英文
- 同一事物用统一表达
- 使用的依赖越少越好
- 选用简单直接的方式实现
- 代码、执行方式改变，调整已有的文档、计划，而非新建

## Blender 开发规范

- 用`b45`来表示适用blender版本。比如`Startup.v0.1.0.b45.zip`
- Operator、Menu、Panel、AddonPreferences... Class 用大驼峰命名，不加任何前缀。Operator 动宾结构，比如`AddCameraBookmark`；Menu、Panel 以它们本身为后缀，比如`CameraBookmarksPieMenu`、`CameraBookmarksPanel`
- 根据项目名提炼项目缩写，作为 bl_idname 和自定义 Property 的前缀以区分其他功能和属性。本项目缩写为`O`（取自`O_General`），`tests/test_addon.py` 会校验该约定
  - bl_idname 用下划线小写命名：Operator 以`o.`为前缀，比如`o.add_camera_bookmark`；Menu 以`O_MT_`为前缀，比如`O_MT_camera_bookmarks_pie`；Panel 以`O_PT_`为前缀，比如`O_PT_camera_bookmarks`
  - 自定义 Property 用下划线小写命名，以`o_`为前缀，比如`o_camera_bookmarks`、`o_identifier`、`o_import_as`
