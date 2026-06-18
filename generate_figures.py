"""Generate all 4 complete figures for the README."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.makedirs('assets', exist_ok=True)

from IeeeTopologyDiagrams.reproduce_fig1_full import draw_fig1_complete
from IeeeTopologyDiagrams.reproduce_fig2 import draw_ieee33bus_diagram
from IeeeTopologyDiagrams.reproduce_fig3 import draw_fig3_diagram
from IeeeTopologyDiagrams.reproduce_fig4 import draw_fig4_diagram

print("生成 Figure 1 (完整的一次回路示意图)...")
p1 = draw_fig1_complete('assets/fig1.png')
print(f"✅ {p1}")

print("生成 Figure 2 (IEEE 33-Bus 完整系统)...")
p2 = draw_ieee33bus_diagram('assets/fig2.png')
print(f"✅ {p2}")

print("生成 Figure 3 (辐射网络 P/Q 标注)...")
p3 = draw_fig3_diagram('assets/fig3.png')
print(f"✅ {p3}")

print("生成 Figure 4 (带开分支的环路)...")
p4 = draw_fig4_diagram('assets/fig4.png')
print(f"✅ {p4}")

print("\n🎉 四幅图全部生成完毕")