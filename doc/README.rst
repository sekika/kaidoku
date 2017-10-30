Kaidoku: Player, solver and creater of sudoku puzzles
=======================

Kaidoku can solve sudoku puzzles, play with the puzzles and create sudoku puzzles from command-line interface.

This is a program in development. Document is to be written in this page.

.. image:: image/3-1.jpg

Install
---------------

Python 3 is required. Install Python at https://www.python.org/ . After that, install kaidoku by running

.. code-block:: bash

 pip3 install kaidoku
 
You can check the `latest version <https://pypi.python.org/pypi/kaidoku>`_ by **pip3 search kaidoku** and update to the latest version by **pip3 install -U kaidoku**.

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

More logics to be implemented.

External great sudoku sites
-----------------

- https://www.websudoku.com/
- http://www.sudoku-solutions.com/
- http://www.sudokuwiki.org

Author
---------------

`Katsutoshi Seki <https://github.com/sekika>`_ wrote this software and published it with the `MIT license <../LICENSE.txt>`_. The email address of the author is available at `this paper <https://dx.doi.org/10.1016/j.geoderma.2015.02.013>`_. Questions and bug reports can be sent to the issue of the GitHub repository here.
