# -*- coding: utf-8 -*-
"""Chain logic."""


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
