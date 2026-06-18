"""CLI entry points — each function saves one element as a standalone PNG."""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .drawing_elements import (
    BUS_LW, NODE_LW, SW_SIZE,
    draw_switch, draw_switch_vertical, draw_switch_open, draw_switch_open_vertical,
    draw_substation_horizontal, draw_bar_node, draw_bar_node_switched,
    draw_node, draw_tf_node, draw_solid_node,
    draw_branch,
)


def _out(name):
    """Output path relative to cwd."""
    return os.path.join(os.getcwd(), name)


# ─── reproduce_fig2 ───
def reproduce_fig2():
    """Generate the complete IEEE 33-Bus single-line diagram (Baran.1989 Figure 2)."""
    from .reproduce_fig2 import draw_ieee33bus_diagram
    out_path = draw_ieee33bus_diagram()
    print(f'Saved IEEE 33-Bus single-line diagram to: {out_path}')


# ─── switch_symbol ───
def save_switch_symbol():
    fig, ax = plt.subplots(figsize=(1, 1))
    draw_switch(ax, 0.0, 0.0, SW_SIZE)
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-0.3, 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('switch_symbol.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('switch_symbol.png'))


# ─── switch_vertical ───
def save_switch_vertical():
    fig, ax = plt.subplots(figsize=(1, 1))
    draw_switch_vertical(ax, 0.0, 0.0, SW_SIZE)
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-0.3, 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('switch_vertical.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('switch_vertical.png'))


# ─── switch_open_h ───
def save_switch_open_h():
    fig, ax = plt.subplots(figsize=(1, 1))
    draw_switch_open(ax, 0.0, 0.0, SW_SIZE)
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-0.3, 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('switch_open_h.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('switch_open_h.png'))


# ─── switch_open_v ───
def save_switch_open_v():
    fig, ax = plt.subplots(figsize=(1, 1))
    draw_switch_open_vertical(ax, 0.0, 0.0, SW_SIZE)
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-0.3, 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('switch_open_v.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('switch_open_v.png'))


# ─── bar_node_short ───
def save_bar_node_short():
    fig, ax = plt.subplots(figsize=(3, 6))
    X, BAR_Y_TOP, BAR_Y_BOT, BAR_W = 0.0, -0.3, -0.9, 0.08
    draw_bar_node(ax, x=X, y_top=BAR_Y_TOP, y_bottom=BAR_Y_BOT, width=BAR_W, label=None)
    h = BAR_Y_TOP - BAR_Y_BOT
    corner_y = BAR_Y_BOT + h * 0.25
    corner_x = X - BAR_W / 2
    dx, dy = 0.16, 0.35
    ax.plot([corner_x, corner_x - dx], [corner_y, corner_y], 'k-', lw=BUS_LW)
    ax.plot([corner_x - dx, corner_x - dx], [corner_y, corner_y - dy], 'k-', lw=BUS_LW)
    arr_x, arr_y, arr_sz = corner_x - dx, corner_y - dy, 0.14
    tri = plt.Polygon([
        (arr_x, arr_y - arr_sz), (arr_x - arr_sz*0.4, arr_y), (arr_x + arr_sz*0.4, arr_y),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-1.5, 0.0)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('bar_node_short.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('bar_node_short.png'))


# ─── bar_node_horizontal ───
def save_bar_node_horizontal():
    fig, ax = plt.subplots(figsize=(5, 2))
    X, BAR_W, BAR_H = 0.0, 0.44, 0.03
    bar_left, bar_top = X - BAR_W/2, BAR_H/2
    ax.add_patch(Rectangle((bar_left, -BAR_H/2), BAR_W, BAR_H,
                 linewidth=0.5, edgecolor='k', facecolor='k', zorder=4))
    corner_x = bar_left + BAR_W * 0.25
    corner_y = -BAR_H/2
    dy, arr_sz = 0.128, 0.05
    ax.plot([corner_x, corner_x], [corner_y, corner_y - dy], 'k-', lw=BUS_LW)
    tri = plt.Polygon([
        (corner_x, corner_y - dy - arr_sz),
        (corner_x - arr_sz*0.4, corner_y - dy),
        (corner_x + arr_sz*0.4, corner_y - dy),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)
    ax.set_xlim(-0.30, 0.30); ax.set_ylim(-0.24, 0.08)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('bar_node_horizontal.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('bar_node_horizontal.png'))


# ─── node15 ───
def save_node15():
    from .coordinates import Y_SW_MID
    fig, ax = plt.subplots(figsize=(3, 4))
    draw_bar_node_switched(ax, x=1.0, y_bar=Y_SW_MID - 0.10, label='15')
    ax.set_xlim(0.5, 2.0); ax.set_ylim(-2.2, -0.8)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('node15.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('node15.png'))


# ─── load_node ───
def save_load_node():
    """Generate load node like Figure 2 node 1 (short bar + downward arrow)."""
    fig, ax = plt.subplots(figsize=(1.5, 2))
    
    # Horizontal bus line
    ax.plot([-0.4, 0.4], [0, 0], 'k-', lw=BUS_LW, zorder=5)
    
    # Short vertical bar (like Figure 2 node 1)
    bar_height = 0.15
    ax.plot([0, 0], [0, -bar_height], 'k-', lw=BUS_LW, zorder=5)
    
    # Downward arrow
    arrow_y = -bar_height - 0.25
    ax.plot([0, 0], [-bar_height, arrow_y], 'k-', lw=BUS_LW, zorder=5)
    # Arrow head
    arrow_size = 0.08
    tri = plt.Polygon([
        (0, arrow_y - arrow_size),
        (-arrow_size*0.5, arrow_y),
        (arrow_size*0.5, arrow_y),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)
    
    # Node label above
    ax.text(0, 0.15, '1', ha='center', va='bottom', 
            fontsize=11, fontweight='bold')
    
    ax.set_xlim(-0.6, 0.6); ax.set_ylim(-0.6, 0.4)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('load_node.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('load_node.png'))


# ─── load_node_left ───
def save_load_node_left():
    """Generate left-output load node (solid black bar + left corner + downward arrow)."""
    fig, ax = plt.subplots(figsize=(3, 6))
    X = 0.0
    BAR_H, BAR_W = 0.44, 0.03
    BAR_Y_TOP = 0.0
    BAR_Y_BOT = BAR_Y_TOP - BAR_H
    draw_bar_node(ax, x=X, y_top=BAR_Y_TOP, y_bottom=BAR_Y_BOT, width=BAR_W, label=None)
    corner_y = BAR_Y_BOT + BAR_H * 0.25
    corner_x = X - BAR_W / 2
    dx, dy = 0.06, 0.128
    ax.plot([corner_x, corner_x - dx], [corner_y, corner_y], 'k-', lw=BUS_LW)
    ax.plot([corner_x - dx, corner_x - dx], [corner_y, corner_y - dy], 'k-', lw=BUS_LW)
    arr_x, arr_y, arr_sz = corner_x - dx, corner_y - dy, 0.05
    tri = plt.Polygon([
        (arr_x, arr_y - arr_sz),
        (arr_x - arr_sz * 0.4, arr_y),
        (arr_x + arr_sz * 0.4, arr_y),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)
    ax.text(X, BAR_Y_TOP + 0.10, 'N', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_xlim(-0.4, 0.4); ax.set_ylim(BAR_Y_BOT - 0.3, BAR_Y_TOP + 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('load_node_left.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('load_node_left.png'))


# ─── load_node_right ───
def save_load_node_right():
    """Generate right-output load node (solid black bar + right corner + downward arrow)."""
    fig, ax = plt.subplots(figsize=(3, 6))
    X = 0.0
    BAR_H, BAR_W = 0.44, 0.03
    BAR_Y_TOP = 0.0
    BAR_Y_BOT = BAR_Y_TOP - BAR_H
    draw_bar_node(ax, x=X, y_top=BAR_Y_TOP, y_bottom=BAR_Y_BOT, width=BAR_W, label=None)
    corner_y = BAR_Y_BOT + BAR_H * 0.25
    corner_x = X + BAR_W / 2
    dx, dy = 0.06, 0.128
    ax.plot([corner_x, corner_x + dx], [corner_y, corner_y], 'k-', lw=BUS_LW)
    ax.plot([corner_x + dx, corner_x + dx], [corner_y, corner_y - dy], 'k-', lw=BUS_LW)
    arr_x, arr_y, arr_sz = corner_x + dx, corner_y - dy, 0.05
    tri = plt.Polygon([
        (arr_x, arr_y - arr_sz),
        (arr_x - arr_sz * 0.4, arr_y),
        (arr_x + arr_sz * 0.4, arr_y),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)
    ax.text(X, BAR_Y_TOP + 0.10, 'N', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_xlim(-0.4, 0.4); ax.set_ylim(BAR_Y_BOT - 0.3, BAR_Y_TOP + 0.3)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('load_node_right.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('load_node_right.png'))


# ─── tf_node ───
def save_tf_node():
    fig, ax = plt.subplots(figsize=(3, 3))
    draw_tf_node(ax, 0.0, 0.0, 'N', 'T1')
    ax.set_xlim(-0.5, 1.0); ax.set_ylim(-1.2, 0.4)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('tf_node.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('tf_node.png'))


# ─── ss1 ───
def save_ss1_symbol():
    fig, ax = plt.subplots(figsize=(1, 1.5))
    ss_w, y_bot, y_top = 0.10, -1.4, 0.0
    ax.add_patch(Rectangle((-ss_w/2, y_bot), ss_w, y_top - y_bot,
                 linewidth=0.5, edgecolor='k', facecolor='k', zorder=4))
    ax.text(0.0, y_top + 0.10, 'SS1', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_xlim(-0.3, 0.3); ax.set_ylim(-1.6, 0.5)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('ss1_symbol.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('ss1_symbol.png'))


# ─── ss2 ───
def save_ss2_symbol():
    fig, ax = plt.subplots(figsize=(2, 2))
    draw_substation_horizontal(ax, 0.0, 0.0, 'SS2')
    ax.set_xlim(-0.4, 0.4); ax.set_ylim(-0.5, 0.6)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('ss2_symbol.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('ss2_symbol.png'))


# ─── solid_node ───
def save_solid_node():
    fig, ax = plt.subplots(figsize=(0.8, 0.8))
    draw_solid_node(ax, 0.0, 0.0)
    ax.set_xlim(-0.15, 0.15); ax.set_ylim(-0.15, 0.15)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('solid_node.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('solid_node.png'))


# ─── reproduce_fig1 ───
def reproduce_fig1():
    """Generate the SS1 + two closed switches diagram (Figure 1)."""
    from .reproduce_fig1 import draw_ss1_switches_diagram
    out_path = draw_ss1_switches_diagram()
    print(f'Saved SS1+switches diagram to: {out_path}')


# ─── reproduce_fig_cb1_cb2 ───
def reproduce_fig_cb1_cb2():
    """Generate the SS1 + CB1 + CB2 + CB3 + CB5 topology diagram."""
    from .reproduce_fig_cb1_cb2 import draw_cb1_cb2_diagram
    out_path = draw_cb1_cb2_diagram()
    print(f'Saved SS1+CB1+CB2+CB3+CB5 diagram to: {out_path}')


# ─── branch ───
def save_branch():
    fig, ax = plt.subplots(figsize=(0.8, 1.5))
    w, h = 0.0375, 0.28125
    draw_branch(ax, 0.0, 0.0, w, h)
    ax.set_xlim(-0.15, 0.15); ax.set_ylim(-0.35, 0.35)
    ax.set_aspect('equal'); ax.axis('off')
    plt.tight_layout()
    plt.savefig(_out('branch.png'), dpi=200, bbox_inches='tight', facecolor='white')
    print('Saved:', _out('branch.png'))


# ─── reproduce_fig3 ───
def reproduce_fig3():
    """Generate Figure 3 -- One line diagram of a radial network."""
    from .reproduce_fig3 import draw_fig3_diagram
    out_path = draw_fig3_diagram()
    print(f'Saved Figure 3 (radial network) to: {out_path}')


# ─── reproduce_fig4 ───
def reproduce_fig4():
    """Generate Figure 4 -- The loop associated with open branch b."""
    from .reproduce_fig4 import draw_fig4_diagram
    out_path = draw_fig4_diagram()
    print(f'Saved Figure 4 (branch exchange loop) to: {out_path}')
