---
layout: app
ref: app
permalink: /it/app
---
# Sudoku Kaidoku
È un'**app di Sudoku** che presenta casualmente problemi da un'**ampia gamma di puzzle** quando selezioni un **livello di difficoltà**. Premendo il pulsante suggerimento, vengono forniti suggerimenti su come risolverlo basati su varie **strategie di risoluzione**, spiegate nel **libro tutorial** allegato.

{% capture markdown_content %}
- Download gratuito senza pubblicità. Nella **versione gratuita**, una volta completato il livello 4, puoi giocare al livello 5, e dopo aver completato il livello 5, puoi passare al livello 6. Il livello 6 è molto difficile per la maggior parte delle persone. Per gli utenti che cercano una sfida, passando alla **versione Pro**, disponibile solo nella **versione iOS**, puoi giocare sempre fino al livello 9.
- Puoi usare i **segni di matita** per annotare più numeri candidati in una cella, che è un modo standard per risolvere i puzzle di Sudoku.
- Ci sono oltre 78 miliardi di combinazioni di puzzle a ogni livello, rendendolo **praticamente infinito** per i solutori umani.
- Il **libro tutorial** comprende un totale di 65 pagine, comprese figure delle posizioni del Sudoku.

**Utilizzo dei suggerimenti**:
- In modalità suggerimento, viene sempre fornito un suggerimento per i consigli di riflessione. Se ci sono numeri **duplicati** o numeri **diversi** dalla risposta corretta, il suggerimento ti avviserà. Se non ci sono errori sulla tavola, viene mostrato un suggerimento basato su varie **strategie di Sudoku**.
- In modalità suggerimento, tutti i numeri candidati vengono automaticamente riempiti come segni di matita quando necessario.
- Inizialmente, risolvi i puzzle di Sudoku facendo riferimento ai suggerimenti per imparare i consigli di risoluzione. Quindi prova a risolvere il puzzle senza suggerimenti. Puoi sempre fare riferimento a un suggerimento quando sei bloccato.
- Quando risolvi un puzzle senza fare riferimento a un suggerimento, hai **completato** il puzzle e il numero di completamenti e il miglior tempo per ogni livello vengono registrati nella tua app.
- Se provi a risolvere un puzzle, fai riferimento a un suggerimento e trovi errori, puoi facilmente **tornare indietro** alla situazione in cui è stato commesso l'errore. Il suggerimento spiegherà come si è verificato l'errore. Puoi quindi analizzare la causa e riprendere la risoluzione da quel punto. Ripetendo questo processo, puoi sempre risolvere un puzzle con l'aiuto dei suggerimenti.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Leggi di più</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Scarica
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="Codice QR" style="display: block; margin-top: 30px;">

## Versione web
È disponibile anche una [versione web](../sudoku/). Nella versione app, la lingua viene selezionata in base alla preferenza del sistema. Nella versione web, la lingua può essere selezionata tra le seguenti opzioni.

{% include mobile-lang.html %}

## Altre versioni
- [Libri PDF](../book)
- [Linea di comando](../)
