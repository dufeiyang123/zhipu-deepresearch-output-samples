#!/usr/bin/env python3
"""
Generate Chapter 6 charts for the Spring Ecosystem report.
Run: python3 generate_charts.py
Output: chart_01.png, chart_02.png, chart_03.png in the same directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUTDIR = os.path.dirname(os.path.abspath(__file__))


def generate_chart_01():
    """Spring Boot Version Timeline (1.0 -> 4.0)"""
    fig, ax = plt.subplots(figsize=(10, 6))

    releases = [
        (2014.33, '1.0', 'Boot 1.0\n(2014-04)'),
        (2018.17, '2.0', 'Boot 2.0\n(2018-03)'),
        (2022.90, '3.0', 'Boot 3.0\n(2022-11)'),
        (2023.40, '3.1', '3.1'),
        (2023.90, '3.2', 'Boot 3.2\n(2023-11)'),
        (2024.40, '3.3', '3.3'),
        (2024.90, '3.4', '3.4'),
        (2025.40, '3.5', '3.5'),
        (2025.90, '4.0', 'Boot 4.0\n(2025-11)'),
    ]

    milestones = {
        '1.0': 'Auto-configuration\nStarter POMs\nEmbedded Servers',
        '2.0': 'Spring 5 / WebFlux\nActuator Overhaul\nKotlin Support',
        '3.0': 'Jakarta EE 10\nGraalVM Native\nJava 17 Baseline',
        '3.2': 'Virtual Threads\nProject CRaC\nRestClient',
        '4.0': 'Jakarta EE 11\nModularization\nJSpecify Null Safety',
    }

    y_base = 0.5
    ax.axhline(y=y_base, color='#cccccc', linewidth=2.5, zorder=1)

    era_spans = [
        (2013.5, 2018.0, 'Boot 1.x Era', '#d6e4f0'),
        (2018.0, 2022.7, 'Boot 2.x Era', '#fdf2d0'),
        (2022.7, 2025.3, 'Boot 3.x Era', '#d9eed9'),
        (2025.3, 2026.5, 'Boot 4.x', '#e8d5f5'),
    ]

    for x_start, x_end, era_label, color in era_spans:
        ax.axvspan(x_start, x_end, alpha=0.3, color=color, zorder=0)
        ax.text((x_start + x_end) / 2, y_base - 0.42, era_label,
                fontsize=7.5, ha='center', va='center', color='#555555', fontstyle='italic')

    for year, label, display in releases:
        is_major = label in milestones
        marker_size = 14 if is_major else 8
        color_dot = COLORS[0] if is_major else '#4bacc6'
        ax.plot(year, y_base, 'o', markersize=marker_size, color=color_dot, zorder=3,
                markeredgecolor='white', markeredgewidth=1.5)

    positions_major = {
        '1.0': ('above', 0.20),
        '2.0': ('below', -0.20),
        '3.0': ('above', 0.20),
        '3.2': ('below', -0.20),
        '4.0': ('above', 0.20),
    }

    for year, label, display in releases:
        if label in milestones:
            pos, y_offset = positions_major[label]
            ax.annotate(display, xy=(year, y_base), xytext=(year, y_base + y_offset),
                        fontsize=8, fontweight='bold', ha='center', va='center',
                        color=COLORS[0],
                        arrowprops=dict(arrowstyle='-', color='#999999', lw=0.8))
            milestone_offset = y_offset + (0.20 if pos == 'above' else -0.20)
            ax.text(year, y_base + milestone_offset, milestones[label],
                    fontsize=6.5, ha='center', va='center', color='#333333',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f7fa',
                              edgecolor='#b0bec5', alpha=0.9))
        else:
            ax.annotate(display, xy=(year, y_base), xytext=(year, y_base + 0.11),
                        fontsize=6, ha='center', va='bottom', color='#777777',
                        arrowprops=dict(arrowstyle='-', color='#cccccc', lw=0.5))

    ax.set_xlim(2013.5, 2026.5)
    ax.set_ylim(-0.05, 1.10)
    ax.set_xlabel('Year', fontsize=10, color='#333333')
    ax.set_xticks(range(2014, 2027))
    ax.set_xticklabels([str(y) for y in range(2014, 2027)], fontsize=8)
    ax.set_yticks([])
    ax.set_title('Spring Boot Version Timeline (1.0 -> 4.0)', fontsize=14, fontweight='bold',
                 color=COLORS[0], pad=18)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#cccccc')
    plt.tight_layout()
    path = os.path.join(OUTDIR, 'chart_01.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def generate_chart_02():
    """Runtime Optimization Strategy Comparison"""
    fig, ax = plt.subplots(figsize=(10, 6))

    strategies = ['Standard JVM\n(HotSpot)', 'JVM +\nSpring AOT', 'Project\nLeyden',
                  'Project\nCRaC', 'GraalVM\nNative Image']
    startup_times = [3.5, 3.0, 1.0, 0.05, 0.05]
    peak_throughput = [100, 100, 95, 100, 70]

    x = np.arange(len(strategies))
    width = 0.35

    ax2 = ax.twinx()

    bars1 = ax.bar(x - width / 2, startup_times, width, label='Startup Time (seconds)',
                   color=COLORS[0], alpha=0.85, zorder=3)
    bars2 = ax2.bar(x + width / 2, peak_throughput, width,
                    label='Peak Throughput (relative %)',
                    color=COLORS[2], alpha=0.85, zorder=3)

    for bar, val in zip(bars1, startup_times):
        label_text = f'{val:.1f}s' if val >= 0.1 else f'{int(val * 1000)}ms'
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.12,
                label_text, ha='center', va='bottom', fontsize=8, fontweight='bold',
                color=COLORS[0])

    for bar, val in zip(bars2, peak_throughput):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                 f'{val}%', ha='center', va='bottom', fontsize=8, fontweight='bold',
                 color='#6a8a3a')

    tradeoffs = [
        'Highest memory\nSlow cold start',
        'Minimal\nconstraints',
        'Experimental\nPremain only',
        'Linux-only\nSecret leakage risk',
        'Closed-world\nNo JIT at runtime',
    ]
    for i, note in enumerate(tradeoffs):
        ax.text(i, -1.1, note, ha='center', va='top', fontsize=6.5,
                color='#888888', fontstyle='italic')

    boot_versions = ['All versions', '3.0+', 'Experimental', '3.2+', '3.0+']
    for i, bv in enumerate(boot_versions):
        ax.text(i, -0.35, f'Boot {bv}', ha='center', va='top', fontsize=7,
                color='#1f4e79', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#e8f0fe',
                          edgecolor='none', alpha=0.8))

    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontsize=8.5)
    ax.set_ylabel('Startup Time (seconds)', fontsize=10, color=COLORS[0])
    ax2.set_ylabel('Peak Throughput (relative %)', fontsize=10, color='#6a8a3a')
    ax.set_ylim(-1.8, 5.5)
    ax2.set_ylim(0, 130)

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper center', fontsize=8.5,
              ncol=2, bbox_to_anchor=(0.5, 0.98), framealpha=0.9)

    ax.set_title('Spring Runtime Optimization Strategies Comparison', fontsize=14,
                 fontweight='bold', color=COLORS[0], pad=18)
    ax.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.grid(axis='y', alpha=0.2, zorder=0)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.22)
    path = os.path.join(OUTDIR, 'chart_02.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def generate_chart_03():
    """Virtual Threads vs. Platform Threads Architecture"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    def draw_box(x, y, w, h, text, facecolor='#e8f0fe', edgecolor='#1f4e79',
                 fontsize=8, fontweight='normal', text_color='#1f4e79'):
        rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1',
                                        facecolor=facecolor, edgecolor=edgecolor,
                                        linewidth=1.5, zorder=2)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight, color=text_color, zorder=3)

    # LEFT: Platform Threads (1:1)
    ax.text(2.5, 6.6, 'Platform Threads (1:1 Model)', ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLORS[1])

    pt_colors = ['#f8d7da', '#f5c6cb', '#f1b0b7', '#eda6ad']
    for i in range(4):
        draw_box(0.3 + i * 1.1, 5.2, 1.0, 0.8, f'OS Thread\n#{i + 1}',
                 facecolor=pt_colors[i], edgecolor=COLORS[1], fontsize=7,
                 text_color=COLORS[1])
        draw_box(0.3 + i * 1.1, 3.8, 1.0, 0.8, f'Request\n#{i + 1}',
                 facecolor='#fff3cd', edgecolor='#856404', fontsize=7,
                 text_color='#856404')
        ax.annotate('', xy=(0.8 + i * 1.1, 5.2), xytext=(0.8 + i * 1.1, 4.6),
                    arrowprops=dict(arrowstyle='->', color='#999', lw=1.2))

    ax.text(2.5, 3.2, '1:1 Mapping | ~1 MB stack/thread | Max ~200 concurrent',
            ha='center', va='center', fontsize=7, color='#666', fontstyle='italic')

    # Divider
    ax.plot([4.8, 4.8], [0.5, 6.5], '--', color='#ccc', lw=1.5, zorder=1)

    # RIGHT: Virtual Threads (M:N)
    ax.text(7.5, 6.6, 'Virtual Threads (M:N Model)', ha='center', va='center',
            fontsize=11, fontweight='bold', color=COLORS[0])

    carrier_colors = ['#d6e4f0', '#bdd4e8', '#a4c4e0']
    for i in range(3):
        draw_box(5.3 + i * 1.5, 1.2, 1.2, 0.8, f'Carrier\nThread #{i + 1}',
                 facecolor=carrier_colors[i], edgecolor=COLORS[0],
                 fontsize=7, text_color=COLORS[0], fontweight='bold')

    draw_box(5.6, 0.2, 3.5, 0.6, 'ForkJoinPool (Work-Stealing, FIFO)',
             facecolor='#f5f7fa', edgecolor='#666', fontsize=7.5,
             text_color='#444', fontweight='bold')

    vt_x = [5.15, 5.95, 6.75, 7.55, 8.35, 9.15]
    vt_labels = ['VT #1', 'VT #2', 'VT #3', 'VT #4', 'VT #5', 'VT #N']
    for i, (xp, label) in enumerate(zip(vt_x, vt_labels)):
        fc = '#e8f5e9' if i < 5 else '#f3e5f5'
        ec = '#388e3c' if i < 5 else '#7b1fa2'
        tc = '#2e7d32' if i < 5 else '#6a1b9a'
        draw_box(xp, 5.2, 0.7, 0.8, label, facecolor=fc, edgecolor=ec,
                 fontsize=6.5, text_color=tc)
        req_label = f'Req #{i + 1}' if i < 5 else 'Req #N'
        draw_box(xp, 3.8, 0.7, 0.8, req_label, facecolor='#fff3cd',
                 edgecolor='#856404', fontsize=6.5, text_color='#856404')
        ax.annotate('', xy=(xp + 0.35, 5.2), xytext=(xp + 0.35, 4.6),
                    arrowprops=dict(arrowstyle='->', color='#999', lw=1))

    mappings = [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (5, 2)]
    for vt_idx, carrier_idx in mappings:
        vt_cx = vt_x[vt_idx] + 0.35
        ct_cx = 5.9 + carrier_idx * 1.5
        ax.annotate('', xy=(ct_cx, 2.0), xytext=(vt_cx, 5.2),
                    arrowprops=dict(arrowstyle='->', color=COLORS[0], lw=0.8,
                                   linestyle='dashed', alpha=0.5))

    ax.annotate('Blocking I/O:\nVT unmounts,\ncarrier freed\nfor other VTs',
                xy=(6.5, 3.0), xytext=(5.1, 3.0),
                fontsize=6.5, color='#444', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff9c4',
                          edgecolor='#f9a825', alpha=0.9))

    ax.text(7.5, 2.55, 'M:N Scheduling | ~1 KB stack/VT | Millions concurrent',
            ha='center', va='center', fontsize=7, color='#444', fontstyle='italic')

    ax.set_title('Virtual Threads vs. Platform Threads Architecture', fontsize=14,
                 fontweight='bold', color=COLORS[0], y=1.02)
    plt.tight_layout()
    path = os.path.join(OUTDIR, 'chart_03.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


if __name__ == '__main__':
    generate_chart_01()
    generate_chart_02()
    generate_chart_03()
    print("All charts generated successfully!")
