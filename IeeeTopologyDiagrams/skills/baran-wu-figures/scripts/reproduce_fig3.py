"""
Figure 3 — One line diagram of a radial network
         辐射状网络单线图
===========================================================================

Author : 黎湛联 (Zhanlian Li)
Package: IeeeTopologyDiagrams
Version: 4.0.6

Source / 出处:
    M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems
    for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery,
    Vol. 4, No. 2, pp. 1401-1407, April 1989.

Paper Description / 原文描述:
    "We represent the lines with impedances z_l = r_l + jx_l, and loads as
    constant power sinks, S_L = P_L + jQ_L. Power flow in a radial
    distribution network can be described by a set of recursive equations,
    called DistFlow branch equations, that use the real power, reactive
    power, and voltage magnitude at the sending end of a branch —
    P_i, Q_i, V_i respectively to express the same quantities at the
    receiving end of the branch."

    — Section II, 2.2 Power Flow Equations (p.1402)

Structure / 结构:
    A radial feeder with nodes 0, i-1, i, i+1, ..., n.
    Each node has load injection P_Li, Q_Li.
    Branch power flows: P_0, P_{i-1}, P_i, P_{i+1}, P_n (horizontal arrows).
    Dashed feeder extension represents downstream omitted lines.

Key Terms / 关键术语:
    - radial network           辐射状网络
    - DistFlow branch equation 配电潮流支路方程
    - forward update           前推更新
    - backward update          回代更新
    - sending/receiving end    送端/受端
    - constant power sink      恒功率负荷
    - load injection           负荷注入
    - branch impedance         支路阻抗(z = r + jx)
    - power loss               网损(i²r)
"""
    draw_fig3_diagram('my_fig3.png')  # Custom path / 自定义路径
