#!/usr/bin/env python3
"""
Chapter 02 图表生成脚本
运行方式: python3 assets/chapter_02/generate_charts.py
将在 assets/chapter_02/ 目录下生成 chart_01.png, chart_02.png, chart_03.png
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_chart_01():
    """奠基期25位头部学者毕业院校分布饼图"""
    labels_legend = [
        '北京大学 — 7人 (28%)',
        '清华大学 — 6人 (24%)',
        '南京系统 — 3人 (12%)',
        '自学成才 — 3人 (12%)',
        '其他院校 — 6人 (24%)'
    ]
    sizes = [7, 6, 3, 3, 6]
    explode = (0.03, 0.03, 0.03, 0.03, 0.03)

    fig, ax = plt.subplots(figsize=(10, 6))
    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, colors=COLORS[:5],
        autopct='%1.0f%%', startangle=140, pctdistance=0.68,
        textprops={'fontsize': 11}
    )
    for at in autotexts:
        at.set_fontsize(11)
        at.set_fontweight('bold')
        at.set_color('white')
    autotexts[2].set_color('#333')
    autotexts[4].set_color('#333')

    ax.legend(wedges, labels_legend, title="院校类别", loc="center left",
              bbox_to_anchor=(0.92, 0, 0.5, 1), fontsize=10, title_fontsize=11)
    ax.set_title('奠基期25位头部学者毕业院校分布（1950–1966）',
                 fontsize=14, fontweight='bold', pad=18)
    fig.text(0.5, 0.01,
             '注：清华+北大合计13人（52%）；加入南京系统共16人（64%）',
             ha='center', fontsize=8.5, color='#555', style='italic')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.08, right=0.7)

    outpath = os.path.join(SCRIPT_DIR, 'chart_01.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {outpath}")


def generate_chart_02():
    """1952年院系调整前后古代文学头部学者流向图"""
    flows = [
        ('清华大学', '北京大学', '吴组缃、王瑶、季镇淮、浦江清', 4),
        ('燕京大学', '北京大学', '林庚', 1),
        ('北京大学', '北京大学', '游国恩（留任）', 1),
        ('清华/北大', '文学研究所', '余冠英、钱锺书、俞平伯', 3),
        ('中央大学', '复旦大学', '朱东润', 1),
        ('同济大学', '复旦大学', '郭绍虞', 1),
        ('复旦大学', '复旦大学', '赵景深（留任）', 1),
        ('山东大学', '山东大学', '陆侃如、冯沅君、萧涤非', 3),
    ]
    dest_colors = {
        '北京大学': COLORS[0], '复旦大学': COLORS[1],
        '山东大学': COLORS[2], '文学研究所': COLORS[3]
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, (src, dst, names, n) in enumerate(flows):
        y = len(flows) - idx - 0.5
        c = dest_colors.get(dst, COLORS[4])
        ax.text(1.0, y, src, ha='center', va='center', fontsize=10,
                bbox=dict(boxstyle='round,pad=0.35', fc='#f0f0f0', ec='#999', lw=0.8))
        ax.annotate('', xy=(5.5, y), xytext=(2.5, y),
                    arrowprops=dict(arrowstyle='->', color=c,
                                    lw=max(1.5, n * 0.9), mutation_scale=15))
        ax.text(7.0, y, dst, ha='center', va='center', fontsize=10,
                color='white', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.35', fc=c, ec=c, lw=0.8))
        ax.text(4.0, y + 0.25, names, ha='center', va='bottom',
                fontsize=8, color='#444')

    ax.text(1.0, len(flows) + 0.15, '调整前院校',
            ha='center', fontsize=11, fontweight='bold', color='#333')
    ax.text(7.0, len(flows) + 0.15, '调整后去向',
            ha='center', fontsize=11, fontweight='bold', color='#333')
    ax.set_title('1952年院系调整前后古代文学头部学者流向',
                 fontsize=14, fontweight='bold', pad=12)
    fig.text(0.5, 0.01,
             '注：仅展示可明确追踪流向的主要调动',
             ha='center', fontsize=8.5, color='#555', style='italic')
    ax.set_xlim(-0.8, 9.2)
    ax.set_ylim(-0.3, len(flows) + 0.6)
    ax.axis('off')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.06, top=0.92)

    outpath = os.path.join(SCRIPT_DIR, 'chart_02.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {outpath}")


def generate_chart_03():
    """奠基期25位学者专业背景与教育路径分布"""
    categories = [
        '中文/国文系直入',
        '跨学科转入\n(物理/经济/历史/外文)',
        '自学/非正规教育',
        '革命教育体系',
        '具有海外经历'
    ]
    counts = [14, 5, 3, 1, 6]
    bar_colors = [COLORS[0], COLORS[1], COLORS[3], COLORS[5], COLORS[4]]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(categories, counts, color=bar_colors, height=0.55,
                   edgecolor='white')
    for bar, val in zip(bars, counts):
        pct = val / 25 * 100
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height() / 2,
                f'{val}人 ({pct:.0f}%)', va='center', fontsize=10, color='#333')

    ax.set_xlim(0, max(counts) + 5)
    ax.set_xlabel('人数', fontsize=11)
    ax.set_title('奠基期25位学者专业背景与教育路径分布',
                 fontsize=14, fontweight='bold', pad=12)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.text(0.5, 0.01,
             '注：各类别存在交叉，故合计超过25人',
             ha='center', fontsize=8.5, color='#555', style='italic')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)

    outpath = os.path.join(SCRIPT_DIR, 'chart_03.png')
    plt.savefig(outpath, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {outpath}")


if __name__ == '__main__':
    generate_chart_01()
    generate_chart_02()
    generate_chart_03()
    print("All charts generated.")
