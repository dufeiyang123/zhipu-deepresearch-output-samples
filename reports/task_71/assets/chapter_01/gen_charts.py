#!/usr/bin/env python3
"""
Generate Chapter 01 charts for the AIGC in K-12 Education report.
Run this script from the project root to produce chart PNGs in assets/chapter_01/.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
from matplotlib.lines import Line2D
from datetime import datetime
import numpy as np
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']


def chart_01():
    """AIGC-in-K-12 Milestone Timeline (2022–2026)"""
    milestones = [
        (datetime(2022, 11, 30), "ChatGPT Launch", "Technology"),
        (datetime(2023, 1, 15),  "NYC Ban", "Policy"),
        (datetime(2023, 3, 14),  "GPT-4 & Khanmigo", "Technology"),
        (datetime(2023, 5, 15),  "USDOE Report", "Policy"),
        (datetime(2023, 7, 13),  "China GenAI Regs", "Policy"),
        (datetime(2023, 9, 7),   "UNESCO Guidance", "Policy"),
        (datetime(2024, 2, 2),   "EU AI Act", "Policy"),
        (datetime(2024, 12, 1),  "China 184 AI Bases", "Deployment"),
        (datetime(2025, 5, 13),  "China MOE Guide", "Policy"),
        (datetime(2025, 9, 1),   "China Mandatory AI", "Deployment"),
        (datetime(2025, 9, 30),  "RAND: 53% Teachers", "Research"),
        (datetime(2025, 10, 15), "TALIS: 41% Teachers", "Research"),
        (datetime(2026, 1, 28),  "OpenAI Edu Countries", "Technology"),
    ]
    cat_colors = {"Technology": COLORS[0], "Policy": COLORS[1],
                  "Deployment": COLORS[2], "Research": COLORS[3]}

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axhline(y=0, color='#555', linewidth=1.5, zorder=1)

    a_i, b_i = 0, 0
    for i, (date, label, cat) in enumerate(milestones):
        color = cat_colors[cat]
        if i % 2 == 0:
            y = 1.2 + (a_i % 3) * 1.0; a_i += 1; va = 'bottom'
        else:
            y = -(1.2 + (b_i % 3) * 1.0); b_i += 1; va = 'top'
        ax.plot([date, date], [0, y * 0.85], color=color, lw=0.7, zorder=2)
        ax.scatter(date, 0, s=20, color=color, zorder=3, edgecolors='w', linewidth=0.3)
        ax.text(mdates.date2num(date), y * 0.85, label, fontsize=6.5, ha='center',
                va=va, color=color, fontweight='bold')

    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.set_xlim(datetime(2022, 10, 1), datetime(2026, 4, 1))
    ax.tick_params(axis='x', labelsize=7)
    ax.set_ylim(-5, 5)
    ax.yaxis.set_visible(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(axis='x', length=0)

    legend_elements = [Line2D([0], [0], marker='o', color='w',
                              markerfacecolor=cat_colors[c], markersize=5, label=c)
                       for c in cat_colors]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=6, framealpha=0.9, ncol=4)
    ax.set_title("AIGC in K-12 Education: Key Milestones (Nov 2022 – Early 2026)",
                 fontsize=10, fontweight='bold', pad=12, color='#1f4e79')
    plt.tight_layout()
    path = os.path.join(OUTDIR, 'chart_01.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {path}")


def chart_02():
    """Global Teacher AI Adoption Comparison Chart"""
    countries = ['UAE', 'Singapore', 'U.S.\n(RAND)', 'UK\n(DfE)', 'OECD\nAvg.', 'France']
    rates = [75, 75, 53, 44, 39, 14]
    sources = ['TALIS 2024', 'TALIS 2024', 'RAND 2025', 'DfE 2024-25', 'TALIS 2024', 'TALIS 2024']

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    bars = ax.bar(countries, rates, color=COLORS[:len(countries)], width=0.6,
                  edgecolor='white', linewidth=0.5)
    for bar, rate in zip(bars, rates):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., h + 1.5,
                f'{rate}%', ha='center', va='bottom', fontsize=9,
                fontweight='bold', color='#333333')
    for bar, src in zip(bars, sources):
        ax.text(bar.get_x() + bar.get_width() / 2., -5,
                src, ha='center', va='top', fontsize=6, color='#777777', style='italic')

    ax.set_ylabel('Teacher AI Adoption Rate (%)', fontsize=9, color='#333333')
    ax.set_ylim(0, 90)
    ax.set_xlim(-0.6, len(countries) - 0.4)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#999999')
    ax.set_axisbelow(True)
    ax.set_title("Global K-12 Teacher AI Adoption Rates by Country/System",
                 fontsize=11, fontweight='bold', pad=15, color='#1f4e79')
    ax.text(0.5, 1.02, "Sources: OECD TALIS 2024, RAND 2025, UK DfE 2024-25",
            transform=ax.transAxes, ha='center', fontsize=7, color='#888888', style='italic')
    plt.subplots_adjust(bottom=0.18)
    plt.tight_layout()
    path = os.path.join(OUTDIR, 'chart_02.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {path}")


def chart_03():
    """Dual-Axis Taxonomy Framework Diagram"""
    functions = [
        "Content Generation\n& Lesson Prep",
        "Personalized Tutoring\n& Adaptive Learning",
        "Assessment, Feedback\n& Evaluation",
        "Creative Expression\n& Multimodal Production",
        "AI Literacy &\nComputational Thinking"
    ]
    stakeholders = ["Teacher-Facing", "Student-Facing", "System-Facing"]
    matrix = np.array([
        [1.0, 0.3, 0.0],
        [0.3, 1.0, 0.0],
        [0.7, 0.7, 0.0],
        [0.0, 1.0, 0.0],
        [0.3, 0.3, 1.0],
    ])
    tools = [
        ["ChatGPT, Gemini\n(lesson plans)", "", ""],
        ["", "Khanmigo,\nMathGPT", ""],
        ["Gradescope,\nformative AI", "Auto-feedback\ntools", ""],
        ["", "DALL-E, Suno,\nCopilot (code)", ""],
        ["", "", "MOE curricula,\nAI literacy courses"],
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    n_rows, n_cols = len(functions), len(stakeholders)
    cell_w, cell_h = 2.0, 1.0
    ml, mb = 3.5, 0.5

    for i in range(n_rows):
        for j in range(n_cols):
            x = ml + j * cell_w
            y = mb + (n_rows - 1 - i) * cell_h
            val = matrix[i][j]
            if val >= 0.7:
                color, alpha = COLORS[0], 0.7
            elif val >= 0.3:
                color, alpha = COLORS[4], 0.35
            else:
                color, alpha = '#f0f0f0', 0.5
            rect = mpatches.FancyBboxPatch((x, y), cell_w, cell_h,
                                            boxstyle="round,pad=0.05",
                                            facecolor=color, alpha=alpha,
                                            edgecolor='#999999', linewidth=0.5)
            ax.add_patch(rect)
            tool = tools[i][j]
            if tool:
                ax.text(x + cell_w / 2, y + cell_h / 2, tool,
                        ha='center', va='center', fontsize=5.5, color='#222222',
                        linespacing=1.2)

    for i, func in enumerate(functions):
        y = mb + (n_rows - 1 - i) * cell_h + cell_h / 2
        ax.text(ml - 0.2, y, func, ha='right', va='center',
                fontsize=7, fontweight='bold', color='#333333', linespacing=1.1)
    for j, sh in enumerate(stakeholders):
        x = ml + j * cell_w + cell_w / 2
        y = mb + n_rows * cell_h + 0.15
        ax.text(x, y, sh, ha='center', va='bottom', fontsize=8,
                fontweight='bold', color='#1f4e79')

    ax.text(ml + n_cols * cell_w / 2, mb + n_rows * cell_h + 0.65,
            "Stakeholder Role Axis", ha='center', fontsize=9,
            fontweight='bold', color='#333')
    ax.text(-0.1, mb + n_rows * cell_h / 2,
            "Pedagogical Function Axis", ha='center', va='center', fontsize=9,
            fontweight='bold', color='#333', rotation=90)
    ax.set_title("Dual-Axis Taxonomic Framework for AIGC in K-12 Education",
                 fontsize=11, fontweight='bold', pad=25, color='#1f4e79')

    legend_elements = [
        mpatches.Patch(facecolor=COLORS[0], alpha=0.7, label='Primary stakeholder'),
        mpatches.Patch(facecolor=COLORS[4], alpha=0.35, label='Secondary stakeholder'),
        mpatches.Patch(facecolor='#f0f0f0', alpha=0.5, edgecolor='#999', label='Not primary'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=6.5,
              framealpha=0.9, edgecolor='#cccccc')
    ax.set_xlim(-0.8, ml + n_cols * cell_w + 0.3)
    ax.set_ylim(0, mb + n_rows * cell_h + 1.2)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    path = os.path.join(OUTDIR, 'chart_03.png')
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {path}")


if __name__ == '__main__':
    chart_01()
    chart_02()
    chart_03()
    print("All charts generated.")
