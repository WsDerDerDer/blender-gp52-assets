# asset: 场景元素/cartoon-cloud
# -*- coding: utf-8 -*-
"""卡通云（资产试点 v1）：确定性圆弧并集点集，零依赖纯几何。

用法：pts = cloud_pts(x, y, scale, variant=0)
返回闭合 2D 点列（未设 z）；调用方 densify + CATMULL_ROM 后即圆润云朵。
颜色由调用方 palette 决定（语义色名），此文件只输出形状——确定性、无 random/bpy。
"""
import math


def _union(circles, cx, cy, n):
    """多圆并集轮廓（星形域）：r(θ) = max over circles。"""
    pts = []
    for i in range(n):
        th = 2 * math.pi * i / n
        cu, su = math.cos(th), math.sin(th)
        rmax = 0.0
        for (ox, oy, r) in circles:
            px = (ox - cx) * cu + (oy - cy) * su
            d2 = px * px - ((ox - cx) ** 2 + (oy - cy) ** 2) + r * r
            if d2 > 0:
                t = px + math.sqrt(d2)
                if t > rmax:
                    rmax = t
        pts.append((cx + rmax * cu, cy + rmax * su))
    return pts


def cloud_pts(x, y, scale, variant=0, n=48):
    """圆弧并集卡通云（大小对比明确：主圆 + 两个从圆）。variant 只影响圆心排布。"""
    off = (0.35 if variant % 2 else -0.35) * scale * 0.6
    circles = [
        (x - 1.6 * scale + off, y - 0.10 * scale, 0.55 * scale),
        (x - 0.55 * scale + off, y + 0.24 * scale, 0.75 * scale),
        (x + 0.45 * scale + off, y + 0.30 * scale, 0.85 * scale),
        (x + 1.35 * scale + off, y - 0.02 * scale, 0.55 * scale),
        (x + 2.05 * scale + off, y - 0.28 * scale, 0.42 * scale),
    ]
    return _union(circles, x, y, n)


def cloud_bottom_flat(pts, flat_y=None):
    """把底部拉平（云贴水平线时用）：低于 flat_y 的点上抬。返回新点列。"""
    if flat_y is None:
        return list(pts)
    return [(px, min(py, flat_y)) for px, py in pts]


if __name__ == "__main__":
    p = cloud_pts(0, 0, 2.0)
    assert len(p) == 48
    assert all(abs(math.hypot(q[0], q[1])) < 8 for q in p)
    print("CARTOON_CLOUD_OK pts=%d" % len(p))