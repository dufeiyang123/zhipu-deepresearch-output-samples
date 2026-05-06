#!/usr/bin/env python3
"""Chart generation script for Chapter 01.
Run: python3 generate_charts.py
Outputs: chart_01.png, chart_02.png, chart_03.png in the same directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

outdir = os.path.dirname(os.path.abspath(__file__))

# ===== Chart 1: 65+ Population & Aging Rate =====
years = [2020, 2025, 2030, 2035, 2040, 2043, 2045, 2050]
pop_65plus = [3603, 3653, 3696, 3773, 3929, 3953, 3945, 3888]
aging_rate = [28.6, 29.6, 30.8, 32.3, 34.8, 35.8, 36.3, 37.1]
years_band = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
rate_high = [28.6, 29.4, 30.4, 31.8, 33.8, 35.2, 35.7]
rate_low = [28.6, 29.8, 31.2, 32.9, 35.8, 37.2, 38.4]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(years, pop_65plus, width=1.8, color=COLORS[0], alpha=0.75, zorder=3, label='65岁以上人口（万人）')
for i in [0, 5, 7]:
    ax1.text(years[i], pop_65plus[i]+40, f'{pop_65plus[i]:,}', ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[0])
ax1.set_xlabel('年份', fontsize=11)
ax1.set_ylabel('65岁以上人口（万人）', fontsize=11, color=COLORS[0])
ax1.tick_params(axis='y', labelcolor=COLORS[0])
ax1.set_ylim(3200, 4300)
ax1.set_xlim(2017, 2053)
ax2 = ax1.twinx()
ax2.fill_between(years_band, rate_high, rate_low, alpha=0.15, color=COLORS[1], label='高龄化率范围（出生高位～低位方案）', zorder=2)
ax2.plot(years, aging_rate, color=COLORS[1], linewidth=2.5, marker='o', markersize=6, zorder=5, label='高龄化率·中位方案（%）')
for i in [0, 5, 7]:
    ax2.annotate(f'{aging_rate[i]}%', xy=(years[i], aging_rate[i]), xytext=(0, 12), textcoords='offset points', ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[1])
ax2.set_ylabel('高龄化率（%）', fontsize=11, color=COLORS[1])
ax2.tick_params(axis='y', labelcolor=COLORS[1])
ax2.set_ylim(25, 43)
ax1.annotate('← 绝对峰值 2043年\n   3,953万人', xy=(2043, 3953), xytext=(2047.5, 4180), fontsize=9, color='#333333', arrowprops=dict(arrowstyle='->', color='#666666', lw=1.2), ha='center', va='bottom')
plt.title('日本65岁以上人口及高龄化率演变（2020–2050）', fontsize=14, fontweight='bold', pad=18)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='upper left', fontsize=8.5, framealpha=0.9)
fig.text(0.5, -0.02, '数据来源：IPSS「日本の将来推計人口（令和5年推計）」出生中位·死亡中位方案', ha='center', fontsize=8, color='#666666')
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_01.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved chart_01.png")

# ===== Chart 2: 前期 vs 后期高龄者 =====
years2 = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
pop_6574 = [1747, 1497, 1404, 1477, 1681, 1643, 1455]
pop_75plus = [1856, 2156, 2292, 2296, 2248, 2302, 2433]

fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(years2, [0]*7, pop_6574, alpha=0.7, color=COLORS[4], label='前期高龄者（65–74岁）', zorder=3)
ax.fill_between(years2, pop_6574, [a+b for a,b in zip(pop_6574, pop_75plus)], alpha=0.7, color=COLORS[1], label='后期高龄者（75岁以上）', zorder=3)
for i in [0, -1]:
    ax.text(years2[i], pop_6574[i]/2, f'{pop_6574[i]:,}', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    ax.text(years2[i], pop_6574[i]+pop_75plus[i]/2, f'{pop_75plus[i]:,}', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
ax.annotate('2018年前后\n后期高龄者首次\n超过前期高龄者', xy=(2020, 1800), xytext=(2023, 700), fontsize=8.5, color='#333333', ha='center', arrowprops=dict(arrowstyle='->', color='#666666', lw=1.0))
ax.set_xlabel('年份', fontsize=11)
ax.set_ylabel('人口（万人）', fontsize=11)
ax.set_title('日本前期高龄者与后期高龄者人口变化（2020–2050）', fontsize=14, fontweight='bold', pad=15)
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
ax.set_ylim(0, 4500)
ax.set_xlim(2018, 2052)
fig.text(0.5, -0.02, '数据来源：IPSS「日本の将来推計人口（令和5年推計）」及内阁府「令和7年版高龄社会白书」', ha='center', fontsize=8, color='#666666')
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_02.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved chart_02.png")

# ===== Chart 3: 独居世带 =====
years3 = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
solo_households = [738, 800, 870, 940, 1000, 1050, 1084]
solo_ratio = [35.2, 36.5, 38.0, 39.8, 41.5, 43.3, 45.1]

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(years3, solo_households, width=2.2, color=COLORS[3], alpha=0.75, zorder=3, label='65岁以上独居世带数（万户）')
for i in [0, 3, 6]:
    ax1.text(years3[i], solo_households[i]+18, f'{solo_households[i]}', ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=COLORS[3])
ax1.set_xlabel('年份', fontsize=11)
ax1.set_ylabel('独居世带数（万户）', fontsize=11, color=COLORS[3])
ax1.tick_params(axis='y', labelcolor=COLORS[3])
ax1.set_ylim(500, 1250)
ax1.set_xlim(2017, 2053)
ax2 = ax1.twinx()
ax2.plot(years3, solo_ratio, color=COLORS[5], linewidth=2.5, marker='s', markersize=7, zorder=5, label='独居占65+全部世带比例（%）')
for i in [0, 6]:
    ax2.annotate(f'{solo_ratio[i]}%', xy=(years3[i], solo_ratio[i]), xytext=(0, 12), textcoords='offset points', ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=COLORS[5])
ax2.set_ylabel('独居占65+全部世带比例（%）', fontsize=11, color=COLORS[5])
ax2.tick_params(axis='y', labelcolor=COLORS[5])
ax2.set_ylim(30, 52)
ax1.annotate('+47%\n(+346万户)', xy=(2050, 1084), xytext=(2050, 1170), fontsize=9, color='#333333', ha='center', va='bottom', fontweight='bold')
plt.title('日本65岁以上独居世带数量及占比变化（2020–2050）', fontsize=14, fontweight='bold', pad=18)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='upper left', fontsize=9, framealpha=0.9)
fig.text(0.5, -0.02, '数据来源：IPSS「日本の世帯数の将来推計（令和6年推計）」', ha='center', fontsize=8, color='#666666')
plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_03.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved chart_03.png")

print("\nAll 3 charts generated successfully.")
