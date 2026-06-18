<div align="center">

# IeeeTopologyDiagrams

> IEEE 33 节点配电网络单线图绘制基元 · IEEE 33-Bus Distribution System Single-Line Diagram Drawing Primitives

[![PyPI version](https://badge.fury.io/py/IeeeTopologyDiagrams.svg)](https://badge.fury.io/py/IeeeTopologyDiagrams)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://pypi.org/project/IeeeTopologyDiagrams/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Power System](https://img.shields.io/badge/Domain-Power%20System-green)](https://en.wikipedia.org/wiki/Distribution_network_reconfiguration)
[![AI Reproducible](https://img.shields.io/badge/AI-Reproducible-blueviolet)](https://github.com/trae-ai)

<br>

**IEEE 33 节点拓扑图可复现实例 — 基于 Baran & Wu (1989) 经典配电网络重构算例，提供完整的绘图函数和参数说明。**

<sub>IEEE 33 节点系统（33-bus distribution system）是配电网络重构、无功优化、分布式电源接入、故障定位等研究中最常用的基准算例。本项目提供 IEEE 33 节点单线图、IEEE 33 节点拓扑图、以及 Baran & Wu 论文原始四幅图的可复现绘制工具。</sub>

<br>

[简介](#简介) · [安装](#安装) · [功能特性](#功能特性) · [IEEE 33 节点拓扑图](#ieee-33-节点拓扑图) · [绘图基元](#绘图基元) · [命令行工具](#命令行工具) · [参考文献](#参考文献)

</div>

---

## 简介

**IEEE 33 节点配电系统**（IEEE 33-bus distribution system）是配电网络重构、无功优化、分布式电源规划、故障定位与隔离、微电网运行等研究领域中广泛使用的基准算例。

本项目实现 Baran & Wu (1989) 论文提出的 IEEE 33 节点拓扑图可复现绘制，涵盖**变电站**（Substation）、**母线**（Bus）、**断路器**（Circuit Breaker, CB）、**配电馈线**（Distribution Feeder）、**支路功率流**（Branch Power Flow）及**负荷注入**（Load Injection）等电力系统标准图元。

每个绘图脚本头部包含**完整参数字典 + 中英文分步绘制说明**，任何人或 AI 都可以按照步骤精确复现 IEEE 33 节点拓扑图、IEEE 33 节点单线图，以及 Baran & Wu 原始论文的 Figure 1–Figure 4。

> M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery, Vol. 4, No. 2, pp. 1401-1407, 1989.

**适用研究方向：** 配电网络重构、无功优化、分布式发电接入、配电网可靠性评估、微电网优化、配电网故障恢复、三相潮流分析。

---

## 安装

```bash
pip install IeeeTopologyDiagrams
```

---

## 功能特性

| 类别 | 功能 | 状态 |
|------|------|:----:|
| **开关设备** | 常闭/常开断路器（水平/垂直） | ✅ |
| **变电站** | 实心矩形 / 空心双线两种样式 | ✅ |
| **母线节点** | 竖母线 / 横母线 / 带开关模块 / 连接点 | ✅ |
| **负荷变压器** | 负荷节点注入 / 配电变压器符号 | ✅ |
| **环路功率标注** | Figure 4 完整 P/ΔP 箭头标注系统 | ✅ |
| **原始图复现** | Baran.1989 四幅原图完整复现 | ✅ |
| **AI Skill 框架** | Trae IDE 技能扩展，支持一键复现 | ✅ |
| **命令行导出** | CLI 一键导出单个符号 / 完整图形 | ✅ |

---

## 📦 IEEE 33 节点拓扑图

**IEEE 33 节点系统参数**（IEEE 33-bus distribution test system）：

| 参数 | 数值 |
|------|------|
| 基准电压 | 12.66 kV |
| 节点数 | 33（含变电站节点 0）|
| 支路数 | 37（32 条工作支路 + 5 条联络线 tie-line）|
| 常开开关（联络线）| 支路 33, 34, 35, 36, 37 |
| 总负荷 | 3.715 MW + j2.300 MVar |
| 有功网损（初始辐射状）| ≈ 202.67 kW |
| 最低电压节点 | Bus 18, ≈ 0.9131 p.u. |

**IEEE 33 节点拓扑结构：**

* **馈线 1：** SS1 → Bus 1 → Bus 2 → ... → Bus 17
* **馈线 2：** SS2 → Bus 18 → Bus 19 → ... → Bus 32
* **联络线：** Bus 8–Bus 21、Bus 9–Bus 15、Bus 12–Bus 22、Bus 18–Bus 33、Bus 25–Bus 29
* **运行方式：** 常开 5 个联络开关，呈辐射状运行；重构时通过开关切换寻找最小网损拓扑

使用一行命令安装并生成 IEEE 33 节点拓扑图：

```bash
pip install IeeeTopologyDiagrams
python -c "from IeeeTopologyDiagrams.reproduce_fig2 import draw_ieee33bus_diagram; draw_ieee33bus_diagram('ieee33.png')"
```

**在 Python 中调用并定制：**

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

ax.set_aspect('equal')
ax.axis('off')
plt.savefig('output.png', dpi=200, bbox_inches='tight')
plt.show()
```

---

## 绘图基元

### 🔹 开关设备 (Switchgear)

| 函数 | 方向 | 状态 | 说明 |
|------|:----:|:----:|------|
| `draw_switch()` | 水平 | 常闭 | Normally-Closed Circuit Breaker (NCB) |
| `draw_switch_vertical()` | 垂直 | 常闭 | Normally-Closed Circuit Breaker (NCB) |
| `draw_switch_open()` | 水平 | 常开 | Normally-Open Circuit Breaker (NOCB) / Tie Switch |
| `draw_switch_open_vertical()` | 垂直 | 常开 | Normally-Open Circuit Breaker (NOCB) / Tie Switch |

### 🔹 变电站 (Substations)

| 函数 | 样式 | 说明 |
|------|------|------|
| `draw_substation_vertical()` | 实心矩形 | 配电变电站 SS1 |
| `draw_substation_horizontal()` | 空心双竖线 | 配电变电站 SS2 |

### 🔹 母线节点 (Bus Nodes)

| 函数 | 说明 |
|------|------|
| `draw_bar_node()` | 竖直母线节点 |
| `draw_bar_node_switched()` | 水平母线带竖直开关模块 |
| `draw_solid_node()` | 实心圆点连接点 |
| `draw_branch()` | 侧馈引出支路 |

### 🔹 环路节点 (Loop Nodes - Figure 4)

| 函数 | 说明 |
|------|------|
| `draw_node_i_minus_1()` | i-1 节点，左拐角 + 虚线延伸 |
| `draw_node_k_minus_1()` | k-1 节点，Pk-1 功率箭头 |
| `draw_node_k()` | k 节点（L侧末端），Pk 垂直箭头 |
| `draw_node_n()` | n 节点，ΔPn 水平箭头 |
| `draw_common_node_o()` | 环路顶部公共节点 0 |

### 🔹 负荷与变压器 (Load & Transformer)

| 函数 | 说明 |
|------|------|
| `draw_load_node()` | 负荷节点，标号 + 虚线框 + 向下箭头 |
| `draw_tf_node()` | 配电变压器，含绕组符号 |

### 📐 样式常量

| 常量 | 值 | 含义 |
|------|-----|------|
| `BUS_LW` | 2.2 | 母线/馈线线宽 |
| `NODE_LW` | 1.1 | 节点/开关边框线宽 |
| `TEXT_FS` | 20 | 节点编号字号 |
| `LABEL_FS` | 18 | 设备标签字号 |
| `SW_SIZE` | 0.18 | 断路器符号尺寸 |

---

## 🖼️ 完整示意图（IEEE 33 节点系统）

本项目可复现 Baran & Wu (1989) 论文的全部四幅关键图，包括 **IEEE 33 节点单线图**、**IEEE 33 节点拓扑图**、以及论文原始的 Figure 1–Figure 4。

运行 `python generate_figures.py` 即可重新生成所有图像，输出到 `assets/` 目录。

---

### Figure 1 — 配电系统一次回路示意图（IEEE 33 节点拓扑来源）

> *Schematic diagram of a simplified primary circuit of a distribution system together with sectionalizing switches.*

| 组件 | 内容 |
|------|------|
| 变电站 | SS1（实心矩形）、SS2（空心双线）|
| 分段开关 | CB1–CB6（常闭，实心黑色）|
| 联络开关 | CB7（馈线-馈线联络）、CB8（变电站-变电站联络）、CB9（环型侧馈线），常开 |
| 负荷点 | "·" 标记，表示配电变压器抽头位置 |

![Figure 1 — 一次回路原理图](assets/fig1.png)

---

### Figure 2 — IEEE 33 节点完整配电系统单线图

> *IEEE 33-bus distribution system one-line diagram: equivalent network derived from Figure 1 with solid branches in service, dotted branches representing lines with open switches. 32 load buses, 37 branches, 5 tie-lines.*

| 组件 | 内容 |
|------|------|
| 规模 | 2 个变电站 + 32 个负荷节点 + 37 条支路 |
| 联络线 | 5 条常开 tie-line（支路 33–37）|
| 开关 | CB1–CB5（常闭分段），cb21–cb22（常开联络）|
| 应用 | 配电网络重构、无功优化、分布式电源接入研究的基准算例 |

![Figure 2 — IEEE 33 节点单线图](assets/fig2.png)

---

### Figure 3 — IEEE 33 节点辐射网络 P/Q 功率流标注

> *Power flow in a radial distribution network described by recursive DistFlow branch equations. Active power P, reactive power Q, node voltage V.*

| 组件 | 内容 |
|------|------|
| 支路方程 | DistFlow — 由发送端 P, Q, V 递推接收端 |
| 标注方式 | 沿馈线水平标注 P, Q；负荷节点 P_L, Q_L 向下注入 |
| 馈线延伸 | 虚线部分表示下游省略的支路 |

![Figure 3 — 辐射网络功率流](assets/fig3.png)

---

### Figure 4 — IEEE 33 节点带开分支 b 的环路示意图

> *A loop associated with open branch b. Branch exchange creates a new tree by closing an open branch b and by opening a closed branch m in the loop.*

| 组件 | 内容 |
|------|------|
| 公共源节点 | o (source) |
| L-side | o → 节点 i−1 → 节点 k−1 → 节点 k |
| R-side | o → … → 节点 n−1 → 节点 n |
| 开分支 b | k 与 n 之间的虚线（联络线）|
| 功率标注 | Pok（L-side 发送功率）、Pon（R-side 发送功率）、Pk、ΔPn |

![Figure 4 — 环路示意图](assets/fig4.png)

---

## 🔧 命令行工具

包安装后自带 CLI 命令可直接导出符号：

```bash
# 导出完整图形
IeeeTopologyDiagrams-fig1   # 导出 Figure 1
IeeeTopologyDiagrams-fig2   # 导出 Figure 2
IeeeTopologyDiagrams-fig3   # 导出 Figure 3
IeeeTopologyDiagrams-fig4   # 导出 Figure 4
IeeeTopologyDiagrams-cb1cb2 # 导出 CB1/CB2 示例

# 导出单个符号
IeeeTopologyDiagrams-switch          # 水平常闭断路器
IeeeTopologyDiagrams-switch-vertical # 竖正常闭断路器
IeeeTopologyDiagrams-switch-open-h   # 水平常开断路器
IeeeTopologyDiagrams-switch-open-v   # 竖正常开断路器
IeeeTopologyDiagrams-ss1             # 变电站 SS1
IeeeTopologyDiagrams-ss2             # 变电站 SS2
IeeeTopologyDiagrams-solid-node      # 实心连接点
IeeeTopologyDiagrams-load-node       # 负荷节点
```

---

## 🧩 术语对照表（IEEE 33 节点配电系统）

| 中文 | English | 缩写 / 备注 |
|------|---------|--------------|
| IEEE 33 节点系统 | IEEE 33-bus distribution test system | 经典配电网络重构基准算例 |
| IEEE 33 节点单线图 | One-line diagram of IEEE 33-bus system | IEEE 33 节点拓扑图 |
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
| 联络线 / 开分支 | Tie-line / Open branch | 支路 33-37 |
| 配电网络重构 | Distribution Network Reconfiguration | Baran & Wu, 1989 |
| 网损 | Power Loss | kW |
| 节点电压 | Bus Voltage | p.u. (per unit) |

---

## 🛠️ AI Skill 扩展

本项目内置 Trae IDE 技能框架，支持一键复现原始论文图形：

- [baran-wu-figures](./IeeeTopologyDiagrams/skills/baran-wu-figures/README_skill.md) - Reproduce original figures from Baran & Wu (1989)

---

## 关于作者

**黎湛联 (Zhanlian Li)**

| 平台 | 链接 |
|------|------|
| 🌐 GitHub | [github.com/lizhanlian](https://github.com/lizhanlian) |
| 📦 PyPI | [IeeeTopologyDiagrams](https://pypi.org/project/IeeeTopologyDiagrams/) |
| 💬 公众号 | 微信搜「湛联说」|
| 🏫 研究方向 | 电力系统 / 配电网络重构 / IEEE 33-Bus |

<img src="assets/wechat-banner.png" alt="湛联说公众号" width="480">

## 许可证

MIT — 随便用，随便改，随便造。

---

## 参考文献

1. Baran, M. E., & Wu, F. F. (1989). Network reconfiguration in distribution systems for loss reduction and load balancing. *IEEE Transactions on Power Delivery*, 4(2), 1401-1407.

---

<div align="center">

**IEEE 33-Bus 拓扑可复现绘图基元**<br>
让学术论文插图复现变得简单。

<br>

MIT License © 黎湛联 (Zhanlian Li)

</div>