# Görsel yön, teknik üretim ve kalite kontrol

Başlamadan `/mnt/skills/public/frontend-design/SKILL.md` dosyasını oku; estetik karar
vermede ve "şablon görünümünden" kaçınmada oradaki ilkeler geçerlidir. Bu dosya o ilkelerin
**akademik kongre sunumu** için somutlaştırılmasıdır.

## Sanat yönü (varsayılan: "laboratuvar defteri × dergi figürü")

- **Zemin:** sıcak kâğıt (#FBFAF6), koyu mürekkep metin (#14213D). Tek vurgu rengi (#E4572E),
  ikincil mavi (#2A6F97). Renk körü dostu çift (lacivert/turuncu). Koyu tema `D` tuşuyla.
- **Yazı tipi:** Inter / Inter Display (Türkçe karakterleri tam destekler), kod için mono.
  Derlemede alt küme olarak gömülür; salon bilgisayarında font aramaz.
- **Figür baskın:** her sonuç sahnesinde şekil ekranın en az %55'ini kaplar. Dergi figürü
  disiplini: eksen etiketi, birim, GA, künye. Süs yok.
- **Hareket anlam taşır:** geçiş düğmesi (naif ↔ doğru), adım adım beliren öğe, slider.
  Dekoratif animasyon yok. Her hareketin sorusu: "Bu, dinleyicinin neyi anlamasına yardım ediyor?"
- **Yoğunluk:** slayt başına ≤ 40 sözcük; gövde ≥ 30 px (1920 tabanda); arka sıradaki
  izleyici okuyabilmeli. Kontrast ≥ 4.5:1.

## Klişe testi (her sahne için)

Başlığı silip yerine başka bir yapay zekâ konuşmasının başlığını koy. Slayt hâlâ "doğru"
görünüyorsa şablondur; konuya özgü hale getir. Kaçınılacaklar: beyin/robot/devre ikonları,
mavi-mor degradeler, "AI" yazılı parlayan küreler, stok embriyo/ hücre fotoğrafı, madde
işaretli sözcük yığını, her sahnede aynı kart ızgarası. Bunun yerine: gerçek (test verili)
program ekranı, depo parçası, kod 2 satırı, dergi figürü, zaman çizgisi, tıklanabilir iş akışı hattı.

## Türkçe tipografi denetimi

- `<html lang="tr">` zorunlu: `text-transform:uppercase` ile i→İ, ı→I doğru olur.
- Tırnak: “ ” ve kesme işareti ’ (düz ' değil) kullan. Eksi işareti: −. Ondalık ayırıcı:
  Türkçe metinde virgül (0,65) **veya** tüm sunum boyunca nokta; ikisini karıştırma. Şekiller
  nokta kullanıyorsa metin de nokta kullansın, ya da şekilleri `locale` ile virgüle çevir.
  Kararı kullanıcıya bırak (Türkçe metinde virgül gelenekseldir; şekiller matplotlib ile nokta üretir). Önerin: tutarlılık için tek biçim seç ve tüm şekilleri ona göre üret.
- Ek ve bitişik yazım: "AUC'si", "GEE'nin", "ICSI'den" (kesme işareti kısaltmalarda).
- Klinik terimler İngilizce kalır (blastocyst, ICSI, PN, ICM, TE, FET, PGT); program
  arayüzüyle birebir tutarlı yaz.
- Kod bloğunda Türkçe karakter yoksa yazı tipi sorunu çıkmaz; yine de gömülü mono kullan.

## Üretim akışı

1. `scripts/sentetik_veri.py` → `sentetik_kohort.csv` (+ `_meta.json`).
2. `scripts/analiz_demo.py --veri ... --cikti-dir sonuc/` (makale/yedek) **ve**
   `--cikti-dir sonuc_slayt/ --slayt` (büyük yazılı, şekil içi başlıksız slayt şekilleri).
3. `assets/deck_iskelet.html` dosyasını `sunum.html` olarak kopyala; örnek slaytları kendi
   sahnelerinle değiştir. Şekilleri `<img class="sekil" src="sonuc_slayt/fig_....svg">` ile ekle
   (SVG tercih: büyütmede keskin).
4. `scripts/sayi_denetle.py sunum.html sonuc_slayt/sonuclar.json` → slayttaki sayılar kaynakla örtüşüyor mu?
5. `scripts/sunum_derle.py sunum.html sunum_salon.html` → fontlar + görseller gömülü tek dosya.
6. `scripts/disa_aktar.py sunum_salon.html --cikti-dir cikti/` → PDF, görsel yedek PPTX, PNG'ler
   ve taşma uyarıları.
7. **Her PNG'yi `view` ile gözle kontrol et.** Kontrol: taşma, kesilen metin, okunmayan şekil,
   eksik Türkçe karakter, "SENTETİK VERİ" etiketi, künye satırı, ekran görüntülerinde kimlik bilgisi.

## Çıktı paketi (kullanıcıya verilecekler)

- `sunum_salon.html` — ana sunum (çevrimdışı, tek dosya; Chrome/Edge'de aç, `F` tam ekran).
- `sunum.pdf` — yedek 1 (vektör, tüm adımlar açık).
- `sunum_yedek.pptx` — yedek 2 (görsel birebir, notlu; metin düzenlenemez, bunu açıkça söyle).
- `sunucu_notlari.md` — konuşma metni + süre; `soru_cevap.md`.
- `analiz/` — betikler, sentetik veri, `sonuclar.json` (tekrarlanabilirlik).
- Düzenlenebilir bir PowerPoint isterse: `/mnt/skills/public/pptx/SKILL.md` ile yerel nesnelerden
  ayrıca üret (aynı şekiller, aynı sayılar); etkileşimler PPTX'te yoktur, bunu belirt.

## Salon riskleri (kullanıcıya kısa bir kontrol listesi olarak ver)

- Sunumu **USB'de + e-postada + telefonda** taşı. Kongre bilgisayarında HTML açılmazsa PDF.
- Salon bilgisayarında tarayıcı: Chrome/Edge güncel mi? Önceden dene. Çözünürlük/oran 4:3 ise
  sahne ortalanır (siyah bantlar), içerik kırpılmaz.
- Sunucu görünümü (`P`) ikinci ekranda açılır; tek ekranda kullanma, notları yazdır.
- Ses/video yok; canlı demo gerekmez. Etkileşimler internetsiz çalışır.
- Zamanlayıcı (`T`) sunucu penceresinde; salon ekranında görünmez.

## Yayınlanan artifact hakkında

Kongre çıktısı çevrimdışı dosyadır. İstenirse hızlı önizleme/paylaşım için sayfa
yayınlanabilir; ama yayınlanmış sayfada dış kaynak ve depolama kısıtları vardır ve hasta
verisi/ekran görüntüsü içeren hiçbir sayfa yayınlanmaz. Varsayılan: `present_files`.

## Sahada öğrenilen tuzaklar (kontrol et)

- **Şablon yorumunda etiket adı yazma:** derleyici ilk `main#sahne` / `script` metnini arar; yorumda
  `<main ...>` yazılırsa tüm CSS silinir. Yorumlarda etiket adlarını açık yazma.
- **Binlik ayırıcı:** ondalık nokta kullanılıyorsa binlik için bölünmeyen dar boşluk (U+202F) kullan
  (`4 428`); düz boşluk satır sonunda sayıyı böler. `sunum_derle.py` bu karakteri fonta dahil eder.
- **Şekil boyutu:** `img.sekil{width:100%}`; yoksa SVG küçük kalır ve yazılar okunmaz. Kare şekiller için `max-height:600px;width:auto`.
- **Sahne taşması:** başlık + 6 satır + altbilgi sığmaz; satır dolgusunu azalt ya da sahneyi böl. `disa_aktar.py` uyarısı ve PNG kontrolü şart.
- **Slider/sayı tutarlılığı:** slider varsayılanı yuvarlanmış değil tam değer olmalı (`step="any"`), yoksa ekran 1.50, kaynak 1.49 der.
- **Her denetimde sayılar:** `sayi_denetle.py` kaynaksız sabitleri yakalar (ör. zamansal bölme eşiği); sabiti `sonuclar.json`'a yaz.
