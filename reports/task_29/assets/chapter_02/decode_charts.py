#!/usr/bin/env python3
"""Run from project root: python3 assets/chapter_02/decode_charts.py"""
import base64, os, glob

script_dir = os.path.dirname(os.path.abspath(__file__))
for txt_file in sorted(glob.glob(os.path.join(script_dir, "*_data.txt"))):
    name = os.path.basename(txt_file).replace("_data.txt", ".png")
    with open(txt_file) as f:
        b64 = f.read().strip()
    outpath = os.path.join(script_dir, name)
    with open(outpath, "wb") as f:
        f.write(base64.b64decode(b64))
    print(f"Decoded: {outpath} ({os.path.getsize(outpath)} bytes)")

print("All charts decoded.")
