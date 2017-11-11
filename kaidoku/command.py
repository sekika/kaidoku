# -*- coding: utf-8 -*-
"""Modules for commandline interpretation."""
import copy
import datetime
import os.path
import sys

from configobj import ConfigObj

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


def command(arg, config):
    """Interpret command."""
    import shutil
    import webbrowser
    c = arg[0]
    if c == 'a' or c == 'ac':
        bookmark = config["bookmark"]
        move2 = config["move"]
        if c == 'a':
            config["move"] = []
        if len(arg) > 1:
            try:
                verbose = int(arg[1])
            except Exception:
                verbose = 1
        else:
            verbose = 1
        config, err = show(c, verbose, config)
        config["move"] = move2
        return config
    if c == 'b':
        move = config["move"]
        if move == []:
            print('Take back unavaillable because we are at initial position.')
            return config
        config["move"] = move[:len(move) - 1]
        config, err = show(c, 0, config)
        config = command(['c'], config)
        return config
    if c == 'c' or c == 'u' or c == 'jpg' or c == 'jm':
        config, err = show(c, 0, config)
        if err:
            print('Going back to problem No. 1.')
            level = config['level']
            pointer = config['pointer']
            pointer[level] = 1
            config['pointer'] = pointer
            config, err = show(c, 0, config)
            if err:
                print(
                    'There is no problem in level ' + config['level'] +
                    '. Change level with l command.')
                return config
        return config
    if c == 'h':
        print(helpmessage())
        return config
    if c == 'ha':
        print(advancedhelp())
        return config
    if c == 'i' or c == 'ii' or c == 'iii':
        config, err = show(c, 0, config)
        return config
    if c == 'l':
        level = int(config["level"])
        try:
            le = int(arg[1])
        except Exception:
            return config
        if le > 0 and le < 10:
            level = le
            config['level'] = level
        config['move'] = []
        config = command(['c'], config)
        return config
    if c == 'n' or c == 'p' or c == 'j' or c == 'initial':
        pointer = config['pointer']
        level = int(config['level'])
        n = pointer[level]
        if int(config["level"]) == 0:
            if c == 'n' or c == 'p':
                return config
        else:
            n = int(n)
        n2 = n
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
        pointer = config['pointer']
        pointer[level] = n
        config['pointer'] = pointer
        config['move'] = []
        config, err = show(c, 0, config)
        if err:
            pointer[level] = n2
            config['pointer'] = pointer
        return config
    if c.isdigit():  # move
        move = config["move"]
        row = int(c) // 100
        if row < 1 or row > 9:
            print('Invalid move. If you want to fill Row 3' +
                  'Column 5 with 7, type 357.')
            return config
        column = int(int(c) - row * 100) // 10
        num = int(c) % 10
        i = (row - 1) * 9 + column - 1
        move.append(int(c))
        config['move'] = move
        config, err = show(c, 0, config)
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
        # If filename is written in bookmark, read bookmark from the file
        if type(config['bookmark']) is str:
            confbookmark = ConfigObj(
                os.path.expanduser(bookmark), encoding='utf-8')
            bookmark = confbookmark['bookmark']
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
                        'Valid sudoku. Appended to the book by level' +
                        +str(level))
                else:  # Add to bookmark
                    problem = short(s2)
                    comment = ''
                    if 'bookmark' in config:
                        bookmark = config['bookmark']
                        # If filename is written in bookmark, read bookmark from the file
                        if type(config['bookmark']) is str:
                            bookmark = ConfigObj(os.path.expanduser(
                                bookmark), encoding='utf-8')['bookmark']
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
                    if type(config['bookmark']) is str:
                        confbookmark['bookmark'] = bookmark
                        confbookmark.write()
                    else:
                        config['bookmark'] = bookmark
        else:
            if err:
                print('This sudoku has no solution.')
            else:
                print(
                    'This sudoku cannot be solved in ' +
                    str(maxtime) + ' seconds.')
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
        creation = config["create"]
        print('Creating {0} new problems.'.format(n))
        append_database(file, giveup, n, creation)
        return config
    if c == 'ba':  # add bookmark
        file = os.path.expanduser(config["file"])
        level = int(config["level"])
        pointer = config['pointer']
        move = config["move"]
        bookmark = config["bookmark"]
        # If filename is written in bookmark, read bookmark from the file
        if type(bookmark) is str:
            confbookmark = ConfigObj(
                os.path.expanduser(bookmark), encoding='utf-8')
            bookmark = confbookmark['bookmark']
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
                    'Level {0} no. {1} not found. ' +
                    'Going back to no. 1'.format(level, n))
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
                config['move'] = move
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
            # If filename is written in bookmark, read bookmark from the file
            if type(bookmark) is str:
                confbookmark = ConfigObj(
                    os.path.expanduser(bookmark), encoding='utf-8')
                bookmark = confbookmark['bookmark']
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
        if type(config['bookmark']) is str:
            confbookmark['bookmark'] = bookmark
            confbookmark.write()
        else:
            config['bookmark'] = bookmark
        return config
    if c == 'bl':
        if 'bookmark' in config:
            bookmark = config['bookmark']
            # If filename is written in bookmark, read bookmark from the file
            if type(bookmark) is str:
                bookmark = ConfigObj(os.path.expanduser(
                    bookmark), encoding='utf-8')['bookmark']
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
        if 'bookmark' in config:
            bookmark = config['bookmark']
            # If filename is written in bookmark, read bookmark from the file
            if type(bookmark) is str:
                confbookmark = ConfigObj(
                    os.path.expanduser(bookmark), encoding='utf-8')
                bookmark = confbookmark['bookmark']
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
        config['level'] = 0
        pointer = config['pointer']
        pointer[0] = n
        config['pointer'] = pointer
        if type(config['bookmark']) is str:
            confbookmark['bookmark'] = bookmark
            confbookmark.write()
        else:
            config['bookmark'] = bookmark
        config['move'] = move
        config, err = show(c, 0, config)
        return config
    if c == 'giveup':
        if len(arg) > 1:
            t = int(arg[1])
        else:
            t = 10
        giveup = os.path.expanduser(config["giveup"])
        reanalyze_giveup(giveup, t)
        return config
    if c == 'html':
        datadir = config['datadir']
        html = os.path.join(datadir, 'sudoku.html')
        here = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(os.path.join(here, 'data/sudoku.html'), html)
        webbrowser.open('file://' + html)
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
        config, err = show(c, 0, config)
        return config

    # Following commands are for debugging and not in help
    if c == 'test':
        from kaidoku.test import test_all
        test_all()
        config2 = copy.copy(config)
        print('Start testing commands.')
        for c in ['book', 'config', 'l 8', 'j 1', '131', '218', 'h', 'ha', 'c', 'u',
                  'jpg', 'jm', 'b', 'i', 'initial', 'j 2', 'n', 'p', 'a 3', 'ac', 'sp', 'ii', 'iii', 'bl', 'br b1',
                  'solve 407001008105090040000570300900083000000000206040900000510000000090160800070000030']:
            print('Testing command ' + c)
            c = c.split()
            config = command(c, config)
        print('\nFinished testing.')
        print('Not tested: all, append, bp, ba, create, giveup, import, reanalyze')
        return config2

    if c == 'createtest':
        from kaidoku.create import create
        maxtime = 3
        maxdepth = 999  # Creating mode
        level = 0
        while level == 0:
            s, level = create(maxdepth,  maxtime, False)
        print(output(s))
        return config

    print('Invalid command. Type h for help.')
    return config


