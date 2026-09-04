# 场景元素资产

云 / 海 / 山 / 植物等可独立复用的场景元素（与"摆件"的区别：摆件靠近镜头可交互，场景元素属背景层）。

- **格式**：`prop_spec.py` 或元素 builder（确定性，接 shape_lib 圆弧并集）
- **消费端**：`scene.py` 元素系统（BG/MG 组）
- **检索**：`asset_cli.py search -c 场景元素 -k 云`
- 首批试点：卡通云（shape_lib.radial_union 圆弧并集）