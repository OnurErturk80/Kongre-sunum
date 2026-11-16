# Bölüm 3: Bu kadar kullanılması sonuçları nasıl etkiliyor? Yapay zekâ kullanımı neye etki ediyor?

## Tek cümlelik cevap

En güçlü kanıta göre yapay zekâ (YZ) ve time-lapse tabanlı seçim canlı doğumu artırmıyor (fark yok; time-lapse için yüksek kesinlik, derin öğrenme için tek RKÇ). Ölçülebilir biçimde değiştirdiği şey embriyo değerlendirme süresi (~10 kat kısa, RKÇ alt çalışması). İlaç miktarı (FSH ~%10 az) ve tutarlılık için yalnız kontrolsüz ya da karışık kanıt var. Maliyet artıyor; hasta güveni sınırlı. Etik riskler tanımlanmış ama ölçülmemiş.

**Ana mesaj (düzeltilmiş):** “Yapay zekânın daha çok bebek getirdiği gösterilmedi; değiştirdiği şey hız ve iş akışı.”
— Taslaktaki “canlı doğumu artırmadı” ifadesi biraz fazla kesin. Illingworth’te canlı doğum farkının %95 GA’sı −9.9 ile +2.2 yüzde puan arasında. Yani ne küçük bir yarar ne de anlamlı bir zarar dışlanabiliyor. Yüksek kesinlikte “fark yok” bulgusu time-lapse/morfokinetik için (Bhide 2026), derin öğrenme için değil. Ayrıca “yaygın kullanım” ile ülke düzeyindeki sonuçları bağlayan bir kayıt analizi taramadık. Kanıt, kullanımın ne kadar yaygın olduğundan değil, randomize karşılaştırmalardan geliyor.

---

## Sahneler

Önerilen sıra: önce asıl soru (bebek sayısı), sonra değişen şey (zaman, tutarlılık, ilaç), en sonda bütün etkileri toplayan pano. Panoyu sona koymak bölüm 4’e (“ne kadar doğru?”) doğal bir geçiş sağlıyor. İstenirse pano başa alınıp bir “içindekiler” gibi de kullanılabilir. O durumda 1. ve 2. sahne panonun iki satırına yakınlaşma olur.

### Sahne 3.1: Asıl soru: daha çok bebek

**Eylem başlığı:** Canlı doğumda fark yok: en güçlü kanıt bunu söylüyor

**Ekranda:**
- Başlık altında: “Canlı doğum: mutlak risk farkı (yüzde puan) · sıfırın solu: standart lehine, sağı: YZ/TLI lehine”
- Grafik satır etiketleri (aynen):
  - “TLI genel · 4 RKÇ · n=2 913”
  - “Kesintisiz kültür · 5 RKÇ · n=2 971”
  - “Morfokinetik seçim · 3 RKÇ · n=2 937”
  - “Derin öğrenme (iDAScore) · 1 RKÇ · n=1 066”
- Alt not: “Freeze-all alt grubu: klinik gebelik %49.5 (YZ) vs %61.3 (embriyolog)”

**Görsel / etkileşim önerisi:**
- Yatay orman grafiği, mutlak risk farkı (ARD, yüzde puan), eksen −12 ile +8. Sıfırda dikey çizgi. Veri: `03_sayilar.json → _grafik_verisi.orman_ARD`.
- İki grup başlığı:
  - Üst grup: “Time-lapse / morfokinetik (derin öğrenme değil) — Bhide 2026, hasta düzeyinde meta-analiz, yüksek kesinlik”.
  - Alt grup: “Derin öğrenme — Illingworth 2024 RKÇ”.
- Illingworth için iki satır: canlı doğum (ikincil sonlanım) ve klinik gebelik (birincil sonlanım). Yalnız klinik gebelik satırında −5 noktasında kesikli “eşdeğerlik (non-inferiority) sınırı” çizgisi olsun. Güven aralığı bu çizgiyi geçtiği için “daha kötü değil” gösterilemedi; ekranda bu kısa bir etiketle belirtilir.
- Noktalar nötr gri, güven aralıkları ince çizgi. Kırmızı/yeşil yargı rengi kullanılmaz.
- Bir satırın üzerine gelince ya da dokununca kutucuk açılır: n, aOR veya oran, PMID ve okuma derinliği.
- Düğme: **“Freeze-all alt grubunu göster”**. Sağda küçük iki çubuklu bir iç grafik açılır:
  - taze transfer: %48.1 vs %44.5
  - freeze-all: %49.5 vs %61.3
  - Etiket: “alt grup analizi — dikkatle yorumlayın”.
- Oran ölçeğindeki değerler (Bhide aOR ve Yaghi RR) aynı JSON’da `_grafik_verisi.orman_oran` olarak duruyor. Tek eksende karışıklık olmaması için ana grafikte yalnız ARD gösterilir. Oran ölçeği yedek slayt ya da soru-cevap için.

