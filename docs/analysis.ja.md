---
layout: default.ja
lang: 日本語
ref: analysis
permalink: /ja/analysis
---

# 問題全体の解析

問題全体を解く手順をまとめて見たいときには、`a`コマンドを使う。

    kaidoku-{{ site.version }}> a
    
    Level 5 No. 1
    Valid sudoku with unique solution of level 5 (hard).

デフォルトでは、その問題が正解が1つだけである有効な問題なのかどうか、そしてそうであれば難易度のレベルはいくつなのかが示される。上記の英語は「唯一解を持つ有効な問題で、難易度はレベル5（難しい）である」と表示されている。これが冗長性 (verbose) 1の表示である。`a`コマンドは引数として冗長性を1から5までの数で指定することができる。冗長性の数が大きくなるにつれて、より多くの解析メッセージが表示される。

- `a` は難易度レベルのみを表示する。
- `a 2` は上級解法の一部を表示する。
- `a 3` はすべての上級解法を表示する。
- `a 4` はすべての解法を表示する。
- `a 5` はすべての解法と図面を表示する。

以下が例である。

```
kaidoku-{{ site.version }}> a 4

Level 5 No. 1
Naked single: R4C4 = 4
Naked single: R3C4 = 9
Hidden single in box 1 : R2C1 = 9
Hidden single in box 1 : R2C2 = 7
Hidden single in box 3 : R2C8 = 3
Hidden single in box 4 : R6C1 = 8
Hidden single in box 5 : R5C4 = 3
Hidden single in box 8 : R9C6 = 9
Hidden single in column 8 : R8C8 = 2
Pointing pair in box 1 removed 5 from R9C3 R7C3 
Pointing pair in box 8 removed 5 from R8C4 (=7) R9C5 
Naked single: R1C4 = 5
Hidden single in box 1 : R2C3 = 5
Hidden single in box 2 : R1C5 = 7
Hidden single in box 7 : R9C1 = 7
Hidden single in box 7 : R8C1 = 5
Hidden single in box 7 : R7C3 = 1
Naked single: R7C8 = 4
Naked single: R1C8 = 9, R7C6 = 5
Naked single: R6C8 = 1, R7C5 = 8
Naked single: R6C6 = 7, R7C9 = 7, R9C5 = 4
Naked single: R3C5 = 1, R5C6 = 1, R6C9 = 9, R9C3 = 2
Naked single: R2C6 = 4, R3C7 = 6, R5C5 = 5, R9C2 = 8
Naked single: R1C7 = 8, R2C9 = 1, R5C7 = 7, R8C2 = 4, R9C7 = 5
Naked single: R1C9 = 4, R3C2 = 2, R8C7 = 1, R8C9 = 8
Naked single: R1C3 = 6, R3C1 = 4, R4C2 = 6
Naked single: R4C9 = 2, R5C1 = 2, R5C3 = 4
Naked single: R4C1 = 1, R5C9 = 6
Valid sudoku with unique solution of level 5 (hard).
Here is the solution.
  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|3 1 6|5 7 2|8 9 4|
2|9 7 5|8 6 4|2 3 1|
3|4 2 8|9 1 3|6 7 5|
 +-----+-----+-----+
4|1 6 7|4 9 8|3 5 2|
5|2 9 4|3 5 1|7 8 6|
6|8 5 3|6 2 7|4 1 9|
 +-----+-----+-----+
7|6 3 1|2 8 5|9 4 7|
8|5 4 9|7 3 6|1 2 8|
9|7 8 2|1 4 9|5 6 3|
 +-----+-----+-----+
```

`a` コマンドは問題を最初から解析し、`ac`コマンドは現在の局面から解析する。`all`コマンドは現在のレベルのすべての問題を解析する。`ac`と`all`コマンドも、冗長性を引数に指定できる。

- - -

- [次: 指定された問題の解析](./specified)
- [前: 高度な解法のヒントを見る](./advancedhint)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
