# -*- coding: utf-8 -*-
import sys
import copy
import datetime
import random
from statistics import mean, stdev
from .calc import (solve, possible)
from .misc import (conv, check, box, blank, lev, status, current, openappend)
from .output import (output, short)


def analyze(file, level, verbose):
    if file == '':
        return
    start = datetime.datetime.now()
    input = open(file, 'r')
    i = []
    l = []
    n = 0
    for line in input:
        n += 1
        data = line.strip().split(' ')
        if int(data[0]) == level:
            s = conv(data[1])[0]
            s2 = copy.copy(s)
            if verbose > 0:
                print('Solving problem No.{0}'.format(len(i) + 1))
            s2, message, level2, solved, err = solve(s2, verbose, 20, 10)
            if not solved and err:
                print('\nNo solution {0}'.format(data[1]))
            if solved and err:
                print('\nMultiple solutions {0}'.format(data[1]))
            if not solved and not err:
                print('\nGive up {0}'.format(data[1]))
            i.append(blank(s))
            l.append(level2)
            if verbose == 0:
                if len(i) % 10 == 0:
                    print('.', end='', flush=True)
                if len(i) % 200 == 0:
                    dt = datetime.datetime.now() - start
                    t = dt.seconds + float(dt.microseconds) / 1000000
                    print(' {0} problems solved in {1:.1f} seconds (mean: {2:.3f} sec).'.format(
                        len(i), t, t / len(i)))

    dt = datetime.datetime.now() - start
    t = dt.seconds + float(dt.microseconds) / 1000000
    print('\n{0} problems solved in {1:.1f} seconds (mean: {2:.3f} sec).'.format(
        len(i), t, t / (len(i))))
    for j in range(11):
        n = l.count(j)
        if n > 0:
            print('Level {0}: {1}'.format(j, n))
    print('Numbers: mean {0:.1f} std {1:.1f} min {2}'.format(
        81 - mean(i), stdev(i), 81 - max(i)))
    input.close
    return


def reanalyze(file, file2):
    if file == '':
        return
    start = datetime.datetime.now()
    input = open(file, 'r')
    output = open(file2, 'w')
    i = 0
    for line in input:
        data = line.strip().split(' ')
        s = conv(data[1])[0]
        s2 = copy.copy(s)
        s2, message, level, solved, err = solve(s2, 0, 20, 10)
        if not solved and err:
            print('\nNo solution {0}'.format(data[1]))
            continue
        if solved and err:
            print('\nMultiple solutions {0}'.format(data[1]))
            continue
        if not solved and not err:
            print('\nGive up {0}'.format(data[1]))
            continue
        output.write(str(level) + ' ' + data[1] + '\n')
        dt = datetime.datetime.now() - start
        t = dt.seconds + float(dt.microseconds) / 1000000
        i += 1
        if i % 10 == 0:
            print('.', end='', flush=True)
        if i % 200 == 0:
            dt = datetime.datetime.now() - start
            t = dt.seconds + float(dt.microseconds) / 1000000
            print(' {0} problems reanalyzed in {1:.1f} seconds (mean: {2:.3f} sec).'.format(
                i, t, t / i))
    input.close
    output.close
    print('')
    return


def append_database(file, giveup, n):

    maxtime = 3
    maxdepth = 999  # Creating mode

    if file == '':
        return
    output = openappend(file)
    if output == 'error':
        print('Unable to write a file:', file)
        return
    start = datetime.datetime.now()
    for i in range(n):
        s, level = create(maxdepth,  maxtime)
        sudoku = short(s)
        print('.', end='', flush=True)
        if level == 0:
            give = openappend(giveup)
            if output == 'error':
                print('Unable to write a file:', giveup)
                return
            give.write('g ' + str(maxtime) + ' ' + sudoku + '\n')
            give.close
        else:
            output.write(str(level) + ' ' + sudoku + '\n')
        if (i + 1) % 10 == 0 and i + 1 < n:
            dt = datetime.datetime.now() - start
            t = dt.seconds + float(dt.microseconds) / 1000000
            print(' {0} problems created in {1:.1f} seconds (mean: {2:.3f} sec).'.format(
                i + 1, t, t / (i + 1)))
            output.close
            output = open(file, 'a')
    output.close
    dt = datetime.datetime.now() - start
    t = dt.seconds + float(dt.microseconds) / 1000000
    print('\nFinished. {0} problems created in {1:.1f} seconds (mean: {2:.3f} sec).'.format(
        n, t, t / n))
    show_status(file)

    return


