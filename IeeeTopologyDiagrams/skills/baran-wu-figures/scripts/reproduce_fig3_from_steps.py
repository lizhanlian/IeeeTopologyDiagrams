"""
根据以下步骤绘制 Figure 3 — 辐射状网络单线图：

参数 / Parameters:
    NODE_SPACING = 0.40  节点间距
    LINE_Y = 0.0         母线 y 坐标
    SCALE = 0.4          节点缩放比例
    BAR_H = 0.44 * SCALE = 0.176  竖条高度
    BAR_W = 0.03 * SCALE = 0.012  竖条宽度
    DX = 0.06 * SCALE = 0.024     拐角水平偏移
    DY = 0.128 * SCALE = 0.051    拐角垂直偏移
    ARR_SZ = 0.05 * SCALE = 0.02  箭头大小
    LABEL_Y = -0.025  P/Q 标签 y 位置
    PLI_Y = -0.125    P_Li 标签 y 位置

画图步骤 / Drawing Steps:

1. 画主水平线（三段：实线 — 虚线 — 实线）
   Draw main horizontal line at y=LINE_Y:
     segment 1: x=0 to NODE_SPACING/4, solid, lw=1.5
     segment 2: x=NODE_SPACING/4 to 3*NODE_SPACING/4, dashed, lw=0.8
     segment 3: x=3*NODE_SPACING/4 to 4*NODE_SPACING, solid, lw=1.5

2. 画节点 0, i-1, i, i+1, n（实心黑色竖条）
   - Node 0: only bar_node(x, y_top=LINE_Y+BAR_H/2, y_bottom=LINE_Y-BAR_H/2, width=BAR_W), no corner
   - Nodes i-1, i, i+1, n: bar_node + right corner + downward arrow
     corner: right edge of bar, at 0.25*BAR_H from bottom
     horizontal line: +DX right, vertical line: -DY down, arrow: triangle at tip
   Draw nodes using draw_bar_node(), corner/arrow with ax.plot() and plt.Polygon()

3. 在每个节点上方 LINE_Y+0.10 处标注编号 (fontsize=12, bold)
   Label node numbers: $0$, $i-1$, $i$, $i+1$, $n$

4. 在节点 i 下方标注负荷 P_Li, Q_Li
   position: x=2*NODE_SPACING+0.02, y=PLI_Y, ha='center', va='top', fontsize=11, italic

5. 在每对节点间下方 LABEL_Y 处标注支路功率 P_j, Q_j
   positions x (in NODE_SPACING units): 0.5, 1.52, 2.5, 3.55
   labels: $\vec{P}_{0}, Q_{0}$, $\vec{P}_{i-1}, Q_{i-1}$, $\vec{P}_{i}, Q_{i}$, $\vec{P}_{i+1}, Q_{i+1}$
   (only P has vector arrow \vec{}, Q does not)
   ha='center', va='top', fontsize=11

6. P_n, Q_n 放在节点 n 右侧同一水平线
   position: x=4*NODE_SPACING+0.06, y=LINE_Y, ha='left', va='center', fontsize=11
   label: $\vec{P}_{n}, Q_{n}$

7. 设置坐标范围 xlim=(-0.15, 4*NODE_SPACING+0.40), ylim=(-0.5, 0.5),
   隐藏坐标轴, aspect='equal', save to PNG (dpi=200, bbox_inches='tight')

Available imports:
    from IeeeTopologyDiagrams.drawing_elements import draw_bar_node, BUS_LW
    import matplotlib.pyplot as plt
    import os
"""

# TODO: implement the 7 drawing steps above using the given parameters
