# KARARLAR — sunum v4 TASLAK (15 Kasım 2026)

Bu bir taslaktır; aşağıdaki kararlar onaylanmadan hiçbir şey kesinleşmez. Yeniden üretim: `./derle.sh`.

## (a) Sahne listesi

| No | Soru | Eylem başlığı | Süre (sn) |
|---|---|---|---|
| 1 | — | IVF laboratuvarında yapay zekâ: beş soru | 15 |
| 2 | 1 | Yapay zekâ hattın her durağında; RKÇ yalnız embriyo seçiminde | 66 |
| 3 | 1 | Otuz yılda tahminden robota; kırılma 2018–2019’da geldi | 54 |
| 4 | 2 | YZ yazılımları 30’dan fazla ülkede, yüzlerce klinikte duyuruluyor | 60 |
| 5 | 2 | Hakemli veride ölçüm az: Japonya’da 345 tesisten 57’si YZ skoru kullanıyor | 60 |
| 6 | 3 | Canlı doğumda fark yok: en güçlü kanıt bunu söylüyor | 65 |
| 7 | 3 | Değişen bebek sayısı değil: süre, tutarlılık, ilaç | 55 |
| 8 | 3 | Neye etki ediyor? Kanıtla gösterilen tek kazanç hız | 60 |
| 9 | 4 | Görmede güçlü, kehanette orta: AUC çoğunlukla 0.6–0.7 | 75 |
| 10 | 4 | Aynı model, iki sayı: parlaklığı payda ve doğrulama belirliyor | 60 |
| 11 | 4 | Bir sayıya güvenmeden önce beş kontrol | 45 |
| 12 | 5 | Elle yapılan altı iş, kayıt girilirken kendiliğinden oluyor | 50 |
| 13 | 5 | İhtiyacı embriyolog söyledi, yapay zekâ kodladı, embriyolog doğruladı | 45 |
| 14 | 5 | Program 5 oranı her ay hesaplıyor; Vienna’yla eşleşmesi kısmi | 45 |
| 15 | 5 | CUSUM düşüşü aylık ortalamadan önce yakalıyor; yaş ayarı haksızlığı düzeltiyor | 55 |
| 16 | 5 | Ham değil, kişisel yapay zekâ; embriyolog onun kalite kontrolcüsü | 45 |
| 17 | — | Beş soru, beş kısa cevap | 15 |

**Toplam: 17 ana sahne, 870 sn (14 dk 30 sn).** Soru başına: 1 → 120, 2 → 120, 3 → 180, 4 → 180, 5 → 240; başlık 15, kapanış 15. Zamanlayıcı hedefi 15:00.

Yedekler (`data-sure="0"`): 18. Yöntem ve sınırlar; 19. Kaynakça 1; 20. Kaynakça 2; 21. Beklenen sorular; 22. Oran ölçeği; 23. Sızıntı; 24. Kalite kontrol izlemi.

## (b) Kullanıcıya sorulacak kararlar (her biri tek satır; → önerilen varsayılan, taslakta uygulanan)

### Ajanların [ONUR’A SOR] maddeleri (hiçbiri benim tarafımdan çözülmedi)
1. Zaman tasarrufu: kendi deneyiminizden bir süre örneği var mı (ör. Bakanlık tablosu, yıl sonu sayımı)? → Slaytta süre iddiası yok; notta “ayrıca ölçmedim” deniyor.
2. Program öncesi KPI nasıl, ne sıklıkla sayılıyordu? → “Yıl sonunda elle” ifadesi kullanılmadı; yalnız “oranlar her ay kendiliğinden”.
3. Blastokist oranının payı (morula/kavitasyon/arrest ve gün 4–7 kayıtları dahil) yalnız 5. gün gerçek blastokistle sınırlansın mı? → Slaytta “tanım birebir değil”; “Vienna KPI’sı hesaplanıyor” denmiyor; ayrıntı ekranda yok.
4. CUSUM/funnel/yaş ayarı için “programa eklemeyi planlıyorum” denebilir mi? → Denmiyor; “programda yok, programın tuttuğu türden veriyle yapılabilir”.
5. Funnel’da A–F’ye “embriyolog” mu, “operatör/vardiya” mı densin; kişi bazlı karşılaştırma gösterilsin mi? → Nötr: “A–F sentetik birimlerdir”.
6. v0.1–v5.8 (git öncesi 34 sürüm notu) ne zaman başladı, hangi araçla yazıldı? → Slayt yalnız git dönemini söylüyor: 32 gün, 341 commit.
7. Kapanış mesajı “Kendi verini kendin tut: kaydı olmayan KPI izlenemez” onaylanıyor mu? → Kullanılmadı; kapanış “beş soru, beş kısa cevap” (yalnız onaylı tezler).
8. Çıkar çatışması deseni (kart sayılarının çoğu üretici firma yazarlı) notu 1. soruda mı, sonra mı verilsin? → 4.1 künyesinde tek cümle; ayrı vurgu yok.
9. Binlik ayırıcı: dar boşluk (1 066) uygun mu? → Dar boşluk; ondalık nokta. Kalın başlık yazısında okunurluk için bölünmez normal boşluk.

