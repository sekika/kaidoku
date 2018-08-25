# -*- coding: utf-8 -*-
"""Calculation modules.

Modules for solving sudoku problems.
"""
import datetime
import itertools

from kaidoku.misc import blank
from kaidoku.misc import cell
from kaidoku.misc import check
from kaidoku.output import output


def solve(s, verbose, maxdepth, maxtime):
    """Solve a problem."""
    from kaidoku.misc import box
    from kaidoku.misc import line
    from kaidoku.misc import pbox
    solved = False
    p = possible(s)
    b = box()
    pb = pbox()
    linescan = line()
    start = datetime.datetime.now()
    endtime = start + datetime.timedelta(seconds=maxtime)
    LevelPoint = int((blank(s) / 15.0)**3)  # 30 -> 8, 64 -> 77
    while (not solved):
        bl = blank(s)
        s, p, message, logic, depth, found, err = solveone(
            s, p, verbose, 0, maxdepth, endtime, b, pb, linescan)
        if err:
            if found:
                return (s, message, 0, True, True)
            else:
                return (s, message, 0, False, True)
        if found:
            if message != '':
                print(message)
            if verbose > 4 and blank(s) < bl:
                print(output(s))
            point = {
                'Naked single': 0,
                'Hidden single':  3,
                'Pointing pair': 25,
                'Pointing triple': 25,
                'Naked pair': 25,
                'Naked triple': 40,
                'Hidden pair': 50,
                'Hidden triple': 70,
                'X-wing': 70,
                'XY-wing': 70,
                'XYZ-wing': 100,
                'Remote pairs': 100,
                'Naked quad': 120,
                'Hidden quad': 150,
                'Swordfish': 150,
                'Jellyfish': 200,
                'Chain of pairs': 200,
                'Chain of pairs (long)': 300,
                'Trial': 500,
                'Trial (deep)': 1000,
                'Search': 1500,
                'Deep search': 2500
            }[logic]
            if point > 800:
                point = point * (0.5 + 0.02 * blank(s))
            LevelPoint += point
        else:
            return (s, 'Give up', 0, False, False)
        if blank(s) == 0:
            solved = True
        else:
            solved = False
    for i in range(9):
        if [0, 8, 45, 70, 120, 320, 1000, 2000, 5000][i] <= LevelPoint:
            level = i + 1
    return (s, 'Solved', level, True, False)


