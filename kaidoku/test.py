# -*- coding: utf-8 -*-
"""modules for tests."""


def test_all():
    """do all the tests in this module"""
    test_calc()
    test_command()
    print('Test completed without error.')
    return


def test_command():
    """test modules in calc.py, wing.py, and chain.py."""
    from kaidoku.command import command
    import os
    import sys
    config = {}
    config['datadir'] = ''
    config['file'] = os.path.abspath(
        os.path.dirname(__file__)) + '/data/sudoku.txt'
    config['level'] = 2
    config['maxtime'] = 60
    config['pointer'] = [''] + [1] * 9
    config['move'] = []
    config['bookmark'] = {}
    config['bookmark']['b1'] = {}
    config['bookmark']['b1']['problem'] = '000001058581094302206080010100960820008402100020018500010036709009100005760809031'
    config['bookmark']['b1']['move'] = ''
    config['bookmark']['b1']['added'] = '2017/11/14'
    config['bookmark']['b1']['comment'] = 'XYZ-wing'
    redirect = os.path.abspath(
        os.path.dirname(__file__)) + '/data/redirect'
    stdout = sys.stdout
    for c in [
        ['book', 'Level 1 trivial'],
        ['l 2', 'Level 2 No. 1'],
        ['299', 'Level 2 No. 1: move 1'],
        ['initial', 'Level 2 No. 1\n'],
        ['299', 'Level 2 No. 1: move 1'],
        ['278', 'Level 2 No. 1: move 2'],
        ['592', 'Both R5C8 and R5C9 have the same value of 2.'],
        ['591', 'Level 2 No. 1: move 3'],
        ['i', 'Look at R1C2. What number is available?'],
        ['a 3', '\nLevel 2 No. 1\nValid sudoku with unique solution'],
        ['ac', '\nLevel 2 No. 1: move 3\nValid sudoku with unique solution'],
        ['658', 'Level 2 No. 1: move 4'],
        ['i', 'There is no solution for this position.'],
        ['h', '246 : In the cell of row 2 column 4, put number 6'],
        ['ha', 'a [verb]'],
        ['c', 'Level 2 No. 1: move 4'],
        ['u', 'http://www.sudoku-solutions.com/index.php?puzzle=900850'],
        ['b', 'Level 2 No. 1: move 3'],
        ['j 3', 'Level 2 No. 3'],
        ['n', 'Level 2 No. 4'],
        ['p', 'Level 2 No. 3'],
        ['j 1', 'Level 2 No. 1'],
        ['sp', 'Naked single: R1C2 = 6, R1C6 = 7,'],
        ['l 5', 'Level 5 No. 1'],
        ['sp', 'Naked single: R4C4 = 4'],
        ['ii', 'Following logics are successively used.'],
        ['iii', 'Pointing pair in box 1 removed 5 from R9C3 R7C3'],
        ['bl', '2017/11/14   b1   XYZ-wing'],
        ['br b1', ''],
        ['c', 'XYZ-wing'],
        ['sp', 'Naked single: R8C6 = 7'],
        ['1234', 'Invalid move. If you want to fill'],
        ['iii', '''Pointing pair in box 4 removed 5 from R4C3 
Pointing pair in box 6 removed 6 from R5C8 R6C8 
Naked pair in row 7 made removal from R7C3
Hidden pair in box 7: R7C3 R9C3
XYZ-wing of R3C4 (3, 5, 7) R3C6 (3, 5) R6C4 (3, 7) removes 3 from R1C4.
Pointing triple in box 1 removed 3 from R3C2 
Hidden pair in box 2: R3C4 R3C6
Chain of pairs. If R5C8 is 7 there is no solution because of following chain.
R5C8 (7,9) = 7
R5C5 (5,7) = 5
R4C6 (3,5) = 3
R6C4 (3,7) = 7
R2C4 (6,7) = 6
R2C8 (6,7) = no candidate
Therefore R5C8 should be 9. '''],
        ['solve -4-3---9-,---------,-----4236,7924--3--,----8----,--1--3627,1385-----,--------4,-7---9-6-', '''  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|  4  |3    |  9  |
2|     |     |     |
3|     |    4|2 3 6|
 +-----+-----+-----+
4|7 9 2|4    |3    |
5|     |  8  |     |
6|    1|    3|6 2 7|
 +-----+-----+-----+
7|1 3 8|5    |     |
8|     |     |    4|
9|  7  |    9|  6  |
 +-----+-----+-----+


Invalid sudoku with multiple solutions.'''],
        ['check 003500902082793006900201830240070003830010020617352498021039004300005200008027300 4', '''  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|    3|5    |9   2|
2|  8 2|7 9 3|    6|
3|9    |2   1|8 3  |
 +-----+-----+-----+
4|2 4  |  7  |    3|
5|8 3  |  1  |  2  |
6|6 1 7|3 5 2|4 9 8|
 +-----+-----+-----+
7|  2 1|  3 9|    4|
8|3    |    5|2    |
9|    8|  2 7|3    |
 +-----+-----+-----+

Pointing pair in box 4 removed 5 from R3C3 
Pointing pair in box 4 removed 9 from R8C3 
Pointing pair in box 9 removed 1 from R8C8 R9C8 
Naked pair in row 3 made removal from R3C2
Naked pair in column 9 made removal from R8C9 R9C9
XYZ-wing of R8C5 (4, 6, 8) R7C4 (6, 8) R8C3 (4, 6) removes 6 from R8C4.
XYZ-wing of R7C7 (5, 6, 7) R9C8 (5, 6) R7C1 (5, 7) removes 5 from R7C8.
Trial. If R8C9 is 1,
(1) Naked single: R9C9 = 9
(2) Hidden single in box 7 : R8C2 = 9
(3) Hidden single in box 7 : R7C1 = 7
(4) Hidden single in box 8 : R9C4 = 1
(5) Hidden single in box 9 : R8C8 = 7
(6) Hidden single in box 3 : R3C9 = 7
(7) Naked single: R3C2 = 5, R5C9 = 5
(8) Naked single: R5C3 = 9, R9C2 = 6
(9) Naked single: R1C2 = 7, R4C3 = 5, R8C3 = 4, R9C8 = 5
(10) Contradiction: R9C1 has no candidate.
Therefore R8C9 is 9.'''],
        ['solve 407001008105090040000570300900083000000000206040900000510000000090160800070000030', '''  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|4   7|    1|    8|
2|1   5|  9  |  4  |
3|     |5 7  |3    |
 +-----+-----+-----+
4|9    |  8 3|     |
5|     |     |2   6|
6|  4  |9    |     |
 +-----+-----+-----+
7|5 1  |     |     |
8|  9  |1 6  |8    |
9|  7  |     |  3  |
 +-----+-----+-----+

Valid sudoku with unique solution'''],
        ['solve 034020000800001700000050620000000907001409800409000000098040000002500006000030410 2', '''  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|  3 4|  2  |     |
2|8    |    1|7    |
3|     |  5  |6 2  |
 +-----+-----+-----+
4|     |     |9   7|
5|    1|4   9|8    |
6|4   9|     |     |
 +-----+-----+-----+
7|  9 8|  4  |     |
8|    2|5    |    6|
9|     |  3  |4 1  |
 +-----+-----+-----+

Determine R9C1 by trial.
Search with depth 1 from R5C5.
Valid sudoku with unique solution of level 8 (extreme).'''],
        ['solve 427001008105090040000570300900083000000000206040900000510000000090160800070000030', '''  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|4 2 7|    1|    8|
2|1   5|  9  |  4  |
3|     |5 7  |3    |
 +-----+-----+-----+
4|9    |  8 3|     |
5|     |     |2   6|
6|  4  |9    |     |
 +-----+-----+-----+
7|5 1  |     |     |
8|  9  |1 6  |8    |
9|  7  |     |  3  |
 +-----+-----+-----+

This sudoku has no solution because R8C1 has no candidate.
Invalid sudoku with no solution.''']
    ]:
        com = c[0].split()
        sys.stdout = open(redirect, 'w')
        config = command(com, config)
        sys.stdout = stdout
        infile = open(redirect, 'r')
        out = ''
        for line in infile:
            out += line
        length = len(c[1])
        assert c[1][:length] == out[:length], 'Error of assertion that ' + \
            c[0] + ' begins with ' + c[1] + '\n' + out
    os.remove(redirect)
    return


