---
layout: default
---

# How to play with a sudoku puzzle

## Showing a problem

We assume that [you installed kaidoku and got into kaidoku prompt](install). Just type `c` and a problem is shown.

```
kaidoku-{{ site.version }}> c
Level 2 No. 1
  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|9    |8 5  |2 1 4|
2|5 4 2|1 6 3|  7  |
3|8    |    2|    3|
 +-----+-----+-----+
4|3   1|    4|    7|
5|  7  |3   6|  2  |
6|2    |9    |4   5|
 +-----+-----+-----+
7|1    |6    |    2|
8|  2  |7 1 5|3 4 8|
9|7 3 8|  4 9|    6|
 +-----+-----+-----+

Type 3 digits (row, column, number) to put a number. i for hint.

kaidoku-{{ site.version }}>
```

Kaidoku is shipped with sudoku problems of different levels of difficulty. At the first time you run kaidoku, level 2 is selected. Therefore, "Level 2 No. 1" is shown.

You can now start solving this problem, but before doing it, you may want to see the image of the problem. At first, you should explicitly create an image file with `jpg` command to designate the directory of the data file. Default data directory is `~/kaidoku`. If you prefer other directory, input the directory when it is prompted.

```
kaidoku-{{ site.version }}> jpg
Data directory does not exist.
Input name of the data directory (default: ~/kaidoku):
See image by "html".
kaidoku-{{ site.version }}>
```

[Home Page](./)
