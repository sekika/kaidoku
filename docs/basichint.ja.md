---
layout: default.ja
lang: 日本語
ref: basichint
permalink: /ja/basichint
---

# 基本解法のヒントを見る

## ヒントを見る

`i`と入力することでヒントを見ることができる。[遊び方](play)で示した最初の図面を例として見る。ここで、問題の最初に戻るには `initial` と入力する。

![]({{'/img/2-1.jpg' | relative_url}})

ここで`i`と入力することで、次のようなヒントを見ることができる。

    kaidoku-{{ site.version }}> i
    Look at R1C2. What number is available?

つまり「R1C2を見てください。どの数字が入りますか？」と聞かれている。これが、マスミすなわち naked single 解法を使うことができるときに表示されるヒントの形式である。この形式のヒントが出たときには、そのマスに入る数字は1つしかない。この場合は、R1C2に入る数字は6しかないことがわかる。マスミはナンプレの基本解法の1つであり、解独では最初にマスミが適用可能であるかどうかを調べる。そのため、このヒントを見る可能性が最も高い。

## 単独候補マス

ナンプレの基本解法には、マスミともう1つ**単独候補マス** (**Hidden single**) がある。[ニコリの解説](http://www.nikoli.co.jp/ja/publication/number/sudoku_communication/)では、ブロックの単独候補マスが**ブロッケン**で、行あるいは列の単独候補マスが**レッツミー**となる。解独立ではマスミの次に単独候補マスを調べるため、マスミの次に出やすいヒントである。

実際には、マスミよりも単独候補マス、特にブロッケンを発見しやすいことがよくある。レベル3の問題1を例にとる。`l 3`と入力することでレベル3に移ることができて、次のような問題が表示される。この問題は、トップページの図と同じである。

![]({{'/img/3-1.jpg' | relative_url}})

ここで、ヒントを見るとこのように表示される。

    kaidoku-{{ site.version }}> i
    Look at R2C2. What number is available?

これはマスミのヒントであり、R2C2を見ると6が入ることがわかる。他にも、マスミによって R2C5 が 3であり、R2C6が4であることがわかる。ところが、このマスミのマスを発見するよりも、次のようなブロッケンのパターンを発見する方がむしろ速いだろう。

R7C8とR8C6の2と、ボックス7に着目して、ボックス7のどこに2が入るのかを考える。ここで、ボックスの番号は

| Box 1  | Box 2  | Box 3  |
| Box 4  | Box 5  | Box 6  |
| Box 7  | Box 8  | Box 9  |

のように決める。そして、R7Rの2は7行に2が入る可能性をなくして、R8C6の2は8行に2が入る可能性をなくすため、次の図のように、R9C3だけにしか2が入る場所がなくなる。

| x | x | x |
| 1 | 8 | x |
| 4 | 7 |  |

よって R9C3 = 2 が決まり、`932`と入力できる。これが単独候補マス (hidden single) の解法である。すなわち、ある行、列、ボックスのいずれかの中で、ある数字が入る場所が1箇所だけだったとする。そのマスが単独候補マスとなる。このケースでは、R9C3がボックス7における2の単独候補マスである。この解法に慣れると、R7C8とR8C6の2を横に流して見ることで簡単に単独候補マスを見つけることができる。ボックスの単独候補マス、すなわちブロッケンは、マスミよりも見つけやすい場合が多い。

R9C3に2を入れた後には、ボックス1には2が入る場所はR1C2の1箇所しかなくなる。ボックス1の単独候補マスである。`122`と入力してこれを埋める。さらに、2の単独候補マスをブロッケンで見つけ続けることができる。`652`, `592`, `372`と連続で2を埋めることができる。これで、すべての2が決まった。次に、すべての4をブロッケンによって連続的に決めることができる。`334`, `264`, `744`と入力する。次に、すべての1を連続的にブロッケンで決めることができる。`131`, `361`, `671`, `521`, `791`となる。このように、この問題は単独候補マスの解法だけで解くことが可能である。また、同じ数字で連続的に単独候補マスが決まることもよくある。

マスミが使えずに単独候補マスが可能なときに `i` でヒントを表示すると、単独候補マスのヒントを見ることができる。たとえば、レベル3の1問目に `initial` コマンドで戻ってから `226`, `253`, `264`, `118`, `277`, `317` と入力して、この図面になったときに

![]({{'/img/3-1-6.jpg' | relative_url}})

次のようにヒントが表示される。

    kaidoku-{{ site.version }}> i
    Hidden single in box 1 can be found.

つまり「ボックス1に単独候補マスがある」と表示される。そこで、ボックス1をよく見ると、4がR3C3のみに入ることがわかる。

レベル3までのほぼすべての問題は naked single と hidden single の基本解法のみで解くことができる。レベル4の問題も、ほとんどは基本解法のみで解くことができるが、時々より進んだ解法が必要となる。

数独にあまり慣れていないのであれば、まずは解独で簡単な問題を解いて基本解法に慣れるのが良いであろう。詰まったときにはヒントを見て考えれば、次第に解法に慣れることができる。

## 高度な解法が必要なとき

より高いレベルの問題を解こうとすると、naked single と hidden single のような基本解法のみでは解けずに、より高度な解法が必要となるときがある。そのようなときには、次のようなヒントが表示される。これは、[後ほど](advancedhint)取り上げる。

    kaidoku-{{ site.version }}> i
    Think candidates of the cells.
    See image by "html".
    For more hints, type ii.

## 間違えたとき

間違えに気がつかずに解き進めて、解答がストップしてしまったとする。このときには `i` コマンドで次のようなメッセージが表示される。

    kaidoku-{{ site.version }}> i
    There is no solution for this position. You can take back one move with b.

「この場面からは解答がありません。b で手を1つ戻すことができます」という意味である。ここで、`b`コマンドで手を1つ戻して考え直すことができる。適正なヒントが表示されるまで同様に繰り返せば、あなたがミスをした直前まで戻ることができる。

- - -

- [次: 難易度レベル別に問題を選ぶ](./level)
- [前: ナンプレで遊ぶ](./play)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
