# 粘贴剪贴板图片

复制图片后，直接在 Blender 当前编辑器按 `CTRL + V`；macOS 使用 `CMD + V`。Blender Startup 会根据上下文决定如何使用图片，并将它 Pack 到当前 `.blend`。

## 支持的上下文

| 上下文 | 结果 |
| --- | --- |
| 3D View / Object Mode | 创建 Reference Image 或带材质的 Plane |
| Sculpt | 设置为笔刷 Texture |
| Vertex Paint | 设置为笔刷 Texture |
| Texture Paint | 设置为笔刷 Texture |
| Shader Editor | 创建 Image Texture 节点 |
| Compositor | 创建 Image 节点 |
| Geometry Nodes | 创建 Image Texture 节点 |

## 在 3D View 中

图片会放在鼠标所在的屏幕位置，并使用当前 3D Cursor 作为视图深度参考。默认导入为 `Reference Image`。

如果在操作面板中切换为 `Plane`，还可以设置：

- **Thickness**：为图片平面增加居中的厚度
- **Subdivide**：按图片比例产生接近方形的网格
- **Unshaded**：使用 Emission，使图片不受场景灯光影响

## 在 Node Editor 中

节点创建在鼠标位置。不同节点编辑器会选择对应的图片节点类型，不需要先保存临时图片再手动浏览文件。

## 与 Blender 原生粘贴共存

如果刚刚使用 `CTRL + C` 复制了 Blender 内部数据，随后按 `CTRL + V` 时会优先让 Blender 处理原生粘贴。只有剪贴板中存在新的图片数据时，图片粘贴功能才接管操作。

## 平台说明

- Windows：直接支持
- macOS：使用 `CMD + V`
- Linux Wayland：需要 `wl-clipboard`
- Linux X11：需要 `xclip`

剪贴板中没有可用图片时，操作会放行，不阻断 Blender 的其他粘贴行为。
