#!/usr/bin/env python3
"""
Generate Chapter 05 charts for the AIGC in K-12 Education report.
Run this script from the project root to produce chart PNGs in assets/chapter_05/.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']


def chart_01():
    """Risk-Severity Assessment Matrix (Heatmap)"""
    risk_domains = [
        'Academic Integrity &\nCognitive Over-Reliance',
        'Data Privacy &\nChild Protection',
        'Equity, Access &\nAlgorithmic Bias',
        'Teacher Identity &\nWorkforce Dynamics'
    ]
    severity_dims = ['Prevalence', 'Documented\nHarm Severity', 'Policy\nPreparedness Gap']

    scores = np.array([
        [4, 3, 4],
        [3, 4, 3],
        [3, 3, 4],
        [4, 2, 3],
    ])

    annotations = [
        ['84% students\nuse AI;\n62% for HW', '-17% exam\nperformance;\n67% worry', 'Only 45%\nhave policies;\n7% permit AI'],
        ['23% breaches;\n13% deepfake\nbullying', 'Child harm\nincidents;\n12% NCII', 'COPPA gap\n13-17; EU age\nvaries 13-16'],
        ['81% vs 58%\nincome gap;\n79% vs 66%', 'Racial bias\nin AI tools;\n0 Africa studies', '2x policy gap\nprivate vs\npublic schools'],
        ['75% cite\nskill deficit;\n53% use AI', '31% less\nconnected;\n50% distrust', '67% vs 39%\ntraining gap;\nDIY common'],
    ]

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('risk', ['#9bbb59', '#f7dc6f', '#e67e22', '#c0504d'], N=4)

    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(scores, cmap=cmap, vmin=1, vmax=4, aspect='auto')

    ax.set_xticks(np.arange(3))
    ax.set_yticks(np.arange(4))
    ax.set_xticklabels(severity_dims, fontsize=10, fontweight='bold')
    ax.set_yticklabels(risk_domains, fontsize=9.5, fontweight='bold')
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    for i in range(4):
        for j in range(3):
            c = 'white' if scores[i, j] >= 3 else '#333333'
            ax.text(j, i, annotations[i][j], ha='center', va='center',
                    fontsize=7.8, color=c, linespacing=1.25)

    for i in range(5):
        ax.axhline(i - 0.5, color='white', linewidth=2.5)
    for j in range(4):
        ax.axvline(j - 0.5, color='white', linewidth=2.5)

    cbar = fig.colorbar(im, ax=ax, shrink=0.6, pad=0.03, ticks=[1, 2, 3, 4])
    cbar.set_ticklabels(['Low', 'Moderate', 'High', 'Very High'], fontsize=9)
    cbar.ax.tick_params(size=0)
    cbar.set_label('Concern Level', fontsize=10, labelpad=8)

    ax.set_title('K-12 AIGC Risk-Severity Assessment Matrix', fontsize=13, fontweight='bold', pad=18)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'chart_01.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: chart_01.png")


def chart_02():
    """GDPR Digital Age of Consent: Regulatory Fragmentation"""
    age_groups = {
        'Age 13': ['Belgium', 'Denmark', 'Estonia', 'Finland', 'Latvia',
                    'Malta', 'Portugal', 'Sweden', 'UK'],
        'Age 14': ['Austria', 'Bulgaria', 'Cyprus', 'Italy', 'Lithuania', 'Spain'],
        'Age 15': ['Czech Rep.', 'France', 'Greece'],
        'Age 16\n(GDPR default)': ['Croatia', 'Germany', 'Hungary', 'Ireland',
                                    'Luxembourg', 'Netherlands', 'Poland',
                                    'Romania', 'Slovakia']
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    group_colors = ['#9bbb59', '#4bacc6', '#f79646', '#c0504d']
    y_positions = []
    bar_widths = []
    bar_colors = []

    for idx, (age, countries) in enumerate(age_groups.items()):
        bar_widths.append(len(countries))
        bar_colors.append(group_colors[idx])
        y_positions.append(idx)

    bars = ax.barh(y_positions, bar_widths, color=bar_colors, height=0.6,
                   edgecolor='white', linewidth=1.5)

    for idx, (age, countries) in enumerate(age_groups.items()):
        count = len(countries)
        country_str = ', '.join(countries)
        ax.text(count + 0.3, y_positions[idx], country_str,
                va='center', ha='left', fontsize=7.5, color='#333333', style='italic')
        ax.text(count / 2, y_positions[idx], str(count),
                va='center', ha='center', fontsize=14, fontweight='bold', color='white')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(list(age_groups.keys()), fontsize=11, fontweight='bold')
    ax.set_xlabel('Number of EU/EEA Countries', fontsize=11, fontweight='bold')
    ax.set_xlim(0, 26)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_title('GDPR Digital Age of Consent: Regulatory Fragmentation\nacross EU/EEA Member States',
                 fontsize=13, fontweight='bold', pad=15)

    fig.text(0.12, 0.02,
             'Note: EdTech platforms serving European schools must navigate up to 27 different consent thresholds.\n'
             'Source: EuConsent / GDPR Article 8',
             fontsize=8, color='#666666', style='italic')

    plt.tight_layout(rect=[0, 0.06, 1, 1])
    plt.savefig(os.path.join(OUTDIR, 'chart_02.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: chart_02.png")


def chart_03():
    """AI-in-Schools Risk Ecosystem: Interconnected Challenges"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.axis('off')

    positions = {
        'Academic\nIntegrity': (0, 1.0),
        'Data Privacy\n& Child Safety': (1.2, 0),
        'Equity &\nBias': (0, -1.0),
        'Teacher Identity\n& Workforce': (-1.2, 0),
    }

    node_colors = [COLORS[0], COLORS[1], COLORS[2], COLORS[3]]
    node_keys = list(positions.keys())

    from matplotlib.patches import FancyBboxPatch
    for idx, (label, (x, y)) in enumerate(positions.items()):
        bbox = FancyBboxPatch((x - 0.45, y - 0.28), 0.9, 0.56,
                              boxstyle='round,pad=0.08',
                              facecolor=node_colors[idx], edgecolor='white',
                              linewidth=2, alpha=0.9)
        ax.add_patch(bbox)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

    connections = [
        (0, 1, 'AI detection\nincreases data\ncollection', 0.3),
        (1, 2, 'Deepfake NCII\ndisproportionately\naffects vulnerable', 0.3),
        (2, 3, 'Under-resourced\nschools lack\nteacher training', 0.3),
        (3, 0, 'Untrained teachers\ncannot guide\nAI-literate use', 0.3),
        (0, 2, 'False accusations\nharm minority\nstudents', -0.15),
        (1, 3, 'Monitoring burden\nerodes teacher\nautonomy', -0.15),
    ]

    for from_idx, to_idx, label, curve in connections:
        x1, y1 = positions[node_keys[from_idx]]
        x2, y2 = positions[node_keys[to_idx]]
        dx, dy = x2 - x1, y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        shrink = 0.48
        sx1 = x1 + dx * shrink / dist
        sy1 = y1 + dy * shrink / dist
        sx2 = x2 - dx * shrink / dist
        sy2 = y2 - dy * shrink / dist

        is_diagonal = abs(from_idx - to_idx) == 2
        if is_diagonal:
            arrow_color, alpha, lw = '#999999', 0.5, 1.2
        else:
            arrow_color, alpha, lw = '#555555', 0.7, 1.8

        style = f'arc3,rad={curve}'
        ax.annotate('', xy=(sx2, sy2), xytext=(sx1, sy1),
                     arrowprops=dict(arrowstyle='->', color=arrow_color,
                                     connectionstyle=style, lw=lw, alpha=alpha))

        mx = (sx1 + sx2) / 2 + curve * (sy2 - sy1) / dist * 0.5
        my = (sy1 + sy2) / 2 - curve * (sx2 - sx1) / dist * 0.5

        ax.text(mx, my, label, ha='center', va='center',
                fontsize=6.5, color='#444444', style='italic',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                          edgecolor='#cccccc', alpha=0.85))

    ax.text(0, 0, 'Interconnected\nRisk\nEcosystem', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#333333',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0',
                      edgecolor='#999999', linewidth=1.5))

    ax.set_title('AI-in-Schools Risk Ecosystem: Interconnected Challenges',
                 fontsize=13, fontweight='bold', pad=15)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, 'chart_03.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: chart_03.png")


if __name__ == '__main__':
    chart_01()
    chart_02()
    chart_03()
    print("All Chapter 05 charts generated successfully.")
