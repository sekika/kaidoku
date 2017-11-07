---
layout: default
lang: English
ref: logic
permalink: /logic
---

# Logics for solving sudoku puzzle

## Basic logics

Easy sudoku puzzles can be solved with basic strategies of

- Naked single
- Hidden single

## Advanced logics

For solving harder puzzles, some advanced logics need to be used, such as

- Pointing pair, triple (also called: Locked candidates, Localization)
- Naked pair, triple, quad
- Hidden pair, triple, quad
- Unique rectangle
- X-wing, XY-wing, XYZ-wing
- Analysis of chain of pairs

To solve such difficult problems, usually people write candidates of the numbers in the cells to think which logic can be applied.

## Trial and search

For more difficult problems, these logics do not directly lead to solution, and 'trial and error' approach is required. Computers can easily perform such trial and error with search algorithm. Such puzzles are too hard for normal human beings, but some people enjoy solving such touch puzzles.

## Logics implemented in Kaidoku

Actually the easiest way for the computers to solve sudoku is to use only the naked single logic and search algorithm, because the computers can make so many times of trial and errors quite easily. However, kaidoku uses many logics to find the best way for humans to solve a sudoku puzzle, and use the search algorithm as a last resort.

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
- Trial and search

Unique rectangle is not implmented. It is valid when we know that the sudoku has unique solution. If it is implemented, kaidoku may not correctly identify a sudoku if it has multiple solutions.

More logics will be hopefully implemented. Especially the following.

- XYZ-wing
- Remote pairs
- Naked quad
- Hidden quad

- - -

- [Document index](./#document)
- [Home Page](./)