def solveone(s, p, verbose, depth, maxdepth, endtime, b, pb, linescan):
    """Solve one move."""
    from kaidoku.chain import pairchain
    from kaidoku.chain import remotepair
    from kaidoku.misc import boxlist
    from kaidoku.misc import combmir
    from kaidoku.misc import pairs
    from kaidoku.misc import wingpos
    from kaidoku.search import search
    from kaidoku.search import trial
    from kaidoku.wing import xwing
    from kaidoku.wing import xywing
    from kaidoku.wing import xyzwing
    # Check validity
    message, err = check(s)
    if verbose == 0:
        message = ''
    if err:
        return (s, p, message, 0, depth, False, True)

    # Basic logic
    boxl = boxlist(s)
    s, p, message, found, err = naksing(s, p, b, verbose)  # Naked single
    if found or err:
        return (s, p, message, 'Naked single', depth, found, err)
    s, p, message, found, err = hidsing(
        s, p, linescan, verbose)  # Hidden single
    if found or err:
        return (s, p, message, 'Hidden single', depth, found, err)

    # Advanced logic

    # Pointing pair or triple
    s, p, logic, message, found, err = pointing(
        s, p, pb, verbose)
    if found or err:
        return (s, p, message, logic, depth, found, err)

    # Naked pair and triple
    comb, mirror = combmir(p, boxl)
    if depth < 2:
        s, p, message, found, err = naked(
            s, p, 2, boxl, comb, verbose)  # Naked pair
        if found or err:
            return (s, p, message, 'Naked pair', depth, found, err)
    if depth < 1:
        s, p, message, found, err = naked(
            s, p, 3, boxl, comb, verbose)  # Naked triple
        if found or err:
            return (s, p, message, 'Naked triple', depth, found, err)

    # Hidden pair and triple
    if depth < 2:
        s, p, message, found, err = hidden(
            s, p, 2, boxl, mirror, verbose)  # Hidden pair
        if found or err:
            return (s, p, message, 'Hidden pair', depth, found, err)
    if depth < 1:
        s, p, message, found, err = hidden(
            s, p, 3, boxl, mirror, verbose)  # Hidden triple
        if found or err:
            return (s, p, message, 'Hidden triple', depth, found, err)

    # Wing families
    wing = wingpos(boxl, mirror)
    pair, paircomb, pairdict = pairs(s, p)
    if depth < 2:
        s, p, message, found, err = xwing(
            s, p, 2, wing, verbose)  # X-wing
        if found or err:
            return (s, p, message, 'X-wing', depth, found, err)
        s, p, message, found, err = xywing(s, p, b, pair, verbose)  # XY-wing
        if found or err:
            return (s, p, message, 'XY-wing', depth, found, err)
        s, p, message, found, err = xyzwing(
            s, p, b, boxl, comb, pb, verbose)  # XYZ-wing
        if found or err:
            return (s, p, message, 'XYZ-wing', depth, found, err)

    if depth == 0:
        # Remote pairs
        if len(pair) > 3:
            s, p, message, found, err = remotepair(
                s, p, b, pair, pairdict, verbose)  # Remote pairs
            if found or err:
                return (s, p, message, 'Remote pairs', depth, found, err)

        # Naked and hidden quad
        s, p, message, found, err = naked(
            s, p, 4, boxl, comb, verbose)  # Naked quad
        if found or err:
            return (s, p, message, 'Naked quad', depth, found, err)

        s, p, message, found, err = hidden(
            s, p, 4, boxl, mirror, verbose)  # Hidden quad
        if found or err:
            return (s, p, message, 'Hidden quad', depth, found, err)

        # Swordfish and Jellyfish
        s, p, message, found, err = xwing(
            s, p, 3, wing, verbose)  # Swordfish
        if found or err:
            return (s, p, message, 'Swordfish', depth, found, err)
        s, p, message, found, err = xwing(
            s, p, 4, wing, verbose)  # Jellyfish
        if found or err:
            return (s, p, message, 'Jellyfish', depth, found, err)

        # Chain of pairs
        if len(pair) > 3:
            s, p, message, chainlength, found, err = pairchain(
                s, p, b, pair, paircomb, verbose)  # Chain of pairs
            if chainlength < 6:
                logic = 'Chain of pairs'  # Short chain
            else:
                logic = 'Chain of pairs (long)'  # Long chain
            if found or err:
                return (s, p, message, logic, depth, found, err)

    # Trial
    # Maximum steps of scan distinguished from full search of 1 depth
    maxstep = 15
    mincell = 100
    if depth == 0 and maxdepth < 999:
        s, p, step, mincell, message, found, err = trial(
            s, p, linescan, maxstep, verbose, b, pair)
        if step < 10:
            logic = 'Trial'
        else:
            logic = 'Trial (deep)'
        if found or err:
            return (s, p, message, logic, depth, found, err)

    # Search from minimum depth
    if maxdepth == 999:
        bla = blank(s)  # Creating mode
    else:
        bla = 0

    if depth == 0:
        if maxdepth > 2 and bla < 60:
            s, p, message, logic, depth2, found, err = search(
                s, p, verbose, 1, 2, endtime, b, pb, linescan, mincell)
            if found or err:
                return (s, p, message, logic, depth2, found, err)
        if maxdepth > 3 and bla < 45:
            s, p, message, logic, depth2, found, err = search(
                s, p, verbose, 1, 3, endtime, b, pb, linescan, mincell)
            if found or err:
                return (s, p, message, logic, depth2, found, err)
        if maxdepth > 4 and bla < 35:
            s, p, message, logic, depth2, found, err = search(
                s, p, verbose, 1, 4, endtime, b, pb, linescan, mincell)
            if found or err:
                return (s, p, message, logic, depth2, found, err)

    # Full search
    if maxdepth > depth:
        s, p, message, logic, depth, found, err = search(
            s, p, verbose, depth + 1, maxdepth, endtime, b, pb, linescan, mincell)
        if found or err:
            return (s, p, message, logic, depth, found, err)

    return (s, p, '', 0, depth, False, False)


