---
layout: default
---

# How to install and get started

## Install Python 3

Python 3 should be installed before installing kaidoku. Install Python 3 by

- Download and install from [Python official page](https://www.python.org/).
- If you are using [Homebrew](https://brew.sh/) on macOS, just run `brew install python3`

You can check your installed version of python 3 by

    python3 -V

## Install Kaidoku

[Latest version](https://pypi.python.org/pypi/kaidoku): **{{ site.version }}**

After installing python 3, install kaidoku by running

    pip3 install kaidoku

from terminal emulator. You can check the latest version by

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

You can get help of the command by typing 'h'.

[Home Page](./)
