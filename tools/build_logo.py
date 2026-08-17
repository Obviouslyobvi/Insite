#!/usr/bin/env python3
"""
build_logo.py - regenerates the INSITE parcel-grid logo assets.

The mark is a 6-column by 4-row parcel grid: 24 cells.
Source of truth is the founder's reference artwork supplied August 13, 2026 and
measured by pixel analysis: 24 discrete blocks, seven green, two outline-only.

Layout, 1-indexed (row, col):
  green cells   : (2,4) (2,5) (2,6) (3,2) (3,5) (3,6)
  outline cells : (4,5) (4,6)
  every other cell is a filled navy square.

Palette is measured from that same artwork: navy #1A3E6C, green #8DB87A. These
differ from the INS-001 Brand Standards palette (#153A5B, #3E7C59), and the 6x4
grid differs from the 5x4 grid shown in INS-001 and in Header_2.png. The founder
directed the change; the discrepancy is recorded in the build log, not resolved.
The tagline is Slate Gray #6B7280 from INS-001, not the #B3B4B3 measured in the
reference, which renders at 2.2:1 on white and fails the contrast gate.
"""

import os

NAVY = "#1A3E6C"
GREEN = "#8DB87A"
GREEN_LIGHT = "#9fd0b4"   # reversed-edition tagline / green cells on navy
TAGLINE_GRAY = "#6B7280"  # INS-001 Slate Gray

ROWS, COLS = 4, 6
GREEN_CELLS = {(2, 4), (2, 5), (2, 6), (3, 2), (3, 5), (3, 6)}
OUTLINE_CELLS = {(4, 5), (4, 6)}
OUTLINE_FILL = "#ECF4FC"


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
                    f'fill="{OUTLINE_FILL}" stroke="{stroke}" stroke-width="{inset * 2}"/>'
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
        word, tag, rule = NAVY, TAGLINE_GRAY, NAVY

    tx = x0 + gw + 41                            # wordmark start, was 360
    return (
        '<svg width="1560" height="360" xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 1560 360" font-family="Helvetica,Arial,sans-serif" '
        'role="img" aria-label="INSITE Development Impact Fee Payment Program">'
        + bg
        + grid(x0, y0, cell, gap, cell_navy, cell_green, stroke)
        + f'<text x="{tx}" y="212" fill="{word}" font-size="132" font-weight="bold" '
          f'letter-spacing="6">INSITE</text>'
        + f'<text x="{tx + 492}" y="128" fill="{word}" font-size="34">&#8482;</text>'
        + f'<line x1="930" y1="80" x2="930" y2="284" stroke="{rule}" stroke-width="3"/>'
        + f'<text x="975" y="160" fill="{tag}" font-size="42" letter-spacing="3" '
          f'font-weight="bold" textLength="330" lengthAdjust="spacingAndGlyphs">'
          f'DEVELOPMENT IMPACT &amp;</text>'
        + f'<text x="975" y="222" fill="{tag}" font-size="42" letter-spacing="3" '
          f'font-weight="bold" textLength="520" lengthAdjust="spacingAndGlyphs">'
          f'SCHOOL FEE PAYMENT PROGRAM</text>'
        + "</svg>"
    )


def inline_masthead_svg():
    """The compact inline lockup used in page mastheads and print briefs.
    Transparent background so it sits on the navy header without a white plaque."""
    cell, gap = 40, 8
    gw = COLS * cell + (COLS - 1) * gap          # 280 at six columns
    tx = gw + 34
    return (
        "<svg width='179' height='46' viewBox='-26 -18 906 220' "
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
