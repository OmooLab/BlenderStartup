# 五分钟上手

不必一次记住完整 Keymap。先掌握下面几组操作，就能理解这套方案的基本语言。

## 1. 用熟悉的方式观察

| 操作 | 快捷键 |
| --- | --- |
| 旋转视图 | `ALT + LMB` |
| 平移视图 | `ALT + MMB` |
| 缩放视图 | `ALT + RMB` |
| 聚焦所选 | `F` |
| 查看全部 | 双击 `F` |

Blender 原生的 `MMB` 导航、数字键盘视图和 `GRAVE` View Pie 仍然可以使用。

## 2. 用 Tab 添加内容

在 Object Mode 中点击并松开 `TAB`，打开 Add Menu。移动到 Node Editor 后，同样点击 `TAB` 添加节点。

这是最重要的统一语义：**向当前上下文添加内容**。

## 3. 拖动 Tab 切换模式

在 3D View 中拖动 `TAB` 打开 Object Mode Pie。原本“按一下 Tab 在 Object/Edit 间切换”的绑定被停用，为添加入口让路；模式选择则保留在同一按键的拖动手势中。

也可以使用数字键快速进入组件模式：

| 快捷键 | 模式 |
| --- | --- |
| `1` | Edit Mode / Vertex |
| `2` | Edit Mode / Edge |
| `3` | Edit Mode / Face |
| `4` | Object Mode |

## 4. 保留 Blender 变换手感

- `G`：立即移动
- `S`：立即缩放
- 双击 `R`：立即旋转
- `Q / W / R / E`：选择、移动、旋转、缩放工具

这样既能使用 Blender 的即时变换，也能按常见 DCC 的工具布局操作。

## 5. 用 Shift + Tab 管理吸附

- `SHIFT + TAB`：切换吸附
- `CTRL + SHIFT + TAB`：打开吸附设置

这一组在 3D View、Node Editor 和 UV 等上下文中保持相近含义。

下一步可以阅读[主要改动](../keymap/changes.md)，或直接从[完整参考](../reference/index.md)查询具体功能。
