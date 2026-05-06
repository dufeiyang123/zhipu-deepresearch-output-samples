#!/usr/bin/env python3
"""
Chart 1: Post-DBS Recovery and Programming Timeline
Chapter 4 — Life After Deep Brain Stimulation
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

fig, ax = plt.subplots(figsize=(10, 6))

phases = [
    {"start": 0, "end": 2, "label": "Microlesion\nEffect", "color": COLORS[4],
     "note": "Transient motor\nimprovement before\nstimulator activation"},
    {"start": 0, "end": 6, "label": "Wound Healing\n& Restrictions", "color": COLORS[2],
     "note": "No heavy lifting\nSuture removal:\n10-14 days"},
    {"start": 4, "end": 6, "label": "Initial\nProgramming", "color": COLORS[0],
     "note": "First activation\n2-3 sessions\nin first week"},
    {"start": 6, "end": 26, "label": "Iterative Optimization", "color": COLORS[3],
     "note": "Parameter refinement\nMedication stable 3-6 mo"},
    {"start": 26, "end": 52, "label": "Long-Term Maintenance", "color": COLORS[5],
     "note": "Visits every 3-4 mo\nMonitor speech/mood/weight"},
]

y_positions = [4.0, 2.5, 4.0, 2.5, 4.0]

for i, phase in enumerate(phases):
    y = y_positions[i]
    width = phase["end"] - phase["start"]
    rect = mpatches.FancyBboxPatch(
        (phase["start"], y - 0.35), width, 0.7,
        boxstyle="round,pad=0.1", facecolor=phase["color"], edgecolor='white',
        alpha=0.85, linewidth=1.5
    )
    ax.add_patch(rect)
    ax.text(phase["start"] + width / 2, y, phase["label"],
            ha='center', va='center', fontsize=7.5, fontweight='bold',
            color='white', linespacing=1.3)
    if y == 4.0:
        note_y = y + 0.75
        va_val = 'bottom'
    else:
        note_y = y - 0.75
        va_val = 'top'
    ax.text(phase["start"] + width / 2, note_y, phase["note"],
            ha='center', va=va_val, fontsize=6.5, color='#333333',
            linespacing=1.3, style='italic')

ax.annotate('', xy=(54, 1.2), xytext=(-1, 1.2),
            arrowprops=dict(arrowstyle='->', color='#1f4e79', lw=2))

time_marks = [
    (0, "Surgery\nDay 0"), (2, "Week 2"), (4, "Week 4"), (6, "Week 6"),
    (13, "Month 3"), (26, "Month 6"), (39, "Month 9"), (52, "Year 1+"),
]
for x, label in time_marks:
    ax.plot(x, 1.2, 'o', color='#1f4e79', markersize=6, zorder=5)
    ax.text(x, 0.5, label, ha='center', va='top', fontsize=7, fontweight='bold', color='#1f4e79')

ax.set_title('Post-DBS Recovery and Programming Timeline',
             fontsize=14, fontweight='bold', color='#1f4e79', pad=20)
ax.set_xlim(-3, 56)
ax.set_ylim(-0.3, 6.3)
ax.axis('off')

plt.tight_layout()
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart_01.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Saved: {out_path}")
