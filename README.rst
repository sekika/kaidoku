Kaidoku: Player, solver and creater of sudoku puzzles
=======================

Kaidoku can solve sudoku puzzles, play with the puzzles and create sudoku puzzles from command-line interface. Kaidoku is a

- player of sudoku. You can play original sudoku puzzles in various level of difficulty with command line interface. You can get hints when you want.
- solver of sudoku. It can solve sudoku puzzles. It evaluates if a given puzzle is valid sudoku with unique solution, or invalid sudoku with no solution or multiple solutions. It can show the procedure of solving a sudoku puzzle with various logics. Based on the logics required to solve a sudoku puzzle, it identifies the difficulty of the sudoku puzzles for humans to solve.
- creater of sudoku. It can create new sudoku puzzles. The puzzles shipped with this program was created by the program itself.

This is a program in development. Document is not written yet. Design of the program can change drastically.

Install
---------------

Python 3 is required. Install Python at https://www.python.org/ . After that, install kaidoku by running

.. code-block:: bash

 pip3 install kaidoku

How to use
-----------------

By invoking kaidoku, you get into kaidoku command prompt. You can get help of the command by typing 'h'.

Logics
-----------------
- Naked single
- Hidden single
- Pointing pair
- Pointing triple
- Naked pair
- Naked triple
- Hidden pair
- Hidden triple
- X-wing
- XY-wing (Y-Wing)
- Chain of pairs
- Trial and search

Logics to be hopefully implemented
-----------------

- XYZ-wing
- Remote pairs
- Naked quad
- Hidden quad
- Swordfish
- Bowman's Bingo

To do, or not to do?
-----------------

- Implement additional logics
- Export bookmark
- Challenge mode (restrict command, no check, no hint, measure time and mistakes, keep record)
- Draw diagram with PyX - http://pyx.sourceforge.net/
- Write document

External great sudoku sites
-----------------

- https://www.websudoku.com/
- http://www.sudoku-solutions.com/
- http://www.sudokuwiki.org
