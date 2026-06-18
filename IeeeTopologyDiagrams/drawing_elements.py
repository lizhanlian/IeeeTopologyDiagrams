"""
IEEE 33-Bus 单线图绘图基元模块
提供所有可复用的绘图函数和样式常量

出处：M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems
      for Loss Reduction and Load Balancing," IEEE Trans. Power Del., 1989.
"""

from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

# ============================================================
# 样式常量
# ============================================================
BUS_LW = 2.2       # 母线线宽
NODE_LW = 1.1      # 节点/开关线宽
TEXT_FS = 20       # 节点编号字号
LABEL_FS = 18      # 配变标签字号
TITLE_FS = 22      # 标题字号
SW_SIZE = 0.18     # 开关符号大小


def draw_switch(ax, x, y, size=SW_SIZE):
    """画一个闭合开关符号（方框内一条水平线，表示常闭断路器 / circuit breaker closed）"""
    box = Rectangle((x - size / 2, y - size / 2), size, size,
                    linewidth=BUS_LW, edgecolor='k', facecolor='white', zorder=4)
    ax.add_patch(box)
    ax.plot([x - size / 2, x + size / 2], [y, y],
            'k-', lw=BUS_LW, zorder=5)


def draw_switch_vertical(ax, x, y, size=SW_SIZE):
    """画一个垂直闭合开关符号（方框内一条竖直线，表示常闭断路器 / circuit breaker closed）"""
    box = Rectangle((x - size / 2, y - size / 2), size, size,
                    linewidth=BUS_LW, edgecolor='k', facecolor='white', zorder=4)
    ax.add_patch(box)
    ax.plot([x, x], [y - size / 2, y + size / 2],
            'k-', lw=BUS_LW, zorder=5)


def draw_switch_open(ax, x, y, size=SW_SIZE):
    """画一个断开开关符号（方框 + 斜线 + 横线，表示常开断路器 / circuit breaker open）"""
    box = Rectangle((x - size / 2, y - size / 2), size, size,
                    linewidth=BUS_LW, edgecolor='k', facecolor='white', zorder=4)
    ax.add_patch(box)
    d = size * 0.25
    ax.plot([x - size/2, x - d, x + d],
            [y, y, y + size/2],
            'k-', lw=BUS_LW, zorder=5, solid_joinstyle='round', solid_capstyle='round')
    ax.plot([x + d, x + size/2], [y, y],
            'k-', lw=BUS_LW, zorder=5)


def draw_switch_open_vertical(ax, x, y, size=SW_SIZE):
    """画一个垂直断开开关符号（常开断路器右旋90° / circuit breaker open, vertical）"""
    box = Rectangle((x - size / 2, y - size / 2), size, size,
                    linewidth=BUS_LW, edgecolor='k', facecolor='white', zorder=4)
    ax.add_patch(box)
    d = size * 0.25
    ax.plot([x, x, x + size/2],
            [y + size/2, y + d, y - d],
            'k-', lw=BUS_LW, zorder=5, solid_joinstyle='round', solid_capstyle='round')
    ax.plot([x, x], [y - d, y - size/2],
            'k-', lw=BUS_LW, zorder=5)


def draw_substation_horizontal(ax, x, y, label):
    """画水平变电站符号（空心双竖线 + 方框）"""
    ax.plot([x - 0.12, x - 0.12], [y - 0.28, y + 0.28], 'k-', lw=NODE_LW)
    ax.plot([x + 0.12, x + 0.12], [y - 0.28, y + 0.28], 'k-', lw=NODE_LW)
    ax.plot([x - 0.12, x + 0.12], [y + 0.28, y + 0.28], 'k-', lw=NODE_LW)
    ax.plot([x - 0.12, x + 0.12], [y - 0.28, y - 0.28], 'k-', lw=NODE_LW)
    ax.text(x, y + 0.40, label, ha='center', va='bottom',
            fontsize=TEXT_FS, fontweight='bold')


def draw_substation_vertical(ax, x, y_bottom, y_top, label, width=0.20):
    """画垂直变电站符号（实心黑色长方形）

    Parameters
    ----------
    x : float
        中心 x 坐标
    y_bottom : float
        底部 y 坐标
    y_top : float
        顶部 y 坐标
    label : str
        标签文字
    width : float
        矩形宽度
    """
    rect = Rectangle((x - width / 2, y_bottom), width, y_top - y_bottom,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect)
    ax.text(x, y_top + 0.10, label, ha='center', va='bottom',
            fontsize=TEXT_FS, fontweight='bold')


