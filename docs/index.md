---
layout: default
---

Kaidoku can solve sudoku puzzles, play with the puzzles and create sudoku puzzles from command-line interface.

![](img/3-1.jpg)

Kaidoku is a

* **player** of sudoku. You can play original sudoku puzzles in various level of difficulty with command line interface. You can get hints when you want.
* **solver** of sudoku. It can solve sudoku puzzles. It evaluates if a given puzzle is valid sudoku with unique solution, or invalid sudoku with no solution or multiple solutions. It can show the procedure of solving a sudoku puzzle with various logics. Based on the logics required to solve a sudoku puzzle, it identifies the difficulty of the sudoku puzzles for humans to solve.
* **creater** of sudoku. It can create new sudoku puzzles. The puzzles shipped with this program was created by the program itself.

# [](#header-1)Install

Python 3 is required. Install Python at https://www.python.org/ . After that, install kaidoku by running

```
pip3 install kaidoku
```

You can check the [latest version](https://pypi.python.org/pypi/kaidoku) by **pip3 search kaidoku** and update to the latest version by **pip3 install -U kaidoku**.
 

## [](#header-2)How to use

By invoking kaidoku, you get into kaidoku command prompt. You can get help of the command by typing 'h'.

This is a program in development. Document is to be written in this page.

### Contents

- [Logics](logic).

### External great sudoku sites

- [Web sudoku](https://www.websudoku.com/)
- [sudoku-solutions.com](http://www.sudoku-solutions.com/)
- [SudokuWiki.org](http://www.sudokuwiki.org)