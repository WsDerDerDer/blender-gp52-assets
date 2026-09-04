# 表情/口型资产

6 表情矩阵参数 + 情绪符号（emotes）+ 口型 flap 对齐参数。

- **格式**：`expressions.json`（表情组）+ `flap.json`（口型时间窗）
- **消费端**：`cast` 表情切片 + 口型对齐（video-pipeline 公式）
- **检索**：`asset_cli.py search -c 表情口型 -k 开心`
- 首批试点：6 表情矩阵（demo_expressions）