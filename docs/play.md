---
layout: default
lang: English
ref: play
permalink: /play
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

## Creating an image file

You can now start solving this problem, but before doing it, you may want to see the image of the problem. At first, you should explicitly create an image file with `jpg` command to designate the directory of the data file. Default data directory is `~/kaidoku`. If you prefer other directory, input the directory when it is prompted.

```
kaidoku-{{ site.version }}> jpg
Data directory does not exist.
Input name of the data directory (default: ~/kaidoku):
See image by "html".
kaidoku-{{ site.version }}>
```

Now this image file is created as current.jpg in the data directory.

![]({{'/img/2-1.jpg' | relative_url}})

Now run `html` and a html file showing this image file is opened with your default web browser. The html file reloads the image file every 2 seconds (interval can be adjusted with a text box). From now on, as you proceed with this problem, the image file is updated and the html file reloads, so that it is easy to follow the change in the state of the board.

## Put a number

Now we are ready to play. Look at the above figure and think where to start.

Look at **row 2, column 9**. Here, it means that

- **Row 2** means a 2nd row from the top
- **Column 9** means a 9th column from the left

It can also be written as **R2C9**. Scan row 2. It has all the digits from 1 to 9 except 8 and 9. Therefore, R2C9 should have 8 or 9. In column 9, there is 8 on R8C9, and therefore R2C9 should not be 8. Therefore, R2C9 should be 9.

When you want to know which number is to be placed in a certain cell, you scan the same row, column, and box. From the digits 1 to 9, the number already filled in the same row, column, and box is removed from the candidate. If there is a unique candidate, that is the number to be filled in that cell. This logic is called **naked single**. By using the naked single logic, R2C9 is 9.

Now we place number 9 on R2C9. Please look at the instruction of **Type 3 digits (row, column, number) to put a number.** You specify row, column, and number to place in this order. In this case, row is 2, column is 9, number is 9, and therefore you type `299`.

    kaidoku-{{ site.version }}> 299

The ascii image of the board is shown and the image file shown in the html file updates automatically as follows.

![]({{'/img/2-1-1.jpg' | relative_url}})

## Keep on solving

Now row 2 has only one blank cell, and it is easy to see that R2C7 is 8. Column 9 has only one blank cell and R5C9 is 1. By the naked single logic, R8C1 is 6. After that, column 1 has only one blank cell and R5C1 is 4. Row 8 has only one blank cell and R8C3 is 9. Put these numbers as follows.

    kaidoku-{{ site.version }}> 278
    kaidoku-{{ site.version }}> 591
    kaidoku-{{ site.version }}> 816
    kaidoku-{{ site.version }}> 514
    kaidoku-{{ site.version }}> 839

![]({{'/img/2-1-6.jpg' | relative_url}})

## Notifying a mistake

When you put a number that is unable to be placed, the number is not placed. For example if you type `722` in this situation, warning message is shown as follows.

    kaidoku-{{ site.version }}> 722
    Both R7C2 and R7C9 have the same value of 2.

## Take back a move

You can always erase a number that was written at the last time. Just type `b`.

    kaidoku-{{ site.version }}> b
    Level 2 No. 1: move 5

Writing a number is regarded as a "move", and we call it "take back a move". You can take back as many moves as possible, until you reach the initial position.

## Quit and restart

You can always quit the game by `q`. The status is saved in configuration file, and when you run kaidoku next time, you can start from the position where you quitted last time. Just type `c` or `html` to show the position and continue.

## Finish a problem and go to the next problem

This problem can be solved with only the naked single logic. When you fill out all the blank cells, a massage appears that

    Now this problem is solved !

You can go to the next problem with `n`.

    kaidoku-{{ site.version }}> n
    Level 2 No. 2

- - -

- [Previous: How to install and get started](./install)
- [Document index](./#document)
- [Home Page](./)