"""

import os
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset'] = 'stix'  # LaTeX-like math rendering
import matplotlib.pyplot as plt
from .drawing_elements import BUS_LW, draw_bar_node


def draw_fig3_diagram(output_path=None):
    """绘制配电网支路功率流示意图 (Figure 3)
    
    参数 / Parameters:
        NODE_SPACING = 0.40  节点间距 / Node spacing
        LINE_Y = 0.0         母线 y 坐标 / Bus y coordinate
        SCALE = 0.4          节点缩放比例 / Node scale factor
        BAR_H = 0.44*SCALE   竖条高度 / Bar height
        BAR_W = 0.03*SCALE   竖条宽度 / Bar width
        DX = 0.06*SCALE      拐角水平偏移 / Corner horizontal offset
        DY = 0.128*SCALE     拐角垂直偏移 / Corner vertical offset
        ARR_SZ = 0.05*SCALE  箭头大小 / Arrow size
        LABEL_Y = -0.025     P/Q 标签 y / P/Q label y
        PLI_Y = -0.125       P_Li 标签 y / P_Li label y
    
    绘制步骤 / Drawing Steps
    ------------------------
    1. 画主水平线（三段：实线 — 虚线 — 实线）
       Draw main horizontal line (3 segments: solid – dashed – solid)
    
    2. 画节点 0, i-1, i, i+1, n（实心黑色竖条，节点 0 无拐角，其余带右拐角 + 向下箭头）
       Draw nodes (solid black bars; node 0 without corner, others with right corner + downward arrow)
    
    3. 在每个节点上方标注编号
       Label node numbers above each node
    
    4. 在节点 i 下方标注负荷 P_Li, Q_Li（仅 P 带向量箭头）
       Label load P_Li, Q_Li (only P with vector arrow) below node i
    
    5. 在每对节点间下方标注支路功率 P_j, Q_j（仅 P 带向量箭头）
       Label branch power P_j, Q_j (only P with vector arrow) between node pairs
    
    6. P_n, Q_n 放在节点 n 右侧同一水平线
       Place P_n, Q_n right of node n on the same horizontal line
    
    7. 设置坐标范围、隐藏坐标轴、保存
       Set axis limits, hide axes, save
    
    Parameters
    ----------
    output_path : str or None
        输出图片路径 / Output image path
        
    Returns
    -------
    str
        保存的文件路径 / Saved file path
    """
    if output_path is None:
        output_path = os.path.join(
            os.getcwd(),
            'Figure 3 - One line diagram of a radial network.png'
        )
    
    # Figure settings
    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    
    # Parameters (using Figure 2 node spacing)
    node_spacing = 0.40  # same as Figure 2 node spacing
    line_y = 0
    
    # Draw main horizontal line in segments
    line_end = 4 * node_spacing
    dash_start = node_spacing / 4   # middle 1/2 centered
    dash_end = 3 * node_spacing / 4
    # Solid before dash
    ax.plot([0, dash_start], [line_y, line_y], 'k-', lw=1.5, zorder=5)
    # Dashed segment (1/3)
    ax.plot([dash_start, dash_end], [line_y, line_y], 'k:', lw=0.8, zorder=3)
    # Solid after dash to end
    ax.plot([dash_end, line_end], [line_y, line_y], 'k-', lw=1.5, zorder=5)
    
    # Node positions: 0, i-1, i, i+1, n
    nodes = [0, 1, 2, 3, 4]
    labels = [r'$0$', r'$i-1$', r'$i$', r'$i+1$', r'$n$']
    
    SCALE = 0.4  # 负荷节点统一缩放比例
    
    for i, (x, label) in enumerate(zip(nodes, labels)):
        x_pos = x * node_spacing
        
        if i == 0:  # 节点 0：实心黑色竖条（无拐角无箭头）
            BAR_H, BAR_W = 0.44 * SCALE, 0.03 * SCALE
            bar_y_top = line_y + BAR_H / 2
            bar_y_bot = line_y - BAR_H / 2
            draw_bar_node(ax, x=x_pos, y_top=bar_y_top, y_bottom=bar_y_bot,
                         width=BAR_W, label=None)
        else:  # i-1, i, i+1, n：右出线负荷节点
            BAR_H, BAR_W = 0.44 * SCALE, 0.03 * SCALE
            DX, DY = 0.06 * SCALE, 0.128 * SCALE
            ARR_SZ = 0.05 * SCALE
            bar_y_top = line_y + BAR_H / 2
            bar_y_bot = line_y - BAR_H / 2
            draw_bar_node(ax, x=x_pos, y_top=bar_y_top, y_bottom=bar_y_bot,
                         width=BAR_W, label=None)
            # 右边拐角 + 向下箭头
            corner_y = bar_y_bot + BAR_H * 0.25
            corner_x = x_pos + BAR_W / 2
            ax.plot([corner_x, corner_x + DX], [corner_y, corner_y], 'k-', lw=1.0, zorder=5)
            ax.plot([corner_x + DX, corner_x + DX], [corner_y, corner_y - DY], 'k-', lw=1.0, zorder=5)
            arr_x, arr_y = corner_x + DX, corner_y - DY
            tri = plt.Polygon([
                (arr_x, arr_y - ARR_SZ),
                (arr_x - ARR_SZ * 0.4, arr_y),
                (arr_x + ARR_SZ * 0.4, arr_y),
            ], closed=True, edgecolor='k', facecolor='k', lw=1.0, zorder=5)
            ax.add_patch(tri)
        
        # Draw node label above
        ax.text(x_pos, line_y + 0.10, label, ha='center', va='bottom', 
                fontsize=12, fontweight='bold')
    
    # P/Q label y-position
    label_y = -0.025
    
    # Label load at node i (position 2)
    ax.text(2 * node_spacing + 0.02, -0.125, r'$\vec{P}_{Li}, Q_{Li}$', 
            ha='center', va='top', fontsize=11, style='italic')
    
    # Draw power flow labels (below the line) — vector notation
    P_positions = [0.5, 1.52, 2.5, 3.55]
    P_labels = [r'$\vec{P}_{0}, Q_{0}$', r'$\vec{P}_{i-1}, Q_{i-1}$',
                r'$\vec{P}_{i}, Q_{i}$', r'$\vec{P}_{i+1}, Q_{i+1}$']
    
    for px, pl in zip(P_positions, P_labels):
        x_pos = px * node_spacing
        ax.text(x_pos, label_y, pl, ha='center', va='top', fontsize=11)
    
    # Pn, Qn 放在 n 节点右侧、与线路同一水平 — vector notation
    n_x = 4 * node_spacing
    ax.text(n_x + 0.06, line_y, r'$\vec{P}_{n}, Q_{n}$',
            ha='left', va='center', fontsize=11)
    
    # Set limits
    ax.set_xlim(-0.15, 4 * node_spacing + 0.40)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title (English-only to avoid CJK font issues)
    ax.set_title('Figure 3 -- One line diagram of a radial network', 
                 fontsize=11, fontweight='bold', pad=12)
    
    # Save
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    
    print(f"Saved: {output_path}")
    return output_path


if __name__ == '__main__':
    draw_fig3_diagram()