**Sayılar:**
- TLI genel aOR 0.97 (0.81–1.15), ARD −0.7 (−4.9 ile 3.4); 4 RKÇ, n=2 913 — `bhide2026`
- Kesintisiz kültür aOR 1.02 (0.84–1.23), ARD 0.5 (−4.1 ile 5.0); 5 RKÇ, n=2 971 — `bhide2026`
- Morfokinetik seçim aOR 0.92 (0.78–1.07), ARD −2.0 (−5.7 ile 1.6); 3 RKÇ, n=2 937 — `bhide2026`
- Bhide toplam: 8 RKÇ, n=5 642; “high-certainty evidence” — `bhide2026`
- Illingworth: 14 klinik, 1 066 hasta (533/533) — `illingworth2024`
- Klinik gebelik %46.5 (248/533) vs %48.2 (257/533); RD −1.7 (−7.7 ile 4.3); non-inferiority sınırı −5 — `illingworth2024`
- Canlı doğum %39.8 (212/533) vs %43.5 (232/533); RD −3.9 (−9.9 ile 2.2); P=0.24 — `illingworth2024`
- Taze transfer klinik gebelik %48.1 (154/320) vs %44.5 (157/353) — `illingworth2024`
- Freeze-all klinik gebelik %49.5 (94/190) vs %61.3 (100/163); etkileşim P=0.022 — `illingworth2024`
- SelecTIMO 12 aylık kümülatif canlı doğum %48.7 / %48.4 / %48.2 (yedek) — `selectimo_cea2026`

**Sunucu notu** (136 sözcük, 65 sn; duraklamaya pay var):
Önce asıl soruyu soralım: bu kadar yaygın kullanım daha çok bebek getirdi mi? Ekrandaki her çizgi bir karşılaştırma. Ortadaki dikey çizgi “fark yok” demek. Üstteki üç satır, sekiz randomize çalışmanın hasta düzeyindeki verisini birleştiren 2026 meta-analizinden geliyor: 5 642 hasta, yüksek kesinlik ve canlı doğumda klinik olarak önemli bir fark yok. Bir şeye dikkat edin: bunlar time-lapse ve morfokinetik algoritmalar, derin öğrenme değil. Derin öğrenmenin bugüne kadarki tek büyük randomize çalışması Illingworth 2024: 14 klinik, 1 066 hasta. Klinik gebelik yüzde 46.5’e karşı 48.2. Çalışma “daha kötü değil” sonucunu bile gösteremedi. Canlı doğum yüzde 39.8’e karşı 43.5. Bir uyarı daha var: freeze-all hastalarında algoritmanın seçtiği embriyolarla gebelik yüzde 49.5, embriyoloğun seçtikleriyle yüzde 61.3. Bu bir alt grup bulgusu, kesin değil. Ama göz ardı da edilmemeli. Kısacası seçim yazılımı, deneyimli bir embriyoloğun seçiminden daha çok bebek getirmiyor.

**Süre (sn):** 65

**Künye satırı:** Bhide ve ark. Hum Reprod Update 2026 (PMID 42955792; IPD-MA, özet) · Illingworth ve ark. Nat Med 2024 (PMID 39122964; RKÇ, tam metin; Vitrolife finansmanı) · freeze-all: önceden belirlenmiş etkileşim analizi, yazarlar tartışmada “post hoc” diyor.

---

### Sahne 3.2: Değişen ne?

**Eylem başlığı:** Değişen bebek sayısı değil: dakikalar, tutarlılık, ilaç

**Ekranda:**
- Sol (kronometre çubukları): “Embriyolog 208.3 sn · Algoritma 21.3 sn (hasta başına, 3 laboratuvar)”
- Sağ üst kart: “Tutarlılık: tek model kendine tutarlı (α 1.00; embriyologlar 0.60). 50 kopya model birbirine değil (W≈0.35).”
- Sağ alt kart: “FSH ~%10 az, MII değişmedi — tarihsel kontrol, tek merkez”

**Görsel / etkileşim önerisi:**
- Sol yarı: iki yatay “kronometre” çubuğu aynı anda dolmaya başlar (ölçek: 1 gerçek saniye = 40 sn).
  - “Algoritma” çubuğu yaklaşık 0.5 sn’de 21.3’te durur.
  - “Embriyolog” çubuğu yaklaşık 5 sn boyunca 208.3’e kadar dolmaya devam eder.
  - Bitişte ±SD bıyıkları belirir: ±18.1 / ±144.7.
  - Altında küçük not: “Fark ~10 kat; klinik sonucu değiştirmedi”.
  - “Tekrar oynat” düğmesi.
- Sağ üst kart (tutarlılık), iki küçük nokta grafiği:
  - (a) Bormann 2020: Cronbach α, embriyologlar 0.60 vs model 1.00.
  - (b) Uyum ölçeği 0–1 üzerinde üç nokta: embriyologlar arası Kendall τ 0.70; embriyolog–YZ 0.53; YZ–YZ 0.47 (Zaninovic 2023). Yanında Thirumalaraju 2025: 50 kopya model W≈0.35.
  - Mesaj: “Bir model kendi içinde tekrarlanabilir; modeller birbirine ve embriyoloğa göre tutarsız.”
- Sağ alt kart (FSH):
  - İki çubuk: toplam FSH 4 654.71 → 4 181.77 IU.
  - Altında MII 11.25 → 11.17.
  - Turuncu “kontrolsüz” rozeti ve “canlı doğum ölçülmedi” etiketi.
- Kartlara tıklanınca künye çekmecesi açılır.

