#!/usr/bin/env python3
"""
Chart 3: DBS Hardware Complication Rates
Chapter 4 — Life After Deep Brain Stimulation

Data source:
  - Jung et al. 2022, 21-year single-center experience, N=426 bilateral DBS
    (Front Aging Neurosci 2022)
  - Doshi 2021 (519-case series, 20 years): lead fracture 2.5%, infection 1.9%
  - Literature broadly: DBS infection rates 2-6%
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

fig, ax = plt.subplots(figsize=(10, 6))

categories = ['Infection', 'Intracranial\nHemorrhage', 'Hardware\nFailure', 'Mortality']
rates = [2.8, 2.3, 0.7, 0.5]
counts = ['12/426', '10/426', '3/426', '2/426']
colors_bar = [COLORS[1], COLORS[5], COLORS[3], COLORS[0]]

bars = ax.barh(categories, rates, height=0.55, color=colors_bar, alpha=0.85,
               edgecolor='white', linewidth=1.5)

for bar, rate, count in zip(bars, rates, counts):
    ax.text(bar.get_width() + 0.12, bar.get_y() + bar.get_height()/2,
            f'{rate}%  ({count})', va='center', ha='left',
            fontsize=10, fontweight='bold', color='#333333')

ax.text(2.8 + 0.12, 0 + 0.32, 'Mean onset: 23.7 mo; none after 4 yrs',
        fontsize=7.5, color='#777777', style='italic', va='bottom')

ax.text(2.3 + 0.12, 1 + 0.32, '0.7% required surgical intervention',
        fontsize=7.5, color='#777777', style='italic', va='bottom')

ax.set_xlim(0, 5.8)
ax.set_xlabel('Rate (%)', fontsize=11, labelpad=10)
ax.set_title('DBS Hardware Complication Rates\n(21-Year Single-Center Experience, N=426 Bilateral DBS)',
             fontsize=13, fontweight='bold', color='#1f4e79', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.invert_yaxis()

ax.text(0.5, -0.1,
        'Contemporary literature reports DBS infection rates of 2-6%; risk higher at IPG replacement than primary implantation\n(Jung et al. 2022; Doshi 2021)',
        transform=ax.transAxes, fontsize=8, color='#666666', ha='center', style='italic')

plt.tight_layout()
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart_03.png')
plt.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"Saved: {out_path}")
