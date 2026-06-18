# IeeeTopologyDiagrams

> IEEE 33-Bus Distribution System Single-Line Diagram Drawing Primitives

<div align="center">

[![PyPI version](https://badge.fury.io/py/IeeeTopologyDiagrams.svg)](https://badge.fury.io/py/IeeeTopologyDiagrams)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://pypi.org/project/IeeeTopologyDiagrams/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 📖 Overview

电力系统**配电网络单线图**（One-Line Diagram / Single-Line Diagram）绘图库，基于 IEEE 33-Bus 标准测试系统。

实现 Baran & Wu (1989) 提出的配电网络重构经典算例的拓扑可视化，涵盖**变电站**（Substation）、**母线**（Bus）、**断路器**（Circuit Breaker, CB）、**配电馈线**（Distribution Feeder）、**支路功率流**（Branch Power Flow）及**负荷注入**（Load Injection）等电力系统标准图元。

每个绘图脚本头部包含**完整参数字段表 + 中英文绘制步骤**，可独立运行或作为 AI 提示词独立复现同样的拓扑图。

## 📚 Citation

> M.E. Baran, F.F. Wu, "Network Reconfiguration in Distribution Systems for Loss Reduction and Load Balancing," IEEE Trans. Power Delivery, Vol. 4, No. 2, pp. 1401-1407, 1989.

## 🚀 Installation

```bash
pip install IeeeTopologyDiagrams
```

## 🎯 Features

| Category | Primitives | Status |
|----------|------------|--------|
| **Switchgear** | NCB/NOCB (horizontal/vertical) | ✅ |
| **Substations** | Solid rectangle / double-line | ✅ |
| **Bus Nodes** | Bar node / solid point / switched module | ✅ |
| **Load & Transformer** | Load injection / distribution transformer | ✅ |
| **Power Flow Labels** | P/Q arrows for loop analysis (Fig 4) | ✅ |
| **Reproducible Examples** | Full figures from Baran.1989 | ✅ |
| **Skill Extensions** | AI-assisted reproduction framework | ✅ |

## 📦 Quick Start

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

## 🎨 Drawing Primitives

### 🔹 Switchgear

| Function | Orientation | State | Description |
|----------|:-----------:|:-----:|-------------|
| `draw_switch()` | horizontal | NCB | Normally-Closed Circuit Breaker |
| `draw_switch_vertical()` | vertical | NCB | Normally-Closed Circuit Breaker |
| `draw_switch_open()` | horizontal | NOCB | Normally-Open Circuit Breaker |
| `draw_switch_open_vertical()` | vertical | NOCB | Normally-Open Circuit Breaker |

### 🔹 Substations

| Function | Style | Description |
|----------|-------|-------------|
| `draw_substation_vertical()` | solid rectangle | Distribution Substation SS1 |
| `draw_substation_horizontal()` | double vertical lines | Distribution Substation SS2 |

### 🔹 Bus Nodes

| Function | Description |
|----------|-------------|
| `draw_bar_node()` | Vertical bus bar node |
| `draw_bar_node_switched()` | Horizontal bus with vertical switch module |
| `draw_solid_node()` | Solid circle connection point |
| `draw_branch()` | Lateral branch / feeder stub |

### 🔹 Loop Nodes (Figure 4)

For the loop representation with open branch b:

| Function | Description |
|----------|-------------|
| `draw_node_i_minus_1()` | Node i-1 with left corner & dashed extension |
| `draw_node_k_minus_1()` | Node k-1 with Pk-1 power arrow |
| `draw_node_k()` | Node k (end of L-side) with Pk vertical arrow |
| `draw_node_n()` | Node n with ΔPn horizontal arrow |
| `draw_common_node_o()` | Common node 0 at loop top |
| `draw_common_node_o_left()` | Left vertical bus for loop |
| `draw_common_node_o_right()` | Right vertical bus for loop |

### 🔹 Load & Transformer

| Function | Description |
|----------|-------------|
| `draw_load_node()` | Load node with label, dashed box & downward arrow |
| `draw_tf_node()` | Distribution transformer node with winding symbol |

## 📐 Style Constants

| Constant | Value | Meaning |
|----------|-------|---------|
| `BUS_LW` | 2.2 | Bus/Feeder line width |
| `NODE_LW` | 1.1 | Node/Switch border line width |
| `TEXT_FS` | 20 | Node label font size |
| `LABEL_FS` | 18 | Equipment label font size |
| `TITLE_FS` | 22 | Figure title font size |
| `SW_SIZE` | 0.18 | Circuit breaker symbol size |

## 📜 Examples

| Script | Figure | Description |
|--------|--------|-------------|
| `reproduce_fig1.py` | Fig 1 | Primary circuit schematic |
| `reproduce_fig2.py` | Fig 2 | IEEE 33-Bus full system one-line diagram |
| `reproduce_fig3.py` | Fig 3 | Radial network with P/Q power flow labeling |
| `reproduce_fig4.py` | Fig 4 | Loop with open branch b (delta P notation) |

Each script includes complete parameter tables and step-by-step instructions at the top, can be used directly as AI prompts for reproduction.

## 🔧 Command Line Tools

The package installs several CLI commands for exporting symbols:

```bash
# Export full figures
IeeeTopologyDiagrams-fig1   # export Figure 1
IeeeTopologyDiagrams-fig2   # export Figure 2
IeeeTopologyDiagrams-fig3   # export Figure 3
IeeeTopologyDiagrams-fig4   # export Figure 4
IeeeTopologyDiagrams-cb1cb2 # export CB1/CB2 example

# Export individual symbols
IeeeTopologyDiagrams-switch          # horizontal NCB
IeeeTopologyDiagrams-switch-vertical # vertical NCB
IeeeTopologyDiagrams-switch-open-h   # horizontal NOCB
IeeeTopologyDiagrams-switch-open-v   # vertical NOCB
IeeeTopologyDiagrams-ss1             # substation SS1
IeeeTopologyDiagrams-ss2             # substation SS2
IeeeTopologyDiagrams-solid-node      # solid connection point
IeeeTopologyDiagrams-load-node       # load node
```

## 🧩 Glossary

| Chinese | English | Abbreviation |
|---------|---------|--------------|
| 单线图 | One-Line Diagram / Single-Line Diagram | SLD |
| 变电站 | Substation | SS |
| 断路器 | Circuit Breaker | CB |
| 常闭断路器 | Normally-Closed CB | NCB |
| 常开断路器 | Normally-Open CB / Tie Switch | NOCB |
| 母线 | Bus / Bus Bar | — |
| 配电馈线 | Distribution Feeder | — |
| 辐射状网络 | Radial Network | — |
| 支路功率流 | Branch Power Flow | — |
| 有功功率 | Active Power | P |
| 无功功率 | Reactive Power | Q |
| 负荷注入 | Load Injection | P_L, Q_L |
| 配电变压器 | Distribution Transformer | TF |

## 🛠️ Skills

This package includes an AI skill framework for Trae IDE:
- [baran-wu-figures](./IeeeTopologyDiagrams/skills/baran-wu-figures/README_skill.md) - Reproduce original figures from Baran & Wu (1989)

## 👨‍💻 Author

**黎湛联 (Zhanlian Li)**

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

## 🔗 References

1. Baran, M. E., & Wu, F. F. (1989). Network reconfiguration in distribution systems for loss reduction and load balancing. *IEEE Transactions on Power Delivery*, 4(2), 1401-1407.