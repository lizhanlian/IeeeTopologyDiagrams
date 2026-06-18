"""
Figure 4 — The loop associated with open branch b
         与常开支路 b 关联的环路示意图
===========================================================================

Author : 黎湛联 (Zhanlian Li)
Package: IeeeTopologyDiagrams
Version: 4.0.6

Source / 出处:
    M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems
    for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery,
    Vol. 4, No. 2, pp. 1401-1407, April 1989.

Paper Description / 原文描述:
    "In general, given a spanning tree T_0, we associate a loop with every
    open branch in the network by considering as if the branch were closed.
    Fig.4 shows such a loop associated with open branch b. Branch exchange
    creates a new tree by closing an open branch, (branch b in the figure)
    and by opening a closed branch in the loop (say branch m in the figure)."

    — Section III: A SEARCH METHOD USING BRANCH EXCHANGES (p.1403)

Structure / 结构:
    The loop consists of:
    - Common node o (source node 0)
    - L-side (left path):  o → Pok → left bus bar → i-1 → k-1 → k
    - R-side (right path): o → Pon → ... → n-1 → n → right bus bar → Pio
    - Open branch b (dashed line) connecting k to n
    - Branch m (to be opened) on the L-side between the stub and i-1
    - Power flow labels: Pm, Pk-1, Pk, ΔPn, Pio, Pok, Pon

Key Terms / 关键术语:
    - branch exchange         支路交换
    - spanning tree           生成树
    - open branch b           常开支路 b
    - common node o           公共节点 o
    - nominal branch exchange 标称支路交换 (b↔k)
    - L-side / R-side         L侧 / R侧
    - power loss reduction    网损降低
    - DistFlow                配电潮流方程
"""

import os
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset'] = 'stix'
import matplotlib.pyplot as plt
from .drawing_elements import (BUS_LW, TEXT_FS, _DASH_ON, _DASH_OFF,
                              draw_common_node_o, draw_common_node_o_left,
                              draw_common_node_o_right, draw_node_i_minus_1,
                              draw_feeder_extension_horizontal,
                              draw_node_k_minus_1, draw_node_k, draw_node_n,
                              draw_bar_node)


