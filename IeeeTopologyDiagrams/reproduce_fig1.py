"""
Figure 1 — Schematic diagram of a primary circuit of a distribution system
          配电系统一次回路示意图
===========================================================================

Source / 出处:
    M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems
    for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery,
    Vol. 4, No. 2, pp. 1401-1407, April 1989.

Paper Description / 原文描述:
    "Fig.1 shows a schematic diagram of a simplified primary circuit of a
    distribution system together with sectionalizing switches. In the figure,
    load points, where the distribution transformers are tapped off from
    the primary circuit, is marked by dots, '·' As also shown in the figure,
    there are two types of switches in the system: normally closed switches
    connecting the line sections (CB1-CB6), and normally open switches on
    the tie-lines connecting either two primary feeders (CB7), or two
    substations (CB8), or loop-type laterals (CB9)."

    — Section I: INTRODUCTION (p.1401)

Key Terms / 关键术语:
    - sectionalizing switch      分段开关
    - normally closed switch     常闭开关(CB)
    - normally open switch       常开开关/联络开关(CB7-CB9)
    - tie-line                   联络线
    - primary circuit            一次回路
    - load point                 负荷点(·标记)
    - distribution transformer   配电变压器
    - loop-type lateral          环型侧馈线
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .drawing_elements import (
    BUS_LW, SW_SIZE,
    draw_switch,
)


def draw_ss1_switches_diagram(output_path=None):
    """
    Draw SS1 with two closed switches.

    Args:
        output_path: Path to save the output PNG. If None, saves to cwd.

    Returns:
        The path where the figure was saved.
    """
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
    fig, ax = plt.subplots(figsize=(3.5, 2.0))

    # 1. SS1 — solid black vertical rectangle
    rect = Rectangle((SS1_X - SS1_WIDTH / 2, SS1_BOT), SS1_WIDTH, SS1_HEIGHT,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect)
    ax.text(SS1_X, SS1_TOP + LABEL_OFFSET, 'SS1',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 2. Two horizontal bus lines
    ss1_right = SS1_X + SS1_WIDTH / 2
    ax.plot([ss1_right, SW1_X - SW_SIZE / 2], [Y_SW1, Y_SW1],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([ss1_right, SW2_X - SW_SIZE / 2], [Y_SW2, Y_SW2],
            'k-', lw=BUS_LW, zorder=5)

    # 3. Two closed switches
    draw_switch(ax, SW1_X, Y_SW1, SW_SIZE)
    draw_switch(ax, SW2_X, Y_SW2, SW_SIZE)

    # 4. Set bounds
    padding_x = 0.3
    padding_y = 0.25
    ax.set_xlim(SS1_X - SS1_WIDTH / 2 - padding_x, SW1_X + SW_SIZE / 2 + padding_x)
    ax.set_ylim(SS1_BOT - padding_y, SS1_TOP + LABEL_OFFSET + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')

    # 5. Save
    if output_path is None:
        output_path = os.path.join(os.getcwd(), 'Figure 1 (partial) - SS1 with closed switches.png')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return output_path