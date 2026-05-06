#!/usr/bin/env python3
"""
Generate all Chapter 4 charts.
Run: python3 generate_all.py
"""
import subprocess, os

script_dir = os.path.dirname(os.path.abspath(__file__))
for i in range(1, 4):
    script = os.path.join(script_dir, f'chart_0{i}.py')
    print(f"Generating chart_0{i}...")
    subprocess.run(['python3', script], check=True)
    print(f"  Done: chart_0{i}.png")
print("All charts generated.")
