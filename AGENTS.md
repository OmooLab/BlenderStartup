# Blender Startup 开发约定

## 总则

- 说明性内容（提交说明、文档、注释、Mermaid 等）以中文为主，专有名词和约定俗成的表达可使用英文
- `README.md` 面向最终用户，只说明产品定位、安装方法和功能用法；构建机制与实现细节保留在本文件或代码中
- 修改代码、构建方式或用户可见行为后，同步更新相关文档和测试，确保描述与实现一致
- 优先选择依赖少、直接、易验证的实现；保留工作区中与当前任务无关的已有改动

## 项目与模板命名

- 项目和发行包统一称为 `Blender Startup`，它可以包含多个 Blender Application Template
- 当前提供的 Application Template 称为 `Omoo Lab`，内部目录与命令行 ID 固定为 `Omoo_Lab`
- 不要把项目名 `Blender Startup`、模板显示名 `Omoo Lab` 和模板 ID `Omoo_Lab` 混用
- 构建目标使用 `b<major><minor>` 表示最低适用 Blender 版本，如 `b45` 表示 Blender 4.5+
- 产物命名为 `BlenderStartup.v<版本号>.b<major><minor>.zip`，如 `BlenderStartup.v<版本号>.b45.zip`
- 当前构建目标为 `b45`（Blender 4.5+）和 `b52`（Blender 5.2+）


- `src/startup/` 只放所有构建目标共用的运行时代码，根 `__init__.py` 是唯一入口
- 每项功能使用独立目录并暴露 `register()` / `unregister()`；入口按 `FEATURE_MODULE_NAMES` 顺序注册，按相反顺序注销
- 功能目录不存在时入口应跳过该功能，不影响其余功能注册；新增、删除或重命名功能时同步更新入口和测试
- 功能内部按职责拆分文件，例如 `camera_bookmark/layout.py`、`preview.py`、`state.py`，不要把无关职责堆进 `__init__.py`
- `template/` 保存构建素材；同一目标必须同时提供 `startup.b<major><minor>.blend`、`userpref.b<major><minor>.blend` 和 `keyconfig.b<major><minor>.py`
- `tools/` 保存仓库维护命令，通过 `pyproject.toml` 的 `[project.scripts]` 暴露为 `uv run pack` 与 `uv run docs`
- 新增构建目标只需补齐同后缀的三项素材并运行 `uv run pack`；缺少任一文件时必须构建失败，不生成不完整产物

## 常见命令

优先在项目根目录使用 Git Bash；环境由 `uv` 管理，`pyproject.toml` 没有运行时依赖。

```bash
# 同步开发环境
uv sync

# 运行全部测试
uv run pytest

# 构建所有版本到 dist/
uv run pack

# 只构建一个目标
uv run pack --target b45

# 本地构建多版本静态页面（只提交到本地 gh-pages 分支，不推送）
uv run docs build

# 本地热更新预览当前文档
uv run docs dev

# 生成相对 Blender Default 的快捷键差异参考
uv run docs keymap

# 用 pyproject.toml 中的 major.minor.x 发布文档并让 latest 指向它（内部执行 mike deploy --update-aliases --push --allow-empty）
uv run docs deploy
```

修改运行时代码、模板发现逻辑或打包规则后，至少运行全部测试；修改构建相关内容后还要实际执行一次打包。

修改文档、Keymap 或文档配置后，运行 `uv run docs build` 在本地构建多版本站点；修改 Keymap 后还要重新生成对应版本的差异参考。快捷键差异只与同版本 `Blender Default` 比较，不以 `Industry Compatible` 为比较基线。

## 发布流程

发布由 `.github/` 中的工作流执行，本地只负责改版本号和打标签。

`.github/` 下的工作流与 Release Drafter 配置统一使用英文，包括工作流名称、步骤名、注释和 Release Notes 模板。

1. 更新 `pyproject.toml` 中的 `version`，提交并推送 `main`
2. 打标签 `v<版本号>`（需与 `pyproject.toml` 完全一致）并推送
3. `release.yml` 校验版本、用 Release Drafter 发布 Release，再把每个目标的 ZIP 作为附件上传
4. Release Notes 由 `.github/release-drafter.yml` 按 PR 标签分组生成

