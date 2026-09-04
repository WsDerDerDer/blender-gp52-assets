# 沙滩海岸

沙滩 + 海洋双区场景模板。

## 坐标约定

- **海岸线 = Y=0**：沙滩与海洋自然衔接，无需拼接
- 沙滩：`Y ∈ [0, Beach Length]`（参数 `Beach Length`）
- 海洋：`Y ∈ [-Ocean Length, 0]`（参数 `Ocean Length`）

## 可调参数（Geometry Nodes 面板）

| 参数 | 说明 |
| --- | --- |
| Beach Length | 沙滩纵深 |
| Ocean Length | 海洋纵深 |
| 分辨率 | 网格细分密度 |
| 噪声尺寸 | 地形波浪特征尺度 |

## StoreNamedAttribute 关键属性

- 沙滩：`shore_distance`（距海岸线距离）、`sand_grain`（沙粒 → 沙滩材质）
- 海水：`shore_depth`（水深）、`foam`（泡沫 → 海水材质）

## 参考实现

- 生成脚本：技能目录 `scripts/beach_scene.py`
- 完整工程样板（2026-09-04）：`d:\desktop\trae\test\jelly_beach_gpv3\`（`jb_common.py` 封装 GPv3 全部修复，分模块 `jb_part1~5` 生成）
- 海洋场景配色样张：`cartoon_boat`（storybook 色板）