---
layout: default
---

# Logics

## Sudoku logics

Easy sudoku puzzles can be solved with basic strategies of

- Naked single
- Hidden single

for solving harder puzzles, some advanced logics need to be used, such as

- Naked pair, triple, quad
- Hidden pair, triple, quad
- X-wing, XY-wing, XYZ-wing
- Analysis of chain of pairs

Some logics are rarely used. For more difficult problems, these logics do not directly lead to solution, and 'trial and error' approach is required. Computers can easily perform such trial and error with search algorithm.

Actually the easiest way for the computers to solve sudoku is to use only the naked single logic and search algorithm, because the computers can make so many times of trial and errors quite easily. For the human being, using advanced logics is required to solve sudoku.

Kaidoku tries to find the best way for humans to solve a sudoku puzzles, and use the search algorithm as a last resort.

## Logics implemented in Kaidoku

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

More logics will be hopefully implemented.

[back](./)
