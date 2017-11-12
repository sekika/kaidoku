# -*- coding: utf-8 -*-
"""Chain logic."""


def remotepair(s, p, b, pair, pairdict, verbose):
    """Remote pairs."""
    from kaidoku.misc import cell
    message = ''
    if len(pair) < 4:
        return (s, p, message, False, False)
    for i in pairdict:
        if len(pairdict[i]) > 3:
            pd = pairdict[i]
            link = {}
            for j in pd:
                for k in pd:
                    if k in b[j]:
                        if j in link:
                            link[j].append(k)
                        else:
                            link[j] = [k, ]
            a = []
            c = []
            for j in link:
                if len(link[j]) > 1:
                    a = [j, ]
                    c = link[j]
                    break
            if len(c) > 0:
                appended = True
            else:
                appended = False
            while appended:
                appended = False
                for d in c:
                    for e in link[d]:
                        if e not in a:
                            a.append(e)
                            appended = True
                            for f in link[e]:
                                if f not in c:
                                    c.append(f)
            if len(a) > 1 and len(c) > 1:
                i1 = i // 10 - 1
                i2 = i % 10 - 1
                rpair = []
                for d in a:
                    for e in c:
                        if d not in link[e]:
                            for f in b[d]:
                                if f in b[e] and s[f] == 0:
                                    if p[f][i1] + p[f][i2] > 0:
                                        rpair.append([d, e, f])
                if len(rpair) > 0:
                    if verbose > 1:
                        if verbose == 2:
                            message = 'Remote pairs.'
                        else:
                            message = 'Remote pairs of (' + str(i1+1) + \
                                ', ' + str(i2+1) + ') are found.'
                    for rp in rpair:
                        if verbose > 2:
                            message += '\n' + \
                                cell(rp[0]) + ' and ' + \
                                cell(rp[1]) + ' are remote pairs.'
                        p[rp[2]][i1] = 0
                        p[rp[2]][i2] = 0
                        if sum(p[rp[2]]) == 0:
                            if verbose > 2:
                                message += '\nNow ' + \
                                    cell(
                                        rp[2]) + ' has no candidate. This sudoku is unsolvable.'
                            return (s, p, message, False, True)
                        if sum(p[rp[2]]) == 1:
                            s[rp[2]] = p[rp[2]].index(1) + 1
                            if verbose > 2:
                                message += ' ' + \
                                    cell(rp[2]) + ' is ' + str(s[rp[2]]) + '.'
                        else:
                            if verbose > 2:
                                message += ' Candidates of ' + \
                                    cell(rp[2]) + ' changes.'
                    return (s, p, message, True, False)
    return (s, p, message, False, False)


def pairchain(s, p, b, pair, paircomb, verbose):
    """Chain of pairs."""
    from kaidoku.misc import cell
    message = ''
    if len(pair) < 4:
        return (s, p, message, False, False)
    for i in paircomb:
        chain = [i]
        chaincell = [i[0]]
        chain2 = findchain(pair, i, b)
        key = i[0] * 10 + i[1]
        dict = {key: chain2}
        path = {key: [i]}
        if chain2 != []:
            for j in chain2:
                chaincell.append(j[0])
            for j in chain2:
                chain.append(j)
                path[j[0] * 10 + j[1]] = path[i[0] * 10 + i[1]] + [j]
            found = True
            loop = False
            while found:
                found = False
                for j in chain2:
                    jkey = j[0] * 10 + j[1]
                    if jkey in dict:
                        chain3 = dict[jkey]
                    else:
                        chain3 = findchain(pair, j, b)
                        dict[jkey] = chain3
                    for j3 in chain3:
                        path[j3[0] * 10 + j3[1]] = path[jkey] + [j3]
                    if chain3 != []:
                        for j2 in chain3:
                            if j2[0] in chaincell:
                                for k in chain:
                                    if k[0] == j2[0]:
                                        if k[1] == j2[1]:
                                            loop = True
                                        else:
                                            # Found a chain
                                            path1 = path[j2[0] * 10 + j2[1]]
                                            path2 = path[j2[0] * 10 + k[1]]
                                            for i in path1[1:]:
                                                if i in path2:
                                                    p1 = path1.index(i)
                                                    path1 = path1[p1:]
                                                    p2 = path2.index(i)
                                                    path2 = path2[p2:]
                                            i = path1[0]
                                            p[i[0]][i[1] - 1] = 0
                                            n = p[i[0]].index(1) + 1
                                            s[i[0]] = n
                                            chainlength = len(
                                                path1) + len(path2)
                                            if verbose > 1:
                                                if verbose == 2:
                                                    message = 'Chain of pairs. Start from ' + \
                                                        cell(i[0]) + '.'
                                                else:
                                                    message = 'Chain of pairs. Assume that ' + \
                                                        cell(i[0]) + ' is ' + str(i[1]) + \
                                                        ' and we have following chains.\n'
                                                    message += '(1) ' + chainpath(path1) + \
                                                        '\n' + \
                                                        '(2) ' + \
                                                        chainpath(path2) + '\n'
                                                    message += 'Now we have contradiction on ' + \
                                                        cell(j2[0]) + '. Therefore ' + cell(i[0]) + \
                                                        ' should be ' + \
                                                        str(n) + '. '
                                            return (s, p, message, chainlength, True, False)
                            chaincell.append(j2[0])
                        if not loop:
                            chain2 = chain3
                            for j in chain2:
                                chain.append(j)
                            found = True

    return (s, p, message, 0, False, False)


def findchain(pair, i, b):
    """Find chain."""
    chain = []
    for j in pair:
        if j[0] in b[i[0]] and (i[1] == j[1] or i[1] == j[2]):
            if i[1] == j[1]:
                chain.append([j[0], j[2]])
            else:
                chain.append([j[0], j[1]])
    return chain


def chainpath(path):
    """Get path of chain."""
    from kaidoku.misc import cell
    chainpath = ''
    for i in path:
        if i != path[0]:
            chainpath += ' >> '
        chainpath += cell(i[0]) + ' = ' + str(i[1])
    return chainpath
