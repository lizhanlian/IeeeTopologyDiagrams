# IeeeTopologyDiagrams

**Author: 黎湛联 (Zhanlian Li)**

电力系统**配电网络单线图**（One-Line Diagram / Single-Line Diagram）绘图库，基于 IEEE 33-Bus 标准测试系统。

实现 Baran & Wu (1989) 提出的配电网络重构经典算例的拓扑可视化，涵盖**变电站**（Substation）、**母线**（Bus）、**断路器**（Circuit Breaker, CB）、**配电馈线**（Distribution Feeder）、**支路功率流**（Branch Power Flow）及**负荷注入**（Load Injection）等电力系统标准图元。

每个绘图脚本头部包含**完整参数字段表 + 中英文绘制步骤**，可独立运行或作为 AI 提示词独立复现同样的拓扑图。

出处：M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery, Vol. 4, No. 2, pp. 1401-1407, 1989.

## 安装

```bash
pip install IeeeTopologyDiagrams
```

## 电力系统绘图基元 (Drawing Primitives)

### 开关设备 / Switchgear

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_switch(ax, x, y, size)` | 水平闭合开关 | 常闭断路器 (Normally-Closed Circuit Breaker, NCB) — 方框内水平贯穿线 |
| `draw_switch_vertical(ax, x, y, size)` | 垂直闭合开关 | 常闭断路器竖直方向 — 方框内竖直贯穿线 |
| `draw_switch_open(ax, x, y, size)` | 水平断开开关 | 常开断路器 (Normally-Open Circuit Breaker, NOCB) — 方框内斜线断开 |
| `draw_switch_open_vertical(ax, x, y, size)` | 垂直断开开关 | 常开断路器竖直方向 — 方框内斜线断开 |

### 变电站 / Substations

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_substation_vertical(ax, x, y_bottom, y_top, ...)` | SS1 (垂直) | 配电变电站 (Distribution Substation) — 实心黑色矩形 |
| `draw_substation_horizontal(ax, x, y, label)` | SS2 (水平) | 配电变电站 — 空心双竖线 + 矩形框 |

### 母线节点 / Bus Nodes

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_bar_node(ax, x, y_top, y_bottom, width, label)` | 实心竖条 | 母线节点 (Bus Bar Node) — 实心黑色垂直矩形 |
| `draw_bar_node_switched(ax, x, y_bar, ...)` | 横条 + 开关 | 水平母线节点带竖直开关模块 — 含拐角出线和负荷箭头 |
| `draw_solid_node(ax, x, y, r)` | 实心圆点 | 母线连接点 (Bus Connection Point) — 实心黑色圆点，半径 0.04 |
| `draw_branch(ax, x, y, width, height)` | 实心竖矩形 | 配电支路 / 配电侧馈线引出 (Lateral Branch) |

### 环路节点 / Loop Nodes (Figure 4)

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_node_i_minus_1(ax, x, y, ...)` | 竖条 + 左拐角 + 虚线 | i-1 节点 — 含左出线拐角和向下虚线延伸 |
| `draw_node_k_minus_1(ax, x, y, next_x, ...)` | 裸竖条 + Pk-1 箭头 | k-1 节点子图 — 含 (k) 支路标签和 Pk-1 功率箭头 |
| `draw_node_k(ax, x, y, ...)` | 竖条 + 左拐角 + 虚线 | k 节点 — L侧末端，无右侧出线，含 Pk 垂直箭头 |
| `draw_node_n(ax, x, y, ...)` | 竖条 + 右拐角 + 虚线 | n 节点 — 含右出线拐角和 ΔPn 水平箭头 |
| `draw_common_node_o(ax, x, y, ...)` | 横母线 + 垂线 | 公共节点 0 — 图4顶部节点 |
| `draw_common_node_o_left(ax, x, y, ...)` | 左侧竖母线 | 左侧竖母线 — stubs 向右 |
| `draw_common_node_o_right(ax, x, y, corner, ...)` | 右侧竖母线 | 右侧竖母线 — stubs 向左，可选右拐角 |

### 功率标注 / Power Flow Labels (Figure 4)

