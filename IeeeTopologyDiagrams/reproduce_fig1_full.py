"""
Figure 1 (complete) — Schematic diagram of a primary circuit of a distribution system
                       配电系统一次回路完整示意图
===================================================================================

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

Structure / 结构:
    * Two substations (SS1, SS2)
    * Two main primary feeders, each with 3 sectionalizing CBs (CB1-CB3, CB4-CB6)
    * CB7 - normally open tie between the two feeders (feeder-to-feeder)
    * CB8 - normally open tie between the two substations (substation-to-substation)
    * CB9 - normally open tie on a loop-type lateral
    * Load points (·) along each feeder section
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .drawing_elements import (
    BUS_LW, SW_SIZE, _SOLID_NODE_R,
    draw_switch, draw_switch_open,
)


def draw_fig1_complete(output_path=None):
    """
    Draw the complete Figure 1 from Baran & Wu (1989).

    Layout:
        Top row:    SS1 ── CB1 ── · ── CB2 ── · ── CB3 ── · ──┐
        Bottom row: SS2 ── CB4 ── · ── CB5 ── · ── CB6 ── · ──┴── (CB7 vertical tie)
        Additional: CB8 horizontal tie between SS1 and SS2
                    CB9 loop on a lateral branch
    """
    # ============================================================
    # Layout parameters
    # ============================================================
    # Y positions of the two feeder rows
    Y_TOP = 0.0        # top feeder row (feeder 1, from SS1)
    Y_BOT = -5.0       # bottom feeder row (feeder 2, from SS2)

    # Feeder x layout: section length = FEEDER_DX
    FEEDER_DX = 2.2

    # Substation position (left side)
    SS_X = 0.0
    SS1_Y_CENTER = (Y_TOP + 0)  # SS1 is on top row
    SS2_Y_CENTER = (Y_BOT + 0)  # SS2 is on bottom row

    SS_WIDTH = 0.30
    SS_HEIGHT = 1.10

    LABEL_FS = 16
    NODE_FS = 14

    # ============================================================
    # Create figure
    # ============================================================
    fig, ax = plt.subplots(figsize=(22, 11))

    # ============================================================
    # Substations
    # ============================================================
    # SS1 (top, solid black rectangle)
    ss1_x_left = SS_X - SS_WIDTH / 2
    ss1_y_bot = Y_TOP - SS_HEIGHT / 2
    rect1 = Rectangle((ss1_x_left, ss1_y_bot), SS_WIDTH, SS_HEIGHT,
                      linewidth=1.2, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect1)
    ax.text(SS_X, Y_TOP + SS_HEIGHT / 2 + 0.20, 'SS1',
            ha='center', va='bottom', fontsize=LABEL_FS, fontweight='bold')

    # SS2 (bottom, hollow rectangle with double-line style)
    ss2_x_left = SS_X - SS_WIDTH / 2
    ss2_y_bot = Y_BOT - SS_HEIGHT / 2
    rect2 = Rectangle((ss2_x_left, ss2_y_bot), SS_WIDTH, SS_HEIGHT,
                      linewidth=1.2, edgecolor='k', facecolor='white', zorder=4)
    ax.add_patch(rect2)
    # inner vertical lines to indicate double-bus style
    ax.plot([ss2_x_left + 0.08, ss2_x_left + 0.08], [ss2_y_bot + 0.10, ss2_y_bot + SS_HEIGHT - 0.10],
            'k-', lw=1.0, zorder=4)
    ax.plot([ss2_x_left + SS_WIDTH - 0.08, ss2_x_left + SS_WIDTH - 0.08], [ss2_y_bot + 0.10, ss2_y_bot + SS_HEIGHT - 0.10],
            'k-', lw=1.0, zorder=4)
    ax.text(SS_X, Y_BOT - SS_HEIGHT / 2 - 0.20, 'SS2',
            ha='center', va='top', fontsize=LABEL_FS, fontweight='bold')

    # ============================================================
    # Feeder row 1 (top, from SS1): 3 CB sections + load dots
    # ============================================================
    # X positions
    x_ss1_right = SS_X + SS_WIDTH / 2
    x_cb1 = x_ss1_right + FEEDER_DX * 0.5
    x_load1 = x_cb1 + FEEDER_DX * 0.5
    x_cb2 = x_load1 + FEEDER_DX * 0.5
    x_load2 = x_cb2 + FEEDER_DX * 0.5
    x_cb3 = x_load2 + FEEDER_DX * 0.5
    x_load3 = x_cb3 + FEEDER_DX * 0.5

    # Draw bus lines
    ax.plot([x_ss1_right, x_cb1 - SW_SIZE / 2], [Y_TOP, Y_TOP], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb1 + SW_SIZE / 2, x_cb2 - SW_SIZE / 2], [Y_TOP, Y_TOP], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb2 + SW_SIZE / 2, x_cb3 - SW_SIZE / 2], [Y_TOP, Y_TOP], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb3 + SW_SIZE / 2, x_load3 + 0.4], [Y_TOP, Y_TOP], 'k-', lw=BUS_LW, zorder=3)

    # Draw CB1, CB2, CB3 (normally closed — solid black boxes)
    draw_switch(ax, x_cb1, Y_TOP, SW_SIZE)
    draw_switch(ax, x_cb2, Y_TOP, SW_SIZE)
    draw_switch(ax, x_cb3, Y_TOP, SW_SIZE)

    # Labels under each CB
    ax.text(x_cb1, Y_TOP - 0.30, 'CB1', ha='center', va='top', fontsize=NODE_FS)
    ax.text(x_cb2, Y_TOP - 0.30, 'CB2', ha='center', va='top', fontsize=NODE_FS)
    ax.text(x_cb3, Y_TOP - 0.30, 'CB3', ha='center', va='top', fontsize=NODE_FS)

    # Load points (solid dots) between CBs and at end
    y_load = Y_TOP + 0.02
    for lx in [x_load1, x_load2, x_load3]:
        circle = plt.Circle((lx, y_load), _SOLID_NODE_R, facecolor='k', edgecolor='k', zorder=5)
        ax.add_artist(circle)
        ax.text(lx, Y_TOP + 0.35, '·', ha='center', va='bottom', fontsize=24)

    # ============================================================
    # Feeder row 2 (bottom, from SS2): CB4-CB6 + load dots
    # ============================================================
    x_ss2_right = SS_X + SS_WIDTH / 2
    x_cb4 = x_ss2_right + FEEDER_DX * 0.5
    x_load4 = x_cb4 + FEEDER_DX * 0.5
    x_cb5 = x_load4 + FEEDER_DX * 0.5
    x_load5 = x_cb5 + FEEDER_DX * 0.5
    x_cb6 = x_load5 + FEEDER_DX * 0.5
    x_load6 = x_cb6 + FEEDER_DX * 0.5

    # Draw bus lines
    ax.plot([x_ss2_right, x_cb4 - SW_SIZE / 2], [Y_BOT, Y_BOT], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb4 + SW_SIZE / 2, x_cb5 - SW_SIZE / 2], [Y_BOT, Y_BOT], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb5 + SW_SIZE / 2, x_cb6 - SW_SIZE / 2], [Y_BOT, Y_BOT], 'k-', lw=BUS_LW, zorder=3)
    ax.plot([x_cb6 + SW_SIZE / 2, x_load6 + 0.4], [Y_BOT, Y_BOT], 'k-', lw=BUS_LW, zorder=3)

    # Draw CB4, CB5, CB6
    draw_switch(ax, x_cb4, Y_BOT, SW_SIZE)
    draw_switch(ax, x_cb5, Y_BOT, SW_SIZE)
    draw_switch(ax, x_cb6, Y_BOT, SW_SIZE)

    # Labels
    ax.text(x_cb4, Y_BOT + 0.30, 'CB4', ha='center', va='bottom', fontsize=NODE_FS)
    ax.text(x_cb5, Y_BOT + 0.30, 'CB5', ha='center', va='bottom', fontsize=NODE_FS)
    ax.text(x_cb6, Y_BOT + 0.30, 'CB6', ha='center', va='bottom', fontsize=NODE_FS)

    # Load points
    for lx in [x_load4, x_load5, x_load6]:
        circle = plt.Circle((lx, Y_BOT - 0.02), _SOLID_NODE_R, facecolor='k', edgecolor='k', zorder=5)
        ax.add_artist(circle)

    # ============================================================
    # CB7 - feeder-to-feeder tie (normally open, vertical line
    # connecting the end of feeder 1 to feeder 2)
    # ============================================================
    x_cb7 = x_load3 + 0.15  # tie position at the right end of both feeders
    y_top_tie = Y_TOP
    y_bot_tie = Y_BOT

    # Vertical dashed tie line (open)
    ax.plot([x_cb7, x_cb7], [y_top_tie, y_bot_tie], 'k--', lw=BUS_LW, zorder=2)

    # CB7 open switch symbol in middle
    y_cb7 = (y_top_tie + y_bot_tie) / 2
    # small open circle to indicate normally open tie
    draw_switch_open(ax, x_cb7, y_cb7, SW_SIZE)
    ax.text(x_cb7 + 0.25, y_cb7, 'CB7 (open tie)', ha='left', va='center', fontsize=NODE_FS)

    # ============================================================
    # CB8 - substation-to-substation tie (normally open,
    # horizontal dashed line connecting SS1 to SS2 on the left)
    # ============================================================
    x_cb8_line = SS_X - SS_WIDTH / 2 - 0.80
    ax.plot([x_cb8_line, x_cb8_line], [Y_TOP - 0.2, Y_BOT + 0.2], 'k--', lw=BUS_LW, zorder=2)
    # CB8 open switch in the middle
    y_cb8 = (Y_TOP + Y_BOT) / 2
    draw_switch_open(ax, x_cb8_line, y_cb8, SW_SIZE)
    # connect to SS1 and SS2
    ax.plot([SS_X - SS_WIDTH / 2, x_cb8_line + 0.05], [Y_TOP, Y_TOP], 'k-', lw=BUS_LW, zorder=2)
    ax.plot([SS_X - SS_WIDTH / 2, x_cb8_line + 0.05], [Y_BOT, Y_BOT], 'k-', lw=BUS_LW, zorder=2)
    ax.text(x_cb8_line - 0.25, y_cb8, 'CB8', ha='right', va='center', fontsize=NODE_FS)

    # ============================================================
    # CB9 - loop-type lateral
    # A loop on the top feeder at x_load2 position — a small
    # rectangular loop off the main feeder, with an open switch.
    # ============================================================
    loop_x = x_load2  # position on the top feeder
    loop_top_y = Y_TOP + 1.1
    loop_bot_y = Y_TOP + 0.2
    loop_left = loop_x - 0.5
    loop_right = loop_x + 0.5

    # Left side of loop: from main feeder up, across, back down
    ax.plot([loop_x, loop_left], [Y_TOP + 0.02, Y_TOP + 0.02], 'k-', lw=BUS_LW, zorder=2)
    ax.plot([loop_left, loop_left], [Y_TOP + 0.02, loop_top_y], 'k-', lw=BUS_LW, zorder=2)
    ax.plot([loop_left, loop_right], [loop_top_y, loop_top_y], 'k-', lw=BUS_LW, zorder=2)
    # Right side of loop (open tie at top): dashed with CB9
    # draw two sections to indicate open switch at middle top
    ax.plot([loop_right, loop_right], [loop_top_y, loop_top_y - 0.1], 'k-', lw=BUS_LW, zorder=2)
    # open switch gap
    draw_switch_open(ax, loop_right, loop_top_y - 0.15, SW_SIZE)
    ax.plot([loop_right, loop_right], [loop_top_y - 0.2, Y_TOP + 0.02], 'k-', lw=BUS_LW, zorder=2)
    ax.text(loop_right + 0.20, loop_top_y - 0.15, 'CB9\n(loop)\n',
            ha='left', va='center', fontsize=NODE_FS)

    # A load point inside the loop
    loop_load_x = (loop_left + loop_right) / 2
    circle = plt.Circle((loop_load_x, loop_top_y - 0.02), _SOLID_NODE_R, facecolor='k', edgecolor='k', zorder=5)
    ax.add_artist(circle)
    # vertical stub to indicate lateral
    ax.plot([loop_load_x, loop_load_x], [loop_top_y, loop_top_y + 0.25], 'k-', lw=BUS_LW, zorder=2)

    # ============================================================
    # Set axis bounds
    # ============================================================
    ax.set_xlim(-2.5, x_load3 + 2.5)
    ax.set_ylim(Y_BOT - 1.2, Y_TOP + 2.0)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0.5, 0.95, 'Figure 1 — Primary circuit schematic',
            ha='center', va='top', fontsize=20, fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.5, 0.90,
            'CB1–CB6 = normally closed sectionalizing switches  |  '
            'CB7–CB9 = normally open tie switches  |  · = load points',
            ha='center', va='top', fontsize=13, style='italic',
            transform=ax.transAxes)

    # ============================================================
    # Save
    # ============================================================
    if output_path is None:
        output_path = os.path.join(os.getcwd(), 'Figure 1 - Complete primary circuit schematic.png')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return output_path