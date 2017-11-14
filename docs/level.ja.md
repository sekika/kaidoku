---
layout: default.ja
lang: 日本語
ref: level
permalink: /ja/level
---

# 難易度レベル別に問題を選ぶ

## レベルと問題の選択

解独は、ナンプレの問題を9種類の難易度レベルに分類する、

|Level 1| trivial | 簡単すぎ |
|Level 2| very easy | 超簡単 |
|Level 3| easy | 簡単 |
|Level 4| normal | 普通 |
|Level 5| hard | 難しい |
|Level 6| very hard | とても難しい |
|Level 7| evil | 意地悪 |
|Level 8| extreme | 難しすぎ |
|Level 9| ultimate | 究極 |

レベルは `l レベル` で選ぶことができる。たとえば、レベル 5 を選ぶためには次のようにする。

    kaidoku-{{ site.version }}> l 5
    Level 5 No. 1

どのレベルからでも好きなところから始めて、問題が難しすぎると思ったらレベルを下げて、簡単すぎると思ったらレベルを上げることで、常に自分に最適な難易度の問題を解くことができる。

At each level, you can select the problems by the following commands.

|n |Go to next problem |
|p |Go to previous problem |
|j num |Jump to problem no. num |

Current problem is stored in each level. For example,

- You solved 23 problems in level 3 and you are at level 3, no. 24.
- You go to level 4 and solve 5 problems. Now you are at level 4, no. 6.
- After that, you go back to level 3. In this case, you are at level 3, no. 24.

Note that only the information of the number of problem is stored in each level. Move is stored only for the current problem.

Therefore, recommended way is to start from no. 1 in each level, and after solving a problem you go to the next problem with `n` command.

You can show the index of the problem book by `book` command, which shows the numbers of problems in each level. Kaidoku is shipped with certain numbers of problems in each level. It can increase the numbers of problems by creating new problems. The rate of creating a new problem is faster than a human to solve the problem. Therefore, you can inifinitely enjoy new problems.

## Determination of level

The levels are determined by the numbers of initial blank cells, the difficulty of the logics, and the complexity of seach. Up to level 3 the numbers of blank cells are the dominant factor, up to level 6 the difficulty of the logics is the dominant factor, and from level 7 complexity of the search is the dominant factor.

Current status of kaidoku is in development, and the algorithm to determine the level is not fixed yet. As more logics will be implemented, the level of a certain problem will change. Therefore, the problem book shipped now is a tentative one.

- - -

- [次: 使われている解法](./logic)
- [前: 基本解法のヒントを見る](./basichint)
- [マニュアルの目次](./#マニュアル)
- [ホームページ](./)
