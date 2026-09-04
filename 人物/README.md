# 人物 / Characters

角色资产：**角色 spec JSON + 侧面参考图**。同一角色跨镜头、跨项目一致复用的最小单元。

## 目录约定

```
人物/
├── <角色名>/
│   ├── char_spec.json      # 纯数据角色定义（可直接喂给 cast.Character(spec)）
│   └── reference/          # 侧面轮廓原画 / 配色参考图
│       └── <view>.png
```

## char_spec.json 字段

继承技能 `cast.HERO_SPEC` 的结构：

| 字段 | 说明 |
| --- | --- |
| `name` | 角色名 |
| `rig` | 骨骼系统（`human_q` 两足 / `quadruped_q` 四足） |
| `style` | 画风名（映射到技能 16 套画风预设） |
| `H` | 身高（u 比例尺，`u = H / 4.0`） |
| `colors` | 部件 → 语义色名映射（`Outline/Body/Hair/Mouth/...`） |
| `fill_opacity` | 各部件填充不透明度 |
| `far_tint` | 远侧肢体调暗系数（默认 0.72） |
| `accessories` | 配件列表（如 `hair_bowl` 碗盖发 / `scarf` 围巾） |

## 已入库

- [hero](hero/) — 技能默认主角 `HERO_SPEC`（碗盖发 + 围巾）
- [pilot](pilot/) — 飞行视角角色（侧面参考图已入库，spec 待补充）

## 取用

```python
from cast import Character
ch = Character(load_spec("hero/char_spec.json"))
ch.draw(drs, st, frame, ("idle", t), expr="happy")
```

新增角色：在子目录放 `char_spec.json` + 参考图，并在此表登记一行。