| 标签 | 箭头方向 | 说明 |
|------|:---:|------|
| Pm | → 水平向右 | 左竖母线到 i-1 的功率流 |
| Pk-1 | → 水平向右 | k-1 节点的功率注入 |
| Pk | ↓ 垂直向下 | k 节点竖线正下方的功率 |
| ΔPn | ← 水平向左 | n 节点左侧的功率变化 |
| Pio | ↓ 垂直向下 | 右竖母线拐角虚线末端下方的功率 |
| Pok | 斜向 | 顶部 node 0 左斜线功率流 |
| Pon | 斜向 | 顶部 node 0 右斜线功率流 |

### 负荷与变压器 / Load & Transformer

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_node(ax, x, y, label)` | 负荷节点 | 含编号 + 短竖线 + 空心负荷框 + 向下箭头 |
| `draw_tf_node(ax, x, y, main_label, tf_label, dx)` | 配变节点 | 配电变压器节点 (Distribution Transformer Node) — 含变压器绕组符号 |

### 馈线延伸 / Feeder Extension

| 函数 | 电力符号 | 学术说明 |
|------|:---:|------|
| `draw_feeder_extension(ax, x, y_start, y_end, ...)` | 垂直虚线 | 垂直馈线延伸虚线 (Vertical Feeder Extension) — 表示下游省略 |
| `draw_feeder_extension_horizontal(ax, x_start, x_end, y, ...)` | 水平虚线 | 水平馈线延伸虚线 — 表示横向下游省略 |

## 样式常量

| 常量 | 值 | 学术含义 |
|------|----|------|
| `BUS_LW` | 2.2 | 母线 / 馈线线宽 (Bus Line Width) |
| `NODE_LW` | 1.1 | 节点 / 开关边框线宽 (Node Line Width) |
| `TEXT_FS` | 20 | 节点编号字号 (Node Label Font Size) |
| `LABEL_FS` | 18 | 设备标签字号 (Equipment Label Font Size) |
| `TITLE_FS` | 22 | 图标题字号 (Figure Title Font Size) |
| `SW_SIZE` | 0.18 | 断路器 (CB) 符号尺寸 (Switch Symbol Size) |
| `_DASH_ON` | 1.5 | 虚线绘制长度 (Dash On Length) |
| `_DASH_OFF` | 1.5 | 虚线间隔长度 (Dash Off Length) |

## 使用示例

```python
import matplotlib.pyplot as plt
from IeeeTopologyDiagrams import (
    draw_switch, draw_solid_node,
    draw_substation_vertical,
    draw_feeder_extension,
    BUS_LW, SW_SIZE,
)

fig, ax = plt.subplots(figsize=(5, 3))
# 配电变电站 SS1
draw_substation_vertical(ax, x=0, y_bottom=-0.9, y_top=0, label='SS1')
# 常闭断路器 CB1
draw_switch(ax, x=0.5, y=-0.225, SW_SIZE)
# 母线连接点
draw_solid_node(ax, x=1.0, y=-0.225)
# 馈线延伸（表示下游省略）
draw_feeder_extension(ax, x=1.0, y_start=-0.5, y_end=-0.8)