**Sayılar:**
- Değerlendirme süresi 21.3 ± 18.1 sn vs 208.3 ± 144.7 sn, P<0.001; “almost 10-fold reduction”; alt çalışma 3 klinikte — `illingworth2024`
- Aynı embriyoyu seçme oranı %65.8 (344/523) — `illingworth2024` (yedek)
- Cronbach α embriyologlar 0.60, ağ 1.00; tutarlılık %83.92 vs %52.14 / %57.68 — `bormann2020`
- Kendall τ: embriyologlar arası 0.70 (tek görüntü/video ile 0.78), embriyolog–YZ 0.53, YZ–YZ 0.47 — `zaninovic2023`
- 50 kopya CNN: Kendall W ≈ 0.35, kritik hata ≈ %15, AUC ≈ 0.60 — `thirumalaraju2025`
- YZ rehberliğiyle gözlemciler arası uyum: kıdemsiz 0.355 → 0.527, kıdemli 0.440 → 0.524 (simülasyon anketi, 61 embriyolog) — `kim2024` (yedek)
- Toplam FSH 4 654.71 vs 4 181.77 IU (P<.01); başlangıç 443.84 vs 397.09 IU; MII 11.25 vs 11.17 (P=.90); 292 vs 292 — `bixby2025`
- Toplam FSH farkı ≈ −%10.2 (hesaplanmış: 472.94 / 4 654.71) — `bixby2025`
- Prospektif + tarihsel kontrol (n=291): toplam FSH −174.35 IU (P=0.13), MII 12.20 vs 11.24 (P=0.16) — `canon2024` (yedek)

**Sunucu notu** (111 sözcük, 55 sn; kronometre animasyonuna pay var):
Peki değişen ne? Birincisi zaman. Aynı çalışmada üç laboratuvarda kronometre tutuldu. Embriyolog bir hastanın embriyolarını ortalama 208 saniyede değerlendirdi, algoritma 21 saniyede: yaklaşık on kat fark. İkincisi tutarlılık. Tek bir model aynı görüntüye her seferinde aynı puanı veriyor; biz embriyologlar arasında ise belirgin bir değişkenlik var. Ama madalyonun öbür yüzü de var. Aynı mimariyle eğitilmiş elli kopya model, embriyoları birbirinden farklı sıralıyor; uyum katsayısı 0.35 civarında. Yani “yapay zekâ tutarlıdır” sözü yalnızca tek bir model için doğru. Üçüncüsü ilaç. Gerçek dünya verisinde, YZ destekli doz seçimiyle toplam FSH yaklaşık yüzde on daha az kullanıldı ve MII sayısı değişmedi. Ama bu tek merkezli, tarihsel kontrollü bir çalışma ve canlı doğum hiç ölçülmedi.

**Süre (sn):** 55

**Künye satırı:** Illingworth 2024 (PMID 39122964, tam metin) · Bormann 2020 Fertil Steril (PMID 32228880, özet) · Zaninovic 2023 F S Sci (PMID 37820865, özet) · Thirumalaraju 2025 Fertil Steril (PMID 40876725, özet) · Bixby & Miller 2025 F S Rep (PMID 40620368, tam metin; Alife Stim Assist)

---

### Sahne 3.3: Bütün tablo

**Eylem başlığı:** Neye etki ediyor? Kanıtın yönü ve gücü tek panoda

**Ekranda** (tablo hücreleri, aynen; ≈ 40 sözcük):

| Çıktı | Etki | Kanıt |
|---|---|---|
| Canlı doğum, gebelik, düşük | = fark yok | IPD-MA · RKÇ |
| Perinatal güvenlik | = fark yok | RKÇ takibi |
| Gebeliğe kadar süre | ölçülmedi | — |
| Değerlendirme süresi | ↓ ~10 kat | RKÇ alt çalışması |
| Tutarlılık | karışık | retrospektif |
| FSH miktarı | ↓ ~%10 | tarihsel kontrol |
| Maliyet | ↑ | ekonomik analiz |
| Hasta güveni | %46 | anket |
| Beceri kaybı, sorumluluk | ölçülmedi | etik yazın |

**Görsel / etkileşim önerisi:**
- Üç sütunlu pano: Çıktı · Etki rozeti · Kanıt türü rozeti.
- Etki rozeti renkleri (lejant ekranda):
  - gri “=” → fark yok
  - yeşil “↓/↑” → kanıtla gösterilen yarar (yalnız süre)
  - turuncu → işaret var ama kontrolsüz ya da sponsorlu (FSH, tutarlılık)
  - kırmızı → olumsuz (maliyet artışı)
  - kesik çerçeveli boş → ölçülmedi
- Kanıt türü rozetinin doluluğu tasarımın gücünü gösterir: IPD-MA ve RKÇ dolu, ekonomik analiz ve RKÇ takibi yarı dolu, tarihsel kontrol, retrospektif, anket ve etik yazın boş çerçeve.
- Pano üç tıklamada açılır:
  - (1) Klinik: ilk 3 satır.
  - (2) Laboratuvar, ilaç ve maliyet: 4.–7. satır.
  - (3) Hasta ve meslek: son 2 satır.
- Her satıra tıklanınca sağdan “künye çekmecesi” açılır. Çekmecede en güçlü kaynak, sayı, PMID, okuma derinliği ve sponsor bulunur. Metinler aşağıdaki “Etki haritası” tablosundan alınır.
- Kapanışta ana mesaj panonun üstüne iner: “Daha çok bebek getirdiği gösterilmedi; değiştirdiği şey hız ve iş akışı.”
- Stok görsel ve robot/beyin ikonu yok. Rozetler yalnız metin ve şekilden oluşur.

