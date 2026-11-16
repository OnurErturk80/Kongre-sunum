# Bölüm 4: Yapay zekâ ne kadar doğru sonuç veriyor?

Süre hedefi: 180 sn (3 sahne: 75 + 60 + 45). Konuşma hızı ≈ 2.3 sözcük/sn.

## Tek cümlelik cevap

Yapay zekâ, embriyoloğun gördüğünü ölçmede ve sınıflamada güçlü (folikül F1 %93), ama geleceği tahmin etmede orta düzeyde: transfer edilen embriyolar arasında implantasyon/FHB AUC'si çoğunlukla 0.60–0.76, görüntüden ploidi tahmini dış merkezlerde ≈ 0.70 (meta-analizde 0.80), oositten öploidi tek başına 0.54. 0.90'ın üstündeki parlak sayılar çoğunlukla paydadan (atılan embriyolar da sayılınca), retrospektif seçimden, küçük ve tek merkezli örneklemden ya da görev türünden (insan etiketini taklit etmek, sonucu tahmin etmek değildir) geliyor.

**Ana mesaj taslağına düzeltme:** “Transfer edilen embriyolar arasında AUC 0.6–0.7” kanıtla uyumlu (Berntsen 0.67, merkezler 0.60–0.75; Ueno 0.66–0.76; Mina meta-analizi 0.7; Thirumalaraju ≈ 0.60). “Ploidi ~0.7–0.8” biraz iyimser: dış doğrulamada 0.70–0.72 (STORK-A), çok merkezli karşılaştırmada en iyisi 0.71 (Bamford), ticari skorla 0.60–0.68 (iDAScore). 0.80 yalnız havuzlanmış meta-analiz değeri ve yazarlar dış doğrulamayı heterojenliğin kaynaklarından biri olarak gösteriyor. Önerilen cümle: **“Transfer edilen embriyolar arasında AUC 0.6–0.7; ploidi tahmini başka merkezde ≈ 0.7. 0.9'un üstündeki sayılar çoğu zaman paydadan, retrospektif seçimden ya da küçük tek merkezli veriden geliyor.”**

**AUC'nin embriyolog diliyle tanımı (Kragh 2021 tam metindeki tanıma dayanıyor):**
“AUC 0.67 şu demek: transfer edilmiş embriyolardan rastgele bir tutan (FHB+) ve bir tutmayan seçersek, model tutana %67 olasılıkla daha yüksek puan verir. 0.5 yazı-tura, 1.0 kusursuz.”
Gerekli dipnot: AUC, farklı hastalardan ve merkezlerden gelen bütün havuz üzerinden hesaplanır. Aynı hastanın kardeş embriyoları arasındaki sıralama başarısını doğrudan göstermez (Kragh 2021, tam metin). Yüksek AUC yüksek implantasyon oranı anlamına da gelmez (Berntsen 2022, tam metin).

---

## Sahneler

### Sahne 1: Görmede güçlü, kehanette orta

- **Eylem başlığı:** Görmede güçlü, kehanette orta: tahmin AUC'si çoğunlukla 0.6–0.7
- **Ekranda (aynen):**
  Üst şerit: **Göz işi** (uzman etiketine uyum) · Folikül ≥ 10 mm F1 0.93 · Sperm morfolojisi: çoğu çalışma > %90 doğruluk
  Alt şerit: **Kehanet işi** (sonuca göre AUC) · 0.5 yazı-tura ··· 1.0 kusursuz
  Alt yazı: “AUC 0.67 = rastgele bir tutan ve bir tutmayan embriyodan tutanı %67 olasılıkla üste koyar.”
- **Görsel / etkileşim önerisi:**
  İki ayrı yatay şerit. Aynı ölçeğe konmaz, çünkü F1/doğruluk ile AUC farklı ölçülerdir ve şeritler bilerek ayrık çizilir.
  - **Üst şerit (göz işi, 0–1, kare işaret):** folikül F1 0.933 (GA 0.907–0.951); tüm foliküllerde duyarlılık 0.689 (küçük foliküller kaçıyor); embriyo morfoloji derecesinde YZ medyan doğruluğu 0.755 (aralık 0.59–0.94); sperm morfolojisi için tek bir nokta yerine “> 0.90 (çoğu çalışma, küçük ve tek merkezli)” yazan soluk bant.
  - **Alt şerit (kehanet işi, AUC 0.5–1.0, yuvarlak işaret, yatay çizgi = aralık):** 0.5'te “yazı-tura” çizgisi. Satırlar görev başına:
    1. Embriyo → FHB/implantasyon (transfer edilenler): Berntsen 0.67, çizgi 0.60–0.75 (merkez dışarıda bırakma testi); Ueno 0.66–0.76 (yaş grupları); Mina meta-analizi 0.70; Thirumalaraju ≈ 0.60.
    2. Görüntüden ploidi: STORK-A iç test 0.737, dış 0.702 / 0.715 (içi boş daire = dış doğrulama); Bamford LR 0.71 (derin öğrenme 0.63); iDAScore + klinik 0.688 (tek başına 0.612); Xin meta-analizi 0.80 (soluk elmas, “havuzlanmış, çoğu iç doğrulama”).
    3. Oosit → öploidi (MAGENTA): tek başına 0.542, blastokist morfolojisi eklenince 0.607, tam model 0.666; donör oositte blastokist gelişimi 0.60 (prospektif, kör).
    4. Tedavi öncesi canlı doğum: İngiltere/ABD modelleri Çin verisinde 0.67–0.69 (dış), merkeze özgü model 0.71; güncellenmiş İngiltere modeli 0.67 (tedavi öncesi) / 0.75 (tedavi sonrası).
  - Her noktaya dokununca künye ve tasarım (retrospektif/prospektif, iç/dış) açılır. Renk tek başına anlam taşımaz: tasarım işaret şekliyle kodlanır (dolu daire iç, içi boş daire dış, elmas meta-analiz).
  - niPGT-A referans çizgisi isteğe bağlı: sağda gri ve kesik bir “niPGT (DNA analizi, YZ değil) AUC 0.91” işareti; etiketi “karşılaştırma için, YZ değil”. Kalabalık olursa yalnız soru-cevapta kullanılır.
