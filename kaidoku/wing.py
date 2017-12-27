# -*- coding: utf-8 -*-
"""Wing logics."""


def xwing(s, p, wings, wing, verbose):
    """X-wing familiy."""
    from kaidoku.calc import naklist
    from kaidoku.misc import cell
    message = ''
    logic = ['X-wing', 'Swordfish', 'Jellyfish'][wings - 2]
    for i in range(2):
        for n in range(9):
            if len(wing[i][n][0]) > 1:
                nk, c, position, f = naklist(wings, wing[i][n][1])
                if nk:
                    pos = []
                    for k in f:
                        po = wing[i][n][0][k]
                        for m in c:
                            if m in wing[i][n][1][k]:
                                if i == 0:
                                    pos.append(po * 9 + m)
                                else:
                                    pos.append(m * 9 + po)
                    for j in pos:
                        p[j][n] = 0
                        if p[j].count(1) == 1:
                            s[j] = p[j].index(1) + 1
                    if verbose > 2:
                        if verbose == 3:
                            message = logic + ' can be found.'
                        else:
                            message = logic + ' of ' + str(n + 1) + ' in '
                            for j in position:
                                message += ['R', 'C'][i] + \
                                    str(wing[i][n][0][j] + 1)
                                if j != position[len(position) - 1]:
                                    message += ', '
                            message += ' and '
                            for j in c:
                                message += ['C', 'R'][i] + str(j + 1)
                                if j != c[len(c) - 1]:
                                    message += ', '
                            message += ' removes ' + str(n + 1) + ' from '
                            for j in pos:
                                message += cell(j)
                                if s[j] > 0:
                                    message += ' (=' + str(s[j]) + ')'
                                if j != pos[len(pos) - 1]:
                                    message += ', '
                    return (s, p, message, True, False)
    return (s, p, message, False, False)


def xywing(s, p, b, pair, verbose):
    """XY-wing."""
    from kaidoku.chain import (findchain)
    from kaidoku.misc import (cell)
    message = ''
    if len(pair) < 3:
        return (s, p, message, False, False)
    for i in pair:
        chainx = findchain(pair, [i[0], i[1]], b)
        chainy = findchain(pair, [i[0], i[2]], b)
        if len(chainx) > 1 and len(chainy) > 1:
            for x in chainx:
                for y in chainy:
                    # if x[1] == y[1] and x[0] not in b[y[0]]:
                    if x[1] == y[1]:
                        for bb in b[x[0]]:
                            if bb in b[y[0]]:
                                if s[bb] == 0 and p[bb][x[1] - 1] == 1 and i not in p[bb]:
                                    if verbose > 2:
                                        if verbose == 3:
                                            message = 'XY-wing can be found.'
                                        else:
                                            message = 'XY-wing of ' + \
                                                cell(
                                                    i[0]) + ' (' + str(i[1]) + ',' + \
                                                str(i[2]) + '), '
                                            message += cell(x[0]) + ' (' + \
                                                str(i[1]) + ',' + \
                                                str(x[1]) + '), ' + \
                                                cell(y[0]) + ' (' + str(i[2]) + \
                                                ',' + str(y[1]) + ') '
                                            message += 'removes ' + \
                                                str(x[1]) + ' from ' + \
                                                cell(bb) + '.'
                                    p[bb][x[1] - 1] = 0
                                    if sum(p[bb]) == 1:
                                        s[bb] = p[bb].index(1) + 1
                                        if verbose > 3:
                                            message += '\nTherefore ' + \
                                                cell(bb) + ' = ' + \
                                                str(s[bb]) + '.'
                                    return (s, p, message, True, False)

    return (s, p, message, False, False)


