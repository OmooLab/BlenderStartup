# Blender Startup

Blender Startup 是 OmooLab 为 Blender 准备的启动方案，目前提供 `Omoo Lab` Application Template。它让你打开 Blender 就能使用整理好的工作区、偏好设置和快捷键，减少重复配置，也方便熟悉其他 DCC 的用户快速上手。


## 合理的设计

**符合用途的 Workspace**

`Omoo Lab` 按常见制作需求整理好 Workspace，一种工作一种布局，一「屋」一用。

- Layout 快速布局场景
- Geometry Nodes 几何沙箱
- Shading 材质沙箱
- Compositing 后期和背景
- Drawing GP画布
- Demo 展示用

**取长补短的工业兼容按键**

`Refined Industry Compatible` 保留 Blender 的 `G / S / R`、`MMB` 导航等核心手感，同时加入其他 DCC 常用的 `ALT + LMB / MMB / RMB` 导航和 `W / E / R` Transform 工具。熟悉 Blender 的人不用放弃已有习惯，来自其他 DCC 的人也能直接使用原有经验。

还有更多超级合理的快捷键！

**开箱即用的远程资产库和插件**

方便直接使用好用的节点组

## 下载与安装

**下载**

在 [Releases](https://github.com/OmooLab/BlenderStartup/releases) 下载与 Blender 版本匹配的安装包（不要解压）：

- Blender 4.5 lts 使用 `BlenderStartup.v<版本号>.b45.zip`
- Blender 5.2 lts 使用 `BlenderStartup.v<版本号>.b52.zip`

**安装 app template**

![install-app-template](assets/install-app-template.png)

点左上角的「Blender 图标」，选择 `Install Application Template...`，再选择刚下载的 ZIP。

**改变你的启动习惯**

![new-file](assets/new-file.png)

安装后从启动画面选择 `Omoo Lab`，或使用 `File > New > Omoo Lab`。

**选择快捷键**

快捷键方案需要手动启用：进入 `Edit > Preferences > Keymap > Preset`，选择 `Refined Industry Compatible`。

## 改变你的启动习惯

复制一份 Blender 快捷方式并命名为 `Omoo Lab`。右键打开“属性”，在“目标”末尾加上 `--app-template Omoo_Lab`：

```text
"C:\Program Files\Blender Foundation\Blender\blender.exe" --app-template Omoo_Lab
```

之后双击这个快捷方式，就会直接打开 `Omoo Lab` Application Template，不再经过模板选择。
