# blender-gp52-assets

**Blender 5.2 Grease Pencil（GPv3）创作可复用素材库**。

配合技能 `blender-grease-pencil-52` 使用：素材按 13 类分类存储，创作前
`asset_cli.py search` 查库、复用后 `asset_cli.py auto` 自动沉淀、`sync push` 回云。

## 分类（13 类，category 中英双字段，index.json 枚举只增不改）

| 目录 | 内容 | 素材格式 | 消费端 |
|---|---|---|---|
| [人物/](人物/) | 角色 spec + 侧面参考图 | `char_spec.json` + `reference/` | `cast.Character` |
| [动物/](动物/) | 四足/飞行/水生角色模板变体 | `char_spec.json`（rig_type 记模板） | `cast` + `quadruped_q` |
| [摆件/](摆件/) | 手持道具 / 环境装饰 | `prop_spec.py`（确定性 builder） | `scene.py` 元素 |
| [载具/](载具/) | 船/车/飞机 | `prop_spec.py` + 尺寸/浮力约定 | 直接 import builder |
| [场景/](场景/) | 整场模板 + 坐标约定 | `scene.json` + README | `scene.py` + `scene_run` |
| [场景元素/](场景元素/) | 云/海/山/植物（背景层） | `prop_spec.py` 或元素 builder | `scene.py` BG/MG 组 |
| [特效/](特效/) | 循环/单帧特效参数集 | `fx.json` | `fx.py` |
| [文字UI/](文字UI/) | 字幕/标题/气泡/打字机样式 | `text_style.json` + 字体约定 | `text_native`/`gp_text` |
| [动作/](动作/) | 角色关键帧动作（循环安全） | `xxx.json`（keys/bob） | `animate` `clip:<名>` |
| [表情口型/](表情口型/) | 表情矩阵 / emotes / flap 口型 | `expressions.json` + `flap.json` | `cast` 表情切片 |
| [姿态/](姿态/) | 动作线站姿模板 I/C/S/Z | `gesture.json` | `gesture.pose_from` |
| [画风/](画风/) | 画风预设索引（本体在 style.py） | `style_index.md` | `Stage(style=)` |
| [镜头/](镜头/) | 运镜/转场模板 | `camera.json` | `Stage` 相机语言 + `cut.py` |

**A 类（图形素材：人物/动物/摆件/载具/场景/场景元素/特效/文字UI）必有样张**（PNG <2MB）；**B 类（参数模板：动作/表情口型/姿态/画风/镜头）无单帧样张但必附 verify 输出**。

## 素材格式约定

- **角色**：`char_spec.json` 为纯数据的角色定义（rig / 身高 / 语义色名配色 / 配件），可直接被 `cast.Character(spec)` 使用；参考图为侧面轮廓原画。

- **动作**：JSON 含 `name / rig / loop / frames / bob / keys`，`keys` 为 `[帧号, 关节角字典, 缓动]`，帧号以 1 开头、收尾帧闭合保证循环。整数周期帧数（如 24/32）→ 与项目 12fps 对齐无缝循环。

- **语义色名**：`outline / main_1 / main_2 / sub_1 / sub_2 / accent` 固定槽位，经 `palette.resolve_color` 映射到当前画风，不写死 sRGB 值。

- **颜色一律 sRGB→linear 再赋值**（技能铁律，见技能 SKILL.md）。

## 命名规范（检索优先）

- 分类目录 = 中文（如上表）；**实体 ID 一律 `kebab-case` 英文**（禁空格/大写/中文，路径与 CLI 安全）
- 材料文件名固定：角色 `char_spec.json` · 动作 `<实体>.json`（平铺） · 摆件/载具 `prop_spec.py` · 场景 `scene.json` · 特效 `fx.json` · 文字 `text_style.json` · 表情 `expressions.json` · 姿态 `gesture.json` · 镜头 `camera.json`
- 版本：`version: N` 整数递增；样张 `reference/<id>_v<N>.png`；引用 `人物/hero@v3`
- 全库索引 `index.json` 由 `asset_cli.py index` 自动生成，push 前强制刷新

## 使用方式（建议走 skill CLI，不手动 git）

```bash
# 定位库（env GP_ASSETS 优先，否则探测 cwd/上级，再否则旁路 clone）
asset_cli.py sync pull                 # 拉最新
asset_cli.py search -k 云 -c 场景元素   # 按中英文关键词/分类/标签检索
asset_cli.py resolve 人物/hero@v1 -o gp_work/assets   # 复制进项目 + 记来源
# 沉淀（P1）：验收 PASS 后
asset_cli.py auto                      # 三信号自动提炼 → staging 确认
asset_cli.py sync push                 # 自动刷 index → commit → push
```

## 贡献新素材

1. 新建/更新素材文件（材料文件名固定 + `index.json` 自动登记）
2. 附上可验证的产出（样例：样张渲染帧、spec/verify 断言输出）
3. `asset_cli.py sync push` 到主分支（素材体积大时以压缩包形式入库，避免单文件 > 100MB）

