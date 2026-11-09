"""Rebuild the Pipewright logo SVGs with the wordmark converted to outlines.

Usage:
  pip install fonttools
  # download Libre Baskerville 400 and 700 TTFs from Google Fonts into this folder as lb400.ttf / lb700.ttf
  python build_logo.py && node raster.js ../
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

BOLD, REG = TTFont('lb700.ttf'), TTFont('lb400.ttf')

def text_path(font, text, size, x0, baseline, tracking=-0.01):
    upm = font['head'].unitsPerEm; s = size / upm
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); hmtx = font['hmtx']
    d = []; x = x0
    for ch in text:
        g = cmap[ord(ch)]; pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        d.append(pen.getCommands()); x += hmtx[g][0] * s + tracking * size
    return ' '.join(d), x

def mark(x, y, h, square, stroke, dot):
    k = h / 32
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.4f})">'
            f'<rect x="1" y="1" width="30" height="30" rx="7" fill="{square}"/>'
            f'<path d="M7 10 H15 A7 7 0 0 1 22 17 V25" fill="none" stroke="{stroke}" stroke-width="4.5" stroke-linecap="round"/>'
            f'<circle cx="22" cy="25" r="2.6" fill="{dot}"/></g>')

def lockup(name, ink, muted, square, stroke, dot):
    size = 100; cap = BOLD['OS/2'].sCapHeight * size / BOLD['head'].unitsPerEm
    mh = cap * 1.55; base = mh * 0.5 + cap * 0.5; tx = mh * 1.38
    p1, x = text_path(BOLD, 'Pipewright', size, tx, base); x += size * 0.26
    p2, x = text_path(REG, 'Studio', size, x, base)
    desc = -BOLD['hhea'].descent * size / BOLD['head'].unitsPerEm
    W = x + 2; H = max(mh, base + desc * 0.75) + 2
    open(name, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.0f}" height="{H:.0f}"><title>Pipewright Studio</title>'
        f'{mark(0, 0, mh, square, stroke, dot)}<path d="{p1}" fill="{ink}"/><path d="{p2}" fill="{muted}"/></svg>')

def mark_only(name, square, stroke, dot):
    open(name, 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="512" height="512"><title>Pipewright Studio</title>'
        f'<rect x="1" y="1" width="30" height="30" rx="7" fill="{square}"/>'
        f'<path d="M7 10 H15 A7 7 0 0 1 22 17 V25" fill="none" stroke="{stroke}" stroke-width="4.5" stroke-linecap="round"/>'
        f'<circle cx="22" cy="25" r="2.6" fill="{dot}"/></svg>')

INK, PAPER = '#111A1C', '#EDF0EE'
lockup('../pipewright-logo-light.svg', INK, '#56625F', INK, PAPER, '#A9761B')
lockup('../pipewright-logo-dark.svg', '#E4EBE9', '#95A39F', '#E4EBE9', '#0E1415', '#D9A748')
lockup('../pipewright-logo-brass.svg', '#E0B05A', '#C99A4C', '#E0B05A', '#3B2709', '#FFF1D2')
mark_only('../pipewright-mark-light.svg', INK, PAPER, '#A9761B')
mark_only('../pipewright-mark-dark.svg', '#E4EBE9', '#0E1415', '#D9A748')
mark_only('../pipewright-mark-brass.svg', '#E0B05A', '#3B2709', '#FFF1D2')
