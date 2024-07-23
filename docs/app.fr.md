---
layout: app
ref: app
permalink: /fr/app
---
# Sudoku Kaidoku
C'est une **application Sudoku** qui présente aléatoirement des problèmes parmi une **large gamme de puzzles** lorsque vous sélectionnez un **niveau de difficulté**. En appuyant sur le bouton d'indice, des indices sur la façon de le résoudre sont fournis en fonction de diverses **stratégies de résolution**, qui sont expliquées dans le **livre tutoriel** accompagnant.

{% capture markdown_content %}
- Téléchargement gratuit sans publicité. Dans la **version gratuite**, une fois que vous avez terminé le niveau 4, vous pouvez jouer au niveau 5, et après avoir terminé le niveau 5, vous pouvez passer au niveau 6. Le niveau 6 est très difficile pour la plupart des gens. Pour les utilisateurs en quête de défis, en passant à la **version Pro**, disponible uniquement sur la **version iOS**, vous pouvez toujours jouer jusqu'au niveau 9.
- Vous pouvez utiliser des **marques de crayon** pour noter plusieurs numéros candidats dans une cellule, ce qui est une méthode standard pour résoudre les puzzles Sudoku.
- Il y a plus de 78 milliards de combinaisons de puzzles à chaque niveau, ce qui le rend **pratiquement infini** pour les solveurs humains.
- Le **livre tutoriel** comprend un total de 65 pages, y compris des figures des positions de Sudoku.

**Utilisation des indices**:
- En mode indice, un indice est toujours fourni pour des conseils de réflexion. S'il y a des numéros **dupliqués** ou des numéros **différents** de la réponse correcte, l'indice vous alertera. S'il n'y a pas d'erreurs sur le tableau, un indice est montré en fonction de diverses **stratégies de Sudoku**.
- En mode indice, tous les numéros candidats sont automatiquement remplis en tant que marques de crayon lorsque cela est nécessaire.
- Au début, résolvez les puzzles de Sudoku en vous référant aux indices pour apprendre des conseils de résolution. Ensuite, essayez de résoudre le puzzle sans indices. Vous pouvez toujours vous référer à un indice lorsque vous êtes bloqué.
- Lorsque vous résolvez un puzzle sans vous référer à un indice, vous avez **terminé** le puzzle, et le nombre de fois que vous l'avez terminé ainsi que le meilleur temps pour terminer chaque niveau sont enregistrés dans votre application.
- Si vous essayez de résoudre un puzzle, vous vous référez à un indice et trouvez des erreurs, vous pouvez facilement **revenir** à la situation où l'erreur a été commise. L'indice expliquera comment l'erreur s'est produite. Vous pouvez alors analyser la cause et reprendre la résolution à partir de ce point. En répétant ce processus, vous pouvez toujours résoudre un puzzle avec l'aide des indices.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Lire plus</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Télécharger
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="Code QR" style="display: block; margin-top: 30px;">

## Version web
Une [version web](../sudoku/) est également disponible. Dans la version de l'application, la langue est sélectionnée en fonction de la préférence du système. Dans la version web, la langue peut être sélectionnée parmi les options suivantes.

{% include mobile-lang.html %}

## Autres versions
- [Livres PDF](../book)
- [Ligne de commande](../)
