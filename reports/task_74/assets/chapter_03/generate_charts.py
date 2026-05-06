"""
Chart generation script for Chapter 03.
Run this script to generate all charts for Chapter 3.
Usage: python3 assets/chapter_03/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Chart 1: Fusion Strategy Accuracy Comparison — Boulahia et al. (2021)
# ============================================================
def chart_01():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: NTU RGB-D
    datasets_ntu = ['Cross-Subject', 'Cross-View']
    early_ntu = [86.74, 87.62]
    inter_ntu = [95.94, 98.11]
    late_ntu = [94.30, 97.61]

    x = np.arange(len(datasets_ntu))
    width = 0.22

    bars1 = axes[0].bar(x - width, early_ntu, width, label='Early Fusion', color=COLORS[0], edgecolor='white', linewidth=0.5)
    bars2 = axes[0].bar(x, inter_ntu, width, label='Intermediate Fusion', color=COLORS[2], edgecolor='white', linewidth=0.5)
    bars3 = axes[0].bar(x + width, late_ntu, width, label='Late Fusion', color=COLORS[1], edgecolor='white', linewidth=0.5)

    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            axes[0].annotate(f'{height:.1f}%',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 5), textcoords="offset points",
                            ha='center', va='bottom', fontsize=9, fontweight='bold')

    axes[0].set_ylabel('Accuracy (%)', fontsize=11)
    axes[0].set_title('NTU RGB-D (56,880 samples, 60 classes)', fontsize=12, fontweight='bold', pad=12)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(datasets_ntu, fontsize=10)
    axes[0].set_ylim(80, 103)
    axes[0].legend(fontsize=9, loc='lower right')
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].grid(axis='y', alpha=0.3)

    # Right: SBU Interaction
    strategies = ['Early\nFusion', 'Intermediate\nFusion', 'Late\nFusion']
    sbu_acc = [89.57, 99.05, 95.61]
    bar_colors = [COLORS[0], COLORS[2], COLORS[1]]

    bars_sbu = axes[1].bar(strategies, sbu_acc, width=0.45, color=bar_colors, edgecolor='white', linewidth=0.5)

    for bar, val in zip(bars_sbu, sbu_acc):
        axes[1].annotate(f'{val:.2f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, val),
                        xytext=(0, 5), textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

    axes[1].set_ylabel('Accuracy (%)', fontsize=11)
    axes[1].set_title('SBU Interaction (282 seq., 8 classes)', fontsize=12, fontweight='bold', pad=12)
    axes[1].set_ylim(82, 105)
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].grid(axis='y', alpha=0.3)

    fig.suptitle('融合策略准确率对比 — Boulahia et al. (2021) 实验基准',
                 fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'chart_01.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")

# ============================================================
# Chart 2: Real-Time Latency Benchmarks
# ============================================================
def chart_02():
    fig, ax = plt.subplots(figsize=(12, 6.5))

    systems = [
        'TempoFuse\n(ARM Cortex-A78)',
        'CAM-Vtrans\n(GPU)',
        'Sports-ACtrans Net\n(GPU)',
        'Jetson INT8\n(Edge GPU)'
    ]
    latencies = [4, 19.2, 128.76, 240]
    colors = [COLORS[2], COLORS[4], COLORS[3], COLORS[1]]

    bars = ax.barh(systems, latencies, height=0.5, color=colors, edgecolor='white', linewidth=0.5)

    for bar, val in zip(bars, latencies):
        label = f'{val:.1f} ms' if val != 4 else '<4 ms'
        ax.annotate(label,
                    xy=(val, bar.get_y() + bar.get_height() / 2),
                    xytext=(8, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=11, fontweight='bold')

    ax.axvline(x=40, color='#e74c3c', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.axvline(x=200, color='#f39c12', linestyle='--', linewidth=1.5, alpha=0.7)

    ax.text(40, len(systems) - 0.15, '25 FPS\n(40 ms)', ha='center', va='bottom',
            fontsize=8.5, color='#e74c3c', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#e74c3c', alpha=0.85))
    ax.text(200, len(systems) - 0.15, '实时反馈阈值\n(200 ms)', ha='center', va='bottom',
            fontsize=8.5, color='#f39c12', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#f39c12', alpha=0.85))

    ax.set_xlabel('推理延迟 (ms)', fontsize=12)
    ax.set_xlim(0, 320)
    ax.set_title('多模态融合架构推理延迟基准对比', fontsize=14, fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', alpha=0.3)

    ax.text(0.98, 0.03,
            '注: LLM融合 (如 Gemini-2.5-Pro) 延迟为秒级，不在此图范围内',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=8.5, fontstyle='italic', color='#666666')

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'chart_02.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")

# ============================================================
# Chart 3: Temporal Alignment Pipeline Diagram
# ============================================================
def chart_03():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    ax.text(7, 7.5, '异构传感器流时序对齐流程', fontsize=16, fontweight='bold',
            ha='center', va='center', color='#1a1a1a')

    # Left: Sensor Streams
    sensor_data = [
        ('视频流\n30 fps', COLORS[0], 6.2),
        ('IMU\n100–1000 Hz', COLORS[1], 4.8),
        ('心率监测\n1 Hz', COLORS[2], 3.4),
        ('GPS\n10 Hz', COLORS[3], 2.0),
    ]

    for label, color, y in sensor_data:
        box = FancyBboxPatch((0.3, y - 0.45), 2.2, 0.9, boxstyle="round,pad=0.15",
                             facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.85)
        ax.add_patch(box)
        ax.text(1.4, y, label, ha='center', va='center', fontsize=9.5,
                fontweight='bold', color='white')

    # Middle: Alignment Methods
    classical_y = 5.5
    ax.add_patch(FancyBboxPatch((4.2, classical_y - 0.55), 2.6, 1.1,
                 boxstyle="round,pad=0.15", facecolor='#dce6f1', edgecolor=COLORS[0], linewidth=1.5))
    ax.text(5.5, classical_y + 0.15, '经典对齐方法', ha='center', va='center',
            fontsize=10, fontweight='bold', color=COLORS[0])
    ax.text(5.5, classical_y - 0.2, 'DTW / CCA / KCCA\n自适应插值 / 重采样',
            ha='center', va='center', fontsize=8, color='#333333')

    learnable_y = 3.3
    ax.add_patch(FancyBboxPatch((4.2, learnable_y - 0.55), 2.6, 1.1,
                 boxstyle="round,pad=0.15", facecolor='#e8f0e0', edgecolor=COLORS[2], linewidth=1.5))
    ax.text(5.5, learnable_y + 0.15, '可学习对齐方法', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#4a7a2e')
    ax.text(5.5, learnable_y - 0.2, 'TempoFuse DTA 层\nDCCA / 端到端训练',
            ha='center', va='center', fontsize=8, color='#333333')

    ax.text(5.5, 4.4, 'OR', ha='center', va='center', fontsize=11,
            fontweight='bold', color='#999999',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    # Right: Unified + Fusion
    unified_y = 4.4
    ax.add_patch(FancyBboxPatch((8.2, unified_y - 0.45), 2.4, 0.9,
                 boxstyle="round,pad=0.15", facecolor=COLORS[4], edgecolor='white', linewidth=1.5, alpha=0.9))
    ax.text(9.4, unified_y, '统一时间参考帧\n对齐后特征', ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='white')

    fusion_y = 4.4
    ax.add_patch(FancyBboxPatch((11.5, fusion_y - 0.55), 2.2, 1.1,
                 boxstyle="round,pad=0.15", facecolor=COLORS[5], edgecolor='white', linewidth=1.5, alpha=0.9))
    ax.text(12.6, fusion_y + 0.12, '跨模态融合网络', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(12.6, fusion_y - 0.22, '(Attention / GNN)', ha='center', va='center',
            fontsize=8, color='white')

    # Arrows
    for y in [6.2, 4.8, 3.4, 2.0]:
        ax.annotate('', xy=(4.2, (classical_y + learnable_y) / 2),
                    xytext=(2.5, y),
                    arrowprops=dict(arrowstyle='->', color='#888888', linewidth=1.2,
                                   connectionstyle='arc3,rad=0.0'))

    ax.annotate('', xy=(8.2, unified_y + 0.1), xytext=(6.8, classical_y),
                arrowprops=dict(arrowstyle='->', color=COLORS[0], linewidth=1.5,
                               connectionstyle='arc3,rad=-0.15'))
    ax.annotate('', xy=(8.2, unified_y - 0.1), xytext=(6.8, learnable_y),
                arrowprops=dict(arrowstyle='->', color=COLORS[2], linewidth=1.5,
                               connectionstyle='arc3,rad=0.15'))

    ax.annotate('', xy=(11.5, fusion_y), xytext=(10.6, unified_y),
                arrowprops=dict(arrowstyle='->', color='#555555', linewidth=1.8))

    # Bottom annotations
    annot_data = [
        (1.4, 0.9, '采样率差异\n可达 1000x', '#666666'),
        (5.5, 1.5, 'TempoFuse: ARM Cortex-A78\n上 <4 ms 延迟', '#4a7a2e'),
        (9.4, 2.5, '消除时钟偏移\n与采样率差异', '#1a7a9a'),
    ]
    for x, y, txt, color in annot_data:
        ax.text(x, y, txt, ha='center', va='center', fontsize=7.5,
                fontstyle='italic', color=color,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#f9f9f9', edgecolor='#dddddd', alpha=0.8))

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'chart_03.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")

if __name__ == '__main__':
    chart_01()
    chart_02()
    chart_03()
