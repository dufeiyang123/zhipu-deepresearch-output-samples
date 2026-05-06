#!/usr/bin/env python3
"""
Chapter 06 Chart Generation Script
Run: python3 assets/chapter_06/generate_charts.py
Generates chart_01.png and chart_02.png in the same directory.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

plt.rcParams["font.sans-serif"] = [
    "Hiragino Sans GB", "STHeiti", "Arial Unicode MS", "DejaVu Sans"
]
plt.rcParams["axes.unicode_minus"] = False

COLORS = ["#1f4e79", "#c0504d", "#9bbb59", "#8064a2", "#4bacc6", "#f79646"]
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_chart_01():
    """Research Priority Matrix: Theoretical Maturity vs. Empirical Evidence"""
    fig, ax = plt.subplots(figsize=(10, 6))

    directions = [
        ("Longitudinal/Causal Design", "\u7eb5\u5411\u56e0\u679c\u8bbe\u8ba1", 2.0, 7.8, 0),
        ("Cross-cultural Research", "\u8de8\u6587\u5316\u7814\u7a76", 1.5, 5.0, 1),
        ("Digital Env. / Algorithm", "\u6570\u5b57\u73af\u5883/\u7b97\u6cd5\u4ea4\u4e92", 1.0, 3.8, 2),
        ("AI-generated Content", "AI\u751f\u6210\u5185\u5bb9", 1.5, 2.5, 3),
        ("Construct Integration", "\u6784\u5ff5\u6574\u5408\u6846\u67b6", 2.8, 6.2, 4),
        ("System Design Translation", "\u7cfb\u7edf\u8bbe\u8ba1\u8f6c\u5316", 3.2, 5.2, 5),
    ]

    ax.axhline(y=5.0, color="#cccccc", linestyle="--", linewidth=0.8, zorder=1)
    ax.axvline(x=5.0, color="#cccccc", linestyle="--", linewidth=0.8, zorder=1)

    ql_kw = dict(ha="center", va="center", fontsize=8, color="#999999", style="italic")
    ax.text(2.5, 9.2, "\u7406\u8bba\u6210\u719f / \u5b9e\u8bc1\u532e\u4e4f  (High Priority Gap)", **ql_kw)
    ax.text(7.5, 9.2, "\u7406\u8bba\u6210\u719f / \u5b9e\u8bc1\u4e30\u5bcc  (Established)", **ql_kw)
    ax.text(2.5, 0.8, "\u7406\u8bba\u521d\u671f / \u5b9e\u8bc1\u532e\u4e4f  (Emerging Frontier)", **ql_kw)
    ax.text(7.5, 0.8, "\u7406\u8bba\u521d\u671f / \u5b9e\u8bc1\u4e30\u5bcc  (Empirically-led)", **ql_kw)

    for en_lab, zh_lab, x, y, ci in directions:
        ax.scatter(x, y, s=550, c=COLORS[ci], alpha=0.85,
                   edgecolors="white", linewidth=1.5, zorder=3)
        combined = f"{en_lab}\n({zh_lab})"
        ax.annotate(combined, (x, y), xytext=(x + 0.45, y),
                    fontsize=8, fontweight="bold", color=COLORS[ci],
                    ha="left", va="center", zorder=4)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel(
        "\u5b9e\u8bc1\u8bc1\u636e\u5145\u88d5\u5ea6 (Empirical Evidence Availability)  \u2192",
        fontsize=10.5, labelpad=10)
    ax.set_ylabel(
        "\u7406\u8bba\u6210\u719f\u5ea6 (Theoretical Maturity)  \u2192",
        fontsize=10.5, labelpad=10)
    ax.set_title(
        "NFC\u4e0e\u9519\u8bef\u4fe1\u606f\u7814\u7a76\uff1a"
        "\u516d\u5927\u524d\u6cbf\u65b9\u5411\u7684\u7406\u8bba\u2013\u5b9e\u8bc1\u5b9a\u4f4d\u77e9\u9635",
        fontsize=12.5, fontweight="bold", pad=14)
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 11))
    ax.tick_params(labelsize=9)
    ax.grid(True, alpha=0.15, zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    note = (
        "\u6ce8\uff1a\u6240\u6709\u516d\u4e2a\u65b9\u5411\u5747\u5904\u4e8e"
        "\u77e9\u9635\u5de6\u4fa7(\u5b9e\u8bc1\u7a00\u7f3a\u533a),\n"
        "\u53cd\u6620\u8be5\u9886\u57df\u201c\u7406\u8bba\u4e30\u5bcc\u3001"
        "\u5b9e\u8bc1\u7a00\u8584\u201d\u7684\u7ed3\u6784\u6027\u7279\u5f81\u3002"
    )
    ax.text(9.8, 0.2, note, fontsize=7, color="#666666",
            ha="right", va="bottom",
            bbox=dict(boxstyle="round,pad=0.35",
                      facecolor="#f7f7f7", edgecolor="#cccccc"))

    plt.tight_layout()
    out = os.path.join(OUT_DIR, "chart_01.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


def generate_chart_02():
    """Epistemic Motivation Integration Framework: Process Flow"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.text(5, 5.55,
            "Epistemic Motivation \u6574\u5408\u6846\u67b6\uff1a"
            "\u4fe1\u606f\u52a0\u5de5\u5e8f\u5217\u4e2d\u7684\u6784\u5ff5\u5b9a\u4f4d",
            fontsize=12.5, fontweight="bold",
            ha="center", va="center", color="#1a1a1a")

    stages = [
        ("\u4fe1\u606f\u641c\u7d22\nInformation\nSearch", 1.3),
        ("\u4fe1\u606f\u8bc4\u4f30\nInformation\nEvaluation", 3.7),
        ("\u4fe1\u606f\u6574\u5408\nInformation\nIntegration", 6.1),
        ("\u5224\u65ad\u8f93\u51fa\nJudgment\nOutput", 8.5),
    ]
    bw, bh = 1.8, 1.3
    yc = 3.5

    for label, cx in stages:
        r = FancyBboxPatch(
            (cx - bw / 2, yc - bh / 2), bw, bh,
            boxstyle="round,pad=0.1",
            facecolor="#e8edf2", edgecolor="#1f4e79",
            linewidth=1.5, zorder=2)
        ax.add_patch(r)
        ax.text(cx, yc, label, fontsize=8.5, ha="center", va="center",
                fontweight="bold", color="#1f4e79", zorder=3)

    for i in range(len(stages) - 1):
        xs = stages[i][1] + bw / 2 + 0.05
        xe = stages[i + 1][1] - bw / 2 - 0.05
        ax.annotate("", xy=(xe, yc), xytext=(xs, yc),
                    arrowprops=dict(arrowstyle="-|>", color="#666666",
                                    lw=1.8, mutation_scale=18),
                    zorder=2)

    constructs = [
        ("NFC / NFCC\n(\u8ba4\u77e5\u95ed\u5408\u9700\u8981)", 1.3, COLORS[0]),
        ("AOT\n(\u79ef\u6781\u5f00\u653e\u6027\u601d\u7ef4)", 3.7, COLORS[1]),
        ("CRT / NfCog\n(\u8ba4\u77e5\u53cd\u601d/\u8ba4\u77e5\u9700\u6c42)", 6.1, COLORS[4]),
    ]
    ycon = 1.4
    cw, ch = 2.0, 0.85

    for label, cx, col in constructs:
        r = FancyBboxPatch(
            (cx - cw / 2, ycon - ch / 2), cw, ch,
            boxstyle="round,pad=0.1",
            facecolor=col, edgecolor=col,
            alpha=0.15, linewidth=1.5, zorder=2)
        ax.add_patch(r)
        bar = plt.Rectangle(
            (cx - cw / 2, ycon - ch / 2), 0.08, ch,
            color=col, zorder=3)
        ax.add_patch(bar)
        ax.text(cx, ycon, label, fontsize=8, ha="center", va="center",
                fontweight="bold", color=col, zorder=3)
        ax.annotate("", xy=(cx, yc - bh / 2 - 0.05),
                    xytext=(cx, ycon + ch / 2 + 0.05),
                    arrowprops=dict(arrowstyle="-|>", color=col,
                                    lw=1.3, linestyle="--",
                                    mutation_scale=14),
                    zorder=2)

    roles = [
        (1.3, "\u51b3\u5b9a\u641c\u7d22\u8303\u56f4\u4e0e\u7ec8\u6b62\u70b9\n"
              "(Scope & Termination)"),
        (3.7, "\u51b3\u5b9a\u5bf9\u7ade\u4e89\u6027\u5047\u8bbe\u7684\u5f00\u653e\u7a0b\u5ea6\n"
              "(Openness to Alternatives)"),
        (6.1, "\u51b3\u5b9a\u662f\u5426\u6295\u5165\u8d44\u6e90\u8fdb\u884c\u6df1\u5ea6\u52a0\u5de5\n"
              "(Deep Processing Investment)"),
    ]
    for rx, rtxt in roles:
        ax.text(rx, 0.5, rtxt, fontsize=6.5, ha="center", va="center",
                color="#555555", style="italic")

    plt.tight_layout()
    out = os.path.join(OUT_DIR, "chart_02.png")
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out}")


if __name__ == "__main__":
    generate_chart_01()
    generate_chart_02()
    print("All Chapter 06 charts generated.")
