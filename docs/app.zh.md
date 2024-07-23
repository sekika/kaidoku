---
layout: app
ref: app
permalink: /zh/app
---
# 数独解独
这是一款**数独应用**，当您选择**难度等级**时，它会随机呈现来自**广泛的谜题**中的问题。按下提示按钮会根据各种**解决策略**提供解决提示，这些策略在随附的**教程书**中进行了说明。

{% capture markdown_content %}
- 免费下载，无广告。在**免费版**中，一旦您通过第4级，您可以玩第5级，并在通过第5级后，您可以继续玩第6级。第6级对于大多数人来说非常困难。对于寻求挑战的用户，通过升级到仅在**iOS版本**中提供的**专业版**，您可以始终玩到第9级。
- 您可以使用**铅笔标记**在单元格中记录多个候选数字，这是解决数独谜题的标准方法。
- 每个级别都有超过780亿种谜题组合，对于人类解决者来说**几乎是无尽的**。
- **教程书**总共包含65页，包括数独位置的图示。

**使用提示**：
- 在提示模式下，始终会提供一个思考提示。如果有**重复**的数字或与正确答案**不同**的数字，提示会提醒您。如果棋盘上没有错误，会根据各种**数独策略**显示提示。
- 在提示模式下，所有候选数字在需要时会自动填充为铅笔标记。
- 最初，通过参考提示解决数独谜题以学习解决技巧。然后尝试在没有提示的情况下解决谜题。当您卡住时，随时可以参考提示。
- 当您在没有参考提示的情况下解决谜题时，您已经**通过**了谜题，并且每个级别的通过次数和最佳通过时间会记录在您的应用程序中。
- 如果您尝试解决谜题，参考提示，并发现错误，您可以轻松地**回溯**到错误发生的情况。提示会解释错误是如何发生的。然后您可以分析原因并从那一点继续解决。通过重复这个过程，您始终可以在提示的帮助下解决谜题。
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>阅读更多</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## 下载
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="二维码" style="display: block; margin-top: 30px;">

## 网页版
也提供[网页版](../sudoku/)。在应用程序版本中，语言是根据系统偏好选择的。在网页版中，可以从以下选项中选择语言。

{% include mobile-lang.html %}

## 其他版本
- [PDF书籍](../book)
- [命令行](../)
