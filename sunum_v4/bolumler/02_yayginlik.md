# Bölüm 2: Ne kadar yaygınlaştı? Nerede, ne kadar kullanılıyor?

## Tek cümlelik cevap

Firmaların kendi duyurularına göre IVF laboratuvarı yapay zekâ yazılımları 30’dan fazla ülkede, yüzlerce klinikte (Türkiye dahil) sunuluyor; kullanımı ulusal ölçekte ölçen hakemli veri ise az: Japonya’daki ulusal ankette yanıt veren 345 tesisten 57’si embriyo değerlendirmesinde yapay zekâ skoru kullanıyordu. Kullanım yayılıyor, ama yaygın kullanım kanıt değildir.

---

## Sahneler

### Sahne 2.1: Harita (firma ve klinik beyanları)

**Eylem başlığı:** YZ yazılımları 30’dan fazla ülkede, yüzlerce klinikte duyuruluyor (9 sözcük)

**Ekranda** (40 sözcük):
> Embriyo seçimi yazılımı: “100’den fazla klinik”, 4 bölge · Oosit yazılımı: “300’den fazla klinik”, 32 ülke · Bir ağ: 60 klinik, 16 ülke, yılda ~77.000 siklus · Türkiye: embriyo seçimi 2022’den beri (bir merkez), YZ ile sperm seçimi (iki merkez)
> Rozet: **Firma/klinik beyanı · hakemli değil**

