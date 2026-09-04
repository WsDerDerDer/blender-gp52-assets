# 姿态资产

动作线站姿模板（I/C/S/Z + contrapposto 承重腿参数）。

- **格式**：`gesture.json`（LINE/amount/weight 参数，接 skill `gesture.py`）
- **消费端**：`gesture.pose_from` 直接喂 `solve()`
- **检索**：`asset_cli.py search -c 姿态 -k contrapposto`
- 首批试点：S 型 contrapposto 站姿