- **Sayılar:** `follis_f1_10mm`, `follis_ga`, `follis_recall_tum`, `salih_yz_morfoloji`, `sperm_sr_calisma`, `sperm_sr_morf_oran`, `berntsen_kid`, `berntsen_klinik_alt`, `berntsen_klinik_ust`, `ueno_auc_min`, `ueno_auc_max`, `mina_auc`, `thirumalaraju_auc`, `barnes_test`, `barnes_dis1`, `barnes_dis2`, `bamford_lr`, `bamford_derin`, `ma_idascore_tek`, `ma_idascore_klinik`, `xin_auc`, `magenta_tek`, `magenta_robust`, `magenta_tam`, `magenta_donor_blast`, `cai_dis_min`, `cai_dis_max`, `cai_merkez`, `ratna_on`, `ratna_sonra`, (isteğe bağlı) `huang_nipgt_auc`.
- **Sunucu notu (≈ 170 sözcük):**
  “Doğruluk sorusuna tek bir sayıyla cevap veremiyoruz, çünkü yapay zekâ labda iki ayrı iş yapıyor. Birincisi göz işi: bizim gördüğümüzü ölçmek, saymak, sınıflamak. Folikül ölçümünde on milimetrenin üstündeki foliküllerde F1 skoru yüzde doksan üç. Sperm morfolojisinde çalışmaların çoğu yüzde doksanın üstünde doğruluk bildiriyor. Burada referans, uzmanın kendi etiketi. İkinci iş kehanet: bu embriyo tutacak mı, öploid mi, bu hasta bebek sahibi olacak mı? Burada referans biyolojinin kendisi ve sayılar belirgin biçimde düşüyor. Cetveli şöyle okuyun: 0.5 yazı-tura, 1 kusursuz. AUC 0.67 şu demek: transfer edilmiş embriyolardan rastgele bir tutan ve bir tutmayan seçersek, model tutana yüzde altmış yedi olasılıkla daha yüksek puan veriyor. Transfer edilen embriyolarda kalp atımı tahmini 0.60 ile 0.76 arasında. Ploidi tahmini başka merkezlerde 0.70 civarında. Meta-analiz 0.80 diyor, ama çalışmaların çoğu kendi verisinde test edilmiş. Oositten öploidi tahmini tek başına 0.54, yani yazı-turaya çok yakın. Tedavi öncesi canlı doğum tahmini de, klasik modelle de yapay zekâyla da 0.67 ile 0.71 arasında kalıyor.”
- **Süre (sn):** 75
- **Künye satırı:** Wygocki 2026 JARG (PMID 41485151) · Varzaneh 2026 Int J Med Inform (PMID 43002852) · Salih 2023 HRO (PMID 37588797) · Berntsen 2022 PLoS One (PMID 35108306) · Ueno 2021 F&S (PMID 34246469) · Mina 2025 Contracept Reprod Med (PMID 41016945) · Thirumalaraju 2025 F&S (PMID 40876725) · Barnes 2023 Lancet Digit Health (PMID 36543475) · Bamford 2023 Hum Reprod (PMID 36825452) · Ma 2024 RB&E (PMID 38778410) · Xin 2024 eClinicalMedicine (PMID 39513188) · Setti 2026 F&S Sci (PMID 41825691) · Cimadomo 2025 Hum Reprod (PMID 40759152) · Cai 2024 Hum Reprod (PMID 37995380) · Ratna 2023 Hum Reprod (PMID 37632223)

---

### Sahne 2: Aynı model, iki sayı: parlaklığı payda belirliyor

- **Eylem başlığı:** Aynı model, iki sayı: parlaklığı payda ve doğrulama belirliyor
- **Ekranda (aynen):**
  Büyük sayı: **0.95** → düğmelerle sönüyor
  Düğmeler: [Yalnız transfer edilenler] 0.67 · [Yeni merkez] 0.60–0.75 · [Embriyoyu kim seçti?] 0.74 / 0.59 · [Hastayı ayır (sentetik)] 0.686 → 0.646