### Derleyicinin tasarım kararları (onay gerekir)
10. Sunum başlığı: “IVF laboratuvarında yapay zekâ: beş soru” → bu; alternatif “Ham değil, kişisel yapay zekâ”.
11. Kurum adı ve çıkar çatışması beyanı: başlıkta “[Kurum]”, yöntem yedeğinde “[beyan]” yer tutucu → sizden bekleniyor.
12. Ayrı “soru” ara slaytı yok; soru her bölümün ilk sahnesinde büyük serif italik, sol omurgada 1–5 göstergesi → böyle kalsın (17 sahne).
13. Bölüm 4’ün son sahnesi “beş soru” yerine “beş kontrol” diye adlandırıldı (sunumun beş sorusuyla karışmasın) → böyle kalsın.
14. Bölüm 3 ana cümlesi “canlı doğumu artırmadı” yerine “daha çok bebek getirdiği gösterilmedi” (ajan düzeltmesi); 3.1 başlığı yine “Canlı doğumda fark yok” → başlık kalsın, altına kesinlik notu eklendi; isterseniz başlık da yumuşatılır.
15. Aşama hattında “Kanıt × olgunluk” matrisi düğmesi var; iki sütun (araştırma / ticari ürün), “rutin” sütunu yok → kalsın; 66 sn’ye sığmazsa düğme atlanır.
16. Program ekran görüntüsü kullanılmadı (elimde test veritabanı görüntüsü yok; resmî formda kurum adı var) → isterseniz test veritabanından cryo haritası ve istatistik ekranı eklenir.
17. Türkiye karesi: “2022’den beri bir merkez; sperm seçimi iki merkez” (ad yok; kaynak önceki oturumda görülen web sayfaları, bu oturumda yeniden doğrulanmadı) → kalsın mı, yalnız sözlü mü?
18. Ürün/firma adları (iDAScore, CHLOE, MAGENTA, Univfy…) yalnız aşama kartlarında ve künyede; yaygınlık sayaçlarında “bir embriyo seçimi yazılımı” → böyle kalsın.
19. Kongre adı “Klinik Embriyoloji Kongresi 2027” önceki sürümden alındı → doğrulayın.

## (c) Doğrulanamayan / çıkarılan içerik
- %24.8 → %53.2 benimseme anketi (ve %83.62, %38.01): asıl kaynak doğrulanamadı → slaytta yok.
- FDA 510(k) (Eylül 2025): yalnız ikincil kaynak (Chang 2026) → zaman çizgisinde içi boş nokta + “ikincil kaynak”. CE (Ekim 2025), CycleClarity, “3 700 km”, “~20 canlı doğum”, LOTUS: slaytta yok.
- Vitrolife “kliniklerin %75’i”: YZ’ye özgü değil → yok. Beyan sayıları toplanmadı.
- Kriyo: hakemli YZ kanıtı yok → “kanıt yok” işareti; kaynak bir sensör deneyi.
- Ploidi “0.7–0.8” yerine dış doğrulama ≈ 0.70 (cetvelde 0.61–0.74, meta-analiz 0.80 ayrı işaretli).
- CHLOE bülteni tarihi 29 Temmuz 2026 olarak düzeltildi; “16 Avrupa ülkesi” → “16 ülke”.
- ASRM 2026 önerileri, Kieslinger 2024 yorumu, EMBRYOLY simülasyonu, iş yükü/FTE hesabı, Univfy ROC-AUC, niPGT 0.91, Sfakianoudis 2022, Japonya %63.2 ve “altıda bir” (yalnız sözlü): slaytta yok.
- Vienna implantasyon eşikleri ve 12 KPI’nın tam listesi doğrulanamadı → yok. README test verisi örneği (20/32 vb.) yanıltıcı karşılaştırma doğurmasın diye konmadı.
- Bhide 2026’nın Illingworth 2024’ü içerip içermediği bilinmiyor → orman grafiğinde iki ayrı başlık.
- PDC’ye atfedilmeyenler: ML modeli, karar desteği, ölçülmüş zaman tasarrufu, CUSUM/funnel/ince ayar (hepsi “programda yok” ve SENTETİK etiketli).

## (d) Sanat yönü (tek cümle)
Aynı motor, yeni dil: solda beş sorunun koyu “omurgası” (etkin soru sarı), soru serif italik (Lora) ve cevap ağır grotesk başlık olarak soru–cevap çifti, kemik zemin + mürekkep + fosforlu-kalem sarısı vurgu + kırmızı kalem uyarı etiketleri; yuvarlak kart ızgarası yerine cetvel çizgili figürler (hat/matris, zaman çizgisi, ülke kareleri, orman, cetvel, funnel) ekranın çoğunu kaplıyor.

## Denetim (15 Kasım 2026)
- `sayi_denetle.py sunum.html analiz/tum_sayilar.json`: temiz (102 sayı adayı, hepsi kaynaklı).
- `disa_aktar.py`: taşma uyarısı yok; 24 PNG gözle kontrol edildi.
- `etkilesim_sina.py`: hat/matris, tür süzgeci, kronometre, “aynı model” düğmeleri, funnel geçişi, klavye gezinme, genel bakış, koyu tema: konsol hatası yok.
- Bilinen kusurlar: kalite kontrol yedeğindeki şekil eski matplotlib çizimi (yazıları küçük); funnel’da A–D etiketleri sıkışık.
