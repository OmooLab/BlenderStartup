## 总规范

- 说明性内容（例如提交说明、文档、注释、mermaid），以中文为主，专有名词、约定俗称可用英文

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

## Shell 规范

- 优先使用、提供 Git Bash 执行所有 Shell 命令
- Windows 路径在 Bash 命令中优先使用正斜杠形式

## Blender 开发规范

- 插件、资产库压缩包名用大驼峰，如果需要，用`b45`来表示适用blender版本。比如`OmooLab.v0.1.0.b45.zip`
- Operator、Menu、Panel、AddonPreferences... Class 用大驼峰命名，不加任何前缀。Operator 动宾结构，比如`RenderImage`。Menu、Panel 以它们本身为后缀，比如`RenderPanel`
- 根据项目名提炼项目缩写，作为 bl_idname 和 自定义 Property 的前缀以区分其他功能和属性，以`Omoo`为例
  - bl_idname 用下划线小写命名，Operator 的 bl_idname 以`omoo.*`为前缀，比如`omoo.render_panel`；Menu 的以`OMOO_MT_*`为前缀；Panel 的以`OMOO_PT_*`为前缀。比如`OMOO_PT_render_panel`
  - 自定义 Property 用下划线小写命名，以`omoo_*`为前缀。比如`omoo_progress_factor`