**Sayılar:**
- Düşük ve klinik gebelik TLI’da benzer — `bhide2026`. Derin öğrenmede canlı olmayan intrauterin gebelik benzer (ek tablo, sayı alınmadı) — `illingworth2024`
- Perinatal: ciddi gebelik komplikasyonu RRadj 0.95 (0.65–1.40) ve 1.03 (0.70–1.50); tekil doğum 827 — `selectimo_perinatal2026`
- Gebeliğe kadar süre: Illingworth’te “not assessed”; Yaghi’de “not reported” — `illingworth2024`, `yaghi2026`
- Maliyet: TLE–CON ortalama fark €237 (−35 ile 508); ek bir canlı doğum başına ICER €45 950 — `selectimo_cea2026`
- Hasta: 200 hastanın %46’sı YZ destekli üreme tedavisine güveniyor; anlaşmazlıkta tüm kararlarda hekim tercih ediliyor — `cromack2025`
- Şirket siteleri: 21/21 yarar anlatıyor, risk yazan yok; geliştirme örneklem büyüklüğünü açıklayan 7/21 — `du2026`
- (Yedek) Klinik gebelikte YZ ile morfoloji arasında fark yok: RR 0.99 (0.87–1.12), yalnız 2 çalışma havuzlanabildi — `yaghi2026`

**Sunucu notu** (129 sözcük, 60 sn; panonun açılışına pay var):
Şimdi hepsini tek panoda toplayalım. Gri “fark yok”, yeşil “kanıtla gösterilmiş etki”, turuncu “işaret var ama kontrolsüz”, kesik çerçeve ise “hiç ölçülmemiş” demek. Klinik sonuçlarda tablo gri: canlı doğum, gebelik, düşük ve perinatal güvenlikte fark yok. Gebeliğe kadar geçen süre ise randomize çalışmalarda hiç ölçülmemiş. Laboratuvarda tek yeşil satır var: süre kısalıyor. Maliyette elimizdeki tek ekonomik analiz, time-lapse ve seçim algoritmasının maliyeti artırdığını ve muhtemelen maliyet-etkin olmadığını söylüyor. Hastalar tarafında, iki yüz hastalık bir ankette yalnızca yüzde 46’sı YZ destekli tedaviye güveniyor ve anlaşmazlık olursa hekimi tercih ediyor. Firmaların web sitelerinin hiçbiri risk yazmıyor. Etik tarafta beceri kaybı, sorumluluk ve şeffaflık tanımlanmış ama ölçülmemiş riskler. Özetle: yapay zekânın daha çok bebek getirdiği gösterilmedi; değiştirdiği şey hız ve iş akışı. Peki ne kadar doğru? Bu da bir sonraki bölümün sorusu.

**Süre (sn):** 60

**Künye satırı:** Bhide 2026 (PMID 42955792) · Kieslinger 2026 perinatal (PMID 41139424) ve maliyet-etkinlik (PMID 42130487) · Cromack 2025 JARG (PMID 39776390) · Du & Zhang 2026 HRO (PMID 42923733) · Koplin 2025 Hum Reprod (PMID 39657965). Tümü özet düzeyinde.

**Toplam süre:** 65 + 55 + 60 = 180 sn.

---

## Etki haritası (ayrıntılı; sahne 3.3 çekmecelerinin ve soru-cevabın kaynağı)

