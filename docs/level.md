---
layout: default
lang: English
ref: level
permalink: /level
---

# Select a problem of a specified difficulty level

## Selection of level and problem

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

You can select the level with `l level`. For example, to select level 5,

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

Therefore, recommended way is to start from no. 1 in each level, and after solving a problem you go to the next problem with `n` command.

You can show the index of the problem book by `book` command, which shows the numbers of problems in each level. Kaidoku is shipped with certain numbers of problems in each level. It can increase the numbers of problems by creating new problems. The rate of creating a new problem is faster than a human to solve the problem. Therefore, you can inifinitely enjoy new problems.

## Determination of level

The levels are determined by the numbers of initial blank cells, the difficulty of the logics that is used, and the complexity of seach. Up to level 3 the number of blank cells is the dominant factor, up to level 6 the difficulty of the logics is the dominant factor, and from level 7 complexity of the search is the dominant factor.

Current status of kaidoku is in development, and algorithm to determine the level is not fixed yet. As more logics will be implemented, the level of a certain problem will change. Therefore, the problem book shipped now is a tentative one.

- - -

- [Next: Logics for solving sudoku puzzles used in this program](./logic)
- [Previous: Getting a hint on basic logics](basichint)
- [Document index](./#document)
- [Home Page](./)
