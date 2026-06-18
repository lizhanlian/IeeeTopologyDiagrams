"""
Figure 2 — One line diagram of a small distribution system (IEEE 33-Bus)
          小型配电系统单线图
===========================================================================

Source / 出处:
    M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems
    for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery,
    Vol. 4, No. 2, pp. 1401-1407, April 1989.

Paper Description / 原文描述:
    "To simplify the presentation, we will represent the system on a phase
    basis and the loads along a feeder section as constant P,Q loads placed
    at the end of the lines. For example, we assume that the system of Fig.1
    can be translated to an equivalent network shown in Fig.2."

    "In the figure, solid branches represent the lines that are in service
    and constitute the base radial configuration. Dotted branches
    (branches 20,21,22) represent the lines with open switches."

    "The test system is a hypothetical 12.66 kV system with a 2 feeder
    substation, 32 busses, and 5 looping branches (tie lines)."

    — Section II, 2.1 Problem Statement & Section VI: TEST RESULTS (pp.1402,1404)

Structure / 结构:
    2-substation system (SS1, SS2)
    32 load buses (nodes 1-32)
    37 branches: 32 solid (in service) + 5 dotted (open tie lines 33-37)
    Switches: CB1-CB5 (normally closed), cb21-cb22 (normally open)

Key Terms / 关键术语:
    - solid branch              实线支路(在运)
    - dotted branch             虚线支路(常开联络线)
    - base radial configuration 基础辐射状拓扑
    - constant P,Q load         恒功率负荷
    - loop                      环路
    - tie line / looping branch 联络线/环网支路(33-37)
    - voltage profile           电压分布(Table 1)
    - phase basis               单相基准

Uses IeeeTopologyDiagrams drawing primitives library
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .drawing_elements import (
    BUS_LW, NODE_LW, SW_SIZE,
    draw_switch, draw_switch_vertical, draw_switch_open, draw_switch_open_vertical,
    draw_bar_node, draw_bar_node_switched,
)

from .coordinates import (
    Y_TOP, Y_MID, Y_BOT, X_SS1, SS_WIDTH, Y_SW_TOP, Y_SW_MID, X_SW,
    x_top, x_mid, x_bot,
)


def draw_ieee33bus_diagram(output_path=None):
    """
    Draw the complete IEEE 33-Bus single-line diagram.
    
    Args:
        output_path: Path to save the output PNG. If None, saves to cwd.
    
    Returns:
        The path where the figure was saved.
    """
    fig, ax = plt.subplots(figsize=(7.5, 7.5))

    # ============================================================
    # === Global control parameters ===
    # Modify these to translate/scale the entire diagram
    # ============================================================
    node_spacing = 0.40              # horizontal spacing between vertical nodes
    sw_node_gap = 0.12               # horizontal gap between switch and node

    # SS1 connection line positions (shortened height 0.75, bottom Y_MID=-1.0, top=-0.25)
    Y_SW_TOP = Y_MID + 0.75 * 0.75
    Y_SW_MID = Y_MID + 0.75 * 0.25

    # ============================================================
    # Step 1: SS1 — solid black vertical rectangle
    # ============================================================
    rect = Rectangle((X_SS1 - SS_WIDTH/2, Y_MID), SS_WIDTH, (Y_TOP - Y_MID) * 0.75,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect)
    ax.text(X_SS1, Y_MID + 0.75 + 0.10, 'SS1', ha='center', va='bottom',
            fontsize=10, fontweight='bold')

    # ============================================================
    # Step 2: Two parallel lines from SS1 → two switches
    # ============================================================
    # Top horizontal line
    ax.plot([X_SS1 + SS_WIDTH/2, X_SW - SW_SIZE/2], [Y_SW_TOP, Y_SW_TOP],
            'k-', lw=BUS_LW)

    # Middle horizontal line
    ax.plot([X_SS1 + SS_WIDTH/2, X_SW - SW_SIZE/2], [Y_SW_MID, Y_SW_MID],
            'k-', lw=BUS_LW)

    # Draw two switches
    draw_switch(ax, X_SW, Y_SW_TOP, SW_SIZE)   # Switch 1
    draw_switch(ax, X_SW, Y_SW_MID, SW_SIZE)   # Switch 2

    # ============================================================
    # Step 3: Switch 1 → Node 1 → Node 2 → Node 3 → Switch 3 → Node 4 → Node 5 → Node 6
    # ============================================================
    SW_OUT_X = X_SW + SW_SIZE / 2  # switch right edge

    BAR_H = 0.44                     # vertical node height
    bar1_y_top = Y_SW_TOP + BAR_H / 2
    bar1_y_bot = Y_SW_TOP - BAR_H / 2
    bar1_y_mid = Y_SW_TOP
    bar1_w = 0.03

    # Switch 1 → Node 1
    NODE1_X = SW_OUT_X + node_spacing
    ax.plot([SW_OUT_X, NODE1_X], [Y_SW_TOP, bar1_y_mid], 'k-', lw=BUS_LW)
    ax.text((SW_OUT_X + NODE1_X) / 2, Y_SW_TOP + 0.1, '1', ha='center', va='bottom',
            fontsize=10, fontweight='bold')
    draw_bar_node(ax, NODE1_X, bar1_y_top, bar1_y_bot, width=bar1_w, label=None)

    # Corner and arrow for Node 1
    corner1_y = bar1_y_bot + BAR_H * 0.25
    corner1_x = NODE1_X - bar1_w / 2
    dx1, dy1 = 0.06, 0.128
    ax.plot([corner1_x, corner1_x - dx1], [corner1_y, corner1_y], 'k-', lw=BUS_LW)
    ax.plot([corner1_x - dx1, corner1_x - dx1], [corner1_y, corner1_y - dy1], 'k-', lw=BUS_LW)
    arrow1_x, arrow1_y, arr_sz = corner1_x - dx1, corner1_y - dy1, 0.05
    tri = plt.Polygon([(arrow1_x, arrow1_y - arr_sz),
                       (arrow1_x - arr_sz * 0.4, arrow1_y),
                       (arrow1_x + arr_sz * 0.4, arrow1_y)],
                      closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)

    # Node 1 → Node 2 → Node 3 → Switch 3 → Node 4 → Node 5 → Node 6
    nodes = [2, 3, 4, 5, 6]
    prev_x = NODE1_X
    for i, node_num in enumerate(nodes, start=1):
        if node_num == 4:  # Node 4 has a switch before it
            node3_right = prev_x + bar1_w / 2
            sw3_x = node3_right + sw_node_gap + SW_SIZE / 2
            ax.plot([node3_right, sw3_x - SW_SIZE / 2], [bar1_y_mid, bar1_y_mid], 'k-', lw=BUS_LW, zorder=5)
            draw_switch(ax, sw3_x, bar1_y_mid, SW_SIZE)
            sw3_out = sw3_x + SW_SIZE / 2 + sw_node_gap
            curr_x = sw3_out + sw_node_gap
            ax.plot([sw3_x + SW_SIZE / 2, curr_x], [bar1_y_mid, bar1_y_mid], 'k-', lw=BUS_LW, zorder=5)
        else:
            curr_x = prev_x + node_spacing
            ax.plot([prev_x + bar1_w/2, curr_x], [bar1_y_mid, bar1_y_mid], 'k-', lw=BUS_LW)
        
        ax.text((prev_x + curr_x) / 2, Y_SW_TOP + 0.1, str(node_num), ha='center', va='bottom',
                fontsize=10, fontweight='bold')
        draw_bar_node(ax, curr_x, bar1_y_top, bar1_y_bot, width=bar1_w, label=None)
        
        # Corner and arrow
        corner_y = bar1_y_bot + BAR_H * 0.25
        corner_x = curr_x - bar1_w / 2
        ax.plot([corner_x, corner_x - dx1], [corner_y, corner_y], 'k-', lw=BUS_LW)
        ax.plot([corner_x - dx1, corner_x - dx1], [corner_y, corner_y - dy1], 'k-', lw=BUS_LW)
        tri = plt.Polygon([(corner_x - dx1, corner_y - dy1 - arr_sz),
                           (corner_x - dx1 - arr_sz * 0.4, corner_y - dy1),
                           (corner_x - dx1 + arr_sz * 0.4, corner_y - dy1)],
                          closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
        ax.add_patch(tri)
        prev_x = curr_x

    NODE6_X = curr_x

    # ============================================================
    # === Middle layer parameters ===
    # ============================================================
    NODE15_X = x_mid[15]
    y15_gap = 0.40
    y16_gap = 0.80
    sw_out_gap = 0.425

    y15_bar = Y_SW_MID - y15_gap
    y16_bar = y15_bar - y16_gap
    sw15_h_end_x = NODE15_X - 0.22 + 0.44 * 0.8 + 0.3
    sw15_h_end_y = y15_bar - sw_out_gap
    sw16_h_end_x = sw15_h_end_x
    sw16_h_end_y = y16_bar - sw_out_gap

    # ============================================================
    # Step 4: Switch 2 → Node 15 → Node 16
    # ============================================================
    knee_x = NODE15_X
    ax.plot([SW_OUT_X, knee_x], [Y_SW_MID, Y_SW_MID], 'k-', lw=BUS_LW, zorder=5)
    ax.plot([knee_x, knee_x], [Y_SW_MID, y16_bar], 'k-', lw=BUS_LW, zorder=5)

    # Node 15: horizontal node with switch
    draw_bar_node_switched(ax, x=NODE15_X, y_bar=y15_bar, label='15',
                           label_fontsize=10)

    # ============================================================
    # Step 7: Node 15 switch → Node 7 → 8 → 9 → 10 → 11
    # ============================================================
    bar7_y_mid = sw15_h_end_y
    bar7_y_top = bar7_y_mid + BAR_H / 2
    bar7_y_bot = bar7_y_mid - BAR_H / 2
    
    nodes7_11 = [7, 8, 9, 10, 11]
    prev_x = sw15_h_end_x
    
    for node_num in nodes7_11:
        curr_x = prev_x + node_spacing
        ax.plot([prev_x, curr_x], [bar7_y_mid, bar7_y_mid], 'k-', lw=BUS_LW)
        
        if node_num == 7:
            ax.text(curr_x - bar1_w / 2, bar7_y_top - BAR_H * 0.20, str(node_num),
                    ha='right', va='center', fontsize=10, fontweight='bold')
        else:
            ax.text(prev_x + node_spacing / 2, bar7_y_mid + 0.08, str(node_num),
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        draw_bar_node(ax, curr_x, bar7_y_top, bar7_y_bot, width=bar1_w, label=None)
        
        # Corner and arrow
        corner_y = bar7_y_bot + BAR_H * 0.25
        corner_x = curr_x - bar1_w / 2
        ax.plot([corner_x, corner_x - dx1], [corner_y, corner_y], 'k-', lw=BUS_LW)
        ax.plot([corner_x - dx1, corner_x - dx1], [corner_y, corner_y - dy1], 'k-', lw=BUS_LW)
        tri = plt.Polygon([(corner_x - dx1, corner_y - dy1 - arr_sz),
                           (corner_x - dx1 - arr_sz * 0.4, corner_y - dy1),
                           (corner_x - dx1 + arr_sz * 0.4, corner_y - dy1)],
                          closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
        ax.add_patch(tri)
        prev_x = curr_x

    NODE11_X = curr_x

    # ============================================================
    # Step 8: Node 11 → Open switch → dashed line → Node 20 → 19 → 18 → Switch 17 → SS2
    # ============================================================
    node11_right = NODE11_X + bar1_w / 2
    sw11_open_x = node11_right + sw_node_gap + SW_SIZE / 2
    ax.plot([node11_right, sw11_open_x - SW_SIZE / 2], [bar7_y_mid, bar7_y_mid], 'k-', lw=BUS_LW, zorder=5)
    draw_switch_open(ax, sw11_open_x, bar7_y_mid, SW_SIZE)
    
    sw11_out_x = sw11_open_x + SW_SIZE / 2 + sw_node_gap
    NODE20_X = sw11_out_x + node_spacing
    ax.plot([sw11_out_x, NODE20_X], [bar7_y_mid, bar7_y_mid], 'k--', lw=BUS_LW, zorder=5)

    # Node 20 → 19 → 18
    nodes20_18 = [20, 19, 18]
    prev_x = NODE20_X
    
    for node_num in nodes20_18:
        if node_num == 20:
            ax.text((sw11_out_x + prev_x) / 2, bar7_y_mid + 0.08, str(node_num),
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
        else:
            curr_x = prev_x + node_spacing
            ax.plot([prev_x + bar1_w / 2, curr_x], [bar7_y_mid, bar7_y_mid], 'k-', lw=BUS_LW)
            ax.text(prev_x + node_spacing / 2, bar7_y_mid + 0.08, str(node_num),
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
            prev_x = curr_x
        
        draw_bar_node(ax, prev_x, bar7_y_top, bar7_y_bot, width=bar1_w, label=None)
        
        # Corner and arrow
        corner_y = bar7_y_bot + BAR_H * 0.25
        corner_x = prev_x - bar1_w / 2
        ax.plot([corner_x, corner_x - dx1], [corner_y, corner_y], 'k-', lw=BUS_LW)
        ax.plot([corner_x - dx1, corner_x - dx1], [corner_y, corner_y - dy1], 'k-', lw=BUS_LW)
        tri = plt.Polygon([(corner_x - dx1, corner_y - dy1 - arr_sz),
                           (corner_x - dx1 - arr_sz * 0.4, corner_y - dy1),
                           (corner_x - dx1 + arr_sz * 0.4, corner_y - dy1)],
                          closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
        ax.add_patch(tri)

    NODE18_X = prev_x

    # Node 18 → Switch 17 → SS2
    node18_right = NODE18_X + bar1_w / 2
    SW17_X = node18_right + node_spacing / 2 + SW_SIZE / 2
    ax.plot([node18_right, SW17_X - SW_SIZE / 2], [bar7_y_mid, bar7_y_mid], 'k-', lw=BUS_LW)
    ax.text((node18_right + SW17_X - SW_SIZE / 2) / 2, bar7_y_mid + 0.08, '17',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
    draw_switch(ax, SW17_X, bar7_y_mid, SW_SIZE)

    SS2_X = SW17_X + SW_SIZE / 2 + node_spacing
    Y_SS2_MID = bar7_y_mid
    Y_SS2_BOT = Y_SS2_MID - 0.375
    Y_SS2_TOP = Y_SS2_MID + 0.375
    ax.plot([SW17_X + SW_SIZE / 2, SS2_X - SS_WIDTH / 2], [bar7_y_mid, bar7_y_mid], 'k-', lw=BUS_LW)
    rect_ss2 = Rectangle((SS2_X - SS_WIDTH/2, Y_SS2_BOT), SS_WIDTH, Y_SS2_TOP - Y_SS2_BOT,
                         linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect_ss2)
    ax.text(SS2_X, Y_SS2_TOP + 0.10, 'SS2', ha='center', va='bottom',
            fontsize=10, fontweight='bold')

    # ============================================================
    # Step 9: Node 16 → Node 12 → 13 → 14
    # ============================================================
    draw_bar_node_switched(ax, x=NODE15_X, y_bar=y16_bar, label='16',
                           label_fontsize=10)

    bar12_y_mid = sw16_h_end_y
    bar12_y_top = bar12_y_mid + BAR_H / 2
    bar12_y_bot = bar12_y_mid - BAR_H / 2
    
    nodes12_14 = [12, 13, 14]
    prev_x = sw16_h_end_x
    
    for node_num in nodes12_14:
        if node_num == 12:
            ax.text(prev_x - bar1_w / 2, bar12_y_top - BAR_H * 0.20, str(node_num),
                    ha='right', va='center', fontsize=10, fontweight='bold')
        else:
            curr_x = prev_x + node_spacing
            ax.plot([prev_x + bar1_w/2, curr_x], [bar12_y_mid, bar12_y_mid], 'k-', lw=BUS_LW)
            ax.text(prev_x + node_spacing / 2, bar12_y_mid + 0.08, str(node_num),
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
            prev_x = curr_x
        
        draw_bar_node(ax, prev_x, bar12_y_top, bar12_y_bot, width=bar1_w, label=None)
        
        # Corner and arrow
        corner_y = bar12_y_bot + BAR_H * 0.25
        corner_x = prev_x - bar1_w / 2
        ax.plot([corner_x, corner_x - dx1], [corner_y, corner_y], 'k-', lw=BUS_LW)
        ax.plot([corner_x - dx1, corner_x - dx1], [corner_y, corner_y - dy1], 'k-', lw=BUS_LW)
        tri = plt.Polygon([(corner_x - dx1, corner_y - dy1 - arr_sz),
                           (corner_x - dx1 - arr_sz * 0.4, corner_y - dy1),
                           (corner_x - dx1 + arr_sz * 0.4, corner_y - dy1)],
                          closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
        ax.add_patch(tri)

    NODE14_X = prev_x

    # ============================================================
    # Step 10: Tie switch 21 (Node 3 ↔ Node 11)
    # ============================================================
    node3_br_x = NODE3_X = NODE1_X + 2 * node_spacing + bar1_w / 2
    corner3_y = bar1_y_bot + BAR_H * 0.25
    dx_r = 0.06

    node11_tl_x = NODE11_X - bar1_w / 2
    corner11_y = bar7_y_top - BAR_H * 0.20

    corner_end_x = node3_br_x + dx_r
    ax.plot([node3_br_x, corner_end_x], [corner3_y, corner3_y], 'k--', lw=BUS_LW, zorder=5)

    corner11_end_x = node11_tl_x - dx_r
    ax.plot([node11_tl_x, corner11_end_x], [corner11_y, corner11_y], 'k--', lw=BUS_LW, zorder=5)

    sw_x = (corner_end_x + corner11_end_x) / 2
    sw_y = (corner3_y + corner11_y) / 2
    short_len = SW_SIZE * 0.3
    
    ax.plot([sw_x - SW_SIZE/2, sw_x - SW_SIZE/2 - short_len], [sw_y, sw_y], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([sw_x + SW_SIZE/2, sw_x + SW_SIZE/2 + short_len], [sw_y, sw_y], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([corner_end_x, sw_x - SW_SIZE/2 - short_len], [corner3_y, sw_y], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([sw_x + SW_SIZE/2 + short_len, corner11_end_x], [sw_y, corner11_y], 'k--', lw=BUS_LW, zorder=4)
    draw_switch_open(ax, sw_x, sw_y, SW_SIZE)
    ax.text(sw_x, sw_y + SW_SIZE * 0.6, '21', ha='center', va='bottom',
            fontsize=10, fontweight='bold', zorder=7)

    # ============================================================
    # Step 11: Tie switch 22 (Node 9 ↔ Node 14)
    # ============================================================
    NODE9_X = NODE7_X = sw15_h_end_x + 2 * node_spacing if 'NODE7_X' not in locals() else NODE7_X + 2 * node_spacing
    node9_br_x = NODE9_X + bar1_w / 2
    corner9_y = bar7_y_bot + BAR_H * 0.25

    node14_rx = NODE14_X + bar1_w / 2
    node14_ry = bar12_y_mid

    sw22_x = NODE9_X + node_spacing / 2
    corner9_end_x = sw22_x
    corner14_end_x = sw22_x

    ax.plot([node9_br_x, corner9_end_x], [corner9_y, corner9_y], 'k--', lw=BUS_LW, zorder=5)
    ax.plot([node14_rx, corner14_end_x], [node14_ry, node14_ry], 'k--', lw=BUS_LW, zorder=5)

    sw22_y = (corner9_y + node14_ry) / 2
    short_len = SW_SIZE * 0.3
    
    ax.plot([sw22_x, sw22_x], [sw22_y - SW_SIZE/2 - short_len, sw22_y - SW_SIZE/2], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([sw22_x, sw22_x], [sw22_y + SW_SIZE/2, sw22_y + SW_SIZE/2 + short_len], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([corner9_end_x, sw22_x], [corner9_y, sw22_y - SW_SIZE/2 - short_len], 'k--', lw=BUS_LW, zorder=4)
    ax.plot([sw22_x, corner14_end_x], [sw22_y + SW_SIZE/2 + short_len, node14_ry], 'k--', lw=BUS_LW, zorder=4)
    draw_switch_open_vertical(ax, sw22_x, sw22_y, SW_SIZE)
    ax.text(sw22_x + SW_SIZE * 0.6, sw22_y, '22', ha='left', va='center',
            fontsize=10, fontweight='bold', zorder=7)

    # ============================================================
    # Final settings
    # ============================================================
    ax.autoscale_view()
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()

    if output_path is None:
        output_path = os.path.join(os.getcwd(), 'Figure 2 - One line diagram of a small distribution system.png')
    
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return output_path


if __name__ == '__main__':
    out_path = draw_ieee33bus_diagram()
    print(f'Saved IEEE 33-Bus single-line diagram to: {out_path}')
