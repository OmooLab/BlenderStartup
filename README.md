# OmooLab Startup

`OmooLab Startup` 是一个 Blender Extension，提供 OmooLab 的
`startup.blend` 和 keymap preset。

## 功能

- 在 `File > Defaults` 中增加 `Use OmooLab Startup`
- 在 Preferences 的 Keymap Presets 中增加
  `Refined Industry Compatible`
- 根据当前 Blender 版本自动选择不高于当前版本的最新资源

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
`dist/startup-0.1.0.zip`。构建完成后，在 Blender 的 Extensions 设置中使用
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

