# 镜头资产

运镜/转场模板（pan/zoom/shake 参数 + 转场类型），无独立样张。

- **格式**：`camera.json`（运镜参数化，接 Stage 相机语言 + cut.py 转场）
- **消费端**：`Stage.cam_pan/cam_zoom/cam_shake` + `cut.py` 转场
- **检索**：`asset_cli.py search -c 镜头 -k cross`
- 首批试点：cross 淡入淡出转场