- **Görsel / etkileşim önerisi:**
  - Solda nokta bulutu, iDAScore test setinin oranlarıyla: 17.249 embriyo (her nokta = 100 embriyo, ≈ 172 nokta). Gri noktalar atılmış/durmuş embriyolar, renkli noktalar 2.212 transfer edilmiş KID embriyo. Sağda büyük AUC sayısı.
  - **Düğme 1 “Yalnız transfer edilenler”:** gri noktalar söner ve sayı 0.95'ten 0.67'ye iner. Alt yazı: “Durmuş embriyoyu ayırmak kolay; zor olan iyi blastokistler arasında seçmek.”
  - **Düğme 2 “Yeni merkez”:** sayı, merkez dışarıda bırakma testindeki 12 merkezin AUC'lerini gösteren bir şeride dönüşür (0.60, 0.63, 0.65, 0.65, 0.65, 0.66, 0.66, 0.67, 0.68, 0.68, 0.72, 0.75).
  - **Düğme 3 “Embriyoyu kim seçti?”:** Kragh simülasyonu. Bütün havuzda eşit iki model (ikisi de AUC 0.76). Model 1'in seçtiği embriyolar arasında değerlendirilince Model 1 0.59'a, Model 2 0.74'e iner. Alt yazı: “Retrospektif veride embriyoloğun skoru, kendi seçtiği embriyolar arasında haksız biçimde kötü görünür.”
  - **Düğme 4 “Hastayı ayır (SENTETİK)”:** sentetik demo. Gradyan artırma rastgele bölmede 0.686, hasta-gruplu bölmede 0.646 (GA 0.629–0.660); lojistik regresyon 0.706 → 0.704 (neredeyse değişmiyor). Kutuda büyük “SENTETİK VERİ” etiketi bulunur.
- **Sayılar:** `berntsen_tum`, `berntsen_kid`, `berntsen_test_embriyo`, `berntsen_test_kid`, `berntsen_klinik_listesi`, `kragh_sim_genel`, `kragh_sim_model1`, `kragh_sim_model2`, `demo_gbm_rastgele`, `demo_gbm_hasta`, `demo_gbm_hasta_ga`, `demo_lr_rastgele`, `demo_lr_hasta`
- **Sunucu notu (≈ 140 sözcük):**
  “Peki 0.95 gibi parlak sayılar nereden geliyor? Aynı model, aynı makale: iDAScore, on sekiz merkez, yüz on beş bin embriyo. Bütün embriyolar arasında AUC 0.95. Ama bu havuzda durmuş ve atılmış embriyolar da var; onları ayırmak bizim için de kolay. Bizim asıl sorumuz, transfere aday iyi blastokistler arasında hangisinin tutacağı. Orada AUC 0.67. Merkez değişince bu sayı 0.60 ile 0.75 arasında oynuyor. Retrospektif veride bir tuzak daha var: transfer edilecek embriyoyu biz seçtiğimiz için, embriyoloğun skoru kendi seçtiği embriyolar arasında haksız biçimde kötü görünüyor. Bir simülasyonda eşit güçteki iki model 0.59'a karşı 0.74 çıkıyor. Son düğme kendi sentetik verimden: aynı hastanın embriyoları hem eğitimde hem testte olunca AUC 0.686; hastayı ayırınca 0.646. Kısacası parlaklık çoğu zaman paydada, seçimde ve doğrulama biçiminde.”
- **Süre (sn):** 60
- **Künye satırı:** Berntsen 2022 PLoS One (PMID 35108306; tam metin; yazarlar Vitrolife) · Kragh & Karstoft 2021 JARG (PMID 34173914; tam metin, simülasyon) · Sentetik demo: kendi analizim, gerçek hasta verisi değildir

---

### Sahne 3: Bir sayıya güvenmeden önce beş soru

- **Eylem başlığı:** Bir sayıya güvenmeden önce beş soru
- **Ekranda (aynen):**
  1. Başka merkezde test edildi mi?
  2. Prospektif mi, randomize mi?
  3. Kalibre mi? (%40 dediği gerçekten %40 mı?)
  4. Benim labımda doğrulandı mı?
  5. Zamanla izleniyor mu?