def possible(s):
    """Make possibility array."""
    from kaidoku.misc import box
    p = [[]] * 81
    b = box()
    for i in range(81):
        if s[i] == 0:
            p[i] = [1] * 9
            for i2 in b[i]:
                if s[i2] > 0:
                    p[i][s[i2] - 1] = 0
        else:
            p[i] = [0] * 9
            p[i][s[i] - 1] = 1
    return (p)


def naksing(s, p, b, verbose):
    """Naked single."""
    for i in range(81):
        if s[i] == 0:
            for i2 in b[i]:
                v = s[i2]
                if v > 0:
                    p[i][v - 1] = 0
        else:
            p[i] = [10]

    found = False
    message = ''
    for i in range(81):
        if (sum(p[i])) == 0:
            if verbose > 0:
                message = 'This sudoku has no solution because ' + \
                    cell(i) + ' has no candidate.'
            return (s, p, message, False, True)
        if (sum(p[i])) == 1:
            i2 = p[i].index(1)
            found = True
            s[i] = i2 + 1
            if verbose > 3:
                if message == '':
                    message = ('Naked single: ')
                else:
                    message = message + ", "
                message = message + cell(i) + " = " + str(i2 + 1)

    if blank(s) == 0:
        message2, err = check(s)
        if verbose == 0:
            message2 = ''
        if err:
            return (s, p, message2, False, True)

    return (s, p, message, found, False)