def xyzwing(s, p, b, boxl, comb, pb, verbose):
    """XYZ-wing."""
    from kaidoku.misc import (cell)
    message = ''
    a = [0, 0, 0]
    for i in range(9):
        for x in comb[i]:
            if len(x) == 3:
                for y in comb[i]:
                    if len(y) == 2:
                        if y[0] in x and y[1] in x:
                            xa = boxl[i][comb[i].index(x)]
                            ya = boxl[i][comb[i].index(y)]
                            xp = xa - [0, 3, 6, 27, 30, 33, 54, 57, 60][i]
                            if abs(xa - ya) > 3:
                                for za in pb[i, xp // 9]:
                                    if s[za] == 0 and sum(p[za]) == 2:
                                        if p[za][x[0] - 1] + p[za][x[1] - 1] + p[za][x[2] - 1] == 2:
                                            if p[za][y[0] - 1] + p[za][y[1] - 1] == 1:
                                                if p[za][y[0] - 1] == 1:
                                                    Z = y[0]
                                                else:
                                                    Z = y[1]
                                                a[0] = xa + [1, -1, -2][xp % 3]
                                                a[1] = xa + [2, 1, -1][xp % 3]
                                                for j in [0, 1]:
                                                    if s[a[j]] == 0:
                                                        if p[a[j]][Z - 1] == 1:
                                                            z = ()
                                                            for k in range(9):
                                                                if p[za][k] == 1:
                                                                    z = z + \
                                                                        (k + 1,)
                                                            message = xyzmessage(
                                                                xa, x, ya, y, za, z, Z, a[j], verbose)
                                                            p[a[j]][Z - 1] = 0
                                                            if sum(p[a[j]]) == 1:
                                                                s[a[j]] = p[a[j]].index(
                                                                    1) + 1
                                                                if verbose > 3:
                                                                    message += '\nTherefore ' + \
                                                                        cell(a[j]) + ' = ' + \
                                                                        str(s[a[j]]
                                                                            ) + '.'
                                                            return (s, p, message, True, False)
                            if (xa - ya) % 3 > 0:
                                for za in pb[i, 3 + xp % 3]:
                                    if s[za] == 0 and sum(p[za]) == 2:
                                        if p[za][x[0] - 1] + p[za][x[1] - 1] + p[za][x[2] - 1] == 2:
                                            if p[za][y[0] - 1] + p[za][y[1] - 1] == 1:
                                                if p[za][y[0] - 1] == 1:
                                                    Z = y[0]
                                                else:
                                                    Z = y[1]
                                                a[0] = xa + \
                                                    [9, -9, -18][xp // 9]
                                                a[1] = xa + [18, 9, -9][xp // 9]
                                                for j in [0, 1]:
                                                    if s[a[j]] == 0:
                                                        if p[a[j]][Z - 1] == 1:
                                                            z = ()
                                                            for k in range(9):
                                                                if p[za][k] == 1:
                                                                    z = z + \
                                                                        (k + 1,)
                                                            message = xyzmessage(
                                                                xa, x, ya, y, za, z, Z, a[j], verbose)
                                                            p[a[j]][Z - 1] = 0
                                                            if sum(p[a[j]]) == 1:
                                                                s[a[j]] = p[a[j]].index(
                                                                    1) + 1
                                                                if verbose > 3:
                                                                    message += '\nTherefore ' + \
                                                                        cell(a[j]) + ' = ' + \
                                                                        str(s[a[j]]
                                                                            ) + '.'
                                                            return (s, p, message, True, False)
    return (s, p, message, False, False)


def xyzmessage(xa, x, ya, y, za, z, Z, a, verbose):
    from kaidoku.misc import (cell)
    message = ''
    if verbose > 2:
        if verbose == 3:
            message = 'XYZ-wing can be found.'
        else:
            message = 'XYZ-wing of ' + cell(xa) + ' ' + str(x) + ' ' + \
                cell(ya) + ' ' + str(y) + ' ' + cell(za) + ' ' + str(z) + ' ' + \
                'removes ' + str(Z) + ' from ' + cell(a) + '.'
    return message
