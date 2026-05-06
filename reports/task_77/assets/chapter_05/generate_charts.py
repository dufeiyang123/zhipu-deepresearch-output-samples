#!/usr/bin/env python3
"""
Chapter 05 Chart Generation Script
Run this script to generate chart_01.png and chart_02.png in the same directory.
Usage: python3 assets/chapter_05/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']


def generate_chart_01():
    """Intervention Strategy x NFC/NFCC Moderation Summary Table"""
    HEADER_BG = '#1f4e79'
    ROW_EVEN = '#eaf0f7'
    ROW_ODD = '#ffffff'

    strategies = [
        'Accuracy Nudge /\nCompetence-building',
        'Debunking\n(Post-hoc correction)',
        'Warning Tags',
        'Source Credibility /\nEpistemic Authority',
        'Self-affirmation',
        'AI Conversational\nIntervention',
        'Prebunking\n(Inoculation)',
    ]
    core_studies = [
        'Rasmussen et al. 2024',
        'Hutmacher et al. 2024',
        'Kaufman et al. 2025',
        'Pica et al. 2021',
        'Saucier et al. 2025',
        'Costello et al. 2024',
        'van Huijstee et al. 2025',
    ]
    nfc_tested = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
    nfc_direction = [
        'Non-significant',
        'Non-significant\n(indep. effect)',
        'Positive\n(\u03b2 = 0.21)',
        'Positive\nmoderation',
        'Included\n(TBD)',
        'Not tested\n(theoretical)',
        'Not tested',
    ]
    construct_used = [
        'NFC\n(possibly NfCog)',
        'NfCog\n(Cacioppo)',
        'NFCC\n(NFC-R 15-item)',
        'NFC\n(Kruglanski)',
        'NFC\n(motivational)',
        'Not measured',
        'Not measured',
    ]
    direction_colors = ['#d4a017', '#d4a017', '#4a7c3f', '#4a7c3f', '#6a6a6a', '#b0413e', '#b0413e']
    nfc_test_colors = ['#4a7c3f' if t == 'Yes' else '#b0413e' for t in nfc_tested]

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis('off')
    n_rows = len(strategies)
    n_cols = 5
    col_widths = [0.20, 0.18, 0.10, 0.20, 0.18]
    col_starts = [0.0]
    for i in range(1, n_cols):
        col_starts.append(col_starts[i - 1] + col_widths[i - 1])
    headers = ['Intervention\nStrategy', 'Core Study', 'NFC\nTested?',
               'NFC Moderation\nDirection', 'Construct /\nScale Used']
    row_height = 0.095
    header_height = 0.08
    top_y = 0.88
    table_left = 0.04

    for j, header in enumerate(headers):
        x = table_left + col_starts[j]
        w = col_widths[j] - 0.004
        rect = FancyBboxPatch((x, top_y), w, header_height,
                               boxstyle='round,pad=0.005',
                               facecolor=HEADER_BG, edgecolor='white', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w / 2, top_y + header_height / 2, header,
                ha='center', va='center', fontsize=10, fontweight='bold',
                color='white', linespacing=1.3)

    all_data = [strategies, core_studies, nfc_tested, nfc_direction, construct_used]
    for i in range(n_rows):
        y = top_y - (i + 1) * row_height
        bg = ROW_EVEN if i % 2 == 0 else ROW_ODD
        for j in range(n_cols):
            x = table_left + col_starts[j]
            w = col_widths[j] - 0.004
            h = row_height - 0.004
            rect = FancyBboxPatch((x, y), w, h,
                                   boxstyle='round,pad=0.003',
                                   facecolor=bg, edgecolor='#cccccc', linewidth=0.8)
            ax.add_patch(rect)
            text = all_data[j][i]
            fontsize, color, fontweight = 9, '#222222', 'normal'
            if j == 0:
                fontweight, color = 'bold', COLORS[0]
            elif j == 2:
                color, fontweight, fontsize = nfc_test_colors[i], 'bold', 10
            elif j == 3:
                color, fontweight, fontsize = direction_colors[i], 'bold', 8.5
            elif j == 4:
                fontsize, color = 8.5, '#444444'
            ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
                    fontsize=fontsize, color=color, fontweight=fontweight, linespacing=1.3)

    ax.text(0.5, 0.98, 'Intervention Strategy \u00d7 NFC/NFCC Moderation Summary',
            ha='center', va='top', fontsize=16, fontweight='bold',
            color=COLORS[0], transform=ax.transAxes)

    legend_y = top_y - (n_rows + 1) * row_height - 0.015
    x_off = 0.10
    for _, c, label in [('\u25cf', '#4a7c3f', 'Positive / Significant'),
                        ('\u25cf', '#d4a017', 'Non-significant / Weak'),
                        ('\u25cf', '#b0413e', 'Not tested'),
                        ('\u25cf', '#6a6a6a', 'To be confirmed')]:
        ax.text(x_off, legend_y, '\u25cf', ha='center', va='center',
                fontsize=14, color=c, fontweight='bold')
        ax.text(x_off + 0.02, legend_y, label, ha='left', va='center',
                fontsize=9, color='#333333')
        x_off += 0.22

    note_y = legend_y - 0.04
    ax.text(table_left, note_y,
            'Note: NfCog = Need for Cognition (Cacioppo); NFCC = Need for Cognitive Closure (Kruglanski);\n'
            '          NFC-R = 15-item revised scale. Illusory truth effect unmoderated by NFC = floor constraint.',
            ha='left', va='top', fontsize=8, color='#666666', style='italic', linespacing=1.5)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(note_y - 0.06, 1.0)

    outpath = os.path.join(OUT_DIR, 'chart_01.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {outpath}")


def generate_chart_02():
    """NFCC Seizing-Freezing Framework: Intervention Strategy Mapping"""
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis('off')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)

    ax.text(7, 8.6, 'NFCC Seizing-Freezing Framework: Intervention Strategy Mapping',
            ha='center', va='center', fontsize=15, fontweight='bold', color=COLORS[0])

    # Central flow
    flow_boxes = [
        (1.5, 5.5, 2.2, 1.0, 'Information\nEnvironment', '#e8eef5', COLORS[0]),
        (5.0, 5.5, 2.0, 1.0, 'SEIZING\nProcess', '#fce4e4', COLORS[1]),
        (8.5, 5.5, 2.2, 1.0, 'Belief\nCrystallization', '#fef5e7', '#d4a017'),
        (11.5, 5.5, 2.0, 1.0, 'FREEZING\nProcess', '#e8f0e4', '#2e7d32'),
    ]
    for (cx, cy, w, h, label, fc, ec) in flow_boxes:
        rect = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                               boxstyle='round,pad=0.12', facecolor=fc,
                               edgecolor=ec, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=11,
                fontweight='bold', color=ec, linespacing=1.3)

    arrow_style = 'Simple,tail_width=6,head_width=18,head_length=10'
    for (x1, x2) in [(2.6, 4.0), (6.0, 7.4), (9.6, 10.5)]:
        arrow = FancyArrowPatch((x1, 5.5), (x2, 5.5), arrowstyle=arrow_style,
                                 color='#888888', linewidth=1.5)
        ax.add_patch(arrow)

    # Top interventions (targeting Seizing)
    top_items = [
        (2.0, 7.8, 'Reduce misinfo\naccessibility\n(Platform design)', COLORS[4]),
        (5.0, 7.8, 'Warning tags\n& source labels\n(Kaufman 2025)', COLORS[0]),
        (8.0, 7.8, 'Accuracy nudge\n& competence\n(Rasmussen 2024)', COLORS[2]),
        (11.0, 7.8, 'Epistemic authority\ncues\n(Pica 2021)', COLORS[3]),
    ]
    for (cx, cy, label, color) in top_items:
        rect = FancyBboxPatch((cx - 1.2, cy - 0.5), 2.4, 1.0,
                               boxstyle='round,pad=0.08', facecolor='white',
                               edgecolor=color, linewidth=2, linestyle='--')
        ax.add_patch(rect)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8.5,
                color=color, fontweight='bold', linespacing=1.25)

    # Arrows from top to Seizing
    targets_top = [(2.0, 2.0), (5.0, 5.0), (8.0, 5.5), (11.0, 5.8)]
    rads = [0.0, 0.0, -0.15, -0.25]
    for idx, ((cx, _cy, _l, color), (_, tgt_x)) in enumerate(zip(top_items, targets_top)):
        kw = {}
        if rads[idx] != 0:
            kw['connectionstyle'] = f'arc3,rad={rads[idx]}'
        arrow = FancyArrowPatch((cx, 7.25), (tgt_x, 6.05),
                                 arrowstyle='->', color=color, linewidth=1.5, **kw)
        ax.add_patch(arrow)

    # Bottom interventions (targeting Freezing)
    bot_items = [
        (2.5, 3.2, 'Alternative explanation\nsupply\n(Guess 2020)', COLORS[1]),
        (5.5, 3.2, 'AI conversational\nintervention\n(Costello 2024)', COLORS[5]),
        (8.5, 3.2, 'Self-affirmation\n(Saucier 2025)', COLORS[3]),
        (11.5, 3.2, 'Prebunking /\nInoculation\n(TBD \u2014 not tested)', '#888888'),
    ]
    for (cx, cy, label, color) in bot_items:
        rect = FancyBboxPatch((cx - 1.2, cy - 0.5), 2.4, 1.0,
                               boxstyle='round,pad=0.08', facecolor='white',
                               edgecolor=color, linewidth=2, linestyle='--')
        ax.add_patch(rect)
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8.5,
                color=color, fontweight='bold', linespacing=1.25)

    # Arrows from bottom to processes
    arrow = FancyArrowPatch((2.5, 3.75), (11.0, 4.95), arrowstyle='->',
                             color=COLORS[1], linewidth=1.5,
                             connectionstyle='arc3,rad=0.25')
    ax.add_patch(arrow)

    arrow = FancyArrowPatch((5.5, 3.75), (5.2, 4.95), arrowstyle='->',
                             color=COLORS[5], linewidth=1.5,
                             connectionstyle='arc3,rad=0.1')
    ax.add_patch(arrow)
    arrow = FancyArrowPatch((6.0, 3.75), (11.2, 4.95), arrowstyle='->',
                             color=COLORS[5], linewidth=1.5,
                             connectionstyle='arc3,rad=0.2')
    ax.add_patch(arrow)

    arrow = FancyArrowPatch((8.5, 3.75), (5.3, 4.95), arrowstyle='->',
                             color=COLORS[3], linewidth=1.5,
                             connectionstyle='arc3,rad=0.15')
    ax.add_patch(arrow)
    arrow = FancyArrowPatch((8.8, 3.75), (11.3, 4.95), arrowstyle='->',
                             color=COLORS[3], linewidth=1.5,
                             connectionstyle='arc3,rad=-0.1')
    ax.add_patch(arrow)

    arrow = FancyArrowPatch((11.5, 3.75), (11.5, 4.95), arrowstyle='->',
                             color='#888888', linewidth=1.5, linestyle='dotted')
    ax.add_patch(arrow)

    # Phase labels
    ax.text(5.0, 4.7, 'Targets Seizing', ha='center', va='center', fontsize=8,
            color=COLORS[1], style='italic', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fce4e4',
                      edgecolor='none', alpha=0.7))
    ax.text(11.5, 4.7, 'Targets Freezing', ha='center', va='center', fontsize=8,
            color='#2e7d32', style='italic', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e8f0e4',
                      edgecolor='none', alpha=0.7))

    # Floor constraint
    rect = FancyBboxPatch((1.5, 1.3), 11, 0.9, boxstyle='round,pad=0.1',
                           facecolor='#fff3e0', edgecolor='#e65100', linewidth=2)
    ax.add_patch(rect)
    ax.text(7, 1.75, 'Floor Constraint: Illusory Truth Effect (repetition) is NOT moderated by NFC',
            ha='center', va='center', fontsize=10, fontweight='bold', color='#e65100')
    ax.text(7, 1.45,
            'De keersmaecker et al. (2020) \u2014 Reducing repetition exposure remains essential',
            ha='center', va='center', fontsize=8, color='#bf360c', style='italic')

    ax.text(1.0, 0.7,
            'Solid border = empirical evidence    Dashed border = theoretical/partial    '
            'Grey = not yet tested',
            ha='left', va='center', fontsize=8, color='#666666', style='italic')

    plt.tight_layout(pad=0.5)
    outpath = os.path.join(OUT_DIR, 'chart_02.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print(f"Saved: {outpath}")


if __name__ == '__main__':
    generate_chart_01()
    generate_chart_02()
    print("All charts generated.")
