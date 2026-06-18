# Figure 4 复现参数规范
# Baran & Wu (1989) - Network Reconfiguration in Distribution Systems

## 1. 画布设置
- `bbox_inches='tight'` 自动裁剪
- `dpi=200`
- xlim: 左边界 -0.6, 右边界自适应 (right_bus_x + 0.9)
- ylim: -2.2 到 3.2
- `aspect='equal'`

## 2. 全局样式参数
```python
BUS_LW = 2.2          # 母线线宽
TEXT_FS = 20          # 节点标签字号 (已翻倍)
LABEL_FS = 18         # 配变标签字号
TITLE_FS = 22         # 标题字号
_DASH_ON = 1.5        # 虚线段长
_DASH_OFF = 1.5       # 虚线间隔
```

## 3. Y坐标系统
| 名称 | 值 | 用途 |
|------|-----|------|
| `o_y` | 1.5 | 顶部节点0标签位置 |
| `bar_y` | 1.3 | 顶部横母线Y坐标 |
| `stub_y` | -0.75 | 底部主馈线Y坐标 |
| `pm_y` | -0.98 | P标签文字Y坐标 |
| `arrow_y` | -0.865 | 水平箭头Y坐标 (stub_y和pm_y中点) |

## 4. 顶部结构 (Node 0)
```python
bar_length = 1.4                      # 顶部横母线长度
o_x = (k_x + n_x) / 2                 # 自动对齐(b)标签
fd_l_x = o_x - bar_length * 0.25      # Pok脚X坐标
fd_r_x = o_x + bar_length * 0.25      # Pon脚X坐标
```

### 4.1 顶部斜虚线 (关键特征)
- **Pok虚线**: 从 (fd_l_x, bar_y-0.1) 到 左竖母线上端
- **Pon虚线**: 从 (fd_r_x, bar_y-0.1) 到 右竖母线上端
- 长度 = (i-1到左stub距离)/2
- **箭头**: 沿虚线方向，长度0.47，指向外侧，位于虚线上方偏移0.35

## 5. 底部主路径 (从左到右)

### 5.1 左侧竖母线
```python
left_bus_x = 0.3
left_bus_y = -0.4
bar_length = 1.4
feeder_len = 0.1                      # stub长度
```

### 5.2 i-1 节点
```python
stub_x = left_bus_x + feeder_len      # 0.4
conn_len = 0.735                      # 0.7*0.7*1.5
i1_x = stub_x + conn_len              # bar_node中心
# 绘制: bar_node + 左拐角 + 向下虚线延长
# 标签: (m) 位于 stub_x 和 i1_x 中点上方0.15
```

### 5.3 i-1 到 k-1 虚线
```python
dash_start_x = i1_x + bar_h * 0.7     # 实线末端
dash_end_x = dash_start_x + bar_h * 0.8  # 虚线终点
```

### 5.4 k-1 节点
```python
k1_x = dash_end_x + bar_h * 0.7
# 特征: bare bar_node (无拐角)
# Pk-1: 水平向右箭头，箭头长度0.47
#       标签位置: x+offset-0.02, pm_y, ha='left'
# (k)标签: 位于 k-1 和 k 中点上方0.15
```

### 5.5 k 节点
```python
k_conn_start_x = k1_x + bar_h * 0.7
k_x = k_conn_start_x + bar_h * 0.7
# 特征: bar + 左拐角 + 向下虚线，无右侧出线
# Pk: 垂直向下箭头
#     箭头起点: bar_bot - 0.0395
#     箭头长度: 0.47
#     标签: bar_bot - 0.389, x+0.10
```

### 5.6 n 节点
```python
n_x = k_x + bar_h * 0.7 * 2           # 纯虚线连接k→n
# (b)标签: 位于 k 和 n 中点上方0.15
# 特征: bar + 右拐角 + 向下虚线
# ΔPn: 水平向左箭头
#      箭头: n_x - 0.10 - 0.47
#      标签: n_x - 0.015 - 0.02, pm_y
```

