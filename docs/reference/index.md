# 完整快捷键参考

这里提供 `Refined Industry Compatible` 相对同版本 **Blender Default** 的完整差异，用来查询具体绑定，不承担方案介绍。

## 选择 Blender 版本

- [Blender 4.5 快捷键参考](keymap-b45.md)
- [Blender 5.2 快捷键参考](keymap-b52.md)

两个构建目标使用各自的 Keymap 素材。请查看与安装包一致的版本。

## 功能分区

每个版本都按以下功能组织：

1. 视图与通用操作
2. 对象、模式与 Transform
3. 建模、雕刻与绘制
4. 节点
5. 动画
6. 图像与 UV
7. 视频、跟踪与遮罩
8. 文件、资源与 Outliner
9. 其他编辑器

页面内的“修改、新增、移除”均以 **Blender Default** 为基线。可以使用右侧目录跳转到功能分区，也可以搜索 Keymap 名称、Operator 或 `TAB`、`ALT + LMB` 等按键。

## 生成方式

参考页由 `tools/keymap.py` 自动生成。Keymap 发生变化后，项目维护者运行：

```powershell
uv run docs keymap
```

生成器使用 Blender 官方对应版本的 `blender_default.py`，避免靠人工记忆维护差异。
