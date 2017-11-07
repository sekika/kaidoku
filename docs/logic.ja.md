---
layout: default.ja
lang: ���{��
ref: logic
permalink: /ja/logic
---

# ���ƁE�i���v���̘_��

���ƁE�i���v�����������߂̘_���ɂ͗l�X�Ȃ��̂�����A�p��A���{��ŗl�X�ȗp�ꂪ����B�����ł́A�p�ꖼ�Ɠ��{�ꖼ��Ή�������B�Ȃ��A�����Ɉ�Έ�Ή������Ă��Ȃ����̂�����B

## ��{���_

�ȒP�Ȗ��́A���̊�{���_�����ŉ������Ƃ��ł���B

- Naked single �}�X�~�A�P�ƌ�␔��
- Hidden single �P�ƌ��}�X

## �����E�㋉�_��

���x�Ȗ��́A��{�_�������ł͑��肸�ɂ��̂悤�Ș_�����g���K�v���o��B

- Pointing pair, triple (also called: Locked candidates, Localization)
- Naked pair, triple, quad �A�̒���m��
- Hidden pair ����m��, Hiddn triple �O������, Hidden quad  �l�d�t�c
- Unique rectangle
- X-wing, Swordfish, Jellyfish �䌅���_
- XY-wing, XYZ-wing
- Analysis of chain of pairs

To solve such difficult problems, usually people write candidates of the numbers in the cells to think which logic can be applied.

## Trial and search

For more difficult problems, these logics do not directly lead to solution, and 'trial and error' approach is required. Computers can easily perform such trial and error with search algorithm. Such puzzles are too hard for normal human beings, but some people enjoy solving such touch puzzles.

## Logics implemented in Kaidoku

Actually the easiest way for the computers to solve sudoku is to use only the naked single logic and search algorithm, because the computers can make so many times of trial and errors quite easily. However, kaidoku uses many logics to find the best way for humans to solve a sudoku puzzle, and use the search algorithm as a last resort.

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
- Chain of pairs
- Trial and search

Unique rectangle is not implmented. It is valid when we know that the sudoku has unique solution. If it is implemented, kaidoku may not correctly identify a sudoku if it has multiple solutions.

More logics will be hopefully implemented.

- - -

- [�}�j���A���̖ڎ�](./#�}�j���A��)
- [�z�[���y�[�W](./)
