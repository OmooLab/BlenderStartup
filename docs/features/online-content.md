# OmooLab 在线内容

## OmooLab Extensions

首次进入 Omoo Lab 时，Blender Startup 会检查 Preferences 中是否已经存在同地址的扩展仓库：

`https://extensions.omoolab.xyz/`

如不存在则添加 `OmooLab Extensions`，并启用启动时同步。已经存在的同地址仓库不会重复创建，只会补充 `Sync on Startup`。

## Remote Asset Library

Blender 5.2 及以上会添加：

| 名称 | 地址 | 导入方式 |
| --- | --- | --- |
| O Essentials | `https://assets.omoolab.xyz/b52/O_Essentials/` | Pack |
| O Extra | `https://assets.omoolab.xyz/b52/O_Extra/` | Pack |
| Stanford 3D Scanning | `https://assets.omoolab.xyz/stanford-3d-scanning/` | Append |

Blender 4.5 不添加 Remote Asset Library。

## 持久性

这些内容写入 Blender 用户 Preferences。切换到 General 或其他 Application Template 后仍然保留，也不会因为 Omoo Lab 注销而自动删除。

如不希望保留，可以在 Blender Preferences 的 Extensions Repository 或 File Paths / Asset Libraries 中手动删除。