def draw_bar_node(ax, x, y_top, y_bottom, width=0.10, label=None):
    """画实心黑色垂直长方形（母线节点基元）

    Parameters
    ----------
    x : float
        中心 x 坐标
    y_top : float
        顶部 y 坐标
    y_bottom : float
        底部 y 坐标
    width : float
        宽度（默认 0.10）
    label : str or None
        标签文字，None 则不标注
    """
    rect = Rectangle((x - width / 2, y_bottom), width, y_top - y_bottom,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect)
    if label is not None:
        ax.text(x, y_top + 0.10, label, ha='center', va='bottom',
                fontsize=TEXT_FS, fontweight='bold')


def draw_node(ax, x, y, label):
    """画负荷节点 / load node（母线引出编号 + 短竖线 + 矩形负荷框 + 向下箭头）"""
    ax.text(x, y + 0.18, str(label), ha='center', va='bottom',
            fontsize=TEXT_FS, fontweight='bold')
    ax.plot([x, x], [y, y - 0.12], 'k-', lw=NODE_LW)
    box = Rectangle((x - 0.09, y - 0.12), 0.18, 0.16,
                    linewidth=NODE_LW, edgecolor='k', facecolor='white', zorder=3)
    ax.add_patch(box)
    ax.annotate('', xy=(x, y - 0.48), xytext=(x, y - 0.28),
                arrowprops=dict(arrowstyle='->', lw=1.0, color='k'))


def draw_tf_node(ax, x, y, main_label, tf_label, dx=0.40):
    """画带配变的节点（普通节点 + 配变方框 + 标签 + 箭头）"""
    draw_node(ax, x, y, main_label)
    tx = x + dx
    ty = y - 0.65
    tf_box = Rectangle((tx - 0.13, ty - 0.13), 0.26, 0.26,
                       linewidth=NODE_LW, edgecolor='k', facecolor='white', zorder=3)
    ax.add_patch(tf_box)
    ax.plot([tx - 0.10, tx + 0.10], [ty + 0.05, ty + 0.05], 'k-', lw=0.8)
    ax.plot([tx - 0.10, tx + 0.10], [ty - 0.05, ty - 0.05], 'k-', lw=0.8)
    ax.plot([x, tx], [y - 0.12, ty + 0.13], 'k-', lw=0.9)
    ax.text(tx, ty - 0.38, str(tf_label), ha='center', va='top',
            fontsize=LABEL_FS, fontweight='bold')
    ax.annotate('', xy=(tx, ty - 0.60), xytext=(tx, ty - 0.26),
                arrowprops=dict(arrowstyle='->', lw=1.0, color='k'))


