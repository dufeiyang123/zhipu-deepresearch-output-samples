"""
Chart generation script for Chapter 01.
Run this script to generate all charts for Chapter 1.
Usage: python3 assets/chapter_01/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Chart 1: ITS Development Timeline (1924–2026)
# ============================================================
def generate_chart_01():
    eras = [
        (1920, 1969, 'CAI Era', COLORS[0]),
        (1970, 1999, 'Classical ITS Era', COLORS[1]),
        (2000, 2027, 'AI / Multimodal Era', COLORS[2]),
    ]
    milestones = [
        (1924, "Pressey's Teaching Machine"),
        (1954, "Skinner's Programmed\nInstruction"),
        (1960, "PLATO System\n(Bitzer, UIUC)"),
        (1970, "SCHOLAR System\n(Carbonell)"),
        (1983, "LISP Tutor\n(Anderson, CMU)"),
        (1984, "Bloom's 2-Sigma Study"),
        (2016, "Kulik & Fletcher\nMeta-Analysis (d=0.66)"),
        (2023, "WHOOP Coach\n(LLM + Sports)"),
        (2026, "Milan-Cortina\nOlympic LLM"),
    ]
    fig, ax = plt.subplots(figsize=(14, 5.5))
    y_band = 0
    band_height = 0.35
    for start, end, label, color in eras:
        ax.barh(y_band, end - start, left=start, height=band_height,
                color=color, alpha=0.15, edgecolor=color, linewidth=1.0)
        mid = (start + end) / 2
        ax.text(mid, y_band - 0.35, label, ha='center', va='top',
                fontsize=9.5, fontweight='bold', color=color)
    ax.plot([1918, 2028], [y_band, y_band], color='#333333', linewidth=2.0, zorder=2)
    for i, (year, label) in enumerate(milestones):
        if i % 2 == 0:
            y_text = 0.85 + (0.4 if i % 4 == 0 else 0.0)
            va = 'bottom'
        else:
            y_text = -0.85 - (0.4 if i % 4 == 1 else 0.0)
            va = 'top'
        ax.plot(year, y_band, 'o', color=COLORS[0], markersize=7, zorder=5,
                markeredgecolor='white', markeredgewidth=1.0)
        ax.annotate(f"{year}: {label}", xy=(year, y_band), xytext=(year, y_text),
                    fontsize=7.8, ha='center', va=va,
                    arrowprops=dict(arrowstyle='-', color='#999999', lw=0.7),
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                              edgecolor='#cccccc', alpha=0.92))
    ax.set_title('Evolution of Intelligent Tutoring Systems: Key Milestones (1924\u20132026)',
                 fontsize=13, fontweight='bold', pad=18, color='#1f4e79')
    ax.set_xlim(1915, 2032)
    ax.set_ylim(-2.2, 2.2)
    ax.set_xlabel('Year', fontsize=10)
    ax.get_yaxis().set_visible(False)
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'chart_01.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")

# ============================================================
# Chart 2: Three Waves of Sports Sensing Technology (1997–2025)
# ============================================================
def generate_chart_02():
    waves = {
        'Wave 1: Optical Tracking': {
            'color': COLORS[0], 'y': 2,
            'milestones': [
                (1997, 'Prozone\n(EPL: Derby County)'),
                (2001, 'Hawk-Eye\n(Cricket)'),
                (2006, 'Hawk-Eye\n(Tennis)'),
                (2013, 'SportVU\n(All 30 NBA arenas)'),
            ]
        },
        'Wave 2: Wearable IMU Sensors': {
            'color': COLORS[1], 'y': 1,
            'milestones': [
                (2006, 'Catapult minimaXx\n(AFL adoption)'),
                (2020, 'Catapult Vector S7\n(1kHz accel, UWB)'),
                (2025, 'STATSports Apex 2.0\n(RTK, cm accuracy)'),
            ]
        },
        'Wave 3: AI Pose Estimation': {
            'color': COLORS[2], 'y': 0,
            'milestones': [
                (2017, 'CMU OpenPose\n(Open-source HPE)'),
                (2020, 'Google MediaPipe\n(Mobile/embedded)'),
                (2023, 'WHOOP Coach\n(LLM integration)'),
            ]
        },
    }
    fig, ax = plt.subplots(figsize=(14, 7))
    for wave_name, wd in waves.items():
        y, color = wd['y'], wd['color']
        ax.axhspan(y - 0.35, y + 0.35, color=color, alpha=0.06, zorder=0)
        ax.plot([1995, 2027], [y, y], color=color, linewidth=2.0, alpha=0.5, zorder=1)
        ax.text(1994.5, y, wave_name, ha='right', va='center', fontsize=9.5,
                fontweight='bold', color=color, style='italic')
        for j, (year, label) in enumerate(wd['milestones']):
            ax.plot(year, y, 'o', color=color, markersize=9, zorder=5,
                    markeredgecolor='white', markeredgewidth=1.2)
            y_offset = 0.50 if j % 2 == 0 else -0.50
            va = 'bottom' if j % 2 == 0 else 'top'
            ax.annotate(f"{year}\n{label}", xy=(year, y),
                        xytext=(year, y + y_offset), fontsize=7.5, ha='center', va=va,
                        arrowprops=dict(arrowstyle='-', color='#aaaaaa', lw=0.6),
                        bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                                  edgecolor=color, alpha=0.90, linewidth=0.8))
    ax.annotate('Convergence\n\u2192 Sports-ITS', xy=(2026, 1), xytext=(2028.5, 1),
                fontsize=10, fontweight='bold', ha='left', va='center', color=COLORS[3],
                arrowprops=dict(arrowstyle='->', color=COLORS[3], lw=2.0),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0ebf5',
                          edgecolor=COLORS[3], linewidth=1.2))
    ax.set_title('Three Waves of Sports Sensing Technology (1997\u20132025)',
                 fontsize=13, fontweight='bold', pad=16, color='#1f4e79')
    ax.set_xlim(1980, 2031)
    ax.set_ylim(-0.9, 3.0)
    ax.set_xlabel('Year', fontsize=10)
    ax.get_yaxis().set_visible(False)
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, 'chart_02.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")

# ============================================================
# Chart 3: Market Convergence Diagram
# ============================================================
def generate_chart_03():
    fig = plt.figure(figsize=(12, 7))
    ax_left = fig.add_axes([0.08, 0.20, 0.38, 0.60])
    ax_right = fig.add_axes([0.56, 0.20, 0.38, 0.60])

    # Left: Sports Analytics Market
    bars1 = ax_left.bar([0, 2], [5.68, 23.15], width=0.4, color=COLORS[0], alpha=0.85,
                         label='Grand View Research\n(broad scope)', edgecolor='white', linewidth=0.5)
    bars2 = ax_left.bar([0.45, 1.45], [2.29, 4.75], width=0.4, color=COLORS[4], alpha=0.85,
                         label='MarketsandMarkets\n(narrow scope)', edgecolor='white', linewidth=0.5)
    for bar in bars1:
        h = bar.get_height()
        ax_left.text(bar.get_x() + bar.get_width()/2, h + 0.4, f'${h:.1f}B',
                     ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[0])
    for bar in bars2:
        h = bar.get_height()
        ax_left.text(bar.get_x() + bar.get_width()/2, h + 0.4, f'${h:.1f}B',
                     ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLORS[4])
    ax_left.set_xticks([0.22, 1.45, 2])
    ax_left.set_xticklabels(['2025', '2030', '2033'], fontsize=9)
    ax_left.set_ylabel('Market Size (USD Billions)', fontsize=9.5)
    ax_left.set_title('Sports Analytics Market', fontsize=11, fontweight='bold', color=COLORS[0], pad=10)
    ax_left.set_ylim(0, 28)
    ax_left.legend(fontsize=7.5, loc='upper left', framealpha=0.9)
    ax_left.spines['top'].set_visible(False)
    ax_left.spines['right'].set_visible(False)
    ax_left.annotate('CAGR 18.5%\n(2026\u20132033)', xy=(1.1, 14), fontsize=8.5, ha='center',
                     color=COLORS[0], fontstyle='italic',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f0f8', edgecolor=COLORS[0], alpha=0.7))
    ax_left.annotate('CAGR 15.7%\n(2025\u20132030)', xy=(1.1, 10.5), fontsize=8.5, ha='center',
                     color=COLORS[4], fontstyle='italic',
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#e6f5f8', edgecolor=COLORS[4], alpha=0.7))

    # Right: AI in Education Market
    bars3 = ax_right.bar([0, 1], [2.21, 5.82], width=0.5, color=COLORS[1], alpha=0.85,
                          edgecolor='white', linewidth=0.5)
    for bar in bars3:
        h = bar.get_height()
        ax_right.text(bar.get_x() + bar.get_width()/2, h + 0.12, f'${h:.1f}B',
                      ha='center', va='bottom', fontsize=10, fontweight='bold', color=COLORS[1])
    ax_right.set_xticks([0, 1])
    ax_right.set_xticklabels(['2024', '2030'], fontsize=9)
    ax_right.set_ylabel('Market Size (USD Billions)', fontsize=9.5)
    ax_right.set_title('AI in Education Market', fontsize=11, fontweight='bold', color=COLORS[1], pad=10)
    ax_right.set_ylim(0, 8)
    ax_right.spines['top'].set_visible(False)
    ax_right.spines['right'].set_visible(False)
    ax_right.annotate('CAGR 17.5%\n(2024\u20132030)', xy=(0.5, 5.2), fontsize=8.5, ha='center',
                      color=COLORS[1], fontstyle='italic',
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='#fce8e6', edgecolor=COLORS[1], alpha=0.7))

    fig.text(0.50, 0.04,
             'Sports-ITS = Intersection of Sports Analytics + AI in Education  |  '
             'China Smart Fitness Market: ~RMB 140B (~$20B) by 2026',
             ha='center', va='center', fontsize=9.5, fontweight='bold', color=COLORS[3],
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0ebf5', edgecolor=COLORS[3], linewidth=1.5))
    fig.suptitle('Market Convergence: Sports Analytics \u00d7 AI in Education \u2192 Sports-ITS',
                 fontsize=13.5, fontweight='bold', y=0.97, color='#1f4e79')
    path = os.path.join(OUT_DIR, 'chart_03.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


if __name__ == '__main__':
    generate_chart_01()
    generate_chart_02()
    generate_chart_03()
    print("All charts generated successfully.")
