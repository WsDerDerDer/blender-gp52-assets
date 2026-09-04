# 画风 / Styles

画风预设与色板约定。

## 说明

技能 `blender-grease-pencil-52` 内置 **16 套画风预设**（定义于技能目录 `scripts/style.py`，纯数据、零 bpy 依赖）。本目录不复制技能代码，只登记约定与索引，避免双源漂移。

## 约定

- **语义色名槽位固定**（≤7 色禁超）：`bg / outline / main_1 / main_2 / sub_1 / sub_2 / accent`
- 取色唯一入口：`palette.resolve_color`（语义色名 / hex / 元组，默认 `storybook`）
- 线宽档位：`outline`（基准）/ `detail`（基准 `ortho_scale = 16`）
- 暗底风格（`horror` / `night-glow`）验收阈值按 0.15% 判定（亮底 0.03%）

## 登记

| 画风 | 用途提示 |
| --- | --- |
| storybook | 通用卡通（默认，hero / 渔船样板） |
| horror | 暗底恐怖 |
| night-glow | 夜景发光 |
| ...（其余见 style.py 预设表） | |

需要把某套画风的色板快照版本化入库时，在本目录导出 `snapshot/<画风名>.json`。样张生成：技能 `scripts/demo_styles.py` → `style_chart.png`。