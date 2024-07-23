---
layout: app
ref: app
permalink: /pt/app
---
# Sudoku Kaidoku
É um **aplicativo de Sudoku** que apresenta aleatoriamente problemas de uma **ampla gama de quebra-cabeças** quando você seleciona um **nível de dificuldade**. Pressionar o botão de dica fornece dicas sobre como resolvê-lo com base em várias **estratégias de resolução**, que são explicadas no **livro tutorial** que o acompanha.

{% capture markdown_content %}
- Download gratuito sem anúncios. Na **versão gratuita**, uma vez que você complete o nível 4, você pode jogar o nível 5, e depois de completar o nível 5, você pode prosseguir para o nível 6. O nível 6 é muito difícil para a maioria das pessoas. Para os usuários que buscam desafios, ao atualizar para a **versão Pro**, que está disponível apenas na **versão iOS**, você sempre pode jogar até o nível 9.
- Você pode usar **marcas de lápis** para anotar vários números candidatos em uma célula, que é uma maneira padrão de resolver quebra-cabeças de Sudoku.
- Existem mais de 78 bilhões de combinações de quebra-cabeças em cada nível, tornando-o **praticamente interminável** para solucionadores humanos.
- O **livro tutorial** é composto por um total de 65 páginas, incluindo figuras das posições do Sudoku.

**Usando dicas**:
- No modo de dicas, uma dica é sempre fornecida para sugestões de pensamento. Se houver números **duplicados** ou números **diferentes** da resposta correta, a dica alertará você. Se não houver erros no tabuleiro, uma dica é mostrada com base em várias **estratégias de Sudoku**.
- No modo de dicas, todos os números candidatos são preenchidos automaticamente como marcas de lápis quando necessário.
- Inicialmente, resolva os quebra-cabeças de Sudoku referindo-se às dicas para aprender sugestões de resolução. Em seguida, tente resolver o quebra-cabeça sem dicas. Você sempre pode se referir a uma dica quando estiver preso.
- Quando você resolve um quebra-cabeça sem se referir a uma dica, você **completou** o quebra-cabeça, e o número de vezes que você completou e o melhor tempo para completar cada nível são registrados no seu aplicativo.
- Se você tentar resolver um quebra-cabeça, referir-se a uma dica e encontrar erros, você pode facilmente **voltar** à situação onde o erro foi cometido. A dica explicará como o erro ocorreu. Você pode então analisar a causa e retomar a resolução a partir desse ponto. Repetindo esse processo, você sempre pode resolver um quebra-cabeça com a ajuda das dicas.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Leia mais</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Download
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="Código QR" style="display: block; margin-top: 30px;">

## Versão web
Uma [versão web](../sudoku/) também está disponível. Na versão do aplicativo, o idioma é selecionado com base na preferência do sistema. Na versão web, o idioma pode ser selecionado entre as seguintes opções.

{% include mobile-lang.html %}

## Outras versões
- [Livros PDF](../book)
- [Linha de comando](../)
