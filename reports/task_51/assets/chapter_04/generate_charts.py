#!/usr/bin/env python3
"""Chart generation script for Chapter 04.
Run: python3 generate_charts.py
Outputs: chart_01.png, chart_02.png, chart_03.png in the same directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

outdir = os.path.dirname(os.path.abspath(__file__))

# ===== Chart 1: Food Expenditure Structure Comparison =====
# Data: 2025 monthly food expenditure breakdown
# All households (二人以上世帯): total food ~94,650 yen/month
#   外食 16,563 (17.5%), 調理食品 13,580 (14.3%), remaining 68.2%
# 65+ elderly couple unemployed households: total food 78,964 yen/month
#   外食 lower (~10%), 調理食品 higher (~18%), remaining ~72%

categories = ['生鮮/加工食品\n飲料/酒類等', '調理食品\n(中食/惣菜)', '外食']

all_ages_pct = [68.2, 14.3, 17.5]
all_ages_val = [64507, 13580, 16563]

elderly_pct = [72.0, 18.0, 10.0]
elderly_val = [56864, 14200, 7900]

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(categories))
width = 0.32

bars1 = ax.bar(x - width/2, all_ages_pct, width,
               label='全年龄二人以上世帯', color=COLORS[0],
               edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + width/2, elderly_pct, width,
               label='65歳以上夫妇无职世帯', color=COLORS[1],
               edgecolor='white', linewidth=0.5)

for bar, pct, val in zip(bars1, all_ages_pct, all_ages_val):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{pct:.1f}%\n({val:,.0f}円/月)',
            ha='center', va='bottom', fontsize=9, color=COLORS[0], fontweight='bold')

for bar, pct, val in zip(bars2, elderly_pct, elderly_val):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
            f'{pct:.1f}%\n({val:,.0f}円/月)',
            ha='center', va='bottom', fontsize=9, color=COLORS[1], fontweight='bold')

ax.set_ylabel('占食料支出比例 (%)', fontsize=12)
ax.set_title('老年世帯食料消费结构对比 (2025年月均)\n65歳以上世帯: 中食占比高、外食占比低',
             fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 98)
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax.yaxis.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

fig.text(0.5, -0.01,
         '数据来源: 総務省「家計調査」2025年平均  |  65+世帯外食/調理食品占比为基于消费特征的估算値',
         ha='center', fontsize=8, color='gray', style='italic')

plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_01.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_01.png")


# ===== Chart 2: Four Sub-market Projections (Stacked Bar) =====
# Data from writer draft Section 4.6.3 (using midpoints of ranges, in 兆日元)
years_proj = ['2025\n(基准)', '2030', '2040', '2050']

# Sub-markets (兆日元, midpoints)
food_total = [16.5, 18.5, 22.0, 23.0]          # 老年世帯食料総額
health_food = [0.50, 0.65, 0.825, 0.90]         # 健康功能食品(老年份额)
care_food = [0.20, 0.30, 0.50, 0.625]           # 介护食品/UDF
catering = [1.65, 1.90, 2.40, 2.75]             # 给食/配食服务(老年部分)

totals = [f + h + c + ca for f, h, c, ca in zip(food_total, health_food, care_food, catering)]

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years_proj))
width = 0.55

b1 = ax.bar(x, food_total, width, label='老年世帯食料消费総額', color=COLORS[0])
b2 = ax.bar(x, health_food, width, bottom=food_total, label='健康功能食品(老年份额)', color=COLORS[2])
bottom2 = [f + h for f, h in zip(food_total, health_food)]
b3 = ax.bar(x, care_food, width, bottom=bottom2, label='介护食品/UDF', color=COLORS[3])
bottom3 = [b + c for b, c in zip(bottom2, care_food)]
b4 = ax.bar(x, catering, width, bottom=bottom3, label='给食/配食服务(老年部分)', color=COLORS[4])

# Add total labels on top
for i, total in enumerate(totals):
    ax.text(i, total + 0.4, f'{total:.1f}兆円',
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#333333')

ax.set_ylabel('市场规模 (兆日元)', fontsize=12)
ax.set_title('"食"领域老年消费四子市场规模推演 (2025-2050)\n基准情景, IPSS中位方案',
             fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(years_proj, fontsize=11)
ax.set_ylim(0, 32)
ax.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax.yaxis.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

fig.text(0.5, -0.01,
         '数据来源: 総務省「家計調査」, 矢野経済研究所, 日本介護食品協議会, IPSS人口推計  |  各子市场取区间中位値',
         ha='center', fontsize=8, color='gray', style='italic')

plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_02.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_02.png")


# ===== Chart 3: 85+ Population vs Care Food Market (Dual Axis) =====
# 85+ population data (from plan/writer):
#   2020: 616万, 2025: ~670万(est), 2030: ~800万(est), 2035: 1036万, 2040: ~1100万(est), 2050: 1170万
# Care food market (介護食品/UDF/高齢者向け食品):
#   2020: ~1500億(est), 2024-25: 2000-2200億, 2028: 2215億(矢野予測)
#   projections: 2030: 2800-3200, 2040: 4500-5500, 2050: 5500-7000

years_dual = [2020, 2025, 2030, 2035, 2040, 2050]
pop_85plus = [616, 670, 800, 1036, 1100, 1170]  # 万人
care_market = [1500, 2100, 3000, 3800, 5000, 6250]  # 億日元 (midpoints)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for 85+ population
bar_width = 0.6
bars = ax1.bar(range(len(years_dual)), pop_85plus, bar_width,
               color=COLORS[0], alpha=0.75, label='85歳以上人口 (万人)', zorder=2)

ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('85歳以上人口 (万人)', fontsize=12, color=COLORS[0])
ax1.tick_params(axis='y', labelcolor=COLORS[0])
ax1.set_xticks(range(len(years_dual)))
ax1.set_xticklabels(years_dual, fontsize=11)
ax1.set_ylim(0, 1500)

# Add population labels on bars (only key values)
for i, (bar, val) in enumerate(zip(bars, pop_85plus)):
    if i in [0, 1, 3, 5]:  # key years
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 25,
                f'{val}万人', ha='center', va='bottom', fontsize=9,
                color=COLORS[0], fontweight='bold')

# Line chart for care food market on secondary axis
ax2 = ax1.twinx()
line = ax2.plot(range(len(years_dual)), care_market, 'o-',
                color=COLORS[1], linewidth=2.5, markersize=8,
                label='介護食品/UDF市场规模 (億円)', zorder=3)

ax2.set_ylabel('介護食品/UDF市场规模 (億日元)', fontsize=12, color=COLORS[1])
ax2.tick_params(axis='y', labelcolor=COLORS[1])
ax2.set_ylim(0, 8000)

# Add market size labels (only key values)
for i, val in enumerate(care_market):
    if i in [0, 1, 4, 5]:
        offset_y = 300 if i != 5 else 300
        ax2.annotate(f'{val:,}億円', (i, val),
                    textcoords="offset points", xytext=(0, 12),
                    ha='center', fontsize=9, color=COLORS[1], fontweight='bold')

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9, framealpha=0.9)

ax1.set_title('85歳以上人口増長与介護食品市场规模対照 (2020-2050)\n超高齢人口倍増が介護食品需要を強力に牽引',
              fontsize=13, fontweight='bold', pad=15)

ax1.yaxis.grid(True, alpha=0.3, linestyle='--')
ax1.set_axisbelow(True)

fig.text(0.5, -0.01,
         '数据来源: IPSS「日本の将来推計人口」, 日本介護食品協議会, 矢野経済研究所  |  2030-2050年市场规模为推演估算',
         ha='center', fontsize=8, color='gray', style='italic')

plt.tight_layout()
plt.savefig(os.path.join(outdir, 'chart_03.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_03.png")
