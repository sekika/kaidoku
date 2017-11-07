---
layout: default.ja
lang: 日本語
ref: install
permalink: /ja/install
---

# インストールと実行

## Python 3 のインストール

解独をインストールするためには、まず Python 3 をインストールする必要がある。Python 3 のインストールについては、以下のようにする。

- [Python オフィシャルホームページ](https://www.python.org/)からダウンロードとインスストールをする。
- macOS で [Homebrew](https://brew.sh/) を使っているのであれば  `brew install python3` を実行する。

インストールされている Python 3 のバージョンは、次のコマンドで確認できる。

    python3 -V

## 解独のインストール

Python 3 のインストールができたら、ターミナルエミュレーターから次のコマンドで解独をインストールする。

    pip3 install kaidoku

## 解独のアップデート

[最新のバージョン](https://pypi.python.org/pypi/kaidoku)は **{{ site.version }}**

解独の最新バージョンは

    pip3 search kaidoku

で確認できる。最新バージョンへのアップデートは

    pip3 install -U kaidoku
 
とする。

## 解独の実行

ターミナルエミュレータから

    kaidoku

と実行すると、次のように解独のコマンドプロンプトに入る。

    $ kaidoku
    Kaidoku - player, solver and creater of sudoku puzzles.
              https://sekika.github.io/kaidoku/
    Type h for help, c for showing a problem, q for quit.
    kaidoku-{{ site.version }}>

コマンドのヘルプは `h` と入力することで、次のように表示される。

```
kaidoku-{{ site.version }}> h
246 : In the cell of row 2 column 4, put number 6
b   : take Back one move
c   : show Current position
i   : show hInt for current position
q   : Quit kaidoku

(中略)

kaidoku-{{ site.version }}> 
```

解独のコマンドプロンプトから抜けるためには `q` と入力する。

- - -

- [次: ナンプレで遊ぶ](./play)
- [前: 数独・ナンプレのルール](./rule)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
