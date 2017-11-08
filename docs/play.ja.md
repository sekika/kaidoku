---
layout: default.ja
lang: 日本語
ref: play
permalink: /ja/play
---

# ナンプレで遊ぶ

## 問題を表示する

[解独のインストールと解独コマンドプロンプトの立ち上げ](install)までは終わっているものとして、ここからは解独コマンドプロンプト内での操作方法について記す。まずは、`c` と入力することで次のように問題が表示される。

```
kaidoku-{{ site.version }}> c
Level 2 No. 1
  1 2 3 4 5 6 7 8 9
 +-----+-----+-----+
1|9    |8 5  |2 1 4|
2|5 4 2|1 6 3|  7  |
3|8    |    2|    3|
 +-----+-----+-----+
4|3   1|    4|    7|
5|  7  |3   6|  2  |
6|2    |9    |4   5|
 +-----+-----+-----+
7|1    |6    |    2|
8|  2  |7 1 5|3 4 8|
9|7 3 8|  4 9|    6|
 +-----+-----+-----+

Type 3 digits (row, column, number) to put a number. i for hint.

kaidoku-{{ site.version }}>
```

解独は難易度がレベル分けされたナンプレの問題集があらかじめ用意されている。解独をはじめて起動したときには、レベル2が自動的に選ばれている。そのため、レベル2の1番目の問題が表示される。

## 画像の生成

ここから問題を解き始めることもできるが、その前に、端末上のアスキー図では見にくいので、画像を生成すると良い。そのために、まずは `jpg` コマンドで画像を生成する。そのときに、データ用のディレクトリを聞かれるので、指定する。何も入力しなければ、デフォルトの `‾/kaidoku` ディレクトリがデータディレクトリとして指定される。

```
kaidoku-{{ site.version }}> jpg
Data directory does not exist.
Input name of the data directory (default: ‾/kaidoku):
See image by "html".
kaidoku-{{ site.version }}>
```

これで、このような画像ファイルが、データディレクトリの下に current.jpg として生成される。

![]({{'/img/2-1.jpg' | relative_url}})

次に、`html`コマンドを実行することで、デフォルトのウェブブラウザで画像ファイルを閲覧するための html ファイルが開かれる。その html ファイルは2秒ごとに画像ファイルを自動的に読み直す（秒数はテキストボックスで調整できる）。ここから先は、問題を解き進めると自動的に画像ファイルが更新されて、html ファイルが画像ファイルを再読み込みするので、ウェブブラウザで図面が更新されるのを見ながら解き進めることができる。

## 数字を埋める

これで、問題を解く準備が整ったので、解き始めることとする。上の図を見て、どこから解き始めるかを考えてみよう。

ここで、**2行9列** (row 2, column 9) を見る。行と列の意味は

- **2行** (row 2) は、上から2番目の横一行
- **9列** (column 9) は、左から9番目の縱一列

である。そして、2行9列は **R2C9** と表記される。2行目に入っている数は、1から9までの数の中で8と9だけが入っていないので、R2C9には8か9が入る。そして、9列目にはR8C9に8があるため、R2C9に8は入らない。よって、R2C9は9となる。

あるマス目にどの数字が入ることが可能かと考えるときには、同じ行、列、ボックスの数字を一通り見て、その中に入っている数字は候補から外れる。その結果、候補がただ1つだけ残るときには、その数がそのマス目に入る数字となる。この解法を **naked single** という。日本語では、**マスミ**あるいは**単独候補数字**などと言われる。この解法を使うことで、R2C9が9であると確定する。

それでは、R2C9に9を入れる。**Type 3 digits (row, column, number) to put a number.** という指示が表示されているように、行 (row)、列 (column)、数字 (number) の順番で3つの数字を入れる。この場合は、2行9列に9を入れるので`299`と入力する。

    kaidoku-{{ site.version }}> 299

更新されたアスキーの図が表示され、ブラウザに表示されている html ファイルの画像が、次のように自動的に更新される。

![]({{'/img/2-1-1.jpg' | relative_url}})

## 解答を続ける

これで2行目には空のマスが1つだけになるため、R2C7が2であることが簡単にわかる。同様に、9列目には空のマスが1つだけなのでR5C9は1である。単独候補数字 (naked single) によってR8C1に6を入れると、1列目は空のマスが1つだけになってR5C1は4となり、8行目は空のマスが1つになってR8C3は9となる。ここまでの数字を、以下のように入れることができる。

    kaidoku-{{ site.version }}> 278
    kaidoku-{{ site.version }}> 591
    kaidoku-{{ site.version }}> 816
    kaidoku-{{ site.version }}> 514
    kaidoku-{{ site.version }}> 839

![]({{'/img/2-1-6.jpg' | relative_url}})

## Notifying a mistake

When you put a number that is unable to be placed, the number is not placed. For example if you type `722` in this situation, warning message is shown as follows.

    kaidoku-{{ site.version }}> 722
    Both R7C2 and R7C9 have the same value of 2.

## Take back a move

You can always erase a number that was written at the last time. Just type `b`.

    kaidoku-{{ site.version }}> b
    Level 2 No. 1: move 5

Writing a number is regarded as a "move", and we call it "take back a move". You can take back as many moves as possible, until you reach the initial position.

## Quit and restart

You can always quit the game by `q`. The status is saved in configuration file, and when you run kaidoku next time, you can start from the position where you quitted last time. Just type `c` or `html` to show the position and continue.

## Finish a problem and go to the next problem

This problem can be solved with only the naked single logic. When you fill out all the blank cells, a massage appears that

    Now this problem is solved !

You can go to the next problem with `n`.

    kaidoku-{{ site.version }}> n
    Level 2 No. 2

- - -

- [前: インストールと実行](./install)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
