# Camera Bookmark

Camera Bookmark 用来保存同一台活动相机的多个视角，并为每个书签保存预览图。适合镜头构图比较、产品角度探索和阶段性评审。

## 快速使用

1. 进入 Camera View。
2. 按 `SHIFT + GRAVE` 打开 Bookmarks Pie。
3. 选择 `Add Bookmark` 保存当前相机状态。
4. 再次打开菜单，进入 `Bookmarks` 浏览预览并恢复视角。

Camera View 的 Sidebar 中也会显示 `View > Bookmarks` Panel。

## 可以做什么

- **Add Bookmark**：记录当前活动相机视角并生成预览
- **Recall**：把书签状态恢复到当前活动相机
- **Update**：使用当前相机状态与新预览覆盖书签
- **Remove**：删除书签和对应预览

## 保存位置

书签属性与预览图片保存在当前 `.blend` 中。打开或分享工程时，它们会跟随文件，不依赖外部缩略图目录。

## 使用条件

菜单和 Panel 只在 Camera View 中可用，并使用 Scene 的活动相机。没有活动相机时，Panel 会提示 `No Active Camera`。
