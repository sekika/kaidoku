---
layout: default.ja
lang: 日本語
ref: advancedhint
permalink: /ja/advancedhint
---

# 高度な解法のヒントを見る

## 高度な解法のヒント

例としてレベル5の問題を取り上げる。`l 5`とすることで、レベル 5 の 1 番目が選ばれる。

    kaidoku-{{ site.version }}> l 5
    Level 5 No. 1

![]({{'/img/5-1.jpg' | relative_url}})

この問題を基本解法だけで解き進めると、この場面でこれ以上何もできなくなる。

![]({{'/img/5-1-9.jpg' | relative_url}})

ここで `i` コマンドによって次のようなヒントを得ることができる。

    kaidoku-{{ site.version }}> i
    Think candidates of the cells.
    See image by "html".
    For more hints, type ii.

「マスの候補を考えてください。画像は "html" で見ることができる。さらにヒントを見るには、ii と入力してください。」という意味である。このメッセージについては[簡単に触れた](basichint.md)。これは、基本解法ではこれ以上なにもできないことを意味している。ここで、画像ファイルが次のようにアップデートされている。

![]({{'/img/5-1-9p.jpg' | relative_url}})

それぞれのマスの候補が自動的に書かれるので、どの解法を使えば解けるのかを考えることができる。さらにヒントが必要であれば、`ii`と入力することで次のようなメッセージを得る。

    kaidoku-{{ site.version }}> ii
    Following logics are successively used.
    Pointing pair
    Pointing pair
    See full explanation by typing iii.

どの解法を使えば良いのかが順番に示される。このヒントの意味は、pointing pair を2回連続して使うことで、あるセルが決まるということである。

どのように解法を使うのかを知りたければ、`iii`と入力することで、次のような説明を見ることができる。

    kaidoku-{{ site.version }}> iii
    Pointing pair in box 1 removed 5 from R9C3 R7C3 
    Pointing pair in box 8 removed 5 from R8C4 (=7) R9C5 

ボックス1に 5 の pointing pair があり(R1C3 と R2C3)、R9C3 と R7C3 から 5 が消される。それから、ボックス8に 5 の pointing pair があり(R7C5 と R7C6)、R8C4 と R9C5 から 5 が消される。R8C4 から 5 が消されると、R8C4 は 7 に決まる。これで、`847`と進めることができる。ここから先は、この問題は基本解法のみで解くことができる。

## 部分的に解く

問題を全部解くのではなく、上級解法の解析のみに集中したいときがある。そのようなときには、上級解法が使われる場面にすぐに行きたいと思うであろう。上記の図面から、`initial` コマンドで初期配置に戻ってから、「部分的に解く (solve partially)」コマンド `sp` を使うと、次のようになる。

    kaidoku-{{ site.version }}> sp
    Naked single: R4C4 = 4
    Naked single: R3C4 = 9
    Hidden single in box 1 : R2C1 = 9
    Hidden single in box 1 : R2C2 = 7
    Hidden single in box 3 : R2C8 = 3
    Hidden single in box 4 : R6C1 = 8
    Hidden single in box 5 : R5C4 = 3
    Hidden single in box 8 : R9C6 = 9
    Hidden single in column 8 : R8C8 = 2

![]({{'/img/5-1-9.jpg' | relative_url}})

基本解法の naked single と hidden single が使える間は使い続けて、上級解法が必要とされる場面まで進む。ここで`i`コマンドまたは`jm`コマンドを使うことで、候補の図を見ることができる。

- - -

- [次: 問題全体の解析](./analysis)
- [前: 使われている解法](./logic)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
