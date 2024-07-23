---
layout: app
ref: app
permalink: /tr/app
---
# Sudoku Kaidoku
Bu, **zorluk seviyesini** seçtiğinizde **çeşitli bulmacalar** arasından rastgele sorunlar sunan bir **Sudoku uygulaması**. İpucu düğmesine basmak, çeşitli **çözme stratejilerine** dayalı olarak çözme konusunda ipuçları sağlar ve bunlar, beraberindeki **öğretici kitapta** açıklanmıştır.

{% capture markdown_content %}
- Reklam olmadan ücretsiz indirin. **Ücretsiz sürümde**, seviye 4'ü tamamladıktan sonra, seviye 5'i oynayabilir ve seviye 5'i tamamladıktan sonra seviye 6'ya geçebilirsiniz. Seviye 6, çoğu insan için çok zordur. Zorlu kullanıcılar için yalnızca **iOS sürümünde** mevcut olan **Pro sürümüne** yükselterek, her zaman seviye 9'a kadar oynayabilirsiniz.
- Bir hücrede birden fazla aday numarayı not etmek için **kalem işaretlerini** kullanabilirsiniz; bu, Sudoku bulmacalarını çözmenin standart bir yoludur.
- Her seviyede 78 milyardan fazla bulmaca kombinasyonu vardır, bu da insan çözücüler için **neredeyse sonsuz** hale getirir.
- **Öğretici kitap**, Sudoku pozisyonlarının figürlerini içeren toplam 65 sayfadan oluşmaktadır.

**İpuçlarını kullanma**:
- İpucu modunda, düşünme ipuçları için her zaman bir ipucu verilir. **Yinelenen** sayılar veya doğru cevaptan **farklı** sayılar varsa, ipucu sizi uyaracaktır. Tahtada hata yoksa, çeşitli **Sudoku stratejilerine** dayalı olarak bir ipucu gösterilir.
- İpucu modunda, gerekli olduğunda tüm aday sayılar otomatik olarak kalem işareti olarak doldurulur.
- Başlangıçta, çözüm ipuçlarını öğrenmek için ipuçlarına başvurarak Sudoku bulmacalarını çözün. Daha sonra ipucu olmadan bulmacayı çözmeye çalışın. Sıkıştığınızda her zaman bir ipucuna başvurabilirsiniz.
- Bir ipucuna başvurmadan bir bulmacayı çözdüğünüzde, bulmacayı **temizlemiş** olursunuz ve her seviyeyi temizleme sayısı ve en iyi süre uygulamanızda kaydedilir.
- Bir bulmacayı çözmeye çalışır, bir ipucuna başvurur ve hatalar bulursanız, hatanın yapıldığı duruma kolayca **geri dönebilirsiniz**. İpucu, hatanın nasıl meydana geldiğini açıklayacaktır. Ardından nedeni analiz edebilir ve o noktadan çözmeye devam edebilirsiniz. Bu süreci tekrarlayarak, ipuçlarının yardımıyla her zaman bir bulmacayı çözebilirsiniz.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Daha fazla oku</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## İndir
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="QR kodu" style="display: block; margin-top: 30px;">

## Web sürümü
Bir [web sürümü](../sudoku/) de mevcuttur. Uygulama sürümünde, dil sistem tercihine göre seçilir. Web sürümünde, dil aşağıdaki seçeneklerden seçilebilir.

{% include mobile-lang.html %}

## Diğer sürümler
- [PDF kitapları](../book)
- [Komut satırı](../)
