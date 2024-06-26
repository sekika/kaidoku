---
layout: app
ref: app
permalink: /app
---
# Sudoku Kaidoku
It is a Sudoku app that randomly presents problems from a wide range of puzzles when you select a difficulty level. Pressing the hint button provides hints on how to solve it, covering not only basic solving techniques but also various advanced strategies such as Naked Pairs and X-Wing, which are explained in the accompanying tutorial book.

{% capture markdown_content %}
- Free download with no ads. In the Free version, once you clear level 4, you can play level 5, and after clearing level 5, you can proceed to level 6. Level 6 is very difficult for most people. For challenging users, by upgrading to the Pro version, you can always play up to level 9.
- You can use "pencil marks" to note multiple candidate numbers in a cell, which is a standard way of solving Sudoku puzzles.
- There are over 78 billion combinations of puzzles at each level, making it virtually endless for human solvers.
- The tutorial book comprises a total of 65 pages, including figures of Sudoku positions.

Using hints:
- In hint mode, a hint is always provided for thinking tips. If there are duplicate numbers or numbers different from the correct answer, the hint will alert you. If there are no mistakes on the board, a hint is shown based on various Sudoku tactics.
- In hint mode, all candidate numbers are automatically filled as pencil marks when required.
- Initially, solve Sudoku puzzles by referring to hints to learn solving tips. Then attempt solving the puzzle without hints. You can always refer to a hint when you get stuck.
- When you solve a puzzle without referring to a hint, you have "cleared" the puzzle, and the numbers of clear and best time for clearing each level are recorded in your app.
- If you attempt to solve a puzzle, refer to a hint, and find mistakes, you can easily backtrack to the situation where the mistake was made. The hint will explain how the mistake occurred. You can then analyze the cause and resume solving from that point. By repeating this process, you can always solve a puzzle with the help of hints.
{% endcapture %}

{::nomarkdown}
<script>
function showMore(btn) {
   var targetId = btn.getAttribute("href").slice(1);
   document.getElementById(targetId).style.display = "block";
   btn.parentNode.style.display = "none";
   return false;
}
</script>
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; Read more</a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Download
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="QR code" style="display: block; margin-top: 30px;">

## Web version
A [web version](sudoku/) is also available. In the app version, the language is selected based on the system preference. In the web version, language can be selected from the following options.

{% include mobile-lang.html %}

## Other versions
- [PDF books](book)
- [Command-line](./)

## Privacy policy

### 1. Introduction
This privacy policy governs your use of the software application "Sudoku Kaidoku" (hereafter referred to as "the App"). The App does not collect any personal information from its users.

### 2. Collection of Personal Information
The App does not collect any personal information from its users. Therefore, any information that you provide while using the App, including device information, is not collected.

### 3. Use of Personal Information
The App does not use any personal information from its users. Therefore, we will not use any information collected from you for marketing activities, nor will we provide it to third parties.

### 4. Protection of Personal Information
As the App does not collect any personal information from its users, no measures are required to protect such information.

### 5. Changes to the Privacy Policy
Changes to this Privacy Policy may be made due to updates to the App's functions or changes in laws and regulations. If changes occur, we will explicitly state the changes on this page. [Revision history of this page](https://github.com/sekika/kaidoku/commits/master/docs/app.md) is recorded.

### 6. Contact Information
If you have any questions or comments about this policy, please contact me, Katsutoshi Seki, to the email address written in [this paper](https://doi.org/10.2478/johh-2022-0039).
