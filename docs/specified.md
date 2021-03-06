---
layout: default
lang: English
ref: specified
permalink: /specified
---

# Analyze a specified sudoku problem

A special position can be checked with `check` command followed by a position. The position is expressed with writing numbers consecutively, with blank cell expressed by 0. For example, this position

![]({{'/img/5-1.jpg' | relative_url}})

can be expressed with

    310002000000860200008003075007098350090000080053620400630200900009036000000100063

When you are solving the [online version of kaidoku](sudoku), you can obtain the position by typing `c`, which copies the current position to the clipboard. Then the position can be checked with `check pos [verb]` where pos is the position, verb is the verbose level, which is 1 when ommitted.

- `check pos` shows if the position has a unique solution.
- `check pos 2` shows a hint for [basic logics](basichint) (naked single and hidden single).
- `check pos 3` shows hints for [advanced logics](logic) to determine a certain cell.
- `check pos 4` shows a procedure to determine a certain cell.

```
kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063

This position has a unique solution.

kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063 2

Look at R4C4. What number is available?
```

`solve` command shows the procedure for solving the problem completely by

    solve pos [verb]
 
- `solve pos` shows only the difficulty level.
- `solve pos 2` shows hints for trial and search.
- `solve pos 3` shows hints of advanced logics and result of trial and search.
- `solve pos 4` shows complete procedure of solving.
- `solve pos 5` shows whole procedure with ascii image of the board.

# Alternative way to express a position

- Numbers can be separated with commas `,`. In this case, 9 numbers should be between the commas.
- 0 can be replaced with other ascii characters such as -.

Therefore following command is also available.

    kaidoku-{{ site.version }}> solve 31---2---,---86-2--,--8--3-75,--7-9835-,-9-----8-,-5362-4--,63-2--9--,--9-36---,---1---63

When you are typing a position from a printed material, this is useful because the input error is shown as to which row is invalid. For example, if you enter

    kaidoku-{{ site.version }}> solve 31---2---,---86-2--,--8--3-75,--7-9835-,-9----8-,-5362-4--,63-2--9--,--9-36---,---1---63

you get the message

    Error in input: -9----8-

and you can just check this row and find that there is only 8 cells in this row. If you enter

    kaidoku-{{ site.version }}> solve 31---2---,---86-2--,--8--3-75,--7-9835-,-8-----8-,-5362-4--,63-2--9--,--9-36---,---1---63

you get a diagram and the message

    Both R5C2 and R5C8 have the same value of 8.

# Validity check

Sudoku is valid only when the solution is unique. If there are multiple solutions, kaidoku shows that it is invalid. For example, if you enter

    kaidoku-{{ site.version }}> solve -4-3---9-,---------,-----4236,7924--3--,----8----,--1--3627,1385-----,--------4,-7---9-6-

you get a message

    Invalid sudoku with multiple solutions.

If you just want to know if the problem is valid, you can use `check` command and enter

    kaidoku-{{ site.version }}> check -4-3---9-,---------,-----4236,7924--3--,----8----,--1--3627,1385-----,--------4,-7---9-6-

If you want to show the multiple solutions, use `solve pos 5`. For example,

    kaidoku-{{ site.version }}> solve -4-3---9-,---------,-----4236,7924--3--,----8----,--1--3627,1385-----,--------4,-7---9-6- 5

It will show 2 possible solutions and common number in the 2 solutions at the end. Note that kaidoku stops looking for solutions after it finds 2 solutions. Therefore there can be more than 2 solutions. If there is no solution, for example,

    kaidoku-{{ site.version }}> solve -4-3---9-,---------,-----4236,7924--3--,4---8----,--1--3627,1385-----,--------4,-7---9-6-

then it will finally show that

    Invalid sudoku with no solution.

If you want to know why there is no solution, use `solve pos 5`.

# Example

Let us analyze this [hardest sudoku](http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html). It takes several seconds to solve, depending on the power of your PC.

    kaidoku-{{ site.version }}> solve 8--------,--36-----,-7--9-2--,-5---7---,----457--,---1---3-,--1----68,--85---1-,-9----4-- 2
    
    Search with depth 3 from R8C7.
    Search with depth 3 from R7C7.
    Search with depth 2 from R7C5.
    Search with depth 3 from R8C9.
    Search with depth 3 from R9C4.
    Search with depth 1 from R6C7.
    Search with depth 2 from R1C7.
    Valid sudoku with unique solution of level 9 (ultimate).
    
It shows how extensive the search is. You can show the complete process by

    kaidoku-{{ site.version }}> solve 8--------,--36-----,-7--9-2--,-5---7---,----457--,---1---3-,--1----68,--85---1-,-9----4-- 5

Here is the [result](https://github.com/sekika/kaidoku/blob/master/docs/solution-Inkala-2012.txt).

- - -

- [Previous: Analysis of a whole problem](analysis)
- [Next: Bookmark management](bookmark)
- [Document index](./#document)
- [Home Page](./)
