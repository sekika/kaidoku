---
layout: default
lang: English
ref: basichint
permalink: /basichint
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



- - -

- [Previous: Logics for solving sudoku puzzles used in this program](logic)
- [Document index](./#document)
- [Home Page](./)
