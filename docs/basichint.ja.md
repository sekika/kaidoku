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

## Hidden single

Hidden single is another basic logic in sudoku. When naked single is not available, kaidoku checks if this logic can be applied. Therefore when you ask for a hint, this hint is likely to be given next to the naked single.

Actually in some situations hidden single can be found more easily than naked single for humans. Take Level 3 No. 1 for example. You can change to level 3 by `l 3` and this problem is shown (this problem is shown at the top page).

![]({{'/img/3-1.jpg' | relative_url}})

Now if you ask for a hint, this hint is given.

    kaidoku-{{ site.version }}> i
    Look at R2C2. What number is available?

and if you check R2C2, you will find only 6 is available. You can find more naked single pattern in R2C5 as 3, R2C6 as 4. However, it is easier to find a hidden single pattern for me, in the following way.

Look at 2 in R7C8 and R8C6, and also look at box 7. Here box is defined as

| Box 1  | Box 2  | Box 3  |
| Box 4  | Box 5  | Box 6  |
| Box 7  | Box 8  | Box 9  |

and think where 2 can be filled. 2 in R7R8 eliminates the possibility of 2 in row 7, and 2 in R8C6 eliminates the possibility of 2 in row 8. Therefore the possibility of 2 only remains in R9C3 as in the following table.

| x | x | x |
| 1 | 8 | x |
| 4 | 7 |  |

Therefore R9C3 = 2 is determined and you can fill it by `932`. This is the **hidden single** logic. Suppose that in a certain row, line or box, therere is only one place that a certain number can be filled. The cell is a **hidden single**. In this case, R9C3 is a hidden single of 2 in box 7. If you get used to this logic, you can easily find this pattern by scanning 2 in R7C8 and R8C6 horizontally. Hidden single in a box is often easier to find than naked single.

Actually, after filling 2 in R9C3, there remains only 1 cell in box 1 that 2 can be filled, R1C2. Hidden single in 2 in box 1. Now type `122`. Then you can keep on finding hidden single of 2 in boxes. Type `652`, `592`, `372`. Now all of the 2s are determined. Next you can determine all 4s successively by applying hidden single in boxes. Confirm it by typing  `334`, `264`, `744`. Then you can determine all 1s successively by applying hidden single in boxes. Confirm it by typing `131`, `361`, `671`, `521`, `791`. Like this way, you can solve this problem by using only the hidden single logic.

When you type `i` to ask for a hint in the situation that naked single is not available and hidden single is available, hidden single is shown as a hint. For example, go back to the initial position of Level 3 No. 1 by typing `initial`, and then type `226`, `253`, `264`, `118`, `277`, `317`, reaching this position

![]({{'/img/3-1-6.jpg' | relative_url}})

Here you get a hint like this.

    kaidoku-{{ site.version }}> i
    Hidden single in box 1 can be found.

Now you can examine box 1 and you will find that 4 is only available in R3C3.

Almost all of the problems up to level 3 can be solved with the basic logics of naked single and hidden single. Most of the problems in level 4 can also be solved with the basic logics, while in some cases some more advanced logics might be needed.

If you are not familiar with solving sudoku, I would recommend solving the easy problems with kaidoku, in the level you feel comfortable, and get used to the basic logics. Get hints when you get stuck and you will get used to the logics.

## When advanced logic is required

When you try to solve problems in higher levels, you will meet the positions when advanced logics other than naked single and hidden single is required. In such cases, following message appears. It will be discussed in a [later page](advancedhint) of this document.

    kaidoku-{{ site.version }}> i
    Think candidates of the cells.
    See image by "html".
    For more hints, type ii.

## When you made a mistake

Suppose that you made a mistake without realizing it, and you get stuck. In this situation, `i` command will return this message.

    kaidoku-{{ site.version }}> i
    There is no solution for this position. You can take back one move with b.

You can take back one move with `b` and think again. You can get a hint again in this position and you may get a similar message. You can keep this until you get a proper hint. Now this is the position where you made a mistake.

- - -

- [次: 難易度レベル別に問題を選ぶ](./level)
- [前: ナンプレで遊ぶ](./play)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
