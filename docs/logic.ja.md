---
layout: default.ja
lang: 日本語
ref: logic
permalink: /ja/logic
---

# 使われている解法

数独・ナンプレを解くための解法（ロジック、テクニック）には様々なものがあり、英語、日本語で様々な用語がある。ここでは、英語名と日本語名を対応させる。なお、用語の定義は人によっても微妙に異なることがあり、英語と日本語で厳密に一対一対応をしていないものもある。

## 基本解法

簡単な問題は、この基本解法だけで解くことができる。

- Naked single マスミ、単独候補数字、裸のシングル
- Hidden single 単独候補マス、隠れたシングル

## 高度な解法

高度な問題は、基本解法だけでは足りずにこのような解法を使う必要が出る。

- Pointing pair, triple (also called: Locked candidates, Localization) いずれにしても理論、ロックされた候補
- Naked pair, Hidden pair 二国同盟
- Naked triple, Hidden triple 三国同盟
- Naked quad, Hidden quad  四国同盟
- Unique rectangle
- X-wing, Swordfish, Jellyfish 井桁理論、四角の対角線
- XY-wing, XYZ-wing
- Remote pairs
- Analysis of chain of pairs

To solve such difficult problems, usually people write candidates of the numbers in the cells to think which logic can be applied. Detail of each logic is not discussed in this page. Please refer to these sites.

- [SudokuWiki.org - Strategy Families](http://www.sudokuwiki.org/Strategy_Families)
- [sudoku-solutions.com - Background](http://www.sudoku-solutions.com/index.php?page=background)

## Trial and search

For more difficult problems, the above logics do not directly lead to solution, and 'trial and error' approach is required. Suppose that R2C3 has 3 candidate numbers, 2, 4, 6. For each number, we assume that R2C3 is that number. First we assume that R2C3 is 2 and keep solving. If we meet a contradiction, we can eliminate 2 from the candidates. If 4 is also eliminated, R2C3 should be 6. Many advanced logics explained in  [SudokuWiki.org](http://www.sudokuwiki.org/) are trying to find a certain (assumption - contradiction) combination strategically. Take [Nishio forcing chains](http://www.sudokuwiki.org/Nishio_Forcing_Chains) for example. In the diagram pattern in the page, assuming G2 = 6 leads J4 = 6 and J1 = 2 by hidden single, H9 = 6 by hidden single, J9 = 5 and G7 = 8 by naked single, and G8 has no candidate, which is contradiction. Trial approach is especially useful for chain of pairs, because one assumption successively determines many cells. Therefore in kaidoku trial and error approach is performed for cells with 2 candidates, and it is regarded as the analysis of chain of pairs.

Trials and errors can be recursively employed with search algorithm. In the first example of this section, while examining R2C3 = 2, we will make another assumption in another cell. If that is not enough, make another assumption. As we have only finite numbers of blank cells and an assumption reduces the numbers of blank cell, this is not infinite steps. Therefore we can always get to the final conclusion. If we have 3 candidates in a certain cell and for each candidates we make 5 trials, we make 15 trials in total. The numbers of trials are multiplied in this way. Computers can easily perform such large numbers of trials and errors with search algorithm. Such puzzles requiring extensive search are too hard for normal human beings, but a small number of trials and errors are actually available. It can also be solved with luck. In any case, problems requiring the trial and error approach is too hard for avaraged sudoku players. Some people enjoy such difficult problems, and kaidoku offers such problems in beyond level 7 to meet the need for strongest sudoku players.

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
- XYZ-wing
- Remote pairs
- Naked quad
- Hidden quad
- Swordfish
- Jellyfish
- Chain of pairs
- Trial
- Search

Unique rectangle is not implmented. It is valid when we know that the sudoku has a unique solution. However, testing the validity of sudoku is one of the purpose in kaidoku. If it is implemented, kaidoku may not correctly evaluate if a sudoku has a unique solution.

Trial and search is basically doing the same thing, but it is distinguished in kaidoku. Search performs a complete search in many depths. Here depth means the numbers of successive assumptions. We make first assumption in a certain cell, keep on solving with logics, and make another assumption; this is depth 2. Trial is the search within depth 1, starting from a pair candidate cell, within certain steps. Here step means the numbers of cells eliminated with naked single or hidden single logic. In short, trial is the search algorithm restricted within human ability. Trial may not get to final conclusion, but search always reaches the final conclusion.

- - -

- [次: 高度な解法のヒントを見る](./advancedhint)
- [前: 難易度レベル別に問題を選ぶ](./level)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