**Görsel / etkileşim önerisi:**
- Dünya haritası yerine **ülke ızgarası (tile-grid)**: her ülke eşit boyutlu bir kare; kareler kabaca coğrafi konuma göre dört bölge bloğunda dizilir (Amerika · Avrupa · Asya-Pasifik · ortada büyütülmüş **Türkiye** karesi, kalın kenarlı). Böylece büyük ülkeler görsel ağırlık kazanmaz ve Türkiye seçilir.
- Her karede **ürün türü noktaları**, renk körlüğüne uygun (Okabe-Ito) beş renk:
  - E = embriyo seçimi (#0072B2 mavi) · O = oosit (#E69F00 turuncu) · S = sperm/ICSI (#009E73 yeşil) · U = stimülasyon/USG (#CC79A7 pembe) · P = prognoz/danışmanlık (#56B4E9 açık mavi).
  - Renk tek başına anlam taşımasın: noktaların içinde harf (E/O/S/U/P) de yazsın.
- Sağda üç **“beyan sayacı” kartı** (CHLOE 100+, MAGENTA 300+, bir ağ 60/16/~77.000); her kartın köşesinde gri “firma/klinik beyanı · hakemli değil” etiketi ve tarih.
- Etkileşim: lejanttaki renge tıklayınca yalnız o türün bulunduğu ülkeler yanar (ör. “S” seçilince yalnız Meksika ve Türkiye kalır; sperm/ICSI tarafının ne kadar dar olduğu görülür). Bir kareye tıklayınca küçük kart açılır: tür, ölçek beyanı, tarih, kaynak türü. Merkez adı hiçbir kartta yok.
- Alt şerit (küçük, gri): “Oosit yazılımının ortak klinik sayfası 32 ülke listeliyor” + o 32 ülkenin kareleri soluk turuncu çerçeveyle eklenebilir (isteğe bağlı; ızgarayı kalabalıklaştırırsa yalnız sayı olarak kalsın).
- Vitrolife’ın “dünyadaki kliniklerin %75’i” beyanı **slayta konmamalı**: tüm ürünler için, YZ’ye özgü değil (aşağıda uyarı).

**Ülke tablosu (ızgaranın verisi):**

| Bölge | Ülke | Tür | Firmanın/kliniğin açıkladığı ölçek | Kaynak anahtarı | Doğrulama |
|---|---|---|---|---|---|
| Amerika | ABD | E, U, P, (O) | Bir ağ: CHLOE + Alife; bir ağ (25+ şube): Stim Assist; bir ağ: pilot; Univfy merkezleri; oosit yazılımı ortak listesinde ABD var | W4, W2 | W2 bugün; W4 önceki oturum |
| Amerika | Meksika | S (ICSI otomasyonu), (O) | AURA iki şehirde (Mexico City, Guadalajara); ABD’de 2027 planı | W4, W2 | önceki oturum; W2 listesinde Meksika var |
| Amerika | Kolombiya | U, (O) | FOLLISCAN tek merkez; 11 klinik/7 ülke doğrulaması | W4, W2 | önceki oturum |
| Avrupa | İspanya | E, O | Bir grup 7 klinik CHLOE; bir merkez MAGENTA | W4, W2 | önceki oturum; W2 listesinde İspanya var |
| Avrupa | İngiltere | O, P | MAGENTA/VIOLET; Univfy | W4, W2 | önceki oturum; W2 listesinde var |
| Avrupa | İsviçre | P, (O) | Univfy merkezi | W4, W2 | önceki oturum; W2 listesinde var |
| Asya-Pasifik | Avustralya | E | Kendi geliştirdiği model + iDAScore RKÇ merkezi | W4 | önceki oturum |
| Asya-Pasifik | Japonya | E, (O) | Life Whisperer sunuluyor; MAGENTA (önceki oturum) — **hakemli:** 57 tesis TLT + YZ skoru (P1) | W4, P1 | P1 tam metin; MAGENTA bugün W2 listesinde görülmedi |
| Asya-Pasifik | Endonezya | E | Life Whisperer sunuluyor | W4 | önceki oturum |
| Asya-Pasifik | Hindistan | E, (O) | Bir ağ 100+ klinikte Life Whisperer (Kasım 2022 duyurusu; güncel durum bilinmiyor) | W4, W2 | önceki oturum; W2 listesinde var |
| **Türkiye** | **Türkiye** | **E, S** | Embriyo seçimi (CHLOE) 2022’den beri, bir merkez, “Türkiye’de ilk” beyanı; YZ ile sperm seçimi iki merkez, farklı ürünler; iDAScore’un Türkçe kılavuzu var | W4 | önceki oturum; Türkiye W2 listesinde yok |
| Çok ülkeli | 4 bölge | E | CHLOE: “more than 100 fertility clinics across North America, Europe, Asia-Pacific, and Latin America” (29 Temmuz 2026) | W1 | **bugün doğrulandı** |
| Çok ülkeli | 32 ülke listesi | O | Future Fertility ortak klinik sayfası: “Explore over 300 clinics worldwide” | W2 | **bugün doğrulandı** |
| Çok ülkeli | 16 ülke | E, P | Bir ağ: “operates 60 clinics across 16 countries”, “more than 77,000 IVF cycles annually”; Alife araçları: Embryo Predict, Success Predictor, Egg Retrieval Report (5 Mayıs 2026) | W3 | **bugün doğrulandı** |

Parantezli tür = yalnız oosit yazılımının ortak klinik listesinde ülkenin geçmesine dayanıyor.

**Sayılar:**
- CHLOE “100’den fazla klinik”, 4 bölge — W1 (web, bugün doğrulandı)
- MAGENTA ortak sayfası “300’den fazla klinik”, 32 ülke listeleniyor — W2 (web, bugün doğrulandı; 32 ülke sayısı sayfadaki listeden sayıldı)
- Bir ağ: 60 klinik, 16 ülke, yılda 77.000’den fazla siklus — W3 (web, bugün doğrulandı)
- Türkiye: 2022’den beri, bir merkez; sperm seçimi iki merkez — W4 (web, önceki oturum)

**Sunucu notu** (≈ 140 sözcük, 60 sn):
Önce şunu söyleyeyim: bu sahnedeki sayıların hiçbiri hakemli bir dergiden gelmiyor; hepsi firmaların ya da kliniklerin kendi duyuruları. Yine de tablo oldukça net. Bir embriyo seçimi yazılımı yüzden fazla klinikte kullanıldığını söylüyor; Kuzey Amerika’da, Avrupa’da, Asya-Pasifik’te ve Latin Amerika’da. Bir oosit kalite yazılımının ortak klinik sayfası üç yüzden fazla klinik ve otuz iki ülke sayıyor. Bir klinik ağı da on altı ülkedeki altmış kliniğinde, yılda yetmiş yedi binden fazla siklusta embriyo seçimi ve prognoz araçlarını devreye aldığını bu yıl mayıs ayında duyurdu. Renklere bakarsanız en yoğun alan embriyo seçimi; onu oosit ve prognoz izliyor. Sperm seçimi ve ICSI otomasyonu ise hâlâ birkaç merkezle sınırlı. Türkiye de bu haritada: bir merkez 2022’den beri embriyo seçiminde yapay zekâ kullandığını duyuruyor, iki merkez de farklı ürünlerle yapay zekâ destekli sperm seçimi sunuyor. Merkez adı vermiyorum; konu merkezler değil, eğilim.

**Süre (sn):** 60

**Künye satırı:**
Firma/klinik beyanları, hakemli değil · Fairtility basın bülteni 29.07.2026 · Future Fertility ortak klinik sayfası · Alife ortaklık bülteni 05.05.2026 (erişim 14.11.2026) · diğerleri: firma/klinik siteleri, tarayıcıda görüldü 10.11.2026

---

### Sahne 2.2: Hakemli veride ölçülen kullanım

**Eylem başlığı:** Japonya ulusal anketi: 345 tesisten 57’si YZ skoru kullanıyor (9 sözcük)

**Ekranda** (39 sözcük):
> Japonya 2022–23: 616 tesis → 345 yanıt → 195 TLT → 184 TLT ile değerlendirme → **57 TLT + YZ skoru**
> 2023 uluslararası anket: 702 embriyolog, çoğu olumlu, etik ve iş kaygısı
> 21 firma sitesi: hiçbiri riski açıkça yazmıyor
> **Yaygın kullanım kanıt değildir.**

**Görsel / etkileşim önerisi:**
- Solda **yatay huni (funnel) çubuğu**: 616 → 345 → 195 → 184 → 57; her basamakta ham sayı; son basamak (57) koyu mavi (embriyo seçimi rengi), diğerleri gri. Huninin altında küçük not: “YZ araçları içinde iDAScore %63.2”. Yüzde yerine ham sayılar: paydalar değiştiği için yüzde karışıklık yaratır (aşağıdaki uyarı).
- Sağ üstte ince kart: “702 embriyolog · 17 Temmuz–31 Ağustos 2023 · 32 soru” + iki ikon yerine iki kısa etiket: “olumlu” / “etik, iş, hasta ilişkisi kaygısı”. Kartın altında gri not: “Yazarların bir kısmı YZ firmalarıyla bağlantılı.”
- Sağ altta ince kart: “21 firma · 30 YZ aracı · 21/21 fayda anlatıyor · 0/21 riski açıkça belirtiyor”.
- En altta tam genişlikte köprü cümlesi, sahnenin son tıklamasında belirir: “Kullanım hızla yayılıyor. Yaygın kullanım kanıt değildir.” → bir sonraki bölümün sorusuna geçiş (“Sonuçları değiştirdi mi?”).
- %24.8 → %53.2 eğrisi bu slayta **konmamalı** (asıl anket doğrulanamadı). Kullanıcı yine de isterse yalnız kesik çizgili, gri, “ikincil aktarım; asıl anket doğrulanamadı” etiketli tek bir ok olarak; önerim koymamak.

**Sayılar:**
- 616 tesis davet; 345 geçerli yanıt (%56.0) — P1 (tam metin)
- TLT olan tesis 195/345 (%56.5; özet ve “key findings” %54.6 diyor) — P1 (tam metin)
- TLT görüntüsünü embriyo değerlendirmesinde kullanan 184/195 (%94.3) — P1 (tam metin)
- TLT + YZ skoru kullanan 57 tesis (%31.0; payda 184) — P1 (tam metin)
- YZ araçları içinde “intelligence data analysis score” %63.2 — P1 (tam metin)
- 57/345 ≈ altıda bir — P1 sayılarından **hesap** (yalnız sunucu notunda)
- 702 yanıt, 32 soru, 17 Temmuz–31 Ağustos 2023 — P2 (yalnız özet)
- 21 firma, 30 YZ aracı; 21/21 fayda; risk açıkça belirten site yok; örneklem büyüklüğü açıklayan 7 (%33.3) — P3 (yalnız özet)

**Sunucu notu** (≈ 140 sözcük, 60 sn):
Peki hakemli literatür ne diyor? Kullanımı ulusal ölçekte ölçen, bulabildiğim tek çalışma Japonya’dan. Japonya Üreme Tıbbı Derneği 2022 sonunda ülkedeki 616 tesise anket gönderdi; 345 tesis yanıt verdi. Bunların 195’inde time-lapse vardı, 184’ü embriyoyu time-lapse görüntüsüyle değerlendiriyordu ve 57 tesis buna bir yapay zekâ skorunu ekliyordu. Kabaca söylersek, yanıt veren her altı tesisten biri. 2023’te yapılan uluslararası ankete 702 embriyolog katıldı; çoğu yapay zekâya olumlu bakıyor, ama etik, iş güvencesi ve hasta ilişkisi konusunda çekinceleri var. Şunu da not edeyim: bu anketin yazarlarının bir kısmı yapay zekâ firmalarıyla bağlantılı. Bir de arz tarafına bakalım: 21 firmanın web sitesi incelenmiş; hepsi fayda anlatıyor, hiçbiri riski açıkça yazmıyor. Yani kullanım hızla yayılıyor, ama yaygın kullanım kanıt değildir. Bu yüzden bir sonraki soru önemli: bu kadar kullanım sonuçları değiştirdi mi?

**Süre (sn):** 60

**Künye satırı:**
Yamada ve ark. AJOG Glob Rep 2024;4:100397, PMID 39493437 · Palmer ve ark. RBMO 50(3):104435, PMID 39939196 · Du & Zhang Hum Reprod Open 2026:hoag086, PMID 42923733

---

## Kaynaklar

### Hakemli (PubMed)

**P1 — Yamada 2024 (Japonya ulusal anketi)**
- Künye: Yamada, Ezoe, Ueno, Yoshino, Takahashi (PubMed yazar listesi; baş harfler kayıtta görülmedi). “Use of time-lapse technology on fertilization verification, embryo evaluation, and utilization: A national survey in Japan.” AJOG Glob Rep. 2024;4(4):100397.
- PMID 39493437 · PMCID PMC11530904 · DOI [10.1016/j.xagr.2024.100397](https://doi.org/10.1016/j.xagr.2024.100397)
- Okuma derinliği: **tam metin** (PMC).
- Tasarım: ulusal, kesitsel çevrim içi anket; Japonya Kadın Hastalıkları ve Doğum Derneği’ne kayıtlı tüm ART tesisleri (n=616), 23 Aralık 2022–16 Ocak 2023; tesis başına bir yanıtlayıcı (%87.0 embriyolog).
- Sayılar (aynen): 345 geçerli yanıt, yanıt oranı %56.0 (345/616); TLT benimseme “56.5% (195/345)” (bulgular) ve “54.6%” (özet, key findings, tartışma); “TLT images were used for embryo evaluation in 94.3% (184/195) of the facilities. Embryos were evaluated at 57 facilities (31.0%) using a combination of TLT images and artificial intelligence-based scoring systems.”; “the intelligence data analysis score (63.2%) had the highest utilization rate”.
- Çıkar çatışması/sponsor: anket Japonya Üreme Tıbbı Derneği’nin komitesi ve Embriyoloji SIG tarafından yapıldı; tam metin çıktısında finansman/çıkar beyanı bölümü görülmedi.

**P2 — Palmer 2024 (uluslararası embriyolog anketi, 702 yanıt)**
- Künye: Palmer GA, Paredes O, Drakeley A, Chavez-Badiola A, Woolley TE, Kaouri K, Cohen J. “Use and understanding of AI in the ART laboratory: an international survey.” Reprod Biomed Online. 50(3):104435; PubMed yayın tarihi 3 Eylül 2024.
- PMID 39939196 · DOI [10.1016/j.rbmo.2024.104435](https://doi.org/10.1016/j.rbmo.2024.104435) · PMC kaydı yok.
- Okuma derinliği: **yalnız özet**.
- Tasarım: kesitsel çevrim içi anket, 32 soru, 17 Temmuz–31 Ağustos 2023, dünya genelinde klinik embriyologlar; 702 yanıtlayıcı.
- Bulgular (özetten): “high degree of awareness of AI concepts”; benimsemeye açık, ancak etik, iş üzerindeki etki ve hasta ilişkisi konusunda çekince; “Most embryologists, independent of age, were positive regarding AI, but workplace concerns diminished with age.” **Özette kullanım oranı (yüzde) yok.**
- Çıkar çatışması/sponsor: yazar bağlantıları arasında IVF 2.0 Ltd ve Conceivable Life Sciences (YZ ürünü geliştiren firmalar) var; “Research Support, Non-U.S. Gov’t”. Çıkar beyanı metni okunmadı.

**P3 — Du & Zhang 2026 (firma web siteleri içerik analizi)**
- Künye: Du L, Zhang Y. “AI-assisted IVF company websites: a content analysis of marketing claims, information quality, legal and ethical issues.” Hum Reprod Open. 2026;2026(4):hoag086.
- PMID 42923733 · PMCID PMC13690092 · DOI [10.1093/hropen/hoag086](https://doi.org/10.1093/hropen/hoag086)
- Okuma derinliği: **yalnız özet** (tam metin PMC’de var, okunmadı).
- Tasarım: nitel/nicel içerik analizi; 21 firma (7 IVF ekipman üreticisi, 14 yalnız YZ geliştiren); merkezleri Avrupa 9, İsrail 4, Kanada/ABD 5, Çin 3; 30 YZ aracı; içerik Ağustos 2023’te alındı, 30 Haziran 2026’da izlem.
- Sayılar (aynen): 21/21 (%100) fayda; “no websites explicitly outlined potential risks”; örneklem büyüklüğü açıklayan %33.3 (n=7); veri çeşitliliği belirten %23.8 (n=5); 19/21 (%90.5) klinisyen gözetimi şartı; 2 firma doğrudan tüketiciye pazarlama.
- Sponsor: Macau Üniversitesi; yazarlar çıkar çatışması olmadığını beyan ediyor.

**P4 — Chang 2026 (yalnız ikincil aktarım için)**
- Künye: Chang ve ark. Front Endocrinol. 2026; DOI [10.3389/fendo.2026.1910448](https://doi.org/10.3389/fendo.2026.1910448) · PMID 42769651 · PMCID PMC13591153.
- Okuma derinliği: **tam metin** (PMC; kaynakça listesi PMC metninde ve yayıncı sayfasının alınan kısmında yok).
- İlgili cümle (aynen): “Global AI adoption among IVF professionals rose from 24.8% in 2022 to 53.2% (any AI use across clinical domains) in 2025, with 83.62% of 2025 respondents indicating likely investment in AI within 1–5 years (10).” Ayrıca: “Cost is the top adoption barrier (38.01% of respondents, 2025)”.
- Tasarım: anlatı derlemesi (yazarlar seçim yanlılığını kabul ediyor). Atıf numarası **10**; kaynakçadaki 10 numaralı girdi görülemedi → asıl anket DOĞRULANAMADI.

### Web kaynakları (firma/klinik beyanı, hakemli DEĞİL; URL’ler slayta girmez)

| Anahtar | URL | Durum |
|---|---|---|
| W1 | https://firstfertility.com/press-release/fairtility-and-first-fertility-expand-strategic-partnership-to-deploy-chloe-across-multiple-ivf-laboratories/ | **14 Kasım 2026’da WebFetch ile doğrulandı.** Aynen: “more than 100 fertility clinics across North America, Europe, Asia-Pacific, and Latin America.” Tarih: **29 Temmuz 2026** (ortak bağlamdaki “27 Temmuz” düzeltilmeli). Ağın kendi klinik sayısı verilmiyor; CHLOE önce bir merkezde kurulmuş, ağın time-lapse laboratuvarlarına yayılacak. |
| W2 | https://futurefertility.com/en/partner-fertility-clinics/ | **14 Kasım 2026’da WebFetch ile doğrulandı.** Aynen: “Explore over 300 clinics worldwide.” (Cümlede MAGENTA/VIOLET adı geçmiyor; sayfa firmanın ortak klinik sayfası.) Listelenen 32 ülke: Arjantin, Bolivya, Brezilya, Kanada, Şili, Kolombiya, Kosta Rika, Kıbrıs, Dominik Cumhuriyeti, Ekvador, Mısır, Finlandiya, Almanya, Yunanistan, Hindistan, İrlanda, İtalya, Libya, Meksika, Panama, Paraguay, Peru, Portekiz, Romanya, Sırbistan, İspanya, İsviçre, BAE, İngiltere, ABD, Uruguay, Venezuela. **Türkiye ve Japonya listede görülmedi** (sayfa özetleyici model tarafından okundu; liste eksik olabilir). |
| W3 | https://futurelifegroup.com/en/press/18-futurelife-in-partnership-with-alife-health/ | **14 Kasım 2026’da WebFetch ile doğrulandı.** Aynen: “operates 60 clinics across 16 countries”, “performs more than 77,000 IVF cycles annually”; tarih satırı “SAN FRANCISCO and PRAGUE – May 5, 2026”; araçlar: Embryo Predict (blastokist değerlendirme), Success Predictor (tedavi öncesi prognoz), Egg Retrieval Report. Not: bülten 16 ülkenin Avrupa’da olduğunu bu çıktıda söylemiyor (ortak bağlamdaki “16 Avrupa ülkesi” ifadesi yerine “16 ülke” kullanıldı). Uzman sayısında bülten içi tutarsızlık (2.400 / 2.100); slayta girmedi. |
| W4 | (URL’ler önceki oturum kaydında yok) | **Önceki oturumda tarayıcıda görüldü, 10 Kasım 2026.** ABD ağları, Meksika (AURA), Kolombiya (FOLLISCAN), İspanya (7 klinik CHLOE), İngiltere/İsviçre (Univfy), Avustralya, Japonya ve Endonezya (Life Whisperer), Hindistan (bir ağ, 100+ klinik, Kasım 2022), Türkiye satırı, Vitrolife “%75”. Bu oturumda yeniden doğrulanmadı. |
| W5 | https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1910448/full | Chang 2026 yayıncı sayfası; %24.8 → %53.2 cümlesi ve atıf numarası (10) görüldü; kaynakça kısmı alınamadı. |

---

## Doğrulanamayanlar ve uyarılar

1. **%24.8 (2022) → %53.2 (2025) anketinin asıl kaynağı: DOĞRULANAMADI.** Chang 2026 tam metninde cümle ve atıf numarası (10) görüldü; kaynakça girdisi PMC metninde ve yayıncı sayfasının alınabilen kısmında yok. Europe PMC ve NCBI E-utilities doğrudan erişimi vekil sunucuda HTTP 403 verdi. PubMed’de “survey/questionnaire + AI + IVF/embryolog/professional” ve “cost/investment/barrier” aramaları, Palmer–Cohen yazar araması bu sayıları içeren hakemli bir anket bulmadı. Kaynak bir kongre özeti, firma raporu ya da hakemsiz bir anket olabilir. **Öneri:** slayta koyma; Onur isterse Chang 2026’nın PDF’indeki 10 numaralı kaynağı elle kontrol etsin.
2. **Palmer 2024 (702 embriyolog):** özette kullanım oranı yok; “çoğu olumlu” niteliksel ifadedir. Tam metin erişilemedi (PMC yok). Yazarların bir kısmı YZ firmalarıyla bağlantılı.
3. **ESHRE/ASRM üye anketi:** PubMed’de YZ kullanımını ölçen bir ESHRE veya ASRM üye anketi bulunamadı (DOĞRULANAMADI / muhtemelen yok).
4. **Japonya verisinde payda tutarsızlığı:** TLT oranı aynı makalede %54.6 (özet) ve %56.5 (195/345, bulgular). %31.0’ın paydası tüm tesisler değil, TLT görüntüsüyle embriyo değerlendiren 184 tesis. Bu yüzden slaytta ham sayılar (57/345) kullanıldı; “altıda bir” hesaptır, yalnız sözlü söylenir. Anket yalnız yanıt veren %56’yı temsil eder (yanıt yanlılığı olabilir).
5. **“30’dan fazla ülke”**, W2’deki 32 ülkelik listeye dayanır (firma beyanı). W2’de Türkiye ve Japonya görülmedi; Japonya’daki MAGENTA bilgisi yalnız önceki oturumdan geliyor.
6. **W1 tarih düzeltmesi:** basın bülteni 29 Temmuz 2026 (ortak bağlamda 27 Temmuz yazıyor).
7. **W3:** ortak bağlamdaki “16 Avrupa ülkesi” bu oturumda doğrulanmadı; yalnız “16 countries” görüldü.
8. **Vitrolife “dünyadaki kliniklerin %75’i”**: tüm ürünler için bir pazar beyanı, YZ kullanımı anlamına gelmez; slayta girmemeli.
9. **Hindistan (bir ağ, 100+ klinik)**: Kasım 2022 duyurusu; güncel durum bilinmiyor. Kartta tarih görünür olmalı.
10. **Merkez adı kuralı:** tablo ve notlarda merkez/ağ adı yok. W1 ve W3 URL’leri ağ adlarını içeriyor; bu URL’ler yalnız bu dosyada, slayta ve künye satırına girmez (künyede firma adı + tarih).
11. Beyan sayıları birbirine eklenmemeli: aynı klinik birden çok ürünü kullanıyor olabilir; “toplam klinik sayısı” hesaplanamaz.