| # | Etki türü | Yön | En güçlü kanıt (tasarım) | Sayı | Kesinlik / uyarı |
|---|---|---|---|---|---|
| 1a | Canlı doğum | Fark yok | Bhide 2026 IPD-MA, 8 RKÇ, n=5 642 | aOR 0.97 / 1.02 / 0.92 (GA’lar 1’i içeriyor) | Yazarlar: “high-certainty”. Ama TLI/morfokinetik için; derin öğrenme değil. |
| 1b | Canlı doğum (derin öğrenme) | Fark gösterilemedi, sayısal olarak düşük | Illingworth 2024 RKÇ | %39.8 vs %43.5, RD −3.9 (−9.9 ile 2.2) | Tek RKÇ; Vitrolife finansmanı; canlı doğum ikincil sonlanım |
| 1c | Klinik gebelik | Fark yok; non-inferiority gösterilemedi | Illingworth 2024 RKÇ; Yaghi 2026 MA | RD −1.7 (−7.7 ile 4.3); RR 0.99 (0.87–1.12) | Yaghi’de yalnız 2 çalışma havuzlanabildi |
| 1d | Freeze-all alt grubu | Olası zarar sinyali | Illingworth 2024 (alt grup) | %49.5 vs %61.3; etkileşim P=0.022 | Alt grup; yazarlar “şans olabilir” diyor |
| 1e | Düşük, biyokimyasal kayıp | Fark yok | Bhide 2026 | “similar” (sayı yok) | TLI için |
| 1f | Gebeliğe kadar süre | Ölçülmedi (RKÇ) | — | EMBRYOLY retrospektif simülasyon: 2.01 → 1.66 siklus (“could have”) | RKÇ kanıtı yok. Simülasyon, gerçek kullanım değil. Slayta konmadı. |
| 1g | Perinatal güvenlik | Fark yok | SelecTIMO takip, RKÇ (Kieslinger 2026) | RRadj 0.95 (0.65–1.40); doğum ağırlığı MD 34 g (−62 ile 129) | Tek sistem (EEVA, 3. gün ML algoritması) |
| 1h | Cinsiyet oranı | Fark yok | Illingworth 2024 | erkek %53.5 vs %58.6, P=0.32 | — |
| 1i | Oosit/sperm YZ → klinik sonuç | RKÇ yok | SiD kardeş-oosit (Montjean 2024); otomatik ICSI pilot (Chavez-Badiola 2026) | SiD: 646 MII, anlamsız eğilim; ICSI: döllenme %64.3 vs %81 (manuel), 11 olgu | Canlı doğumu sonlanım alan RKÇ bulunamadı; ICSI pilotu sponsorlu |
| 2a | Değerlendirme süresi | ~10 kat kısa | Illingworth 2024, RKÇ içi alt çalışma | 21.3 ± 18.1 vs 208.3 ± 144.7 sn | 3 klinik. Süre ölçümü dosyanın açılışından seçime kadar. İş yükü/FTE ölçülmedi. |
| 2b | Tutarlılık (aynı model) | Yüksek | Bormann 2020 (retrospektif veri, prospektif kör değerlendirme) | α 1.00 vs 0.60 | Deterministik modelden beklenen sonuç |
| 2c | Uyum (embriyolog ↔ YZ ↔ YZ) | Düşük–orta | Zaninovic 2023; Thirumalaraju 2025 | τ 0.70 / 0.53 / 0.47; W≈0.35 | Retrospektif |
| 2d | YZ rehberliğinde gözlemciler arası uyum | Artış | Kim 2024 JMIR (simülasyon anketi) | 0.355 → 0.527 (kıdemsiz) | Gerçek klinik karar değil |
| 2e | Aynı embriyoyu seçme | ~2/3 | Illingworth 2024; Harir 2025 | %65.8; %64.6 | — |
| 2f | Standardizasyon | Varsayım | Dirican 2026 derleme: “workflow standardization rather than improved clinical outcome” | — | Yorum; ölçülmüş bir sonlanım değil |
| 3 | Maliyet | Artış; muhtemelen maliyet-etkin değil | SelecTIMO maliyet-etkinlik (RKÇ’ye dayalı) | €237 (−35 ile 508); ICER €45 950 | TLM + 3. gün ML; derin öğrenme için maliyet-etkinlik analizi bulunamadı |
| 4a | FSH miktarı | ~%10 az | Bixby & Miller 2025 (gerçek dünya, tarihsel kontrol) | 4 654.71 → 4 181.77 IU; MII 11.25 → 11.17 | Kontrolsüz zaman eğilimi; canlı doğum yok; ilaç maliyeti hesaplanmadı |
| 4b | FSH + MII (prospektif) | Anlamsız eğilim | Canon 2024 Sci Rep (n=291 + tarihsel kontrol) | −174.35 IU (P=0.13); MII +0.96 (P=0.16) | Alife yazarlar |
| 4c | RKÇ | Sonuç yok | IDoser protokolü (Trials 2024), n=236 planlandı | — | Yayımlanmış sonuç bulunamadı |
| 4d | Kapsam taraması | Az kanıt | Lu 2026 scoping review: 5 çalışma, n=16 441 | −195 IU, +1.5 MII (tek çalışma); gebelik sonucu bildirilmemiş | — |
| 5a | Hasta güveni | Sınırlı | Cromack 2025 anket, n=200 | %46 güven; hekim tercihi | Tek merkez, eğitim düzeyi yüksek örneklem |
| 5b | Hasta ve profesyonel görüşü | Güvensizlik, açıklama talebi | Webb 2026 nitel (10+10 görüşme) | — | Avustralya |
| 5c | Hastaya bilgi kalitesi | Olumsuz | Du & Zhang 2026, 21 şirket sitesi | Risk yazan 0/21 | — |
| 5d | LLM danışmanlığı | Kısmen doğru | Chervenak 2023 | 147 ifadeden 9’u (%6.12) yanlış | ChatGPT Şubat 2023 sürümü |
| 5e | Prognoz danışmanlığı | Model metrikleri daha iyi | Yao 2025 Nat Commun (Univfy) | — (klinik sonuç yok) | Yazarlar Univfy bağlantılı |
| 6a | Etik riskler | Tanımlı, ölçülmemiş | Koplin 2025; Afnan 2021 | İnsanlıktan uzaklaştırma, yanlılık, sorumluluk, şeffaflık, beceri kaybı, adalet | Kavramsal |
| 6b | Meslek | Rol değişimi | Palmer 2024 (702 embriyolog); Dirican 2026 | “verification, exception-handling, and quality oversight” | — |
| 6c | Kurumsal görüş | Temkin | ASRM 2026; ESHRE 2023 | ESHRE: 42 önerinin hiçbiri yüksek kaliteli kanıta dayanmıyor | ASRM yalnız özet |

**Gözlemciler arası uyum (kappa) sorusunun cevabı:** Ölçülmüş, ama yalnız retrospektif ya da simülasyon tasarımlarda.
- Embriyologlar arası κ: 0.56 (Fordham 2022) ve 0.3–0.4 (Toschi 2024).
- YZ rehberliğiyle uyum artışı: 0.355 → 0.527 (Kim 2024).
- Gelişim evresi sınıflamasında evre bazlı uyum embriyologlar arasında DL modellerinden yüksek: 0.778–0.952 vs 0.385–0.681 (Kakulavarapu 2026).
- Prospektif klinik ortamda, YZ kullanımının laboratuvarın gözlemciler arası uyumunu değiştirdiğini ölçen bir RKÇ **bulunamadı**.