def draw_bar_node_switched(ax, x, y_bar, bar_width=0.44, label=None,
                           switch_y=None, input_len=0.12, output_len=0.12,
                           h_output_len=0.3, corner_frac=0.25, switch_frac=0.8,
                           label_fontsize=None):
    """画水平节点带开关模块（横形实心节点 + 左侧箭头 + 右侧竖形开关 + 出线）

    结构：
      ┌─ 序号（左上 1/4）
      │   ┌──────────────────┐
      │   │  横形实心节点     │───┐   ┌───┐
      ▼   └──────────────────┘   │   │ S │── 出线 ──
      左侧箭头                   │   │ W │
                              入线  └───┘

    Parameters
    ----------
    x : float
        节点中心 x 坐标
    y_bar : float
        横形节点中心 y 坐标
    bar_width : float
        横形节点宽度（默认 0.44 = 普通节点 2 倍）
    label : str or None
        节点序号
    switch_y : float or None
        竖形开关中心 y 坐标，None 则自动计算（y_bar - 0.215）
    input_len : float
        节点到开关入线长度（默认 0.12）
    output_len : float
        开关底部出线长度（默认 0.12）
    h_output_len : float
        水平出线长度（默认 0.3）
    corner_frac : float
        左侧拐角位置比例（默认 0.25）
    switch_frac : float
        右侧开关位置比例（默认 0.8）
    """
    BAR_H = 0.03
    bar_left = x - bar_width / 2
    bar_top = y_bar + BAR_H / 2
    bar_bot = y_bar - BAR_H / 2

    # 横形实心节点
    rect = Rectangle((bar_left, bar_bot), bar_width, BAR_H,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=3)
    ax.add_patch(rect)

    # 序号（左上 1/4 处）
    if label is not None:
        fs = label_fontsize if label_fontsize is not None else TEXT_FS
        ax.text(bar_left + bar_width * corner_frac, bar_top + 0.08, str(label),
                ha='center', va='bottom', fontsize=fs, fontweight='bold')

    # 左侧拐角 + 向下箭头
    corner_x = bar_left + bar_width * corner_frac
    corner_y = bar_bot
    dy, arr = 0.128, 0.05
    ax.plot([corner_x, corner_x], [corner_y, corner_y - dy], 'k-', lw=BUS_LW, zorder=5)
    tri = plt.Polygon([
        (corner_x, corner_y - dy - arr),
        (corner_x - arr * 0.4, corner_y - dy),
        (corner_x + arr * 0.4, corner_y - dy),
    ], closed=True, edgecolor='k', facecolor='k', lw=BUS_LW, zorder=5)
    ax.add_patch(tri)

    # 右侧竖形开关
    if switch_y is None:
        switch_y = y_bar - 0.215
    sw_x = bar_left + bar_width * switch_frac
    sw_top = switch_y + SW_SIZE / 2
    sw_bot = switch_y - SW_SIZE / 2

    # 入线：节点底部 → 开关顶部
    ax.plot([sw_x, sw_x], [bar_bot, sw_top], 'k-', lw=BUS_LW, zorder=5)
    # 竖形开关
    draw_switch_vertical(ax, sw_x, switch_y, SW_SIZE)
    # 出线：开关底部 → 垂直向下
    ax.plot([sw_x, sw_x], [sw_bot, sw_bot - output_len], 'k-', lw=BUS_LW, zorder=5)
    # 水平出线
    out_y = sw_bot - output_len
    ax.plot([sw_x, sw_x + h_output_len], [out_y, out_y], 'k-', lw=BUS_LW, zorder=5)


_SOLID_NODE_R = 0.04   # 实心圆点节点默认半径


def draw_solid_node(ax, x, y, r=_SOLID_NODE_R):
    """画实心圆点节点（母线连接点 / bus connection point）

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        圆心坐标
    r : float
        圆半径（默认 0.04）
    """
    nd = plt.Circle((x, y), r, edgecolor='k', facecolor='k', zorder=7)
    ax.add_patch(nd)


_DASH_ON = 1.5   # 虚线实线段长度
_DASH_OFF = 1.5  # 虚线空白段长度


def draw_feeder_extension(ax, x, y_start, y_end, lw=BUS_LW, dash_on=_DASH_ON,
                          dash_off=_DASH_OFF):
    """画一条垂直馈线延伸虚线，表示馈线向下游延伸/省略

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x : float
        虚线 x 坐标
    y_start : float
        虚线起点 y 坐标
    y_end : float
        虚线终点 y 坐标
    lw : float
        线宽（默认 BUS_LW）
    dash_on : float
        虚线实线段长度（默认 1.5）
    dash_off : float
        虚线空白段长度（默认 1.5）
    """
    ax.plot([x, x], [y_start, y_end],
            color='k', lw=lw, linestyle=(0, (dash_on, dash_off)), zorder=5)


def draw_feeder_extension_horizontal(ax, x_start, x_end, y, lw=BUS_LW,
                                     dash_on=_DASH_ON, dash_off=_DASH_OFF):
    """画一条水平馈线延伸虚线，表示馈线向下游延伸/省略

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x_start : float
        虚线起点 x 坐标
    x_end : float
        虚线终点 x 坐标
    y : float
        虚线 y 坐标
    lw : float
        线宽（默认 BUS_LW）
    dash_on : float
        虚线实线段长度（默认 1.5）
    dash_off : float
        虚线空白段长度（默认 1.5）
    """
    ax.plot([x_start, x_end], [y, y],
            color='k', lw=lw, linestyle=(0, (dash_on, dash_off)), zorder=5)


def draw_branch(ax, x, y, width, height):
    """画一个配电支路 / lateral branch（实心黑色垂直长方形），表示配电馈线的分支引出

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x : float
        支路中心 x 坐标
    y : float
        支路中心 y 坐标
    width : float
        支路宽度
    height : float
        支路高度
    """
    rect = Rectangle((x - width / 2, y - height / 2), width, height,
                     linewidth=0.5, edgecolor='k', facecolor='k', zorder=4)
    ax.add_patch(rect)


