---
layout: app
ref: app
permalink: /ko/app
---
# Sudoku Kaidoku
이것은 **스도쿠 앱**으로, **난이도 레벨**을 선택할 때 **다양한 퍼즐**에서 무작위로 문제를 제공합니다. 힌트 버튼을 누르면 다양한 **해결 전략**을 기반으로 문제를 푸는 방법에 대한 힌트를 제공합니다. 이러한 전략은 **튜토리얼 책**에 설명되어 있습니다.

{% capture markdown_content %}
- 광고 없는 무료 다운로드. **무료 버전**에서는 4단계를 클리어하면 5단계를 플레이할 수 있으며, 5단계를 클리어한 후에는 6단계로 진행할 수 있습니다. 6단계는 대부분의 사람들에게 매우 어렵습니다. 도전적인 사용자들을 위해 **iOS 버전**에서만 제공되는 **프로 버전**으로 업그레이드하면 항상 9단계까지 플레이할 수 있습니다.
- 셀에 여러 후보 숫자를 기재하기 위해 **연필 표시**를 사용할 수 있으며, 이는 스도쿠 퍼즐을 푸는 표준 방법입니다.
- 각 레벨에서 780억 개 이상의 퍼즐 조합이 있어 인간 해결자에게는 **사실상 무한**입니다.
- **튜토리얼 책**은 스도쿠 위치의 그림을 포함하여 총 65페이지로 구성되어 있습니다.

**힌트 사용**:
- 힌트 모드에서는 사고 팁을 위한 힌트가 항상 제공됩니다. **중복된** 숫자나 정답과 **다른** 숫자가 있으면 힌트가 경고합니다. 보드에 오류가 없으면 다양한 **스도쿠 전략**을 기반으로 힌트가 표시됩니다.
- 힌트 모드에서는 필요한 경우 모든 후보 숫자가 자동으로 연필 표시로 채워집니다.
- 처음에는 힌트를 참고하여 해결 팁을 배우면서 스도쿠 퍼즐을 풉니다. 그런 다음 힌트 없이 퍼즐을 풀어보세요. 막히면 언제든지 힌트를 참고할 수 있습니다.
- 힌트를 참고하지 않고 퍼즐을 풀면 퍼즐을 **클리어**한 것이며, 각 레벨을 클리어한 횟수와 최단 시간이 앱에 기록됩니다.
- 퍼즐을 풀다가 힌트를 참고하고 오류를 발견하면, 오류가 발생한 상황으로 쉽게 **되돌아갈 수** 있습니다. 힌트는 오류가 어떻게 발생했는지 설명합니다. 그런 다음 원인을 분석하고 그 지점부터 해결을 재개할 수 있습니다. 이 과정을 반복하면 항상 힌트의 도움을 받아 퍼즐을 풀 수 있습니다.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>더 읽기</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## 다운로드
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="QR 코드" style="display: block; margin-top: 30px;">

## 웹 버전
[웹 버전](../sudoku/)도 제공됩니다. 앱 버전에서는 시스템 설정에 따라 언어가 선택됩니다. 웹 버전에서는 아래 옵션에서 언어를 선택할 수 있습니다.

{% include mobile-lang.html %}

## 기타 버전
- [PDF 책](../book)
- [명령 줄](../)