### 5.7 n-1 节点
```python
n1_x = n_x + bar_h * 0.7 * 2
# 特征: bare bar_node (无拐角，无标签)
```

### 5.8 右侧竖母线
```python
conn_total = 1.5                      # n-1到母线总长
solid_len = conn_total / 4            # 实线段长度
dash_len = conn_total / 2             # 虚线段长度(占1/2)
right_bus_x = n1_x + conn_total + 0.1
right_bus_y = -0.4
# 连接: 实线(1/4) — 虚线(1/2) — 实线(1/4) — stub
# Pio: 垂直向下箭头，末端与拐角虚线末端对齐
#      箭头长度0.47，标签在箭头中点左侧
```

## 6. 箭头规范

### 6.1 水平箭头 (Pm, Pk-1, ΔPn)
- 箭头长度: 0.47
- 线宽: BUS_LW (2.2)
- 标签y: pm_y = -0.98

### 6.2 垂直箭头 (Pk, Pio)
- 箭头长度: 0.47
- Pk: 向下，标签在右侧
- Pio: 向下，末端与拐角虚线末端对齐，标签在左侧

### 6.3 斜向箭头 (Pok, Pon)
- 箭头长度: 0.47 (归一化)
- 方向: 与斜虚线平行
- 位置: 斜线上方偏移0.35，向外偏移0.50
- 指向: 向下 (从xytext到xy)

## 7. 标签位置汇总

| 标签 | 位置 | 对齐 |
|------|------|------|
| 0 | (k_x+n_x)/2, o_y+0.08 | center, bottom |
| (m) | (stub_x+i1_x)/2, stub_y+0.15 | center, bottom |
| k-1 | k1_x, stub_y+bar_h/2+0.06 | center, bottom |
| (k) | (k1_x+k_x)/2, stub_y+0.15 | center, bottom |
| k | k_x, stub_y+bar_h/2+0.06 | center, bottom |
| (b) | (k_x+n_x)/2, stub_y+0.15 | center, bottom |
| n | n_x, stub_y+bar_h/2+0.06 | center, bottom |
| n-1 | n1_x, stub_y+bar_h/2+0.06 | center, bottom |
| Pm | stub_x-0.02, pm_y | left, top |
| Pk-1 | k1_x+0.08, pm_y | left, top |
| Pk | k_x+0.10, bar_bot-0.389 | left, center |
| ΔPn | n_x-0.035, pm_y | right, top |
| Pio | right_bus_x-0.10, (arrow_start+end)/2 | right, center |
| Pok | 左斜线中点上方0.40 | right, center |
| Pon | 右斜线中点上方0.40 | left, center |

## 8. 函数调用链
```
draw_common_node_o(ax, o_x, o_y, bar_length=1.4, label=r'$0$')
draw_common_node_o_left(ax, 0.3, -0.4, bar_length=1.4, feeder_len=0.1)
draw_node_i_minus_1(ax, i1_x, stub_y, label=None)  # 无i-1标签
draw_node_k_minus_1(ax, k1_x, stub_y, next_x=k_x, ...)
draw_node_k(ax, k_x, stub_y)
draw_node_n(ax, n_x, stub_y)
draw_bar_node(ax, n1_x, ...)  # n-1 bare bar
draw_common_node_o_right(ax, right_bus_x, right_bus_y, corner=True)
```

## 9. 绘图顺序
1. 底部路径从左到右 (i-1 → k-1 → k → n → n-1 → 右母线)
2. 计算 o_x = (k_x + n_x) / 2
3. 顶部 Node 0
4. 虚线斜线连接 (Pok, Pon)
5. 所有箭头
6. 所有标签
7. 标题

## 10. 与原图的关键差异修正
- 顶部节点标为 "0" 而非 "o"
- 删除 i-1 节点标签 (只保留节点结构)
- Pok/Pon 箭头方向向外指
- Pk 垂直箭头位置
- ΔPn 标签右移避免重叠