---

## Kaynaklar

| Anahtar | Künye | PMID | DOI | Okuma | Tasarım | Sponsor / çıkar çatışması |
|---|---|---|---|---|---|---|
| illingworth2024 | Illingworth PJ ve ark. Deep learning versus manual morphology-based embryo selection in IVF. Nat Med 2024 | 39122964 (PMC11564097) | 10.1038/s41591-024-03166-5 | tam metin | Çok merkezli, çift kör, non-inferiority RKÇ; 14 klinik | Vitrolife finansmanı; sponsor çalışanları tasarıma ve yazıma katıldı |
| bhide2026 | Bhide P ve ark. Does time-lapse imaging of embryos improve reproductive outcomes? IPD meta-analysis. Hum Reprod Update 2026 | 42955792 | 10.1093/humupd/dmag035 | özet | IPD meta-analizi, 8 RKÇ | Özette beyan yok |
| selectimo_lancet2023 | Kieslinger DC ve ark. SelecTIMO. Lancet 2023 | 37004670 | 10.1016/S0140-6736(23)00168-X | özet | Üç kollu RKÇ, 15 klinik, n=1 731 | ZonMw ve Merck |
| selectimo_cea2026 | Kieslinger DC ve ark. Cost-effectiveness of time-lapse monitoring… Hum Reprod Open 2026 | 42130487 (PMC13167187) | 10.1093/hropen/hoag034 | özet | RKÇ’ye dayalı maliyet-etkinlik analizi | ZonMw; Merck inkübatör sağladı |
| selectimo_perinatal2026 | Kieslinger DC ve ark. Obstetric and perinatal outcomes… Hum Reprod 2026 | 41139424 (PMC12769441) | 10.1093/humrep/deaf197 | özet | RKÇ takibi | ZonMw; Merck |
| yaghi2026 | Yaghi ve ark. Impact of AI in embryo selection… Eur J Obstet Gynecol Reprod Biol 2026 | 42914619 | 10.1016/j.ejogrb.2026.115495 | özet | Sistematik derleme ve MA (10 çalışma; 2’si havuzlandı) | Özette beyan yok |
| eshre2023 | ESHRE Add-ons Working Group. Good practice recommendations on add-ons. Hum Reprod 2023 | 37747409 (PMC10628516) | 10.1093/humrep/dead184 | özet (önceki oturumda tam metin) | İyi uygulama önerisi | ESHRE fonu; bazı yazarların Vitrolife, Alife bağlantısı var |
| asrm2026 | ASRM Practice Committee. AI in the IVF laboratory: a committee opinion. Fertil Steril 2026;126(3):494–8 | 42285874 | 10.1016/j.fertnstert.2026.05.004 | yalnız özet (tam metin erişilemedi) | Komite görüşü | — |
| kieslinger2024 | Kieslinger DC, Lambalk CB, Vergouw CG. The inconvenient reality of AI-assisted embryo selection in IVF. Nat Med 2024 | 39354198 | 10.1038/s41591-024-03289-9 | web: yalnız giriş cümlesi (ücretli) | Yorum | SelecTIMO yazarları (ZonMw, Merck) |
| bormann2020 | Bormann CL ve ark. Consistency and objectivity of automated embryo assessments using deep neural networks. Fertil Steril 2020 | 32228880 (PMC7583085) | 10.1016/j.fertnstert.2019.12.004 | özet | Retrospektif veriyle prospektif kör değerlendirme | NIH ve diğer |
| zaninovic2023 | Zaninovic N ve ark. Embryo ranking agreement between embryologists and AI algorithms. F S Sci 2023 | 37820865 | 10.1016/j.xfss.2023.10.002 | özet | Retrospektif, 100 siklus, 5 embriyolog, 8 algoritma | Özette yok |
| thirumalaraju2025 | Thirumalaraju P ve ark. Stability and reliability of AI models in embryo selection. Fertil Steril 2025 | 40876725 (PMC12494150) | 10.1016/j.fertnstert.2025.08.021 | özet | Laboratuvar çalışması, 50 kopya CNN, 2 merkez | — |
| kim2024 | Kim ve ark. Evaluation of the clinical efficacy and trust in AI-assisted embryo ranking. J Med Internet Res 2024 | 38830209 (PMC11184268) | 10.2196/52637 | özet | Anket tabanlı simülasyon, 61 embriyolog, 12 klinik | — |
| fordham2022 | Fordham DE ve ark. Embryologist agreement when assessing blastocyst implantation probability. Hum Reprod 2022 | 35944167 | 10.1093/humrep/deac171 | özet | Retrospektif; 36 embriyolog | Embryonics Ltd (şirket) |
| toschi2024 | Toschi ve ark. AI with genetic algorithms… Int J Fertil Steril 2024 | 39564830 (PMC11589968) | 10.22074/ijfs.2024.2008339.1510 | özet | Retrospektif, 223 görüntü | — |
| kakulavarapu2026 | Kakulavarapu ve ark. Discrepancies in accuracy, agreement and interpretability… Front Reprod Health 2026 | 41928854 (PMC13040276) | 10.3389/frph.2026.1778326 | özet | Retrospektif, tek merkez, 245 görüntü | — |
| harir2025 | Harir ve ark. Embryologist versus AI in embryo selection. In Vitro Cell Dev Biol Anim 2025 | 40751026 | 10.1007/s11626-025-01099-y | özet | Retrospektif, 82 siklus | — |
| dissler2024 | Dissler ve ark. AI-powered assisted ranking of sibling embryos. RBMO 2024 | 38701632 | 10.1016/j.rbmo.2024.103887 | özet | Retrospektif simülasyon (EMBRYOLY) | Muhtemelen şirket bağlantılı (DOĞRULANAMADI) |
| bixby2025 | Bixby CJ, Miller B. Real-world use of an AI-powered clinical decision support tool for ovarian stimulation. F S Rep 2025 | 40620368 (PMC12223591) | 10.1016/j.xfre.2025.01.015 | tam metin | Retrospektif kohort, eşleştirilmiş tarihsel kontrol, tek merkez | Yazarlar “nothing to disclose”; ürün Alife Stim Assist |
| canon2024 | Canon C ve ark. Optimizing oocyte yield utilizing a ML model for dose and trigger decisions. Sci Rep 2024 | 39164339 (PMC11335759) | 10.1038/s41598-024-69165-1 | özet | Prospektif + tarihsel kontrol, 2 merkez | Alife bağlantılı yazarlar (ortak bağlam) |
| fanton2022 | Fanton M ve ark. An interpretable ML model for individualized gonadotrophin starting dose selection. RBMO 2022 | 36096871 | 10.1016/j.rbmo.2022.07.010 | özet | Retrospektif, n=18 591 | Alife (ortak bağlam) |
| idoser2024 | Correa N ve ark. Personalizing the first dose of FSH… study protocol. Trials 2024 | 38212837 (PMC10782678) | 10.1186/s13063-024-07907-2 | özet | RKÇ protokolü (n=236) | — |
| lu2026 | Lu ve ark. Clinical decision support models to optimize COH: scoping review. Clin Transl Sci 2026 | 42876358 (PMC13670003) | 10.1111/cts.70742 | özet | Kapsam taraması | — |
| montjean2024 | Montjean D ve ark. Automated single-sperm selection software (SiD) during ICSI. Med Sci (Basel) 2024 | 38651413 (PMC11036211) | 10.3390/medsci12020019 | özet | Prospektif kardeş-oosit | — |
| chavezbadiola2026 | Chavez-Badiola A ve ark. Automated oocyte retrieval, denudation, sperm preparation, and ICSI. Hum Reprod 2026 | 41453368 (PMC12957933) | 10.1093/humrep/deaf240 | özet | Kavram kanıtı pilotu, 11 olgu | Conceivable Life Sciences sponsorlu; çok sayıda patent |
| cromack2025 | Cromack SC ve ark. The perception of AI and infertility care among patients. J Assist Reprod Genet 2025 | 39776390 (PMC11950478) | 10.1007/s10815-024-03382-5 | özet | Kesitsel anket, n=200 | — |
| webb2026 | Webb ANS ve ark. Two sides of the same algorithm. J Assist Reprod Genet 2026 | 42303882 (PMC13598045) | 10.1007/s10815-026-03932-z | özet | Nitel, 10 profesyonel ve 10 hasta | — |
| du2026 | Du L, Zhang Y. AI-assisted IVF company websites. Hum Reprod Open 2026 | 42923733 (PMC13690092) | 10.1093/hropen/hoag086 | özet | İçerik analizi, 21 şirket | Çıkar çatışması yok |
| chervenak2023 | Chervenak J ve ark. The promise and peril of using a LLM… ChatGPT. Fertil Steril 2023 | 37217092 | 10.1016/j.fertnstert.2023.05.151 | özet | Karşılaştırmalı değerlendirme | — |
| yao2025 | Yao MWM ve ark. ML center-specific models… Nat Commun 2025 | 40246850 (PMC12006386) | 10.1038/s41467-025-58744-z | özet | Retrospektif model doğrulama, 6 merkez | Univfy yazarlar |
| koplin2025 | Koplin JJ ve ark. Ethics of AI in embryo assessment: mapping the terrain. Hum Reprod 2025 | 39657965 (PMC11788194) | 10.1093/humrep/deae264 | özet | Mini derleme | — |
| afnan2021 | Afnan MAM ve ark. Interpretable, not black-box, AI should be used for embryo selection. Hum Reprod Open 2021 | 34938903 (PMC8687137) | 10.1093/hropen/hoab040 | özet | Görüş / derleme | — |
| palmer2024 | Palmer GA ve ark. Use and understanding of AI in the ART laboratory: an international survey. RBMO 2024 | 39939196 | 10.1016/j.rbmo.2024.104435 | özet | Anket, 702 embriyolog | Yazarlar IVF 2.0 ve Conceivable bağlantılı |
| dirican2026 | Dirican EK. Automation in the IVF laboratory in 2026. J Assist Reprod Genet 2026 | 42337202 (PMC13598027) | 10.1007/s10815-026-03946-7 | özet | Anlatı derlemesi | — |
| cimadomo2026co | Cimadomo D, Coticchio G, Rienzi L. AI in human-assisted reproduction: a paradigm shift still in search of clinical impact. Curr Opin Obstet Gynecol 2026 | 41621090 | 10.1097/GCO.0000000000001092 | özet | Derleme | — |

