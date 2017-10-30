# -*- coding: utf-8 -*-
"""Modules for output."""


def output(s):
    """Convert to text output format."""
    out = '  1 2 3 4 5 6 7 8 9\n'
    out += ' +-----+-----+-----+\n'
    for i in range(9):
        out += str(i + 1) + '|'
        for j in range(9):
            v = s[i * 9 + j]
            if v == 0:
                out += ' '
            else:
                out = out + str(v)
            if j % 3 == 2:
                out += "|"
            else:
                out += ' '
        out += '\n'
        if i % 3 == 2:
            out += ' +-----+-----+-----+\n'
    return out


def url(s):
    """Convert to URL."""
    out = "http://www.sudoku-solutions.com/index.php?puzzle="
    for i in range(81):
        v = str(s[i])
        if v == 0:
            out = out + '.'
        else:
            out = out + str(v)
    return out


def short(s):
    """Convert to short form."""
    sudoku = ''
    for j in s:
        sudoku += str(j)
    return sudoku