- **Görsel / etkileşim önerisi:** Beş satırlık kontrol listesi. Her satırın sağında tek bir kanıt kartı “durum ışığı” gibi açılır (renk + ikon + metin; renk tek başına anlam taşımaz):
  1. Dış doğrulama → “Oosit sayısı tahmin eden 9 ML modelinin hiçbiri dış doğrulanmamış” (Wilkinson 2025) · “Ploidi meta-analizinde dış doğrulama, heterojenliğin kaynaklarından biri” (Xin 2024).
  2. Prospektif/RKÇ → “Zaman atlamalı CNN derlemesi: 22/22 çalışma retrospektif, 10'unda yüksek yanlılık riski” (Berman 2023) · “YZ-embriyolog karşılaştırması: hiçbiri prospektif değil” (Salih 2023). Bölüm 3'e köprü: tek büyük RKÇ'de (Illingworth 2024) eşdeğerlik gösterilemedi.
  3. Kalibrasyon → “MAGENTA tek başına: kalibrasyon eğimi 0.259 (ideal 1); tam modelde 0.645” (Setti 2026) · “İngiltere modelleri Çin verisinde canlı doğumu düşük tahmin etti” (Cai 2024).
  4. Yerel doğrulama → “Aynı model, 12 merkezde 0.60–0.75” (Berntsen 2022).
  5. Sürekli izleme → “Aynı mimariyle 50 kopya model: sıralama uyumu Kendall W ≈ 0.35; kritik hata ≈ %15; başka merkezde hata varyansı %46.07 arttı” (Thirumalaraju 2025).
  - Alt bant (tek satır): “Basit model ≥ derin öğrenme: ploidi tahmininde lojistik regresyon 0.71, derin öğrenme 0.63” (Bamford 2023).
- **Sayılar:** `wilkinson_model`, `wilkinson_dis`, `berman_calisma`, `berman_yuksek_risk`, `magenta_egim_tek`, `magenta_egim_tam`, `berntsen_klinik_alt`, `berntsen_klinik_ust`, `thirumalaraju_kopya`, `thirumalaraju_w`, `thirumalaraju_kritik`, `thirumalaraju_varyans_delta`, `bamford_lr`, `bamford_derin`
- **Sunucu notu (≈ 105 sözcük):**
  “O yüzden bir firma ya da makale bana bir sayı gösterdiğinde beş soru soruyorum. Bir: başka merkezde test edildi mi? Oosit sayısını tahmin eden dokuz modelin hiçbiri dış doğrulanmamış. İki: prospektif mi, randomize mi? Zaman atlamalı derin öğrenme derlemesindeki yirmi iki çalışmanın hepsi retrospektif. Üç: kalibre mi, yani yüzde kırk dediğinde gerçekten yüzde kırk mı? MAGENTA tek başına kullanıldığında kalibrasyon eğimi 0.26; ideal değer 1. Dört: benim labımda doğrulandı mı? Beş: zamanla izleniyor mu? Aynı mimariyle eğitilen elli kopya model embriyoları farklı sıralıyor ve başka merkezde bu kararsızlık artıyor. Bir de not: basit lojistik regresyon, derin öğrenmeyi geçebiliyor.”
- **Süre (sn):** 45
- **Künye satırı:** Wilkinson 2025 RBMO (PMID 41780078) · Xin 2024 (PMID 39513188) · Berman 2023 AJOG (PMID 37116822) · Salih 2023 (PMID 37588797) · Setti 2026 F&S Sci (PMID 41825691) · Cai 2024 Hum Reprod (PMID 37995380) · Berntsen 2022 (PMID 35108306) · Thirumalaraju 2025 F&S (PMID 40876725) · Bamford 2023 Hum Reprod (PMID 36825452)

Toplam: 75 + 60 + 45 = 180 sn.

---

## Görev × doğruluk cetveli (tam tablo, sahne 1'in verisi)

