#!/usr/bin/env python3
"""
Chapter 01 Chart Generation Script
Run this script to generate chart_01.png and chart_02.png in the same directory.
Usage: python3 assets/chapter_01/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Research report color palette
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
C_SEIZING = '#1f4e79'
C_FREEZING = '#c0504d'
C_CRYSTAL = '#f79646'
C_TEXT = '#333333'
C_HIGH = '#8064a2'
C_LOW = '#9bbb59'

# ================================================================
# Chart 1: Seizing-Freezing Dual Process Diagram
# ================================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

ax.text(6, 7.45, 'NFC Dual Process: Seizing & Freezing',
        ha='center', va='center', fontsize=15, fontweight='bold', color=C_TEXT)

ax.add_patch(FancyBboxPatch((0.3, 1.3), 5.0, 5.2, boxstyle="round,pad=0.15",
             facecolor='#dce6f1', edgecolor=C_SEIZING, linewidth=1.5, alpha=0.5))
ax.add_patch(FancyBboxPatch((6.7, 1.3), 5.0, 5.2, boxstyle="round,pad=0.15",
             facecolor='#f2dcdb', edgecolor=C_FREEZING, linewidth=1.5, alpha=0.5))

ax.text(2.8, 6.2, 'Seizing', ha='center', fontsize=13, fontweight='bold', color=C_SEIZING)
ax.text(9.2, 6.2, 'Freezing', ha='center', fontsize=13, fontweight='bold', color=C_FREEZING)

ax.plot([6, 6], [1.5, 6.1], color=C_CRYSTAL, linewidth=2.5, linestyle='--', zorder=5)
ax.text(6, 6.7, 'Belief Crystallization Point', ha='center', va='center',
        fontsize=10, fontweight='bold', color=C_CRYSTAL,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff5e6', edgecolor=C_CRYSTAL, linewidth=1.5))

seize_steps = [
    (2.8, 5.3, 'Limited information input'),
    (2.8, 4.3, 'Seize accessible cues'),
    (2.8, 3.3, 'Fewer competing hypotheses'),
    (2.8, 2.3, 'Rapid initial judgment'),
]
for x, y, l in seize_steps:
    ax.add_patch(FancyBboxPatch((x - 1.7, y - 0.27), 3.4, 0.54, boxstyle="round,pad=0.1",
                 facecolor='white', edgecolor=C_SEIZING, linewidth=1.2))
    ax.text(x, y, l, ha='center', va='center', fontsize=9.5, color=C_SEIZING, fontweight='bold')

for i in range(len(seize_steps) - 1):
    ax.annotate('', xy=(2.8, seize_steps[i + 1][1] + 0.31), xytext=(2.8, seize_steps[i][1] - 0.31),
                arrowprops=dict(arrowstyle='->', color=C_SEIZING, lw=1.5))

ax.annotate('', xy=(5.85, 2.3), xytext=(4.55, 2.3),
            arrowprops=dict(arrowstyle='->', color=C_CRYSTAL, lw=2))

freeze_steps = [
    (9.2, 5.3, 'Judgment solidified'),
    (9.2, 4.3, 'Resist contradictory info'),
    (9.2, 3.3, 'Persuasion resistance'),
    (9.2, 2.3, 'High subjective confidence'),
]
for x, y, l in freeze_steps:
    ax.add_patch(FancyBboxPatch((x - 1.7, y - 0.27), 3.4, 0.54, boxstyle="round,pad=0.1",
                 facecolor='white', edgecolor=C_FREEZING, linewidth=1.2))
    ax.text(x, y, l, ha='center', va='center', fontsize=9.5, color=C_FREEZING, fontweight='bold')

for i in range(len(freeze_steps) - 1):
    ax.annotate('', xy=(9.2, freeze_steps[i + 1][1] + 0.31), xytext=(9.2, freeze_steps[i][1] - 0.31),
                arrowprops=dict(arrowstyle='->', color=C_FREEZING, lw=1.5))

ax.annotate('', xy=(7.45, 5.3), xytext=(6.15, 5.3),
            arrowprops=dict(arrowstyle='->', color=C_CRYSTAL, lw=2))

ax.text(3.2, 1.6, 'High NFC: less info processed, fewer hypotheses,',
        ha='center', fontsize=8, color=C_HIGH, fontweight='bold')
ax.text(3.2, 1.35, 'faster judgment, higher (unwarranted) confidence',
        ha='center', fontsize=8, color=C_HIGH, fontweight='bold')

ax.text(9.0, 1.6, 'Low NFC: more info processed, more hypotheses,',
        ha='center', fontsize=8, color=C_LOW, fontweight='bold')
ax.text(9.0, 1.35, 'slower judgment, greater openness to revision',
        ha='center', fontsize=8, color=C_LOW, fontweight='bold')

ax.text(6, 0.8, 'Source: Kruglanski & Webster (1996), Psychological Review, Vol.103, No.2, pp.263-283',
        ha='center', fontsize=7.5, color='#999', style='italic')

plt.tight_layout(pad=0.3)
plt.savefig(os.path.join(OUT_DIR, 'chart_01.png'), dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("Saved: chart_01.png")

# ================================================================
# Chart 2: NFCS Scale Development & Revision Timeline
# ================================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(1992, 2013)
ax.set_ylim(-1.5, 4)
ax.axis('off')

ax.text(2002.5, 3.7, 'NFCS Scale Development & Revision Timeline',
        ha='center', fontsize=14, fontweight='bold', color=C_TEXT)

ax.plot([1993, 2012], [1.5, 1.5], color='#666', lw=2, zorder=3)

events = [
    (1994, 'Webster & Kruglanski\n42-item NFCS\n5 facets, \u03b1=.84', 2.8, C_SEIZING),
    (1997, 'Neuberg et al.\nTwo-factor critique:\nNFSS vs Decisiveness', 0.0, '#8064a2'),
    (2002, 'Mannetti et al.\nCross-cultural\ninvariance (4 countries)', 2.8, '#4bacc6'),
    (2007, 'Roets & Van Hiel\nAbility vs Need\nDecisiveness resolution', 0.0, C_CRYSTAL),
    (2011, 'Roets & Van Hiel\n15-item NFC-R\nN=1584, \u03b1=.88', 2.8, C_FREEZING),
]

for year, label, y_offset, color in events:
    ax.plot(year, 1.5, 'o', color=color, markersize=10, zorder=5)
    ax.text(year, 1.15, str(year), ha='center', fontsize=9, fontweight='bold', color=color)

    if y_offset > 1.5:
        ax.plot([year, year], [1.6, y_offset - 0.55], color=color, lw=1.2, ls='-')
        ax.text(year, y_offset, label, ha='center', va='bottom', fontsize=8, color=color,
                fontweight='bold', linespacing=1.4,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, lw=1, alpha=0.9))
    else:
        ax.plot([year, year], [1.4, y_offset + 0.7], color=color, lw=1.2, ls='-')
        ax.text(year, y_offset, label, ha='center', va='top', fontsize=8, color=color,
                fontweight='bold', linespacing=1.4,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, lw=1, alpha=0.9))

ax.annotate('', xy=(2006.7, 0.5), xytext=(1997.3, 0.5),
            arrowprops=dict(arrowstyle='->', color='#999', lw=1, ls='--'))
ax.text(2002, 0.3, 'Decisiveness debate resolved', ha='center', fontsize=7,
        color='#999', style='italic')

ax.annotate('', xy=(2010.7, 2.0), xytext=(2007.3, 2.0),
            arrowprops=dict(arrowstyle='->', color='#999', lw=1, ls='--'))
ax.text(2009, 2.15, 'Led to revision', ha='center', fontsize=7, color='#999', style='italic')

ax.text(2002.5, -1.3, 'Sources: Webster & Kruglanski (1994); Neuberg et al. (1997); Roets & Van Hiel (2007, 2011)',
        ha='center', fontsize=7, color='#999', style='italic')

plt.tight_layout(pad=0.3)
plt.savefig(os.path.join(OUT_DIR, 'chart_02.png'), dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()
print("Saved: chart_02.png")
