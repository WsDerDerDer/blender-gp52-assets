# 载具资产

船 / 车 / 飞机等可动载具（确定性参数化 builder，含尺寸/浮力/速度约定）。

- **格式**：`prop_spec.py`（确定性 builder + params，接 shape_lib/line_weight/明度/阴影全规则）
- **原型样板**：skill `scripts/cartoon_boat.py`（8 秒循环木船）
- **消费端**：`scene.py` 元素 / 直接 import builder
- 首批试点：卡通木船