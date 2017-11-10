---
layout: default
lang: English
ref: advancedhint
permalink: /advancedhint
---

# Getting a hint on advanced logics

## Hint on advanced logic

Let us take a problem in level 5 for example. By typing `l 5`, Level 5 no. 1 is selected.

    kaidoku-{{ site.version }}> l 5
    Level 5 No. 1

![]({{'/img/5-1.jpg' | relative_url}})

We can solve this problem with basic logics to some extent, but we get stuck in this position.

![]({{'/img/5-1-9.jpg' | relative_url}})

Now let us get a hint with `i` command and we get this message.

    kaidoku-{{ site.version }}> i
    Think candidates of the cells.
    See image by "html".
    For more hints, type ii.

This is the message that was briefly described [previously](basichint.md). It means that there is nothing we can do with basic logics. Now the image file is updated like this.

![]({{'/img/5-1-9p.jpg' | relative_url}})

Candidates of each cell is written automatically in this image, and you can think which logic can be applied to solve this problem. If you need further hints, type `ii` and 

    kaidoku-{{ site.version }}> ii
    Following logics are successively used.
    Pointing pair
    Pointing pair
    See full explanation by typing iii.

Now the logic which can be applied is shown. This hint means that after using pointing pair logic two times, we can determine a number of a certain cell.

If you want to know how the logics are applied, type `iii` and you will get the full explanation like this.

    kaidoku-{{ site.version }}> iii
    Pointing pair in box 1 removed 5 from R9C3 R7C3 
    Pointing pair in box 8 removed 5 from R8C4 (=7) R9C5 

There is a pointing pair of 5 in box 1 (R1C3 and R2C3), which removes 5 from R9C3 R7C3. After that, there is a pointing pair of 5 in box 8 (R7C5 and R7C6) in box 8, which removes 5 from R8C4 R9C5. After removing 5 from R8C4, R8C4 is 7.

After R8C4 as 7, this problem can be solved with only naked single and hidden single logics.

## Solve partially

Sometimes you may just want to concentrate on analyzing the advanced logics, rather than solving the whole problem. In such situation, you want to directly go to the position where advanced logic is applied. Go back to the initial position of the above problem by `initial` and use "solve partially" command, `sp`.

    kaidoku-{{ site.version }}> iii
    Naked single: R4C4 = 4
    Naked single: R3C4 = 9
    Hidden single in box 1 : R2C1 = 9
    Hidden single in box 1 : R2C2 = 7
    Hidden single in box 3 : R2C8 = 3
    Hidden single in box 4 : R6C1 = 8
    Hidden single in box 5 : R5C4 = 3
    Hidden single in box 8 : R9C6 = 9
    Hidden single in column 8 : R8C8 = 2

![]({{'/img/5-1-9p.jpg' | relative_url}})

Now naked single and hidden single are applied repeatedly until the basic logic is not available. `sp` command directly leads us to the position where advanced logic has to be used. You can use `i` command or `jm` command to show the image with candidates.

- - -

- [Previous: Logics for solving sudoku puzzles used in this program](logic)
- [Document index](./#document)
- [Home Page](./)
