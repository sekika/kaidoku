# -*- coding: utf-8 -*-
"""Modules for commandline interpretation."""
import copy
import datetime
from kaidoku.calc import possible
from kaidoku.calc import solve
from kaidoku.calc import solveone
from kaidoku.create import analyze
from kaidoku.create import append_database
from kaidoku.create import merge
from kaidoku.create import reanalyze
from kaidoku.create import reanalyze_giveup
from kaidoku.create import show_status
from kaidoku.help import advancedhelp
from kaidoku.help import helpmessage
from kaidoku.image import drawimage
from kaidoku.misc import blank
from kaidoku.misc import box
from kaidoku.misc import check
from kaidoku.misc import conv
from kaidoku.misc import current
from kaidoku.misc import duplicate
from kaidoku.misc import lev
from kaidoku.misc import openappend
from kaidoku.misc import pbox
from kaidoku.output import output
from kaidoku.output import short
from kaidoku.output import url
import os.path
import sys


def command(arg, config):
    """Interpret command."""
    c = arg[0]
    if c == 'a' or c == 'ac':
        bookmark = config["bookmark"]
        if c == 'a':
            move = []
        else:
            move = config["move"]
        if len(arg) > 1:
            try:
                verbose = int(arg[1])
            except Exception:
                verbose = 1
        else:
            verbose = 1
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        maxtime = int(config['maxtime'])
        n = pointer[level]
        datadir = config["datadir"]
        n, move, datadir = show(file, move, level, n,
                                bookmark, datadir, verbose, maxtime)
        pointer[level] = n
        return config
    if c == 'b':
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        datadir = config["datadir"]
        if move == []:
            print('Take back unavaillable because we are at initial position.')
            return config
        move = move[:len(move) - 1]
        n = pointer[level]
        n, move, datadir = show(file, move, level, n, bookmark, datadir, 0, 0)
        pointer[level] = n
        config['move'] = move
        return config
    if c == 'c' or c == 'u' or c == 'jpg' or c == 'jm':
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        datadir = config["datadir"]
        n = pointer[level]
        if c == 'c':
            type = 0
        if c == 'u':
            type = 6
        if c == 'jpg':
            type = 7
        if c == 'jm':
            type = 8
        n, move, datadir = show(file, move, level, n,
                                bookmark, datadir, type, 0)
        if n == -1:
            print('Going back to problem No. 1.')
            n = 1
            n, move, datadir = show(
                file, move, level, n, bookmark, datadir, 0, 0)
            if n == -1:
                print(
                    'There is no problem in level {0}. Change level with l command.'.format(level))
                return config
        pointer[level] = n
        config['pointer'] = pointer
        config['move'] = move
        config['datadir'] = datadir
        return config
    if c == 'h':
        print(helpmessage())
        return config
    if c == 'ha':
        print(advancedhelp())
        return config
    if c == 'i' or c == 'ii' or c == 'iii':
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        maxtime = int(config['maxtime'])
        n = pointer[level]
        datadir = config["datadir"]
        type = len(c) + 10
        n, move, datadir = show(file, move, level, n,
                                bookmark, datadir, type, maxtime)
        config['datadir'] = datadir
        return config
    if c == 'l':
        level = int(config["level"])
        try:
            l = int(arg[1])
        except Exception:
            return config
        if l > 0 and l < 10:
            level = l
            config['level'] = level
        config = command(['c'], config)
        return config
    if c == 'n' or c == 'p' or c == 'j' or c == 'initial':
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        bookmark = config["bookmark"]
        n = pointer[level]
        datadir = config["datadir"]
        if level == 0:
            if c == 'n' or c == 'p':
                return config
        else:
            n = int(n)
        if c == 'p':
            n -= 1
            if n == 0:
                print('No previous problem.')
                n = 1
                return config
        if c == 'n':
            n += 1
        if c == 'j':
            if len(arg) < 2:
                return config
            try:
                n = int(arg[1])
            except Exception:
                return config
        move = []
        n, move, datadir = show(file, move, level, n, bookmark, datadir, 0, 0)
        if n == -1:
            return config
        pointer[level] = n
        config['pointer'] = pointer
        config['move'] = move
        return config
    if c.isdigit():  # move
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        n = pointer[level]
        move = config["move"]
        bookmark = config["bookmark"]
        row = int(c) // 100
        datadir = config["datadir"]
        if row < 1 or row > 9:
            print('Invalid move. If you want to fill Row 3 Column 5 with 7, type 357.')
            return config
        column = int(int(c) - row * 100) // 10
        num = int(c) % 10
        i = (row - 1) * 9 + column - 1
        move.append(int(c))
        n, move, datadir = show(file, move, level, n, bookmark, datadir, 0, 0)
        config['move'] = move
        return config
    if c == 'all':
        if len(arg) > 1:
            verbose = int(arg[1])
        else:
            verbose = 0
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        analyze(file, level, verbose)
        return config
    if c == 'append' or c == 'bp':
        file = os.path.expanduser(config["file"])
        maxtime = int(config['maxtime'])
        bookmark = config['bookmark']
        if len(arg) > 2:
            verbose = int(arg[2])
        else:
            verbose = 1
        if len(arg) == 1:
            print('Position not specified.')
            return(config)
        try:
            s, err = conv(arg[1])
        except Exception:
            print('Invalid position.')
            return config
        if err:
            print(s)
            return config
        s2 = copy.copy(s)
        s, message, level, solved, err = solve(s, 0, blank(s), maxtime)
        if solved:
            if err:
                print('This sudoku has multiple solutions.')
            else:
                if c == 'append':  # Append to book
                    infile = open(file)
                    for line in infile:
                        data = line.strip().split(' ')
                        s3 = conv(data[1])[0]
                        if s2 == s3:
                            print('This sudoku is already in the book.')
                            infile.close
                            return config
                    infile.close
                    out = openappend(file)
                    if output == 'error':
                        print('Unable to write a file:', file)
                        return config
                    out.write(str(level) + ' ' + short(s2) + '\n')
                    out.close
                    print(
                        'Valid sudoku. Appended to the book by level {0}.'.format(level))
                else:  # Add to bookmark
                    problem = short(s2)
                    comment = ''
                    if 'bookmark' in config:
                        bookmark = config['bookmark']
                        num = 1
                        while 'b' + str(num) in bookmark:
                            num += 1
                        label = 'b' + str(num)
                        for lab in bookmark:
                            if bookmark[lab]['problem'] == problem:
                                label = lab
                                print('Already labeled as {0}'.format(label))
                                if 'comment' in bookmark[label]:
                                    comment = bookmark[label]['comment']
                                    print('Comment = {0}'.format(comment))
                                    break
                                else:
                                    bookmark = {}
                    try:
                        com = input('Comment on this position: ')
                    except Exception:
                        com = ''
                        print('')
                    if com != '':
                        comment = com
                    bookmark[label] = {}
                    bookmark[label]['problem'] = problem
                    bookmark[label]['move'] = ''
                    bookmark[label]['added'] = datetime.datetime.now(
                    ).strftime('%Y/%m/%d')
                    if comment != '':
                        bookmark[label]['comment'] = comment
                    config['bookmark'] = bookmark
        else:
            if err:
                print('This sudoku has no solution.')
            else:
                print(
                    'This sudoku cannot be solved in {0} seconds.'.format(maxtime))
        return config
    if c == 'book':
        file = os.path.expanduser(config["file"])
        show_status(file)
        return config
    if c == "config":
        for i in config:
            if i != 'bookmark':
                print('{0} = {1}'.format(i, config[i]))
        return config
    if c == 'create':
        if len(arg) > 1:
            n = int(arg[1])
        else:
            n = 10
        file = os.path.expanduser(config["file"])
        giveup = os.path.expanduser(config["giveup"])
        print('Creating {0} new problems.'.format(n))
        append_database(file, giveup, n)
        return config
    if c == 'ba':  # add bookmark
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        n = pointer[level]
        if level == 0:  # bookmark
            if n not in bookmark:
                print('Label {0} not found in bookmark.')
                print('Going to level 3.')
                config['level'] = 3
                return config
            if 'problem' not in bookmark[n]:
                print('Label {0} broken.')
                print('Going to level 3.')
                config['level'] = 3
                return config
            problem = bookmark[n]['problem']
        else:
            n = int(n)
            infile = open(file, 'r')
            no = 0
            problem = ''
            for line in infile:
                data = line.strip().split(' ')
                if int(data[0]) == level:
                    no += 1
                    if no == n:
                        infile.close
                        problem = data[1]
                        break
            if problem == '':
                pointer[level] = 1
                print(
                    'Level {0} no. {1} not found. Going back to no. 1'.format(level, n))
                return config
        s, err = conv(problem)
        if err:
            print(s)
            print('This problem is not valid.')
            return config
        s2 = copy.copy(s)
        if len(move) > 0:
            s2, move, message, err = current(s2, move)
            if err:
                print(message)
                return config
        problem = short(s)
        mo = ''
        for i in move:
            mo += str(i)
        if len(arg) > 1:
            label = arg[1]
        else:
            label = 'b1'
        comment = ''
        if 'bookmark' in config:
            bookmark = config['bookmark']
            num = 1
            for i in bookmark:
                num += 1
            label = 'b' + str(num)
            for lab in bookmark:
                if bookmark[lab]['problem'] == problem and bookmark[lab]['move'] == mo:
                    label = lab
                    print('Already labeled as {0}'.format(label))
                    if 'comment' in bookmark[label]:
                        comment = bookmark[label]['comment']
                        print('Comment = {0}'.format(comment))
                    break
        else:
            bookmark = {}
        try:
            com = input('Comment on this position: ')
        except Exception:
            com = ''
            print('')
        if com != '':
            comment = com
        bookmark[label] = {}
        bookmark[label]['problem'] = problem
        bookmark[label]['move'] = mo
        bookmark[label]['added'] = datetime.datetime.now().strftime('%Y/%m/%d')
        if comment != '':
            bookmark[label]['comment'] = comment
        config['bookmark'] = bookmark
        return config
    if c == 'bl':
        if 'bookmark' in config:
            bookmark = config['bookmark']
        else:
            print('No bookmark.')
            return config
        for label in bookmark:
            if 'comment' in bookmark[label]:
                comment = bookmark[label]['comment']
            else:
                comment = ''
            if 'added' in bookmark[label]:
                added = bookmark[label]['added']
            else:
                added = ' ' * 10
            print('{0}   {1}   {2}'.format(added, label, comment))
        return config
    if c == 'br':
        file = os.path.expanduser(config["file"])
        datadir = config["datadir"]
        if 'bookmark' in config:
            bookmark = config['bookmark']
        else:
            print('No bookmark.')
            return config
        if len(arg) == 1:
            print('Label is not specified.')
            return config
        n = arg[1]
        level = 0
        if n not in bookmark:
            print('Label {0} not found in bookmark.'.format(n))
            print('Going to level 3.')
            config['level'] = 3
            return config
        mo = bookmark[n]['move']
        move = []
        while len(mo) > 2:
            move.append(int(mo[:3]))
            mo = mo[3:]
        n, move, datadir = show(file, move, level, n, bookmark, datadir, 0, 0)
        config['level'] = level
        config['move'] = move
        pointer = config['pointer']
        pointer[level] = n
        return config
    if c == 'giveup':
        if len(arg) > 1:
            t = int(arg[1])
        else:
            t = 10
        giveup = os.path.expanduser(config["giveup"])
        reanalyze_giveup(giveup, t)
        return config
    if c == 'import':
        file = os.path.expanduser(config["file"])
        file2 = os.path.expanduser(config["file2"])
        merge(file, file2)
        return config
    if c == 'reanalyze':
        file = os.path.expanduser(config["file"])
        file2 = os.path.expanduser(config["file2"])
        reanalyze(file, file2)
        return config
    if c == 'solve':
        maxtime = int(config['maxtime'])
        if len(arg) > 2:
            verbose = int(arg[2])
        else:
            verbose = 1
        if len(arg) == 1:
            print('Position not specified.')
            return(config)
        try:
            s, err = conv(arg[1])
        except Exception:
            print('Invalid position.')
            return config
        if err:
            print(s)
            return config
        print(output(s))
        message, err = check(s)
        if err:
            print(message)
            return config
        solveprint(s, verbose, blank(s), maxtime)
        return config
    if c == 'sp':
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        maxtime = int(config['maxtime'])
        datadir = config["datadir"]
        n = pointer[level]
        type = 20
        n, move, datadir = show(file, move, level, n,
                                bookmark, datadir, type, maxtime)
        config['move'] = move
        pointer[level] = n
        return config
    print('Invalid command. Type h for help.')
    return config