def draw_common_node_o(ax, x, y, bar_length=1.4, label=r'$o$ (source)'):
    """画公共节点 o（论文 Fig.4 源端/环路汇合点 / common node of the loop）

    来自 Baran & Wu (1989) Fig.4："the common node" 或 "node o"，
    是支路交换法中 L 侧和 R 侧路径在源端的汇合节点。

    结构：
          o (source)      ← 标签
            │             ← 短垂直线
       ─────┴─────        ← 水平横母线

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        标签位置（垂直线从 y 处开始）
    bar_length : float
        横母线总长度（默认 1.4）
    label : str
        节点标签文字（默认 r'$o$ (source)'）
    """
    bar_y = y - 0.2         # 横母线 y = 标签下方固定距离
    bar_l = x - bar_length / 2
    bar_r = x + bar_length / 2

    # 标签
    ax.text(x, y + 0.08, label,
            ha='center', va='bottom', fontsize=TEXT_FS,
            fontweight='bold', fontstyle='italic')
    # 垂直线
    ax.plot([x, x], [y, bar_y], 'k-', lw=BUS_LW, zorder=5)
    # 横母线
    ax.plot([bar_l, bar_r], [bar_y, bar_y], 'k-', lw=BUS_LW, zorder=5)


def draw_common_node_o_left(ax, x, y, bar_length=1.4, feeder_len=0.1,
                             label=None):
    """画左侧旋转 90° 的公共节点 o（去掉靠近 o 的竖线，保留 P 两条线）

    原始结构（仅去掉上方靠近 o 的竖线）：
          o (source)
       ─────┴─────
        ↑      ↑        ← 保留 P 两条线
       P_{ok} P_{on}

    左旋 90° 后：
                  ──→ P_{on}
                 │
       (label) ──┤  ← 竖母线（水平横线旋转而来）
                 │
                  ──→ P_{ok}     ← P 线变成水平短棒

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖母线中心坐标
    bar_length : float
        竖母线总长度（默认 1.4）
    feeder_len : float
        P 线水平短棒长度（默认 0.1）
    label : str or None
        标签文字（默认 None，不显示）
    """
    half = bar_length / 2
    q = bar_length * 0.25   # 四分之一处偏移
    off = 0.2               # o 标签向左偏移（对应原上竖线长度）

    # 竖母线（原水平横母线旋转 90° 得来）
    ax.plot([x, x], [y - half, y + half], 'k-', lw=BUS_LW, zorder=5)

    # 上方 P 线（原右馈线，现指向上方右侧）
    f_top_y = y + q
    ax.plot([x, x + feeder_len], [f_top_y, f_top_y], 'k-', lw=BUS_LW, zorder=5)

    # 下方 P 线（原左馈线，现指向下方右侧）
    f_bot_y = y - q
    ax.plot([x, x + feeder_len], [f_bot_y, f_bot_y], 'k-', lw=BUS_LW, zorder=5)

    # o 标签（可选，默认不显示）
    if label is not None:
        ax.text(x - off, y, label, ha='right', va='center',
                fontsize=11, fontweight='bold', fontstyle='italic')