| Görev | Temsilî değer | Ölçü | Tasarım | Kaynak (okuma) |
|---|---|---|---|---|
| Embriyo canlılığı (FHB), transfer edilen KID embriyolar | 0.67 (GA 0.64–0.69) | AUC | Retrospektif, 18 merkez, embriyo düzeyinde rastgele bölünmüş test | Berntsen 2022 (tam metin) |
| Aynı model, tüm embriyolar (atılanlar FH− sayılmış) | 0.95 (GA 0.95–0.96) | AUC | Aynı test seti, 17.249 embriyo | Berntsen 2022 (tam metin) |
| Aynı model, yeni merkez (12 merkez dışarıda bırakma) | 0.60–0.75 | AUC | Merkez dışarıda bırakma çapraz doğrulaması | Berntsen 2022 (tam metin) |
| FHB, tek dondurulmuş blastokist transferi, yaş gruplarına göre | iDAScore 0.66–0.76; Gardner 0.63–0.75 | AUC | Retrospektif, tek merkez, 3.018 siklus | Ueno 2021 (özet) |
| Embriyo YZ → implantasyon (meta-analiz) | Duyarlılık 0.69, özgüllük 0.62, AUC 0.7 | SROC | Sistematik derleme + tanısal meta-analiz | Mina 2025 (özet) |
| 50 kopya CNN, canlı doğum | AUC ≈ 0.60; Kendall W ≈ 0.35; kritik hata ≈ %15 | AUC / uyum | Retrospektif, 2 merkez | Thirumalaraju 2025 (özet) |
| Euploid embriyoyu ilk sıraya koyma (kohort içi) | YZ v2 %68, YZ v1 %62, morfodinamik %64, Gardner %58, rastgele %44 | Kohort içi doğru sıralama | Retrospektif, tek merkez, 279 siklus | Cimadomo 2026 (özet) |
| Görüntüden ploidi (STORK-A) | Test 0.737; dış 0.702 / 0.715 | AUC | Retrospektif, 10.378 embriyo, 2 dış set | Barnes 2023 (özet) |
| Ploidi, 12 model karşılaştırması | LR 0.71 (0.67–0.73); RF 0.68; XGB 0.63; DL 0.63; yalnız derece 0.52 | AUC | 9 klinik, iç-dış çapraz doğrulama + dış doğrulama | Bamford 2023 (özet) |
| Ploidi, iDAScore | Tek başına 0.612; klinik + embriyo özellikleri eklenince 0.688 | AUC | Retrospektif, 3.448 blastokist | Ma 2024 (özet) |
| Ploidi, iDAScore derlemesi | 0.60–0.68 | AUC aralığı | Anlatı derlemesi, 6 retrospektif çalışma | Selntigia 2025 (özet) |
| Ploidi (meta-analiz) | Duyarlılık 0.71, özgüllük 0.75, AUC 0.80 | SROC | 12 çalışma, 6.879 embriyo | Xin 2024 (özet) |
| niPGT (DNA, YZ değil; karşılaştırma) | Duyarlılık 0.84, özgüllük 0.85, AUC 0.91; < 100 olgulu çalışmalarda daha yüksek | SROC | 20 çalışma | Huang 2023 (özet) |
| niPGT-A + makine öğrenmesi (metabolomik) | Doğruluk %91; duyarlılık %92.16; özgüllük %97.30 | Doğruluk | Retrospektif, 120 örnek, firma yazarları | Walsh 2026 (özet) |
| Oosit → öploidi (MAGENTA) | 0.542 → 0.607 → 0.666; kalibrasyon eğimi 0.259 → 0.645 | AUC | Retrospektif, tek merkez, 3.514 PGT-A embriyosu | Setti 2026 (özet) |
| Donör oosit → blastokist (MAGENTA) | 0.60; yaşla 0.62; ek değişkenlerle 0.65; kümülatif canlı doğum 0.691 | AUC | Prospektif, kör, 3 merkez, 1.179 oosit | Cimadomo 2025 (özet) |
| Oosit sayısı tahmini (ML) | MAE 0.62–4.13; 9 çalışmanın hiçbiri dış doğrulanmamış | Ortalama mutlak hata | Sistematik derleme (8 retrospektif + 1 prospektif) | Wilkinson 2025 (özet) |
| Folikül ölçümü (≥ 10 mm) | F1 %93.3 (90.7–95.1); kesinlik %98.2; duyarlılık %88.9 | F1 | Retrospektif + prospektif 904 tarama; 4 merkez | Wygocki 2026 (özet) |
| Folikül, tüm boyutlar | Kesinlik %94.2; duyarlılık %68.9 | Kesinlik / duyarlılık | Aynı çalışma | Wygocki 2026 (özet) |
| Sperm analizi (56 çalışma) | Morfoloji sınıflamasında sıklıkla > %90 doğruluk; çoğu küçük ve tek merkezli | Doğruluk | Sistematik derleme | Varzaneh 2026 (özet) |
| Sperm seçimi (SiD) | Kardeş oositlerde anlamlı fark yok | Klinik sonuç | Prospektif, 646 MII oosit | Montjean 2024 (özet) |
| Embriyo morfoloji derecesi (YZ ve embriyolog) | YZ medyan %75.5; embriyolog %65.4 | Doğruluk | 20 çalışma, hiçbiri prospektif değil | Salih 2023 (özet) |
| Tedavi öncesi canlı doğum (klasik modeller, dış) | 0.67–0.69; merkeze özgü 0.71; dış modeller düşük tahmin | AUC | Retrospektif, 26.382 hasta, Çin | Cai 2024 (özet) |
| Kümülatif canlı doğum (OPIS, güncellenmiş) | Tedavi öncesi 0.67; tedavi sonrası 0.75 | c-istatistiği | HFEA, 91.035 kadın; güncelleme gerekti | Ratna 2023 (özet) |
| Merkeze özgü ML (Univfy) | SART modeline göre PR-AUC ve F1 daha iyi (ROC-AUC özette yok) | PR-AUC / F1 | Retrospektif, 6 merkez, 4.635 hasta; firma yazarları | Yao 2025 (özet) |

---

## “Neden bazı sayılar parlak?” Altı mekanizma (soru-cevap ve sahne 2 için)

