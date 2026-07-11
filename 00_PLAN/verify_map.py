#!/usr/bin/env python3
"""Mechanical audit for INSITE_Program_Structure_Map.svg.
Checks: (1) numbered flow circles form an unbroken 1..N sequence;
(2) every party box has at least one arrow endpoint touching it (tolerance 8px).
Exit 1 on any failure."""
import re, sys

svg = open(sys.argv[1] if len(sys.argv)>1 else 'INSITE_Program_Structure_Map.svg').read()

# Numbered nodes: green circles r=13 followed by their number text
circles = re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="13" fill="#3E7C59"/>\s*<text[^>]*>(\d+)</text>', svg)
nums = sorted(int(n) for _,_,n in circles)
seq_ok = nums == list(range(1, len(nums)+1))

# Party boxes: rounded rects rx=6 (excludes brand-grid squares, annexation squares, loop container)
boxes = []
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" rx="6"', svg):
    x,y,w,h = map(float, m.groups()); boxes.append((x,y,w,h))
# Box titles for reporting (first bold text after each rect)
titles = re.findall(r'rx="6"[^/]*/>\s*<text[^>]*font-weight="bold">([^<]+)</text>', svg)

ends = []
for m in re.finditer(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', svg):
    x1,y1,x2,y2 = map(float, m.groups()); ends += [(x1,y1),(x2,y2)]

TOL = 8
def touched(b):
    x,y,w,h = b
    return any(x-TOL <= ex <= x+w+TOL and y-TOL <= ey <= y+h+TOL for ex,ey in ends)

orphans = [titles[i] if i < len(titles) else f'box#{i}' for i,b in enumerate(boxes) if not touched(b)]

print(f"Numbered nodes found: {nums}")
print(f"Sequence unbroken 1..{len(nums)}: {'PASS' if seq_ok else 'FAIL'}")
print(f"Party boxes: {len(boxes)}; arrow endpoints: {len(ends)}")
print(f"Connectivity: {'PASS - every box touched' if not orphans else 'FAIL - orphaned: ' + ', '.join(orphans)}")
sys.exit(0 if (seq_ok and not orphans) else 1)
