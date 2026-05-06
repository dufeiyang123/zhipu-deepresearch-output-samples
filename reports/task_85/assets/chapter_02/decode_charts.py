#!/usr/bin/env python3
"""Decode base64 chart data to PNG files for Chapter 2.
Run: python3 decode_charts.py
This reads chart_XX.b64 files and writes chart_XX.png files in the same directory.
For full-quality 150 DPI charts, run generate_charts.py instead.
"""
import base64, os

DIR = os.path.dirname(os.path.abspath(__file__))

for i in range(1, 4):
    b64_path = os.path.join(DIR, f"chart_{i:02d}.b64")
    png_path = os.path.join(DIR, f"chart_{i:02d}.png")
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            enc = f.read().strip()
        with open(png_path, "wb") as f:
            f.write(base64.b64decode(enc))
        print(f"Decoded: {png_path}")
    else:
        print(f"Not found: {b64_path}")
