# -*- coding: utf-8 -*-
"""Help messages."""


def welcommessage(version):
    """Return welcome message."""
    message = 'Kaidoku - player, solver and creater of sudoku puzzles.\n' + \
        '          https://sekika.github.io/kaidoku/\n' + \
        'Type h for help, c for showing a problem, q for quit.'
    return message


def helpmessage():
    """Return help message."""
    message = '246 : In the cell of row 2 column 4, put number 6\n'
    message += 'b   : take Back one move\n'
    message += 'c   : show Current position\n'
    message += 'i   : show hInt for current position\n'
    message += 'q   : Quit kaidoku\n\n'
    message += '[Select problem]\n'
    message += 'j num  : Jump to problem num\n'
    message += 'n      : Next problem\n'
    message += 'p      : Previous problem\n'
    message += 'l level: change Level\n'
    message += 'book   : show index of the book\n\n'
    message += '[Help]\n'
    message += 'h  : show this Help\n'
    message += 'ha : show Help for Advanced commands'
    return message


def advancedhelp():
    """Return help message for advanced commands."""
    message = 'a [verb]        : Analyze the current problem\n'
    message += 'ac [verb]       : Analyze from the Current position\n'
    message += 'all [verb]      : analyze all the problems in the current level\n'
    message += 'append pos      : append a position to book\n'
    message += 'ba [label]      : add current position to bookmark\n'
    message += 'bl              : list bookmark\n'
    message += 'bp pos          : add a specified position bookmark\n'
    message += 'br label        : read bookmark\n'
    message += 'config          : show configuration\n'
    message += 'create [numbers]: create new problems and append to book\n'
    message += 'giveup [sec]    : reanalyze giveup positions\n'
    message += 'html            : see image in web browzer as html\n'
    message += 'jpg             : draw jpeg image\n'
    message += 'jm              : draw jpeg image with mark\n'
    message += 'import          : import file2\n'
    message += 'initial         : go back to initial position\n'
    message += 'maxtime [sec]   : set maximum time for analyzing a position (todo)\n'
    message += 'reanalyze       : reanalyze whole book\n'
    message += 'solve pos [verb]: solve a specified position\n'
    message += 'sp              : Solve Partially with naked or hidden single\n'
    message += 'u               : show URL of the current position'
    return message
