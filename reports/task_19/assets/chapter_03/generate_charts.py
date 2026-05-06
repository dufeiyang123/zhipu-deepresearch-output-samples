#!/usr/bin/env python3
"""
Chapter 03 Chart Generation Script
Generates 3 charts for: 缓解与治理高流失率的系统性方案
Run: python3 assets/chapter_03/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Heiti TC', 'Arial Unicode MS', 'STHeiti', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)


# ======== Chart 1: Heatmap Matrix ========
def chart_01():
    measures = [
        '标签治理与指标设计',
        'metric_relabel_configs',
        'write_relabel_configs',
        'sample_limit / target_limit',
        'WAL 压缩',
        'Go GC 调优',
        '双重保留策略',
        'Recording Rules 预聚合',
        '层级联邦',
        'Agent 模式',
        'Remote Write 队列调优',
        '远端准入控制 (Mimir)',
        'Adaptive Metrics',
    ]
    dimensions = ['内存', 'CPU', '磁盘', '查询性能', '告警可靠性', 'Remote\nWrite', '成本']

    data = np.array([
        [3, 1, 3, 3, 1, 2, 3],
        [3, 1, 3, 2, 1, 3, 2],
        [0, 0, 0, 0, 0, 3, 3],
        [3, 0, 1, 0, 0, 0, 1],
        [0, 0, 3, 0, 0, 0, 1],
        [3, 3, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 2],
        [1, 1, 0, 3, 3, 0, 1],
        [1, 0, 0, 1, 0, 3, 2],
        [3, 1, 2, 0, 0, 1, 2],
        [2, 0, 0, 0, 0, 3, 1],
        [0, 0, 0, 0, 0, 2, 3],
        [0, 0, 2, 2, 0, 0, 3],
    ])

    fig, ax = plt.subplots(figsize=(11, 8.5))
    cmap_colors = ['#f0f0f0', '#b3d4e8', '#5a9bc7', '#1f4e79']
    custom_cmap = LinearSegmentedColormap.from_list('custom', cmap_colors, N=4)
    ax.imshow(data, cmap=custom_cmap, aspect='auto', vmin=0, vmax=3)

    ax.set_xticks(np.arange(len(dimensions)))
    ax.set_yticks(np.arange(len(measures)))
    ax.set_xticklabels(dimensions, fontsize=11, fontweight='bold')
    ax.set_yticklabels(measures, fontsize=10)
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

    effect_labels = {0: '', 1: '间接', 2: '中等', 3: '强效'}
    for i in range(len(measures)):
        for j in range(len(dimensions)):
            val = data[i, j]
            if val > 0:
                text_color = 'white' if val >= 2 else '#1f4e79'
                ax.text(j, i, effect_labels[val], ha='center', va='center',
                        fontsize=9, color=text_color, fontweight='bold')

    ax.set_xticks(np.arange(len(dimensions)+1)-.5, minor=True)
    ax.set_yticks(np.arange(len(measures)+1)-.5, minor=True)
    ax.grid(which='minor', color='white', linewidth=2)
    ax.tick_params(which='minor', bottom=False, left=False, top=False)
    ax.set_title('治理方案与影响维度映射矩阵', fontsize=14, fontweight='bold', pad=25)

    legend_elements = [
        mpatches.Patch(facecolor='#1f4e79', label='强效'),
        mpatches.Patch(facecolor='#5a9bc7', label='中等'),
        mpatches.Patch(facecolor='#b3d4e8', label='间接'),
        mpatches.Patch(facecolor='#f0f0f0', edgecolor='#cccccc', label='无关'),
    ]
    ax.legend(handles=legend_elements, loc='lower center',
              bbox_to_anchor=(0.5, -0.06), ncol=4, fontsize=10,
              frameon=True, edgecolor='#cccccc')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.06)
    out = os.path.join(OUT_DIR, 'chart_01.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")


# ======== Chart 2: Relabeling Pipeline ========
def chart_02():
    fig, ax = plt.subplots(figsize=(14, 6.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    c_stage = '#1f4e79'
    c_filter = '#c0504d'
    c_arrow = '#555555'

    ax.text(7, 6.15, 'Prometheus 采集管道中的三阶段 Relabeling 流程',
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1f4e79')

    stages = [
        {'x': 1.2, 'label': 'Service\nDiscovery', 'color': c_stage, 'w': 1.8},
        {'x': 3.6, 'label': '阶段 1\nrelabel_configs', 'color': c_filter, 'w': 2.0},
        {'x': 6.2, 'label': 'Scrape\n(HTTP 采集)', 'color': c_stage, 'w': 1.8},
        {'x': 8.6, 'label': '阶段 2\nmetric_relabel\n_configs', 'color': c_filter, 'w': 2.0},
        {'x': 11.2, 'label': 'TSDB\nWrite', 'color': c_stage, 'w': 1.6},
    ]

    y_main = 3.6
    box_h = 1.3
    for s in stages:
        rect = FancyBboxPatch((s['x'] - s['w']/2, y_main - box_h/2), s['w'], box_h,
                              boxstyle="round,pad=0.1", facecolor=s['color'], alpha=0.9,
                              edgecolor='white', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(s['x'], y_main, s['label'], ha='center', va='center',
                fontsize=9.5, color='white', fontweight='bold', linespacing=1.3)

    arrow_pairs = [
        (stages[0]['x']+stages[0]['w']/2, stages[1]['x']-stages[1]['w']/2),
        (stages[1]['x']+stages[1]['w']/2, stages[2]['x']-stages[2]['w']/2),
        (stages[2]['x']+stages[2]['w']/2, stages[3]['x']-stages[3]['w']/2),
        (stages[3]['x']+stages[3]['w']/2, stages[4]['x']-stages[4]['w']/2),
    ]
    for (x1, x2) in arrow_pairs:
        ax.annotate('', xy=(x2, y_main), xytext=(x1, y_main),
                    arrowprops=dict(arrowstyle='->', color=c_arrow, lw=2))

    wr_x, wr_y, wr_w, wr_h = 11.2, 1.6, 2.2, 1.1
    rect_wr = FancyBboxPatch((wr_x-wr_w/2, wr_y-wr_h/2), wr_w, wr_h,
                             boxstyle="round,pad=0.1", facecolor=c_filter, alpha=0.9,
                             edgecolor='white', linewidth=1.5)
    ax.add_patch(rect_wr)
    ax.text(wr_x, wr_y, '阶段 3\nwrite_relabel_configs', ha='center', va='center',
            fontsize=9.5, color='white', fontweight='bold', linespacing=1.3)
    ax.annotate('', xy=(11.2, wr_y+wr_h/2), xytext=(11.2, y_main-box_h/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=2))

    re_x, re_y, re_w, re_h = 11.2, 0.35, 2.0, 0.7
    rect_re = FancyBboxPatch((re_x-re_w/2, re_y-re_h/2), re_w, re_h,
                             boxstyle="round,pad=0.1", facecolor='#8064a2', alpha=0.85,
                             edgecolor='white', linewidth=1.5)
    ax.add_patch(rect_re)
    ax.text(re_x, re_y, 'Remote Write 端点', ha='center', va='center',
            fontsize=9.5, color='white', fontweight='bold')
    ax.annotate('', xy=(re_x, re_y+re_h/2), xytext=(wr_x, wr_y-wr_h/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=2))

    desc_configs = [
        {'x': 3.6, 'y': 1.6, 'lines': ['过滤不需要的 target', '基于 K8s 注解控制采集范围', '在 scrape 前执行']},
        {'x': 8.6, 'y': 1.6, 'lines': ['丢弃高基数标签/冗余指标', '在 sample_limit 之前执行', 'Coveo 案例: 30GB→8GB']},
    ]
    for desc in desc_configs:
        bw, bh = 2.8, 1.3
        rect_bg = FancyBboxPatch((desc['x']-bw/2, desc['y']-bh/2), bw, bh,
                                 boxstyle="round,pad=0.08", facecolor='#f0f4f8',
                                 edgecolor='#c0c8d0', linewidth=1)
        ax.add_patch(rect_bg)
        text = '\n'.join(f'• {l}' for l in desc['lines'])
        ax.text(desc['x'], desc['y'], text, ha='center', va='center',
                fontsize=8, color='#333333', linespacing=1.5)
        ax.plot([desc['x'], desc['x']], [desc['y']+bh/2, y_main-box_h/2],
                color='#999999', linestyle='--', linewidth=1)

    wr_desc_x, wr_desc_y = 8.2, 0.35
    wr_bw, wr_bh = 2.8, 1.1
    rect_wr_bg = FancyBboxPatch((wr_desc_x-wr_bw/2, wr_desc_y-wr_bh/2), wr_bw, wr_bh,
                                boxstyle="round,pad=0.08", facecolor='#f0f4f8',
                                edgecolor='#c0c8d0', linewidth=1)
    ax.add_patch(rect_wr_bg)
    ax.text(wr_desc_x, wr_desc_y, '• 本地保留全量, 远端精简\n• 减少 Remote Write 流量\n• 可降低 50%-80% 传输量',
            ha='center', va='center', fontsize=8, color='#333333', linespacing=1.5)
    ax.plot([wr_desc_x+wr_bw/2, wr_x-wr_w/2], [wr_desc_y+0.3, wr_y-0.2],
            color='#999999', linestyle='--', linewidth=1)

    timing_labels = [
        {'x': 2.4, 'y': y_main+0.85, 'text': 'target 元数据'},
        {'x': 5.0, 'y': y_main+0.85, 'text': '过滤后 targets'},
        {'x': 7.4, 'y': y_main+0.85, 'text': '原始 samples'},
        {'x': 10.0, 'y': y_main+0.85, 'text': '过滤后 samples'},
    ]
    for tl in timing_labels:
        ax.text(tl['x'], tl['y'], tl['text'], ha='center', va='center',
                fontsize=8, color='#666666', style='italic')

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'chart_02.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")


# ======== Chart 3: Decision Tree ========
def chart_03():
    fig, ax = plt.subplots(figsize=(13, 8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis('off')

    c_start = '#1f4e79'
    c_decision = '#c0504d'
    c_action = '#9bbb59'
    c_advanced = '#8064a2'
    c_arrow = '#555555'

    def draw_box(x, y, w, h, text, color, fs=9):
        rect = FancyBboxPatch((x-w/2, y-h/2), w, h,
                              boxstyle="round,pad=0.12", facecolor=color, alpha=0.9,
                              edgecolor='white', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center',
                fontsize=fs, color='white', fontweight='bold', linespacing=1.3)

    def draw_diamond(cx, cy, w, h, text, color, fs=8.5):
        diamond = plt.Polygon([
            (cx, cy+h/2), (cx+w/2, cy), (cx, cy-h/2), (cx-w/2, cy),
        ], closed=True, facecolor=color, alpha=0.9, edgecolor='white', linewidth=1.5)
        ax.add_patch(diamond)
        ax.text(cx, cy, text, ha='center', va='center',
                fontsize=fs, color='white', fontweight='bold', linespacing=1.2)

    ax.text(6.5, 7.6, 'Prometheus 渐进式扩展路径决策树',
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1f4e79')

    draw_box(2.5, 6.6, 3.2, 0.75, '单 Prometheus 实例\n(≤1,000 台服务器)', c_start, 10)

    d1_x, d1_y = 2.5, 5.3
    draw_diamond(d1_x, d1_y, 3.0, 1.1, '流失率/基数\n超出单实例容量?', c_decision, 9)
    ax.annotate('', xy=(2.5, d1_y+1.1/2), xytext=(2.5, 6.6-0.75/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))

    draw_box(6.5, 5.3, 2.8, 0.7, '维持单实例 +\n配置调优 (§3.3)', '#4bacc6', 9)
    ax.annotate('', xy=(6.5-2.8/2, 5.3), xytext=(d1_x+3.0/2, d1_y),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(4.8, 5.65, '否', ha='center', fontsize=8, color='#666666', style='italic')

    draw_box(2.5, 3.8, 3.4, 0.75, '按用途拆分\n(高/低流失率工作负载隔离)', c_action, 9)
    ax.annotate('', xy=(2.5, 3.8+0.75/2), xytext=(d1_x, d1_y-1.1/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(2.85, 4.45, '是', ha='center', fontsize=8, color='#666666', style='italic')

    d2_x, d2_y = 2.5, 2.5
    draw_diamond(d2_x, d2_y, 3.0, 1.1, '需要全局聚合\n查询/告警?', c_decision, 9)
    ax.annotate('', xy=(2.5, d2_y+1.1/2), xytext=(2.5, 3.8-0.75/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))

    draw_box(6.5, 3.2, 2.8, 0.85, 'Agent 模式\n+ 远程存储\n(无本地状态)', c_advanced, 9)
    ax.annotate('', xy=(6.5-2.8/2, 3.2), xytext=(d2_x+3.0/2, d2_y+0.15),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(4.8, 2.9, '否 / 边缘场景', ha='center', fontsize=8, color='#666666', style='italic')
    ax.text(6.5, 3.2-0.65, '• 消除 Head Block 膨胀\n• 无本地查询/告警\n• 适合边缘/临时集群',
            ha='center', va='top', fontsize=7.5, color='#555555', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f0f8', edgecolor='#c0b8c8', linewidth=0.8))

    draw_box(2.5, 0.9, 3.6, 0.75, '层级联邦 / hashmod 分片\n+ Recording Rules 预聚合', c_action, 9)
    ax.annotate('', xy=(2.5, 0.9+0.75/2), xytext=(d2_x, d2_y-1.1/2),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(2.85, 1.55, '是', ha='center', fontsize=8, color='#666666', style='italic')

    d3_x, d3_y = 7.5, 0.9
    draw_diamond(d3_x, d3_y, 3.2, 1.0, '基数 > 1亿\n或多租户?', c_decision, 9)
    ax.annotate('', xy=(d3_x-3.2/2, d3_y), xytext=(2.5+3.6/2, 0.9),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(5.6, 1.15, '规模继续增长', ha='center', fontsize=8, color='#666666', style='italic')

    draw_box(11.0, 2.2, 2.6, 0.85, 'Mimir / Thanos /\nVictoriaMetrics\n(第5章详述)', c_advanced, 9)
    ax.annotate('', xy=(11.0-2.6/2, 2.2-0.3), xytext=(d3_x+3.2/2, d3_y+0.15),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(10.0, 1.6, '是', ha='center', fontsize=8, color='#666666', style='italic')

    draw_box(11.0, 0.3, 2.6, 0.6, '联邦 + 远端预聚合\n满足需求', '#4bacc6', 8.5)
    ax.annotate('', xy=(11.0-2.6/2, 0.3+0.1), xytext=(d3_x+3.2/2, d3_y-0.15),
                arrowprops=dict(arrowstyle='->', color=c_arrow, lw=1.8))
    ax.text(10.2, 0.65, '否', ha='center', fontsize=8, color='#666666', style='italic')

    ax.text(11.0, 2.2+0.7, '• 原生多租户隔离\n• 水平扩展 + 对象存储\n• per-tenant 基数限制',
            ha='center', va='bottom', fontsize=7.5, color='#555555', linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f0f8', edgecolor='#c0b8c8', linewidth=0.8))

    sx = 11.5
    ax.text(sx, 6.6, '各阶段治理重点', ha='center', fontsize=10, fontweight='bold', color='#1f4e79')
    annotations = [
        (sx, 6.1, '§3.1 标签治理 + §3.2 Relabeling\n→ 减少序列产生'),
        (sx, 5.4, '§3.3 配置调优 + §3.4 Recording Rules\n→ 限制单实例冲击'),
        (sx, 4.7, '§3.5 架构改进 + §3.6 远端流控\n→ 分散与隔离影响'),
    ]
    for (sxx, sy, stxt) in annotations:
        ax.text(sxx, sy, stxt, ha='center', va='center', fontsize=8, color='#444444', linespacing=1.4,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#eef3f8', edgecolor='#b0c0d0', linewidth=0.8))

    plt.tight_layout()
    out = os.path.join(OUT_DIR, 'chart_03.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {out}")


if __name__ == '__main__':
    chart_01()
    chart_02()
    chart_03()
