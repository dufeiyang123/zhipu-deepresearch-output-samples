#!/usr/bin/env python3
"""
Chart 2: Medication Reduction and Motor Improvement After STN-DBS
Chapter 4 — Life After Deep Brain Stimulation

Data sources:
  - Chu et al. 2025 (10-year follow-up, N=31, Southern China): LEDD reductions 36.29% (1yr), 40.40% (3yr), 29.10% (10+yr); UPDRS-III improvements 53.02% (1yr), 22.56% (10+yr)
  - INTREPID trial (N=191, 23 US centers, JAMA Neurol 2025): 28% medication reduction, 36% motor improvement at 5 years
  - Meta-analysis (Lachenmayer et al. 2021, 31 studies, N=1,644): average LEDD reduction ~50%
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

fig, ax1 = plt.subplots(figsize=(10, 6))

time_points = ['1 Year', '3 Years', '5 Years', '10+ Years']
ledd_reduction = [36.29, 40.40, 28.0, 29.10]
motor_improvement = [53.02, None, 36.0, 22.56]

x = np.arange(len(time_points))
width = 0.35

bars1 = ax1.bar(x - width/2, ledd_reduction, width, label='LEDD Reduction (%)',
                color=COLORS[0], alpha=0.85, edgecolor='white', linewidth=1)

motor_vals = [v if v is not None else 0 for v in motor_improvement]
motor_colors = [COLORS[1] if v is not None else 'none' for v in motor_improvement]
motor_edges = ['white' if v is not None else 'none' for v in motor_improvement]
bars2 = ax1.bar(x + width/2, motor_vals, width, label='UPDRS-III Improvement (%)',
                color=motor_colors, alpha=0.85, edgecolor=motor_edges, linewidth=1)

for bar, val in zip(bars1, ledd_reduction):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.2,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold',
             color=COLORS[0])

for bar, val in zip(bars2, motor_improvement):
    if val is not None:
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.2,
                 f'{val:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold',
                 color=COLORS[1])

ax1.annotate('Chu et al. 2025\n(N=31, Southern China)',
             xy=(0, 36.29), xytext=(-0.6, 58),
             fontsize=7, color='#555555', style='italic',
             arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8),
             ha='center')

ax1.annotate('INTREPID Trial\n(N=191, 23 US centers)',
             xy=(2, 28), xytext=(2.6, 58),
             fontsize=7, color='#555555', style='italic',
             arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8),
             ha='center')

ax1.text(1 + width/2, 2, 'N/A', ha='center', va='bottom', fontsize=8, color='#999999')

ax1.set_xlabel('Time After DBS Surgery', fontsize=11, labelpad=10)
ax1.set_ylabel('Percentage (%)', fontsize=11, labelpad=10)
ax1.set_title('Medication Reduction and Motor Improvement After STN-DBS',
              fontsize=14, fontweight='bold', color='#1f4e79', pad=18)
ax1.set_xticks(x)
ax1.set_xticklabels(time_points, fontsize=10)
ax1.set_ylim(0, 68)
ax1.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax1.text(0.5, -0.12,
         'Meta-analysis average LEDD reduction after STN-DBS: ~50% (Lachenmayer et al. 2021, 31 studies, N=1,644)',
         transform=ax1.transAxes, fontsize=8, color='#666666', ha='center', style='italic')

plt.tight_layout()
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart_02.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Saved: {out_path}")
