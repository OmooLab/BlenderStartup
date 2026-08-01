# OmooLab Startup

`OmooLab Startup` 是一个 Blender Extension，提供 OmooLab 的
`startup.blend` 和 keymap preset。

## 功能

- 在 `File > Defaults` 中增加 `Use OmooLab Startup`
- 在 Preferences 的 Keymap Presets 中增加
  `Refined Industry Compatible`
- 根据当前 Blender 版本自动选择不高于当前版本的最新资源
- 在 Camera View 下通过 3D View 原生 `View > Bookmarks` 顶部面板保存
  当前活动相机状态，并以
  图片预览画廊呈现。点击预览会把所选状态恢复到当前活动相机，也可通过 `Recall`
  再次调取；`Update` 会以当前相机覆盖所选状态和预览。书签记录相机变换、镜头、
  传感器、裁切、透视/正交/全景与景深参数，数据和 packed 预览图均随当前
  `.blend` 保存。此功能默认开启，可在 Extension Preferences 的
  `Bookmarks` 中关闭。在 3D View 中按 `Shift + \`` 可打开专用 Pie Menu：
  `Add Bookmark` 保存当前相机，`Bookmarks` 在鼠标附近打开无名称缩略图选择层；
  点击缩略图即可 Recall，点击外部或按 `Esc` 关闭。快捷选择和侧边栏均不显示
  Bookmark 名称，侧边栏继续用于完整的创建、更新与删除管理。离开 Camera View
  时，专用 Pie 和管理面板均不显示
- 在 3D View 的 Object Mode 中右键物体并选择 `Toggle Phantom`，可切换 Phantom
  模式。开启后物体在 Solid 着色模式下半透明，关闭 Camera 与 Shadow Ray
  Visibility，并关闭 Raycast，因此在 Material Preview、Rendered 视图和最终渲染中
  不可见、不投射阴影，也不参与 Raycast rays；关闭后恢复各项原始设置，不改变
  `hide_render`。此功能默认开启，可在 Extension Preferences 中通过
  `Toggle Phantom` 关闭
- 在 Windows 上按 `Ctrl+V`，根据鼠标所在编辑器和模式粘贴剪贴板图片：
  - 3D View 的 Object Mode：默认创建保持图片宽高比的平面和透明材质；粘贴后可在
    Adjust Last Operation 的 `Import As` 中切换为 `Reference Image`。选择 Plane
    时还可调整 `Thickness` 和 `Subdivide`。`Thickness` 默认为 `0`，生成完全平坦
    的平面；值大于 `0` 时以物体原点为厚度中点生成封闭块体。`Subdivide` 默认值
    `0`，平面生成单个四边形；值大于 `0` 时长边和块体厚度方向会根据实际尺寸自动
    增加切割，使各面网格接近方形。块体侧面使用图片对应边缘的像素沿厚度方向拉伸，
    不会重复显示完整图片。开启 `Unshaded` 可使用保留图片 Alpha 的 Emission 材质，
    避免受到场景灯光影响
  - 3D View 的 Sculpt、Vertex Paint、Texture Paint：设为当前笔刷的 Texture，使用
    `STENCIL` mapping 并匹配图片宽高比
  - 材质 Shader Editor：创建 `Image Texture` 节点
  - World Shader Editor：创建 `Environment Texture` 节点
  - Compositor：创建 `Image` 节点
  - Geometry Nodes：创建 `Image Texture` 节点

粘贴生成的 Image 数据会立即 pack 到当前 `.blend`，临时文件随即删除。没有图片时，
原有的 `Ctrl+V` 行为会继续执行。此功能默认开启，可在 Extension Preferences 的
`Paste Clipboard Images` 中关闭。相同的剪贴板图片会复用已经 pack 的 Image 和
插件创建的 Texture，不会重复创建数据块。外部 Brush Asset 会在设置 Texture 前
复制为当前文件的 Local Brush Asset，使 Brush、Image 和 Texture 属于同一个
`.blend` 数据域。在 Vertex Paint 和 Texture Paint 中还会把 Brush Color 与
Unified Paint Color 设为纯白，避免贴图投射产生偏色。

使用 `Use OmooLab Startup` 并确认后，会把匹配版本的资源文件原子替换到当前
Blender 用户配置目录的 `config/startup.blend`。它不会立即打开这个文件，替换结果
会用于后续的 Blender 启动或新建默认文件。

Extension 启用时会把匹配版本的 keymap preset 同步到当前 Blender 用户目录的
`scripts/presets/keyconfig`。同步时会逐字节比较文件；文件缺失或内容不同时会原子
替换为 Extension 携带的版本，因此扩展更新后的 preset 会自动同步。同步过程不会
自动切换当前 keymap。

同步后的 preset 在 Extension 取消注册时仍会保留，因此 Blender 下次启动可以在
加载 Extension 之前恢复用户选择的 `Refined Industry Compatible`。

## 兼容性

- 最低支持 Blender 4.5
- 使用 Blender Extensions 范式
- 当前包含 4.5 和 5.2 两套资源

资源选择示例：

| Blender | 使用资源 |
| --- | --- |
| 4.5、4.6 | 4.5 |
| 5.0、5.1 | 4.5 |
| 5.2、5.3 | 5.2 |
| 6.0 | 5.2 |

## 项目结构

```text
.
├── pack.py
├── pyproject.toml
├── uv.lock
├── src/
│   └── startup/
│       ├── __init__.py
│       ├── blender_manifest.toml
│       ├── camera_bookmarks.py
│       ├── clipboard_image/
│       ├── phantom.py
│       ├── resource_loader.py
│       └── resources/
│           ├── 4.5/
│           │   ├── config/startup.blend
│           │   └── scripts/presets/keyconfig/
│           └── 5.2/
│               ├── config/startup.blend
│               └── scripts/presets/keyconfig/
└── tests/
```

版本资源内部保留 Blender 用户配置目录结构，因此它既可由 Extension 使用，也可
作为手动安装资源。

## 开发与构建

使用 Git Bash：

```bash
uv sync
uv run python -m unittest discover -s tests -v
uv run python pack.py
```

`pack.py` 从 manifest 读取扩展 ID 和版本，把 Extension 源目录打包为
`dist/startup-0.2.19.zip`。构建完成后，在 Blender 的 Extensions 设置中使用
`Install from Disk` 安装 ZIP。

如需单独验证 manifest，可在 Extension 源目录运行：

```bash
(
  cd src/startup
  blender --command extension validate
)
```

## 手动安装资源

也可以不安装 Extension，直接把对应版本资源目录中的内容复制到 Blender 用户配置
根目录。例如 `resources/5.2/config/startup.blend` 对应用户目录中的
`5.2/config/startup.blend`。

手动复制 `config/startup.blend` 会覆盖原有启动文件，操作前应先备份。Extension
中的 `Use OmooLab Startup` 会在确认后执行同样的替换。

