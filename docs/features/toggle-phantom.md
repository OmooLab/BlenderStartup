# Toggle Phantom

Toggle Phantom 将活动对象临时切换为半透明、不会进入相机渲染和阴影计算的状态。它适合把外壳、遮挡物或参考模型留在视图中，同时继续观察和选择内部对象。

## 使用方法

1. 在 Object Mode 选择对象。
2. 打开鼠标右键上下文菜单。
3. 选择 `Toggle Phantom`。
4. 再次执行以恢复。

## 启用时发生什么

- Viewport Alpha 设置为 `0.35`
- 开启透明显示
- 关闭 Camera Ray 可见性
- 关闭 Shadow Ray 可见性
- Blender 版本支持时关闭 Raycast 可见性

## 可逆状态

功能会把对象原本的 Alpha 和可见性设置记录到对象自定义属性中。关闭 Phantom 时恢复原值并清理临时状态，而不是强制恢复为一组假定的默认值。

Phantom 状态会跟随 `.blend` 保存；对象处于 Phantom 时关闭并重新打开文件，仍可再次执行 Toggle Phantom 恢复之前的设置。