def show_status(file):
    if file == '':
        return
    input = open(file, 'r')
    l = [0] * 10
    for line in input:
        data = line.strip().split(' ')
        l[int(data[0])] += 1
    su = sum(l)
    if su == 0:
        print('No problem in the book.')
        print('Create problems with c command.')
        return
    for i in range(1, 10):
        print('Level {0} {1:<10}: {2:>6} ({3:5.2f} %)'.format(
            i, lev(i), l[i], l[i] / su * 100))
    print('Total numbers     : {0:>6}'.format(su))
    input.close
    return


def create(maxdepth, maxtime):

    min = 17  # proven minimum numbers

    order = []
    for i in range(81):
        order.append(i)
    err = True
    while err:
        random.shuffle(order)
        n = []
        v = 0
        while (v < 8):
            for i in range(min):
                n.append(random.randint(1, 9))
                v = len(set(n))
        s = [0] * 81
        for i in range(8):
            s[order[i]] = i + 1
        for i in range(8, min):
            p = set(range(1, 10))
            for j in box()[i]:
                if s[j] in p:
                    p.remove(s[j])
            if len(p) == 0:
                continue
            s[order[i]] = int(random.sample(p, 1)[0])
        message, err = check(s)
        # if err: print ('err ', end='', flush=True) ##############
        if not err:
            s2 = copy.copy(s)
            s3 = copy.copy(s)
            start = datetime.datetime.now()
            s2, message, level, solved, err = solve(s2, 0, maxdepth, maxtime)
            dt = datetime.datetime.now() - start
            # print (status(level, solved, err)+' ', end='', flush=True) #######
#            if dt.seconds > maxtime - 2:
            # print ('\n{0} seconds for {1}: {2}'.format(dt.seconds,status(level, solved, err),short(s3)))
            if not solved and err:
                return (s3, 0)
            if solved:
                break
            err = True

    t = dt.seconds + float(dt.microseconds) / 1000000
    while len(s2) == 2:

        j = []
        p = possible(s)
        maxp = 0
        for i in range(81):
            if s2[0][i] != s2[1][i]:
                j.append([i, sum(p[i])])
                if sum(p[i]) > maxp:
                    maxp = sum(p[i])
        k = []
        for i in range(len(j)):
            if j[i][1] == maxp:
                k.append(j[i][0])
        random.shuffle(k)
        i = k[0]
        s[i] = s2[0][i]
        s = shuffle(s)
        s2 = copy.copy(s)
        start = datetime.datetime.now()
        s2, message, level, solved, err = solve(s2, 0, maxdepth, maxtime + 3)
        dt = datetime.datetime.now() - start
        t = dt.seconds + float(dt.microseconds) / 1000000

    if level < 3:
        s = make_easy(s)
        if blank(s) < 30:
            level = 1

    return (s, level)


def make_easy(s):
    s2 = copy.copy(s)
    sol, message, level, solved, err = solve(s2, 0, 1, 1)
    if not solved or err:
        return(s)
    if blank(s) < 25:
        return s
    if blank(s) < 43:
        level = 1
    else:
        level = random.randint(1, 2)
    if level == 1:
        bl = random.randint(24, 28)
    else:
        bl = random.randint(37, 43)
    fill = blank(s) - bl
    cell = []
    for i in range(81):
        if s[i] == 0:
            cell.append(i)
    random.shuffle(cell)
    for i in range(fill):
        s[cell[i]] = sol[cell[i]]

    return s