---

## Doğrulanamayanlar ve uyarılar

**DOĞRULANAMADI / bulunamadı**
- **Bhide 2026’nın içindeki çalışmalar:** “Morfokinetik seçim” kolundaki 3 RKÇ’nin Illingworth 2024’ü (iDAScore) içerip içermediği özetten anlaşılamıyor. Tam metin PMC’de yok. İçeriyorsa ormandaki iki grup bağımsız değildir; bu yüzden ayrı başlıklar altında gösterildi.
- **ASRM 2026 komite görüşü:** Yalnız özet okundu (“caution is recommended in interpreting the retrospective data”). Tam metne erişilemedi (Elsevier yönlendirmesi). Öneri maddeleri slayta konmadı.
- **Kieslinger 2024 Nat Med yorumu:** Gövde metni ücretli. Yalnız giriş cümlesi görüldü: “the inflated expectations of new technologies are not always justified”. Okuma derinliği: web, giriş cümlesi. Slayta konmadı. Soru-cevapta kullanılacaksa bu sınır söylenmeli.
- **Derin öğrenmeyle embriyo seçiminin maliyet-etkinliği:** Analiz bulunamadı. SelecTIMO’nun maliyet analizi TLM ile 3. gün ML algoritmasına (EEVA) ait.
- **Gebeliğe kadar süre ve kümülatif canlı doğum (derin öğrenme):** RKÇ verisi yok. Illingworth bunları ölçmedi; Yaghi “not reported” diyor.
- **İş yükü, personel zamanı, FTE:** Süre dışında iş yükünü ölçen prospektif bir çalışma bulunamadı. “21 sn × günlük hasta sayısı” gibi bir hesap slayta konmamalı; tahmin olur.
- **Oosit veya sperm YZ’si için canlı doğumu sonlanım alan RKÇ:** Bulunamadı.
- **IDoser RKÇ sonucu:** PubMed’de yayımlanmış sonuç bulunamadı.
- **Prospektif klinik kullanımda gözlemciler arası uyum değişimi:** RKÇ bulunamadı. Mevcut kappa değerleri retrospektif ya da simülasyon çalışmalarından.
- **Dissler 2024 (EMBRYOLY) sponsor bilgisi:** Özette yok.
- **Bhide 2026 sponsor ve çıkar çatışması:** Özette yok.

