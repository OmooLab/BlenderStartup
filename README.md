# Blender Startup

Blender Startup 是 OmooLab 团队特供的 Blender 启动方案，目前提供 `Omoo Lab` Application Template。它在 Blender 的基础体验上加入了一套全新的快捷方式，以及多项开箱即用的小功能，让常用操作更顺手，也减少重复配置。

它以 Application Template 的形式安装，不会覆盖 Blender 原本的启动文件。需要原生 Blender 环境时，仍然可以照常使用默认的 General 模板。

完整的使用方法、快捷键设计与 Blender Default 差异参考见 [Blender Startup 文档](https://docs.omoolab.xyz/blender-startup/)。

## 下载

在 [Releases](https://github.com/OmooLab/BlenderStartup/releases) 页面下载最新安装包，根据 Blender 版本选择，文件名格式为 `BlenderStartup.v<版本号>.b<目标>.zip`：

- Blender 4.5 LTS：`BlenderStartup.v<版本号>.b45.zip`
- Blender 5.2 LTS：`BlenderStartup.v<版本号>.b52.zip`

## 安装

1. 下载对应 Blender 版本的 ZIP 安装包，不要解压。
2. 打开 Blender，点击左上角的 Blender 图标。
3. 选择 `Install Application Template...`。
4. 选择刚刚下载的 ZIP 文件并确认安装。

更新 Blender Startup 时，直接安装新版 ZIP 即可替换旧版本。

## 开始使用

安装后，可以通过以下任一方式进入模板：

- 在 Blender 启动画面中选择 `Omoo Lab`
- 进入 `File > New > Omoo Lab`

进入后即可使用 Blender Startup 提供的工作区、偏好设置、快捷方式和附加功能。

首次进入模板时，如尚未配置，Blender Startup 会加入 `OmooLab Extensions` 扩展仓库，地址为 `https://extensions.omoolab.xyz/`，并启用启动时检查更新。已有的同地址仓库不会重复添加，只会补充启用启动检查，其他设置保持不变。

Blender 5.2 还会加入三个 Remote Asset Library：

- `O Essentials`：`https://assets.omoolab.xyz/b52/O_Essentials/`
- `O Extra`：`https://assets.omoolab.xyz/b52/O_Extra/`
- `Stanford 3D Scanning`：`https://assets.omoolab.xyz/stanford-3d-scanning/`，导入方式为 Append

这些配置在切换到其他 Application Template 后仍会保留。

如需回到 Blender 默认环境，选择 `File > New > General` 即可。

## 快捷方式

Blender Startup 提供 `Refined Industry Compatible` Keymap。首次进入模板后，它会出现在：

`Edit > Preferences > Keymap > Preset`

选择 `Refined Industry Compatible` 即可启用。该 Keymap 不会自动替换你当前使用的快捷键方案。

## 实用功能

### Camera Bookmark

在 Camera View 中按 `Shift + \`` 打开书签菜单。你可以保存、更新和恢复相机视角，书签及其预览图会跟随当前 `.blend` 文件保存。

### Toggle Phantom

在 Object Mode 中打开右键菜单，选择 `Toggle Phantom`，可快速将对象切换为便于观察和穿透选择的半透明状态。再次执行即可恢复。

## 卸载

打开 Blender 的 Application Template 安装目录，删除 `Omoo_Lab` 文件夹即可。Blender Startup 不会修改或删除 Blender 默认的 General 模板。
