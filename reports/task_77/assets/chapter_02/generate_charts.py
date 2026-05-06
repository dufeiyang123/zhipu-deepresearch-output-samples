#!/usr/bin/env python3
"""
Chapter 02 Chart Generation Script
Generates chart_01.png (dual-process framework) and chart_02.png (evidence comparison table)
Usage: python3 assets/chapter_02/generate_charts.py
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
C_DARK_BLUE = '#1f4e79'
C_RED = '#c0504d'
C_GREEN = '#9bbb59'
C_PURPLE = '#8064a2'
C_TEAL = '#4bacc6'
C_ORANGE = '#f79646'
C_LIGHT_BLUE = '#d6e4f0'
C_LIGHT_RED = '#f2dcdb'
C_LIGHT_GREEN = '#ebf1de'
C_LIGHT_PURPLE = '#e4dfec'
C_LIGHT_TEAL = '#daeef3'
C_LIGHT_ORANGE = '#fde9d9'


def generate_chart_01():
    """Dual-process theory framework with NFC positioning."""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(6, 8.1, '错误信息接受的双过程理论框架与NFC定位',
            fontsize=16, fontweight='bold', ha='center', va='center', color=C_DARK_BLUE)

    # Information Input
    box = FancyBboxPatch((4.3, 7.0), 3.4, 0.7, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_BLUE, edgecolor=C_DARK_BLUE, linewidth=2)
    ax.add_patch(box)
    ax.text(6, 7.35, '信息输入（新闻标题）', fontsize=11, fontweight='bold',
            ha='center', va='center', color=C_DARK_BLUE)

    # System 1
    box = FancyBboxPatch((1.0, 5.0), 4.2, 1.2, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_ORANGE, edgecolor=C_ORANGE, linewidth=2)
    ax.add_patch(box)
    ax.text(3.1, 5.85, 'System 1（直觉加工）', fontsize=11, fontweight='bold',
            ha='center', va='center', color=C_ORANGE)
    ax.text(3.1, 5.35, '自动·快速·启发式依赖\n来源熟悉度 / 情感唤起 / 叙事流畅性',
            fontsize=8.5, ha='center', va='center', color='#555555')

    # System 2
    box = FancyBboxPatch((6.8, 5.0), 4.2, 1.2, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_GREEN, edgecolor=C_GREEN, linewidth=2)
    ax.add_patch(box)
    ax.text(8.9, 5.85, 'System 2（分析加工）', fontsize=11, fontweight='bold',
            ha='center', va='center', color='#5a7a1e')
    ax.text(8.9, 5.35, '审慎·缓慢·反思性校正\n内容可信度评估 / 竞争性假设生成',
            fontsize=8.5, ha='center', va='center', color='#555555')

    # Arrows from info
    ax.annotate('', xy=(3.1, 6.25), xytext=(5.2, 6.95),
                arrowprops=dict(arrowstyle='->', color=C_ORANGE, lw=1.8,
                              connectionstyle='arc3,rad=0.12'))
    ax.annotate('', xy=(8.9, 6.25), xytext=(6.8, 6.95),
                arrowprops=dict(arrowstyle='->', color=C_GREEN, lw=1.8,
                              connectionstyle='arc3,rad=-0.12'))

    # NFC Box
    box = FancyBboxPatch((3.8, 3.1), 4.4, 1.5, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_RED, edgecolor=C_RED, linewidth=2.5)
    ax.add_patch(box)
    ax.text(6, 4.2, 'NFC（认知闭合需要）', fontsize=12, fontweight='bold',
            ha='center', va='center', color=C_RED)
    ax.text(6, 3.7, 'Seizing: 加速System 1判断  |  信息量↓  竞争假设↓  主观自信↑',
            fontsize=8.2, ha='center', va='center', color='#555555')
    ax.text(6, 3.35, 'Freezing: 抑制System 2校正  |  抵制不一致信息的修正',
            fontsize=8.2, ha='center', va='center', color='#555555')

    # NFC -> System 1 (enhance)
    ax.annotate('Seizing\n增强', xy=(3.1, 4.95), xytext=(4.5, 4.65),
                fontsize=8.5, fontweight='bold', color=C_RED, ha='center',
                arrowprops=dict(arrowstyle='->', color=C_RED, lw=2.2))
    # NFC -> System 2 (suppress)
    ax.annotate('Freezing\n抑制', xy=(8.9, 4.95), xytext=(7.5, 4.65),
                fontsize=8.5, fontweight='bold', color=C_RED, ha='center',
                arrowprops=dict(arrowstyle='->', color=C_RED, lw=2.2, ls='--'))

    # Lazy hypothesis
    box = FancyBboxPatch((0.3, 1.2), 3.5, 1.5, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_TEAL, edgecolor=C_TEAL, linewidth=1.8)
    ax.add_patch(box)
    ax.text(2.05, 2.3, '"懒惰"假说', fontsize=10.5, fontweight='bold',
            ha='center', va='center', color='#2a7f8f')
    ax.text(2.05, 1.7, 'System 2 不足 → 错误信息接受\nCRT↑ → 辨别力↑ (两端均成立)\nPennycook & Rand 2019',
            fontsize=8, ha='center', va='center', color='#555555')

    # Motivated reasoning
    box = FancyBboxPatch((8.2, 1.2), 3.5, 1.5, boxstyle="round,pad=0.15",
                         facecolor=C_LIGHT_PURPLE, edgecolor=C_PURPLE, linewidth=1.8)
    ax.add_patch(box)
    ax.text(9.95, 2.3, '"动机推理"假说', fontsize=10.5, fontweight='bold',
            ha='center', va='center', color=C_PURPLE)
    ax.text(9.95, 1.7, 'System 2 被身份动机"劫持"\nCRT↑ → 极化↑ (身份议题)\nKahan 2013',
            fontsize=8, ha='center', va='center', color='#555555')

    # Tension arrow
    ax.annotate('', xy=(3.85, 1.95), xytext=(8.15, 1.95),
                arrowprops=dict(arrowstyle='<->', color='#888888', lw=1.8, ls='-.'))
    ax.text(6, 2.15, '核心理论张力', fontsize=9, ha='center', va='center',
            color='#888888', fontweight='bold', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.8))

    # Bottom cognitive biases
    for x, w, title, desc, fc, ec in [
        (0.3, 3.5, '真相错觉效应', 'NFC 不调节 (绕过 seizing/freezing)', '#f5f5f5', '#999999'),
        (4.25, 3.5, '情感因素', '焦虑/威胁 → 情境性NFC↑ → S2抑制', C_LIGHT_ORANGE, C_ORANGE),
        (8.2, 3.5, '确认偏误', 'NFC × 身份动机 → 放大偏见', C_LIGHT_PURPLE, C_PURPLE),
    ]:
        box = FancyBboxPatch((x, 0.0), w, 0.9, boxstyle="round,pad=0.1",
                             facecolor=fc, edgecolor=ec, linewidth=1.3, linestyle='--')
        ax.add_patch(box)
        ax.text(x + w/2, 0.6, title, fontsize=9, fontweight='bold',
                ha='center', va='center', color='#666666')
        ax.text(x + w/2, 0.25, desc, fontsize=7.5, ha='center', va='center', color='#888888')

    plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.02)
    plt.savefig(os.path.join(OUT_DIR, 'chart_01.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Saved chart_01.png")


def generate_chart_02():
    """Evidence comparison table for lazy vs. biased hypotheses."""
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis('off')

    ax.text(0.5, 0.97, '"懒惰"假说 vs. "动机推理"假说：关键实证证据对比',
            fontsize=14, fontweight='bold', ha='center', va='center',
            transform=ax.transAxes, color=C_DARK_BLUE)

    columns = ['维度', 'Pennycook & Rand\n(2019, Cognition)', 'Bago, Rand &\nPennycook (2020, JEP:G)', 'Kahan\n(2013, JDM)']
    data = [
        ['假说归属', '"懒惰"假说', '"懒惰"假说（因果证据）', '"动机推理"假说'],
        ['样本量', 'N = 3,446\n(MTurk)', 'N = 1,635\n(MTurk)', 'N = 1,750'],
        ['核心测量', 'CRT\n(认知反思测试)', '双反应范式\n(时间压力+认知负荷)', 'CRT +\n意识形态量表'],
        ['关键发现', 'CRT↑ → 假新闻辨别力↑\n政治光谱两端均成立', '深思熟虑显著降低\n假新闻信念\n(b=0.36, p<.0001)', 'CRT↑ → 意识形态动机\n推理更强\n(高能力者更极化)'],
        ['政治一致性\n交互', '无显著差异\n(两端均受益)', '无显著交互\n(b=0.004, p=.96)', '对称存在\n(自由派与保守派)'],
        ['对S2的解读', 'S2帮助识别\n不可信内容', 'S2纠正S1直觉错误\n不增加党派偏见', 'S2被"劫持"服务于\n身份保护动机'],
        ['适用情境', '一般性假新闻标题', '一般性假新闻标题', '高度政治化\n科学争议'],
    ]

    n_rows = len(data)
    n_cols = len(columns)

    table_top = 0.88
    row_height = 0.098
    col_widths = [0.14, 0.27, 0.27, 0.27]
    col_starts = [0.025]
    for i in range(1, n_cols):
        col_starts.append(col_starts[i-1] + col_widths[i-1] + 0.01)

    # Header
    for j in range(n_cols):
        rect = plt.Rectangle((col_starts[j], table_top), col_widths[j], row_height,
                              transform=ax.transAxes, facecolor=C_DARK_BLUE,
                              edgecolor='white', linewidth=1.5, clip_on=False)
        ax.add_patch(rect)
        ax.text(col_starts[j] + col_widths[j]/2, table_top + row_height/2,
                columns[j], fontsize=9, fontweight='bold', ha='center', va='center',
                transform=ax.transAxes, color='white')

    col_colors = ['#f0f0f0', '#e8f4f8', '#e8f4f8', '#ece4f0']
    alt_colors = ['#f8f8f8', '#f0f9fc', '#f0f9fc', '#f4eef8']

    for i, row in enumerate(data):
        row_y = table_top - (i + 1) * row_height
        for j in range(n_cols):
            bg = col_colors[j] if i % 2 == 0 else alt_colors[j]
            rect = plt.Rectangle((col_starts[j], row_y), col_widths[j], row_height,
                                  transform=ax.transAxes, facecolor=bg,
                                  edgecolor='#cccccc', linewidth=0.8, clip_on=False)
            ax.add_patch(rect)
            fw = 'bold' if j == 0 else 'normal'
            fs = 8.5 if j == 0 else 8
            ax.text(col_starts[j] + col_widths[j]/2, row_y + row_height/2,
                    row[j], fontsize=fs, fontweight=fw, ha='center', va='center',
                    transform=ax.transAxes, color='#333333' if j == 0 else '#444444',
                    linespacing=1.3)

    # Summary bar
    summary_y = table_top - (n_rows + 1) * row_height - 0.01
    total_w = col_starts[-1] + col_widths[-1] - col_starts[0]
    rect = plt.Rectangle((col_starts[0], summary_y), total_w, 0.055,
                          transform=ax.transAxes, facecolor='#fff8e7',
                          edgecolor=C_ORANGE, linewidth=1.5, clip_on=False)
    ax.add_patch(rect)
    ax.text(col_starts[0] + total_w/2, summary_y + 0.0275,
            '整合观点：两种假说可能并非互斥——分析性思维在一般假新闻情境中发挥保护作用，但在高度身份化议题中可能被方向性动机"劫持"',
            fontsize=8.5, ha='center', va='center', transform=ax.transAxes,
            color='#555555', fontstyle='italic')

    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    plt.savefig(os.path.join(OUT_DIR, 'chart_02.png'), dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Saved chart_02.png")


if __name__ == '__main__':
    generate_chart_01()
    generate_chart_02()
