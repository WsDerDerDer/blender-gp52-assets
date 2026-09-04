# -*- coding: utf-8 -*-
"""卡通木船（载具试点 v1）：确定性几何点集，零依赖纯 Python。

从 skill scripts/cartoon_boat.py 提炼：船体/帆/桅杆/舵 的纯几何函数。
用法（调用方注入 dr/idx/pal 完成绘制）：
    hull_pts(x, y, s)      # 船体外轮廓（13 点 → densify+CATMULL_ROM 圆润）
    sail_pts(x, y, s, wind)  # 鼓风帆（外缘外凸 8 控制点，wind∈[0,1]）
    mast_line / rudder_pts
尺寸约定：s=1 时船长 6.2u、桅高 3.2u；颜色由调用方 palette (语义色名) 决定。
"""
import math


def hull_pts(x, y, s):
    """船体外轮廓：两端上翘 + 底部圆弧（浮力形态）。返回闭合 2D 点列。"""
    return [
        ( 3.10*s + x,  0.40*s + y), ( 2.30*s + x,  0.20*s + y),
        ( 0.80*s + x,  0.10*s + y), (-0.80*s + x,  0.05*s + y),
        (-2.40*s + x,  0.10*s + y), (-3.10*s + x,  0.20*s + y),
        (-3.00*s + x, -0.30*s + y), (-2.00*s + x, -0.75*s + y),
        (-0.30*s + x, -0.95*s + y), ( 1.30*s + x, -0.90*s + y),
        ( 2.40*s + x, -0.55*s + y), ( 2.95*s + x, -0.05*s + y),
        ( 3.10*s + x,  0.40*s + y),
    ]


def sail_pts(x, y, s, wind=0.5):
    """鼓风帆：桅杆边固定 + 外缘外凸（wind 相位驱动，确定性）。"""
    bul_x = -0.35 * s * max(0.0, min(1.0, wind))
    clew_x = -2.40 * s - 0.30 * s * wind
    return [
        ( 0.0,                    0.30*s + y),   # tack 桅杆底（固定）
        ( 0.0,                    3.20*s + y),   # head 桅杆顶（固定）
        (-0.35*s - 1.0*bul_x + x,  2.90*s + y),
        (-0.95*s - 1.6*bul_x + x,  2.40*s + y),
        (-1.70*s - 2.2*bul_x + x,  1.95*s + y),
        (clew_x + x,              1.55*s + y),   # clew 外下角
        (clew_x*0.40 + x,         1.05*s + y),
        (-0.35*s + clew_x*0.12 + x, 0.55*s + y),
    ]


def mast_line(x, y, s):
    """桅杆线段 [(x, 0.2s+y), (x, 3.2s+y)]。"""
    return [(x, 0.20*s + y), (x, 3.20*s + y)]


def rudder_pts(x, y, s):
    """舵板轮廓（闭合，挂在船尾 -3.1s 处）。"""
    return [
        (x - 3.10*s, -0.30*s + y), (x - 3.30*s, -0.40*s + y),
        (x - 3.30*s, -0.85*s + y), (x - 3.10*s, -0.85*s + y),
        (x - 3.10*s, -0.30*s + y),
    ]


if __name__ == "__main__":
    hp = hull_pts(0, 0, 1.0)
    assert len(hp) == 13 and max(p[1] for p in hp) > 0.3
    sp = sail_pts(0, 0, 1.0, 0.5)
    assert len(sp) == 8 and sp[-1][0] < sp[0][0]          # 帆在桅杆左侧展开
    assert len(mast_line(0, 0, 1.0)) == 2
    assert len(rudder_pts(0, 0, 1.0)) == 5
    print("WOOD_BOAT_SPEC_OK")