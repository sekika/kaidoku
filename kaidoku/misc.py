# -*- coding: utf-8 -*-
"""Miscellaneous modules."""
import copy


def conv(problem):
    """Convert problem to array."""
    s = []
    if problem.find(',') == -1:
        for i in problem:
            if i.isdigit():
                s = s + [int(i)]
            else:
                s = s + [0]
        if len(s) != 81:
            return ('Error in input.', True)
    else:
        for line in problem.split(","):
            if (len(line)) == 9:
                for i in line:
                    if i.isdigit():
                        s = s + [int(i)]
                    else:
                        s = s + [0]
            else:
                return ('Error in input: ' + line, True)

    if len(s) == 81:
        return (s, False)
    else:
        return ('Error in input', True)


def check(s):
    """Check if there is no duplicate numbers in same row, column and box."""
    b = box()
    for i in range(81):
        if s[i] > 0:
            for j in b[i]:
                if s[i] == s[j]:
                    return ('Both ' + cell(i) + ' and ' + cell(j)
                            + ' have the same value of ' + str(
                            s[i]) + '.', True)
    return ('', False)


def box():
    """Define the effective cells."""
    box = []
    for i in range(9):
        for j in range(9):
            b = [0] * 81
            for i2 in range(9):
                b[i2 * 9 + j] = 1
            for j2 in range(9):
                b[i * 9 + j2] = 1
            begin = (i // 3) * 27 + (j // 3) * 3
            for i2 in [0, 1, 2]:
                for j2 in [0, 1, 2]:
                    b[begin + i2 * 9 + j2] = 1
            b[i * 9 + j] = 0
            bb = []
            for i2 in range(81):
                if b[i2] == 1:
                    bb = bb + [i2]
            box = box + [bb]
    return (box)


def pbox():
    """List for use in calculating pointing pair and triple."""
    pbox = {}
    for b in range(9):
        begin = [0, 3, 6, 27, 30, 33, 54, 57, 60][b]
        left = [0, 0, 0, 27, 27, 27, 54, 54, 54][b]
        top = [0, 3, 6, 0, 3, 6, 0, 3, 6][b]
        box = set([])
        for i in (0, 1, 2, 9, 10, 11, 18, 19, 20):
            box = box | set([begin + i])
        for j in range(3):
            line = set([])
            for i in range(9):
                line = line | set([left + j * 9 + i])
            pbox[(b, j)] = line - box
        for j in range(3, 6):
            line = set([])
            for i in range(9):
                line = line | set([top + j - 3 + i * 9])
            pbox[(b, j)] = line - box
    return (pbox)


def boxlist(s):
    """Boxes, row, and columns to scan."""
    boxlist = []
    for b in range(9):
        begin = [0, 3, 6, 27, 30, 33, 54, 57, 60][b]
        bo = []
        for i in (0, 1, 2, 9, 10, 11, 18, 19, 20):
            if s[begin + i] == 0:
                bo.append(begin + i)
        boxlist.append(bo)
    for i in range(9):
        line = []
        for j in range(9):
            if s[i * 9 + j] == 0:
                line.append(i * 9 + j)
        boxlist.append(line)
    for j in range(9):
        line = []
        for i in range(9):
            if s[i * 9 + j] == 0:
                line.append(i * 9 + j)
        boxlist.append(line)

    return boxlist


def combmir(p, boxl):
    """Make lists for calculating naked and hidden combination."""
    comb = []
    mirror = []
    for bo in boxl:
        co = []
        mi = []
        for i in bo:
            c = ()
            for j in range(9):
                if p[i][j] == 1:
                    c = c + (j + 1,)
            co.append(c)
        comb.append(co)
        n = []
        for i in co:
            for j in i:
                if j not in n:
                    n.append(j)
        n = sorted(n)
        for i in n:
            m = ()
            for j in range(len(co)):
                if i in co[j]:
                    m = m + (j,)
            mi.append(m)
        mirror.append([n, mi])
    return (comb, mirror)


def pairs(s, p):
    """Extract pair."""
    pair = []
    paircomb = []
    pairdict = {}
    for i in range(81):
        if s[i] == 0:
            if sum(p[i]) == 2:
                m = p[i].index(1) + 1
                n = p[i][m:].index(1) + m + 1
                pair.append([i, m, n])
                paircomb.append([i, m])
                paircomb.append([i, n])
                if m*10+n not in pairdict:
                    pd = []
                else:
                    pd = pairdict[m*10+n]
                pd.append(i,)
                pairdict[m*10+n] = pd
    return (pair, paircomb, pairdict)


def cell(i):
    """Address of the cell."""
    return ('R' + str(i // 9 + 1) + 'C' + str(i % 9 + 1))


def blank(s):
    """Count numbers of blank cells."""
    blank = 0
    for i in range(81):
        if s[i] == 0:
            blank = blank + 1
    return (blank)


def lev(i):
    """Description of levels."""
    return (['undefined', 'trivial', 'very easy', 'easy', 'normal', 'hard',
             'very hard', 'evil', 'extreme', 'ultimate'][i])


def duplicate(s1, s2):
    """Find different cells."""
    s = []
    for i in range(81):
        if s1[i] == s2[i]:
            s.append(s1[i])
        else:
            s.append(0)
    return (s)


def status(level, solved, err):
    """Calculate status from status and err."""
    if solved:
        if err:
            status = 'multiple solution'
        else:
            status = 'level ' + str(level)
    else:
        if err:
            status = 'no solution'
        else:
            status = 'give up'
    return status


def current(s, move):
    """Move to current position."""
    pos = 0
    for m in move:
        m = int(m)
        row = m // 100
        column = (int(m) - row * 100) // 10
        n = m % 10
        i = (row - 1) * 9 + column - 1
        if s[i] > 0:
            message = 'Cell ' + \
                cell(i) + ' is already filled with ' + str(s[i])
            if pos == 0:
                return (s, [], message, True)
            else:
                return (s, move[:pos], message, True)
        s2 = copy.copy(s)
        s2[i] = n
        message, err = check(s2)
        if err:
            if pos == 0:
                return (s, [], message, True)
            else:
                return (s, move[:pos], message, True)
        message = 'Moved: ' + cell(i) + ' = ' + str(n)
        s = s2
        pos += 1
    return s, move, message, False


def openappend(file):
    """Open as append if exists, write if not."""
    try:
        output = open(file, 'a')
    except Exception:
        try:
            output = open(file, 'w')
        except Exception:
            return 'error'
    return output