def draw_fig4_diagram(output_path=None):
    if output_path is None:
        output_path = os.path.join(
            os.getcwd(),
            'Figure 4 - The loop associated with open branch b.png'
        )

    fig, ax = plt.subplots()                         # figsize 由 bbox_inches='tight' 自动确定

    # ============================================================
    # Y-axis shared parameters
    # ============================================================
    o_y = 1.5
    bar_y = 1.3
    stub_y = -0.75                                   # 左竖母线底部 stub y
    pm_y = -0.98
    arrow_y = (stub_y + pm_y) / 2
    bar_h = 0.7

    # ============================================================
    # 1. Left bus bar + Pm + i-1 (fixed left anchor)
    # ============================================================
    left_bus_x, left_bus_y = 0.3, -0.4
    draw_common_node_o_left(ax, left_bus_x, left_bus_y, bar_length=1.4, feeder_len=0.1)

    stub_x = left_bus_x + 0.1                        # 0.4
    ax.annotate('', xy=(0.87, arrow_y), xytext=(stub_x, arrow_y),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    ax.text(stub_x - 0.02, pm_y, r'$P_m$', ha='left', va='top',
            fontsize=18, fontstyle='italic')
    conn_len = 0.7 * 0.7 * 1.5
    i1_x = stub_x + conn_len
    ax.plot([stub_x, i1_x], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)
    ax.text((stub_x + i1_x) / 2, stub_y + 0.15, r'$(m)$',
            ha='center', va='bottom', fontsize=18, fontstyle='italic')
    draw_node_i_minus_1(ax, i1_x, stub_y, label=None)

    # ============================================================
    # 2. Right side — compute all x positions from i-1
    # ============================================================
    dash_start_x = i1_x + bar_h * 0.7
    dash_end_x = dash_start_x + bar_h * 0.8
    draw_feeder_extension_horizontal(ax, dash_start_x, dash_end_x, stub_y)

    k1_x = dash_end_x + bar_h * 0.7
    ax.plot([dash_end_x, k1_x], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)

    k_conn_start_x = k1_x + bar_h * 0.7
    k_x = k_conn_start_x + bar_h * 0.7
    ax.plot([k_conn_start_x, k_x], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)

    # k-1 subfigure + k node
    draw_node_k_minus_1(ax, k1_x, stub_y, next_x=k_x, bar_h=bar_h, pm_y=pm_y)
    draw_node_k(ax, k_x, stub_y, bar_h=bar_h)

    # Pk
    bar_bot = stub_y - bar_h / 2
    pk_y = bar_bot - 0.389                          # 下移 1/2
    pk_arrow_start = bar_bot - 0.0395
    pk_arrow_end = pk_arrow_start - 0.47
    ax.annotate('', xy=(k_x, pk_arrow_end), xytext=(k_x, pk_arrow_start),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    ax.text(k_x + 0.10, pk_y, r'$P_k$',
            ha='left', va='center', fontsize=18, fontstyle='italic', color='#333333')

    # n node via dashed
    n_x = k_x + bar_h * 0.7 * 2
    draw_feeder_extension_horizontal(ax, k_x, n_x, stub_y)
    draw_node_n(ax, n_x, stub_y, bar_h=bar_h)

    # ΔPn
    n_pn_arrow_y = stub_y - 0.115
    ax.annotate('', xy=(n_x - 0.10 - 0.47, n_pn_arrow_y),
                xytext=(n_x - 0.10, n_pn_arrow_y),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    ax.text(n_x - 0.015 - 0.02, pm_y, r'$\Delta P_n$',
            ha='right', va='top', fontsize=18, fontstyle='italic', color='#333333')

    # n-1 node
    n1_x = n_x + bar_h * 0.7 * 2
    ax.plot([n_x, n1_x], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)
    draw_bar_node(ax, n1_x, y_top=stub_y + bar_h / 2, y_bottom=stub_y - bar_h / 2,
                  width=0.06)
    ax.text(n1_x, stub_y + bar_h / 2 + 0.06, r'$n\!-\!1$',
            ha='center', va='bottom', fontsize=TEXT_FS, fontweight='bold')

    # Right bus bar connection (solid-dashed-solid)
    conn_total = 1.5
    right_feeder_len = 0.1
    conn_end = n1_x + conn_total
    right_bus_x = conn_end + right_feeder_len
    right_bus_y = -0.4
    dash_len = conn_total / 2
    solid_len = conn_total / 4
    db_start = n1_x + solid_len
    db_end = conn_end - solid_len
    ax.plot([n1_x, db_start], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)
    draw_feeder_extension_horizontal(ax, db_start, db_end, stub_y)
    ax.plot([db_end, conn_end], [stub_y, stub_y], 'k-', lw=BUS_LW, zorder=5)
    draw_common_node_o_right(ax, right_bus_x, right_bus_y,
                              bar_length=1.4, feeder_len=right_feeder_len,
                              corner=True, corner_h=0.7)

    # Pio
    c_h = 0.7
    rb_half = 0.7
    c_y = right_bus_y - rb_half + c_h * 0.25
    dash_bot = c_y - c_h * 0.29 - c_h * 0.7
    pio_arrow_end = dash_bot
    pio_arrow_start = pio_arrow_end + 0.47
    pio_y = (pio_arrow_start + pio_arrow_end) / 2
    ax.annotate('', xy=(right_bus_x, pio_arrow_end), xytext=(right_bus_x, pio_arrow_start),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    ax.text(right_bus_x - 0.10, pio_y, r'$P_{io}$',
            ha='right', va='center', fontsize=18, fontstyle='italic', color='#333333')

    # ============================================================
    # 3. (b) label — between k and n
    # ============================================================
    ax.text((k_x + n_x) / 2, stub_y + 0.15, r'$(b)$',
            ha='center', va='bottom', fontsize=18, fontstyle='italic')

    # ============================================================
    # 4. Top node o — center aligned with (b)
    # ============================================================
    o_x = (k_x + n_x) / 2
    bar_length = 1.4
    draw_common_node_o(ax, o_x, o_y, bar_length=bar_length, label=r'$0$')
    # Pok (left feeder)
    fd_l_x = o_x - bar_length * 0.25
    ax.plot([fd_l_x, fd_l_x], [bar_y, bar_y - 0.1], 'k-', lw=BUS_LW, zorder=5)
    # Pon (right feeder)
    fd_r_x = o_x + bar_length * 0.25
    ax.plot([fd_r_x, fd_r_x], [bar_y, bar_y - 0.1], 'k-', lw=BUS_LW, zorder=5)

    # ============================================================
    # 5. stub 虚线延长 + 斜线连接
    #    Pok/Pon：垂直向下
    #    竖母线上端：水平
    #    延长长度 = (i-1 到左 stub) 的 1/2
    # ============================================================
    dash_extend = (i1_x - (left_bus_x + 0.1)) / 2
    pok_foot_x, pok_foot_y = fd_l_x, bar_y - 0.1
    pon_foot_x, pon_foot_y = fd_r_x, bar_y - 0.1
    left_top_x, left_top_y = left_bus_x + 0.1, left_bus_y + 1.4 * 0.25
    right_top_x, right_top_y = right_bus_x - 0.1, right_bus_y + 1.4 * 0.25
    # Pok 脚：垂直向下虚线延长
    pok_y_ext = pok_foot_y - dash_extend
    ax.plot([pok_foot_x, pok_foot_x], [pok_foot_y, pok_y_ext],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # Pon 脚：垂直向下虚线延长
    pon_y_ext = pon_foot_y - dash_extend
    ax.plot([pon_foot_x, pon_foot_x], [pon_foot_y, pon_y_ext],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # 左竖母线上端：水平向右虚线延长
    l_ext_x = left_top_x + dash_extend
    ax.plot([left_top_x, l_ext_x], [left_top_y, left_top_y],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # 右竖母线上端：水平向左虚线延长
    r_ext_x = right_top_x - dash_extend
    ax.plot([r_ext_x, right_top_x], [right_top_y, right_top_y],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # 斜线连接
    ax.plot([pok_foot_x, l_ext_x], [pok_y_ext, left_top_y],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # 左斜线平行箭头（向下，与斜线同斜率，长度固定）
    dx_l = l_ext_x - pok_foot_x
    dy_l = left_top_y - pok_y_ext
    l_len = (dx_l**2 + dy_l**2)**0.5
    l_nx, l_ny = dx_l / l_len, dy_l / l_len
    l_mid_x = (pok_foot_x + l_ext_x) / 2
    l_mid_y = (pok_y_ext + left_top_y) / 2
    alen = 0.47
    ax.annotate('', xy=(l_mid_x + 0.50, l_mid_y + 0.35),
                xytext=(l_mid_x + 0.50 - l_nx * alen, l_mid_y + 0.35 - l_ny * alen),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    # Pok 标签：左斜线上方
    ax.text(l_mid_x, l_mid_y + 0.40,
            r'$P_{ok}$', ha='right', va='center',
            fontsize=20, fontstyle='italic', color='#333333')
    ax.plot([pon_foot_x, r_ext_x], [pon_y_ext, right_top_y],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)
    # 右斜线平行箭头（向下，与斜线同斜率，长度固定）
    dx_r = r_ext_x - pon_foot_x
    dy_r = right_top_y - pon_y_ext
    r_len = (dx_r**2 + dy_r**2)**0.5
    r_nx, r_ny = dx_r / r_len, dy_r / r_len
    r_mid_x = (pon_foot_x + r_ext_x) / 2
    r_mid_y = (pon_y_ext + right_top_y) / 2
    ax.annotate('', xy=(r_mid_x - 0.50, r_mid_y + 0.35),
                xytext=(r_mid_x - 0.50 - r_nx * alen, r_mid_y + 0.35 - r_ny * alen),
                arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
    # Pon 标签：右斜线上方
    ax.text(r_mid_x, r_mid_y + 0.40,
            r'$P_{on}$', ha='left', va='center',
            fontsize=20, fontstyle='italic', color='#333333')
    # Axis settings（自动跟随最右侧元素）
    # ============================================================
    x_left = -0.6
    x_right = right_bus_x + 0.9                       # 右侧留边距（Pn 标签）
    ax.set_xlim(x_left, x_right)
    ax.set_ylim(-2.2, 3.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # ============================================================
    # Title
    # ============================================================
    ax.set_title('Figure 4 -- The loop associated with open branch $b$',
                 fontsize=22, fontweight='bold', pad=8)

    # ============================================================
    # 6. Save
    # ============================================================
    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)

    print(f"Saved: {output_path}")
    return output_path


if __name__ == '__main__':
    draw_fig4_diagram()
