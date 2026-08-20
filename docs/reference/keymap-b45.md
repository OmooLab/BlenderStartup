# Blender 4.5 快捷键差异

本页由当前 `Refined Industry Compatible` Keymap 与同版本的 **Blender Default** 自动比较生成。Industry Compatible 不是比较基线。

<div class="keymap-summary">
<div><strong>446</strong>修改绑定</div>
<div><strong>176</strong>新增绑定</div>
<div><strong>17</strong>移除绑定</div>
<div><strong>67</strong>受影响 Keymap</div>
</div>

!!! note "怎样理解差异"

    “修改”表示同一个 Blender Operator 的触发方式或属性发生变化；“新增”和“移除”表示在相同编辑器 Keymap 中只存在于一侧。Blender 在运行时生成的工具 Keymap 不会因为没有出现在导出文件中就被记为删除。

基线来源：[Blender 官方 `b45` Blender Default 源文件](https://raw.githubusercontent.com/blender/blender/blender-v4.5-release/scripts/presets/keyconfig/keymap_data/blender_default.py)。

## 视图与通用操作

### 3D View

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>SHIFT + RMB</code> | `view3d.cursor3d` | 默认：<code>LMB + 点击</code> |
| 修改 | <code>CTRL + SHIFT + GRAVE</code> | `view3d.navigate` | 默认：<code>SHIFT + GRAVE</code> |
| 修改 | <code>LMB + 点击</code> | `view3d.select`<br><small>deselect_all=True</small> | 默认：<code>RMB + 点击</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB + 点击</code> | `view3d.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `view3d.select`<br><small>center=True, object=True</small> | 默认：<code>CTRL + RMB</code>；center=True, object=True |
| 修改 | <code>ALT + LMB + 点击</code> | `view3d.select`<br><small>enumerate=True</small> | 默认：<code>ALT + RMB</code>；enumerate=True |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `view3d.select`<br><small>toggle=True, center=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；toggle=True, center=True |
| 修改 | <code>CTRL + ALT + LMB + 点击</code> | `view3d.select`<br><small>center=True, enumerate=True</small> | 默认：<code>CTRL + ALT + RMB</code>；center=True, enumerate=True |
| 修改 | <code>SHIFT + ALT + LMB + 点击</code> | `view3d.select`<br><small>toggle=True, enumerate=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；toggle=True, enumerate=True |
| 修改 | <code>CTRL + SHIFT + ALT + LMB + 点击</code> | `view3d.select`<br><small>toggle=True, center=True, enumerate=True</small> | 默认：<code>CTRL + SHIFT + ALT + RMB</code>；toggle=True, center=True, enumerate=True |
| 修改 | <code>B</code> | `view3d.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + GRAVE</code> | `wm.context_toggle`<br><small>data_path='space_data.show_gizmo', active=False</small> | 默认：<code>CTRL + GRAVE</code>；data_path='space_data.show_gizmo' |
| 新增 | <code>SHIFT + RMB + 拖动</code> | `transform.translate`<br><small>cursor_transform=True, release_confirm=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>ALT + MMB</code> | `view3d.move` | Blender Default 中没有此绑定 |
| 新增 | <code>ALT + LMB</code> | `view3d.rotate` | Blender Default 中没有此绑定 |
| 新增 | <code>ALT + RMB</code> | `view3d.zoom` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `view3d.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>F + 双击</code> | `view3d.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ALT + LMB</code> | `view3d.move` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + ALT + LMB</code> | `view3d.zoom` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + LMB</code> | `view3d.cursor3d` | Blender Default 中没有此绑定 |
| 新增 | <code>T</code> | `wm.call_menu_pie`<br><small>name='VIEW3D_MT_orientations_pie'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + T</code> | `wm.call_menu_pie`<br><small>name='VIEW3D_MT_pivot_pie'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + ALT + Q + 可重复</code> | `view3d.view_roll`<br><small>angle=5.0, type='LEFT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + ALT + E + 可重复</code> | `view3d.view_roll`<br><small>angle=5.0, type='RIGHT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>ALT + GRAVE</code> | `view3d.camera_to_view` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + GRAVE</code> | `object.select_camera` | Blender Default 中没有此绑定 |
| 移除 | <code>RMB</code> | `view3d.select`<br><small>deselect_all=True, select_passthrough=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |

### 3D View Generic

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |

### 3D View Tool: Move

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>RMB</code> | `transform.translate` | Blender Default 中没有此绑定 |

### 3D View Tool: Rotate

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>RMB</code> | `transform.rotate` | Blender Default 中没有此绑定 |

### 3D View Tool: Scale

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>RMB</code> | `transform.resize` | Blender Default 中没有此绑定 |

### Frames

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>SPACE</code> | `screen.animation_play` | 默认：<code>SHIFT + SPACE</code> |
| 新增 | <code>CTRL + ALT + WHEEL DOWN</code> | `screen.keyframe_jump`<br><small>next=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + ALT + WHEEL UP</code> | `screen.keyframe_jump`<br><small>next=False</small> | Blender Default 中没有此绑定 |
| 新增 | <code>ESC</code> | `screen.frame_jump`<br><small>active=False</small> | Blender Default 中没有此绑定 |

### Screen

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + ALT + Q</code> | `screen.region_quadview`<br><small>active=False</small> | 默认：<code>CTRL + ALT + Q</code> |

### User Interface

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + SHIFT + F</code> | `ui.list_start_filter` | 默认：<code>CTRL + F</code> |
| 修改 | <code>CTRL + SHIFT + F</code> | `ui.view_start_filter` | 默认：<code>CTRL + F</code> |

### View2D

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>MMB</code> | `view2d.pan`<br><small>active=False</small> | 默认：<code>MMB</code> |
| 新增 | <code>ALT + MMB</code> | `view2d.pan` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ALT + LMB</code> | `view2d.pan` | Blender Default 中没有此绑定 |
| 新增 | <code>ALT + RMB</code> | `view2d.zoom` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + ALT + LMB</code> | `view2d.zoom` | Blender Default 中没有此绑定 |

### Window

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>A</code> | `wm.call_menu`<br><small>name='SCREEN_MT_user_menu'</small> | 默认：<code>Q</code>；name='SCREEN_MT_user_menu' |
| 修改 | <code>SHIFT + SPACE</code> | `wm.toolbar` | 默认：<code>SPACE</code> |
| 新增 | <code>ALT + GRAVE + 可重复</code> | `wm.context_toggle`<br><small>data_path='space_data.lock_camera'</small> | Blender Default 中没有此绑定 |

## 对象、模式与 Transform

### Object Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>A</code> | `object.select_all`<br><small>action='SELECT', active=False</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>ALT + W</code> | `object.location_clear`<br><small>clear_delta=False</small> | 默认：<code>ALT + G</code>；clear_delta=False |
| 修改 | <code>ALT + E</code> | `object.rotation_clear`<br><small>clear_delta=False</small> | 默认：<code>ALT + R</code>；clear_delta=False |
| 修改 | <code>ALT + R</code> | `object.scale_clear`<br><small>clear_delta=False</small> | 默认：<code>ALT + S</code>；clear_delta=False |
| 修改 | <code>CTRL + SHIFT + A</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_object_apply'</small> | 默认：<code>CTRL + A</code>；name='VIEW3D_MT_object_apply' |
| 修改 | <code>ONE</code> | `object.hide_collection`<br><small>collection_index=1, extend=False, active=False</small> | 默认：<code>ONE</code>；collection_index=1, extend=False |
| 修改 | <code>TWO</code> | `object.hide_collection`<br><small>collection_index=2, extend=False, active=False</small> | 默认：<code>TWO</code>；collection_index=2, extend=False |
| 修改 | <code>THREE</code> | `object.hide_collection`<br><small>collection_index=3, extend=False, active=False</small> | 默认：<code>THREE</code>；collection_index=3, extend=False |
| 修改 | <code>FOUR</code> | `object.hide_collection`<br><small>collection_index=4, extend=False, active=False</small> | 默认：<code>FOUR</code>；collection_index=4, extend=False |
| 修改 | <code>FIVE</code> | `object.hide_collection`<br><small>collection_index=5, extend=False, active=False</small> | 默认：<code>FIVE</code>；collection_index=5, extend=False |
| 修改 | <code>SIX</code> | `object.hide_collection`<br><small>collection_index=6, extend=False, active=False</small> | 默认：<code>SIX</code>；collection_index=6, extend=False |
| 修改 | <code>SEVEN</code> | `object.hide_collection`<br><small>collection_index=7, extend=False, active=False</small> | 默认：<code>SEVEN</code>；collection_index=7, extend=False |
| 修改 | <code>EIGHT</code> | `object.hide_collection`<br><small>collection_index=8, extend=False, active=False</small> | 默认：<code>EIGHT</code>；collection_index=8, extend=False |
| 修改 | <code>NINE</code> | `object.hide_collection`<br><small>collection_index=9, extend=False, active=False</small> | 默认：<code>NINE</code>；collection_index=9, extend=False |
| 修改 | <code>ZERO</code> | `object.hide_collection`<br><small>collection_index=10, extend=False, active=False</small> | 默认：<code>ZERO</code>；collection_index=10, extend=False |
| 修改 | <code>ALT + ONE</code> | `object.hide_collection`<br><small>collection_index=11, extend=False, active=False</small> | 默认：<code>ALT + ONE</code>；collection_index=11, extend=False |
| 修改 | <code>ALT + TWO</code> | `object.hide_collection`<br><small>collection_index=12, extend=False, active=False</small> | 默认：<code>ALT + TWO</code>；collection_index=12, extend=False |
| 修改 | <code>ALT + THREE</code> | `object.hide_collection`<br><small>collection_index=13, extend=False, active=False</small> | 默认：<code>ALT + THREE</code>；collection_index=13, extend=False |
| 修改 | <code>ALT + FOUR</code> | `object.hide_collection`<br><small>collection_index=14, extend=False, active=False</small> | 默认：<code>ALT + FOUR</code>；collection_index=14, extend=False |
| 修改 | <code>ALT + FIVE</code> | `object.hide_collection`<br><small>collection_index=15, extend=False, active=False</small> | 默认：<code>ALT + FIVE</code>；collection_index=15, extend=False |
| 修改 | <code>ALT + SIX</code> | `object.hide_collection`<br><small>collection_index=16, extend=False, active=False</small> | 默认：<code>ALT + SIX</code>；collection_index=16, extend=False |
| 修改 | <code>ALT + SEVEN</code> | `object.hide_collection`<br><small>collection_index=17, extend=False, active=False</small> | 默认：<code>ALT + SEVEN</code>；collection_index=17, extend=False |
| 修改 | <code>ALT + EIGHT</code> | `object.hide_collection`<br><small>collection_index=18, extend=False, active=False</small> | 默认：<code>ALT + EIGHT</code>；collection_index=18, extend=False |
| 修改 | <code>ALT + NINE</code> | `object.hide_collection`<br><small>collection_index=19, extend=False, active=False</small> | 默认：<code>ALT + NINE</code>；collection_index=19, extend=False |
| 修改 | <code>ALT + ZERO</code> | `object.hide_collection`<br><small>collection_index=20, extend=False, active=False</small> | 默认：<code>ALT + ZERO</code>；collection_index=20, extend=False |
| 修改 | <code>SHIFT + ONE</code> | `object.hide_collection`<br><small>collection_index=1, extend=True, active=False</small> | 默认：<code>SHIFT + ONE</code>；collection_index=1, extend=True |
| 修改 | <code>SHIFT + TWO</code> | `object.hide_collection`<br><small>collection_index=2, extend=True, active=False</small> | 默认：<code>SHIFT + TWO</code>；collection_index=2, extend=True |
| 修改 | <code>SHIFT + THREE</code> | `object.hide_collection`<br><small>collection_index=3, extend=True, active=False</small> | 默认：<code>SHIFT + THREE</code>；collection_index=3, extend=True |
| 修改 | <code>SHIFT + FOUR</code> | `object.hide_collection`<br><small>collection_index=4, extend=True, active=False</small> | 默认：<code>SHIFT + FOUR</code>；collection_index=4, extend=True |
| 修改 | <code>SHIFT + FIVE</code> | `object.hide_collection`<br><small>collection_index=5, extend=True, active=False</small> | 默认：<code>SHIFT + FIVE</code>；collection_index=5, extend=True |
| 修改 | <code>SHIFT + SIX</code> | `object.hide_collection`<br><small>collection_index=6, extend=True, active=False</small> | 默认：<code>SHIFT + SIX</code>；collection_index=6, extend=True |
| 修改 | <code>SHIFT + SEVEN</code> | `object.hide_collection`<br><small>collection_index=7, extend=True, active=False</small> | 默认：<code>SHIFT + SEVEN</code>；collection_index=7, extend=True |
| 修改 | <code>SHIFT + EIGHT</code> | `object.hide_collection`<br><small>collection_index=8, extend=True, active=False</small> | 默认：<code>SHIFT + EIGHT</code>；collection_index=8, extend=True |
| 修改 | <code>SHIFT + NINE</code> | `object.hide_collection`<br><small>collection_index=9, extend=True, active=False</small> | 默认：<code>SHIFT + NINE</code>；collection_index=9, extend=True |
| 修改 | <code>SHIFT + ZERO</code> | `object.hide_collection`<br><small>collection_index=10, extend=True, active=False</small> | 默认：<code>SHIFT + ZERO</code>；collection_index=10, extend=True |
| 修改 | <code>SHIFT + ALT + ONE</code> | `object.hide_collection`<br><small>collection_index=11, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + ONE</code>；collection_index=11, extend=True |
| 修改 | <code>SHIFT + ALT + TWO</code> | `object.hide_collection`<br><small>collection_index=12, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + TWO</code>；collection_index=12, extend=True |
| 修改 | <code>SHIFT + ALT + THREE</code> | `object.hide_collection`<br><small>collection_index=13, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + THREE</code>；collection_index=13, extend=True |
| 修改 | <code>SHIFT + ALT + FOUR</code> | `object.hide_collection`<br><small>collection_index=14, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + FOUR</code>；collection_index=14, extend=True |
| 修改 | <code>SHIFT + ALT + FIVE</code> | `object.hide_collection`<br><small>collection_index=15, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + FIVE</code>；collection_index=15, extend=True |
| 修改 | <code>SHIFT + ALT + SIX</code> | `object.hide_collection`<br><small>collection_index=16, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + SIX</code>；collection_index=16, extend=True |
| 修改 | <code>SHIFT + ALT + SEVEN</code> | `object.hide_collection`<br><small>collection_index=17, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + SEVEN</code>；collection_index=17, extend=True |
| 修改 | <code>SHIFT + ALT + EIGHT</code> | `object.hide_collection`<br><small>collection_index=18, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + EIGHT</code>；collection_index=18, extend=True |
| 修改 | <code>SHIFT + ALT + NINE</code> | `object.hide_collection`<br><small>collection_index=19, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + NINE</code>；collection_index=19, extend=True |
| 修改 | <code>SHIFT + ALT + ZERO</code> | `object.hide_collection`<br><small>collection_index=20, extend=True, active=False</small> | 默认：<code>SHIFT + ALT + ZERO</code>；collection_index=20, extend=True |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_object_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_object_context_menu' |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `object.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + A</code> | `object.select_all`<br><small>action='SELECT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `object.duplicate_move` | Blender Default 中没有此绑定 |
| 新增 | <code>ONE</code> | `object.mode_set_with_submode`<br><small>mode='EDIT', toggle=False, mesh_select_mode={'VERT'}</small> | Blender Default 中没有此绑定 |
| 新增 | <code>TWO</code> | `object.mode_set_with_submode`<br><small>mode='EDIT', toggle=False, mesh_select_mode={'EDGE'}</small> | Blender Default 中没有此绑定 |
| 新增 | <code>THREE</code> | `object.mode_set_with_submode`<br><small>mode='EDIT', mesh_select_mode={'FACE'}</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + ONE</code> | `object.select_grouped` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + TWO</code> | `object.select_linked` | Blender Default 中没有此绑定 |
| 新增 | <code>TAB + 松开</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_add'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ONE</code> | `object.mode_set`<br><small>mode='SCULPT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ONE</code> | `object.mode_set`<br><small>mode='PAINT_GREASE_PENCIL'</small> | Blender Default 中没有此绑定 |

### Object Non-modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>TAB</code> | `object.mode_set`<br><small>mode='EDIT', toggle=True, active=False</small> | 默认：<code>TAB</code>；mode='EDIT', toggle=True |
| 修改 | <code>TAB + 拖动</code> | `view3d.object_mode_pie_or_toggle` | 默认：<code>CTRL + TAB</code> |
| 新增 | <code>LMB + 双击</code> | `object.transfer_mode` | Blender Default 中没有此绑定 |
| 新增 | <code>ESC</code> | `object.mode_set`<br><small>mode='OBJECT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>FOUR</code> | `object.mode_set`<br><small>mode='OBJECT'</small> | Blender Default 中没有此绑定 |

### Pose

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + SHIFT + A</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_pose_apply'</small> | 默认：<code>CTRL + A</code>；name='VIEW3D_MT_pose_apply' |
| 修改 | <code>ALT + E</code> | `pose.rot_clear` | 默认：<code>ALT + R</code> |
| 修改 | <code>ALT + W</code> | `pose.loc_clear` | 默认：<code>ALT + G</code> |
| 修改 | <code>ALT + R</code> | `pose.scale_clear` | 默认：<code>ALT + S</code> |
| 修改 | <code>CTRL + A</code> | `pose.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_pose_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_pose_context_menu' |
| 新增 | <code>CTRL + F</code> | `pose.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Transform Modal Map

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>Q</code> | `AXIS_X` | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `AXIS_Y` | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `AXIS_Z` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + Q</code> | `PLANE_X` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + W</code> | `PLANE_Y` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + E</code> | `PLANE_Z` | Blender Default 中没有此绑定 |

## 建模、雕刻与绘制

### Armature

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + A</code> | `armature.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + LMB + 点击</code> | `armature.shortest_path_pick` | 默认：<code>CTRL + RMB</code> |
| 修改 | <code>E</code> | `armature.extrude_move`<br><small>active=False</small> | 默认：<code>E</code> |
| 修改 | <code>CTRL + RMB + 点击</code> | `armature.click_extrude` | 默认：<code>CTRL + LMB + 点击</code> |
| 修改 | <code>F</code> | `armature.fill`<br><small>active=False</small> | 默认：<code>F</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_armature_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_armature_context_menu' |
| 新增 | <code>CTRL + F</code> | `armature.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `armature.duplicate_move` | Blender Default 中没有此绑定 |

### Curve

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + RMB + 点击</code> | `curve.vertex_add` | 默认：<code>CTRL + LMB + 点击</code> |
| 修改 | <code>CTRL + A</code> | `curve.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + LMB + 点击</code> | `curve.shortest_path_pick` | 默认：<code>CTRL + RMB</code> |
| 修改 | <code>E</code> | `curve.extrude_move`<br><small>active=False</small> | 默认：<code>E</code> |
| 修改 | <code>F</code> | `curve.make_segment`<br><small>active=False</small> | 默认：<code>F</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_curve_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_edit_curve_context_menu' |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `curve.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `curve.duplicate_move` | Blender Default 中没有此绑定 |

### Curves

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + A</code> | `curves.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>E</code> | `curves.extrude_move`<br><small>active=False</small> | 默认：<code>E</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_curves_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_edit_curves_context_menu' |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `curves.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `curves.duplicate_move` | Blender Default 中没有此绑定 |

### Grease Pencil

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>CTRL + F</code> | `grease_pencil.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Grease Pencil Edit Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>F</code> | `grease_pencil.cyclical_set`<br><small>type='CLOSE', subdivide_cyclic_segment=True, active=False</small> | 默认：<code>F</code>；type='CLOSE', subdivide_cyclic_segment=True |
| 修改 | <code>E</code> | `grease_pencil.extrude_move`<br><small>active=False</small> | 默认：<code>E</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_greasepencil_edit_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_greasepencil_edit_context_menu' |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `grease_pencil.duplicate_move` | Blender Default 中没有此绑定 |

### Grease Pencil Paint Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>B</code> | `grease_pencil.erase_box`<br><small>wait_for_input=True, active=False</small> | 默认：<code>B</code>；wait_for_input=True |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_paint.brush.size'</small> | 默认：<code>F</code>；data_path_primary='tool_settings.gpencil_paint.brush.size' |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_paint.brush.strength'</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.gpencil_paint.brush.strength' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_gpencil_paint'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_gpencil_paint' |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_greasepencil_draw_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_greasepencil_draw_context_menu' |
| 新增 | <code>SHIFT + LMB + 双击</code> | `paint.sample_color` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + ALT + LMB</code> | `grease_pencil.erase_lasso` | Blender Default 中没有此绑定 |

### Grease Pencil Sculpt Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_sculpt_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.gpencil_sculpt_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_sculpt_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.gpencil_sculpt_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_gpencil_sculpt'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_gpencil_sculpt' |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_greasepencil_sculpt_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_greasepencil_sculpt_context_menu' |
| 新增 | <code>G</code> | `brush.asset_activate`<br><small>asset_library_type='ESSENTIALS', asset_library_identifier='', relative_asset_identifier='brushes/essentials_brushes-gp_sculpt.blend/Brush/Grab'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |

### Grease Pencil Selection

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `grease_pencil.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |

### Grease Pencil Vertex Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.gpencil_vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.gpencil_vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_greasepencil_vertex_paint_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_greasepencil_vertex_paint_context_menu' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_gpencil_vertex'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_gpencil_vertex' |

### Grease Pencil Weight Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.gpencil_weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.gpencil_weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | <code>CTRL + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.gpencil_weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False, active=False</small> | 默认：<code>CTRL + F</code>；data_path_primary='tool_settings.gpencil_weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_greasepencil_weight_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_greasepencil_weight_context_menu' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_gpencil_weight'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_gpencil_weight' |
| 新增 | <code>ALT + LMB</code> | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ALT + LMB</code> | `view3d.select`<br><small>toggle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + LMB</code> | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + LMB + 双击</code> | `grease_pencil.weight_sample` | Blender Default 中没有此绑定 |

### Lattice

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + A</code> | `lattice.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_lattice_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_edit_lattice_context_menu' |
| 新增 | <code>CTRL + F</code> | `lattice.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Mesh

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + A</code> | `transform.skin_resize`<br><small>active=False</small> | 默认：<code>CTRL + A</code> |
| 修改 | <code>ALT + LMB + 点击</code> | `mesh.loop_select` | 默认：<code>ALT + RMB</code> |
| 修改 | <code>SHIFT + ALT + LMB + 点击</code> | `mesh.loop_select`<br><small>toggle=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + ALT + LMB + 点击</code> | `mesh.edgering_select` | 默认：<code>CTRL + ALT + RMB</code> |
| 修改 | <code>CTRL + SHIFT + ALT + LMB + 点击</code> | `mesh.edgering_select`<br><small>toggle=True</small> | 默认：<code>CTRL + SHIFT + ALT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `mesh.shortest_path_pick`<br><small>use_fill=False</small> | 默认：<code>CTRL + RMB</code>；use_fill=False |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `mesh.shortest_path_pick`<br><small>use_fill=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；use_fill=True |
| 修改 | <code>CTRL + A</code> | `mesh.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>E</code> | `view3d.edit_mesh_extrude_move_normal`<br><small>active=False</small> | 默认：<code>E</code> |
| 修改 | <code>F + 可重复</code> | `mesh.edge_face_add`<br><small>active=False</small> | 默认：<code>F + 可重复</code> |
| 修改 | <code>CTRL + RMB + 点击</code> | `mesh.dupli_extrude_cursor`<br><small>rotate_source=True</small> | 默认：<code>CTRL + LMB + 点击</code>；rotate_source=True |
| 修改 | <code>CTRL + SHIFT + RMB + 点击</code> | `mesh.dupli_extrude_cursor`<br><small>rotate_source=False</small> | 默认：<code>CTRL + SHIFT + LMB + 点击</code>；rotate_source=False |
| 修改 | <code>CTRL + F</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_mesh_faces', active=False</small> | 默认：<code>CTRL + F</code>；name='VIEW3D_MT_edit_mesh_faces' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_mesh_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_edit_mesh_context_menu' |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `mesh.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `mesh.duplicate_move` | Blender Default 中没有此绑定 |

### Metaball

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>CTRL + A</code> | `mball.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_edit_metaball_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_edit_metaball_context_menu' |
| 新增 | <code>CTRL + F</code> | `mball.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `mball.duplicate_move` | Blender Default 中没有此绑定 |

### Paint Curve

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + RMB</code> | `paintcurve.add_point_slide` | 默认：<code>CTRL + LMB</code> |
| 修改 | <code>LMB</code> | `paintcurve.select` | 默认：<code>RMB</code> |
| 修改 | <code>SHIFT + LMB</code> | `paintcurve.select`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>RMB</code> | `paintcurve.slide`<br><small>align=False</small> | 默认：<code>LMB</code>；align=False |
| 修改 | <code>SHIFT + RMB</code> | `paintcurve.slide`<br><small>align=True</small> | 默认：<code>SHIFT + LMB</code>；align=True |
| 修改 | <code>CTRL + A</code> | `paintcurve.select`<br><small>toggle=True</small> | 默认：<code>A</code>；toggle=True |
| 修改 | <code>CTRL + SHIFT + RMB</code> | `paintcurve.cursor` | 默认：<code>CTRL + SHIFT + LMB</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |

### Paint Vertex Selection (Weight, Vertex)

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `paint.vert_select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + SHIFT + ALT + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>B</code> | `view3d.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 新增 | <code>CTRL + F</code> | `paint.vert_select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Particle

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `particle.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.particle_edit.brush.size'</small> | 默认：<code>F</code>；data_path_primary='tool_settings.particle_edit.brush.size' |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.particle_edit.brush.strength'</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.particle_edit.brush.strength' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='VIEW3D_MT_particle_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_MT_particle_context_menu' |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 新增 | <code>CTRL + F</code> | `particle.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Point Cloud

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>A</code> | `pointcloud.select_all`<br><small>action='SELECT', active=False</small> | 默认：<code>A</code>；action='SELECT' |

### Sculpt

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>SHIFT + A</code> | `sculpt.expand`<br><small>target='MASK', falloff_type='GEODESIC', invert=False, use_mask_preserve=True, use_auto_mask=False</small> | 默认：<code>SHIFT + A</code>；target='MASK', falloff_type='GEODESIC', invert=False, use_auto_mask=False, use_mask_preserve=True |
| 修改 | <code>B</code> | `paint.mask_box_gesture`<br><small>mode='VALUE', value=0.0, active=False</small> | 默认：<code>B</code>；mode='VALUE', value=0.0 |
| 修改 | <code>D</code> | `sculpt.dyntopo_detail_size_edit` | 默认：<code>R</code> |
| 修改 | <code>CTRL + D</code> | `sculpt.detail_flood_fill` | 默认：<code>CTRL + R</code> |
| 修改 | <code>CTRL + D</code> | `object.voxel_remesh` | 默认：<code>CTRL + R</code> |
| 修改 | <code>D</code> | `object.voxel_size_edit` | 默认：<code>R</code> |
| 修改 | <code>X</code> | `paint.brush_colors_flip`<br><small>active=False</small> | 默认：<code>X</code> |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | <code>CTRL + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.sculpt.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False, active=False</small> | 默认：<code>CTRL + F</code>；data_path_primary='tool_settings.sculpt.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_sculpt_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_sculpt_context_menu' |
| 修改 | <code>V</code> | `brush.asset_activate`<br><small>asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Draw', active=False</small> | 默认：<code>V</code>；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Draw' |
| 修改 | <code>S</code> | `brush.asset_activate`<br><small>asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Smooth', active=False</small> | 默认：<code>S</code>；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Smooth' |
| 修改 | <code>SHIFT + T</code> | `brush.asset_activate`<br><small>asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Scrape/Fill', active=False</small> | 默认：<code>SHIFT + T</code>；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Scrape/Fill' |
| 修改 | <code>C</code> | `brush.asset_activate`<br><small>asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Clay Strips', active=False</small> | 默认：<code>C</code>；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Clay Strips' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_sculpt'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_sculpt' |
| 修改 | <code>CTRL + SHIFT + RMB</code> | `paint.mask_lasso_gesture`<br><small>value=1.0</small> | 默认：<code>CTRL + SHIFT + LMB</code>；value=1.0 |
| 修改 | <code>CTRL + RMB</code> | `paint.mask_lasso_gesture`<br><small>value=0.0</small> | 默认：<code>CTRL + SHIFT + ALT + LMB</code>；value=0.0 |
| 新增 | <code>CTRL + F</code> | `paint.mask_flood_fill`<br><small>mode='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + A</code> | `paint.mask_flood_fill`<br><small>mode='VALUE'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + D</code> | `sculpt.dynamic_topology_toggle` | Blender Default 中没有此绑定 |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.box_mask', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + LMB + 双击</code> | `sculpt.sample_color` | Blender Default 中没有此绑定 |
| 新增 | <code>C</code> | `wm.tool_set_by_id`<br><small>name='builtin.box_face_set', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>X</code> | `wm.tool_set_by_id`<br><small>name='builtin.lasso_trim', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>V</code> | `wm.tool_set_by_id`<br><small>name='builtin.lasso_hide', cycle=True</small> | Blender Default 中没有此绑定 |

### Sculpt Curves

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.curves_sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.curves_sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.curves_sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.curves_sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False |
| 修改 | <code>CTRL + A</code> | `curves.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>R</code> | `sculpt_curves.min_distance_edit` | 默认：<code>R</code> |
| 修改 | <code>SHIFT + A</code> | `sculpt_curves.select_grow` | 默认：<code>SHIFT + A</code> |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_sculpt_curves'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_sculpt_curves' |
| 新增 | <code>CTRL + F</code> | `curves.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Sculpt Expand Modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>B</code> | `BRUSH_GRADIENT_TOGGLE`<br><small>active=False</small> | 默认：<code>B</code> |

### Vertex Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | <code>CTRL + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.vertex_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False, active=False</small> | 默认：<code>CTRL + F</code>；data_path_primary='tool_settings.vertex_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_paint_vertex_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_paint_vertex_context_menu' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_vertex_paint'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_vertex_paint' |
| 新增 | <code>SHIFT + LMB + 双击</code> | `paint.sample_color` | Blender Default 中没有此绑定 |

### Weight Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False</small> | 默认：<code>F</code>；data_path_primary='tool_settings.weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | <code>CTRL + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False, active=False</small> | 默认：<code>CTRL + F</code>；data_path_primary='tool_settings.weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_paint_weight_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_paint_weight_context_menu' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_weight_paint'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_weight_paint' |
| 新增 | <code>ALT + LMB</code> | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + ALT + LMB</code> | `view3d.select`<br><small>toggle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + LMB</code> | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + LMB + 双击</code> | `paint.weight_sample` | Blender Default 中没有此绑定 |

## 节点

### Node Editor

上下文：`NODE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 点击</code> | `node.select`<br><small>select_passthrough=True</small> | 默认：<code>LMB</code>；select_passthrough=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `node.select` | 默认：<code>CTRL + LMB</code> |
| 修改 | <code>ALT + LMB + 点击</code> | `node.select` | 默认：<code>ALT + LMB</code> |
| 修改 | <code>CTRL + ALT + LMB + 点击</code> | `node.select` | 默认：<code>CTRL + ALT + LMB</code> |
| 修改 | <code>SHIFT + LMB + 点击</code> | `node.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + LMB</code>；toggle=True |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `node.select`<br><small>toggle=True</small> | 默认：<code>CTRL + SHIFT + LMB</code>；toggle=True |
| 修改 | <code>SHIFT + ALT + LMB + 点击</code> | `node.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + ALT + LMB</code>；toggle=True |
| 修改 | <code>CTRL + SHIFT + ALT + LMB + 点击</code> | `node.select`<br><small>toggle=True</small> | 默认：<code>CTRL + SHIFT + ALT + LMB</code>；toggle=True |
| 修改 | <code>LMB + 拖动</code> | `node.select_box`<br><small>tweak=True</small> | 默认：<code>RMB + 拖动</code>；tweak=True |
| 修改 | <code>B</code> | `node.select_box`<br><small>tweak=False, active=False</small> | 默认：<code>B</code>；tweak=False |
| 修改 | <code>ALT + RMB</code> | `node.backimage_sample` | 默认：<code>ALT + LMB</code> |
| 修改 | <code>F</code> | `node.link_make`<br><small>replace=False, active=False</small> | 默认：<code>J</code>；replace=False |
| 修改 | <code>SHIFT + F</code> | `node.link_make`<br><small>replace=True, active=False</small> | 默认：<code>SHIFT + J</code>；replace=True |
| 修改 | <code>F</code> | `node.join_named`<br><small>active=False</small> | 默认：<code>F</code> |
| 修改 | <code>CTRL + A</code> | `node.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + SHIFT + F</code> | `node.find_node` | 默认：<code>CTRL + F</code> |
| 修改 | <code>TAB</code> | `node.group_edit`<br><small>exit=False, active=False</small> | 默认：<code>TAB</code>；exit=False |
| 修改 | <code>CTRL + TAB</code> | `node.group_edit`<br><small>exit=True, active=False</small> | 默认：<code>CTRL + TAB</code>；exit=True |
| 修改 | <code>LMB + 拖动</code> | `transform.translate`<br><small>view2d_edge_pan=True, release_confirm=True</small> | 默认：<code>LMB + 拖动</code>；release_confirm=True, view2d_edge_pan=True |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>ALT + RMB + 拖动</code> | `node.move_detach_links_release`<br><small>NODE_OT_translate_attach=[('TRANSFORM_OT_translate', [('view2d_edge_pan', True)])]</small> | 默认：<code>ALT + LMB + 拖动</code>；NODE_OT_translate_attach=[('TRANSFORM_OT_translate', [('view2d_edge_pan', True)])] |
| 修改 | <code>ALT + LMB + 拖动</code> | `node.move_detach_links`<br><small>TRANSFORM_OT_translate=[('view2d_edge_pan', True)]</small> | 默认：<code>ALT + RMB + 拖动</code>；TRANSFORM_OT_translate=[('view2d_edge_pan', True)] |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='NODE_MT_context_menu'</small> | 默认：<code>W</code>；name='NODE_MT_context_menu' |
| 修改 | <code>MMB</code> | `transform.translate` | 默认：<code>RMB + 拖动</code>；release_confirm=True, view2d_edge_pan=True |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>F + 双击</code> | `node.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `node.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `node.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + LMB + 双击</code> | `node.backimage_sample` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `node.duplicate_move` | Blender Default 中没有此绑定 |
| 新增 | <code>LMB + 双击</code> | `node.group_edit` | Blender Default 中没有此绑定 |
| 新增 | <code>ESC</code> | `node.group_edit`<br><small>exit=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>TAB</code> | `wm.call_menu`<br><small>name='NODE_MT_add'</small> | Blender Default 中没有此绑定 |
| 移除 | <code>RMB</code> | `node.select`<br><small>select_passthrough=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>CTRL + RMB</code> | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>ALT + RMB</code> | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>CTRL + ALT + RMB</code> | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>SHIFT + RMB</code> | `node.select`<br><small>toggle=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>CTRL + SHIFT + RMB</code> | `node.select`<br><small>toggle=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>SHIFT + ALT + RMB</code> | `node.select`<br><small>toggle=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>CTRL + SHIFT + ALT + RMB</code> | `node.select`<br><small>toggle=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>RMB + 点击</code> | `node.select`<br><small>deselect_all=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>LMB + 点击</code> | `node.select`<br><small>deselect_all=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>RMB + 拖动</code> | `node.translate_attach`<br><small>TRANSFORM_OT_translate=[('view2d_edge_pan', True)]</small> | 当前 Keymap 中没有此 Blender Default 绑定 |

### Node Generic

上下文：`NODE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |

## 动画

### Animation Channels

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + SHIFT + F</code> | `anim.channels_select_filter` | 默认：<code>CTRL + F</code> |
| 修改 | <code>CTRL + A</code> | `anim.channels_select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `anim.channels_select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='DOPESHEET_MT_channel_context_menu'</small> | 默认：<code>W</code>；name='DOPESHEET_MT_channel_context_menu' |
| 新增 | <code>F</code> | `anim.channels_view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `anim.channels_select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Clip Graph Editor

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB</code> | `clip.graph_select` | 默认：<code>RMB</code> |
| 修改 | <code>SHIFT + LMB</code> | `clip.graph_select`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>CTRL + A</code> | `clip.graph_select_all_markers`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `clip.graph_select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>SHIFT + RMB</code> | `clip.change_frame` | 默认：<code>LMB</code> |
| 新增 | <code>CTRL + F</code> | `clip.graph_select_all_markers`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Dopesheet

上下文：`DOPESHEET_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB</code> | `action.clickselect`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>ALT + LMB</code> | `action.clickselect`<br><small>column=True</small> | 默认：<code>ALT + RMB</code>；column=True |
| 修改 | <code>SHIFT + LMB</code> | `action.clickselect`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>SHIFT + ALT + LMB</code> | `action.clickselect`<br><small>extend=True, column=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；extend=True, column=True |
| 修改 | <code>CTRL + ALT + LMB</code> | `action.clickselect`<br><small>channel=True</small> | 默认：<code>CTRL + ALT + RMB</code>；channel=True |
| 修改 | <code>CTRL + SHIFT + ALT + LMB</code> | `action.clickselect`<br><small>extend=True, channel=True</small> | 默认：<code>CTRL + SHIFT + ALT + RMB</code>；extend=True, channel=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `action.select_leftright`<br><small>mode='CHECK'</small> | 默认：<code>CTRL + RMB + 点击</code>；mode='CHECK' |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `action.select_leftright`<br><small>mode='CHECK', extend=True</small> | 默认：<code>CTRL + SHIFT + RMB + 点击</code>；mode='CHECK', extend=True |
| 修改 | <code>CTRL + A</code> | `action.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `action.select_box`<br><small>axis_range=False, active=False</small> | 默认：<code>B</code>；axis_range=False |
| 修改 | <code>ALT + B</code> | `action.select_box`<br><small>axis_range=True, active=False</small> | 默认：<code>ALT + B</code>；axis_range=True |
| 修改 | <code>LMB + 拖动</code> | `action.select_box`<br><small>mode='SET', tweak=True</small> | 默认：<code>RMB + 拖动</code>；tweak=True, mode='SET' |
| 修改 | <code>SHIFT + LMB + 拖动</code> | `action.select_box`<br><small>mode='ADD', tweak=True</small> | 默认：<code>SHIFT + RMB + 拖动</code>；tweak=True, mode='ADD' |
| 修改 | <code>CTRL + LMB + 拖动</code> | `action.select_box`<br><small>mode='SUB', tweak=True</small> | 默认：<code>CTRL + RMB + 拖动</code>；tweak=True, mode='SUB' |
| 修改 | <code>CTRL + RMB + 拖动</code> | `action.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `action.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + SHIFT + F</code> | `anim.channels_select_filter` | 默认：<code>CTRL + F</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.transform`<br><small>mode='TIME_TRANSLATE'</small> | 默认：<code>RMB + 拖动</code>；mode='TIME_TRANSLATE' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='DOPESHEET_MT_context_menu'</small> | 默认：<code>W</code>；name='DOPESHEET_MT_context_menu' |
| 修改 | <code>SHIFT + RMB</code> | `anim.change_frame` | 默认：<code>LMB</code> |
| 新增 | <code>F + 双击</code> | `view3d.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `action.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `action.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `action.duplicate_move` | Blender Default 中没有此绑定 |

### Graph Editor

上下文：`GRAPH_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB</code> | `graph.clickselect`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>ALT + LMB</code> | `graph.clickselect`<br><small>column=True</small> | 默认：<code>ALT + RMB</code>；column=True |
| 修改 | <code>SHIFT + LMB</code> | `graph.clickselect`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>SHIFT + ALT + LMB</code> | `graph.clickselect`<br><small>extend=True, column=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；extend=True, column=True |
| 修改 | <code>CTRL + ALT + LMB</code> | `graph.clickselect`<br><small>curves=True</small> | 默认：<code>CTRL + ALT + RMB</code>；curves=True |
| 修改 | <code>CTRL + SHIFT + ALT + LMB</code> | `graph.clickselect`<br><small>extend=True, curves=True</small> | 默认：<code>CTRL + SHIFT + ALT + RMB</code>；extend=True, curves=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `graph.select_leftright`<br><small>mode='CHECK'</small> | 默认：<code>CTRL + RMB + 点击</code>；mode='CHECK' |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `graph.select_leftright`<br><small>mode='CHECK', extend=True</small> | 默认：<code>CTRL + SHIFT + RMB + 点击</code>；mode='CHECK', extend=True |
| 修改 | <code>CTRL + A</code> | `graph.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `graph.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>ALT + B</code> | `graph.select_box`<br><small>axis_range=True, active=False</small> | 默认：<code>ALT + B</code>；axis_range=True |
| 修改 | <code>LMB + 拖动</code> | `graph.select_box`<br><small>tweak=True, mode='SET'</small> | 默认：<code>RMB + 拖动</code>；tweak=True, mode='SET' |
| 修改 | <code>SHIFT + LMB + 拖动</code> | `graph.select_box`<br><small>tweak=True, mode='ADD'</small> | 默认：<code>SHIFT + RMB + 拖动</code>；tweak=True, mode='ADD' |
| 修改 | <code>CTRL + LMB + 拖动</code> | `graph.select_box`<br><small>tweak=True, mode='SUB'</small> | 默认：<code>CTRL + RMB + 拖动</code>；tweak=True, mode='SUB' |
| 修改 | <code>CTRL + RMB + 拖动</code> | `graph.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `graph.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + RMB + 点击</code> | `graph.click_insert` | 默认：<code>CTRL + LMB + 点击</code> |
| 修改 | <code>CTRL + SHIFT + RMB + 点击</code> | `graph.click_insert`<br><small>extend=True</small> | 默认：<code>CTRL + SHIFT + LMB + 点击</code>；extend=True |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='GRAPH_MT_context_menu'</small> | 默认：<code>W</code>；name='GRAPH_MT_context_menu' |
| 修改 | <code>SHIFT + RMB</code> | `graph.cursor_set` | 默认：<code>LMB</code> |
| 新增 | <code>F + 双击</code> | `graph.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `graph.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `graph.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `graph.duplicate_move` | Blender Default 中没有此绑定 |

### Markers

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 拖动</code> | `marker.move`<br><small>tweak=True</small> | 默认：<code>RMB + 拖动</code>；tweak=True |
| 修改 | <code>LMB</code> | `marker.select` | 默认：<code>RMB</code> |
| 修改 | <code>SHIFT + LMB</code> | `marker.select`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>CTRL + LMB</code> | `marker.select`<br><small>camera=True</small> | 默认：<code>CTRL + RMB</code>；camera=True |
| 修改 | <code>CTRL + SHIFT + LMB</code> | `marker.select`<br><small>extend=True, camera=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；extend=True, camera=True |
| 修改 | <code>LMB + 拖动</code> | `marker.select_box`<br><small>tweak=True</small> | 默认：<code>RMB + 拖动</code>；tweak=True |
| 修改 | <code>SHIFT + LMB + 拖动</code> | `marker.select_box`<br><small>mode='ADD', tweak=True</small> | 默认：<code>SHIFT + RMB + 拖动</code>；tweak=True, mode='ADD' |
| 修改 | <code>CTRL + LMB + 拖动</code> | `marker.select_box`<br><small>mode='SUB', tweak=True</small> | 默认：<code>CTRL + RMB + 拖动</code>；tweak=True, mode='SUB' |
| 修改 | <code>B</code> | `marker.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + A</code> | `marker.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 新增 | <code>CTRL + F</code> | `marker.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `marker.duplicate` | Blender Default 中没有此绑定 |

### NLA Editor

上下文：`NLA_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB</code> | `nla.click_select`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB</code> | `nla.click_select`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `nla.select_leftright`<br><small>mode='CHECK'</small> | 默认：<code>CTRL + RMB + 点击</code>；mode='CHECK' |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `nla.select_leftright`<br><small>mode='CHECK', extend=True</small> | 默认：<code>CTRL + SHIFT + RMB + 点击</code>；mode='CHECK', extend=True |
| 修改 | <code>CTRL + A</code> | `nla.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `nla.select_box`<br><small>axis_range=False, active=False</small> | 默认：<code>B</code>；axis_range=False |
| 修改 | <code>ALT + B</code> | `nla.select_box`<br><small>axis_range=True, active=False</small> | 默认：<code>ALT + B</code>；axis_range=True |
| 修改 | <code>LMB + 拖动</code> | `nla.select_box`<br><small>tweak=True, mode='SET'</small> | 默认：<code>RMB + 拖动</code>；tweak=True, mode='SET' |
| 修改 | <code>SHIFT + LMB + 拖动</code> | `nla.select_box`<br><small>tweak=True, mode='ADD'</small> | 默认：<code>SHIFT + RMB + 拖动</code>；tweak=True, mode='ADD' |
| 修改 | <code>CTRL + LMB + 拖动</code> | `nla.select_box`<br><small>tweak=True, mode='SUB'</small> | 默认：<code>CTRL + RMB + 拖动</code>；tweak=True, mode='SUB' |
| 修改 | <code>ALT + D</code> | `nla.duplicate_linked_move` | 默认：<code>SHIFT + D</code> |
| 修改 | <code>SHIFT + D</code> | `nla.duplicate_move` | 默认：<code>ALT + D</code> |
| 修改 | <code>CTRL + SHIFT + A</code> | `nla.apply_scale` | 默认：<code>CTRL + A</code> |
| 修改 | <code>ALT + R</code> | `nla.clear_scale` | 默认：<code>ALT + S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.transform`<br><small>mode='TRANSLATION'</small> | 默认：<code>RMB + 拖动</code>；mode='TRANSLATION' |
| 修改 | <code>S</code> | `transform.transform`<br><small>mode='TIME_SCALE', active=False</small> | 默认：<code>S</code>；mode='TIME_SCALE' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='NLA_MT_context_menu'</small> | 默认：<code>W</code>；name='NLA_MT_context_menu' |
| 修改 | <code>SHIFT + RMB</code> | `anim.change_frame`<br><small>seq_solo_preview=True</small> | 默认：<code>LMB</code>；seq_solo_preview=True |
| 新增 | <code>F + 双击</code> | `nla.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `nla.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `nla.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `nla.duplicate_move` | Blender Default 中没有此绑定 |

## 图像与 UV

### Image

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>RMB</code> | `image.sample` | 默认：<code>LMB</code> |
| 修改 | <code>CTRL + RMB</code> | `image.curves_point_set`<br><small>point='BLACK_POINT'</small> | 默认：<code>CTRL + LMB</code>；point='BLACK_POINT' |
| 修改 | <code>SHIFT + RMB</code> | `image.curves_point_set`<br><small>point='WHITE_POINT'</small> | 默认：<code>SHIFT + LMB</code>；point='WHITE_POINT' |
| 修改 | <code>FOUR</code> | `object.mode_set`<br><small>mode='OBJECT', toggle=False</small> | 默认：<code>TAB</code>；mode='EDIT', toggle=True |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='IMAGE_MT_mask_context_menu'</small> | 默认：<code>W</code>；name='IMAGE_MT_mask_context_menu' |
| 新增 | <code>SHIFT + LMB + 双击</code> | `image.sample` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `image.view_all`<br><small>fit_view=True</small> | Blender Default 中没有此绑定 |

### Image Editor Tool: Uv, Grab

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.size'</small> | 默认：<code>F</code>；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.strength'</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Editor Tool: Uv, Pinch

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.size'</small> | 默认：<code>F</code>；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.strength'</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Editor Tool: Uv, Relax

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.size'</small> | 默认：<code>F</code>；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.uv_sculpt.strength'</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Generic

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |

### Image Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.image_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='space_data.zoom', image_id='tool_settings.image_paint.brush', secondary_tex=True</small> | 默认：<code>F</code>；data_path_primary='tool_settings.image_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='space_data.zoom', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | <code>ALT + S</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.image_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True</small> | 默认：<code>SHIFT + F</code>；data_path_primary='tool_settings.image_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | <code>CTRL + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.image_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=False, active=False</small> | 默认：<code>CTRL + F</code>；data_path_primary='tool_settings.image_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=False |
| 修改 | <code>CTRL + ALT + F</code> | `wm.radial_control`<br><small>data_path_primary='tool_settings.image_paint.brush.mask_texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True, active=False</small> | 默认：<code>CTRL + ALT + F</code>；data_path_primary='tool_settings.image_paint.brush.mask_texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | <code>RMB</code> | `wm.call_panel`<br><small>name='VIEW3D_PT_paint_texture_context_menu'</small> | 默认：<code>W</code>；name='VIEW3D_PT_paint_texture_context_menu' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='VIEW3D_AST_brush_texture_paint'</small> | 默认：<code>SPACE</code>；name='VIEW3D_AST_brush_texture_paint' |
| 修改 | <code>B</code> | `wm.call_asset_shelf_popover`<br><small>name='IMAGE_AST_brush_paint'</small> | 默认：<code>SPACE</code>；name='IMAGE_AST_brush_paint' |
| 新增 | <code>SHIFT + LMB + 双击</code> | `paint.sample_color` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + SHIFT + LMB + 双击</code> | `paint.sample_color`<br><small>merged=True</small> | Blender Default 中没有此绑定 |

### UV Editor

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 点击</code> | `uv.select`<br><small>deselect_all=True</small> | 默认：<code>RMB + 点击</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB + 点击</code> | `uv.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + RMB</code>；toggle=True |
| 修改 | <code>ALT + LMB + 点击</code> | `uv.select_loop` | 默认：<code>ALT + RMB</code> |
| 修改 | <code>SHIFT + ALT + LMB + 点击</code> | `uv.select_loop`<br><small>extend=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；extend=True |
| 修改 | <code>CTRL + ALT + LMB + 点击</code> | `uv.select_edge_ring` | 默认：<code>CTRL + ALT + RMB</code> |
| 修改 | <code>CTRL + SHIFT + ALT + LMB + 点击</code> | `uv.select_edge_ring`<br><small>extend=True</small> | 默认：<code>CTRL + SHIFT + ALT + RMB</code>；extend=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `uv.shortest_path_pick`<br><small>use_fill=False</small> | 默认：<code>CTRL + RMB</code>；use_fill=False |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `uv.shortest_path_pick`<br><small>use_fill=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；use_fill=True |
| 修改 | <code>B</code> | `uv.select_box`<br><small>pinned=False, active=False</small> | 默认：<code>B</code>；pinned=False |
| 修改 | <code>CTRL + B</code> | `uv.select_box`<br><small>pinned=True, active=False</small> | 默认：<code>CTRL + B</code>；pinned=True |
| 修改 | <code>CTRL + RMB + 拖动</code> | `uv.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `uv.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + A</code> | `uv.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='IMAGE_MT_uvs_context_menu'</small> | 默认：<code>W</code>；name='IMAGE_MT_uvs_context_menu' |
| 修改 | <code>SHIFT + RMB</code> | `uv.cursor_set` | 默认：<code>LMB + 点击</code> |
| 新增 | <code>SHIFT + RMB + 拖动</code> | `transform.translate`<br><small>cursor_transform=True, release_confirm=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `uv.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 移除 | <code>RMB</code> | `uv.select`<br><small>deselect_all=True, select_passthrough=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |

## 视频、跟踪与遮罩

### Clip

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |

### Clip Editor

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB</code> | `clip.select`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB</code> | `clip.select`<br><small>extend=True</small> | 默认：<code>SHIFT + RMB</code>；extend=True |
| 修改 | <code>CTRL + A</code> | `clip.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `clip.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + ALT + RMB + 拖动</code> | `clip.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + ALT + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + ALT + RMB + 拖动</code> | `clip.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + ALT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>SHIFT + RMB</code> | `clip.cursor_set` | 默认：<code>LMB + 点击</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='CLIP_MT_tracking_context_menu'</small> | 默认：<code>W</code>；name='CLIP_MT_tracking_context_menu' |
| 新增 | <code>F + 双击</code> | `clip.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `clip.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `clip.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Mask Editing

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>SHIFT + LMB</code> | `mask.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + A</code> | `mask.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `mask.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + ALT + RMB + 拖动</code> | `mask.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + ALT + LMB + 拖动</code>；mode='ADD' |
| 修改 | <code>CTRL + SHIFT + ALT + RMB + 拖动</code> | `mask.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + ALT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + LMB</code> | `clip.select` | 默认：<code>CTRL + RMB</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>SHIFT + RMB</code> | `uv.cursor_set` | 默认：<code>LMB + 点击</code> |
| 新增 | <code>SHIFT + RMB + 拖动</code> | `transform.translate`<br><small>cursor_transform=True, release_confirm=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `mask.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `mask.duplicate_move` | Blender Default 中没有此绑定 |
| 移除 | <code>RMB</code> | `mask.select`<br><small>deselect_all=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |

### Paint Face Mask (Weight, Vertex, Texture)

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `paint.face_select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + SHIFT + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='SUB'</small> | 默认：<code>CTRL + SHIFT + LMB + 拖动</code>；mode='SUB' |
| 修改 | <code>CTRL + RMB + 拖动</code> | `view3d.select_lasso`<br><small>mode='ADD'</small> | 默认：<code>CTRL + SHIFT + ALT + LMB + 拖动</code>；mode='ADD' |
| 新增 | <code>CTRL + F</code> | `paint.face_select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 移除 | <code>ALT + RMB</code> | `paint.face_select_loop`<br><small>extend=False, select=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>SHIFT + ALT + RMB</code> | `paint.face_select_loop`<br><small>extend=True, select=True</small> | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | <code>CTRL + SHIFT + ALT + RMB</code> | `paint.face_select_loop`<br><small>extend=True, select=False</small> | 当前 Keymap 中没有此 Blender Default 绑定 |

### Preview

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 点击</code> | `sequencer.select`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB + 点击</code> | `sequencer.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `sequencer.select`<br><small>center=True</small> | 默认：<code>CTRL + RMB</code>；center=True |
| 修改 | <code>ALT + LMB + 点击</code> | `sequencer.select`<br><small>ignore_connections=True</small> | 默认：<code>ALT + RMB</code>；ignore_connections=True |
| 修改 | <code>CTRL + SHIFT + LMB + 点击</code> | `sequencer.select`<br><small>toggle=True, center=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；toggle=True, center=True |
| 修改 | <code>SHIFT + ALT + LMB + 点击</code> | `sequencer.select`<br><small>toggle=True, ignore_connections=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；toggle=True, ignore_connections=True |
| 修改 | <code>CTRL + A</code> | `sequencer.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `sequencer.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>R + 双击</code> | `transform.rotate` | 默认：<code>R</code> |
| 修改 | <code>S</code> | `transform.resize`<br><small>active=False</small> | 默认：<code>S</code> |
| 修改 | <code>LMB + 拖动</code> | `transform.translate` | 默认：<code>RMB + 拖动</code> |
| 修改 | <code>ALT + W</code> | `sequencer.strip_transform_clear`<br><small>property='POSITION'</small> | 默认：<code>ALT + G</code>；property='POSITION' |
| 修改 | <code>ALT + R</code> | `sequencer.strip_transform_clear`<br><small>property='SCALE'</small> | 默认：<code>ALT + S</code>；property='SCALE' |
| 修改 | <code>ALT + E</code> | `sequencer.strip_transform_clear`<br><small>property='ROTATION'</small> | 默认：<code>ALT + R</code>；property='ROTATION' |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='SEQUENCER_MT_preview_context_menu'</small> | 默认：<code>W</code>；name='SEQUENCER_MT_preview_context_menu' |
| 修改 | <code>SHIFT + RMB</code> | `sequencer.cursor_set` | 默认：<code>LMB + 点击</code> |
| 新增 | <code>SHIFT + RMB + 拖动</code> | `transform.translate`<br><small>cursor_transform=True, release_confirm=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>F + 双击</code> | `sequencer.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `sequencer.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.move', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>R</code> | `wm.tool_set_by_id`<br><small>name='builtin.rotate', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `wm.tool_set_by_id`<br><small>name='builtin.scale', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `sequencer.preview_duplicate_move` | Blender Default 中没有此绑定 |

### Sequencer

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 点击</code> | `sequencer.select`<br><small>deselect_all=True</small> | 默认：<code>RMB</code>；deselect_all=True |
| 修改 | <code>SHIFT + LMB + 点击</code> | `sequencer.select`<br><small>toggle=True</small> | 默认：<code>SHIFT + RMB</code>；toggle=True |
| 修改 | <code>CTRL + LMB</code> | `sequencer.select`<br><small>linked_time=True</small> | 默认：<code>CTRL + RMB</code>；linked_time=True |
| 修改 | <code>CTRL + SHIFT + LMB</code> | `sequencer.select`<br><small>extend=True, linked_time=True</small> | 默认：<code>CTRL + SHIFT + RMB</code>；linked_time=True, extend=True |
| 修改 | <code>CTRL + LMB + 点击</code> | `sequencer.select`<br><small>side_of_frame=True</small> | 默认：<code>CTRL + RMB + 点击</code>；side_of_frame=True |
| 修改 | <code>ALT + LMB</code> | `sequencer.select`<br><small>deselect_all=True, ignore_connections=True</small> | 默认：<code>ALT + RMB</code>；deselect_all=True, ignore_connections=True |
| 修改 | <code>SHIFT + ALT + LMB</code> | `sequencer.select`<br><small>toggle=True, ignore_connections=True</small> | 默认：<code>SHIFT + ALT + RMB</code>；toggle=True, ignore_connections=True |
| 修改 | <code>LMB + 拖动</code> | `sequencer.select_box`<br><small>mode='SET', tweak=True</small> | 默认：<code>RMB + 拖动</code>；tweak=True, mode='SET' |
| 修改 | <code>SHIFT + LMB + 拖动</code> | `sequencer.select_box`<br><small>mode='ADD', tweak=True</small> | 默认：<code>SHIFT + RMB + 拖动</code>；tweak=True, mode='ADD' |
| 修改 | <code>CTRL + LMB + 拖动</code> | `sequencer.select_box`<br><small>mode='SUB', tweak=True</small> | 默认：<code>CTRL + RMB + 拖动</code>；tweak=True, mode='SUB' |
| 修改 | <code>ALT + LMB + 拖动</code> | `sequencer.select_box`<br><small>mode='SET', tweak=True, ignore_connections=True</small> | 默认：<code>ALT + RMB + 拖动</code>；tweak=True, ignore_connections=True, mode='SET' |
| 修改 | <code>B</code> | `sequencer.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + B</code> | `sequencer.select_box`<br><small>include_handles=True, active=False</small> | 默认：<code>CTRL + B</code>；include_handles=True |
| 修改 | <code>CTRL + A</code> | `sequencer.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>LMB + 拖动</code> | `transform.seq_slide`<br><small>use_restore_handle_selection=True, view2d_edge_pan=True</small> | 默认：<code>RMB + 拖动</code>；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | <code>ALT + LMB + 拖动</code> | `transform.seq_slide`<br><small>use_restore_handle_selection=True, view2d_edge_pan=True</small> | 默认：<code>ALT + RMB + 拖动</code>；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | <code>CTRL + LMB + 拖动</code> | `transform.seq_slide`<br><small>use_restore_handle_selection=True, view2d_edge_pan=True</small> | 默认：<code>CTRL + RMB + 拖动</code>；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='SEQUENCER_MT_context_menu'</small> | 默认：<code>W</code>；name='SEQUENCER_MT_context_menu' |
| 新增 | <code>F + 双击</code> | `sequencer.view_all` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `sequencer.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>B</code> | `sequencer.split` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + B</code> | `sequencer.split`<br><small>type='HARD'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + D</code> | `sequencer.duplicate_move` | Blender Default 中没有此绑定 |

## 文件、资源与 Outliner

### File Browser

上下文：`FILE_BROWSER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |
| 修改 | <code>RMB</code> | `file.select`<br><small>open=False, only_activate_if_selected=True, pass_through=True</small> | 默认：<code>RMB</code>；open=False, only_activate_if_selected=False, pass_through=True |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='FILEBROWSER_MT_context_menu'</small> | 默认：<code>W</code>；name='FILEBROWSER_MT_context_menu' |

### File Browser Main

上下文：`FILE_BROWSER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `file.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `file.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='ASSETBROWSER_MT_context_menu'</small> | 默认：<code>W</code>；name='ASSETBROWSER_MT_context_menu' |
| 新增 | <code>LMB + 双击</code> | `poselib.apply_pose_asset` | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `file.view_selected` | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `file.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Outliner

上下文：`OUTLINER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>LMB + 双击</code> | `outliner.item_activate`<br><small>deselect_all=True, recurse=True</small> | 默认：<code>LMB + 双击</code>；recurse=True, deselect_all=True |
| 修改 | <code>CTRL + LMB + 双击</code> | `outliner.item_activate`<br><small>extend=True, deselect_all=True, recurse=True</small> | 默认：<code>CTRL + LMB + 双击</code>；recurse=True, extend=True, deselect_all=True |
| 修改 | <code>SHIFT + LMB + 双击</code> | `outliner.item_activate`<br><small>extend_range=True, deselect_all=True, recurse=True</small> | 默认：<code>SHIFT + LMB + 双击</code>；recurse=True, extend_range=True, deselect_all=True |
| 修改 | <code>CTRL + SHIFT + LMB + 双击</code> | `outliner.item_activate`<br><small>extend=True, extend_range=True, deselect_all=True, recurse=True</small> | 默认：<code>CTRL + SHIFT + LMB + 双击</code>；recurse=True, extend=True, extend_range=True, deselect_all=True |
| 修改 | <code>B</code> | `outliner.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>CTRL + A</code> | `outliner.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>CTRL + SHIFT + F</code> | `outliner.start_filter` | 默认：<code>CTRL + F</code> |
| 新增 | <code>CTRL + F</code> | `outliner.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |
| 新增 | <code>F</code> | `outliner.show_active` | Blender Default 中没有此绑定 |
| 新增 | <code>SHIFT + F</code> | `outliner.show_hierarchy` | Blender Default 中没有此绑定 |

## 其他编辑器

### Gesture Straight Line

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>F</code> | `FLIP`<br><small>active=False</small> | 默认：<code>F</code> |

### Info

上下文：`INFO / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + A</code> | `info.select_all`<br><small>action='SELECT'</small> | 默认：<code>A</code>；action='SELECT' |
| 修改 | <code>B</code> | `info.select_box`<br><small>active=False</small> | 默认：<code>B</code> |
| 修改 | <code>RMB</code> | `wm.call_menu`<br><small>name='INFO_MT_context_menu'</small> | 默认：<code>W</code>；name='INFO_MT_context_menu' |
| 新增 | <code>CTRL + F</code> | `info.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### Knife Tool Modal Map

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | <code>Q</code> | `X_AXIS` | Blender Default 中没有此绑定 |
| 新增 | <code>W</code> | `Y_AXIS` | Blender Default 中没有此绑定 |
| 新增 | <code>E</code> | `Z_AXIS` | Blender Default 中没有此绑定 |

### Property Editor

上下文：`PROPERTIES / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>CTRL + SHIFT + F</code> | `buttons.start_filter` | 默认：<code>CTRL + F</code> |
| 修改 | <code>CTRL + SHIFT + A</code> | `object.modifier_apply`<br><small>report=True</small> | 默认：<code>CTRL + A</code>；report=True |
| 修改 | <code>CTRL + SHIFT + A</code> | `constraint.apply`<br><small>report=True</small> | 默认：<code>CTRL + A</code>；report=True |
| 新增 | <code>CTRL + D</code> | `constraint.copy` | Blender Default 中没有此绑定 |

### Spreadsheet Generic

上下文：`SPREADSHEET / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_channels', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_channels' |

### Video Sequence Editor

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>T</code> | `wm.context_toggle`<br><small>data_path='space_data.show_region_toolbar', active=False</small> | 默认：<code>T</code>；data_path='space_data.show_region_toolbar' |
| 新增 | <code>W</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True, active=False</small> | Blender Default 中没有此绑定 |
| 新增 | <code>Q</code> | `wm.tool_set_by_id`<br><small>name='builtin.select_box', cycle=True</small> | Blender Default 中没有此绑定 |
| 新增 | <code>CTRL + F</code> | `sequencer.select_all`<br><small>action='INVERT'</small> | Blender Default 中没有此绑定 |

### View3D Walk Modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | <code>V</code> | `JUMP` | 默认：<code>V</code> |
| 修改 | <code>V + 松开</code> | `JUMP_STOP` | 默认：<code>V + 松开</code> |
| 修改 | <code>SPACE</code> | `TELEPORT`<br><small>active=False</small> | 默认：<code>SPACE</code> |
| 新增 | <code>SPACE</code> | `JUMP` | Blender Default 中没有此绑定 |
| 新增 | <code>SPACE</code> | `JUMP_STOP` | Blender Default 中没有此绑定 |
