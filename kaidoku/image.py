# -*- coding: utf-8 -*-
"""Modules for generating sudoku figures."""
import os.path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def drawimage(s, p, label, size, imgfile, figure, mark):
    """Draw sudoku image."""
    font = figure['font']
    textcolor = figure['color']
    axis = figure['axis']
    scalelist = {'small': 0.8, 'medium': 1, 'large': 1.5, 'x-large': 2}
    if size in scalelist:
        scale = scalelist[size]
    else:
        size = 'medium'
        scale = 1.5

    blankfile = os.path.abspath(
        os.path.dirname(__file__)) + '/data/blank-' + size
    if not os.path.isfile(blankfile + '.eps'):
        blankimage(blankfile, scale)
    c = Image.open(blankfile + '.eps')
    draw = ImageDraw.Draw(c)
    try:
        tfont = ImageFont.truetype(font, int(16 * scale))
    except Exception:
        print('Font file cannot be loaded: ', font)
        print('Rewrite font variable in the configuration file.')
        return True
    nfont = ImageFont.truetype(font, int(24 * scale))
    sfont = ImageFont.truetype(font, int(9 * scale))
    if axis == 'numeric':
        draw.text((20 * scale, 0), label, font=tfont, fill='#000')
    else:
        draw.text((20 * scale, 10 * scale), label, font=tfont, fill='#000')
    if axis == 'numeric':
        for i in range(9):
            draw.text((scale, (45 + i * 28.3) * scale), str(i + 1),
                      font=sfont, fill=textcolor)
        for j in range(9):
            draw.text(((24 + j * 28.3) * scale, 21 * scale), str(j + 1),
                      font=sfont, fill=textcolor)
    for i in range(9):
        for j in range(9):
            n = int(s[i * 9 + j])
            if n == 0 and mark:
                for m in range(9):
                    if p[i * 9 + j][m] == 1:
                        draw.text(((16 + j * 28.3 + (m % 3) * 8) * scale,
                                   (36 + i * 28.3 +
                                    (m // 3) * 8) * scale), str(m + 1),
                                  font=sfont, fill=textcolor)
            if n > 0:
                draw.text(((20 + j * 28.3) * scale, (36 + i * 28.3)
                           * scale), str(n), font=nfont, fill=textcolor)
    c.save(imgfile, 'JPEG', quality=100, optimize=True)
    return False


def blankimage(file, scale):
    """Draw blank image."""
    import pyx
    m = 0.4  # margin
    tm = 1.2  # top margin
    c = pyx.canvas.canvas()
    c.stroke(pyx.path.rect(0, 0, (9 + 2 * m) * scale,
                           (9 + m + tm) * scale), [pyx.color.grey(1)])
    for i in range(10):
        if i % 3 == 0:
            c.stroke(pyx.path.line((i + m) * scale, m * scale,
                                   (i + m) * scale, (9 + m) * scale),
                     [pyx.style.linewidth.THIck])
            c.stroke(pyx.path.line(m * scale, (i + m) * scale, (9 + m)
                                   * scale, (i + m) * scale),
                     [pyx.style.linewidth.THIck])
        else:
            c.stroke(pyx.path.line((i + m) * scale, m *
                                   scale, (i + m) * scale, (9 + m) * scale))
            c.stroke(pyx.path.line(m * scale, (i + m) *
                                   scale, (9 + m) * scale, (i + m) * scale))
    c.writeEPSfile(file)
    return