1. **Payda:** Atılan embriyolar FH− sayılınca AUC 0.95 olur; yalnız transfer edilenlerde 0.67. Yazarların kendi cümlesi: kolay olan, durmuş embriyodan iyi blastokisti ayırmak; zor olan, iyi blastokistler arasında sıralamak. Her iki ölçünün de raporlanmasını öneriyorlar (Berntsen 2022, tam metin).
2. **Retrospektif seçim yanlılığı:** Transfer edilen embriyoları embriyolog seçtiği için, embriyoloğun yöntemi bu alt kümede düşük görünür. Simülasyonda eşit iki model (genel AUC 0.76) seçilmiş embriyolarda 0.59'a karşı 0.74 çıkıyor. Yazarlara göre retrospektif çalışmalarda üstünlük iddiaları bu nedenle dikkatle okunmalı (Kragh 2021, tam metin).
3. **Merkez değişimi:** Merkez dışarıda bırakma testinde 0.60–0.75. Yazarlar düşük merkezlerdeki farkı, genç hastalarda transfer edilen embriyoların hep iyi kaliteli ve birbirine benzer olmasıyla açıklıyor (Berntsen 2022, tam metin). STORK-A da dış setlerde düşüyor: test 0.737, dış 0.702 / 0.715 (Barnes 2023).
4. **Aynı mimari, farklı sıralama:** 50 kopya modelin AUC'si benzer (≈ 0.60), ama Kendall W ≈ 0.35 ve kritik hata ≈ %15. Başka merkezde kararsızlık artıyor (Thirumalaraju 2025).
5. **Basit model ≥ derin öğrenme:** Ploidi tahmininde karma lojistik regresyon 0.71, derin öğrenme 0.63 (Bamford 2023). Sentetik demoda da lojistik regresyon doğrulama biçimine duyarsız (0.706 → 0.704), gradyan artırma ise düşüyor (0.686 → 0.646).
6. **Kalibrasyon nadiren raporlanıyor ve çoğu zaman bozuk çıkıyor:** MAGENTA tek başına eğim 0.259 (Setti 2026). İngiltere/ABD modelleri Çin verisinde düşük tahmin etti (Cai 2024). İkinci siklus modelinde eğim 0.85 ve aşırı tahmin görüldü (Ratna 2022, PMID 35866894, yalnız özet). Kragh 2021, eşik kullanılacaksa önce kalibrasyon yapılmasını öneriyor.
7. **(Ek) Küçük örneklem ve görev türü:** niPGT meta-analizinde < 100 olgulu çalışmaların duyarlılığı ve özgüllüğü daha yüksek (Huang 2023). Metabolomik ML'de 120 örnekle %91 doğruluk bildirildi (Walsh 2026). Sperm morfolojisindeki > %90 doğruluk, insan etiketini taklit etme başarısıdır, klinik sonucu tahmin etme başarısı değildir (Varzaneh 2026).
8. **(Ek) Yaş etkisi:** Modele yaş eklemek genel AUC'yi yükseltir, ama aynı hastanın embriyoları arasındaki sıralamayı iyileştirmeyebilir (Berntsen 2022 tartışması, tam metin). Ueno'da > 42 yaş grubunda Gardner bile 0.75.

---

## Soru-cevap yedekleri