def hidsing(s, p, linescan, verbose):
    """Hidden single."""

    for sc in linescan:
        mat = []
        for i in sc:
            if s[i] == 0:
                mat.append(p[i])
        if mat == []:
            continue
        matrix = list(zip(*mat))
        for n in range(9):
            if matrix[n].count(1) == 1:
                for i in sc:
                    if (s[i] == 0) and (p[i][n]) == 1:
                        s[i] = n + 1
                        if verbose < 4:
                            message = ''
                        else:
                            m = linescan.index(sc)
                            message = 'Hidden single in ' + ['box ', 'row ', 'column '][m // 9] + \
                                str(m % 9 + 1) + ' : ' + \
                                cell(i) + ' = ' + str(n + 1)
                        return (s, p, message, True, False)

    return (s, p, '', False, False)


def pointing(s, p, pb, verbose):
    """Pointing pair or triple."""
    for b in range(9):
        begin = [0, 3, 6, 27, 30, 33, 54, 57, 60][b]
        blank = set()
        for i in range(9):
            if s[begin + (0, 1, 2, 9, 10, 11, 18, 19, 20)[i]] == 0:
                blank.add(i)
        for i in range(6):
            j = [set([0, 1, 2]), set([3, 4, 5]), set([6, 7, 8]),
                 set([0, 3, 6]), set([1, 4, 7]), set([2, 5, 8])][i]
            b2 = blank & j
            if len(b2) > 1 > 0:
                for n in range(9):
                    sum = 0
                    for a in b2:
                        sum = sum + \
                            p[begin + (0, 1, 2, 9, 10, 11, 18, 19, 20)[a]][n]
                    if sum > 1:
                        sum2 = 0
                        sum3 = 0
                        for a in (blank - b2):
                            sum2 = sum2 + \
                                p[begin + (0, 1, 2, 9, 10, 11,
                                           18, 19, 20)[a]][n]
                        for a in pb[(b, i)]:
                            if s[a] == 0:
                                sum3 = sum3 + p[a][n]
                        if (sum2 == 0) != (sum3 == 0):
                            logic = 'Pointing ' + \
                                ['', '', 'pair', 'triple'][sum]
                            message = ''
                            if verbose > 2:
                                message = logic + ' in box ' + str(b + 1)
                            if verbose > 3:
                                message = message + " removed " + \
                                    str(n + 1) + " from "
                            if (sum2 == 0):
                                for a in pb[(b, i)]:
                                    if s[a] == 0 and p[a][n] == 1:
                                        p[a][n] = 0
                                        if verbose > 3:
                                            message = message + cell(a) + ' '
                                        if p[a].count(1) == 1:
                                            if verbose > 3:
                                                message = message + \
                                                    '(=' + \
                                                    str(p[a].index(
                                                        1) + 1) + ') '
                                            s[a] = p[a].index(1) + 1
                            else:
                                for a in (blank - b2):
                                    a2 = begin + (0, 1, 2, 9, 10,
                                                  11, 18, 19, 20)[a]
                                    if p[a2][n] == 1:
                                        r = p[a2]
                                        r[n] = 0
                                        p[a2] = r
                                        if verbose > 3:
                                            message = message + cell(a2) + ' '
                                        if p[a2].count(1) == 1:
                                            if verbose > 3:
                                                message = message + \
                                                    '(=' + \
                                                    str(p[a2].index(
                                                        1) + 1) + ') '
                                            s[a2] = p[a2].index(1) + 1
                            return (s, p, logic, message, True, False)
    return (s, p, '', '', False, False)


def naked(s, p, length, boxl, comb, verbose):
    """Naked pair, triple or quad."""
    message = ''
    for i in range(len(comb)):
        list = comb[i]
        if len(list) >= length * 2:
            nk, c, position, f = naklist(length, list)
            if nk:
                if verbose > 2:
                    message = 'Naked ' + ['single', 'pair', 'triple', 'quad'][length - 1] + ' in ' + \
                        ['box ', 'row ', 'column '][i // 9] + \
                        str(i % 9 + 1)
                if verbose > 3:
                    message = message + ' made removal from'
                for j in f:
                    k = boxl[i][j]
                    for m in range(length):
                        p[k][c[m] - 1] = 0
                    if verbose > 3:
                        message = message + ' ' + cell(k)
                    if p[k].count(1) == 1:
                        if verbose > 3:
                            message = message + \
                                '(=' + str(p[k].index(1) + 1) + ') '
                        s[k] = p[k].index(1) + 1
                return (s, p, message, True, False)
    return (s, p, '', False, False)


def hidden(s, p, length, boxl, mirror, verbose):
    """Hidden pair, triple or quad."""
    message = ''
    for i in range(len(mirror)):
        list2 = mirror[i][1]
        if len(list2) > length * 2:
            hd, c, position, f = naklist(length, list2)
            if hd:
                rem = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                for k in range(length):
                    rem.remove(mirror[i][0][position[k]])
                for k in range(length):
                    for m in rem:
                        p[boxl[i][c[k]]][m - 1] = 0
                message = ''
                if verbose > 2:
                    message = 'Hidden ' + ['single', 'pair', 'triple', 'quad'][length - 1] + ' in ' + \
                        ['box ', 'row ', 'column '][i // 9] + \
                        str(i % 9 + 1)
                if verbose > 3:
                    message = 'Hidden ' + ['single', 'pair', 'triple', 'quad'][length - 1] + ' in ' + [
                        'box ', 'row ', 'column '][i // 9] + str(
                        i % 9 + 1) + ': '
                    for m in range(length):
                        message += cell(boxl[i][c[m]])
                        if m < length - 1:
                            message += ' '
                return (s, p, message, True, False)
    return (s, p, '', False, False)


def naklist(length, list):
    """Naked pair, triple or quad."""
    if length == 2:
        np, c, position, f = nakpair(list)
        return (np, c, position, f)
    naked = []
    num = set()
    for i in list:
        if len(i) <= length:
            naked.append(i)
            for j in i:
                num.add(j)
    for c in itertools.combinations(num, length):
        n = 0
        for k in naked:
            if set(k).issubset(set(c)):
                n += 1
        if n == length:
            nak = []
            position = []
            m = 0
            f = []
            for k in list:
                if set(k).issubset(set(c)):
                    nak.append(k)
                    position.append(m)
                else:
                    if set(k).intersection(set(c)):
                        f.append(m)
                m += 1
            if len(f) > 0:
                return (True, c, position, f)
    return (False, 0, 0, 0)


def nakpair(list):
    """Naked pair."""
    pair = []
    for i in list:
        if len(i) == 2:
            pair.append(i)
    if len(set(pair)) < len(pair):
        pairs = []
        for i in range(len(pair)):
            for j in range(i + 1, len(pair)):
                if pair[i] == pair[j]:
                    pairs.append(pair[i])
        for pa in pairs:
            other = set(list) - set([pa])
            f = []
            for q in other:
                if pa[0] in q or pa[1] in q:
                    f.append(list.index(q))
            if len(f) > 0:
                position = [i for i, x in enumerate(list) if x == pa]
                return (True, pa, position, f)
    return (False, 0, 0, 0)