def draw_node_i_minus_1(ax, x, y, bar_w=0.06, bar_h=0.7, label=r'$i\!-\!1$'):
    """画 Fig.3 风格的 i-1 节点（细长竖条 + 左拐角向下）

    结构：
         i-1 ──┬──   ← 标签 + 水平入线 + bar_node（黑色细长竖条）
               ┃
            ──┘       ← 左拐角（从竖条底部 1/4 处向左）
            │

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖条中心坐标
    bar_w : float
        竖条宽度（默认 0.06）
    bar_h : float
        竖条高度（默认 0.7，= 左竖节点 bar_length 的一半）
    label : str or None
        上方标签（默认 r'$i\!-\!1$'）
    """
    # 水平入线（从右侧来）
    ax.plot([x, x + bar_h * 0.7], [y, y], 'k-', lw=BUS_LW, zorder=5)
    # bar_node
    draw_bar_node(ax, x, y_top=y + bar_h / 2, y_bottom=y - bar_h / 2,
                  width=bar_w)
    # 标签在竖条顶部上方
    if label is not None:
        ax.text(x, y + bar_h / 2 + 0.06, label,
                ha='center', va='bottom', fontsize=TEXT_FS, fontweight='bold')
    # 左拐角：从竖条底部 1/4 处向左，再向下
    c_y = y - bar_h / 2 + bar_h * 0.25
    corner_x = x - bar_w / 2        # 左边缘
    dx, dy = bar_h * 0.14, bar_h * 0.29
    ax.plot([corner_x, corner_x - dx], [c_y, c_y],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([corner_x - dx, corner_x - dx],
            [c_y, c_y - dy], 'k-', lw=BUS_LW, zorder=5)
    # 虚线延长线（同 Fig.1 风格），延长至 3 段
    # 虚线延长线缩短 1/3（原 bar_h * 1.05 → bar_h * 0.7）
    ax.plot([corner_x - dx, corner_x - dx],
            [c_y - dy, c_y - dy - bar_h * 0.7],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)


def draw_node_k_minus_1(ax, x, y, next_x=None, bar_h=0.7, bar_w=0.06,
                         label=r'$k\!-\!1$', p_label=r'$P_{k-1}$',
                         k_label=r'$(k)$', draw_p=True, draw_k=True,
                         p_offset=0.10, arrow_len=0.47, pm_y=-0.98,
                         arrow_y_offset=-0.115):
    """画 k-1 子图：bare bar_node + (k) 标签 + P_{k-1} 箭头和标签

    结构：
              (k)
        ←────┃────→          ← 入线 · 竖条节点 · 出线
              └──→ P_{k-1}   ← 底部水平箭头和标签

    适用于 Fig.4 中虚线馈线延伸线后的 k-1 节点。

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖条节点中心坐标
    next_x : float or None
        下一个节点 (k) 的中心 x，用于放置 (k) 标签。
        None 则不绘制 (k) 标签。
    bar_h : float
        竖条高度（默认 0.7）
    bar_w : float
        竖条宽度（默认 0.06）
    label : str or None
        k-1 节点标签（默认 r'$k\\!-\\!1$'）
    p_label : str
        P 标签文字（默认 r'$P_{k-1}$'）
    k_label : str
        (k) 支路标签文字（默认 r'$(k)$'）
    draw_p : bool
        是否绘制 P_{k-1} 箭头和标签（默认 True）
    draw_k : bool
        是否绘制 (k) 标签（默认 True）
    p_offset : float
        P 箭头距节点右边缘的偏移（默认 0.10）
    arrow_len : float
        P 箭头长度（默认 0.47）
    pm_y : float
        P 标签 y 坐标（默认 -0.98，同 Pm）
    arrow_y_offset : float
        箭头 y 相对节点中心的偏移（默认 -0.115，同 Pm）
    """
    half = bar_h / 2
    bar_bot_y = y - half

    # ── 入线（从左侧来）──
    ax.plot([x - bar_h * 0.7, x], [y, y],
            'k-', lw=BUS_LW, zorder=5)

    # ── 竖条节点 ──
    draw_bar_node(ax, x, y_top=y + half, y_bottom=bar_bot_y,
                  width=bar_w)

    # ── 标签 ──
    if label is not None:
        ax.text(x, y + half + 0.06, label,
                ha='center', va='bottom', fontsize=TEXT_FS, fontweight='bold')

    # ── 右侧出线 ──
    ax.plot([x, x + bar_h * 0.7], [y, y],
            'k-', lw=BUS_LW, zorder=5)

    # ── (k) 标签（k-1 和 k 之间）──
    if draw_k and next_x is not None:
        ax.text((x + next_x) / 2, y + 0.15, k_label,
                ha='center', va='bottom', fontsize=18, fontstyle='italic')

    # ── P_{k-1} 箭头和标签 ──
    if draw_p:
        a_y = y + arrow_y_offset
        ax.annotate('', xy=(x + p_offset + arrow_len, a_y),
                    xytext=(x + p_offset, a_y),
                    arrowprops=dict(arrowstyle='->', lw=BUS_LW, color='k'))
        ax.text(x + p_offset - 0.02, pm_y, p_label,
                ha='left', va='top', fontsize=18, fontstyle='italic',
                color='#333333')


def draw_node_k(ax, x, y, bar_h=0.7, bar_w=0.06, label=r'$k$'):
    """画节点 k：竖条 + 左拐角 + 向下虚线，无右侧出线（L 侧末端节点）

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖条中心坐标
    bar_h : float
        竖条高度（默认 0.7）
    bar_w : float
        竖条宽度（默认 0.06）
    label : str or None
        节点标签（默认 r'$k$'）
    """
    half = bar_h / 2
    # bar_node
    draw_bar_node(ax, x, y_top=y + half, y_bottom=y - half, width=bar_w)
    # 标签
    if label is not None:
        ax.text(x, y + half + 0.06, label,
                ha='center', va='bottom', fontsize=TEXT_FS, fontweight='bold')
    # 左拐角：从竖条底部 1/4 处向左，再向下
    c_y = y - half + bar_h * 0.25
    corner_x = x - bar_w / 2
    dx, dy = bar_h * 0.14, bar_h * 0.29
    ax.plot([corner_x, corner_x - dx], [c_y, c_y],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([corner_x - dx, corner_x - dx],
            [c_y, c_y - dy], 'k-', lw=BUS_LW, zorder=5)
    # 虚线延长线
    ax.plot([corner_x - dx, corner_x - dx],
            [c_y - dy, c_y - dy - bar_h * 0.7],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)


def draw_node_n(ax, x, y, bar_h=0.7, bar_w=0.06, label=r'$n$'):
    """画节点 n：竖条 + 右拐角 + 向下虚线（拐角在右侧）

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖条中心坐标
    bar_h : float
        竖条高度（默认 0.7）
    bar_w : float
        竖条宽度（默认 0.06）
    label : str or None
        节点标签（默认 r'$n$'）
    """
    half = bar_h / 2
    # bar_node
    draw_bar_node(ax, x, y_top=y + half, y_bottom=y - half, width=bar_w)
    # 标签
    if label is not None:
        ax.text(x, y + half + 0.06, label,
                ha='center', va='bottom', fontsize=TEXT_FS, fontweight='bold')
    # 右拐角：从竖条底部 1/4 处向右，再向下
    c_y = y - half + bar_h * 0.25
    corner_x = x + bar_w / 2    # 右边缘
    dx, dy = bar_h * 0.14, bar_h * 0.29
    ax.plot([corner_x, corner_x + dx], [c_y, c_y],
            'k-', lw=BUS_LW, zorder=5)
    ax.plot([corner_x + dx, corner_x + dx],
            [c_y, c_y - dy], 'k-', lw=BUS_LW, zorder=5)
    # 虚线延长线
    ax.plot([corner_x + dx, corner_x + dx],
            [c_y - dy, c_y - dy - bar_h * 0.7],
            color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)


def draw_common_node_o_right(ax, x, y, bar_length=1.4, feeder_len=0.1,
                              label=None, corner=False, corner_h=0.7):
    """画右侧竖母线（与左侧对称，stubs 向左，可选右拐角）

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    x, y : float
        竖母线中心坐标
    bar_length : float
        竖母线总长度（默认 1.4）
    feeder_len : float
        stubs 水平短棒长度（默认 0.1）
    label : str or None
        标签文字（默认 None）
    corner : bool
        是否画右拐角 + 向下虚线（默认 False）
    corner_h : float
        拐角竖条高度（默认 0.7）
    """
    half = bar_length / 2
    q = bar_length * 0.25
    off = 0.2

    # 竖母线
    ax.plot([x, x], [y - half, y + half], 'k-', lw=BUS_LW, zorder=5)

    # 上方 stub：向左
    f_top_y = y + q
    ax.plot([x - feeder_len, x], [f_top_y, f_top_y], 'k-', lw=BUS_LW, zorder=5)

    # 下方 stub：向左
    f_bot_y = y - q
    ax.plot([x - feeder_len, x], [f_bot_y, f_bot_y], 'k-', lw=BUS_LW, zorder=5)

    # 右拐角（同 draw_node_n 风格）
    if corner:
        c_y = y - half + corner_h * 0.25
        dx, dy = corner_h * 0.14, corner_h * 0.29
        ax.plot([x, x + dx], [c_y, c_y], 'k-', lw=BUS_LW, zorder=5)
        ax.plot([x + dx, x + dx], [c_y, c_y - dy], 'k-', lw=BUS_LW, zorder=5)
        ax.plot([x + dx, x + dx],
                [c_y - dy, c_y - dy - corner_h * 0.7],
                color='k', lw=BUS_LW, linestyle=(0, (_DASH_ON, _DASH_OFF)), zorder=5)

    if label is not None:
        ax.text(x + off, y, label, ha='left', va='center',
                fontsize=11, fontweight='bold', fontstyle='italic')