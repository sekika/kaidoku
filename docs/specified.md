---
layout: default
lang: English
ref: specified
permalink: /specified
---

# Analyze a specified sudoku problem

A special position can be checked with `check` command followed by a position. The position is expressed with writing numbers consecutively, with blank cell expressed by 0. For example, in this diagram, level 5 no. 1,

![]({{'/img/5-1.jpg' | relative_url}})

can be expressed with

    310002000000860200008003075007098350090000080053620400630200900009036000000100063

When you are solving the [online version of kaidoku](sudoku), you can obtain the position by typing `c`, which copies the current posiotion to a clipboard. Then this position can be checked with `check pos [verb]` where pos is the position, verb is the verbose level, which is 1 when 

- `check pos` shows if the position has a unique solution, multiple solutions or no solution.
- `check pos 2` shows a hint for basic logic.
- `check pos 3` shows hints for advanced logics to determine a cell.
- `check pos 4` shows a procedure to determine a cell.

    kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063
    
    This position has a unique solution.

    kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063 2
    
   Look at R4C4. What number is available?

`solve` command shows the procedure for solving the problem completely by

    solve pos [verb]
 
- `solve pos` shows only the difficulty level.
- `solve pos 2` shows part of advanced logics.
- `solve pos 3` shows all of advanced logics.
- `solve pos 4` shows all the logics and complete procedure of solving.
- `solve pos 5` shows whole procedure with ascii image of the board.

# Alternate way to express a position

- Numbers can be separated with commas `,`. In this case, 9 numbers should be between the commas.
- 0 can be replaced with other ascii characters such as -.

Therefore following command is also available.

    kaidoku-{{ site.version }}> check 31---2---,---86-2--,--8--3-75,--7-9835-,-9-----8-,-5362-4--,63-2--9--,--9-36---,---1---63

When you are typing a position from a printed material, this is useful because the input error is shown as to which row is invalid.

- - -

- [Previous: Analysis of a whole problem](analysis)
- [Document index](./#document)
- [Home Page](./)