```bash
git tag v<版本号>
git push origin v<版本号>
```

- `test.yml` 在 `main` 推送和 PR 上只运行 `uv run pytest`
- `release-drafter.yml` 在 `main` 推送和 PR 事件上维护 Release 草稿，Release Notes 来自 PR 标签
- `release.yml` 只由 `v*` 标签触发，按 `b45`、`b52` 矩阵分别构建并上传 `BlenderStartup.v<版本号>.b<目标>.zip`；标签与项目版本不一致时终止发布
- 文档版本只使用 `pyproject.toml` 中的 major.minor，写成 `x.y.x` 系列标识，不写具体 patch；`docs build` 和 `docs deploy` 都部署到该版本并更新 `latest`
- mike 默认只提交不推送，`--push` 不能省；内容没有变化时 mike 会跳过提交并连带跳过推送，所以 `uv run docs deploy` 额外带 `--allow-empty`
- 安装包命名、目标发现和校验规则仍由 `tools/pack.py` 负责，工作流不重复实现

## 命名规范

- 变量、函数和 Docstring 使用英文；同一概念在代码、测试和文档中使用统一表达
- Python 类使用大驼峰，不添加项目名前缀
- Operator 使用动宾结构，如 `AddCameraBookmark`；Menu、Panel、AddonPreferences、PropertyGroup 使用实际类型后缀，如 `CameraBookmarksPieMenu`、`CameraBookmarksPanel`
- 项目在 Blender API 中使用缩写 `O`（取自 OmooLab），`tests/test_addon.py` 负责校验该约定
- Operator `bl_idname` 使用 `o.` 前缀和下划线小写，如 `o.add_camera_bookmark`
- Menu `bl_idname` 使用 `O_MT_` 前缀，如 `O_MT_camera_bookmarks_pie`
- Panel `bl_idname` 使用 `O_PT_` 前缀，如 `O_PT_camera_bookmarks`
- 挂载到公共 Blender RNA 类型的自定义 Property 使用 `o_` 前缀，如 `o_camera_bookmarks`、`o_identifier`、`o_import_as`
- Operator 自身 Property 不加项目名前缀，直接使用业务名称

## 代码规范

- 避免不必要的嵌套，优先使用提前返回和小而明确的函数
- 只为特殊、非常规或存在兼容性原因的实现写注释，不复述代码本身
- 使用最少依赖和最直接的实现，不为尚未出现的需求提前增加抽象层
- 删除功能时同时删除失效的参数、分支、测试和文档，不保留没有实际消费者的兼容代码
- 新增或修改 Blender 类型时，同步检查注册顺序、逆序注销和重复注册行为，并补充对应测试
- Application Template 功能只在模板激活期间注册；切换到其他模板后必须完整注销
- 不替换 Blender 默认配置目录中的 `config/startup.blend`，也不把本项目改造成 Extension 安装流程
- Keymap Preset 可以同步到用户脚本目录，但不得未经用户选择就切换其当前 Keymap
- 版本素材必须严格匹配目标后缀，不允许在不同 Blender 目标间隐式复用 `startup.blend`、`userpref.blend` 或 Keymap

## 文档与 Markdown 规范

- `README.md` 描述当前可用的 `Omoo Lab` 模板，但以 `Blender Startup` 作为项目名称
- README 不包含目录结构、注册机制、原子写入、ZIP 内部布局等开发细节
- 不使用 `---` 分隔线；一级标题只在文档开头使用一次
- Mermaid 节点 ID 使用英文字符，节点显示文本可以使用中文
- 文档只描述当前已实现的行为；版本范围、快捷键、菜单名称、默认值和文件名必须能从代码、素材或测试中验证
- 文档中不写死项目版本号，安装包统一使用 `BlenderStartup.v<版本号>.b<目标>.zip` 这类占位写法
- `docs/reference/keymap-b45.md` 和 `docs/reference/keymap-b52.md` 由 `tools/keymap.py` 生成，不手工修改
