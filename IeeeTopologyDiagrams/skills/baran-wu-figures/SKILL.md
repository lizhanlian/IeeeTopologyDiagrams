---
name: baran-wu-figures
description: |
  Reproduce and modify IEEE 33-bus topology diagrams from Baran & Wu (1989) paper
  "Network Reconfiguration in Distribution Systems for Loss Reduction and Load Balancing."
  This skill should be used when users need to draw, modify, or adjust Figures 3 and 4
  from the paper, including one-line diagrams of radial networks and loop diagrams
  with common node o, i-1, k-1, k, n, n-1 nodes, feeder extensions, and power flow labels.
---

# Baran & Wu Figure Reproduction Skill

## Purpose

Reproduce and iteratively modify IEEE 33-bus distribution system topology diagrams
from Baran & Wu (1989). Supports drawing Figures 3 (radial network one-line diagram)
and Figure 4 (loop associated with open branch b).

## When to Use

- User mentions "Baran", "Baran & Wu", "Figure 3", "Figure 4", "distribution system",
  "IEEE 33-bus", or "radial network" diagrams
- User asks to draw or modify a one-line diagram for a distribution network
- User requests adjustments to dashed feeder extension, bar nodes, power flow labels
  (Pm, Pk-1, Pk, ΔPn, Pio, Pok, Pon), or connection arrows

## Drawing Elements Reference

All reusable drawing functions are defined in `scripts/drawing_elements.py`:

| Function | Description |
|----------|-------------|
| `draw_bar_node(x, y_top, y_bottom, width, label)` | Solid black vertical bar node |
| `draw_common_node_o(x, y, bar_length)` | Common node o with horizontal bus bar + vertical line + label |
| `draw_common_node_o_left(x, y, bar_length, feeder_len)` | Left vertical bus bar, stubs go right |
| `draw_common_node_o_right(x, y, bar_length, feeder_len, label, corner, corner_h)` | Right vertical bus bar, stubs go left, optional right corner |
| `draw_node_i_minus_1(x, y, bar_w, bar_h, label)` | i-1 style: bar + left corner + dashed extension + right line |
| `draw_node_k(x, y, bar_h, bar_w, label)` | k node: bar + left corner + dashed extension, no right line |
| `draw_node_k_minus_1(x, y, next_x, bar_h, bar_w, label, ...)` | k-1 subfigure: bare bar + (k) label + Pk-1 arrow |
| `draw_node_n(x, y, bar_h, bar_w, label)` | n node: bar + right corner + dashed extension |
| `draw_feeder_extension_horizontal(x_start, x_end, y)` | Horizontal dashed feeder extension |
| `draw_feeder_extension(x, y_start, y_end)` | Vertical dashed feeder extension |
| `draw_switch(x, y, size)` | Closed switch (horizontal) |
| `draw_switch_open(x, y, size)` | Open switch (horizontal) |
| `draw_node(x, y, label)` | Load node with downward arrow |
| `draw_tf_node(x, y, main_label, tf_label, dx)` | Transformer node |

Styles: `BUS_LW=2.2`, `NODE_LW=1.1`, `TEXT_FS=10`, `LABEL_FS=9`, `SW_SIZE=0.18`

Dashed pattern: `_DASH_ON=1.5`, `_DASH_OFF=1.5`, linestyle `(0, (1.5, 1.5))`

## Figure 3 — Radial Network One-Line Diagram

Run: `scripts/reproduce_fig3.py`

Structure: `0 — i-1 — i — i+1 — n` with horizontal feeder line (solid–dashed–solid),
labeled power flows (P0, Pi-1, Pi, Pi+1, Pn) and load (PLi, QLi).

## Figure 4 — Loop with Open Branch b

Run: `scripts/reproduce_fig4.py`

Complete structure:
```
                        o (source)
                        ├── Pok (vertical: ↓ dashed extension)
                        │    └── slanted dashed ──┐
                        └── Pon (vertical: ↓ dashed extension)
                             └── slanted dashed ──┐
                                                  │
     ┌────────────────────────────────────────────┘
     │
     ├── Pok slanted → left bus bar upper stub (horizontal: → dashed extension)
     │
left bus bar:  upper stub ─→ dashed ─→ ┐
               │                        │ (slanted)
               │                        ↓
               │ bottom stub → Pm → i-1 (m) → dashed feeder → k-1 (k) → k
               │                                                    ↓ Pk-1  ↓ Pk
               └── right corner + dashed extension
                                                                          ↓ (b) dashed
                                                                          n → ΔPn
                                                                          ↓ solid
                                                                          n-1
                                                                          ↓ solid—dashed(1/2)—solid
                                                                          right bus bar (right corner + dashed)
                                                                          ↓ Pio
     right bus bar: upper stub ←─ dashed ←─ ┐
                    │                        │ (slanted)
                    │                        ↓
                    └── Pon slanted ← Pon extension
```

