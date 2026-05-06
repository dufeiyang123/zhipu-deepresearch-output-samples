#!/usr/bin/env python3
"""
Chapter 01 Chart Generation Script
Generates 3 charts for: 时间序列流失（Churn）的概念与成因
Run: python3 assets/chapter_01/generate_charts.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

plt.rcParams['font.sans-serif'] = ['Heiti TC', 'Arial Unicode MS', 'STHeiti', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

COLORS = ['#1f4e79', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646']
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ======== Chart 1: Prometheus Churn Mechanism ========
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.5)
ax.axis('off')

ax.text(5, 6.2, 'Prometheus 时间序列 Churn 机制示意图', fontsize=14, fontweight='bold',
        ha='center', va='center', color='#1f4e79')

old_box = FancyBboxPatch((0.2, 3.8), 2.8, 1.3, boxstyle="round,pad=0.12",
                          facecolor='#dce6f1', edgecolor='#1f4e79', linewidth=1.5)
ax.add_patch(old_box)
ax.text(1.6, 4.85, '旧序列', fontsize=10, fontweight='bold', ha='center', color='#1f4e79')
ax.text(1.6, 4.4, 'pod="app-abc12"', fontsize=7.5, ha='center', family='monospace', color='#c0504d')

ax.annotate('', xy=(4.8, 4.5), xytext=(3.1, 4.5),
            arrowprops=dict(arrowstyle='->', color='#c0504d', lw=2))
ax.text(3.95, 4.85, '标签值变化', fontsize=8, ha='center', color='#c0504d', fontweight='bold')

new_box = FancyBboxPatch((4.9, 3.8), 2.8, 1.3, boxstyle="round,pad=0.12",
                          facecolor='#e2efda', edgecolor='#9bbb59', linewidth=1.5)
ax.add_patch(new_box)
ax.text(6.3, 4.85, '新序列', fontsize=10, fontweight='bold', ha='center', color='#4a7c2e')
ax.text(6.3, 4.4, 'pod="app-xyz89"', fontsize=7.5, ha='center', family='monospace', color='#9bbb59')

principle_box = FancyBboxPatch((8.0, 3.9), 1.8, 1.1, boxstyle="round,pad=0.08",
                               facecolor='#fff2cc', edgecolor='#f79646', linewidth=1.2)
ax.add_patch(principle_box)
ax.text(8.9, 4.7, '核心原则', fontsize=8, fontweight='bold', ha='center', color='#f79646')
ax.text(8.9, 4.3, '标签变化\n= 全新序列', fontsize=7.5, ha='center', color='#c0504d', fontweight='bold')

head_box = FancyBboxPatch((0.4, 1.3), 6.8, 2.0, boxstyle="round,pad=0.15",
                           facecolor='#f2f2f2', edgecolor='#1f4e79', linewidth=2)
ax.add_patch(head_box)
ax.text(3.8, 3.05, 'Head Block（2~3h 保留窗口）', fontsize=10, fontweight='bold',
        ha='center', color='#1f4e79')

old_inner = FancyBboxPatch((0.6, 1.5), 3.0, 1.1, boxstyle="round,pad=0.08",
                            facecolor='#f8d7da', edgecolor='#c0504d', linewidth=1, linestyle='--')
ax.add_patch(old_inner)
ax.text(2.1, 2.3, '旧序列 (stale)', fontsize=8, fontweight='bold', ha='center', color='#c0504d')
ax.text(2.1, 1.85, '等待 GC 清理', fontsize=7, ha='center', color='#888')

new_inner = FancyBboxPatch((4.0, 1.5), 3.0, 1.1, boxstyle="round,pad=0.08",
                            facecolor='#d4edda', edgecolor='#9bbb59', linewidth=1)
ax.add_patch(new_inner)
ax.text(5.5, 2.3, '新序列 (active)', fontsize=8, fontweight='bold', ha='center', color='#4a7c2e')
ax.text(5.5, 1.85, '接收新样本', fontsize=7, ha='center', color='#888')

ax.annotate('', xy=(2.1, 3.3), xytext=(1.6, 3.8),
            arrowprops=dict(arrowstyle='->', color='#c0504d', lw=1.2, linestyle='--'))
ax.annotate('', xy=(5.5, 3.3), xytext=(6.3, 3.8),
            arrowprops=dict(arrowstyle='->', color='#9bbb59', lw=1.2))

impact_box = FancyBboxPatch((7.6, 1.3), 2.2, 2.0, boxstyle="round,pad=0.12",
                             facecolor='#fce4ec', edgecolor='#c0504d', linewidth=1.5)
ax.add_patch(impact_box)
ax.text(8.7, 3.0, '高 Churn 后果', fontsize=9, fontweight='bold', ha='center', color='#c0504d')
ax.text(8.7, 2.55, '· 索引膨胀', fontsize=7.5, ha='center', color='#333')
ax.text(8.7, 2.25, '· 内存攀升', fontsize=7.5, ha='center', color='#333')
ax.text(8.7, 1.95, '· GC 频繁', fontsize=7.5, ha='center', color='#333')
ax.text(8.7, 1.65, '· OOM 风险', fontsize=7.5, ha='center', color='#333')

ax.annotate('', xy=(7.6, 2.3), xytext=(7.2, 2.3),
            arrowprops=dict(arrowstyle='->', color='#c0504d', lw=1.5))

ax.annotate('', xy=(7.5, 0.65), xytext=(0.5, 0.65),
            arrowprops=dict(arrowstyle='->', color='#666', lw=1.2))
for x, label in [(1.0, 'T0:旧Pod'), (3.0, 'T1:更新'), (5.0, 'T2:新Pod'), (7.0, 'T3:GC')]:
    ax.plot(x, 0.65, 'o', color='#1f4e79', markersize=5)
    ax.text(x, 0.3, label, fontsize=6.5, ha='center', color='#333')

ax.annotate('', xy=(5.0, 0.95), xytext=(3.0, 0.95),
            arrowprops=dict(arrowstyle='<->', color='#c0504d', lw=1.2))
ax.text(4.0, 1.12, '共存期', fontsize=7, ha='center', color='#c0504d', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#c0504d', alpha=0.9))

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'chart_01.png'), dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved: chart_01.png")

# ======== Chart 2: Kubernetes Churn Causes ========
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

ax.text(5, 6.7, 'Kubernetes 环境典型 Churn 成因分类', fontsize=14, fontweight='bold',
        ha='center', color='#1f4e79')

root_box = FancyBboxPatch((3.0, 5.7), 4.0, 0.65, boxstyle="round,pad=0.12",
                           facecolor='#1f4e79', edgecolor='#1f4e79', linewidth=2)
ax.add_patch(root_box)
ax.text(5, 6.02, '高时间序列流失率', fontsize=11, fontweight='bold', ha='center', color='white')

categories = [
    ('Pod 频繁重建', 'CrashLoop/OOMKill', '分钟级', '高', COLORS[1], '#fce4ec', (0.1, 3.0)),
    ('滚动更新', 'Deployment Rollout', '小时级', '中高', COLORS[0], '#dce6f1', (3.4, 3.0)),
    ('自动扩缩容', 'HPA/VPA/CA', '分钟~时级', '中高', COLORS[3], '#e8daef', (6.7, 3.0)),
    ('Job/CronJob', '短暂 Pod', '分钟级', '高', COLORS[4], '#d5f5e3', (0.1, 0.3)),
    ('标签值膨胀', 'pod/ID/IP 无界', '持续性', '高', COLORS[5], '#fef9e7', (3.4, 0.3)),
    ('Sidecar 爆炸', 'Istio/Envoy', '持续性', '极高', COLORS[2], '#eafaf1', (6.7, 0.3)),
]

for title, subtitle, freq, impact, color, bg, (x, y) in categories:
    w, h = 3.1, 2.3
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                          facecolor=bg, edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x+w/2, y+h-0.3, title, fontsize=9, fontweight='bold', ha='center', color=color)
    ax.text(x+w/2, y+h-0.8, subtitle, fontsize=7.5, ha='center', color='#444')

    freq_box = FancyBboxPatch((x+0.1, y+0.1), 1.3, 0.4, boxstyle="round,pad=0.06",
                               facecolor=color, edgecolor=color, alpha=0.85)
    ax.add_patch(freq_box)
    ax.text(x+0.75, y+0.3, freq, fontsize=6.5, fontweight='bold', ha='center', color='white')

    imp_box = FancyBboxPatch((x+1.6, y+0.1), 1.3, 0.4, boxstyle="round,pad=0.06",
                              facecolor='white', edgecolor=color, linewidth=1)
    ax.add_patch(imp_box)
    ax.text(x+2.25, y+0.3, '影响:'+impact, fontsize=6.5, fontweight='bold', ha='center', color=color)

    ax.plot([x+w/2, 5], [y+h, 5.7], color='#ccc', lw=0.8, zorder=0)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'chart_02.png'), dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved: chart_02.png")

# ======== Chart 3: Diagnostic Metrics Relationship ========
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

ax.text(5, 6.7, 'Prometheus Churn 诊断指标关系图', fontsize=14, fontweight='bold',
        ha='center', color='#1f4e79')

gauge_box = FancyBboxPatch((2.5, 4.7), 5.0, 1.4, boxstyle="round,pad=0.12",
                            facecolor='#dce6f1', edgecolor='#1f4e79', linewidth=2)
ax.add_patch(gauge_box)
ax.text(5, 5.8, 'prometheus_tsdb_head_series', fontsize=10, fontweight='bold',
        ha='center', color='#1f4e79', family='monospace')
ax.text(5, 5.35, 'Gauge：Head Block 当前活跃序列数', fontsize=8.5, ha='center', color='#555')
ax.text(5, 5.0, '反映瞬时基数', fontsize=7.5, ha='center', color='#888', style='italic')

created_box = FancyBboxPatch((0.1, 2.5), 4.5, 1.6, boxstyle="round,pad=0.12",
                              facecolor='#e2efda', edgecolor='#9bbb59', linewidth=1.5)
ax.add_patch(created_box)
ax.text(2.35, 3.8, '..._created_total', fontsize=9, fontweight='bold',
        ha='center', color='#4a7c2e', family='monospace')
ax.text(2.35, 3.35, 'Counter：累计创建序列数', fontsize=8, ha='center', color='#555')
ax.text(2.35, 2.9, 'rate() = 流失率', fontsize=8, ha='center', color='#4a7c2e', fontweight='bold')

removed_box = FancyBboxPatch((5.4, 2.5), 4.5, 1.6, boxstyle="round,pad=0.12",
                              facecolor='#f8d7da', edgecolor='#c0504d', linewidth=1.5)
ax.add_patch(removed_box)
ax.text(7.65, 3.8, '..._removed_total', fontsize=9, fontweight='bold',
        ha='center', color='#c0504d', family='monospace')
ax.text(7.65, 3.35, 'Counter：累计 GC 移除序列数', fontsize=8, ha='center', color='#555')
ax.text(7.65, 2.9, 'rate() = GC 清理速率', fontsize=8, ha='center', color='#c0504d', fontweight='bold')

ax.annotate('', xy=(3.8, 4.7), xytext=(3.0, 4.1),
            arrowprops=dict(arrowstyle='->', color='#9bbb59', lw=2))
ax.text(2.8, 4.5, '+', fontsize=16, fontweight='bold', color='#9bbb59', ha='center')

ax.annotate('', xy=(6.2, 4.7), xytext=(7.0, 4.1),
            arrowprops=dict(arrowstyle='->', color='#c0504d', lw=2))
ax.text(7.2, 4.5, '−', fontsize=16, fontweight='bold', color='#c0504d', ha='center')

target_box = FancyBboxPatch((0.2, 0.3), 4.3, 1.5, boxstyle="round,pad=0.12",
                             facecolor='#fff2cc', edgecolor='#f79646', linewidth=1.5)
ax.add_patch(target_box)
ax.text(2.35, 1.5, 'scrape_series_added', fontsize=9, fontweight='bold',
        ha='center', color='#f79646', family='monospace')
ax.text(2.35, 1.1, 'Per-Target：每次采集新增序列', fontsize=8, ha='center', color='#555')
ax.text(2.35, 0.7, '可按 job 归因（v2.10+）', fontsize=7, ha='center', color='#888', style='italic')

insight_box = FancyBboxPatch((5.5, 0.3), 4.3, 1.5, boxstyle="round,pad=0.12",
                              facecolor='#e8daef', edgecolor='#8064a2', linewidth=1.5)
ax.add_patch(insight_box)
ax.text(7.65, 1.5, '高 Churn 判定准则', fontsize=9, fontweight='bold',
        ha='center', color='#8064a2')
ax.text(7.65, 1.1, 'rate(created) >> 0', fontsize=8, ha='center', color='#333', family='monospace')
ax.text(7.65, 0.7, 'rate(created) ≈ rate(removed)', fontsize=8, ha='center', color='#333', family='monospace')

ax.annotate('', xy=(2.35, 2.5), xytext=(2.35, 1.8),
            arrowprops=dict(arrowstyle='->', color='#f79646', lw=1.2, linestyle='--'))

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'chart_03.png'), dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Saved: chart_03.png")

print("\nAll Chapter 01 charts generated successfully!")
