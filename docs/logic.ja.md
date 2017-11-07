---
layout: default.ja
lang: 日本語
ref: logic
permalink: /ja/logic
---

# 使われている論理

数独・ナンプレを解くための論理には様々なものがあり、英語、日本語で様々な用語がある。ここでは、英語名と日本語名を対応させる。なお、厳密に一対一対応をしていないものもある。

## 基本理論

簡単な問題は、この基本理論だけで解くことができる。

- Naked single マスミ、単独候補数字
- Hidden single 単独候補マス

## 中級・上級論理

高度な問題は、基本論理だけでは足りずにこのような論理を使う必要が出る。

- Pointing pair, triple (also called: Locked candidates, Localization)
- Naked pair, triple, quad 陰の定員確定
- Hidden pair 定員確定, Hiddn triple 三国同盟, Hidden quad  四重奏団
- Unique rectangle
- X-wing, Swordfish, Jellyfish 井桁理論
- XY-wing, XYZ-wing
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

More logics will be hopefully implemented.

- - -

- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
