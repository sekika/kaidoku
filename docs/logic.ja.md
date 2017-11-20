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

このような難しい問題を解くためには、通常候補数字をメモする。紙と鉛筆を使うときには、それぞれの数字をセル内の位置に対応させたペンシルマークで候補数字を簡易的にメモする技法もある。このような高度な解法について、詳細ではこのサイトでは踏み込まない。以下のサイトを参照。

- [ナンバープレース、数独 解法まとめ](http://www.geocities.jp/master_mishichan/)
- [数独の解き方](http://www.sudokugame.org/solv/)
- [SudokuWiki.org - Strategy Families](http://www.sudokuwiki.org/Strategy_Families)

## 試行と探索

より難しい問題では、上述のような解法を使っても正解にたどり着くことができず、試行錯誤が必要とされる。たとえば、 R2C3 に2, 4, 6 の3つの候補数字があるとする。それぞれの数について、R2C3がその数であると仮定をして解き進める。はじめに、R2C3が2であると仮定して説き進め、矛盾が生じたとすれば、2を候補数字から外すことができる。4も候補数字から外すことができれば、R2C3が6であると確定する。[SudokuWiki.org](http://www.sudokuwiki.org/) で解説されている多くの高度な解法は、ある「仮定ー矛盾」関係をいかにして見つけるか、という戦略である。[西尾理論](http://www.sudokuwiki.org/Nishio_Forcing_Chains)のページの解説図を例にとる。この図において、G2 = 6 と仮定すれば、hidden single によって J4 = 6 と J1 = 2 が、さらに hidden single によって H9 = 6 が、そして naked single によって J9 = 5 と G7 = 8 が決まり、 G8 の候補がなくなって矛盾となる。試行錯誤は、特にペア（2つの候補数字）のチェーンで有効である。なぜならば、1つのマス目を仮定すれば、次々と他のペアのマス目が決定するためである。そこで、解独では2つの候補数字を持つマス目だけに限定した試行を実行して、ペアチェーンの解析 (analysis of chain of pairs) としている。

試行錯誤は、探索アルゴリズムによって再帰的に実行することができる。このページの最初の例において、R2C3 = 2 の仮定を探索している途中で、他のマス目で他の仮定をする。それで十分でなければ、さらに別の仮定をする。空白セルの数は有限であり、仮定を1つするたびに空白セルの数が1つ減るため、これは無限ループとはならない。したがって、この再帰的な探索アルゴリズムによって必ず最終的な結論を得ることができる。If we have 3 candidates in a certain cell and for each candidates we make 5 trials, we make 15 trials in total. The numbers of trials are multiplied in this way. Computers can easily perform such large numbers of trials and errors with search algorithm. Such puzzles requiring extensive search are too hard for normal human beings, but a small number of trials and errors are actually available. It can also be solved with luck. In any case, problems requiring the trial and error approach is too hard for avaraged sudoku players. Some people enjoy such difficult problems, and kaidoku offers such problems in beyond level 7 to meet the need for strongest sudoku players.

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
