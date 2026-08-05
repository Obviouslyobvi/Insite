#!/usr/bin/env python3
"""sharpen_assets.py - cleans the INS-002 line-art graphics for web display.

The source files are JPEGs carrying visible 8x8 compression blocking and a
mottled off-white paper. Measured before this ran, assets_ins002_types.jpg had a
blockiness ratio of 1.334 against a clean baseline of 1.0. This pipeline removes
that noise, snaps the paper to pure white, sharpens the linework, and writes a
palette PNG so nothing is ever re-compressed lossily again.

The JPEGs stay in the repo as the sources of truth. This script is the only
thing that writes the PNGs; never hand-edit the output.

Usage: python3 tools/sharpen_assets.py
"""
import os
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(HERE), '05_WEBSITE')

# (source jpeg, output png, palette size)
JOBS = [
    ('assets_ins002_types.jpg',   'assets_ins002_types.png',   32),
    ('assets_ins002_factors.jpg', 'assets_ins002_factors.png', 32),
]

PAPER_THRESHOLD = 232   # grey level above which a pixel is treated as paper
SHARPEN_RADIUS = 1.4
SHARPEN_AMOUNT = 1.7


def blockiness(rgb):
    """Mean horizontal gradient on JPEG block boundaries over the same off them.
    1.0 means no block structure; higher means visible 8x8 seams."""
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(float)
    col = np.abs(np.diff(g, axis=1)).mean(axis=0)
    on = col[7::8].mean()
    off = np.delete(col, np.arange(7, len(col), 8)).mean()
    return on / off


def edge_energy(rgb):
    g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(float)
    return cv2.Laplacian(g, cv2.CV_64F).var()


def clean(rgb):
    # 1. non-local means removes the 8x8 block structure that a bilateral filter leaves behind
    out = cv2.fastNlMeansDenoisingColored(rgb, None, 7, 7, 7, 21)
    # 2. snap the paper to pure white so compression mottle in the background disappears
    paper = cv2.cvtColor(out, cv2.COLOR_RGB2GRAY) > PAPER_THRESHOLD
    out[paper] = [255, 255, 255]
    # 3. unsharp tuned for line art: small radius so strokes tighten without haloing
    blur = cv2.GaussianBlur(out, (0, 0), SHARPEN_RADIUS)
    out = np.clip(cv2.addWeighted(out, SHARPEN_AMOUNT, blur, -(SHARPEN_AMOUNT - 1.0), 0), 0, 255).astype(np.uint8)
    out[paper] = [255, 255, 255]   # keep the paper clean after sharpening
    return out


def main():
    for src_name, out_name, colors in JOBS:
        src = os.path.join(SITE, src_name)
        out = os.path.join(SITE, out_name)
        rgb = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2RGB)
        before = (blockiness(rgb), edge_energy(rgb))
        cleaned = clean(rgb)
        img = Image.fromarray(cleaned).quantize(colors=colors, method=Image.MEDIANCUT).convert('RGB')
        img.save(out, optimize=True)

        after_arr = np.array(img)
        drift = np.abs(after_arr.astype(int) - cleaned.astype(int))
        assert os.path.exists(out) and os.path.getsize(out) > 0, f"{out} missing or empty"
        assert drift.mean() < 2.0, f"palette drift too high on {out_name}: {drift.mean():.2f}"
        print(f"{src_name} -> {out_name}  {img.size[0]}x{img.size[1]}  "
              f"{os.path.getsize(src):,} -> {os.path.getsize(out):,} bytes | "
              f"blockiness {before[0]:.3f} -> {blockiness(after_arr):.3f} | "
              f"edge energy {before[1]:.0f} -> {edge_energy(after_arr):.0f} | "
              f"palette drift {drift.mean():.2f}")


if __name__ == '__main__':
    main()