def show(file, move, level, n, bookmark, datadir, type, maxtime):
    """Show current position."""
    infile = open(file, 'r')
    no = 0
    if level == 0:  # bookmark
        if n not in bookmark:
            print('Label {0} not found in bookmark.')
            return n, move, datadir
        if 'problem' not in bookmark[n]:
            print('Label {0} broken.')
            return n, move, datadir
        problem = bookmark[n]['problem']
    else:
        n = int(n)
        infile = open(file, 'r')
        no = 0
        problem = ''
        for line in infile:
            data = line.strip().split(' ')
            if int(data[0]) == level:
                no += 1
                if no == n:
                    infile.close
                    problem = data[1]
                    break
        infile.close
        if problem == '':
            print('Level {0} no. {1} not found.'.format(level, n))
            return -1, move, datadir  # not found

    s, err = conv(problem)

    if err:
        print(s)
        print('This problem is not valid. Going to next problem.')
        return n + 1, move, datadir

    if level == 0:
        if 'comment' in bookmark[n]:
            label = bookmark[n]['comment']
        else:
            label = str(n)
    else:
        label = 'Level ' + str(level) + ' No. ' + str(n)
    if len(move) > 0:
        s, move, message, err = current(s, move)
        if err:
            print(message)
        if blank(s) == 0:
            label += ': solution'
        else:
            label += ': move ' + str(len(move))
    if type == 0:  # show
        print(label)
        print(output(s))
        if blank(s) == 0:
            print('Now this problem is solved !')
        else:
            print('Type 3 digits (row, column, number) to put a number. i for hint.')
    if type > 0 and type < 6:
        print('\n' + label)
        solveprint(s, type, blank(s), maxtime)
    if type == 6:  # url
        print(url(s))
    if type == 7 or type == 8:  # jpg
        p = possible(s)
        textcolor = 'black'
        datadir = checkdatadir(datadir)
        imgfile = datadir + '/current.jpg'
        if type == 7:
            size = 'small'
            mark = False
        if type == 8:
            size = 'medium'
            mark = True
        drawimage(s, p, label, size, textcolor, imgfile, mark)
        print('Image file created: ' + imgfile)
    if type == 11 or type == 12 or type == 13 or type == 20:  # prepare solving
        if blank(s) == 0:
            print('Already solved.')
            return n, move, datadir
        s2 = copy.copy(s)
        s2, message, level2, solved, err = solve(s2, 0, blank(s), maxtime)
        if err:
            if solved:
                print('This position has multiple solutions.')
            else:
                print(
                    'There is no solution for this position.'
                    + 'You can take back one move with b.')
            return n, move, datadir
        p = possible(s)
        b = box()
        pb = pbox()
        blank1 = blank(s)
        start = datetime.datetime.now()
        endtime = start + datetime.timedelta(seconds=maxtime)
    if type == 11 or type == 12 or type == 13:  # show hint
        s2, p, message, logic, depth, found, err = solveone(
            s, p, 4, 0, blank1, endtime, b, pb)
        if logic == 'Naked single' or logic == 'Hidden single':
            if logic == 'Naked single':
                print('Look at {0}. What number is available?'.format(
                    message[14:18]))
            else:
                print(message[:message.index(':')] + 'can be found.')
        else:
            if type == 11:
                print('Think candidates of the cells.')
                size = 'medium'
                textcolor = 'black'
                imgfile = os.path.abspath(
                    os.path.dirname(file)) + '/current.jpg'
                p = possible(s)
                drawimage(s, p, label, size, textcolor, imgfile, True)
                print('Image file: ' + str(imgfile))
                print('For more hints, type ii.')
            if type == 12 or type == 13:
                logi = [logic]
                mes = [message]
                while blank(s2) == blank1:
                    s, p, message, logic, depth, found, err = solveone(
                        s, p, 4, 0, blank1, endtime, b, pb)
                    logi.append(logic)
                    mes.append(message)
                if type == 12:
                    if len(logi) > 1:
                        print('Following logics are successively used.')
                    for i in range(len(logi)):
                        print(logi[i])
                    print('See full explanation by typing iii.')
                else:
                    for message in mes:
                        print(message)
    if type == 20:  # Solve partially
        logic = 'Naked single'
        while (logic == 'Naked single' or logic == 'Hidden single') and blank(s) > 0:
            s2 = copy.copy(s)
            s, p, message, logic, depth, found, err = solveone(
                s, p, 4, 0, blank(s), endtime, b, pb)
            if logic == 'Naked single' or logic == 'Hidden single':
                print(message)
            for i in range(81):
                if s[i] != s2[i]:
                    j = (i // 9) * 10 + i % 9 + 11
                    m = j * 10 + s[i]
                    move.append(m)
        print('\n' + output(s))
    return n, move, datadir


def checkdatadir(datadir):
    """Check data directory."""
    if datadir == '':
        print('Data directory does not exist.')
        while True:
            datadir = input(
                'Input name of the data directory (default: ~/kaidoku): ')
            if datadir == '':
                datadir = os.path.expanduser('~/kaidoku')
            datadir = os.path.expanduser(datadir)
            if not os.path.isdir(datadir):
                try:
                    os.mkdir(datadir)
                    break
                except Exception:
                    print('Error: directory cannot be created.', datadir)
                datadir = ''
            else:
                break
    return datadir


def solveprint(s, verbose, maxdepth, maxtime):
    """Analyze a problem (from a command through show)."""
    s, message, level, solved, err = solve(s, verbose, maxdepth, maxtime)
    if err:
        if verbose > 0:
            print(message)
        if solved:
            if verbose > 0:
                print("Invalid sudoku with multiple solutions.")
            if verbose > 4:
                print('Solution 1.')
                print(output(s[0]))
                print('Solution 2.')
                print(output(s[1]))
                s = duplicate(s[0], s[1])
                print('Common numbers in the 2 solutions')
                print(output(s))
        else:
            if verbose > 0:
                print("Invalid sudoku with no solution.")
        sys.exit()
    if solved:
        if verbose > 0:
            print('Valid sudoku with unique solution of level {0} ({1}).'.format(
                level, lev(level)))
        if verbose == 4:
            print('Here is the solution.')
            print(output(s))
    else:
        print('\nGive up with {0} blank cells.'.format(blank(s)))
        print(output(s))

    return
