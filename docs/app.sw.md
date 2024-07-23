---
layout: app
ref: app
permalink: /sw/app
---
# Sudoku Kaidoku
Hii ni **programu ya Sudoku** inayowasilisha matatizo kwa nasibu kutoka kwa **aina mbalimbali za vichanganuzi** unapochagua **kiwango cha ugumu**. Kubonyeza kitufe cha dalili kunatoa dalili za jinsi ya kutatua kulingana na **mikakati mbalimbali ya utatuzi**, ambayo imeelezwa katika **kitabu cha mafunzo** kilichoambatanishwa.

{% capture markdown_content %}
- Pakua bila malipo bila matangazo. Katika **toleo la bure**, mara tu unapomaliza kiwango cha 4, unaweza kucheza kiwango cha 5, na baada ya kumaliza kiwango cha 5, unaweza kuendelea hadi kiwango cha 6. Kiwango cha 6 ni kigumu sana kwa watu wengi. Kwa watumiaji wanaotafuta changamoto, kwa kuboresha hadi **toleo la Pro**, ambalo linapatikana tu kwenye **toleo la iOS**, unaweza kucheza kila wakati hadi kiwango cha 9.
- Unaweza kutumia **alama za penseli** kuandika nambari kadhaa za wagombea kwenye seli, ambayo ni njia ya kawaida ya kutatua vichanganuzi vya Sudoku.
- Kuna zaidi ya mchanganyiko bilioni 78 wa vichanganuzi katika kila kiwango, na kuifanya kuwa **karibu kutokuwa na mwisho** kwa watatuzi wa kibinadamu.
- **Kitabu cha mafunzo** kinajumuisha jumla ya kurasa 65, ikiwa ni pamoja na takwimu za nafasi za Sudoku.

**Kutumia dalili**:
- Katika hali ya dalili, dalili hutolewa kila wakati kwa vidokezo vya mawazo. Ikiwa kuna nambari **zilizorudiwa** au nambari **tofauti** na jibu sahihi, dalili itakuonya. Ikiwa hakuna makosa kwenye ubao, dalili huonyeshwa kulingana na **mikakati mbalimbali ya Sudoku**.
- Katika hali ya dalili, nambari zote za wagombea hujazwa kiotomatiki kama alama za penseli inapohitajika.
- Mwanzoni, tatua vichanganuzi vya Sudoku kwa kurejelea dalili kujifunza vidokezo vya utatuzi. Kisha jaribu kutatua kibonyeo bila dalili. Unaweza kila wakati kurejelea dalili unapokwama.
- Unapotatua kibonyeo bila kurejelea dalili, ume**maliza** kibonyeo, na idadi ya malizo na muda bora zaidi wa kumaliza kila kiwango huandikwa kwenye programu yako.
- Ukijaribu kutatua kibonyeo, kurejelea dalili, na kupata makosa, unaweza kwa urahisi **kurudi nyuma** hadi hali ambapo kosa lilitokea. Dalili itaeleza jinsi kosa lilivyotokea. Kisha unaweza kuchanganua sababu na kuendelea kutatua kutoka hapo. Kwa kurudia mchakato huu, unaweza kila wakati kutatua kibonyeo kwa msaada wa dalili.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Soma zaidi</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Pakua
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="QR code" style="display: block; margin-top: 30px;">

## Toleo la wavuti
Toleo la [wavuti](../sudoku/) linapatikana pia. Katika toleo la programu, lugha inachaguliwa kulingana na upendeleo wa mfumo. Katika toleo la wavuti, lugha inaweza kuchaguliwa kutoka kwa chaguzi zifuatazo.

{% include mobile-lang.html %}

## Matoleo mengine
- [Vitabu vya PDF](../book)
- [Laini ya amri](../)
