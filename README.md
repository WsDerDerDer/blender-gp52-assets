# blender-gp52-assets

**Blender 5.2 Grease Pencil（GPv3）创作可复用素材库**。

配合技能 `blender-grease-pencil-52` 使用：素材按「人物 / 场景 / 摆件 / 动作 / 画风」分类存储，创作时直接取用、跨项目复用。

## 分类

| 目录 | 内容 | 素材格式 |
| --- | --- | --- |
| [人物/](人物/) | 角色资产：角色 spec（JSON 可序列化）+ 侧面参考图 | `char_spec.json` + `reference/*.png` |
| [场景/](场景/) | 场景模板与坐标/参数约定（如沙滩海岸） | 每场景一个子目录，README 记录约定 |
| [摆件/](摆件/) | 手持道具 / 环境摆件 / 装饰物 | 待入库（建议 `prop_spec.py` + 每道具一个 `.py`） |
| [动作/](动作/) | 角色关键帧动作库（循环安全） | `xxx.json`（keys/bob 描述） |
| [画风/](画风/) | 画风预设与色板约定 | 索引文档（预设定义在技能 `scripts/style.py`） |

## 素材格式约定

- **角色**：`char_spec.json` 为纯数据的角色定义（rig / 身高 / 语义色名配色 / 配件），可直接被 `cast.Character(spec)` 使用；参考图为侧面轮廓原画。
- **动作**：JSON 含 `name / rig / loop / frames / bob / keys`，`keys` 为 `[帧号, 关节角字典, 缓动]`，帧号以 1 开头、收尾帧闭合保证循环。整数周期帧数（如 24/32）→ 与项目 12fps 对齐无缝循环。
- **语义色名**：`outline / main_1 / main_2 / sub_1 / sub_2 / accent` 固定槽位，经 `palette.resolve_color` 映射到当前画风，不写死 sRGB 值。
- **颜色一律 sRGB→linear 再赋值**（技能铁律，见技能 SKILL.md）。

## 使用方式

```bash
git clone https://github.com/WsDerDerDer/blender-gp52-assets.git
```

创作时把所需素材复制进工作目录（如 `gp_work/assets/`），或直接引用本库路径。

## 贡献新素材

1. 新建/更新素材文件 + 该分类 README 的登记条目
2. 附上可验证的产出（渲染帧、spec 断言输出）
3. commit 到本仓库主分支（素材体积大时以压缩包形式入库，避免单文件 > 100MB）