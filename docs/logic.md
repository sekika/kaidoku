---
layout: default
lang: English
ref: logic
permalink: /logic
---

# Logics for solving sudoku puzzles used in this program

## Basic logics

Easy sudoku puzzles can be solved with basic logics of

- Naked single
- Hidden single

which were explained at previous pages.

## Intermediate and advanced logics

For solving harder puzzles, some advanced logics need to be used, such as

- Pointing pair, triple (also called: Locked candidates, Localization)
- Naked pair, triple, quad
- Hidden pair, triple, quad
- Unique rectangle
- X-wing, XY-wing, XYZ-wing
- Analysis of chain of pairs

To solve such difficult problems, usually people write candidates of the numbers in the cells to think which logic can be applied. Detail of each logic is not discussed in this page. Please refer to these sites.

- [SudokuWiki.org](http://www.sudokuwiki.org/Strategy_Families)
- [sudoku-solutions.com - Background](http://www.sudoku-solutions.com/index.php?page=background)

## Trial and search

For more difficult problems, the above logics do not directly lead to solution, and 'trial and error' approach is required. Suppose that R2C3 has 3 candidate numbers, 2, 4, 6. For each number, we assume that R2C3 is that number. First we assume that R2C3 is 2 and keep solving. If we meet a contradiction, we can eliminate 2 from the candidates. If 4 is also eliminated, R2C3 should be 6. Many advanced logics explained in  [SudokuWiki.org](http://www.sudokuwiki.org/) are trying to find a certain (assumption - contradiction) combination strategically. Trial approach is especially useful for chain of pairs, because one assumption successively determines many cells. Therefore in kaidoku trial and error approach is performed for pairs, and it is regarded as the analysis of chain of pairs.

Trials and errors can be recursively employed with search algorithm. In the above example, while examining R2C3 = 2, we will make another assumption in another cell. If that is not enough, make another assumptions. As we have only finite numbers of blank cells, this is not infinite steps. Therefore we can always get to the final conclusion. If we have 3 candidates in a certain cell and for each candidates we make 5 trials, we make 15 trials in total. The numbers of trials are multiplied in this way. Computers can easily perform such large numbers of trials and errors with search algorithm. Such puzzles requiring extensive search are too hard for normal human beings, but a small number of trials and errors are actually available. It can also be solved with luck. In any case, problems requiring the trial and error approach is too hard for avaraged sudoku players. Some people enjoy such difficult problems, and kaidoku offers such problems in beyond level 7 to meet the need for strongest sudoku players.

## Logics implemented in Kaidoku

Actually the easiest way for the computers to solve sudoku is to use only the naked single logic and search algorithm, because the computers can make so many times of trials and errors quite easily. However, kaidoku uses many logics to find the best way for humans to solve a sudoku puzzle, and use the search algorithm as a last resort.

Following logics are currently implemented in Kaidoku. These logics are applied in this order.

- Naked single
- Hidden single
- Pointing pair
- Pointing triple
- Naked pair
- Naked triple
- Hidden pair
- Hidden triple
- X-wing
- XY-wing (Y-Wing)
- Chain of pairs
- Trial
- Search

Unique rectangle is not implmented. It is valid when we know that the sudoku has unique solution. If it is implemented, kaidoku may not correctly identify a sudoku if it has multiple solutions.

Trial and search is basically doing the same thing, but it is distinguished in kaidoku. Search performs a complete search in many depths. Here depth means the numbers of successive assumptions. We make first assumption in a certain cell, keep on solving with logics, and make another assumption. This is depth 2. Trial is the search within depth 1, starting from a pair candidate cell, within a certain steps. Here step means the numbers of cells eliminated with naked single or hidden single logic. In short, trial is the search algorithm restricted to human ability. Trial may not get to final conclusion, but search always reaches the final conclusion.

More logics will be hopefully implemented. Especially the following.

- XYZ-wing
- Remote pairs
- Naked quad
- Hidden quad

- - -

- [Previous: Select a problem of a specified difficulty level](./level)
- [Document index](./#document)
- [Home Page](./)