def shuffle(s):
    # rotate right
    s2 = [0] * 81
    for i in range(9):
        for j in range(9):
            s2[j * 9 + 8 - i] = s[i * 9 + j]
    s = copy.copy(s2)
    # mirror 50%
    if random.randint(1, 2) == 1:
        for i in range(9):
            for j in range(9):
                s2[i * 9 + 8 - j] = s[i * 9 + j]
    s = copy.copy(s2)
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(n)
    for i in range(81):
        if s[i] == 0:
            s2[i] = 0
        else:
            s2[i] = n[s[i] - 1]
    return (s2)


def merge(file, file2):
    if file == '':
        return
    if file2 == '':
        return
    input = open(file, 'r')
    problem = []
    new = []
    for line in input:
        data = line.strip().split(' ')
        problem.append(data[1])
    input.close
    n = countproblem(file2)
    print('Importing {0} problems.'.format(n))
    input = open(file2, 'r')
    j = 0
    k = 0
    output = openappend(file)
    if output == 'error':
        print('Unable to write a file:', file)
        return
    for line in input:
        k += 1
        data = line.strip().split(' ')
        if data[1] not in problem:
            j += 1
            output.write(line)
    input.close
    output.close
    print('{0} / {1} problems appended.'.format(j, k))
    return


def countproblem(file):
    input = open(file, 'r')
    n = 0
    for line in input:
        data = line.strip().split(' ')
        if conv(data[1])[1] == False:
            n += 1
    input.close
    return(n)


def reanalyze_giveup(giveup, t):
    maxdepth = 999  # Creating mode
    give = givedata(giveup, t)
    for i in give[4]:
        print('Invalid data: ', i)
    if len(give[3]) == 0:
        print('No position to analyze.')
        return
    print('Reanalyzing {0} giveup positions for {1} seconds.'.format(
        len(give[3]), t))
    while True:
        give = givedata(giveup, t)
        if len(give[3]) == 0:
            break
        prob = give[3][0][1]
        s, err = conv(prob)
        print('Analyzing ... ', end='', flush=True)
        start = datetime.datetime.now()
        dt = datetime.datetime.now() - start
        s, message, level, solved, err = solve(s, 0, maxdepth, t)
        if solved:
            if err:  # Discard multiple solutions
                give = givedata(giveup, t)
                give[3] = give[3][1:]
                writegive(giveup, give)
                print('multiple solutions. {0} left.'.format(len(give[3])))
            else:
                give = givedata(giveup, t)
                give[3] = give[3][1:]
                give[0].append('u ' + str(dt.seconds) + ' ' + prob)
                writegive(giveup, give)
                print('unique solution. {0} left.'.format(len(give[3])))
        else:
            if err:
                give = givedata(giveup, t)
                give[3] = give[3][1:]
                if dt.seconds > 3:  # Discard no solution shorter than 3 seconds
                    give[1].append('n ' + str(dt.seconds) + ' ' + prob)
                writegive(giveup, give)
                print('no solution. {0} left.'.format(len(give[3])))
            else:
                give = givedata(giveup, t)
                give[3] = give[3][1:]
                give[2].append('g ' + str(t) + ' ' + prob)
                writegive(giveup, give)
                print('give up. {0} left.'.format(len(give[3])))
    return


def givedata(giveup, t):
    input = open(giveup, 'r')
    uniq = []
    no = []
    long = []
    short = []
    invalid = []
    for line in input:
        data = line.strip().split(' ')
        if data[0] == 'u':
            uniq.append(line)
            continue
        if data[0] == 'n':
            no.append(line)
            continue
        if data[0] == 'g':
            if conv(data[1])[1]:
                t2 = int(data[1])
                s = data[2]
            else:
                t2 = 3
                s = data[1]
            if t2 < t:
                short.append([t2, s])
                continue
            else:
                long.append(line)
                continue
        invalid.append(line)
    input.close
    g = [uniq, no, long, short, invalid]
    return(g)


def writegive(giveup, g):
    try:
        output = open(giveup, 'w')
    except:
        print('Unable to write a file:', giveup)
        return
    for i in range(3):
        for j in g[i]:
            output.write(j.strip() + '\n')
    for i in g[3]:
        output.write('g ' + str(i[0]) + ' ' + i[1] + '\n')
    output.close
    return
