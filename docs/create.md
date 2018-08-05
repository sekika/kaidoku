---
layout: default
lang: English
ref: create
permalink: /create
---

# Create new sudoku problems

## Create new problems and append to the problem book

As explained in [selection of level and problem](./level), kaidoku is shipped with certain numbers of problems classified with difficulty level, and `book` command shows the numbers of problems in each level like this.

```
kaidoku-{{ site.version }}> book
Level 1 trivial   :   3000 (12.00 %)
Level 2 very easy :   3000 (12.00 %)
Level 3 easy      :   3000 (12.00 %)
Level 4 normal    :   3000 (12.00 %)
Level 5 hard      :   3000 (12.00 %)
Level 6 very hard :   3000 (12.00 %)
Level 7 evil      :   3000 (12.00 %)
Level 8 extreme   :   3000 (12.00 %)
Level 9 ultimate  :   1000 ( 4.00 %)
Total numbers     :  25000
```

The problem book is stored in a single file. You can create new problems with `create` command.

```
kaidoku-{{ site.version }}> create
Creating 10 new problems.
..........
Finished. 10 problems created in 15.8 seconds (mean: 1.581 sec).
Level 1 trivial   :   3003 (12.01 %)
Level 2 very easy :   3002 (12.00 %)
:
Total numbers     :  25010
```

Now the problems are added to the system default file. When the system default file is not writable, it is copied to data directory, such as

```
Unable to write a file: /usr/local/lib/python3.7/dist-packages/kaidoku/data/sudoku.txt
Copying the system default file to /home/seki/kaidoku/sudoku.txt
```

Now new problems were appended to the problem book. The appended problems are brand-new puzzles that are not found anywhere else.

By default, 10 puzzles are made. If you want to make more, just type the numbers of problems to create after create command, such as

```
kaidoku-{{ site.version }}> create 100
Creating 100 new problems.
.......... 10 problems created in 14.4 seconds (mean: 1.444 sec).
.......... 20 problems created in 28.4 seconds (mean: 1.422 sec).
.......... 30 problems created in 46.1 seconds (mean: 1.536 sec).
.......... 40 problems created in 62.0 seconds (mean: 1.551 sec).
.......... 50 problems created in 75.7 seconds (mean: 1.514 sec).
.......... 60 problems created in 91.2 seconds (mean: 1.520 sec).
.......... 70 problems created in 105.6 seconds (mean: 1.509 sec).
.......... 80 problems created in 123.6 seconds (mean: 1.545 sec).
.......... 90 problems created in 142.1 seconds (mean: 1.579 sec).
..........
Finished. 100 problems created in 164.6 seconds (mean: 1.646 sec).
```

Please note that the the difficulty level created is determined by certain probability distribution. Roughly speaking, 95% of the problems are up to level 4. Level 9 is quite rare, and you may have to create tens of thousands of puzzles to get 1 puzzle of level 9.

If you want to get only hard problems, getting so many easy problems with create command is just a waste of disk space, and therefore you can just set the minimum level of difficulty of the puzzle to create. For example, if you set minimum level = 4, problems with levels 1,2 and 3 are just discarded. It is in the configuration of "create: minlevel". Type `config` and you will be prompted to `Entry to edit:`, and then type `create`. Then again you will be prompted to `Entry to edit in create:`, and this time type `minlevel`. Then you will be prompted as `minlevel = `, and type the minimum level setting. After that, you will be prompted again as `Entry to edit:`, and just type return. For example, if you want to set the minimum level to be 4, it is like this.

```
kaidoku-{{ site.version }}> config
:
Entry to edit: create
Editing the config entry of create
symmetry = y
minlevel = 1
mincell = 17
Entry to edit in create: minlevel
minlevel = 4
:
Entry to edit: 
```

## Managing the location of the problem book

The location of the file of the problem book is shown by `config` command. It shows the parameter `file`with other parameters, such as

```
file = /usr/local/lib/python3.7/site-packages/kaidoku/data/sudoku.txt
```

Then it askes if it changes the parameter by

```
Entry to edit: 
```

If you do not want to change the file location, you can just press return. All the problems are stored in this single file, and you may want to change the location of the file. For example, if you want to change the location of the file to `~/kaidoku/sudoku.txt`, type `file` when prompted to `Entry to edit:`, and then type `~/kaidoku/sudoku.txt` when prompted to `file = `, like this.

```
kaidoku-{{ site.version }}> config
:
file = /usr/local/lib/python3.7/site-packages/kaidoku/data/sudoku.txt
:
Entry to edit: file
file = ~/kaidoku/sudoku.txt
```

Then it shows the configuration list again and the prompted as `Entry to edit:` again. You just type return.

Now you changed the location of the problem book to `~/kaidoku/sudoku.txt`, but there is no such file yet. If you want to use the default book, just copy the file from the installed sudoku file, or download it from [here](https://github.com/sekika/kaidoku/blob/master/kaidoku/data/sudoku.txt). If you just start from empty book, you have to make a file anyway; otherwise the file location is changed to system default when kaidoku is invoked. Therefore make a empty file by touch command from terminal, like this.

```
touch ~/kaidoku/sudoku.txt
```

Now you can create new problems to the new file location with `create` command.

- - -

- [Previous: Bookmark management](bookmark)
- [Document index](./#document)
- [Home Page](./)