def test_calc():
    """test modules in calc.py, wing.py, and chain.py.

    Also testing misc.py that are used from these modules
    """
    import copy
    import datetime
    # Following modules are tested
    from kaidoku.calc import hidden
    from kaidoku.calc import hidsing
    from kaidoku.calc import naked
    from kaidoku.calc import naksing
    from kaidoku.calc import pointing
    from kaidoku.calc import possible
    from kaidoku.calc import solve
    from kaidoku.calc import solveone
    from kaidoku.chain import pairchain
    from kaidoku.chain import remotepair
    from kaidoku.misc import box
    from kaidoku.misc import boxlist
    from kaidoku.misc import combmir
    from kaidoku.misc import conv
    from kaidoku.misc import line
    from kaidoku.misc import pairs
    from kaidoku.misc import pbox
    from kaidoku.misc import wingpos
    from kaidoku.wing import xwing
    from kaidoku.wing import xywing
    from kaidoku.wing import xyzwing
    problem = '013003000002040800098000000850007930000504000023900056000000360005090400000600010'
    s, err = conv(problem)
    s2 = copy.copy(s)
    s2, message, level, solved, err = solve(s2, 1, 10, 5)
    assert message == 'Both R1C3 and R1C6 have the same value of 3.', 'Error in solve'
    problem = '010003000002040800098000000850007930000504000023900056000000360005090400000600010'
    s, err = conv(problem)
    assert s[:9] == [0, 1, 0, 0, 0, 3, 0, 0, 0], 'Error in conv'
    s2 = copy.copy(s)
    s2, message, level, solved, err = solve(s2, 1, 10, 5)
    assert message == 'Solved', 'Error in solve'
    p = possible(s)
    assert p[0] == [0, 0, 0, 1, 1, 1, 1, 0, 0], 'Error in possible'
    b = box()
    assert b[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18,
                    19, 20, 27, 36, 45, 54, 63, 72], 'Error in box'
    pb = pbox()
    linescan = line()
    assert pb[(0, 0)] == {3, 4, 5, 6, 7, 8}, 'Error in pbox'
    start = datetime.datetime.now()
    endtime = start + datetime.timedelta(seconds=3)
    s, p, message, logic, depth, found, err = solveone(
        s, p, 4, 0, 3, endtime, b, pb, linescan)
    assert message == 'Hidden single in box 2 : R2C6 = 9', 'Error in solveone'
    s, p, message, found, err = naksing(s, p, b, 4)
    assert message == 'Naked single: R2C8 = 7', 'Error in naksing'
    s, err = conv(
        '085002000970601000020000000000500073001203900260004000000000080000409061000700530')
    p = possible(s)
    linescan = line()
    assert linescan[0] == [0, 1, 2, 9, 10, 11, 18, 19, 20], 'Error in line'
    s, p, message, found, err = hidsing(s, p, linescan, 4)
    assert message == 'Hidden single in box 4 : R6C3 = 3', 'Error in hidsing'
    s, err = conv(
        '178500390396000205452093810621384759587169432934275168263450980805900603709030520')
    p = possible(s)
    s, p, logic, message, found, err = pointing(s, p, pb, 4)
    assert message == 'Pointing pair in box 2 removed 7 from R2C6 ', 'Error in pointing'
    s, err = conv(
        '700060050501080000060002008040000007600803905900000020100700090000010206030090001')
    p = possible(s)
    boxl = boxlist(s)
    assert boxl[0] == [1, 2, 10, 18, 20], 'Error in boxlist'
    assert boxl[1] == [3, 5, 12, 14, 21, 22], 'Error in boxlist'
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = naked(
        s, p, 2, boxl, comb, 4)
    assert message == 'Naked pair in column 9 made removal from R1C9', 'Error in naked'
    s, err = conv(
        '250400068960020000041600200586142379192367080734985612000006800000090056670004023')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    assert comb[0] == [(3, 7), (3, 7, 8), (3, 8)], 'Error in combmir'
    assert mirror[0] == [[3, 7, 8], [
        (0, 1, 2), (0, 1), (1, 2)]], 'Error in combmir'
    s, p, message, found, err = naked(
        s, p, 3, boxl, comb, 4)
    assert message == 'Naked triple in box 7 made removal from R7C3 R9C3', 'Error in naked'
    s, err = conv(
        '528641739614937258793500641902000017487195326100000980870403192301209000209010003')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = hidden(
        s, p, 2, boxl, mirror, 4)
    assert message == 'Hidden pair in row 9: R9C2 R9C7', 'Error in hidden'
    s, err = conv(
        '000039760006000004700500010900608030560390002310705006070083001200000803003450000')
    p = possible(s)
    boxl = boxlist(s)
    found = True
    while found:
        comb, mirror = combmir(p, boxl)
        s, p, message, found, err = naked(
            s, p, 2, boxl, mirror, 4)
    s, p, message, found, err = hidden(
        s, p, 3, boxl, mirror, 4)
    assert message == 'Hidden triple in row 2: R2C2 R2C7 R2C8', 'Error in hidden'
    s, err = conv(
        '320456000014200000070008040006020009050000020192080400941500070200801904000940031')
    p = possible(s)
    found = True
    while found:
        s, p, logic, message, found, err = pointing(s, p, pb, 4)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = naked(
        s, p, 2, boxl, comb, 4)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = naked(
        s, p, 4, boxl, comb, 4)
    assert message == 'Naked quad in box 3 made removal from R2C7 R2C9', 'Error in nakquad'
    # Hidden Quads example by Klaus Brenner at http://www.sudokuwiki.org/Hidden_Candidates
    s, err = conv(
        '901500046425090081860010020502000000019000460600000002196040253200060817000001694')
    p = possible(s)
    found = True
    while found:
        s, p, logic, message, found, err = pointing(s, p, pb, 4)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = naked(
        s, p, 2, boxl, comb, 4)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = hidden(
        s, p, 4, boxl, mirror, 4)
    assert message == 'Hidden quad in box 5: R4C4 R4C6 R6C4 R6C6', 'Error in hidquad'
    s, err = conv(
        '030600078270080010500007004027591403090378120103264097300800749040750001700009052')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    wing = wingpos(boxl, mirror)
    s, p, message, found, err = xwing(s, p, 2, wing, 4)
    assert (
        message) == 'X-wing of 8 in C1, C8 and R4, R8 removes 8 from R8C7, R8C3', 'Error in xwing'
    s, err = conv(
        '589312746236740005714006023362987050847135269951264387478603500603001078105070630')
    p = possible(s)
    pair, paircomb, pairdict = pairs(s, p)
    s, p, message, found, err = xywing(s, p, b, pair, 4)
    assert (message[:21]) == 'XY-wing of R8C7 (4,9)', 'Error in xywing'
    s, err = conv(
        '240800039073900084800034257064208793907003805308009410732586941481390500600001308')
    p = possible(s)
    boxl = boxlist(s)
    s, p, logic, message, found, err = pointing(s, p, pb, 4)
    assert message == 'Pointing pair in box 2 removed 5 from R1C5 R2C5 ', 'Error in pointing'
    comb, mirror = combmir(p, boxl)
    wing = wingpos(boxl, mirror)
    s, p, message, found, err = xwing(s, p, 2, wing, 4)
    assert (
        message) == 'X-wing of 1 in C2, C4 and R3, R5 removes 1 from R5C5', 'Error in xwing'
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = xyzwing(s, p, b, boxl, comb, pb, 4)
    assert (
        message[:50]) == 'XYZ-wing of R5C4 (1, 4, 6) R5C5 (4, 6) R3C4 (1, 6)', 'Error in xyzwing'
    s, err = conv(
        '917854623040106007605027104074080016109760042060410970406200701701640230823571469')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    wing = wingpos(boxl, mirror)
    s, p, message, found, err = xwing(s, p, 3, wing, 4)
    assert (
        message) == 'Swordfish of 3 in R2, R6, R7 and C1, C5, C6 removes 3 from R4C1, R4C6, R5C6 (=5)'
    comb, mirror = combmir(p, boxl)
    # Jellyfish example from http://www.sudokuwiki.org/Jelly_Fish_Strategy
    s, err = conv(
        '001753800050000007700890100000601570625478931017905400000067004070000010006309700')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    wing = wingpos(boxl, mirror)
    s, p, message, found, err = xwing(s, p, 4, wing, 4)
    assert (
        message) == 'Jellyfish of 2 in R1, R4, R6, R9 and C1, C5, C8, C9 removes 2 from R2C1, R2C5, R2C8, R3C8, R3C9, R7C1, R7C8, R8C1, R8C5, R8C9'
    comb, mirror = combmir(p, boxl)
    s, err = conv(

        '037080405658194300402357860063528004504761203201943650829415736006039540345070000')
    p = possible(s)
    boxl = boxlist(s)
    s, p, logic, message, found, err = pointing(s, p, pb, 4)
    assert message == 'Pointing pair in box 2 removed 2 from R1C8 ', 'Error in pointing'
    s, p, logic, message, found, err = pointing(s, p, pb, 4)
    assert message == 'Pointing pair in box 7 removed 1 from R8C9 ', 'Error in pointing'
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = hidden(
        s, p, 2, boxl, mirror, 4)
    assert message == 'Hidden pair in column 9: R3C9 R9C9', 'Error in hidden'
    pair, paircomb, pairdict = pairs(s, p)
    assert pair[0] == [0, 1, 9], 'Error in pairs.'
    assert paircomb[0] == [0, 1], 'Error in pairs.'
    assert pairdict[19] == [0, 7, 19, 26, 33, 78, 80], 'Error in pairs.'
    s, p, message, found, err = remotepair(
        s, p, b, pair, pairdict, 4)
    assert (
        message[:32]) == 'Remote pairs of (1,9) are found.', 'Error in remotepair'
    s, err = conv(
        '300957800074368015050142000005271639163894050792536100000703590507689420009405006')
    p = possible(s)
    pair, paircomb, pairdict = pairs(s, p)
    s, p, message, chainlength, found, err = pairchain(
        s, p, b, pair, paircomb, 4)
    assert (
        message[:28]) == 'Chain of pairs. If R3C8 is 7', 'Error in pairchain'
    return
