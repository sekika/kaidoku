# -*- coding: utf-8 -*-
import os.path
from pyx import *
from PIL import Image, ImageDraw, ImageFont

def drawimage(s, p, label, textcolor, imgfile, mark):
    font = 'Arial'
    blankfile = os.path.abspath(os.path.dirname(__file__))+'/data/blank'
    if not os.path.isfile(blankfile+'.eps'):
        blankimage(blankfile)
    c = Image.open(blankfile+'.eps')
    draw = ImageDraw.Draw(c)
    tfont = ImageFont.truetype('/Library/Fonts/'+font+'.ttf', 17)
    nfont = ImageFont.truetype('/Library/Fonts/'+font+'.ttf', 24)
    sfont = ImageFont.truetype('/Library/Fonts/'+font+'.ttf', 9)
    draw.text((20, 10), label, font=tfont, fill='#000')
    for i in range(9):
        for j in range(9):
            n = int(s[i*9+j])
            if n == 0 and mark:
                for m in range(9):
                    if p[i*9+j][m] == 1:
                        draw.text((18+j*28+(m%3)*8, 38+i*28+(m//3)*8), str(m+1), font=sfont, fill=textcolor)
            if n > 0:
                draw.text((22+j*28, 37+i*28), str(n), font=nfont, fill=textcolor)
    c.save(imgfile, 'JPEG', quality=100, optimize=True)

# make sudoku.eps

def blankimage(file):
    m = 0.4 # margin
    tm = 1.2 # top margin
    c = canvas.canvas()
    c.stroke(path.rect(0, 0, 9+2*m, 9+m+tm), [color.grey(1)])
    for i in range(10):
        if i % 3 == 0:
            c.stroke(path.line(i+m, m, i+m, 9+m), [style.linewidth.THIck])
            c.stroke(path.line(m, i+m, 9+m, i+m), [style.linewidth.THIck])
        else:
            c.stroke(path.line(i+m, m, i+m, 9+m))
            c.stroke(path.line(m, i+m, 9+m, i+m))
    c.writeEPSfile(file)
