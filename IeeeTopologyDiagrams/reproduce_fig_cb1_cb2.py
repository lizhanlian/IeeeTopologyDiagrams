"""
Figure 1 — Schematic Diagram of a Primary Circuit of a Distribution System
         配电系统一次回路示意图
===========================================================================

Author : 黎湛联 (Zhanlian Li)
Package: IeeeTopologyDiagrams
Version: 4.0.6

--------------
Overview / 概览
--------------
EN: This module reproduces Figure 1 of the IEEE distribution system single-line
    diagram, fully illustrating the primary and secondary distribution network
    topology with two substations (SS1, SS2), nine circuit breakers (CB1–CB9),
    load nodes, branch elements, feeder extensions, and tie-switch connections.
    It serves as a reference case for distribution system single-line diagram
    drawing and can be used directly after installing this package.

CN: 本模块重现 IEEE 配电系统单线图的 Figure 1，完整展示包含两座变电站 (SS1, SS2)、
    九个断路器 (CB1–CB9)、负载节点、分支元件、馈线延伸线及跨接开关连接的一、二次
    配电网拓扑结构。可作为配电系统单线图绘制的参考案例，供安装本包后直接运行参考。

-----------------------------------
Topology Steps / 拓扑结构步骤
-----------------------------------
Step  1 – SS1              : (EN) Left-side black substation rectangle (vertical)
                             (CN) 左侧黑色变电站矩形 (垂直)
Step  2 – CB1              : (EN) Closed circuit breaker to the right of SS1 (horizontal),
                                   controlling the upper primary bus
                             (CN) SS1 右侧闭合断路器 (水平), 控制上方一次母线
Step  3 – CB2              : (EN) Closed circuit breaker to the right of SS1 (horizontal),
                                   turns vertically downward via a corner
                             (CN) SS1 右侧闭合断路器 (水平), 经拐角转垂直向下
Step  4 – Vertical Branch  : (EN) 4 solid nodes vertically downward from CB2 corner,
                                   with dashed feeder extension at the end
                             (CN) CB2 拐角后垂直向下列 4 个实心节点, 末端虚线延伸
Step  5 – CB4              : (EN) From the 3rd solid node of the vertical branch →
                                   CB4 closed switch → 3 load nodes → branch end
                             (CN) 垂直分支第 3 实心节点右出 → CB4 闭合断路器 → 3 个负载节点 → 分支末端
Step  6 – CB3              : (EN) Between 2nd/3rd nodes of vertical branch →
                                   CB3 closed switch, total 6 load nodes
                             (CN) 垂直分支第 2/3 节点之间右出 → CB3 闭合断路器, 共 6 个负载节点
Step  7 – Branch1 (CB3)    : (EN) Vertical branch (T-type) inserted between 3rd/4th
                                   nodes on CB3 line → connects to CB9
                             (CN) CB3 第 3/4 节点间插入垂直分支 (T 型) → 连接 CB9
Step  8 – Branch2 (CB3)    : (EN) Vertical branch (T-type) after the 6th node on
                                   CB3 line → connects to CB7/CB8
                             (CN) CB3 第 6 节点后插入垂直分支 (T 型) → 连接 CB7/CB8
Step  9 – CB8              : (EN) Open circuit breaker to the right of CB3's
                                   2nd branch → 4 load nodes
                             (CN) CB3 第 2 分支右侧断开断路器 → 4 个负载节点
Step 10 – CB6              : (EN) Closed circuit breaker to the right of CB8's
                                   load nodes → directly connected to SS2
                             (CN) CB8 负载节点右侧闭合断路器 → 直接连接至 SS2
Step 11 – SS2              : (EN) Right-side black substation rectangle (vertical),
                                   same style as SS1 but half-width
                             (CN) 右侧黑色变电站矩形 (垂直), 与 SS1 同样式仅宽度减半
Step 12 – CB9              : (EN) Vertical open circuit breaker with cornered
                                   connections: from CB3 1st branch bottom (4/5)
                                   to middle of CB4 branch
                             (CN) 垂直断开断路器, 拐角连接 CB3 第 1 分支底端 4/5 处至 CB4 分支中段
Step 13 – CB1 Branch       : (EN) After CB1 on the upper primary bus:
                                   4 load nodes → upward T-type branch
                             (CN) SS1 上方一次母线 CB1 后 4 个节点 → 上行分支 (T 型)
Step 14 – CB5              : (EN) Closed switch to the right of the CB1 branch →
                                   3 load nodes
                             (CN) CB1 分支右侧闭合开关 → 3 个负载节点
Step 15 – CB7              : (EN) Diagonal open circuit breaker (mimicking Figure 2
                                   switch 21), with cornered short-stub connections:
                                   CB1 branch bottom-right 1/6 ↔ CB3 2nd branch top-left 1/5
                             (CN) 斜线断开断路器 (仿 Figure 2 开关 21), 拐角短桩连接:
                                  CB1 分支右下角 1/6 ↔ CB3 第 2 分支左上角 1/5
Step 16 – Feeder Extension : (EN) Vertical dashed extension at end of CB4 and CB2
                             (CN) CB4 末端垂直虚线延伸及 CB2 垂直末端虚线延伸

----------------------
Topology / 拓扑连线图
----------------------
        SS1 ──┤CB1├── ●●●● ── T branch(CB1) ── ┤CB5├── ●●●
               │
               └──┤CB2├──┐
                         │ vertical down / 垂直向下
                         ●
                         ● ── ●●● ┤CB3├ ●●● ├T1├ ├●●●├ ├T2├ ── ┤CB8├ ●●●● ┤CB6├── SS2
                         ●              │     │                │
                         ●              │    CB9(cornered)  CB7(diagonal/solid)── T(CB1 br. bottom-right 1/6)
                         :              │
                         : ── ┤CB4├ ●●● ├T end├

------------
Usage / 使用方式
------------
EN: After installing the package, call the drawing function directly to
    generate a PNG single-line diagram::

        pip install IeeeTopologyDiagrams

        from IeeeTopologyDiagrams.reproduce_fig_cb1_cb2 import draw_cb1_cb2_diagram
        draw_cb1_cb2_diagram()                 # default output path / 默认输出路径

        # or specify output path / 或指定输出路径
        draw_cb1_cb2_diagram(output_path='./my_fig1.png')

    The function returns the saved file path.
    (CN) 本函数返回保存的图片文件路径。

-----------------------
Drawing Primitives / 包含的基元
-----------------------
| Primitive / 基元              | Function / 函数                   | Used by / 使用者    |
|-------------------------------|-----------------------------------|---------------------|
| Substation / 变电站           | `draw_substation_vertical`        | SS1, SS2            |
| Closed breaker / 闭合断路器    | `draw_switch`                     | CB1–CB6             |
| Open breaker (horiz.) / 水平断开  | `draw_switch_open`             | CB7, CB8            |
| Open breaker (vert.) / 垂直断开   | `draw_switch_open_vertical`    | CB9                 |
| Solid node / 实心节点          | `draw_solid_node`                 | load / connection   |
| T-branch / 分支(T 型)         | `draw_branch`                     | all lateral taps    |
| Feeder extension / 馈线延伸    | `draw_feeder_extension`           | CB2 & CB4 ends      |
| Horiz. feeder / 水平馈线       | `draw_feeder_extension_horizontal`| (reserved / 备用)   |

"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .drawing_elements import (
    BUS_LW, SW_SIZE,
    draw_switch,
    draw_solid_node,
    draw_branch,
    draw_feeder_extension,
    draw_feeder_extension_horizontal,
    draw_switch_open_vertical,
    draw_switch_open,
    draw_substation_vertical,
)


def draw_cb1_cb2_diagram(output_path=None):
    """绘制 SS1 + CB1 + CB2 + CB3 + CB5 配电系统拓扑图

    Parameters
    ----------
    output_path : str or None
        输出图片路径，None 则使用默认路径

    Returns
    -------
    str
        保存的文件路径
    """
    if output_path is None:
        output_path = os.path.join(os.getcwd(),
            'Figure 1 - Schematic diagram of a primary circuit of a distribution system.png')

    # ============================================================
    # Layout parameters
    # ============================================================
    SS1_X = 0.0
    SS1_WIDTH = 0.12
    SS1_TOP = 0.0
    SS1_BOT = -0.90
    SS1_HEIGHT = SS1_TOP - SS1_BOT

    Y_SW1 = SS1_TOP - SS1_HEIGHT * 0.25
    Y_SW2 = SS1_TOP - SS1_HEIGHT * 0.75

    SW_GAP = 0.35
    SW1_X = SS1_X + SS1_WIDTH / 2 + SW_GAP + SW_SIZE / 2
    SW2_X = SS1_X + SS1_WIDTH / 2 + SW_GAP + SW_SIZE / 2

    LABEL_OFFSET = 0.15

    # ============================================================
    # Create figure
    # ============================================================
    fig, ax = plt.subplots(figsize=(5.0, 3.0))

    # Step 1: SS1 — substation
    draw_substation_vertical(ax, SS1_X, SS1_BOT, SS1_TOP, 'SS1', width=SS1_WIDTH / 2)

    # Step 2: Bus lines from SS1 to switches
    ss1_right = SS1_X + SS1_WIDTH / 2
    sw1_left = SW1_X - SW_SIZE / 2
    sw1_right = SW1_X + SW_SIZE / 2
    sw2_left = SW2_X - SW_SIZE / 2
    sw2_right = SW2_X + SW_SIZE / 2

    NODE_OFFSET = 0.25
    HORIZ_GAP = 0.22
    GAP = 0.22

    # Bus: SS1 -> switch
    ax.plot([ss1_right, sw1_left], [Y_SW1, Y_SW1],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([ss1_right, sw2_left], [Y_SW2, Y_SW2],
            'k-', lw=BUS_LW, zorder=5)

    # Step 3: Two closed switches (CB1, CB2)
    draw_switch(ax, SW1_X, Y_SW1, SW_SIZE)   # CB1
    draw_switch(ax, SW2_X, Y_SW2, SW_SIZE)   # CB2

    # Switch labels
    ax.text(SW1_X, Y_SW1 + SW_SIZE / 2 + 0.08, 'CB1',
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(SW2_X, Y_SW2 + SW_SIZE / 2 + 0.08, 'CB2',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Step 4: CB1 horizontal connection to first node
    node1_x = sw1_right + NODE_OFFSET
    ax.plot([sw1_right, node1_x], [Y_SW1, Y_SW1],
            'k-', lw=BUS_LW, zorder=5)

    # Step 5: CB2 horizontal then vertical down
    CB2_HORIZ_OUT = 0.25
    CB2_VERT_DOWN = 0.1
    cb2_corner_x = sw2_right + CB2_HORIZ_OUT
    ax.plot([sw2_right, cb2_corner_x], [Y_SW2, Y_SW2],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([cb2_corner_x, cb2_corner_x], [Y_SW2, Y_SW2 - CB2_VERT_DOWN],
            'k-', lw=BUS_LW, zorder=5)
    node2_x = cb2_corner_x
    node2_y = Y_SW2 - CB2_VERT_DOWN

    # Step 6: Solid circle nodes after CB1 and CB2
    draw_solid_node(ax, node1_x, Y_SW1)          # After CB1
    draw_solid_node(ax, node2_x, node2_y)         # After CB2

    # Step 7: CB1 branch — add 3 more horizontal nodes (total 4 on CB1 line)
    for i in range(1, 4):
        nx = node1_x + i * HORIZ_GAP
        ax.plot([node1_x + (i - 1) * HORIZ_GAP, nx], [Y_SW1, Y_SW1],
                'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, Y_SW1)

    # Branch element dimensions (scaled-down SS1 rectangle)
    BRANCH_WIDTH = SS1_WIDTH / 4 * 1.25
    BRANCH_HEIGHT = SS1_HEIGHT / 4 * 1.25 * 1.25 * 0.75

    # Step 8: CB2 vertical line extends down with 3 more nodes (total 4 vertical nodes)
    CB3_VERT_EXTEND = 4 * HORIZ_GAP

    # Vertical intermediate solid nodes at HORIZ_GAP spacing
    cb3_mid_y1 = node2_y - 1 * HORIZ_GAP
    cb3_mid_y2 = node2_y - 2 * HORIZ_GAP
    cb3_mid_y3 = node2_y - 3 * HORIZ_GAP
    ax.plot([cb2_corner_x, cb2_corner_x], [node2_y, cb3_mid_y1],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb2_corner_x, cb3_mid_y1)
    ax.plot([cb2_corner_x, cb2_corner_x], [cb3_mid_y1, cb3_mid_y2],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb2_corner_x, cb3_mid_y2)
    ax.plot([cb2_corner_x, cb2_corner_x], [cb3_mid_y2, cb3_mid_y3],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb2_corner_x, cb3_mid_y3)

    # 4th vertical node: extend one node spacing (solid), then dashed extension
    cb3_ext_y = cb3_mid_y3 - HORIZ_GAP
    ax.plot([cb2_corner_x, cb2_corner_x], [cb3_mid_y3, cb3_ext_y],
            'k-', lw=BUS_LW, zorder=5)
    dash_end_y = cb3_ext_y - 1.5 * HORIZ_GAP
    draw_feeder_extension(ax, cb2_corner_x, cb3_ext_y, dash_end_y)

    # CB4 — horizontal closed switch branching right from end of CB2 vertical solid line
    cb4_y = cb3_ext_y
    cb4_x = cb2_corner_x + HORIZ_GAP
    ax.plot([cb2_corner_x, cb4_x - SW_SIZE / 2], [cb4_y, cb4_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch(ax, cb4_x, cb4_y, SW_SIZE)
    ax.text(cb4_x, cb4_y + SW_SIZE / 2 + 0.08, 'CB4',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

    # CB4 right side: 3 solid nodes, then branch
    cb4_node_x = cb4_x + SW_SIZE / 2 + GAP
    ax.plot([cb4_x + SW_SIZE / 2, cb4_node_x], [cb4_y, cb4_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb4_node_x, cb4_y)
    for i in range(1, 3):
        nx = cb4_node_x + i * HORIZ_GAP
        ax.plot([cb4_node_x + (i - 1) * HORIZ_GAP, nx], [cb4_y, cb4_y],
                'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, cb4_y)
    # Branch element at the end of CB4 line
    cb4_last_node_x = cb4_node_x + 2 * HORIZ_GAP
    branch3_x = cb4_last_node_x + HORIZ_GAP / 2 + BRANCH_WIDTH / 2
    ax.plot([cb4_last_node_x, branch3_x - BRANCH_WIDTH / 2], [cb4_y, cb4_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_branch(ax, branch3_x, cb4_y, BRANCH_WIDTH, BRANCH_HEIGHT)
    cb4_dash_end_x = branch3_x + BRANCH_WIDTH / 2

    # Step 9: CB3 — horizontal switch between 2nd and 3rd vertical nodes
    cb3_y = (cb3_mid_y1 + cb3_mid_y2) / 2
    cb3_x = cb2_corner_x + HORIZ_GAP

    ax.plot([cb2_corner_x, cb3_x - SW_SIZE / 2], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch(ax, cb3_x, cb3_y, SW_SIZE)
    ax.text(cb3_x, cb3_y + SW_SIZE / 2 + 0.08, 'CB3',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Step 10: CB3 horizontal nodes (6 nodes total, branch between 3rd and 4th)
    cb3_right = cb3_x + SW_SIZE / 2
    cb3_node_start = cb3_right + GAP
    ax.plot([cb3_right, cb3_node_start], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)

    # First 3 nodes
    for i in range(3):
        nx = cb3_node_start + i * HORIZ_GAP
        if i > 0:
            ax.plot([cb3_node_start + (i - 1) * HORIZ_GAP, nx], [cb3_y, cb3_y],
                    'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, cb3_y)

    # Branch between 3rd and 4th node on CB3 line
    cb3_node3_x = cb3_node_start + 2 * HORIZ_GAP
    branch2_x = cb3_node3_x + HORIZ_GAP / 2 + BRANCH_WIDTH / 2
    ax.plot([cb3_node3_x, branch2_x - BRANCH_WIDTH / 2], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_branch(ax, branch2_x, cb3_y, BRANCH_WIDTH, BRANCH_HEIGHT)

    # Continue to 4th node and beyond
    cb3_node4_x = branch2_x + BRANCH_WIDTH / 2 + HORIZ_GAP / 2
    ax.plot([branch2_x + BRANCH_WIDTH / 2, cb3_node4_x], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb3_node4_x, cb3_y)
    for i in range(1, 3):
        nx = cb3_node4_x + i * HORIZ_GAP
        ax.plot([cb3_node4_x + (i - 1) * HORIZ_GAP, nx], [cb3_y, cb3_y],
                'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, cb3_y)

    # Branch to the right of the 6th node on CB3 line
    cb3_node6_x = cb3_node4_x + 2 * HORIZ_GAP
    branch3_x_cb3 = cb3_node6_x + HORIZ_GAP / 2 + BRANCH_WIDTH / 2
    ax.plot([cb3_node6_x, branch3_x_cb3 - BRANCH_WIDTH / 2], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_branch(ax, branch3_x_cb3, cb3_y, BRANCH_WIDTH, BRANCH_HEIGHT)

    # CB8 — open switch after CB3 2nd branch
    cb8_x = branch3_x_cb3 + BRANCH_WIDTH / 2 + HORIZ_GAP + SW_SIZE / 2
    ax.plot([branch3_x_cb3 + BRANCH_WIDTH / 2, cb8_x - SW_SIZE / 2], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch_open(ax, cb8_x, cb3_y, SW_SIZE)
    ax.text(cb8_x, cb3_y + SW_SIZE / 2 + 0.08, 'CB8',
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    # 4 load nodes after CB8
    cb8_node_x = cb8_x + SW_SIZE / 2 + GAP
    ax.plot([cb8_x + SW_SIZE / 2, cb8_node_x], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb8_node_x, cb3_y)
    for i in range(1, 4):
        nx = cb8_node_x + i * HORIZ_GAP
        ax.plot([cb8_node_x + (i - 1) * HORIZ_GAP, nx], [cb3_y, cb3_y],
                'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, cb3_y)
    cb8_last_node_x = cb8_node_x + 3 * HORIZ_GAP

    # CB6 — closed switch after CB8 load nodes
    cb6_x = cb8_last_node_x + HORIZ_GAP + SW_SIZE / 2
    ax.plot([cb8_last_node_x, cb6_x - SW_SIZE / 2], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch(ax, cb6_x, cb3_y, SW_SIZE)
    ax.text(cb6_x, cb3_y + SW_SIZE / 2 + 0.08, 'CB6',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

    # SS2 — substation directly after CB6
    ss2_top = cb3_y + SS1_HEIGHT / 2
    ss2_bot = cb3_y - SS1_HEIGHT / 2
    ss2_x = cb6_x + SW_SIZE / 2 + HORIZ_GAP + SS1_WIDTH / 4
    draw_substation_vertical(ax, ss2_x, ss2_bot, ss2_top, 'SS2', width=SS1_WIDTH / 2)
    # Line from CB6 to SS2
    ax.plot([cb6_x + SW_SIZE / 2, ss2_x - SS1_WIDTH / 4], [cb3_y, cb3_y],
            'k-', lw=BUS_LW, zorder=5)

    # CB9 — vertical open switch aligned with 4th node on CB3 line
    cb3_branch_top = cb3_y + BRANCH_HEIGHT / 2
    cb3_branch_bot = cb3_y - BRANCH_HEIGHT / 2
    # Upper connection at 4/5 from branch top
    cb9_upper_y = cb3_branch_top - 4 * BRANCH_HEIGHT / 5
    # Lower connection at 1/2 (middle) of CB4 branch
    cb4_branch_mid = cb4_y
    cb9_y = cb9_upper_y - 2.5 * (cb9_upper_y - cb4_branch_mid) / 6
    cb9_x = cb3_node4_x
    # Upper: CB3 branch 1/4 point → left to cb9_x → down to switch
    ax.plot([branch2_x, cb9_x], [cb9_upper_y, cb9_upper_y],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([cb9_x, cb9_x], [cb9_upper_y, cb9_y + SW_SIZE / 2],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch_open_vertical(ax, cb9_x, cb9_y, SW_SIZE)
    ax.text(cb9_x + SW_SIZE / 2 + 0.08, cb9_y, 'CB9',
            ha='left', va='center', fontsize=9, fontweight='bold')
    # Lower: switch bottom → down → right to CB4 branch middle
    ax.plot([cb9_x, cb9_x], [cb9_y - SW_SIZE / 2, cb4_branch_mid],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([cb9_x, branch2_x], [cb4_branch_mid, cb4_branch_mid],
            'k-', lw=BUS_LW, zorder=5)

    # Step 11: CB1 branch — connected via line from 4th horizontal node
    node4_x = node1_x + 3 * HORIZ_GAP
    branch_gap = HORIZ_GAP
    branch_x = node4_x + branch_gap
    ax.plot([node4_x, branch_x - BRANCH_WIDTH / 2], [Y_SW1, Y_SW1],
            'k-', lw=BUS_LW, zorder=5)
    draw_branch(ax, branch_x, Y_SW1, BRANCH_WIDTH, BRANCH_HEIGHT)

    # Step 12: CB5 — switch after CB1 branch
    cb5_x = branch_x + BRANCH_WIDTH / 2 + HORIZ_GAP + SW_SIZE / 2
    cb5_y = Y_SW1
    branch_right = branch_x + BRANCH_WIDTH / 2
    ax.plot([branch_right, cb5_x - SW_SIZE / 2], [cb5_y, cb5_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch(ax, cb5_x, cb5_y, SW_SIZE)
    ax.text(cb5_x, cb5_y + SW_SIZE / 2 + 0.08, 'CB5',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

    # 3 load nodes after CB5
    cb5_node_start = cb5_x + SW_SIZE / 2 + GAP
    ax.plot([cb5_x + SW_SIZE / 2, cb5_node_start], [cb5_y, cb5_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_solid_node(ax, cb5_node_start, cb5_y)
    for i in range(1, 3):
        nx = cb5_node_start + i * HORIZ_GAP
        ax.plot([cb5_node_start + (i - 1) * HORIZ_GAP, nx], [cb5_y, cb5_y],
                'k-', lw=BUS_LW, zorder=5)
        draw_solid_node(ax, nx, cb5_y)
    cb5_last_node_x = cb5_node_start + 2 * HORIZ_GAP

    # CB7 — diagonal open switch (like switch 21) with horizontal stubs + short lines
    cb1_connect_y = Y_SW1 - BRANCH_HEIGHT / 2 + BRANCH_HEIGHT / 6   # CB1 branch 右下角 1/6
    cb3_connect_x = branch3_x_cb3 - BRANCH_WIDTH / 2 + BRANCH_WIDTH / 5  # CB3 2nd branch 左上 1/5
    cb3_connect_y = cb3_y + BRANCH_HEIGHT / 2 - BRANCH_HEIGHT / 5    # CB3 2nd branch 左上 1/5
    stub = HORIZ_GAP / 2
    short = SW_SIZE / 2
    # Upper stub: horizontal right from CB1 branch
    stub1_x = branch_right + stub
    ax.plot([branch_right, stub1_x], [cb1_connect_y, cb1_connect_y],
            'k-', lw=BUS_LW, zorder=5)
    # Lower stub: horizontal left from CB3 branch
    stub2_x = cb3_connect_x - stub
    ax.plot([stub2_x, cb3_connect_x], [cb3_connect_y, cb3_connect_y],
            'k-', lw=BUS_LW, zorder=5)
    # CB7 at midpoint
    cb7_x = (stub1_x + stub2_x) / 2
    cb7_y = (cb1_connect_y + cb3_connect_y) / 2
    # Upper diagonal (solid): stub1 down-left to LEFT of switch
    left_end_x = cb7_x - SW_SIZE / 2 - short
    ax.plot([stub1_x, left_end_x], [cb1_connect_y, cb7_y],
            'k-', lw=BUS_LW, zorder=5)
    # Short horizontal LEFT of switch
    ax.plot([left_end_x, cb7_x - SW_SIZE / 2], [cb7_y, cb7_y],
            'k-', lw=BUS_LW, zorder=5)
    draw_switch_open(ax, cb7_x, cb7_y, SW_SIZE)
    ax.text(cb7_x, cb7_y + SW_SIZE / 2 + 0.08, 'CB7',
            ha='center', va='bottom', fontsize=9, fontweight='bold')
    # Short horizontal RIGHT of switch
    right_start_x = cb7_x + SW_SIZE / 2 + short
    ax.plot([cb7_x + SW_SIZE / 2, right_start_x], [cb7_y, cb7_y],
            'k-', lw=BUS_LW, zorder=5)
    # Lower diagonal (solid): RIGHT of switch down-left to stub2
    ax.plot([right_start_x, stub2_x], [cb7_y, cb3_connect_y],
            'k-', lw=BUS_LW, zorder=5)

    # Step 13: Set bounds
    padding_x = 0.3
    padding_y = 0.25
    rightmost_x_cb1 = max(cb5_last_node_x, branch_x + BRANCH_WIDTH / 2)
    cb3_node6_x_final = cb3_node4_x + 2 * HORIZ_GAP
    rightmost_x_cb3 = max(cb3_node6_x_final, branch2_x + BRANCH_WIDTH / 2, ss2_x + SS1_WIDTH / 2)
    rightmost_x = max(rightmost_x_cb1, rightmost_x_cb3, cb4_dash_end_x)
    ax.set_xlim(SS1_X - SS1_WIDTH / 2 - padding_x,
                rightmost_x + padding_x)
    branch_top_1 = Y_SW1 + BRANCH_HEIGHT / 2
    branch_bot_1 = Y_SW1 - BRANCH_HEIGHT / 2
    branch_top_2 = cb3_y + BRANCH_HEIGHT / 2
    branch_bot_2 = cb3_y - BRANCH_HEIGHT / 2
    ax.set_ylim(min(dash_end_y, branch_bot_1, branch_bot_2) - padding_y,
                max(SS1_TOP + LABEL_OFFSET, branch_top_1 + 0.06, branch_top_2 + 0.06) + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')

    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)

    print(f"Saved: {output_path}")
    return output_path