### Code Layout (auto-aligning)

The script computes all positions from left to right, then sets `o_x = (k_x + n_x) / 2`
so that node o is always vertically aligned with the `(b)` label. Axis limits and
figsize auto-adapt via `bbox_inches='tight'` and `xlim` based on `right_bus_x`.

### Key Y Coordinates

| Name | Value | Used for |
|------|-------|----------|
| `o_y` | 1.5 | Node o label |
| `bar_y` | 1.3 | Top horizontal bar |
| `stub_y` | -0.75 | Main feeder line (all horizontal connections) |
| `pm_y` | -0.98 | Pm, Pk-1, ΔPn, Pio text |
| `arrow_y` | (stub_y+pm_y)/2 ≈ -0.865 | Pm, Pk-1 arrows |

### Node Functions Summary

| Node | Function | Corner | Right Line | Special |
|------|----------|--------|------------|---------|
| i-1 | `draw_node_i_minus_1` | Left | Yes | (m) label |
| k-1 | `draw_node_k_minus_1` | None | Yes | (k) label, Pk-1 arrow |
| k | `draw_node_k` | Left | **No** | Pk vertical arrow below |
| n | `draw_node_n` | Right | Yes | ΔPn leftward arrow |
| n-1 | `draw_bar_node` directly | None | Yes | Bare bar, no label |

### Slanted Dashed Lines (stub extensions)

Four stub extensions + two slanted lines + two parallel downward arrows:
- **Pok foot**: vertical dashed ↓ (length = (i-1到左stub)/2)
- **Pon foot**: vertical dashed ↓ (same length)
- **Left bus bar upper stub**: horizontal dashed → (same length)
- **Right bus bar upper stub**: horizontal dashed ← (same length)
- **Slanted 1**: Pok extension end → left bus bar extension end
- **Slanted 2**: Pon extension end → right bus bar extension end
- **Parallel arrows**: one on each slanted line, offset 0.50 to side, length=0.47,
  downward direction (same slope as slanted line), above the slanted line
- **Pok/Pon labels**: above each slanted line at midpoint + 0.40 y-offset

### Font Sizes (doubled)

| Constant | Value |
|----------|-------|
| `TEXT_FS` | 20 |
| `LABEL_FS` | 18 |
| `TITLE_FS` | 22 |
| Inline large | 20 (Pok, Pon) |
| Inline regular | 18 (Pm, Pk, Pk-1, ΔPn, Pio, etc.) |

### P Label Styles

| Label | Type | Direction | Position |
|-------|------|-----------|----------|
| Pm | Horizontal arrow | → Right | x-0.02, pm_y, ha='left' |
| Pk-1 | Horizontal arrow | → Right | x-0.02, pm_y, ha='left' |
| Pk | Vertical arrow | ↓ Down | x+0.10, ha='left' |
| ΔPn | Horizontal arrow | ← Left | x-0.47-0.02, pm_y, ha='right' |
| Pio | Vertical arrow | ↑ Up | x-0.10, ha='right', at arrow midpoint |

### Common Adjustments

- **Dashed extension length**: `bar_h * 0.7` in `draw_node_i_minus_1` / `draw_node_k` / `draw_node_n`
- **P arrow position**: offset from node center, arrow length (default 0.47)
- **Node spacing**: `bar_h * 0.7` factor between nodes
- **Axis**: auto-driven by `right_bus_x + 0.9` for x_right, `x_left = -0.6`
- **Stub extension length**: `(i1_x - left_top_x) / 2`

## Workflow

1. Read the relevant reproduce script to understand current layout
2. Make targeted edits using `replace_in_file`
3. Regenerate: `cd v4.0.6 && python -m IeeeTopologyDiagrams.reproduce_fig4`
4. Check output and iterate

## Paper Reference

`references/Baran.1989...md` — Full paper markdown.
