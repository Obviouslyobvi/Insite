#!/usr/bin/env python3
"""
build_logo.py - regenerates the INSITE parcel-grid logo assets.

The mark is a 5-column by 4-row parcel grid: 20 cells.
Source of truth for the layout is Dennis's brand artifact (Header_2), measured
by pixel analysis July 31, 2026: 20 discrete blocks, three green, two outline-only.

Layout, 1-indexed (row, col):
  green cells   : (2,4) (3,3) (3,4)
  outline cells : (4,4) (4,5)
  every other cell is a filled navy square.

Palette is the canonical brand palette documented in INS-001 Brand Standards
and in 04_BRAND/INSITE_Brand_Kit.html: navy #153A5B, green #3E7C59.
"""

import os

NAVY = "#153A5B"
GREEN = "#3E7C59"
GREEN_LIGHT = "#9fd0b4"   # reversed-edition tagline / green cells on navy

ROWS, COLS = 4, 5
GREEN_CELLS = {(2, 4), (3, 3), (3, 4)}
OUTLINE_CELLS = {(4, 4), (4, 5)}


def grid(x0, y0, cell, gap, fill_navy, fill_green, stroke):
    """Emit the 20 rects of the parcel grid."""
    out = []
    for r in range(1, ROWS + 1):
        for c in range(1, COLS + 1):
            x = x0 + (c - 1) * (cell + gap)
            y = y0 + (r - 1) * (cell + gap)
            if (r, c) in OUTLINE_CELLS:
                inset = max(2, round(cell * 0.045))
                out.append(
                    f'<rect x="{x + inset}" y="{y + inset}" '
                    f'width="{cell - 2 * inset}" height="{cell - 2 * inset}" '
                    f'fill="none" stroke="{stroke}" stroke-width="{inset * 2}"/>'
                )
            else:
                fill = fill_green if (r, c) in GREEN_CELLS else fill_navy
                out.append(
                    f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}"/>'
                )
    return "".join(out)


def mark_svg():
    cell, gap = 88, 16
    w = COLS * cell + (COLS - 1) * gap          # 504
    h = ROWS * cell + (ROWS - 1) * gap          # 400
    return (
        f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="INSITE parcel grid mark">'
        + grid(0, 0, cell, gap, NAVY, GREEN, NAVY)
        + "</svg>"
    )


def lockup_svg(reversed_edition=False):
    """1560x360 horizontal lockup. Wordmark, rule and tagline geometry is
    unchanged from the prior edition; only the mark is rebuilt, resized so the
    5-column grid occupies the same footprint the 4-column grid did."""
    cell, gap = 46, 9
    x0 = 54
    gw = COLS * cell + (COLS - 1) * gap          # 266
    gh = ROWS * cell + (ROWS - 1) * gap          # 211
    y0 = 45 + (265 - gh) // 2                    # vertically centred in old band

    if reversed_edition:
        bg = f'<rect width="1560" height="360" fill="{NAVY}"/>'
        cell_navy, cell_green, stroke = "#ffffff", GREEN_LIGHT, "#ffffff"
        word, tag, rule = "#ffffff", GREEN_LIGHT, "#ffffff"
    else:
        bg = '<rect width="1560" height="360" fill="#ffffff"/>'
        cell_navy, cell_green, stroke = NAVY, GREEN, NAVY
        word, tag, rule = NAVY, GREEN, NAVY

    tx = x0 + gw + 41                            # wordmark start, was 360
    return (
        '<svg width="1560" height="360" xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 1560 360" font-family="Helvetica,Arial,sans-serif" '
        'role="img" aria-label="INSITE Development Impact Fee Financing Program">'
        + bg
        + grid(x0, y0, cell, gap, cell_navy, cell_green, stroke)
        + f'<text x="{tx}" y="212" fill="{word}" font-size="132" font-weight="bold" '
          f'letter-spacing="6">INSITE</text>'
        + f'<text x="{tx + 492}" y="128" fill="{word}" font-size="34">&#8482;</text>'
        + f'<line x1="930" y1="80" x2="930" y2="284" stroke="{rule}" stroke-width="3"/>'
        + f'<text x="975" y="160" fill="{tag}" font-size="42" letter-spacing="3" '
          f'font-weight="bold" textLength="550" lengthAdjust="spacingAndGlyphs">'
          f'DEVELOPMENT IMPACT FEE</text>'
        + f'<text x="975" y="222" fill="{tag}" font-size="42" letter-spacing="3" '
          f'font-weight="bold" textLength="475" lengthAdjust="spacingAndGlyphs">'
          f'FINANCING PROGRAM</text>'
        + "</svg>"
    )


def inline_masthead_svg():
    """The compact inline lockup used in page mastheads and print briefs.
    Transparent background so it sits on the navy header without a white plaque."""
    cell, gap = 40, 8
    gw = COLS * cell + (COLS - 1) * gap          # 232
    tx = gw + 34
    return (
        "<svg width='179' height='46' viewBox='-26 -18 858 220' "
        "xmlns='http://www.w3.org/2000/svg' aria-label='INSITE'>"
        + grid(0, 0, cell, gap, NAVY, GREEN, NAVY)
        + f"<text x='{tx}' y='138' font-family='Helvetica,Arial,sans-serif' "
          f"font-weight='bold' font-size='120' letter-spacing='8' fill='{NAVY}'>INSITE</text>"
        + f"<text x='{tx + 468}' y='44' font-family='Helvetica,Arial,sans-serif' "
          f"font-size='36' fill='{NAVY}'>&#8482;</text>"
        + "</svg>"
    )


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    brand = os.path.join(os.path.dirname(here), "04_BRAND")
    writes = {
        "INSITE_Mark.svg": mark_svg(),
        "INSITE_Logo_Horizontal.svg": lockup_svg(False),
        "INSITE_Logo_Reversed.svg": lockup_svg(True),
    }
    for name, body in writes.items():
        path = os.path.join(brand, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body + "\n")
        rects = body.count("<rect")
        print(f"wrote {name:32s} rects={rects}")
    print("\ninline masthead SVG (for HTML pages):")
    print(inline_masthead_svg())
