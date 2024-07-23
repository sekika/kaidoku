---
layout: app
ref: app
permalink: /de/app
---
# Sudoku Kaidoku
Es ist eine **Sudoku-App**, die bei Auswahl eines **Schwierigkeitsgrads** zufällig Aufgaben aus einer **großen Auswahl an Rätseln** präsentiert. Wenn Sie die Hinweis-Taste drücken, erhalten Sie Hinweise zur Lösung basierend auf verschiedenen **Lösungsstrategien**, die im beiliegenden **Tutorial-Buch** erklärt werden.

{% capture markdown_content %}
- Kostenloser Download ohne Werbung. In der **kostenlosen Version** können Sie nach dem Erreichen von Level 4 Level 5 spielen und nach dem Erreichen von Level 5 zu Level 6 übergehen. Level 6 ist für die meisten Menschen sehr schwierig. Für herausfordernde Benutzer können Sie durch ein Upgrade auf die **Pro-Version**, die nur in der **iOS-Version** verfügbar ist, immer bis zu Level 9 spielen.
- Sie können **Bleistiftmarkierungen** verwenden, um mehrere Kandidatenzahlen in einer Zelle zu notieren, was eine gängige Methode zur Lösung von Sudoku-Rätseln ist.
- Es gibt über 78 Milliarden Kombinationen von Rätseln auf jedem Level, was es für menschliche Löser **praktisch endlos** macht.
- Das **Tutorial-Buch** umfasst insgesamt 65 Seiten, einschließlich Figuren von Sudoku-Positionen.

**Verwendung von Hinweisen**:
- Im Hinweis-Modus wird immer ein Hinweis für Denktipps gegeben. Wenn es **doppelte** Zahlen oder Zahlen gibt, die **anders** als die richtige Antwort sind, wird der Hinweis Sie darauf hinweisen. Wenn es keine Fehler auf dem Brett gibt, wird ein Hinweis basierend auf verschiedenen **Sudoku-Strategien** angezeigt.
- Im Hinweis-Modus werden alle Kandidatenzahlen automatisch als Bleistiftmarkierungen ausgefüllt, wenn dies erforderlich ist.
- Lösen Sie anfangs Sudoku-Rätsel, indem Sie sich auf Hinweise beziehen, um Lösungstipps zu lernen. Versuchen Sie dann, das Rätsel ohne Hinweise zu lösen. Sie können immer auf einen Hinweis zurückgreifen, wenn Sie stecken bleiben.
- Wenn Sie ein Rätsel ohne Bezug auf einen Hinweis lösen, haben Sie das Rätsel **gelöst**, und die Anzahl der gelösten Rätsel und die beste Zeit für das Lösen jedes Levels werden in Ihrer App aufgezeichnet.
- Wenn Sie versuchen, ein Rätsel zu lösen, einen Hinweis verwenden und Fehler finden, können Sie leicht **zurückverfolgen** zu der Situation, in der der Fehler gemacht wurde. Der Hinweis erklärt, wie der Fehler aufgetreten ist. Sie können dann die Ursache analysieren und von diesem Punkt aus mit der Lösung fortfahren. Durch Wiederholen dieses Prozesses können Sie ein Rätsel immer mit Hilfe von Hinweisen lösen.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Mehr lesen</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Download
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="QR-Code" style="display: block; margin-top: 30px;">

## Webversion
Eine [Webversion](../sudoku/) ist ebenfalls verfügbar. In der App-Version wird die Sprache basierend auf der Systemeinstellung ausgewählt. In der Webversion kann die Sprache aus den folgenden Optionen ausgewählt werden.

{% include mobile-lang.html %}

## Andere Versionen
- [PDF-Bücher](../book)
- [Kommandozeile](../)
