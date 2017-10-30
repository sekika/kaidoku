"""Trial and search."""
import copy
import datetime
from kaidoku.misc import blank
from kaidoku.misc import cell


def trial(s, p, maxstep, verbose, b, pair):
    """Trial."""
    if len(pair) == 0:
        return (s, p, 0, '', False, False)
    for x in pair:
        i = x[0]
        for j in x[1:]:
            s2 = copy.deepcopy(s)
            p2 = copy.deepcopy(p)
            s2[i] = j
            p2[i] = [10]
            found = True
            minblank = blank(s2) - maxstep
            if minblank < 0:
                minblank = 0
            message2 = ''
            line = 1
            while found and blank(s2) > minblank:
                s2, p2, message3, found, err = scan(s2, p2, 4, b)
                message2 += '(' + str(line) + ') ' + message3 + '\n'
                line += 1
            if err:
                message = ''
                if verbose > 1:
                    if verbose == 2:
                        message = 'Determine ' + cell(i) + ' by trial.'
                    else:
                        message = 'Trial. If ' + cell(i) + ' is ' + str(j) + \
                            ',\n' + message2.replace(
                            'This sudoku has no solution because', 'Contradiction:')
                p[i][j - 1] = 0
                s[i] = p[i].index(1) + 1
                step = message2.count('=')
                if verbose > 2:
                    message += 'Therefore ' + \
                        cell(i) + ' is ' + str(s[i]) + '.'
                return (s, p, step, message, True, False)
    return (s, p, 0, '', False, False)


def scan(s, p, verbose, b):
    """Scan."""
    from kaidoku.calc import hidsing
    from kaidoku.calc import naksing
    from kaidoku.misc import check
    s, p, message, found, err = naksing(s, p, b, verbose)  # Naked single
    if found or err:
        return (s, p, message, found, err)
    message, err = check(s)
    if err:
        return (s, p, message, False, True)
    s, p, message, found, err = hidsing(s, p, verbose)  # Hidden single
    return (s, p, message, found, err)


def search(s, p, verbose, depth, maxdepth, endtime, b, pb):
    """Full search."""
    from kaidoku.calc import (solveone)

    if datetime.datetime.now() > endtime:
        message = ''
        if verbose > 0:
            message = 'Search time limit'
        return (s, p, message, 9 + depth, depth, False, False)

    message = ''
    smallest = 10
    pair = []
    pairnum = [[], [], [], [], [], [], [], [], []]
    for j in range(81):
        if s[j] == 0:
            if sum(p[j]) == 2:
                pair.append(j)
                for k in range(9):
                    if p[j][k] == 1:
                        pairnum[k].append([j])
            if sum(p[j]) < smallest:
                i = j
                smallest = sum(p[j])
    if len(pair) > 1:
        m = 0
        for j in range(9):
            if len(pairnum[j]) > m:
                i = int(pairnum[j][0][0])

    solution = []
    removed = []

    for n in range(9):
        if p[i][n] == 0:
            continue
        s2 = copy.deepcopy(s)
        p2 = copy.deepcopy(p)
        s2[i] = n + 1
        while (True):
            s2, p2, message, logic, depth2, found, err = solveone(
                s2, p2, 0, depth, maxdepth, endtime, b, pb)
            if found:
                if err:  # Multiple solutions
                    if depth2 > depth:
                        depth = depth2
                    return (s2, p2, message, logic, depth, True, True)
                else:
                    if blank(s2) == 0:
                        solution.append([n, s2])
                        break
            else:
                if err:  # No solution
                    if depth2 > depth:
                        depth = depth2
                    removed.append(n)
                    break
                else:
                    break
        if len(solution) > 1:
            break

    if depth == 1:
        logic = 'Search'
    else:
        logic = 'Deep search'

    if len(solution) > 1:
        if verbose > 1:
            message = 'Search with depth ' + \
                str(depth) + ' shows that this sudoku has multiple solutions.'
        s = [solution[0][1], solution[1][1]]
        return (s, p, message, logic, depth, True, True)
    if len(removed) > 0:
        for n in removed:
            p[i][n] = 0
        if sum(p[i]) == 0:
            if verbose > 1:
                message = 'Search with depth ' + \
                    str(depth) + ' shows that ' + \
                    cell(i) + ' has no candidate.'
            return (s, p, message, logic, depth, False, True)
        if sum(p[i]) == 1:
            s[i] = p[i].index(1) + 1
            if verbose > 1:
                message = 'Search with depth ' + \
                    str(depth) + ' shows that ' + \
                    cell(i) + ' should be ' + str(s[i])
            return (s, p, message, logic, depth, True, False)
        if verbose > 1:
            message = 'Search with depth ' + \
                str(depth) + ' shows that ' + \
                cell(i) + ' is not ' + str(removed)
        return (s, p, message, logic, depth, True, False)
    else:
        if verbose > 1:
            message = 'Search with depth ' + \
                str(depth) + ' on ' + cell(i) + ' did not give any clue.'
        return (s, p, message, logic, depth, False, False)
