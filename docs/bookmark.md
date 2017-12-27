---
layout: default
lang: English
ref: bookmark
permalink: /bookmark
---

# Bookmark management

Here is a list of bookmark commands.

|ba [label] | add current position to bookmark |
|bp pos| add a specified position bookmark |
|bl | list bookmark |
|br label | read bookmark |

When you are solving a problem and encounter a position that you want to bookmark, run `ba`, and input a comment of the position when prompted. Note that move is not saved and the current position is saved as a new puzzle. A label is automatically attached to the bookmark, such as b1, b2, b3,... A label is unique and can identify a bookmark, while a comment is not for identification.

When you want to add a specified position to the bookmark, use `bp` command followed by position with a format explained in the [previous section](specified) such as

    kaidoku-{{ site.version }}> bp 8--------,--36-----,-7--9-2--,-5---7---,----457--,---1---3-,--1----68,--85---1-,-9----4--

`bl` command lists the date added, label, and comment of the bookmarks.
 
By `br` command, followed by a label, the bookmark is read.

- - -

- [Previous: Analyze a specified sudoku problem](specified)
- [Document index](./#document)
- [Home Page](./)
