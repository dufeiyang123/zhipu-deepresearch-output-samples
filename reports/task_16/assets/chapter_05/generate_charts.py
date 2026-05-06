#!/usr/bin/env python3
"""
Chapter 5 Chart Generation Script
Run: python3 generate_charts.py
Outputs: chart_01.png, chart_02.png, chart_03.png in the same directory
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Chart 1: Fusion Level Comparison (RFiDAR System)
# Data: Khan et al., IEEE IoT Magazine 2025
# ============================================================
fusion_levels = ['Single-modal\nBaseline', 'Decision-level\nFusion', 'Data-level\nFusion', 'Feature-level\nFusion']
acc_2m = [93.5, 95.2, 96.6, 98.8]
acc_3m = [91.7, 94.4, 96.7, 97.9]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(fusion_levels))
width = 0.32

bars1 = ax.bar(x - width/2, acc_2m, width, label='2 m', color=COLORS[0], edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + width/2, acc_3m, width, label='3 m', color=COLORS[1], edgecolor='white', linewidth=0.5)

for bar in bars1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.25, f'{h:.1f}%',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[0])
for bar in bars2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.25, f'{h:.1f}%',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[1])

gains_labels = ['+1.7% / +2.7%', '+3.1% / +5.0%', '+5.3% / +6.2%']
for i in range(3):
    ax.text(x[i+1], 89.3, gains_labels[i], ha='center', va='bottom', fontsize=8,
            color=COLORS[2], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#e8f0e0', edgecolor=COLORS[2], alpha=0.85))

ax.set_ylabel('HAR Accuracy (%)', fontsize=12)
ax.set_title('Fusion Level Comparison: RFiDAR System (RFID + UWB Radar)\n5-Class Activity Recognition Accuracy (Khan et al., IEEE IoT Magazine 2025)',
             fontsize=11, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(fusion_levels, fontsize=10)
ax.set_ylim(88, 102)
ax.legend(loc='upper left', fontsize=10, framealpha=0.9, title='Distance')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3)
ax.text(0.02, 0.02, 'Green labels: gain vs single-modal baseline (2m / 3m)',
        transform=ax.transAxes, fontsize=8, color='gray', style='italic')
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, 'chart_01.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_01.png")

# ============================================================
# Chart 2: Foundation Model Comparison Table
# Data: X-Fi (ICLR 2025), Babel (SenSys 2025), AM-FM (arXiv 2026), LWM (arXiv 2024)
# ============================================================
fig, ax = plt.subplots(figsize=(12, 7))
ax.axis('off')

col_labels = ['Model', 'Venue', 'Modalities', 'Pre-train\nData Scale', 'Params', 'Key Performance', 'Open\nSource']
table_data = [
    ['X-Fi', 'ICLR 2025', 'RGB, Depth,\nLiDAR, mmWave, WiFi', '-\n(supervised)', '-', 'HPE MPJPE -24.8%\nHAR Acc +2.8%', 'Yes'],
    ['Babel', 'SenSys 2025', 'WiFi, mmWave, IMU,\nLiDAR, Video, Depth', '5 datasets\n(partial pairs)', '-', 'Fusion +22%\n1-shot +25.2% vs MLLM', 'Yes'],
    ['AM-FM', 'arXiv\nFeb 2026', 'WiFi CSI', '9.2M samples\n439 days', '5M\n(Base)', '9 tasks AUROC > 0.9\nHAR 0.527 -> 0.923', '-'],
    ['LWM', 'arXiv\n2024/2025', 'Wireless\nChannel', '1M+ channel\nsamples', '-', 'Beam prediction\nLoS/NLoS improved', 'Yes\n(HF)'],
]

table = ax.table(cellText=table_data, colLabels=col_labels, loc='center',
                 cellLoc='center', colWidths=[0.08, 0.08, 0.15, 0.12, 0.07, 0.20, 0.07])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2.2)

for j in range(len(col_labels)):
    cell = table[0, j]
    cell.set_facecolor(COLORS[0])
    cell.set_text_props(color='white', fontweight='bold', fontsize=9)
    cell.set_edgecolor('white')

row_colors = ['#f0f4f8', '#ffffff', '#f0f4f8', '#ffffff']
for i in range(len(table_data)):
    for j in range(len(col_labels)):
        cell = table[i+1, j]
        cell.set_facecolor(row_colors[i])
        cell.set_edgecolor('#d0d0d0')
        cell.set_text_props(fontsize=8.5)

ax.set_title('Foundation Models for Contactless Sensing (2024\u20132026 Q1)\nPre-training Paradigm Landscape',
             fontsize=13, fontweight='bold', pad=20, color=COLORS[0])
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, 'chart_02.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_02.png")

# ============================================================
# Chart 3: LLM Sensing Paradigm Comparison
# Data: Apple Research, Wi-Chat, SensorLLM, GLSDA, Wi-Fringe
# ============================================================
fig, ax = plt.subplots(figsize=(12, 7))
ax.axis('off')

paradigms = ['LLM as\nLate Fuser', 'LLM Direct\nInference', 'LLM Semantic\nDistillation']
dimensions = ['Representative\nWork', 'Accuracy', 'Inference\nLatency', 'Deployment\nCost', 'Scalability\n(# Classes)', 'Engineering\nFeasibility']

data = [
    ['Apple Research\n(NeurIPS 2025 WS)', 'F1 > random\n(limited)', 'High\n(LLM call)', 'Low\n(no training)', '12 classes\n(Ego4D)', 'Medium'],
    ['Wi-Chat\nSensorLLM', '62\u201390%\n(4 classes)', 'High\n(API call)', 'High\n(API cost)', '4\u201312\nclasses', 'Low\n(short-term)'],
    ['GLSDA\nWi-Fringe', '95.39%\n(Widar 3.0)', 'Low\n(local model)', 'Medium\n(train once)', '6+ classes\n(expandable)', 'High\n(recommended)'],
]

col_labels_t = ['Dimension'] + paradigms
table_data_t = []
for i, dim in enumerate(dimensions):
    row = [dim] + [data[j][i] for j in range(3)]
    table_data_t.append(row)

table = ax.table(cellText=table_data_t, colLabels=col_labels_t, loc='center',
                 cellLoc='center', colWidths=[0.14, 0.20, 0.20, 0.20])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2.4)

header_colors = ['#555555', COLORS[4], COLORS[1], COLORS[2]]
for j in range(4):
    cell = table[0, j]
    cell.set_facecolor(header_colors[j])
    cell.set_text_props(color='white', fontweight='bold', fontsize=10)
    cell.set_edgecolor('white')

for i in range(len(table_data_t)):
    for j in range(4):
        cell = table[i+1, j]
        if j == 0:
            cell.set_facecolor('#f5f5f5')
            cell.set_text_props(fontweight='bold', fontsize=9)
        else:
            cell.set_facecolor('#ffffff' if i % 2 == 0 else '#f8f8f8')
            cell.set_text_props(fontsize=9)
        cell.set_edgecolor('#d0d0d0')

    # Highlight semantic distillation column (recommended)
    cell3 = table[i+1, 3]
    cell3.set_facecolor('#f0f5e8' if i % 2 == 0 else '#e5eddb')

ax.set_title('LLM-Driven Sensing: Three Technical Paradigms Compared\nAccuracy, Latency, Cost & Feasibility Trade-offs',
             fontsize=13, fontweight='bold', pad=20, color=COLORS[0])
ax.text(0.5, -0.02,
        'Green column (Semantic Distillation): highest short-term engineering feasibility; '
        'Direct Inference: long-term disruptive potential',
        transform=ax.transAxes, fontsize=8.5, ha='center', color='gray', style='italic')
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, 'chart_03.png'), dpi=150, bbox_inches='tight')
plt.close()
print("Saved: chart_03.png")

print("\nAll 3 charts generated successfully!")
