# 动作 / Actions

角色关键帧动作库。每个 JSON 为一个**循环安全**的动作（整数周期帧数，12fps 无缝循环）。

## JSON 格式

```json
{
  "name": "wave",
  "rig": "human_q_v2",
  "loop": true,
  "frames": 24,
  "bob": { "amp": 0.0, "freq": 1 },
  "keys": [
    [1,  {"upper_arm_L": 140.0}, "ease_in_out"],
    [6,  {"upper_arm_L": 175.0}, "ease_in_out"],
    [24, {"upper_arm_L": 140.0}, "linear"]
  ]
}
```

| 字段 | 说明 |
| --- | --- |
| `name` | 动作名 |
| `rig` | 适用的骨骼系统 |
| `loop` | 是否循环（首帧 = 尾帧闭合） |
| `frames` | 总帧数（**整数周期**，如 24/32，保证循环平滑） |
| `bob` | 上下浮动（`amp` 振幅 / `freq` 频率） |
| `keys` | `[帧号(1 起), 关节角/头角字典, 缓动]` |

## 已入库

| 动作 | 帧数 | 说明 |
| --- | --- | --- |
| [wave](wave.json) | 24 | 挥手（近臂胸前摆动） |
| [nod](nod.json) | 24 | 点头（带轻微下浮 bob） |
| [shake_head](shake_head.json) | 32 | 摇头 |

## 取用

动作 JSON 可被画帧逻辑读取为关节角插值；也可直接用技能内置 `ACTIONS = {walk, idle, run, talk}`（代码级动作）。