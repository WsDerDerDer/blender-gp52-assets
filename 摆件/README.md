# 摆件 / Props

手持道具、环境摆件与装饰物。**当前暂无入库素材**，目录结构与约定先行。

## 目录约定

```
摆件/<摆件名>/
├── prop_spec.py    # 绘制函数（统一签名 fn(dr, idx, pal, x, y, s, ang)）
├── preview/        # 渲染样张（可选）
└── README.md       # 挂点/锚点、尺寸、动效说明
```

## 签名约定（来自技能 scripts/fx_props.py 原型）

- 统一签名：`fn(dr, idx, pal, x, y, s, ang)`
  - `x, y` = 挂点世界坐标（如手部锚点）
  - `s` = 尺度（u，可并入弹入缩放）
  - `ang` = 跟随旋转角（度），锚点随前臂世界角转动
- 情绪符号与手持道具分类参照 `fx_props.py` 的 `EMOTES` / `PROPS` 注册表

## 可借鉴参考

- 渔船：`gp_work/scripts/cartoon_boat.py`（storybook 色板样张）
- 手机/弹窗/单据：`gp_work/scripts/kit.py`（扁平商务信息图图元）

入库时在此表登记一行。