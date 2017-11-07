---
layout: default
lang: English
ref: install
permalink: /install
---

# How to install and get started

## Install Python 3

Python 3 should be installed before installing kaidoku. Install Python 3 by

- Download and install from [Python official page](https://www.python.org/).
- If you are using [Homebrew](https://brew.sh/) on macOS, just run `brew install python3`

You can check your installed version of Python 3 by

    python3 -V

## Install Kaidoku

After installing Python 3, install kaidoku by running

    pip3 install kaidoku

from terminal emulator.

## Update Kaidoku

[Latest version](https://pypi.python.org/pypi/kaidoku): **{{ site.version }}**

You can check the latest version of kaidoku by

    pip3 search kaidoku

and update to the latest version by

    pip3 install -U kaidoku
 
## Getting started

Just run

    kaidoku

from the terminal emulator. You get into kaidoku command prompt.

    $ kaidoku
    Kaidoku - player, solver and creater of sudoku puzzles.
              https://sekika.github.io/kaidoku/
    Type h for help, c for showing a problem, q for quit.
    kaidoku-{{ site.version }}>

You can get help of the command by typing `h` (and Enter key), like this

```
kaidoku-{{ site.version }}> h
246 : In the cell of row 2 column 4, put number 6
b   : take Back one move
c   : show Current position
i   : show hInt for current position
q   : Quit kaidoku

(continues)

kaidoku-{{ site.version }}> 
```

You can quit from the kaidoku prompt by typing `q`.

- - -

- [Next: How to play with a sudoku puzzle](./play)
- [Previous: Rule of sudoku](./rule)
- [Document index](./#document)
- [Home Page](./)
