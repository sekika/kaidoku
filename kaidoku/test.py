# -*- coding: utf-8 -*-
"""modules for tests."""

def test_all():
    """do all the tests in this module"""
    test_calc()
    return

def test_calc():
    """test modules in calc.py, wing.py, and chain.py."""
    import copy
    import datetime
    from kaidoku.calc import solve
    from kaidoku.calc import solveone
    from kaidoku.calc import naksing
    from kaidoku.calc import pointing
    from kaidoku.calc import nakhid
    from kaidoku.chain import pairchain
    from kaidoku.misc import box
    from kaidoku.misc import boxlist
    from kaidoku.misc import combmir
    from kaidoku.misc import conv
    from kaidoku.misc import pairs
    from kaidoku.misc import pbox
    from kaidoku.calc import possible
    from kaidoku.output import output
    from kaidoku.wing import xwing
    from kaidoku.wing import xywing
    problem = '010003000002040800098000000850007930000504000023900056000000360005090400000600010'
    s, err = conv(problem)
    s2 = copy.copy(s)
    s2, message, level, solved, err = solve(s2, 1, 10, 5)
    assert message =='Solved', 'Error in solve'
    p = possible(s)
    b = box()
    pb = pbox()
    start = datetime.datetime.now()
    endtime = start + datetime.timedelta(seconds=3)
    s, p, message, logic, depth, found, err = solveone(s, p, 4, 0, 3, endtime, b, pb)
    assert message == 'Hidden single in box 2 : R2C6 = 9', 'Error in solveone'
    s, p, message, found, err = naksing(s, p, b, 4)
    assert message == 'Naked single: R2C8 = 7', 'Error in naksing'
    s, err = conv('178500390396000205452093810621384759587169432934275168263450980805900603709030520')
    p = possible(s)
    s, p, logic, message, found, err = pointing(s, p, pb, 4)
    assert message == 'Pointing pair in box 2 removed 7 from R2C6 ', 'Error in pointing'
    s, err = conv('700060050501080000060002008040000007600803905900000020100700090000010206030090001')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, logic, message, found, err = nakhid(s, p, boxl, comb, mirror, 4, False)
    assert message == 'Naked pair in column 9 made removal from R1C9', 'Error in nakhid'
    s, err = conv('250400068960020000041600200586142379192367080734985612000006800000090056670004023')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, logic, message, found, err = nakhid(s, p, boxl, comb, mirror, 4, False)
    assert message == 'Naked triple in box 7 made removal from R7C3 R9C3', 'Error in nakhid'
    s, err = conv('528641739614937258793500641902000017487195326100000980870403192301209000209010003')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, logic, message, found, err = nakhid(s, p, boxl, comb, mirror, 4, False)
    assert message == 'Hidden pair in row 9', 'Error in nakhid'
    s, err = conv('030600078270080010500007004027591403090378120103264097300800749040750001700009052')
    p = possible(s)
    boxl = boxlist(s)
    comb, mirror = combmir(p, boxl)
    s, p, message, found, err = xwing(s, p, b, boxl, mirror, 4)
    assert (message[:42]) == 'X-wing is found. R4C1, R8C1, R4C8 and R8C8', 'Error in xwing'
    s, err = conv('589312746236740005714006023362987050847135269951264387478603500603001078105070630')
    p = possible(s)
    pair, paircomb = pairs(s, p)
    s, p, message, found, err = xywing(s, p, b, pair, 4)
    assert (message[:21]) == 'XY-wing of R8C7 (4,9)', 'Error in xywing'
    s, err = conv('300957800074368015050142000005271639163894050792536100000703590507689420009405006')
    p = possible(s)
    pair, paircomb = pairs(s, p)
    s, p, message, chainlength, found, err = pairchain(s, p, b, pair, paircomb, 4)
    assert (message[:37]) == 'Chain of pairs. Assume that R3C8 is 7', 'Error in pairchain'
    
    return
    