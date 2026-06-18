"""
IEEE 33-Bus 单线图绘图库
Author: 黎湛联 (Zhanlian Li)

提供 IEEE 33-Bus 配电系统的单线图绘图基元和坐标定义，
基于 Baran.1989 Figure 1-4 的布局。

Ver 4.0.6: 新增 Figure 4 (环路关联常开支路b) + 所有图原文出处引用 + 字号翻倍

使用示例：
    from IeeeTopologyDiagrams import (
        drawing_elements, coordinates,
        Y_TOP, Y_MID, Y_BOT, X_SS1, X_SW,
        draw_switch, draw_node, draw_substation_vertical,
    )

    fig, ax = plt.subplots(figsize=FIG_SIZE)
    draw_substation_vertical(ax, X_SS1, Y_MID, Y_TOP, 'SS1')
    draw_switch(ax, X_SW, Y_SW_TOP)
"""

from .drawing_elements import (
    BUS_LW, NODE_LW, TEXT_FS, LABEL_FS, TITLE_FS, SW_SIZE,
    _DASH_ON, _DASH_OFF,
    draw_switch,
    draw_switch_vertical,
    draw_switch_open,
    draw_switch_open_vertical,
    draw_substation_horizontal,
    draw_substation_vertical,
    draw_bar_node,
    draw_bar_node_switched,
    draw_node,
    draw_tf_node,
    draw_solid_node,
    draw_feeder_extension,
    draw_feeder_extension_horizontal,
    draw_branch,
    draw_common_node_o,
    draw_common_node_o_left,
    draw_common_node_o_right,
    draw_node_i_minus_1,
    draw_node_k_minus_1,
    draw_node_k,
    draw_node_n,
)

from .coordinates import (
    Y_TOP, Y_MID, Y_BOT,
    X_SS1, SS_WIDTH,
    Y_SW_TOP, Y_SW_MID,
    X_SW,
    x_top, X_TOP_END,
    x_mid, X_SS2, X_MID_END,
    x_bot, X_BOT_END,
    X_NODE15,
    XLIM, YLIM, FIG_SIZE,
)

__all__ = [
    'BUS_LW', 'NODE_LW', 'TEXT_FS', 'LABEL_FS', 'TITLE_FS', 'SW_SIZE',
    '_DASH_ON', '_DASH_OFF',
    'draw_switch', 'draw_switch_vertical', 'draw_switch_open', 'draw_switch_open_vertical', 'draw_substation_horizontal', 'draw_substation_vertical',
    'draw_bar_node', 'draw_bar_node_switched', 'draw_node', 'draw_tf_node', 'draw_solid_node',
    'draw_feeder_extension', 'draw_feeder_extension_horizontal', 'draw_branch',
    'draw_common_node_o', 'draw_common_node_o_left', 'draw_common_node_o_right',
    'draw_node_i_minus_1', 'draw_node_k_minus_1', 'draw_node_k', 'draw_node_n',
    'Y_TOP', 'Y_MID', 'Y_BOT',
    'X_SS1', 'SS_WIDTH', 'Y_SW_TOP', 'Y_SW_MID', 'X_SW',
    'x_top', 'X_TOP_END',
    'x_mid', 'X_SS2', 'X_MID_END',
    'x_bot', 'X_BOT_END',
    'X_NODE15',
    'XLIM', 'YLIM', 'FIG_SIZE',
    'cli',
]