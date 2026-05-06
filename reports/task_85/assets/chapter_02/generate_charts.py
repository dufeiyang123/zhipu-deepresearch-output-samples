#!/usr/bin/env python3
"""Generate Chapter 2 charts: Sensor Technologies for Precision Vibration Isolation."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial Unicode MS", "Noto Sans CJK SC", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

COLORS = ["#1f4e79", "#c0504d", "#9bbb59", "#8064a2", "#4bacc6", "#f79646"]
OUT = os.path.dirname(os.path.abspath(__file__))


def chart_01():
    """Sensor Noise Floor Comparison (log-log)."""
    freq = np.logspace(-1, 3, 200)
    pcb_g = np.interp(np.log10(freq), np.log10([1, 10, 100]),
                       np.log10([3e-7, 1e-7, 4e-8]))
    pcb_nm = 10**pcb_g * 9.81 / (2 * np.pi * freq)**2 * 1e9
    geo_nm = np.where(freq >= 2, 0.01, 0.01 * (2 / freq)**2)
    mems_g = np.where(freq >= 50, 2.5e-9, 2.5e-9 * (50 / freq)**1.5)
    mems_nm = mems_g * 9.81 / (2 * np.pi * freq)**2 * 1e9
    cap_nm = np.where(freq >= 1, 0.02, 0.02 * (1 / freq)**0.5)
    strain_nm = np.where(freq >= 1, 0.015, 0.015 * (1 / freq))
    pstrain_nm = np.where(freq >= 0.5, 0.00015, 0.00015 * (0.5 / freq)**3)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(freq, pcb_nm, color=COLORS[0], lw=2,
              label="Piezoelectric Accelerometer (PCB 393B04)")
    ax.loglog(freq, geo_nm, color=COLORS[1], lw=2,
              label="Geophone / Inertial Velocity (STACIS-type)")
    ax.loglog(freq, mems_nm, color=COLORS[2], lw=2, ls="--",
              label="Optomechanical MEMS Geophone (Jiao et al. 2024)")
    ax.loglog(freq, cap_nm, color=COLORS[3], lw=2,
              label="Capacitive Sensor (PI D-series, ~20 pm/\u221aHz)")
    ax.loglog(freq, strain_nm, color=COLORS[4], lw=2, ls="-.",
              label="Resistive Strain Gauge (~15 pm/\u221aHz)")
    ax.loglog(freq, pstrain_nm, color=COLORS[5], lw=2, ls=":",
              label="Piezoelectric Strain Sensor (>100\u00d7 lower >1 Hz)")
    ax.set_xlabel("Frequency (Hz)", fontsize=12)
    ax.set_ylabel("Equivalent Displacement Noise Density (nm/\u221aHz)", fontsize=12)
    ax.set_title("Sensor Noise Floor Comparison for Vibration Isolation Applications",
                 fontsize=13, fontweight="bold")
    ax.set_xlim(0.1, 1000)
    ax.set_ylim(1e-5, 1e4)
    ax.legend(fontsize=8.5, loc="upper right", framealpha=0.92, handlelength=2.5)
    ax.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    path = os.path.join(OUT, "chart_01.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


def chart_02():
    """Sensor Selection Decision Matrix (table image)."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis("off")
    col_labels = ["Sensor Type", "Resolution", "Bandwidth", "Dynamic\nRange",
                  "Low-Freq\nLimit", "Collocated\nControl", "Environ.\nRobustness"]
    row_data = [
        ["Geophone\n(STACIS-type)", "<0.05 nm\nRMS (sys.)", "0.2\u2013150 Hz",
         "High", "~0.2 Hz", "No", "Moderate"],
        ["Piezo Accel.\n(PCB 393B04)", "~0.3 nm/\u221aHz\n@ 1 Hz", "0.06\u2013450 Hz",
         "High", "~0.06 Hz", "No", "Good\n(ICP \u2264120\u00b0C)"],
        ["MEMS Geophone\n(Jiao 2024)", "2.5 ng/\u221aHz\n(100\u2013200 Hz)", "500 Hz",
         "124 dB", "~50 Hz", "No", "Emerging"],
        ["Capacitive\n(PI D-series)", "<0.01 nm", "10 kHz",
         "Moderate", "DC", "No", "Moderate\n(gap-sensitive)"],
        ["Laser Interf.\n(ZYGO ZMI)", "0.31 nm\n(\u03bb/1024)", ">MHz",
         "Very High", "DC", "No", "Sensitive\n(air refract.)"],
        ["Quartz Force\n(Kistler)", "~10\u207b\u00b3 N", "19.9\u201358.5\nkHz (fn)",
         "High", "~0.05 Hz", "Yes\n(IFF)", "Good\n(>200\u00b0C)"],
        ["Piezo Strain", "~0.15 pm/\u221aHz\n(>1 Hz)", ">10 kHz",
         "Moderate", "~0.5 Hz", "Yes\n(embedded)", "Good"],
        ["Resistive\nStrain Gauge", "~15 pm/\u221aHz", ">10 kHz",
         "Moderate", "DC", "Yes\n(embedded)", "Good"],
    ]
    table = ax.table(cellText=row_data, colLabels=col_labels, cellLoc="center",
                     loc="center", colWidths=[0.14, 0.13, 0.12, 0.10, 0.10, 0.11, 0.12])
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1.0, 2.2)
    for j in range(len(col_labels)):
        cell = table[0, j]
        cell.set_facecolor("#1f4e79")
        cell.set_text_props(color="white", fontweight="bold", fontsize=8)
    for i in range(1, len(row_data) + 1):
        for j in range(len(col_labels)):
            cell = table[i, j]
            cell.set_facecolor("#e8edf3" if i % 2 == 0 else "#f5f7fa")
    ax.set_title("Sensor Selection Decision Matrix for Precision Vibration Isolation",
                 fontsize=13, fontweight="bold", pad=20)
    plt.tight_layout()
    path = os.path.join(OUT, "chart_02.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


def chart_03():
    """Collocated vs Non-Collocated Pole-Zero Map."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # --- (a) Collocated: alternating poles and zeros on imaginary axis ---
    poles_im = [10, 30, 55]
    zeros_im = [18, 42, 68]
    for p in poles_im:
        ax1.plot(0, p, "x", color=COLORS[1], ms=12, mew=2.5)
        ax1.plot(0, -p, "x", color=COLORS[1], ms=12, mew=2.5)
    for z in zeros_im:
        ax1.plot(0, z, "o", color=COLORS[0], ms=10, mew=2, fillstyle="none")
        ax1.plot(0, -z, "o", color=COLORS[0], ms=10, mew=2, fillstyle="none")
    ax1.axhline(0, color="gray", lw=0.5); ax1.axvline(0, color="gray", lw=0.5)
    ax1.set_xlim(-40, 40); ax1.set_ylim(-80, 80)
    ax1.set_xlabel("Real Axis", fontsize=11); ax1.set_ylabel("Imaginary Axis", fontsize=11)
    ax1.set_title("(a) Collocated:\nPole-Zero Interlacing", fontsize=11, fontweight="bold")
    ax1.grid(True, alpha=0.3)
    for lbl, val in zip(["\u03c9\u2081", "\u03c9\u2082", "\u03c9\u2083"], poles_im):
        ax1.annotate(lbl, xy=(0, val), xytext=(10, val), fontsize=10, color=COLORS[1],
                     arrowprops=dict(arrowstyle="->", color=COLORS[1], lw=1.2))
    for lbl, val in zip(["z\u2081", "z\u2082", "z\u2083"], zeros_im):
        ax1.annotate(lbl, xy=(0, val), xytext=(10, val), fontsize=10, color=COLORS[0],
                     arrowprops=dict(arrowstyle="->", color=COLORS[0], lw=1.2))
    ax1.plot([], [], "x", color=COLORS[1], ms=10, mew=2, label="Poles (\u00d7)")
    ax1.plot([], [], "o", color=COLORS[0], ms=8, mew=2, fillstyle="none", label="Zeros (\u25cb)")
    ax1.legend(fontsize=9, loc="lower right")
    ax1.text(0.05, 0.95,
             "Alternating pattern:\n\u03c9\u2081<z\u2081<\u03c9\u2082<z\u2082<\u03c9\u2083<z\u2083\n"
             "\u2192 Unconditionally stable\n   (IFF, PPF, IRC)",
             transform=ax1.transAxes, fontsize=8, va="top",
             bbox=dict(boxstyle="round,pad=0.4", fc="#e8f4e8", alpha=0.8))

    # --- (b) Non-collocated: broken interlacing ---
    poles_nc_im = [10, 30, 55]
    zeros_nc = [(-3, 22), (5, 35), (-2, 52)]
    for p in poles_nc_im:
        ax2.plot(0, p, "x", color=COLORS[1], ms=12, mew=2.5)
        ax2.plot(0, -p, "x", color=COLORS[1], ms=12, mew=2.5)
    for re, im in zeros_nc:
        ax2.plot(re, im, "o", color=COLORS[0], ms=10, mew=2, fillstyle="none")
        ax2.plot(re, -im, "o", color=COLORS[0], ms=10, mew=2, fillstyle="none")
    ax2.axhline(0, color="gray", lw=0.5); ax2.axvline(0, color="gray", lw=0.5)
    ax2.set_xlim(-40, 40); ax2.set_ylim(-80, 80)
    ax2.set_xlabel("Real Axis", fontsize=11); ax2.set_ylabel("Imaginary Axis", fontsize=11)
    ax2.set_title("(b) Non-Collocated:\nBroken Interlacing", fontsize=11, fontweight="bold")
    ax2.grid(True, alpha=0.3)
    ax2.plot([], [], "x", color=COLORS[1], ms=10, mew=2, label="Poles (\u00d7)")
    ax2.plot([], [], "o", color=COLORS[0], ms=8, mew=2, fillstyle="none", label="Zeros (\u25cb)")
    ax2.legend(fontsize=9, loc="lower right")
    ax2.annotate("RHP zero\n(non-min. phase)", xy=(5, 35), xytext=(18, 48),
                 fontsize=9, color=COLORS[1], fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=COLORS[1], lw=1.5),
                 bbox=dict(boxstyle="round,pad=0.3", fc="#fde8e8", alpha=0.8))
    ax2.text(0.05, 0.95,
             "Interlacing broken:\nzeros off imaginary axis\n"
             "\u2192 Phase margin limited\n\u2192 Robust control needed (H\u221e)",
             transform=ax2.transAxes, fontsize=8, va="top",
             bbox=dict(boxstyle="round,pad=0.4", fc="#fde8e8", alpha=0.8))

    plt.tight_layout()
    path = os.path.join(OUT, "chart_03.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


if __name__ == "__main__":
    chart_01()
    chart_02()
    chart_03()
    print("All Chapter 2 charts generated.")
