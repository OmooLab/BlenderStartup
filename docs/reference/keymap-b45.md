# Blender 4.5 快捷键差异

本页由当前 `Refined Industry Compatible` Keymap 与同版本的 **Blender Default** 自动比较生成。Industry Compatible 不是比较基线。

- **修改绑定**：471
- **新增绑定**：175
- **移除绑定**：17
- **受影响 Keymap**：64

!!! note "怎样理解差异"

    “修改”表示同一个 Blender Operator 的触发方式或属性发生变化；“新增”和“移除”表示在相同编辑器 Keymap 中只存在于一侧。Blender 在运行时生成的工具 Keymap 不会因为没有出现在导出文件中就被记为删除。

基线来源：[Blender 官方 `b45` Blender Default 源文件](https://raw.githubusercontent.com/blender/blender/blender-v4.5-release/scripts/presets/keyconfig/keymap_data/blender_default.py)。

## 视图与通用操作

### 3D View

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `SHIFT + RMB` | `view3d.cursor3d` | 默认：`LMB + 点击` |
| 修改 | `CTRL + SHIFT + GRAVE` | `view3d.navigate` | 默认：`SHIFT + GRAVE` |
| 修改 | `LMB + 点击` | `view3d.select`（deselect_all=True） | 默认：`RMB + 点击`；deselect_all=True |
| 修改 | `SHIFT + LMB + 点击` | `view3d.select`（toggle=True） | 默认：`SHIFT + RMB`；toggle=True |
| 修改 | `CTRL + LMB + 点击` | `view3d.select`（center=True, object=True） | 默认：`CTRL + RMB`；center=True, object=True |
| 修改 | `ALT + LMB + 点击` | `view3d.select`（enumerate=True） | 默认：`ALT + RMB`；enumerate=True |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `view3d.select`（toggle=True, center=True） | 默认：`CTRL + SHIFT + RMB`；toggle=True, center=True |
| 修改 | `CTRL + ALT + LMB + 点击` | `view3d.select`（center=True, enumerate=True） | 默认：`CTRL + ALT + RMB`；center=True, enumerate=True |
| 修改 | `SHIFT + ALT + LMB + 点击` | `view3d.select`（toggle=True, enumerate=True） | 默认：`SHIFT + ALT + RMB`；toggle=True, enumerate=True |
| 修改 | `CTRL + SHIFT + ALT + LMB + 点击` | `view3d.select`（toggle=True, center=True, enumerate=True） | 默认：`CTRL + SHIFT + ALT + RMB`；toggle=True, center=True, enumerate=True |
| 修改 | `B` | `view3d.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + RMB + 拖动` | `view3d.select_lasso`（mode='ADD'） | 默认：`CTRL + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `view3d.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + GRAVE` | `wm.context_toggle`（data_path='space_data.show_gizmo', active=False） | 默认：`CTRL + GRAVE`；data_path='space_data.show_gizmo' |
| 新增 | `SHIFT + RMB + 拖动` | `transform.translate`（cursor_transform=True, release_confirm=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `ALT + MMB` | `view3d.move` | Blender Default 中没有此绑定 |
| 新增 | `ALT + LMB` | `view3d.rotate` | Blender Default 中没有此绑定 |
| 新增 | `ALT + RMB` | `view3d.zoom` | Blender Default 中没有此绑定 |
| 新增 | `F` | `view3d.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `F + 双击` | `view3d.view_all` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ALT + LMB` | `view3d.move` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + ALT + LMB` | `view3d.zoom` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + LMB` | `view3d.cursor3d` | Blender Default 中没有此绑定 |
| 新增 | `T` | `wm.call_menu_pie`（name='VIEW3D_MT_orientations_pie'） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + T` | `wm.call_menu_pie`（name='VIEW3D_MT_pivot_pie'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + ALT + Q + 可重复` | `view3d.view_roll`（angle=5.0, type='LEFT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + ALT + E + 可重复` | `view3d.view_roll`（angle=5.0, type='RIGHT'） | Blender Default 中没有此绑定 |
| 新增 | `ALT + GRAVE` | `view3d.camera_to_view` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + GRAVE` | `object.select_camera` | Blender Default 中没有此绑定 |
| 移除 | `RMB` | `view3d.select`（deselect_all=True, select_passthrough=True） | 当前 Keymap 中没有此 Blender Default 绑定 |

### 3D View Generic

上下文：`VIEW_3D / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |

### Frames

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `SPACE` | `screen.animation_play` | 默认：`SHIFT + SPACE` |
| 新增 | `CTRL + ALT + WHEEL DOWN` | `screen.keyframe_jump`（next=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + ALT + WHEEL UP` | `screen.keyframe_jump`（next=False） | Blender Default 中没有此绑定 |
| 新增 | `ESC` | `screen.frame_jump`（active=False） | Blender Default 中没有此绑定 |

### Screen

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + ALT + Q` | `screen.region_quadview`（active=False） | 默认：`CTRL + ALT + Q` |

### User Interface

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + SHIFT + F` | `ui.list_start_filter` | 默认：`CTRL + F` |
| 修改 | `CTRL + SHIFT + F` | `ui.view_start_filter` | 默认：`CTRL + F` |

### View2D

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `MMB` | `view2d.pan`（active=False） | 默认：`MMB` |
| 新增 | `ALT + MMB` | `view2d.pan` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ALT + LMB` | `view2d.pan` | Blender Default 中没有此绑定 |
| 新增 | `ALT + RMB` | `view2d.zoom` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + ALT + LMB` | `view2d.zoom` | Blender Default 中没有此绑定 |

### Window

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `A` | `wm.call_menu`（name='SCREEN_MT_user_menu'） | 默认：`Q`；name='SCREEN_MT_user_menu' |
| 修改 | `SHIFT + SPACE` | `wm.toolbar` | 默认：`SPACE` |
| 新增 | `ALT + GRAVE + 可重复` | `wm.context_toggle`（data_path='space_data.lock_camera'） | Blender Default 中没有此绑定 |

## 对象、模式与 Transform

### Object Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `A` | `object.select_all`（action='SELECT', active=False） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `object.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `ALT + W` | `object.location_clear`（clear_delta=False） | 默认：`ALT + G`；clear_delta=False |
| 修改 | `ALT + E` | `object.scale_clear`（clear_delta=False） | 默认：`ALT + S`；clear_delta=False |
| 修改 | `ALT + A` | `wm.call_menu`（name='VIEW3D_MT_object_apply'） | 默认：`CTRL + A`；name='VIEW3D_MT_object_apply' |
| 修改 | `ONE` | `object.hide_collection`（collection_index=1, extend=False, active=False） | 默认：`ONE`；collection_index=1, extend=False |
| 修改 | `TWO` | `object.hide_collection`（collection_index=2, extend=False, active=False） | 默认：`TWO`；collection_index=2, extend=False |
| 修改 | `THREE` | `object.hide_collection`（collection_index=3, extend=False, active=False） | 默认：`THREE`；collection_index=3, extend=False |
| 修改 | `FOUR` | `object.hide_collection`（collection_index=4, extend=False, active=False） | 默认：`FOUR`；collection_index=4, extend=False |
| 修改 | `FIVE` | `object.hide_collection`（collection_index=5, extend=False, active=False） | 默认：`FIVE`；collection_index=5, extend=False |
| 修改 | `SIX` | `object.hide_collection`（collection_index=6, extend=False, active=False） | 默认：`SIX`；collection_index=6, extend=False |
| 修改 | `SEVEN` | `object.hide_collection`（collection_index=7, extend=False, active=False） | 默认：`SEVEN`；collection_index=7, extend=False |
| 修改 | `EIGHT` | `object.hide_collection`（collection_index=8, extend=False, active=False） | 默认：`EIGHT`；collection_index=8, extend=False |
| 修改 | `NINE` | `object.hide_collection`（collection_index=9, extend=False, active=False） | 默认：`NINE`；collection_index=9, extend=False |
| 修改 | `ZERO` | `object.hide_collection`（collection_index=10, extend=False, active=False） | 默认：`ZERO`；collection_index=10, extend=False |
| 修改 | `ALT + ONE` | `object.hide_collection`（collection_index=11, extend=False, active=False） | 默认：`ALT + ONE`；collection_index=11, extend=False |
| 修改 | `ALT + TWO` | `object.hide_collection`（collection_index=12, extend=False, active=False） | 默认：`ALT + TWO`；collection_index=12, extend=False |
| 修改 | `ALT + THREE` | `object.hide_collection`（collection_index=13, extend=False, active=False） | 默认：`ALT + THREE`；collection_index=13, extend=False |
| 修改 | `ALT + FOUR` | `object.hide_collection`（collection_index=14, extend=False, active=False） | 默认：`ALT + FOUR`；collection_index=14, extend=False |
| 修改 | `ALT + FIVE` | `object.hide_collection`（collection_index=15, extend=False, active=False） | 默认：`ALT + FIVE`；collection_index=15, extend=False |
| 修改 | `ALT + SIX` | `object.hide_collection`（collection_index=16, extend=False, active=False） | 默认：`ALT + SIX`；collection_index=16, extend=False |
| 修改 | `ALT + SEVEN` | `object.hide_collection`（collection_index=17, extend=False, active=False） | 默认：`ALT + SEVEN`；collection_index=17, extend=False |
| 修改 | `ALT + EIGHT` | `object.hide_collection`（collection_index=18, extend=False, active=False） | 默认：`ALT + EIGHT`；collection_index=18, extend=False |
| 修改 | `ALT + NINE` | `object.hide_collection`（collection_index=19, extend=False, active=False） | 默认：`ALT + NINE`；collection_index=19, extend=False |
| 修改 | `ALT + ZERO` | `object.hide_collection`（collection_index=20, extend=False, active=False） | 默认：`ALT + ZERO`；collection_index=20, extend=False |
| 修改 | `SHIFT + ONE` | `object.hide_collection`（collection_index=1, extend=True, active=False） | 默认：`SHIFT + ONE`；collection_index=1, extend=True |
| 修改 | `SHIFT + TWO` | `object.hide_collection`（collection_index=2, extend=True, active=False） | 默认：`SHIFT + TWO`；collection_index=2, extend=True |
| 修改 | `SHIFT + THREE` | `object.hide_collection`（collection_index=3, extend=True, active=False） | 默认：`SHIFT + THREE`；collection_index=3, extend=True |
| 修改 | `SHIFT + FOUR` | `object.hide_collection`（collection_index=4, extend=True, active=False） | 默认：`SHIFT + FOUR`；collection_index=4, extend=True |
| 修改 | `SHIFT + FIVE` | `object.hide_collection`（collection_index=5, extend=True, active=False） | 默认：`SHIFT + FIVE`；collection_index=5, extend=True |
| 修改 | `SHIFT + SIX` | `object.hide_collection`（collection_index=6, extend=True, active=False） | 默认：`SHIFT + SIX`；collection_index=6, extend=True |
| 修改 | `SHIFT + SEVEN` | `object.hide_collection`（collection_index=7, extend=True, active=False） | 默认：`SHIFT + SEVEN`；collection_index=7, extend=True |
| 修改 | `SHIFT + EIGHT` | `object.hide_collection`（collection_index=8, extend=True, active=False） | 默认：`SHIFT + EIGHT`；collection_index=8, extend=True |
| 修改 | `SHIFT + NINE` | `object.hide_collection`（collection_index=9, extend=True, active=False） | 默认：`SHIFT + NINE`；collection_index=9, extend=True |
| 修改 | `SHIFT + ZERO` | `object.hide_collection`（collection_index=10, extend=True, active=False） | 默认：`SHIFT + ZERO`；collection_index=10, extend=True |
| 修改 | `SHIFT + ALT + ONE` | `object.hide_collection`（collection_index=11, extend=True, active=False） | 默认：`SHIFT + ALT + ONE`；collection_index=11, extend=True |
| 修改 | `SHIFT + ALT + TWO` | `object.hide_collection`（collection_index=12, extend=True, active=False） | 默认：`SHIFT + ALT + TWO`；collection_index=12, extend=True |
| 修改 | `SHIFT + ALT + THREE` | `object.hide_collection`（collection_index=13, extend=True, active=False） | 默认：`SHIFT + ALT + THREE`；collection_index=13, extend=True |
| 修改 | `SHIFT + ALT + FOUR` | `object.hide_collection`（collection_index=14, extend=True, active=False） | 默认：`SHIFT + ALT + FOUR`；collection_index=14, extend=True |
| 修改 | `SHIFT + ALT + FIVE` | `object.hide_collection`（collection_index=15, extend=True, active=False） | 默认：`SHIFT + ALT + FIVE`；collection_index=15, extend=True |
| 修改 | `SHIFT + ALT + SIX` | `object.hide_collection`（collection_index=16, extend=True, active=False） | 默认：`SHIFT + ALT + SIX`；collection_index=16, extend=True |
| 修改 | `SHIFT + ALT + SEVEN` | `object.hide_collection`（collection_index=17, extend=True, active=False） | 默认：`SHIFT + ALT + SEVEN`；collection_index=17, extend=True |
| 修改 | `SHIFT + ALT + EIGHT` | `object.hide_collection`（collection_index=18, extend=True, active=False） | 默认：`SHIFT + ALT + EIGHT`；collection_index=18, extend=True |
| 修改 | `SHIFT + ALT + NINE` | `object.hide_collection`（collection_index=19, extend=True, active=False） | 默认：`SHIFT + ALT + NINE`；collection_index=19, extend=True |
| 修改 | `SHIFT + ALT + ZERO` | `object.hide_collection`（collection_index=20, extend=True, active=False） | 默认：`SHIFT + ALT + ZERO`；collection_index=20, extend=True |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_object_context_menu'） | 默认：`W`；name='VIEW3D_MT_object_context_menu' |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `object.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + A` | `object.select_all`（action='SELECT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `object.duplicate_move` | Blender Default 中没有此绑定 |
| 新增 | `ONE` | `object.mode_set_with_submode`（mode='EDIT', toggle=False, mesh_select_mode={'VERT'}） | Blender Default 中没有此绑定 |
| 新增 | `TWO` | `object.mode_set_with_submode`（mode='EDIT', toggle=False, mesh_select_mode={'EDGE'}） | Blender Default 中没有此绑定 |
| 新增 | `THREE` | `object.mode_set_with_submode`（mode='EDIT', mesh_select_mode={'FACE'}） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + ONE` | `object.select_grouped` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + TWO` | `object.select_linked` | Blender Default 中没有此绑定 |
| 新增 | `TAB + 松开` | `wm.call_menu`（name='VIEW3D_MT_add'） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ONE` | `object.mode_set`（mode='SCULPT'） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ONE` | `object.mode_set`（mode='PAINT_GREASE_PENCIL'） | Blender Default 中没有此绑定 |

### Object Non-modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `TAB` | `object.mode_set`（mode='EDIT', toggle=True, active=False） | 默认：`TAB`；mode='EDIT', toggle=True |
| 修改 | `TAB + 拖动` | `view3d.object_mode_pie_or_toggle` | 默认：`CTRL + TAB` |
| 新增 | `LMB + 双击` | `object.transfer_mode` | Blender Default 中没有此绑定 |
| 新增 | `ESC` | `object.mode_set`（mode='OBJECT'） | Blender Default 中没有此绑定 |
| 新增 | `FOUR` | `object.mode_set`（mode='OBJECT'） | Blender Default 中没有此绑定 |

### Pose

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `ALT + A` | `wm.call_menu`（name='VIEW3D_MT_pose_apply'） | 默认：`CTRL + A`；name='VIEW3D_MT_pose_apply' |
| 修改 | `ALT + W` | `pose.loc_clear` | 默认：`ALT + G` |
| 修改 | `ALT + E` | `pose.scale_clear` | 默认：`ALT + S` |
| 修改 | `CTRL + A` | `pose.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `pose.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_pose_context_menu'） | 默认：`W`；name='VIEW3D_MT_pose_context_menu' |
| 新增 | `CTRL + F` | `pose.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Transform Modal Map

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | `Q` | `AXIS_X` | Blender Default 中没有此绑定 |
| 新增 | `W` | `AXIS_Y` | Blender Default 中没有此绑定 |
| 新增 | `E` | `AXIS_Z` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + Q` | `PLANE_X` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + W` | `PLANE_Y` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + E` | `PLANE_Z` | Blender Default 中没有此绑定 |

## 建模、雕刻与绘制

### Armature

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + A` | `armature.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `armature.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `CTRL + LMB + 点击` | `armature.shortest_path_pick` | 默认：`CTRL + RMB` |
| 修改 | `E` | `armature.extrude_move`（active=False） | 默认：`E` |
| 修改 | `CTRL + RMB + 点击` | `armature.click_extrude` | 默认：`CTRL + LMB + 点击` |
| 修改 | `F` | `armature.fill`（active=False） | 默认：`F` |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_armature_context_menu'） | 默认：`W`；name='VIEW3D_MT_armature_context_menu' |
| 新增 | `CTRL + F` | `armature.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `armature.duplicate_move` | Blender Default 中没有此绑定 |

### Curve

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + RMB + 点击` | `curve.vertex_add` | 默认：`CTRL + LMB + 点击` |
| 修改 | `CTRL + A` | `curve.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `curve.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `CTRL + LMB + 点击` | `curve.shortest_path_pick` | 默认：`CTRL + RMB` |
| 修改 | `E` | `curve.extrude_move`（active=False） | 默认：`E` |
| 修改 | `F` | `curve.make_segment`（active=False） | 默认：`F` |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_edit_curve_context_menu'） | 默认：`W`；name='VIEW3D_MT_edit_curve_context_menu' |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `curve.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `curve.duplicate_move` | Blender Default 中没有此绑定 |

### Curves

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + A` | `curves.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `curves.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `E` | `curves.extrude_move`（active=False） | 默认：`E` |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_edit_curves_context_menu'） | 默认：`W`；name='VIEW3D_MT_edit_curves_context_menu' |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `curves.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `curves.duplicate_move` | Blender Default 中没有此绑定 |

### Grease Pencil

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | `CTRL + F` | `grease_pencil.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Grease Pencil Edit Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `F` | `grease_pencil.cyclical_set`（type='CLOSE', subdivide_cyclic_segment=True, active=False） | 默认：`F`；type='CLOSE', subdivide_cyclic_segment=True |
| 修改 | `E` | `grease_pencil.extrude_move`（active=False） | 默认：`E` |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_greasepencil_edit_context_menu'） | 默认：`W`；name='VIEW3D_MT_greasepencil_edit_context_menu' |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `grease_pencil.duplicate_move` | Blender Default 中没有此绑定 |

### Grease Pencil Paint Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `B` | `grease_pencil.erase_box`（wait_for_input=True, active=False） | 默认：`B`；wait_for_input=True |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_paint.brush.size'） | 默认：`F`；data_path_primary='tool_settings.gpencil_paint.brush.size' |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_paint.brush.strength'） | 默认：`SHIFT + F`；data_path_primary='tool_settings.gpencil_paint.brush.strength' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_gpencil_paint'） | 默认：`SPACE`；name='VIEW3D_AST_brush_gpencil_paint' |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_greasepencil_draw_context_menu'） | 默认：`W`；name='VIEW3D_PT_greasepencil_draw_context_menu' |
| 新增 | `SHIFT + LMB + 双击` | `paint.sample_color` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + ALT + LMB` | `grease_pencil.erase_lasso` | Blender Default 中没有此绑定 |

### Grease Pencil Sculpt Mode

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_sculpt_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.gpencil_sculpt_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_sculpt_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.gpencil_sculpt_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_sculpt_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_sculpt_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_sculpt_paint.brush', secondary_tex=False |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_gpencil_sculpt'） | 默认：`SPACE`；name='VIEW3D_AST_brush_gpencil_sculpt' |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_greasepencil_sculpt_context_menu'） | 默认：`W`；name='VIEW3D_PT_greasepencil_sculpt_context_menu' |
| 新增 | `G` | `brush.asset_activate`（asset_library_type='ESSENTIALS', asset_library_identifier='', relative_asset_identifier='brushes/essentials_brushes-gp_sculpt.blend/Brush/Grab'） | Blender Default 中没有此绑定 |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |

### Grease Pencil Selection

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `grease_pencil.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `grease_pencil.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |

### Grease Pencil Vertex Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.gpencil_vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.gpencil_vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_vertex_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_vertex_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_vertex_paint.brush', secondary_tex=False |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_greasepencil_vertex_paint_context_menu'） | 默认：`W`；name='VIEW3D_PT_greasepencil_vertex_paint_context_menu' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_gpencil_vertex'） | 默认：`SPACE`；name='VIEW3D_AST_brush_gpencil_vertex' |

### Grease Pencil Weight Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.gpencil_weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.gpencil_weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | `CTRL + F` | `wm.radial_control`（data_path_primary='tool_settings.gpencil_weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False, active=False） | 默认：`CTRL + F`；data_path_primary='tool_settings.gpencil_weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.gpencil_weight_paint.brush.texture_slot.angle', color_path='tool_settings.gpencil_weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.gpencil_weight_paint.brush', secondary_tex=False |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_greasepencil_weight_context_menu'） | 默认：`W`；name='VIEW3D_PT_greasepencil_weight_context_menu' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_gpencil_weight'） | 默认：`SPACE`；name='VIEW3D_AST_brush_gpencil_weight' |
| 新增 | `ALT + LMB` | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ALT + LMB` | `view3d.select`（toggle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + LMB` | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + LMB + 双击` | `grease_pencil.weight_sample` | Blender Default 中没有此绑定 |

### Lattice

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + A` | `lattice.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `lattice.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_edit_lattice_context_menu'） | 默认：`W`；name='VIEW3D_MT_edit_lattice_context_menu' |
| 新增 | `CTRL + F` | `lattice.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Mesh

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + A` | `transform.skin_resize`（active=False） | 默认：`CTRL + A` |
| 修改 | `ALT + LMB + 点击` | `mesh.loop_select` | 默认：`ALT + RMB` |
| 修改 | `SHIFT + ALT + LMB + 点击` | `mesh.loop_select`（toggle=True） | 默认：`SHIFT + ALT + RMB`；toggle=True |
| 修改 | `CTRL + ALT + LMB + 点击` | `mesh.edgering_select` | 默认：`CTRL + ALT + RMB` |
| 修改 | `CTRL + SHIFT + ALT + LMB + 点击` | `mesh.edgering_select`（toggle=True） | 默认：`CTRL + SHIFT + ALT + RMB`；toggle=True |
| 修改 | `CTRL + LMB + 点击` | `mesh.shortest_path_pick`（use_fill=False） | 默认：`CTRL + RMB`；use_fill=False |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `mesh.shortest_path_pick`（use_fill=True） | 默认：`CTRL + SHIFT + RMB`；use_fill=True |
| 修改 | `CTRL + A` | `mesh.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `mesh.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `E` | `view3d.edit_mesh_extrude_move_normal`（active=False） | 默认：`E` |
| 修改 | `F + 可重复` | `mesh.edge_face_add`（active=False） | 默认：`F + 可重复` |
| 修改 | `CTRL + RMB + 点击` | `mesh.dupli_extrude_cursor`（rotate_source=True） | 默认：`CTRL + LMB + 点击`；rotate_source=True |
| 修改 | `CTRL + SHIFT + RMB + 点击` | `mesh.dupli_extrude_cursor`（rotate_source=False） | 默认：`CTRL + SHIFT + LMB + 点击`；rotate_source=False |
| 修改 | `CTRL + F` | `wm.call_menu`（name='VIEW3D_MT_edit_mesh_faces', active=False） | 默认：`CTRL + F`；name='VIEW3D_MT_edit_mesh_faces' |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_edit_mesh_context_menu'） | 默认：`W`；name='VIEW3D_MT_edit_mesh_context_menu' |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `mesh.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `mesh.duplicate_move` | Blender Default 中没有此绑定 |

### Metaball

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `CTRL + A` | `mball.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `mball.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_edit_metaball_context_menu'） | 默认：`W`；name='VIEW3D_MT_edit_metaball_context_menu' |
| 新增 | `CTRL + F` | `mball.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `mball.duplicate_move` | Blender Default 中没有此绑定 |

### Paint Curve

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + RMB` | `paintcurve.add_point_slide` | 默认：`CTRL + LMB` |
| 修改 | `LMB` | `paintcurve.select` | 默认：`RMB` |
| 修改 | `SHIFT + LMB` | `paintcurve.select`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `RMB` | `paintcurve.slide`（align=False） | 默认：`LMB`；align=False |
| 修改 | `SHIFT + RMB` | `paintcurve.slide`（align=True） | 默认：`SHIFT + LMB`；align=True |
| 修改 | `CTRL + A` | `paintcurve.select`（toggle=True） | 默认：`A`；toggle=True |
| 修改 | `CTRL + SHIFT + RMB` | `paintcurve.cursor` | 默认：`CTRL + SHIFT + LMB` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |

### Paint Vertex Selection (Weight, Vertex)

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `paint.vert_select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `paint.vert_select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `view3d.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + RMB + 拖动` | `view3d.select_lasso`（mode='ADD'） | 默认：`CTRL + SHIFT + ALT + LMB + 拖动`；mode='ADD' |
| 修改 | `B` | `view3d.select_box`（active=False） | 默认：`B` |
| 新增 | `CTRL + F` | `paint.vert_select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Particle

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `particle.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `particle.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.particle_edit.brush.size'） | 默认：`F`；data_path_primary='tool_settings.particle_edit.brush.size' |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.particle_edit.brush.strength'） | 默认：`SHIFT + F`；data_path_primary='tool_settings.particle_edit.brush.strength' |
| 修改 | `RMB` | `wm.call_menu`（name='VIEW3D_MT_particle_context_menu'） | 默认：`W`；name='VIEW3D_MT_particle_context_menu' |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 新增 | `CTRL + F` | `particle.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Point Cloud

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `A` | `pointcloud.select_all`（action='SELECT', active=False） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `pointcloud.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |

### Sculpt

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `SHIFT + A` | `sculpt.expand`（target='MASK', falloff_type='GEODESIC', invert=False, use_mask_preserve=True, use_auto_mask=False） | 默认：`SHIFT + A`；target='MASK', falloff_type='GEODESIC', invert=False, use_auto_mask=False, use_mask_preserve=True |
| 修改 | `B` | `paint.mask_box_gesture`（mode='VALUE', value=0.0, active=False） | 默认：`B`；mode='VALUE', value=0.0 |
| 修改 | `D` | `sculpt.dyntopo_detail_size_edit` | 默认：`R` |
| 修改 | `CTRL + D` | `sculpt.detail_flood_fill` | 默认：`CTRL + R` |
| 修改 | `CTRL + D` | `object.voxel_remesh` | 默认：`CTRL + R` |
| 修改 | `D` | `object.voxel_size_edit` | 默认：`R` |
| 修改 | `X` | `paint.brush_colors_flip`（active=False） | 默认：`X` |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | `CTRL + F` | `wm.radial_control`（data_path_primary='tool_settings.sculpt.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False, active=False） | 默认：`CTRL + F`；data_path_primary='tool_settings.sculpt.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.sculpt.brush.texture_slot.angle', color_path='tool_settings.sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.sculpt.brush', secondary_tex=False |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_sculpt_context_menu'） | 默认：`W`；name='VIEW3D_PT_sculpt_context_menu' |
| 修改 | `V` | `brush.asset_activate`（asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Draw', active=False） | 默认：`V`；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Draw' |
| 修改 | `S` | `brush.asset_activate`（asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Smooth', active=False） | 默认：`S`；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Smooth' |
| 修改 | `SHIFT + T` | `brush.asset_activate`（asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Scrape/Fill', active=False） | 默认：`SHIFT + T`；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Scrape/Fill' |
| 修改 | `C` | `brush.asset_activate`（asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Clay Strips', active=False） | 默认：`C`；asset_library_type='ESSENTIALS', relative_asset_identifier='brushes/essentials_brushes-mesh_sculpt.blend/Brush/Clay Strips' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_sculpt'） | 默认：`SPACE`；name='VIEW3D_AST_brush_sculpt' |
| 修改 | `CTRL + SHIFT + RMB` | `paint.mask_lasso_gesture`（value=1.0） | 默认：`CTRL + SHIFT + LMB`；value=1.0 |
| 修改 | `CTRL + RMB` | `paint.mask_lasso_gesture`（value=0.0） | 默认：`CTRL + SHIFT + ALT + LMB`；value=0.0 |
| 新增 | `CTRL + F` | `paint.mask_flood_fill`（mode='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + A` | `paint.mask_flood_fill`（mode='VALUE'） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + D` | `sculpt.dynamic_topology_toggle` | Blender Default 中没有此绑定 |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.box_mask', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + LMB + 双击` | `sculpt.sample_color` | Blender Default 中没有此绑定 |
| 新增 | `C` | `wm.tool_set_by_id`（name='builtin.box_face_set', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `X` | `wm.tool_set_by_id`（name='builtin.lasso_trim', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `V` | `wm.tool_set_by_id`（name='builtin.lasso_hide', cycle=True） | Blender Default 中没有此绑定 |

### Sculpt Curves

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.curves_sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.curves_sculpt.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.curves_sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.curves_sculpt.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.curves_sculpt.brush.texture_slot.angle', color_path='tool_settings.curves_sculpt.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.curves_sculpt.brush', secondary_tex=False |
| 修改 | `CTRL + A` | `curves.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `curves.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `R` | `sculpt_curves.min_distance_edit` | 默认：`R` |
| 修改 | `SHIFT + A` | `sculpt_curves.select_grow` | 默认：`SHIFT + A` |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_sculpt_curves'） | 默认：`SPACE`；name='VIEW3D_AST_brush_sculpt_curves' |
| 新增 | `CTRL + F` | `curves.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Sculpt Expand Modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `B` | `BRUSH_GRADIENT_TOGGLE`（active=False） | 默认：`B` |

### Vertex Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.vertex_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.vertex_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | `CTRL + F` | `wm.radial_control`（data_path_primary='tool_settings.vertex_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False, active=False） | 默认：`CTRL + F`；data_path_primary='tool_settings.vertex_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.vertex_paint.brush.texture_slot.angle', color_path='tool_settings.vertex_paint.brush.cursor_color_add', fill_color_path='tool_settings.vertex_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.vertex_paint.brush', secondary_tex=False |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_paint_vertex_context_menu'） | 默认：`W`；name='VIEW3D_PT_paint_vertex_context_menu' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_vertex_paint'） | 默认：`SPACE`；name='VIEW3D_AST_brush_vertex_paint' |
| 新增 | `SHIFT + LMB + 双击` | `paint.sample_color` | Blender Default 中没有此绑定 |

### Weight Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False） | 默认：`F`；data_path_primary='tool_settings.weight_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False） | 默认：`SHIFT + F`；data_path_primary='tool_settings.weight_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | `CTRL + F` | `wm.radial_control`（data_path_primary='tool_settings.weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False, active=False） | 默认：`CTRL + F`；data_path_primary='tool_settings.weight_paint.brush.weight', data_path_secondary='tool_settings.unified_paint_settings.weight', use_secondary='tool_settings.unified_paint_settings.use_unified_weight', rotation_path='tool_settings.weight_paint.brush.texture_slot.angle', color_path='tool_settings.weight_paint.brush.cursor_color_add', fill_color_path='', fill_color_override_path='', fill_color_override_test_path='', zoom_path='', image_id='tool_settings.weight_paint.brush', secondary_tex=False |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_paint_weight_context_menu'） | 默认：`W`；name='VIEW3D_PT_paint_weight_context_menu' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_weight_paint'） | 默认：`SPACE`；name='VIEW3D_AST_brush_weight_paint' |
| 新增 | `ALT + LMB` | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + ALT + LMB` | `view3d.select`（toggle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + LMB` | `view3d.select` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + LMB + 双击` | `paint.weight_sample` | Blender Default 中没有此绑定 |

## 节点

### Node Editor

上下文：`NODE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 点击` | `node.select`（select_passthrough=True） | 默认：`LMB`；select_passthrough=True |
| 修改 | `CTRL + LMB + 点击` | `node.select` | 默认：`CTRL + LMB` |
| 修改 | `ALT + LMB + 点击` | `node.select` | 默认：`ALT + LMB` |
| 修改 | `CTRL + ALT + LMB + 点击` | `node.select` | 默认：`CTRL + ALT + LMB` |
| 修改 | `SHIFT + LMB + 点击` | `node.select`（toggle=True） | 默认：`SHIFT + LMB`；toggle=True |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `node.select`（toggle=True） | 默认：`CTRL + SHIFT + LMB`；toggle=True |
| 修改 | `SHIFT + ALT + LMB + 点击` | `node.select`（toggle=True） | 默认：`SHIFT + ALT + LMB`；toggle=True |
| 修改 | `CTRL + SHIFT + ALT + LMB + 点击` | `node.select`（toggle=True） | 默认：`CTRL + SHIFT + ALT + LMB`；toggle=True |
| 修改 | `LMB + 拖动` | `node.select_box`（tweak=True） | 默认：`RMB + 拖动`；tweak=True |
| 修改 | `B` | `node.select_box`（tweak=False, active=False） | 默认：`B`；tweak=False |
| 修改 | `ALT + RMB` | `node.backimage_sample` | 默认：`ALT + LMB` |
| 修改 | `F` | `node.link_make`（replace=False, active=False） | 默认：`J`；replace=False |
| 修改 | `SHIFT + F` | `node.link_make`（replace=True, active=False） | 默认：`SHIFT + J`；replace=True |
| 修改 | `F` | `node.join_named`（active=False） | 默认：`F` |
| 修改 | `CTRL + A` | `node.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `node.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `CTRL + SHIFT + F` | `node.find_node` | 默认：`CTRL + F` |
| 修改 | `TAB` | `node.group_edit`（exit=False, active=False） | 默认：`TAB`；exit=False |
| 修改 | `CTRL + TAB` | `node.group_edit`（exit=True, active=False） | 默认：`CTRL + TAB`；exit=True |
| 修改 | `LMB + 拖动` | `transform.translate`（view2d_edge_pan=True, release_confirm=True） | 默认：`LMB + 拖动`；release_confirm=True, view2d_edge_pan=True |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `ALT + RMB + 拖动` | `node.move_detach_links_release`（NODE_OT_translate_attach=[('TRANSFORM_OT_translate', [('view2d_edge_pan', True)])]） | 默认：`ALT + LMB + 拖动`；NODE_OT_translate_attach=[('TRANSFORM_OT_translate', [('view2d_edge_pan', True)])] |
| 修改 | `ALT + LMB + 拖动` | `node.move_detach_links`（TRANSFORM_OT_translate=[('view2d_edge_pan', True)]） | 默认：`ALT + RMB + 拖动`；TRANSFORM_OT_translate=[('view2d_edge_pan', True)] |
| 修改 | `RMB` | `wm.call_menu`（name='NODE_MT_context_menu'） | 默认：`W`；name='NODE_MT_context_menu' |
| 修改 | `MMB` | `transform.translate` | 默认：`RMB + 拖动`；release_confirm=True, view2d_edge_pan=True |
| 新增 | `CTRL + C` | `anyimage.track_native_copy` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + V` | `anyimage.paste_clipboard_image` | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `F + 双击` | `node.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `node.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `node.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + LMB + 双击` | `node.backimage_sample` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `node.duplicate_move` | Blender Default 中没有此绑定 |
| 新增 | `LMB + 双击` | `node.group_edit` | Blender Default 中没有此绑定 |
| 新增 | `ESC` | `node.group_edit`（exit=True） | Blender Default 中没有此绑定 |
| 新增 | `TAB` | `wm.call_menu`（name='NODE_MT_add'） | Blender Default 中没有此绑定 |
| 移除 | `RMB` | `node.select`（select_passthrough=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `CTRL + RMB` | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `ALT + RMB` | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `CTRL + ALT + RMB` | `node.select` | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `SHIFT + RMB` | `node.select`（toggle=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `CTRL + SHIFT + RMB` | `node.select`（toggle=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `SHIFT + ALT + RMB` | `node.select`（toggle=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `CTRL + SHIFT + ALT + RMB` | `node.select`（toggle=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `RMB + 点击` | `node.select`（deselect_all=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `LMB + 点击` | `node.select`（deselect_all=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `RMB + 拖动` | `node.translate_attach`（TRANSFORM_OT_translate=[('view2d_edge_pan', True)]） | 当前 Keymap 中没有此 Blender Default 绑定 |

### Node Generic

上下文：`NODE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |

## 动画

### Animation Channels

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + SHIFT + F` | `anim.channels_select_filter` | 默认：`CTRL + F` |
| 修改 | `CTRL + A` | `anim.channels_select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `anim.channels_select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `anim.channels_select_box`（active=False） | 默认：`B` |
| 修改 | `RMB` | `wm.call_menu`（name='DOPESHEET_MT_channel_context_menu'） | 默认：`W`；name='DOPESHEET_MT_channel_context_menu' |
| 新增 | `F` | `anim.channels_view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `anim.channels_select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Clip Graph Editor

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB` | `clip.graph_select` | 默认：`RMB` |
| 修改 | `SHIFT + LMB` | `clip.graph_select`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `CTRL + A` | `clip.graph_select_all_markers`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `clip.graph_select_all_markers`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `clip.graph_select_box`（active=False） | 默认：`B` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `SHIFT + RMB` | `clip.change_frame` | 默认：`LMB` |
| 新增 | `CTRL + F` | `clip.graph_select_all_markers`（action='INVERT'） | Blender Default 中没有此绑定 |

### Dopesheet

上下文：`DOPESHEET_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB` | `action.clickselect`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `ALT + LMB` | `action.clickselect`（column=True） | 默认：`ALT + RMB`；column=True |
| 修改 | `SHIFT + LMB` | `action.clickselect`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `SHIFT + ALT + LMB` | `action.clickselect`（extend=True, column=True） | 默认：`SHIFT + ALT + RMB`；extend=True, column=True |
| 修改 | `CTRL + ALT + LMB` | `action.clickselect`（channel=True） | 默认：`CTRL + ALT + RMB`；channel=True |
| 修改 | `CTRL + SHIFT + ALT + LMB` | `action.clickselect`（extend=True, channel=True） | 默认：`CTRL + SHIFT + ALT + RMB`；extend=True, channel=True |
| 修改 | `CTRL + LMB + 点击` | `action.select_leftright`（mode='CHECK'） | 默认：`CTRL + RMB + 点击`；mode='CHECK' |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `action.select_leftright`（mode='CHECK', extend=True） | 默认：`CTRL + SHIFT + RMB + 点击`；mode='CHECK', extend=True |
| 修改 | `CTRL + A` | `action.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `action.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `action.select_box`（axis_range=False, active=False） | 默认：`B`；axis_range=False |
| 修改 | `ALT + B` | `action.select_box`（axis_range=True, active=False） | 默认：`ALT + B`；axis_range=True |
| 修改 | `LMB + 拖动` | `action.select_box`（mode='SET', tweak=True） | 默认：`RMB + 拖动`；tweak=True, mode='SET' |
| 修改 | `SHIFT + LMB + 拖动` | `action.select_box`（mode='ADD', tweak=True） | 默认：`SHIFT + RMB + 拖动`；tweak=True, mode='ADD' |
| 修改 | `CTRL + LMB + 拖动` | `action.select_box`（mode='SUB', tweak=True） | 默认：`CTRL + RMB + 拖动`；tweak=True, mode='SUB' |
| 修改 | `CTRL + RMB + 拖动` | `action.select_lasso`（mode='ADD'） | 默认：`CTRL + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `action.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + SHIFT + F` | `anim.channels_select_filter` | 默认：`CTRL + F` |
| 修改 | `LMB + 拖动` | `transform.transform`（mode='TIME_TRANSLATE'） | 默认：`RMB + 拖动`；mode='TIME_TRANSLATE' |
| 修改 | `RMB` | `wm.call_menu`（name='DOPESHEET_MT_context_menu'） | 默认：`W`；name='DOPESHEET_MT_context_menu' |
| 修改 | `SHIFT + RMB` | `anim.change_frame` | 默认：`LMB` |
| 新增 | `F + 双击` | `view3d.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `action.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `action.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `action.duplicate_move` | Blender Default 中没有此绑定 |

### Graph Editor

上下文：`GRAPH_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB` | `graph.clickselect`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `ALT + LMB` | `graph.clickselect`（column=True） | 默认：`ALT + RMB`；column=True |
| 修改 | `SHIFT + LMB` | `graph.clickselect`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `SHIFT + ALT + LMB` | `graph.clickselect`（extend=True, column=True） | 默认：`SHIFT + ALT + RMB`；extend=True, column=True |
| 修改 | `CTRL + ALT + LMB` | `graph.clickselect`（curves=True） | 默认：`CTRL + ALT + RMB`；curves=True |
| 修改 | `CTRL + SHIFT + ALT + LMB` | `graph.clickselect`（extend=True, curves=True） | 默认：`CTRL + SHIFT + ALT + RMB`；extend=True, curves=True |
| 修改 | `CTRL + LMB + 点击` | `graph.select_leftright`（mode='CHECK'） | 默认：`CTRL + RMB + 点击`；mode='CHECK' |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `graph.select_leftright`（mode='CHECK', extend=True） | 默认：`CTRL + SHIFT + RMB + 点击`；mode='CHECK', extend=True |
| 修改 | `CTRL + A` | `graph.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `graph.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `graph.select_box`（active=False） | 默认：`B` |
| 修改 | `ALT + B` | `graph.select_box`（axis_range=True, active=False） | 默认：`ALT + B`；axis_range=True |
| 修改 | `LMB + 拖动` | `graph.select_box`（tweak=True, mode='SET'） | 默认：`RMB + 拖动`；tweak=True, mode='SET' |
| 修改 | `SHIFT + LMB + 拖动` | `graph.select_box`（tweak=True, mode='ADD'） | 默认：`SHIFT + RMB + 拖动`；tweak=True, mode='ADD' |
| 修改 | `CTRL + LMB + 拖动` | `graph.select_box`（tweak=True, mode='SUB'） | 默认：`CTRL + RMB + 拖动`；tweak=True, mode='SUB' |
| 修改 | `CTRL + RMB + 拖动` | `graph.select_lasso`（mode='ADD'） | 默认：`CTRL + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `graph.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + RMB + 点击` | `graph.click_insert` | 默认：`CTRL + LMB + 点击` |
| 修改 | `CTRL + SHIFT + RMB + 点击` | `graph.click_insert`（extend=True） | 默认：`CTRL + SHIFT + LMB + 点击`；extend=True |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `RMB` | `wm.call_menu`（name='GRAPH_MT_context_menu'） | 默认：`W`；name='GRAPH_MT_context_menu' |
| 修改 | `SHIFT + RMB` | `graph.cursor_set` | 默认：`LMB` |
| 新增 | `F + 双击` | `graph.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `graph.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `graph.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `graph.duplicate_move` | Blender Default 中没有此绑定 |

### Markers

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 拖动` | `marker.move`（tweak=True） | 默认：`RMB + 拖动`；tweak=True |
| 修改 | `LMB` | `marker.select` | 默认：`RMB` |
| 修改 | `SHIFT + LMB` | `marker.select`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `CTRL + LMB` | `marker.select`（camera=True） | 默认：`CTRL + RMB`；camera=True |
| 修改 | `CTRL + SHIFT + LMB` | `marker.select`（extend=True, camera=True） | 默认：`CTRL + SHIFT + RMB`；extend=True, camera=True |
| 修改 | `LMB + 拖动` | `marker.select_box`（tweak=True） | 默认：`RMB + 拖动`；tweak=True |
| 修改 | `SHIFT + LMB + 拖动` | `marker.select_box`（mode='ADD', tweak=True） | 默认：`SHIFT + RMB + 拖动`；tweak=True, mode='ADD' |
| 修改 | `CTRL + LMB + 拖动` | `marker.select_box`（mode='SUB', tweak=True） | 默认：`CTRL + RMB + 拖动`；tweak=True, mode='SUB' |
| 修改 | `B` | `marker.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + A` | `marker.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `marker.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 新增 | `CTRL + F` | `marker.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `marker.duplicate` | Blender Default 中没有此绑定 |

### NLA Editor

上下文：`NLA_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB` | `nla.click_select`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `SHIFT + LMB` | `nla.click_select`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `CTRL + LMB + 点击` | `nla.select_leftright`（mode='CHECK'） | 默认：`CTRL + RMB + 点击`；mode='CHECK' |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `nla.select_leftright`（mode='CHECK', extend=True） | 默认：`CTRL + SHIFT + RMB + 点击`；mode='CHECK', extend=True |
| 修改 | `CTRL + A` | `nla.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `nla.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `nla.select_box`（axis_range=False, active=False） | 默认：`B`；axis_range=False |
| 修改 | `ALT + B` | `nla.select_box`（axis_range=True, active=False） | 默认：`ALT + B`；axis_range=True |
| 修改 | `LMB + 拖动` | `nla.select_box`（tweak=True, mode='SET'） | 默认：`RMB + 拖动`；tweak=True, mode='SET' |
| 修改 | `SHIFT + LMB + 拖动` | `nla.select_box`（tweak=True, mode='ADD'） | 默认：`SHIFT + RMB + 拖动`；tweak=True, mode='ADD' |
| 修改 | `CTRL + LMB + 拖动` | `nla.select_box`（tweak=True, mode='SUB'） | 默认：`CTRL + RMB + 拖动`；tweak=True, mode='SUB' |
| 修改 | `ALT + D` | `nla.duplicate_linked_move` | 默认：`SHIFT + D` |
| 修改 | `SHIFT + D` | `nla.duplicate_move` | 默认：`ALT + D` |
| 修改 | `ALT + A` | `nla.apply_scale` | 默认：`CTRL + A` |
| 修改 | `ALT + E` | `nla.clear_scale` | 默认：`ALT + S` |
| 修改 | `LMB + 拖动` | `transform.transform`（mode='TRANSLATION'） | 默认：`RMB + 拖动`；mode='TRANSLATION' |
| 修改 | `RMB` | `wm.call_menu`（name='NLA_MT_context_menu'） | 默认：`W`；name='NLA_MT_context_menu' |
| 修改 | `SHIFT + RMB` | `anim.change_frame`（seq_solo_preview=True） | 默认：`LMB`；seq_solo_preview=True |
| 新增 | `F + 双击` | `nla.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `nla.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `nla.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `nla.duplicate_move` | Blender Default 中没有此绑定 |

## 图像与 UV

### Image

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `RMB` | `image.sample` | 默认：`LMB` |
| 修改 | `CTRL + RMB` | `image.curves_point_set`（point='BLACK_POINT'） | 默认：`CTRL + LMB`；point='BLACK_POINT' |
| 修改 | `SHIFT + RMB` | `image.curves_point_set`（point='WHITE_POINT'） | 默认：`SHIFT + LMB`；point='WHITE_POINT' |
| 修改 | `FOUR` | `object.mode_set`（mode='OBJECT', toggle=False） | 默认：`TAB`；mode='EDIT', toggle=True |
| 修改 | `RMB` | `wm.call_menu`（name='IMAGE_MT_mask_context_menu'） | 默认：`W`；name='IMAGE_MT_mask_context_menu' |
| 新增 | `SHIFT + LMB + 双击` | `image.sample` | Blender Default 中没有此绑定 |
| 新增 | `F` | `image.view_all`（fit_view=True） | Blender Default 中没有此绑定 |

### Image Editor Tool: Uv, Grab

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.size'） | 默认：`F`；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.strength'） | 默认：`SHIFT + F`；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Editor Tool: Uv, Pinch

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.size'） | 默认：`F`；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.strength'） | 默认：`SHIFT + F`；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Editor Tool: Uv, Relax

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.size'） | 默认：`F`；data_path_primary='tool_settings.uv_sculpt.size' |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.uv_sculpt.strength'） | 默认：`SHIFT + F`；data_path_primary='tool_settings.uv_sculpt.strength' |

### Image Generic

上下文：`IMAGE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |

### Image Paint

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `S` | `wm.radial_control`（data_path_primary='tool_settings.image_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='space_data.zoom', image_id='tool_settings.image_paint.brush', secondary_tex=True） | 默认：`F`；data_path_primary='tool_settings.image_paint.brush.size', data_path_secondary='tool_settings.unified_paint_settings.size', use_secondary='tool_settings.unified_paint_settings.use_unified_size', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='space_data.zoom', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | `ALT + S` | `wm.radial_control`（data_path_primary='tool_settings.image_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True） | 默认：`SHIFT + F`；data_path_primary='tool_settings.image_paint.brush.strength', data_path_secondary='tool_settings.unified_paint_settings.strength', use_secondary='tool_settings.unified_paint_settings.use_unified_strength', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | `CTRL + F` | `wm.radial_control`（data_path_primary='tool_settings.image_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=False, active=False） | 默认：`CTRL + F`；data_path_primary='tool_settings.image_paint.brush.texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=False |
| 修改 | `CTRL + ALT + F` | `wm.radial_control`（data_path_primary='tool_settings.image_paint.brush.mask_texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True, active=False） | 默认：`CTRL + ALT + F`；data_path_primary='tool_settings.image_paint.brush.mask_texture_slot.angle', data_path_secondary='', use_secondary='', rotation_path='tool_settings.image_paint.brush.mask_texture_slot.angle', color_path='tool_settings.image_paint.brush.cursor_color_add', fill_color_path='tool_settings.image_paint.brush.color', fill_color_override_path='tool_settings.unified_paint_settings.color', fill_color_override_test_path='tool_settings.unified_paint_settings.use_unified_color', zoom_path='', image_id='tool_settings.image_paint.brush', secondary_tex=True |
| 修改 | `RMB` | `wm.call_panel`（name='VIEW3D_PT_paint_texture_context_menu'） | 默认：`W`；name='VIEW3D_PT_paint_texture_context_menu' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='VIEW3D_AST_brush_texture_paint'） | 默认：`SPACE`；name='VIEW3D_AST_brush_texture_paint' |
| 修改 | `B` | `wm.call_asset_shelf_popover`（name='IMAGE_AST_brush_paint'） | 默认：`SPACE`；name='IMAGE_AST_brush_paint' |
| 新增 | `SHIFT + LMB + 双击` | `paint.sample_color` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + SHIFT + LMB + 双击` | `paint.sample_color`（merged=True） | Blender Default 中没有此绑定 |

### UV Editor

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 点击` | `uv.select`（deselect_all=True） | 默认：`RMB + 点击`；deselect_all=True |
| 修改 | `SHIFT + LMB + 点击` | `uv.select`（toggle=True） | 默认：`SHIFT + RMB`；toggle=True |
| 修改 | `ALT + LMB + 点击` | `uv.select_loop` | 默认：`ALT + RMB` |
| 修改 | `SHIFT + ALT + LMB + 点击` | `uv.select_loop`（extend=True） | 默认：`SHIFT + ALT + RMB`；extend=True |
| 修改 | `CTRL + ALT + LMB + 点击` | `uv.select_edge_ring` | 默认：`CTRL + ALT + RMB` |
| 修改 | `CTRL + SHIFT + ALT + LMB + 点击` | `uv.select_edge_ring`（extend=True） | 默认：`CTRL + SHIFT + ALT + RMB`；extend=True |
| 修改 | `CTRL + LMB + 点击` | `uv.shortest_path_pick`（use_fill=False） | 默认：`CTRL + RMB`；use_fill=False |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `uv.shortest_path_pick`（use_fill=True） | 默认：`CTRL + SHIFT + RMB`；use_fill=True |
| 修改 | `B` | `uv.select_box`（pinned=False, active=False） | 默认：`B`；pinned=False |
| 修改 | `CTRL + B` | `uv.select_box`（pinned=True, active=False） | 默认：`CTRL + B`；pinned=True |
| 修改 | `CTRL + RMB + 拖动` | `uv.select_lasso`（mode='ADD'） | 默认：`CTRL + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `uv.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + A` | `uv.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `uv.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `RMB` | `wm.call_menu`（name='IMAGE_MT_uvs_context_menu'） | 默认：`W`；name='IMAGE_MT_uvs_context_menu' |
| 修改 | `SHIFT + RMB` | `uv.cursor_set` | 默认：`LMB + 点击` |
| 新增 | `SHIFT + RMB + 拖动` | `transform.translate`（cursor_transform=True, release_confirm=True） | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `uv.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 移除 | `RMB` | `uv.select`（deselect_all=True, select_passthrough=True） | 当前 Keymap 中没有此 Blender Default 绑定 |

## 视频、跟踪与遮罩

### Clip

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |

### Clip Editor

上下文：`CLIP_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB` | `clip.select`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `SHIFT + LMB` | `clip.select`（extend=True） | 默认：`SHIFT + RMB`；extend=True |
| 修改 | `CTRL + A` | `clip.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `clip.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `clip.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + ALT + RMB + 拖动` | `clip.select_lasso`（mode='ADD'） | 默认：`CTRL + ALT + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + ALT + RMB + 拖动` | `clip.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + ALT + LMB + 拖动`；mode='SUB' |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `SHIFT + RMB` | `clip.cursor_set` | 默认：`LMB + 点击` |
| 修改 | `RMB` | `wm.call_menu`（name='CLIP_MT_tracking_context_menu'） | 默认：`W`；name='CLIP_MT_tracking_context_menu' |
| 新增 | `F + 双击` | `clip.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `clip.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `clip.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Mask Editing

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `SHIFT + LMB` | `mask.select`（toggle=True） | 默认：`SHIFT + RMB`；toggle=True |
| 修改 | `CTRL + A` | `mask.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `mask.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `mask.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + ALT + RMB + 拖动` | `mask.select_lasso`（mode='ADD'） | 默认：`CTRL + ALT + LMB + 拖动`；mode='ADD' |
| 修改 | `CTRL + SHIFT + ALT + RMB + 拖动` | `mask.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + ALT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + LMB` | `clip.select` | 默认：`CTRL + RMB` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `SHIFT + RMB` | `uv.cursor_set` | 默认：`LMB + 点击` |
| 新增 | `SHIFT + RMB + 拖动` | `transform.translate`（cursor_transform=True, release_confirm=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `mask.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `mask.duplicate_move` | Blender Default 中没有此绑定 |
| 移除 | `RMB` | `mask.select`（deselect_all=True） | 当前 Keymap 中没有此 Blender Default 绑定 |

### Paint Face Mask (Weight, Vertex, Texture)

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `paint.face_select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `paint.face_select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `CTRL + SHIFT + RMB + 拖动` | `view3d.select_lasso`（mode='SUB'） | 默认：`CTRL + SHIFT + LMB + 拖动`；mode='SUB' |
| 修改 | `CTRL + RMB + 拖动` | `view3d.select_lasso`（mode='ADD'） | 默认：`CTRL + SHIFT + ALT + LMB + 拖动`；mode='ADD' |
| 新增 | `CTRL + F` | `paint.face_select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 移除 | `ALT + RMB` | `paint.face_select_loop`（extend=False, select=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `SHIFT + ALT + RMB` | `paint.face_select_loop`（extend=True, select=True） | 当前 Keymap 中没有此 Blender Default 绑定 |
| 移除 | `CTRL + SHIFT + ALT + RMB` | `paint.face_select_loop`（extend=True, select=False） | 当前 Keymap 中没有此 Blender Default 绑定 |

### Preview

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 点击` | `sequencer.select`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `SHIFT + LMB + 点击` | `sequencer.select`（toggle=True） | 默认：`SHIFT + RMB`；toggle=True |
| 修改 | `CTRL + LMB + 点击` | `sequencer.select`（center=True） | 默认：`CTRL + RMB`；center=True |
| 修改 | `ALT + LMB + 点击` | `sequencer.select`（ignore_connections=True） | 默认：`ALT + RMB`；ignore_connections=True |
| 修改 | `CTRL + SHIFT + LMB + 点击` | `sequencer.select`（toggle=True, center=True） | 默认：`CTRL + SHIFT + RMB`；toggle=True, center=True |
| 修改 | `SHIFT + ALT + LMB + 点击` | `sequencer.select`（toggle=True, ignore_connections=True） | 默认：`SHIFT + ALT + RMB`；toggle=True, ignore_connections=True |
| 修改 | `CTRL + A` | `sequencer.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `sequencer.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `sequencer.select_box`（active=False） | 默认：`B` |
| 修改 | `R + 双击` | `transform.rotate` | 默认：`R` |
| 修改 | `S` | `transform.resize`（active=False） | 默认：`S` |
| 修改 | `LMB + 拖动` | `transform.translate` | 默认：`RMB + 拖动` |
| 修改 | `ALT + W` | `sequencer.strip_transform_clear`（property='POSITION'） | 默认：`ALT + G`；property='POSITION' |
| 修改 | `ALT + R` | `sequencer.strip_transform_clear`（property='SCALE'） | 默认：`ALT + S`；property='SCALE' |
| 修改 | `ALT + E` | `sequencer.strip_transform_clear`（property='ROTATION'） | 默认：`ALT + R`；property='ROTATION' |
| 修改 | `RMB` | `wm.call_menu`（name='SEQUENCER_MT_preview_context_menu'） | 默认：`W`；name='SEQUENCER_MT_preview_context_menu' |
| 修改 | `SHIFT + RMB` | `sequencer.cursor_set` | 默认：`LMB + 点击` |
| 新增 | `SHIFT + RMB + 拖动` | `transform.translate`（cursor_transform=True, release_confirm=True） | Blender Default 中没有此绑定 |
| 新增 | `F + 双击` | `sequencer.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `sequencer.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.move', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `R` | `wm.tool_set_by_id`（name='builtin.rotate', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `E` | `wm.tool_set_by_id`（name='builtin.scale', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `sequencer.preview_duplicate_move` | Blender Default 中没有此绑定 |

### Sequencer

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 点击` | `sequencer.select`（deselect_all=True） | 默认：`RMB`；deselect_all=True |
| 修改 | `SHIFT + LMB + 点击` | `sequencer.select`（toggle=True） | 默认：`SHIFT + RMB`；toggle=True |
| 修改 | `CTRL + LMB` | `sequencer.select`（linked_time=True） | 默认：`CTRL + RMB`；linked_time=True |
| 修改 | `CTRL + SHIFT + LMB` | `sequencer.select`（extend=True, linked_time=True） | 默认：`CTRL + SHIFT + RMB`；linked_time=True, extend=True |
| 修改 | `CTRL + LMB + 点击` | `sequencer.select`（side_of_frame=True） | 默认：`CTRL + RMB + 点击`；side_of_frame=True |
| 修改 | `ALT + LMB` | `sequencer.select`（deselect_all=True, ignore_connections=True） | 默认：`ALT + RMB`；deselect_all=True, ignore_connections=True |
| 修改 | `SHIFT + ALT + LMB` | `sequencer.select`（toggle=True, ignore_connections=True） | 默认：`SHIFT + ALT + RMB`；toggle=True, ignore_connections=True |
| 修改 | `LMB + 拖动` | `sequencer.select_box`（mode='SET', tweak=True） | 默认：`RMB + 拖动`；tweak=True, mode='SET' |
| 修改 | `SHIFT + LMB + 拖动` | `sequencer.select_box`（mode='ADD', tweak=True） | 默认：`SHIFT + RMB + 拖动`；tweak=True, mode='ADD' |
| 修改 | `CTRL + LMB + 拖动` | `sequencer.select_box`（mode='SUB', tweak=True） | 默认：`CTRL + RMB + 拖动`；tweak=True, mode='SUB' |
| 修改 | `ALT + LMB + 拖动` | `sequencer.select_box`（mode='SET', tweak=True, ignore_connections=True） | 默认：`ALT + RMB + 拖动`；tweak=True, ignore_connections=True, mode='SET' |
| 修改 | `B` | `sequencer.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + B` | `sequencer.select_box`（include_handles=True, active=False） | 默认：`CTRL + B`；include_handles=True |
| 修改 | `CTRL + A` | `sequencer.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `sequencer.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `LMB + 拖动` | `transform.seq_slide`（use_restore_handle_selection=True, view2d_edge_pan=True） | 默认：`RMB + 拖动`；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | `ALT + LMB + 拖动` | `transform.seq_slide`（use_restore_handle_selection=True, view2d_edge_pan=True） | 默认：`ALT + RMB + 拖动`；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | `CTRL + LMB + 拖动` | `transform.seq_slide`（use_restore_handle_selection=True, view2d_edge_pan=True） | 默认：`CTRL + RMB + 拖动`；view2d_edge_pan=True, use_restore_handle_selection=True |
| 修改 | `RMB` | `wm.call_menu`（name='SEQUENCER_MT_context_menu'） | 默认：`W`；name='SEQUENCER_MT_context_menu' |
| 新增 | `F + 双击` | `sequencer.view_all` | Blender Default 中没有此绑定 |
| 新增 | `F` | `sequencer.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `B` | `sequencer.split` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + B` | `sequencer.split`（type='HARD'） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + D` | `sequencer.duplicate_move` | Blender Default 中没有此绑定 |

## 文件、资源与 Outliner

### File Browser

上下文：`FILE_BROWSER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |
| 修改 | `RMB` | `file.select`（open=False, only_activate_if_selected=True, pass_through=True） | 默认：`RMB`；open=False, only_activate_if_selected=False, pass_through=True |
| 修改 | `RMB` | `wm.call_menu`（name='FILEBROWSER_MT_context_menu'） | 默认：`W`；name='FILEBROWSER_MT_context_menu' |

### File Browser Main

上下文：`FILE_BROWSER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `file.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `file.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `file.select_box`（active=False） | 默认：`B` |
| 修改 | `RMB` | `wm.call_menu`（name='ASSETBROWSER_MT_context_menu'） | 默认：`W`；name='ASSETBROWSER_MT_context_menu' |
| 新增 | `LMB + 双击` | `poselib.apply_pose_asset` | Blender Default 中没有此绑定 |
| 新增 | `F` | `file.view_selected` | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `file.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Outliner

上下文：`OUTLINER / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `LMB + 双击` | `outliner.item_activate`（deselect_all=True, recurse=True） | 默认：`LMB + 双击`；recurse=True, deselect_all=True |
| 修改 | `CTRL + LMB + 双击` | `outliner.item_activate`（extend=True, deselect_all=True, recurse=True） | 默认：`CTRL + LMB + 双击`；recurse=True, extend=True, deselect_all=True |
| 修改 | `SHIFT + LMB + 双击` | `outliner.item_activate`（extend_range=True, deselect_all=True, recurse=True） | 默认：`SHIFT + LMB + 双击`；recurse=True, extend_range=True, deselect_all=True |
| 修改 | `CTRL + SHIFT + LMB + 双击` | `outliner.item_activate`（extend=True, extend_range=True, deselect_all=True, recurse=True） | 默认：`CTRL + SHIFT + LMB + 双击`；recurse=True, extend=True, extend_range=True, deselect_all=True |
| 修改 | `B` | `outliner.select_box`（active=False） | 默认：`B` |
| 修改 | `CTRL + A` | `outliner.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `CTRL + SHIFT + F` | `outliner.start_filter` | 默认：`CTRL + F` |
| 新增 | `CTRL + F` | `outliner.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |
| 新增 | `F` | `outliner.show_active` | Blender Default 中没有此绑定 |
| 新增 | `SHIFT + F` | `outliner.show_hierarchy` | Blender Default 中没有此绑定 |

## 其他编辑器

### Gesture Straight Line

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `F` | `FLIP`（active=False） | 默认：`F` |

### Info

上下文：`INFO / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + A` | `info.select_all`（action='SELECT'） | 默认：`A`；action='SELECT' |
| 修改 | `ALT + A` | `info.select_all`（action='DESELECT', active=False） | 默认：`ALT + A`；action='DESELECT' |
| 修改 | `B` | `info.select_box`（active=False） | 默认：`B` |
| 修改 | `RMB` | `wm.call_menu`（name='INFO_MT_context_menu'） | 默认：`W`；name='INFO_MT_context_menu' |
| 新增 | `CTRL + F` | `info.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### Knife Tool Modal Map

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 新增 | `Q` | `X_AXIS` | Blender Default 中没有此绑定 |
| 新增 | `W` | `Y_AXIS` | Blender Default 中没有此绑定 |
| 新增 | `E` | `Z_AXIS` | Blender Default 中没有此绑定 |

### Property Editor

上下文：`PROPERTIES / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `CTRL + SHIFT + F` | `buttons.start_filter` | 默认：`CTRL + F` |
| 修改 | `ALT + A` | `object.modifier_apply`（report=True） | 默认：`CTRL + A`；report=True |
| 修改 | `ALT + A` | `constraint.apply`（report=True） | 默认：`CTRL + A`；report=True |
| 新增 | `CTRL + D` | `constraint.copy` | Blender Default 中没有此绑定 |

### Spreadsheet Generic

上下文：`SPREADSHEET / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_channels', active=False） | 默认：`T`；data_path='space_data.show_region_channels' |

### Video Sequence Editor

上下文：`SEQUENCE_EDITOR / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `T` | `wm.context_toggle`（data_path='space_data.show_region_toolbar', active=False） | 默认：`T`；data_path='space_data.show_region_toolbar' |
| 新增 | `W` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True, active=False） | Blender Default 中没有此绑定 |
| 新增 | `Q` | `wm.tool_set_by_id`（name='builtin.select_box', cycle=True） | Blender Default 中没有此绑定 |
| 新增 | `CTRL + F` | `sequencer.select_all`（action='INVERT'） | Blender Default 中没有此绑定 |

### View3D Walk Modal

上下文：`EMPTY / WINDOW`

| 类型 | 当前按键 | Operator | 与 Blender Default 的差异 |
| --- | --- | --- | --- |
| 修改 | `V` | `JUMP` | 默认：`V` |
| 修改 | `V + 松开` | `JUMP_STOP` | 默认：`V + 松开` |
| 修改 | `SPACE` | `TELEPORT`（active=False） | 默认：`SPACE` |
| 新增 | `SPACE` | `JUMP` | Blender Default 中没有此绑定 |
| 新增 | `SPACE` | `JUMP_STOP` | Blender Default 中没有此绑定 |