- **“AUC 0.67 iyi mi kötü mü?”** Gardner derecelendirmesi aynı veride 0.64–0.65 civarında (Ueno 2021). YZ çoğunlukla ya eşit ya biraz iyi. Fark anlamlılığa yalnız < 35 yaş grubunda ulaştı (0.72'ye karşı 0.64).
- **“Kohort içinde ne kadar işe yarıyor?”** Euploid embriyoyu ilk sıraya koyma oranı: YZ v2 %68, Gardner %58, rastgele %44 (Cimadomo 2026, PMID 42546812, özet; ortak yazarlardan biri Vitrolife).
- **“Yüksek AUC = yüksek gebelik oranı mı?”** Hayır. Berntsen'in yazarları açıkça yazıyor: AUC, verilen bir kohort içinde sıralamayı ölçer, implantasyon oranını değil (tam metin).
- **Berntsen'in test bölmesi:** Veri, embriyo düzeyinde ve tedaviler arasında rastgele bölünmüş (tam metin: “randomly split … for individual embryos across all treatments and clinics”). Aynı hastanın kardeş embriyoları hem eğitimde hem testte bulunabilir. Bu sorunu merkez dışarıda bırakma testi kısmen giderir. Bunun AUC'yi ne kadar etkilediği makalede ölçülmemiş; slaytta iddia edilmez, yalnız soru gelirse söylenir.

---

## Kaynaklar

| Anahtar | Künye | PMID | DOI | Okuma | Tasarım | Çıkar çatışması / sponsor |
|---|---|---|---|---|---|---|
| berntsen_2022 | Berntsen J ve ark. Robust and generalizable embryo selection based on AI and time-lapse image sequences. PLoS One 2022;17(2):e0262661 | 35108306 | 10.1371/journal.pone.0262661 | Tam metin (PMC8809568) | Retrospektif, 18 merkez, 115.832 embriyo; test 17.249 / KID 2.212; merkez dışarıda bırakma testi | 4 yazar Vitrolife (iDAScore üreticisi) |
| kragh_2021 | Kragh MF, Karstoft H. Embryo selection with AI: how to evaluate and compare methods? JARG 2021;38(7):1675–1689 | 34173914 | 10.1007/s10815-021-02254-6 | Tam metin (ilgili bölümler; PMC8324599) | Yöntem makalesi + simülasyon | İlk yazar Vitrolife bağlantılı |
| ueno_2021 | Ueno S ve ark. F&S 2021;116(4):1172–1180 | 34246469 | 10.1016/j.fertnstert.2021.06.001 | Yalnız özet | Retrospektif, tek merkez, 3.018 SVBT | Ortak yazar Vitrolife |
| mina_2025 | Mina A ve ark. Contracept Reprod Med 2025;10(1):59 | 41016945 | 10.1186/s40834-025-00400-4 | Yalnız özet | Sistematik derleme + tanısal meta-analiz (QUADAS-2) | Özette bildirilmemiş; dergi etki düzeyi görece düşük |
| thirumalaraju_2025 | Thirumalaraju P ve ark. F&S 2025/26;125(2):277–286 | 40876725 | 10.1016/j.fertnstert.2025.08.021 | Yalnız özet | Laboratuvar temelli, retrospektif, 2 merkez (10.713 + 648 embriyo) | Özette bildirilmemiş |
| cimadomo_2026 | Cimadomo D ve ark. F&S 2026;126(5):842–850 | 42546812 | 10.1016/j.fertnstert.2026.07.025 | Yalnız özet | Retrospektif, tek merkez, 279 siklus | Ortak yazarlardan biri Vitrolife |
| barnes_2023 | Barnes J ve ark. Lancet Digit Health 2023;5(1):e28–e40 | 36543475 | 10.1016/S2589-7500(22)00213-8 | Yalnız özet | Retrospektif geliştirme + 2 dış set; 10.378 embriyo | NIH finansmanı |
| bamford_2023 | Bamford T ve ark. Hum Reprod 2023;38(4):569–581 | 36825452 | 10.1093/humrep/dead034 | Yalnız özet | Çok merkezli kohort, 9 klinik, 8.147 embriyo | Bir yazar katılımcı merkezlerde küçük hissedar |
| ma_2024 | Ma BX ve ark. Reprod Biol Endocrinol 2024;22(1):58 | 38778410 | 10.1186/s12958-024-01230-w | Yalnız özet | Retrospektif, 3.448 blastokist | Özette bildirilmemiş |
| selntigia_2025 | Selntigia A ve ark. Genes 2025;16(8):981 | 40870029 | 10.3390/genes16080981 | Yalnız özet | Anlatı derlemesi, 6 retrospektif çalışma | Özette bildirilmemiş |
| xin_2024 | Xin X ve ark. EClinicalMedicine 2024;77:102897 | 39513188 | 10.1016/j.eclinm.2024.102897 | Yalnız özet | Sistematik derleme + meta-analiz (QUADAS-AI), 12 çalışma | Çin ulusal fonu |
| huang_2023 | Huang B ve ark. JARG 2023;40(6):1243–1253 | 36952146 | 10.1007/s10815-023-02760-9 | Yalnız özet | Tanısal doğruluk meta-analizi, 20 çalışma. **niPGT; YZ değil** | Özette bildirilmemiş |
| walsh_2026 | Walsh R ve ark. RBMO 2026;53(5):105892 | 42759383 | 10.1016/j.rbmo.2026.105892 | Yalnız özet | Retrospektif, 120 SECM örneği, metabolomik + LightGBM | İlk yazar Progenesis Inc. (firma) |
| setti_2026 | Setti A ve ark. F&S Science 2026;7(3):196–208 | 41825691 | 10.1016/j.xfss.2026.03.002 | Yalnız özet | Retrospektif, tek merkez, 13.370 oosit, 3.514 PGT-A embriyosu | Bir yazar Future Fertility (MAGENTA üreticisi) |
| cimadomo_2025 | Cimadomo D ve ark. Hum Reprod 2025;40(10):1886–1892 | 40759152 | 10.1093/humrep/deaf153 | Yalnız özet | Prospektif, gözlemsel, kör, 3 merkez, 1.179 oosit | 4 yazar Future Fertility çalışanı ve hisse opsiyonu sahibi |
| wilkinson_2025 | Wilkinson J ve ark. RBMO 2025;52(4):105362 | 41780078 | 10.1016/j.rbmo.2025.105362 | Yalnız özet | Sistematik derleme (TRIPOD, PROBAST), 9 çalışma, 62.354 siklus | Bazı yazarlar Care Fertility |
| wygocki_2026 | Wygocki P ve ark. JARG 2026;43(3):715–729 | 41485151 | 10.1007/s10815-025-03777-y | Yalnız özet | Retrospektif 5.508 tarama, 4 merkez + prospektif 904 tarama | Yazarların çoğu MIM Fertility (geliştirici) |
| varzaneh_2026 | Varzaneh ZA ve ark. Int J Med Inform 2026;224:106766 | 43002852 | 10.1016/j.ijmedinf.2026.106766 | Yalnız özet | Sistematik derleme (PRISMA), 56 çalışma | Özette bildirilmemiş |
| montjean_2024 | Montjean D ve ark. Med Sci (Basel) 2024;12(2):19 | 38651413 | 10.3390/medsci12020019 | Yalnız özet | Prospektif, kardeş oosit, 646 MII | Özette bildirilmemiş |
| salih_2023 | Salih M ve ark. Hum Reprod Open 2023;2023(3):hoad031 | 37588797 | 10.1093/hropen/hoad031 | Yalnız özet | Sistematik derleme, 20 çalışma | Monash fonu; çıkar çatışması yok |
| berman_2023 | Berman A ve ark. AJOG 2023;229(5):490–501 | 37116822 | 10.1016/j.ajog.2023.04.027 | Yalnız özet | Tanısal doğruluk derlemesi, 22 çalışma (hepsi retrospektif) | Özette bildirilmemiş |
| cai_2024 | Cai J ve ark. Hum Reprod 2024;39(2):364–373 | 37995380 | 10.1093/humrep/dead242 | Yalnız özet | Retrospektif dış doğrulama, tek merkez, 26.382 hasta | Çin kamu fonları |
| ratna_2023 | Ratna MB ve ark. Hum Reprod 2023;38(10):1998–2010 | 37632223 | 10.1093/humrep/dead165 | Yalnız özet | Dış doğrulama, HFEA, 91.035 kadın | Bazı yazarlara Merck konuşma ücreti |
| ratna_2022 | Ratna MB ve ark. Hum Reprod 2022;37(9):2075–2086 | 35866894 | 10.1093/humrep/deac152 | Yalnız özet | Geliştirme + dış doğrulama, HFEA | Çıkar çatışması yok |
| yao_2025 | Yao MWM ve ark. Nat Commun 2025;16(1):3661 | 40246850 | 10.1038/s41467-025-58744-z | Yalnız özet | Retrospektif doğrulama, 6 merkez, 4.635 hasta | Univfy yazarları |
| sentetik_demo | Kendi sentetik analizi: `/home/claude/sunum/analiz/sonuc_slayt/sonuclar.json` (4.428 embriyo, 700 sentetik hasta) | — | — | Dosya | Sentetik veri; klinik bulgu değil | — |

Not: Bölüm 3'e köprü olarak anılan Illingworth 2024 (PMID 39122964) bu bölümde sayıyla kullanılmadı; sayıları `03_*` dosyasında.

---

## Doğrulanamayanlar ve uyarılar

- **YZ ve niPGT-A birleşimi için büyük, dış doğrulanmış hakemli veri bulunamadı.** Bulunan tek doğruluk sayısı Walsh 2026'dan (120 örnek, retrospektif, firma yazarları; %91 doğruluk). DECENT (Zhang 2025, PMID 40583136) yöntem makalesi; özette AUC/duyarlılık yok. Huang 2023'ün 0.91'i **YZ değildir** (DNA tabanlı niPGT); slaytta kullanılırsa “YZ değil, karşılaştırma için” etiketi zorunlu.
- **Sperm:** Varzaneh 2026 özetinde havuzlanmış tek bir sayı yok; yalnız “frequently achieved accuracies exceeding 90%” ifadesi var. Bu yüzden slayta nokta değil, soluk bant konur. Sperm seçiminin klinik sonuca etkisinde YZ için doğruluk (AUC) verisi bulunamadı; SiD çalışmasında anlamlı fark yok.
- **Univfy (Yao 2025):** ROC-AUC değeri özette yok (PR-AUC ve F1 karşılaştırması var); slayta sayı konmadı. Tam metin okunmadı.
- **Mina 2025** meta-analizi görece düşük etkili bir dergide; havuzlanan çalışma sayısı özette yok. Değer (AUC 0.7) yalnız destekleyici nokta olarak kullanılmalı; ana dayanak Berntsen.
- **Thirumalaraju** AUC'si özette “approximately 60%” olarak geçiyor; slaytta “≈ 0.60” yazılmalı.
- **Ueno 2021 ve Cimadomo 2026'da Vitrolife ortak yazar; Berntsen ve Kragh Vitrolife bağlantılı; MAGENTA çalışmalarında Future Fertility yazarları; FOLLISCAN'da MIM Fertility yazarları; Walsh'ta Progenesis.** Künye satırında “firma yazarları” notu önerilir.
- **Setti 2026 (MAGENTA öploidi):** Ortak bağlamda “doi:10.1016/j.xfss.2026.03.002” olarak geçen çalışma; PMID 41825691 olarak doğrulandı. Kalibrasyon eğimi 0.259 → 0.645 özetle birebir uyumlu.
- **Ortak bağlamdaki Kragh 2021 için DOI** verilmemişti; doğrusu 10.1007/s10815-021-02254-6.
- **Sentetik demo** (0.686 → 0.646) gerçek hasta verisi değildir; ekranda “SENTETİK” etiketi zorunlu.
- **Berntsen'deki embriyo düzeyinde rastgele bölme**, kardeş embriyoların eğitim ve test setine dağılmasına izin veriyor (tam metin). Bunun AUC'ye etkisi makalede ölçülmemiş; slayta “şişirdi” iddiası konmamalı.
- Sfakianoudis 2022 (Biomedicines, PMID 35327499, yalnız özet): canlı doğumda SROC AUC 0.905, ama O:E oranı 1.12 ve %95 tahmin aralığı 0.02–6.54. Kalibrasyon heterojenliğine çarpıcı bir örnek; ancak dergi düzeyi ve yöntem nedeniyle yalnız soru-cevap yedeği olarak önerilir, slayta konmadı.
