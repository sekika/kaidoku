---
layout: default.ja
lang: 日本語
ref: specified
permalink: /ja/specified
---

# 指定された問題の解析

指定された問題を `check` コマンドに続いて問題の局面を入れることでチェックすることができる。局面は数字を連続して入れることで表現する。空白のマスは0とする。例えば、この図面は

![]({{'/img/5-1.jpg' | relative_url}})

次のように表現できる。

    310002000000860200008003075007098350090000080053620400630200900009036000000100063

オンラインで[ナンプレ問題集](sudoku)を解いているのであれば、キーボードから`c`と入力することで、現局面がクリップボードにコピーされる。その局面は `check pos [verb]` コマンドでチェックすることができる。ここで pos は局面で verb は冗長性レベル（省略時は 1）である。

- `check pos` はその局面が唯一解を持つかどうかを表示する。
- `check pos 2` は[基本解法](basichint) (naked single と hidden single) のヒントを表示する。
- `check pos 3` はあるセルが決定するまでの[上級解法](logic)のヒントを表示する。
- `check pos 4` はあるセルが決定するまでの手順を表示する。

```
kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063

This position has a unique solution.

kaidoku-{{ site.version }}> check 310002000000860200008003075007098350090000080053620400630200900009036000000100063 2

Look at R4C4. What number is available?
```

`solve` コマンドによってその問題を解くための手順がすべて表示される。このコマンドの使い方は

    solve pos [verb]
 
であり、
 
- `solve pos` は難易度レベルのみを表示する。
- `solve pos 2` は探索のヒントを表示する。
- `solve pos 3` は探索の結果と上級解法のヒントを表示する。
- `solve pos 4` はすべての解法を表示する。
- `solve pos 5` はすべての解法と図面を表示する。

# 図面を表現する他の方法

- 数字を列ごとにコンマ`,`で区切ることができる。この場合は、コンマの間に9個の数字がなければならない。
- 0 は - のような他のアスキー文字に変えることができる。

したがって、次のようなコマンドが可能となる。

    kaidoku-{{ site.version }}> check 31---2---,---86-2--,--8--3-75,--7-9835-,-9-----8-,-5362-4--,63-2--9--,--9-36---,---1---63

印刷物から図面を入力するときには、入力ミスをしたときにどの列が間違えているのかが表示されるため、この方法は便利である。

# 例

[数独の最難問](http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html)を解析する。PCの性能にもよるが、解析には数秒かかる。

    kaidoku-{{ site.version }}> solve 8--------,--36-----,-7--9-2--,-5---7---,----457--,---1---3-,--1----68,--85---1-,-9----4-- 2
    
    Search with depth 3 from R8C7.
    Search with depth 3 from R7C7.
    Search with depth 2 from R7C5.
    Search with depth 3 from R8C9.
    Search with depth 3 from R9C4.
    Search with depth 1 from R6C7.
    Search with depth 2 from R1C7.
    Valid sudoku with unique solution of level 9 (ultimate).
    
いかに深い探索がなされているかが分かる。完全な解法を見るには、このようにする。

    kaidoku-{{ site.version }}> solve 8--------,--36-----,-7--9-2--,-5---7---,----457--,---1---3-,--1----68,--85---1-,-9----4-- 5

[結果](https://github.com/sekika/kaidoku/blob/master/docs/solution-Inkala-2012.txt)はこのようになる。

- - -

- [前: 問題全体の解析](./analysis)
- [次: ブックマークの管理](./bookmark)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
