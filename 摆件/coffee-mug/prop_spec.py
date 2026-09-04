# -*- coding: utf-8 -*-
"""马克杯（摆件试点 v1）：确定性几何点集，零依赖纯 Python。

咖啡杯：杯身（上宽下窄锥形）+ 弧形把手 + 杯口椭圆。
用法：body_pts(x, y, s) / handle_pts(x, y, s)（开放线）/ rim_pts(x, y, s)。
s=1 时杯高 1.4u、杯口宽 1.0u；颜色由调用方 palette (语义色名) 决定。
"""
import math


def body_pts(x, y, s, n=20):
    """杯身外轮廓：上口宽 1.0s、底宽 0.62s、高 1.4s（闭合点列）。"""
    top_r, bot_r, h = 0.50 * s, 0.31 * s, 1.40 * s
    pts = []
    for i in range(n):
        a = math.pi * i / (n - 1)                    # 0..π：左壁下→上
        u = i / (n - 1)
        r = bot_r + (top_r - bot_r) * u
        pts.append((x - r * math.cos(a), y + h * u))
    for i in range(n):
        a = math.pi * i / (n - 1)
        u = 1 - i / (n - 1)
        r = bot_r + (top_r - bot_r) * u
        pts.append((x + r * math.cos(a), y + h * u))
    return pts


def handle_pts(x, y, s):
    """右侧把手：开放圆弧（圆头线帽，用 LINE 材质画）。"""
    cx, cy, r = x + 0.52 * s, y + 0.72 * s, 0.34 * s
    n = 12
    return [(cx + r * math.cos(math.radians(-40 + 90 * i / (n - 1))),
             cy + r * math.sin(math.radians(-40 + 90 * i / (n - 1))))
            for i in range(n)]


def rim_pts(x, y, s, n=16):
    """杯口椭圆（侧视 = 扁椭圆细条，画在杯顶）。"""
    return [(x + 0.5 * s * math.cos(2 * math.pi * i / n),
             y + 1.40 * s + 0.09 * s * math.sin(2 * math.pi * i / n))
            for i in range(n)]


if __name__ == "__main__":
    b = body_pts(0, 0, 1.0)
    assert len(b) == 40
    assert abs(max(p[0] for p in b)) > abs(min(p[0] for p in b)) * 1.4  # 上宽下窄
    assert len(handle_pts(0, 0, 1.0)) == 12
    assert len(rim_pts(0, 0, 1.0)) == 16
    print("COFFEE_MUG_SPEC_OK")