**Yorum uyarıları**
- **Freeze-all bulgusunun statüsü:** Illingworth makalesi kendi içinde çelişkili. Sonuçlarda “prespecified interaction analysis” (P=0.022), tartışmada “observational post hoc analysis” deniyor. Ortak bağlamdaki “post hoc” etiketi makalenin bir yerindeki ifadeyle uyumlu. Slaytta “alt grup analizi” denmesi önerilir.
- **Illingworth birincil sonlanımı:** Birincil sonlanım klinik gebelik; canlı doğum ikincil. Kontrol grubunun gebelik oranı beklenenden (%35.4) yüksek çıktı (%48.2) ve bu gücü düşürdü. Yazarlar non-inferiority için yaklaşık 7 800 katılımcı gerektiğini hesaplıyor (tam metin).
- **Süre ölçümü:** Bir hastanın embriyo dosyasını açmaktan seçime kadar geçen süre. 3 klinikteki alt çalışmadan geliyor (güç hesabında en az 51 hasta). Bütün laboratuvar iş akışı değil.
- **FSH −%10:** Yüzde makalede yazmıyor; ortalamalardan biz hesapladık (472.94 / 4 654.71 = %10.16). Ölçüm tarihsel kontrollü: AI dönemi 2022–2023, kontrol dönemi 2019–2022. Zaman eğilimi ve hekimin öğrenmesi karıştırıcı. Eşleştirme yerine koymalı (with replacement). Hastaların %17’sinde AMH/AFC eksik ve doldurulmuş. Sınırlılıklar sunucu notunda “tarihsel kontrol, tek merkez” olarak söyleniyor.
- **“Tutarlılık” iddiası:** Bormann 2020’deki α=1.00, deterministik bir modelin aynı girdiye aynı çıktıyı vermesinin beklenen sonucu. Bu, doğruluğun ya da modeller arası uyumun kanıtı değil (Thirumalaraju 2025). Bu ikilik sahne 3.2’de açıkça veriliyor.
- **Bin ayırıcısı:** Ortak bağlam ondalık için nokta istiyor. Ama aynı dosyada bin ayırıcı olarak da nokta kullanılmış (“1.066”, “5.642”). Slaytta karışıklık olmaması için bin ayırıcı olarak dar boşluk (U+202F) önerilir: “1 066”, “5 642”, “4 654.71”. Bu dosyada böyle yazıldı. Kullanıcı onayı gerekir: **[ONUR’A SOR]**.
- **Hasta güveni:** Cromack 2025 tek merkezli ve eğitim düzeyi yüksek bir ABD örneklemi. Türkiye’ye genellenemez.
- **Kapsam:** “Yaygın kullanım” ile ulusal ya da kayıt düzeyindeki sonuçları ilişkilendiren bir analiz bu bölümde taranmadı. Bölümün kanıtı randomize karşılaştırmalara dayanıyor.