def show(c, verbose, config):
    """Show current position."""
    file = os.path.expanduser(config["file"])
    move = config["move"]
    level = int(config["level"])
    pointer = config['pointer']
    maxtime = int(config['maxtime'])
    bookmark = config["bookmark"]
    # If filename is written in bookmark, read bookmark from the file
    if type(config['bookmark']) is str:
        bookmark = ConfigObj(os.path.expanduser(bookmark),
                             encoding='utf-8')['bookmark']
    n = pointer[level]
    datadir = config["datadir"]
    infile = open(file, 'r')
    no = 0
    if level == 0:  # bookmark
        if n not in bookmark:
            print('Label {0} not found in bookmark.'.format(n))
            return config, False
        if 'problem' not in bookmark[n]:
            print('Label {0} broken.'.format(n))
            return config, False
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
            return config, True  # not found

    s, err = conv(problem)

    if err:
        print(s)
        print('This problem is not valid.')
        return config, True

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
            config['move'] = move
            print(message)
        if blank(s) == 0:
            label += ': solution'
        else:
            label += ': move ' + str(len(move))
    if c == 'c' or c == 'n' or c == 'p' or c == 'j' or c == 'initial' or c.isdigit():
        print(label)
        print(output(s))
        if blank(s) == 0:
            print('Now this problem is solved !')
        else:
            print('Type 3 digits (row, column, number) to put a number. i for hint.')
        if datadir != '':
            size = 'medium'
            datadir = checkdatadir(datadir)
            config['datadir'] = datadir
            imgfile = datadir + '/current.jpg'
            figure = config['figure']
            err = drawimage(s, '', label, size, imgfile,
                            figure, False)
            if not err:
                print('See image by "html".')

    if c == 'a' or c == 'ac':
        print('\n' + label)
        solveprint(s, verbose, blank(s), maxtime)
    if c == 'u':
        print(url(s))
    if c == 'jpg' or c == 'jm':  # jpg
        p = possible(s)
        datadir = checkdatadir(datadir)
        config['datadir'] = datadir
        imgfile = datadir + '/current.jpg'
        if c == 'jpg':
            size = 'medium'
            mark = False
        if c == 'jm':
            size = 'large'
            mark = True
        figure = config['figure']
        err = drawimage(s, p, label, size, imgfile, figure, mark)
        if not err:
            print('See image by "html".')
    if c == 'i' or c == 'ii' or c == 'iii' or c == 'sp':  # prepare solving
        if blank(s) == 0:
            print('Already solved.')
            return config, True
        s2 = copy.copy(s)
        s2, message, level2, solved, err = solve(s2, 0, blank(s), maxtime)
        if err:
            if solved:
                print('This position has multiple solutions.')
            else:
                print(
                    'There is no solution for this position. '
                    + 'You can take back one move with b.')
            return config, True
        p = possible(s)
        b = box()
        pb = pbox()
        blank1 = blank(s)
        start = datetime.datetime.now()
        endtime = start + datetime.timedelta(seconds=maxtime)
    if c == 'i' or c == 'ii' or c == 'iii':  # show hint
        s2 = copy.copy(s)
        s2, p, message, logic, depth, found, err = solveone(
            s2, p, 4, 0, blank1, endtime, b, pb)
        if logic == 'Naked single' or logic == 'Hidden single':
            if logic == 'Naked single':
                print('Look at {0}. What number is available?'.format(
                    message[14:18]))
            else:
                print(message[:message.index(':')] + 'can be found.')
        else:
            if c == 'i':
                print('Think candidates of the cells.')
                if datadir == '':
                    print('Use jm command to see the diagram of candidates.')
                else:
                    size = 'large'
                    datadir = checkdatadir(datadir)
                    config['datadir'] = datadir
                    imgfile = datadir + '/current.jpg'
                    p = possible(s)
                    figure = config['figure']
                    err = drawimage(s, p, label, size, imgfile,
                                    figure, True)
                    if not err:
                        print('See image by "html".')
                print('For more hints, type ii.')
            if c == 'ii' or c == 'iii':
                logi = [logic]
                mes = [message]
                while blank(s2) == blank1:
                    s2, p, message, logic, depth, found, err = solveone(
                        s2, p, 4, 0, blank1, endtime, b, pb)
                    logi.append(logic)
                    mes.append(message)
                if c == 'ii':
                    if len(logi) > 1:
                        print('Following logics are successively used.')
                    for i in range(len(logi)):
                        print(logi[i])
                    print('See full explanation by typing iii.')
                else:
                    for message in mes:
                        print(message)
    if c == 'sp':
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
            else:
                s = s2
        print('\n' + output(s))
        config, err = show('jpg', 0, config)
    return config, False


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
