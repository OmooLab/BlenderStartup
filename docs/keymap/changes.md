# 主要改动

这一页只介绍最常用、最能体现设计思路的改动。它不是完整快捷键表；其他变化可以到[完整参考](../reference/index.md)中查询。

## 新增的常用设计

### 两套视图导航并存

Blender 原有的 `MMB` 导航完整保留，同时增加其他 DCC 常用的 `ALT + LMB / MMB / RMB`。

不论原来习惯 Blender、Maya 还是 3ds Max，都可以直接转动、平移和缩放视图，不必先改变肌肉记忆。

### 两套 Transform 方式并存

保留 Blender 的 `G / S / R` 操作逻辑，同时加入 `W / E / R` Transform 工具。即时变换和工具操控可以按场景选择。

执行 Transform 时，除了 Blender 原有的 `X / Y / Z`，还可以使用更靠近左手的：

- `Q / W / E`：约束到 X / Y / Z 轴
- `SHIFT + Q / W / E`：排除 X / Y / Z 轴，在另外两个轴构成的平面上变换

### 更直接的视图与轴心控制

- `F` 聚焦所选，双击 `F` 查看全部
- `T` 打开 Transform Orientation Pie
- `SHIFT + T` 打开 Pivot Point Pie

聚焦、坐标方向和轴心都能由左手快速控制，不必频繁移动到界面顶部。

### 数字键直接进入编辑层级

选中 Mesh 后，使用 `1 / 2 / 3` 直接进入 Edit Mode 的点、边、面层级，使用 `4` 返回 Object Mode。

在 Edit Mode 中，`SHIFT + 1 / 2 / 3` 会把点、边、面加入当前选择模式，方便使用混合组件选择。

在 Object Mode 中，`SHIFT + 1` 可以进一步进入 Sculpt Mode；Grease Pencil 对象则进入对应的 Paint Mode。

### `TAB` 同时服务于添加和模式

- 在 3D View 点击 `TAB` 添加物体
- 在 Node Editor 点击 `TAB` 添加节点
- 在 3D View 拖动 `TAB` 打开 Mode Pie

点击负责向当前上下文添加内容，拖动负责切换工作模式。相关操作集中在同一个入口，又不会互相冲突。

### 常见意图跨 Editor 保持一致

- `SHIFT + TAB` 切换吸附
- `CTRL + SHIFT + TAB` 打开吸附设置
- `CTRL + A` 全选
- `CTRL + D` 复制
- `RMB` 打开上下文菜单

这些按键尽量在 3D View、Node Editor、UV 和动画编辑器中表达相同意图，减少每个 Editor 单独记忆一套规则。

## Blender Default 中被关闭的常用绑定

为了给上述操作让出清晰、统一的入口，部分 Blender 老用户熟悉的默认绑定被关闭或调整。下面这些最值得提前注意。

### `TAB` 不再直接切换 Object/Edit Mode

Blender Default 的单击 `TAB` 切换模式被关闭，因为点击 `TAB` 现在统一用于添加内容。

需要切换模式时，拖动 `TAB` 打开 Mode Pie，或者使用 `1 / 2 / 3 / 4` 直接进入目标层级。

### `A` 不再直接全选

单键 `A` 的全选绑定被关闭，全选改为更通用的 `CTRL + A`。这也让选择操作在不同 Editor 中更加一致。

Blender Default 中原本由 `CTRL + A` 打开的 Apply 菜单相应调整为 `CTRL + SHIFT + A`。

### 单击 `R` 不再立即旋转

单击 `R` 现在选择 Rotate Tool。需要 Blender 式即时旋转时，使用双击 `R`。

### `W` 不再打开上下文菜单

`W` 现在选择 Move Tool。Blender Default 的 `W` 上下文菜单改由 `RMB` 打开，与其他 Editor 和常见 DCC 保持一致。

### `T` 不再开关 Toolbar

`T` 现在用于 Transform Orientation Pie，`SHIFT + T` 用于 Pivot Point Pie。Blender Default 的 Toolbar 开关绑定被关闭，需要从界面边缘展开 Toolbar，或按个人习惯重新设置。

### `B` 不再直接启动 Box Select

Blender Default 的 `B` Box Select 被关闭。使用 `Q` 选择或循环 Select Box 工具，使选择工具与 `W / E / R` 构成连续的工具布局。

### 建模中的 `E` 和 `F` 单键操作被关闭

Mesh、Curve 等编辑上下文中，Blender Default 的 `E` Extrude 和 `F` Fill / Make Face 会与新的工具、聚焦体系冲突，因此相关单键绑定被关闭。

这些操作仍可通过对应工具、菜单或搜索调用。依赖 `E`、`F` 建模肌肉记忆的 Blender 用户需要特别留意。

### 清除 Transform 不再使用 `ALT + G / R / S`

为了与 `W / E / R` Transform 工具的位置对应，清除 Location、Rotation、Scale 分别调整为 `ALT + W / E / R`。

### 数字键不再控制 Collection 显隐

Blender Default 中用数字键切换 Collection 显隐的绑定被关闭，数字键改用于更高频的组件层级和模式切换。

### Node Group 不再使用 `TAB` 进入

Node Editor 的 `TAB` 用于添加节点，因此默认的 `TAB` 进入 Node Group 被关闭。双击节点组进入，按 `ESC` 退出。

## 查询全部变化

以上只列出最常用的新设计，以及最容易影响 Blender 老用户的关闭项。其他新增、调整和停用绑定，请按 Blender 版本查看[完整快捷键参考](../reference/index.md)。
