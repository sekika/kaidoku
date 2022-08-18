import copy
import datetime

from kaidoku.calc import solve
from kaidoku.calc import solveone
from kaidoku.calc import possible
from kaidoku.misc import box
from kaidoku.misc import line
from kaidoku.misc import pbox
from kaidoku.misc import check
from kaidoku.misc import conv
from kaidoku.misc import blank

MAXDEPTH = 20
MAXTIME = 120


class Kaidoku:

    def __init__(self, position):
        self.position = position
        s, err = conv(position)
        self.hints = 0
        if err:
            self.mes = s
            self.valid = False
            return
        self.mes, err = check(s)
        if err:
            self.valid = False
            return
        s2 = copy.deepcopy(s)
        s, self.mes, self.level, found, err = solve(s, 0, MAXDEPTH, MAXTIME)
        s = copy.deepcopy(s2)
        if err:
            self.valid = False
            if found:
                self.mes = 'Multiple solutions to this position'
            else:
                self.mes = 'No solution to this position'
            return
        self.valid = True
        if blank(s) == 0:
            self.mes = 'Already solved'
            return
        start = datetime.datetime.now()
        endtime = start + datetime.timedelta(seconds=MAXTIME)
        p = possible(s)
        b = box()
        pb = pbox()
        linescan = line()
        s, p, self.mes, self.logic, self.depth, found, err = solveone(
            s, p, 4, 0, MAXDEPTH, endtime, b, pb, linescan)
        self.hints = 1
        if self.logic == 'Naked single':
            self.hint = 'Look at {0}. What number is available?'.format(
                self.pos(self.mes[14:18]))
            return
        self.hints = 2
        if self.logic == 'Hidden single':
            mes = self.mes[:self.mes.index(':')]
            self.hint = mes + 'can be found.'
            self.hint2 = mes + 'for ' + self.mes[-1:]
            return
        self.hint = 'Think candidates of the cells.'
        self.hints = 3
        logi = [self.logic]
        mes = [self.mes]
        blank1 = blank(s2)
        while blank(s2) == blank1:
            s2, p, message, logic, depth, found, err = solveone(
                s2, p, 4, 0, blank1, endtime, b, pb, linescan)
            logi.append(logic)
            mes.append(message)
        self.hint2 = 'Use ' + ', '.join(logi) + ' successively.'
        self.hint3 = '\n'.join(mes)

    def pos(self, p):
        return p.replace('R', 'Row:').replace('C', ' Column:')
