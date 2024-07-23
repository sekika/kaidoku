---
layout: app
ref: app
permalink: /es/app
---
# Sudoku Kaidoku
Es una **aplicación de Sudoku** que presenta problemas al azar de una **amplia gama de rompecabezas** cuando seleccionas un **nivel de dificultad**. Al presionar el botón de pista, se proporcionan pistas sobre cómo resolverlo basadas en varias **estrategias de resolución**, que se explican en el **libro tutorial** adjunto.

{% capture markdown_content %}
- Descarga gratuita sin anuncios. En la **versión gratuita**, una vez que superes el nivel 4, puedes jugar al nivel 5, y después de superar el nivel 5, puedes proceder al nivel 6. El nivel 6 es muy difícil para la mayoría de las personas. Para los usuarios que buscan un desafío, al actualizar a la **versión Pro**, que está disponible solo en la **versión iOS**, siempre puedes jugar hasta el nivel 9.
- Puedes usar **marcas de lápiz** para anotar múltiples números candidatos en una celda, lo cual es una forma estándar de resolver rompecabezas de Sudoku.
- Hay más de 78 mil millones de combinaciones de rompecabezas en cada nivel, lo que lo hace **prácticamente interminable** para los solucionadores humanos.
- El **libro tutorial** consta de un total de 65 páginas, incluyendo figuras de posiciones de Sudoku.

**Usando pistas**:
- En el modo de pistas, siempre se proporciona una pista para consejos de pensamiento. Si hay números **duplicados** o números **diferentes** de la respuesta correcta, la pista te alertará. Si no hay errores en el tablero, se muestra una pista basada en varias **estrategias de Sudoku**.
- En el modo de pistas, todos los números candidatos se llenan automáticamente como marcas de lápiz cuando es necesario.
- Inicialmente, resuelve los rompecabezas de Sudoku refiriéndote a las pistas para aprender consejos de resolución. Luego intenta resolver el rompecabezas sin pistas. Siempre puedes referirte a una pista cuando te quedes atascado.
- Cuando resuelvas un rompecabezas sin referirte a una pista, habrás **superado** el rompecabezas, y el número de veces que lo superes y el mejor tiempo para superar cada nivel se registran en tu aplicación.
- Si intentas resolver un rompecabezas, te refieres a una pista y encuentras errores, puedes **retroceder** fácilmente a la situación en la que se cometió el error. La pista explicará cómo ocurrió el error. Luego puedes analizar la causa y reanudar la resolución desde ese punto. Al repetir este proceso, siempre puedes resolver un rompecabezas con la ayuda de las pistas.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Leer más</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Descargar
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="Código QR" style="display: block; margin-top: 30px;">

## Versión web
También está disponible una [versión web](../sudoku/). En la versión de la aplicación, el idioma se selecciona según la preferencia del sistema. En la versión web, el idioma se puede seleccionar de las siguientes opciones.

{% include mobile-lang.html %}

## Otras versiones
- [Libros PDF](../book)
- [Línea de comandos](../)
