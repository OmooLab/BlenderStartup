# 更新与卸载

## 更新

下载与当前 Blender 目标匹配的新 ZIP，重复 Application Template 安装流程即可替换旧版本。

改名前的模板使用不同目录，安装新版不会覆盖旧模板。升级后请删除旧模板文件夹，避免同时保留两个入口。

更新后建议：

1. 重新进入 `Omoo Lab`，让模板同步新版 Keymap Preset。
2. 在 Preferences 中确认当前仍选择 `Refined Industry Compatible`。
3. 查看[主要改动](../keymap/changes.md)和对应版本的[完整参考](../reference/index.md)。

## 回到原生 Blender

使用 `File > New > General`。Blender Startup 不会覆盖 Blender 默认 General 模板。

## 卸载

打开 Blender 的 Application Template 安装目录，删除 `Omoo_Lab` 文件夹。

已同步到用户配置中的 Keymap Preset、Extension Repository 和 Remote Asset Library 属于持久配置，不会随模板注销自动删除。如不再需要，可分别在 Blender Preferences 中删除。
