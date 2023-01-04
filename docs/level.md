---
layout: default
lang: English
ref: level
permalink: /level
---

# Select a problem of a specified difficulty level

## Determination of level

Kaidoku classifies sudoku problems with 9 difficulty levels.

|Level 1| trivial |
|Level 2| very easy |
|Level 3| easy |
|Level 4| normal |
|Level 5| hard |
|Level 6| very hard |
|Level 7| evil |
|Level 8| extreme |
|Level 9| ultimate |

The levels are determined by the numbers of initial blank cells, the difficulty of the logics, and the complexity of seach. Up to level 3 the numbers of blank cells are the dominant factor, up to level 6 the difficulty of the logics is the dominant factor, and from level 7 complexity of the search is the dominant factor.

10 random problems of "evel" level in [web sudoku](https://www.websudoku.com/) were checked and all of them were classified as level 5 (hard) in Kaidoku.

## Selection of level and problem

In the [online version](sudoku), you can select the level from the pulldown menu and number from the textbox.

In the commandline version of kaidoku, you can select the level with `l level`. For example, to select level 5,

    kaidoku-{{ site.version }}> l 5
    Level 5 No. 1

You can start from whichever level you want. When you feel that the problem is too hard, go to lower level. When you feel that the problem is too easy, go to higher level. In this way, you can always solve the problems that are most comfortable for you.

At each level, you can select the problems by the following commands.

|n |Go to next problem |
|p |Go to previous problem |
|j num |Jump to problem no. num |

Current problem is stored in each level. For example,

- You solved 23 problems in level 3 and you are at level 3, no. 24.
- You go to level 4 and solve 5 problems. Now you are at level 4, no. 6.
- After that, you go back to level 3. In this case, you are at level 3, no. 24.

Note that only the information of the number of problem is stored in each level. Move is stored only for the current problem.

Therefore, recommended way is to start from no. 1 in each level, and after solving a problem you go to the next problem with `n` command.

You can show the index of the problem book by `book` command, which shows the numbers of problems in each level. Kaidoku is shipped with certain numbers of problems in each level. It can increase the numbers of problems by creating new problems. The rate of creating a new problem is faster than a human to solve the problem. Therefore, you can inifinitely enjoy new problems.

The problems shipped with the latest kaidoku can also be played with the [online version](sudoku) of kaidoku.

- - -

- [Next: Logics for solving sudoku puzzles used in this program](./logic)
- [Previous: Getting a hint on basic logics](basichint)
- [Document index](./#document)
- [Home Page](./)
