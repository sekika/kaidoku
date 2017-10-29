import copy

###########################
#             X-wing
###########################


def xwing(s, p, b, boxl, mirror, verbose):
    from .misc import (cell)
    message = ''
    double = {}
    for i in range(9, 27):
        for j in range(len(mirror[i][0])):
            if len(mirror[i][1][j]) == 2:
                n = mirror[i][0][j]
                if not n in double:
                    double[n] = []
                a = boxl[i][mirror[i][1][j][0]]
                b = boxl[i][mirror[i][1][j][1]]
                if i < 18:  # row
                    c = (b - a) * 9 + a % 9
                else:  # column
                    c = 81 + b - a + a // 9
                m = n * 162 + c
                if m in double:
                    double[m].append([a, b])
                else:
                    double[m] = [[a, b]]
    wing = {}
    for m in double:
        if len(double[m]) > 1:
            n = m // 162
            if len(double[m]) > 2:
                message = 'This sudoku has no solution because ' + cell(double[m][0][0]) + ' or ' + cell(double[m][0][1]) + ' is ' + str(n) + ' and ' + cell(double[m][1][0]) + ' or ' + cell(
                    double[m][1][1]) + ' is ' + str(n) + ' and ' + cell(double[m][2][0]) + ' or ' + cell(double[m][2][1]) + ' is ' + str(n) + ', but all of them cannot be true.'
                return (s, p, message, False, True)
            if n in wing:
                wing[n].append([double[m][0][0], double[m][0][1],
                                double[m][1][0], double[m][1][1]])
            else:
                wing[n] = [([double[m][0][0], double[m][0][1],
                             double[m][1][0], double[m][1][1]])]
    for n in wing:
        win = copy.copy(wing[n])
        for square in win:
            if [square[0], square[2], square[1], square[3]] in wing[n]:
                wing[n].remove(square)
                wing[n].remove([square[0], square[2], square[1], square[3]])
        if len(wing[n]) > 0:
            if verbose > 1:
                if verbose == 2:
                    message = 'X-wing can be found.'
                else:
                    message = 'X-wing is found. ' + cell(wing[n][0][0]) + ', ' + cell(wing[n][0][1]) + ', ' + cell(
                        wing[n][0][2]) + ' and ' + cell(wing[n][0][3]) + ' are X-wing of ' + str(n) + '. ' + str(n) + ' is removed from'
            w = wing[n][0]
            i = [0, 0]
            if w[1] - w[0] < 9:  # row
                i[0] = w[0] % 9 + 18
                i[1] = w[1] % 9 + 18
            else:  # column
                i[0] = w[0] // 9 + 9
                i[1] = w[1] // 9 + 9
            for j in [0, 1]:
                box = boxl[i[j]]
                position = mirror[i[j]][1][mirror[i[j]][0].index(n)]
                for pos in position:
                    i2 = box[pos]
                    if i2 not in w:
                        p[i2][n - 1] = 0
                        if sum(p[i2]) == 1:
                            s[i2] = p[i2].index(1) + 1
                        if verbose > 2:
                            message += ' ' + cell(i2)
            if verbose > 2:
                message += '.'
            return (s, p, message, True, False)
    return (s, p, message, False, False)

###########################
#             XY-wing
###########################


def xywing(s, p, b, pair, verbose):
    from .misc import (cell)
    from .chain import (findchain)
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
                                    if verbose > 1:
                                        if verbose == 2:
                                            message = 'XY-wing can be found.'
                                        else:
                                            message = 'XY-wing of ' + \
                                                cell(
                                                    i[0]) + ' (' + str(i[1]) + ',' + str(i[2]) + '), '
                                            message += cell(x[0]) + ' (' + str(i[1]) + ',' + str(x[1]) + '), ' + cell(
                                                y[0]) + ' (' + str(i[2]) + ',' + str(y[1]) + ') '
                                            message += 'removes ' + \
                                                str(x[1]) + ' from ' + \
                                                cell(bb) + '.'
                                    p[bb][x[1] - 1] = 0
                                    if sum(p[bb]) == 1:
                                        s[bb] = p[bb].index(1) + 1
                                        if verbose > 2:
                                            message += '\nTherefore ' + \
                                                cell(bb) + ' = ' + \
                                                str(s[bb]) + '.'
                                    return (s, p, message, True, False)

    return (s, p, message, False, False)
