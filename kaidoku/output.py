# -*- coding: utf-8 -*-
from .misc import (conv, blank)


def output(s):

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
    out = "http://www.sudoku-solutions.com/index.php?puzzle="
    for i in range(81):
        v = str(s[i])
        if v == 0:
            out = out + '.'
        else:
            out = out + str(v)
    return out


def short(s):
    sudoku = ''
    for j in s:
        sudoku += str(j)
    return sudoku

# not using now


def listup(file, level):
    input = open(file, 'r')
    i = 0
    for line in input:
        data = line.strip().split(' ')
        s = conv(data[1])[0]
        i += 1
        if int(data[0]) == level:
            print('No.{0} with {1} numbers starting from {2}'.format(
                i, 81 - blank(s), data[1][:18]))
    input.close
    return
