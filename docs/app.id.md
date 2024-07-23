---
layout: app
ref: app
permalink: /id/app
---
# Sudoku Kaidoku
Ini adalah **aplikasi Sudoku** yang secara acak menampilkan masalah dari **berbagai macam teka-teki** saat Anda memilih **tingkat kesulitan**. Menekan tombol petunjuk memberikan petunjuk tentang cara menyelesaikannya berdasarkan berbagai **strategi penyelesaian**, yang dijelaskan dalam **buku tutorial** yang menyertainya.

{% capture markdown_content %}
- Unduh gratis tanpa iklan. Dalam **versi Gratis**, setelah Anda menyelesaikan level 4, Anda dapat memainkan level 5, dan setelah menyelesaikan level 5, Anda dapat melanjutkan ke level 6. Level 6 sangat sulit bagi kebanyakan orang. Bagi pengguna yang mencari tantangan, dengan meningkatkan ke **versi Pro**, yang hanya tersedia di **versi iOS**, Anda selalu dapat memainkan hingga level 9.
- Anda dapat menggunakan **tanda pensil** untuk mencatat beberapa angka kandidat dalam sebuah sel, yang merupakan cara standar untuk menyelesaikan teka-teki Sudoku.
- Ada lebih dari 78 miliar kombinasi teka-teki di setiap level, membuatnya **hampir tak terbatas** bagi pemecah manusia.
- **Buku tutorial** terdiri dari total 65 halaman, termasuk gambar posisi Sudoku.

**Menggunakan petunjuk**:
- Dalam mode petunjuk, selalu diberikan petunjuk untuk tips berpikir. Jika ada angka yang **duplikat** atau angka yang **berbeda** dari jawaban yang benar, petunjuk akan memberi tahu Anda. Jika tidak ada kesalahan pada papan, petunjuk ditampilkan berdasarkan berbagai **strategi Sudoku**.
- Dalam mode petunjuk, semua angka kandidat otomatis diisi sebagai tanda pensil saat diperlukan.
- Awalnya, selesaikan teka-teki Sudoku dengan merujuk pada petunjuk untuk mempelajari tips penyelesaian. Kemudian cobalah menyelesaikan teka-teki tanpa petunjuk. Anda selalu dapat merujuk pada petunjuk saat Anda mengalami kesulitan.
- Saat Anda menyelesaikan teka-teki tanpa merujuk pada petunjuk, Anda telah **menyelesaikan** teka-teki, dan jumlah penyelesaian dan waktu terbaik untuk menyelesaikan setiap level dicatat dalam aplikasi Anda.
- Jika Anda mencoba menyelesaikan teka-teki, merujuk pada petunjuk, dan menemukan kesalahan, Anda dapat dengan mudah **kembali** ke situasi di mana kesalahan dibuat. Petunjuk akan menjelaskan bagaimana kesalahan terjadi. Anda kemudian dapat menganalisis penyebabnya dan melanjutkan penyelesaian dari titik itu. Dengan mengulangi proses ini, Anda selalu dapat menyelesaikan teka-teki dengan bantuan petunjuk.
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
<p><a href="#readmore1" onclick="return showMore(this);">&gt;&gt;&gt; <strong>Baca lebih lanjut</strong></a></p>
<div id="readmore1" style="display: none";>
{:/nomarkdown}
{{ markdown_content | markdownify }}
{::nomarkdown}</div>{:/nomarkdown}

## Unduh
{% include mobile.html %}
<img src="{{'/img/qr.png' | relative_url}}" alt="Kode QR" style="display: block; margin-top: 30px;">

## Versi web
Sebuah [versi web](../sudoku/) juga tersedia. Dalam versi aplikasi, bahasa dipilih berdasarkan preferensi sistem. Dalam versi web, bahasa dapat dipilih dari opsi berikut.

{% include mobile-lang.html %}

## Versi lainnya
- [Buku PDF](../book)
- [Baris perintah](../)