ax.set_aspect('equal'); ax.axis('off')
plt.savefig('output.png', dpi=200, bbox_inches='tight')
```

## 绘图脚本 (`drawingScripts/`)

每个脚本文件头部包含完整参数字段表 + 中英文绘制步骤，可直接作为 AI 提示词复现。

### 完整单线图 (One-Line Diagrams)

| 脚本 | 输出 | 学术说明 |
|------|------|------|
| `reproduce_fig1.py` | Figure 1 | 配电系统一次回路原理图 (Primary Circuit Schematic) — SS1 + CB1 + 辐射状馈线节点 |
| `reproduce_fig2.py` | Figure 2 | 小型配电系统单线图 (IEEE 33-Bus System) — 含 SS1/SS2、CB/cb、联络开关、左/右出线负荷节点 |
| `reproduce_fig3.py` | Figure 3 | 辐射状网络支路功率流图 (Radial Network Branch Power Flow) — 支路有功功率 P 和无功功率 Q 的向量标注 |
| `reproduce_fig3_from_steps.py` | — | Fig3 的纯步骤提示文件（无代码实现，供 AI 复现验证用） |
| `reproduce_fig4.py` | Figure 4 | 环路关联常开支路 b 的示意图 (Loop with Open Branch b) — 完整的 L侧/R侧路径、节点标注、功率箭头 |

### 负荷节点 / Load Node（左/右出线）

采用 **实心母线节点 + 直角拐角 + 向下箭头** 的负荷注入表示：

| 脚本 | 出线 | 输出 | 关键参数 |
|------|:--:|------|------|
| `save_load_node_left.py` | ← 左 | `load_node_left.png` | BAR_H=0.44, BAR_W=0.03, DX=0.06, DY=0.128 |
| `save_load_node_right.py` | → 右 | `load_node_right.png` | 同左出线，仅拐角方向相反 |

### 母线节点基元 / Bus Bar Primitives

| 脚本 | 输出 | 关键参数 |
|------|------|------|
| `save_bar_node_short.py` | 竖形母线节点（左出线） | H=0.6, W=0.08, DX=0.16, DY=0.35 |
| `save_bar_node_horizontal.py` | 横形母线节点（下出线） | W=0.55, H=0.03, DY=0.128 |

### 断路器符号 / Circuit Breakers

| 脚本 | 输出 | 状态 | 关键参数 |
|------|------|:--:|------|
| `save_switch_symbol.py` | 水平 CB（常闭） | NCB | SW_SIZE=0.18 |
| `save_switch_vertical.py` | 垂直 CB（常闭） | NCB | SW_SIZE=0.18 |
| `save_switch_open_h.py` | 水平 CB（常开） | NOCB | SW_SIZE=0.18 |
| `save_switch_open_v.py` | 垂直 CB（常开） | NOCB | SW_SIZE=0.18 |
| `save_switch_open.py` | 开/闭对比（水平+垂直） | NCB + NOCB | 四合一对比图 |

### 变电站 / Distribution Substations

| 脚本 | 输出 | 符号形式 | 关键参数 |
|------|------|------|------|
| `save_ss1_symbol.py` | SS1 | 实心黑色垂直矩形 | W=0.10, H=1.40 |
| `save_ss2_symbol.py` | SS2 | 空心双竖线 + 方框 | 双竖线间距 0.12, 框高 0.56 |

### 其他电力元件 / Miscellaneous Components

| 脚本 | 输出 | 学术说明 | 关键参数 |
|------|------|------|------|
| `save_solid_node.py` | 母线连接点 | Bus Connection Point — 实心圆点 | R=0.04 |
| `save_branch.py` | 配电支路 | Lateral Branch / 侧馈线引出 | W=0.0375, H=0.28125 |
| `save_tf_node.py` | 配变节点 | Distribution Transformer Node — 变压器绕组符号 | DX=0.40, 变压器方框 0.26 |
| `save_node15.py` | 水平节点 + 竖形 CB | Bar Node with Vertical Switch Module | BAR_W=0.44, SW_SIZE=0.18 |

## 学术术语速查 / Glossary

| 中文 | English | 缩写 |
|------|------|:--:|
| 单线图 | One-Line Diagram / Single-Line Diagram | SLD |
| 变电站 | Substation | SS |
| 断路器 | Circuit Breaker | CB |
| 常闭断路器 | Normally-Closed CB | NCB |
| 常开断路器 / 联络开关 | Normally-Open CB / Tie Switch | NOCB |
| 母线 | Bus / Bus Bar | — |
| 配电馈线 | Distribution Feeder | — |
| 辐射状网络 | Radial Network | — |
| 支路功率流 | Branch Power Flow | — |
| 有功功率 | Active Power | P |
| 无功功率 | Reactive Power | Q |
| 负荷注入 | Load Injection | P_L, Q_L |
| 配电变压器 | Distribution Transformer | TF |
| 侧馈线 / 支路 | Lateral Branch | — |
| 母线连接点 | Bus Connection Point | — |

## 许可

参考库内源文件头部的引用信息。
