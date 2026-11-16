# Bölüm 1: Yapay zekâ labda hangi aşamalarda kullanılmaya başlandı?

## Tek cümlelik cevap

Yapay zekâ bugün IVF hattının neredeyse her durağına girdi: danışmanlıktan stimülasyona, oosit, sperm ve embriyo değerlendirmesinden ICSI robotuna, KPI izlemeden hasta iletişimine kadar. Ama yayımlanmış randomize kontrollü çalışmayı (RKÇ) yalnız embriyo seçiminde bulduk ve o çalışma da eşdeğerliği gösteremedi. Ticari ürünler kanıtın önünden gidiyor. İvme 2018’de başladı: o yıl ASRM ve ESHRE’deki yapay zekâ bildirisi bir yıl öncekinin sekiz katına çıktı (2 → 16).

---

## Sahneler

### Sahne 1: İş akışı hattı

**Eylem başlığı:** Yapay zekâ hattın her durağında; RKÇ yalnız embriyo seçiminde
(10 sözcük)

**Ekranda** (aynen):
> Danışmanlık · Stimülasyon · Folikül USG · Oosit · Sperm · ICSI · Embriyo seçimi · Ploidi · Endometriyum · Lab KPI · Kriyo · Hasta iletişimi
> Rozet: RKÇ / prospektif / retrospektif / kavram kanıtı / kanıt yok
> Olgunluk: araştırma · ticari · rutin

(31 sözcük)

**Görsel / etkileşim önerisi:**
- Soldan sağa yatay bir **hat** çiziliyor; 12 durak hastanın yolculuk sırasıyla diziliyor. Durakların rengi olgunluğu gösteriyor: gri = araştırma, mavi = ticari, koyu = rutin. Her durağın altında bir **kanıt rozeti** var; şekli tasarımı gösteriyor (dolu kare = RKÇ, dolu daire = prospektif, içi boş daire = retrospektif, üçgen = kavram kanıtı, çizgi = kanıt yok). Renk tek başına bilgi taşımıyor, şekil ve etiket de aynı bilgiyi veriyor.
- Bir durağa **dokununca** kart açılıyor (metinler aşağıdaki tabloda): *Amaç*, *Örnek araç*, *En güçlü kanıt* (rozet ve tek sayı), *Künye*. Kartta en fazla 30 sözcük var.
- **Önerilen ikinci görünüm (daha güçlü):** sağ üstteki “Hat / Matris” düğmesi aynı 12 durağı bir **olgunluk × kanıt matrisine** taşıyor (x: araştırma → ticari → rutin; y: kanıt yok → kavram kanıtı → retrospektif → prospektif → RKÇ). Noktalar animasyonla yerine kayıyor. Matrisin sağ alt köşesinin, yani “ticari ama kanıtı zayıf” bölgesinin dolu olduğu tek bakışta görülüyor: folikül USG, oosit, stimülasyon. Sağ üstteki tek nokta embriyo seçimi; yanında “eşdeğerlik gösterilemedi” notu duruyor. Bölüm 3–4’e geçişi bu görüntü hazırlıyor.
- Robot ya da beyin ikonu ve stok görsel kullanılmıyor. Duraklar yalnız metin etiketi ve basit geometrik şekillerle gösteriliyor.

**Kart içerikleri (aşama haritası):**

| # | Durak | Amaç (YZ ne için?) | Örnek araç | Olgunluk | En güçlü kanıt tasarımı | Kartta tek sayı | Kaynak |
|---|---|---|---|---|---|---|---|
| 1 | Danışmanlık / prognoz | Kişiye özel canlı doğum olasılığı | Univfy (merkeze özgü ML) | Ticari | Retrospektif dış doğrulama, 6 merkez | 4.635 hasta | yao_2025 |
| 2 | Stimülasyon | FSH başlangıç dozu ve tetik günü önerisi | Alife (Stim Assist), IDoser | Ticari | Prospektif + tarihsel kontrol; RKÇ yalnız protokol | MII 12.20 vs 11.24, p = 0.16 | canon_2024, correa_2024 |
| 3 | Folikül USG | Folikülleri otomatik sayıp ölçmek | MIM Fertility (FOLLISCAN) | Ticari | Retrospektif çok merkezli + prospektif gerçek dünya kohortu | ≥10 mm F1 %93.3 | wygocki_2026 |
| 4 | Oosit | MII oositin blastokiste gelişme şansı | MAGENTA (Future Fertility) | Ticari | Prospektif gözlemsel, 3 merkez | AUC 0.6 (1.179 donör oositi) | cimadomo_2025 |
| 5 | Sperm | Analiz: otomatik sayım ve motilite. Seçim: ICSI için tek sperm | Otomatik semen analizörleri; SiD | Analiz rutin*, seçim araştırma | Prospektif kardeş oosit (seçim) | 646 MII; fark anlamsız | montjean_2024, mcculloh_2026 |
| 6 | ICSI otomasyonu | Enjeksiyon adımlarını robota ya da uzaktan kumandaya devretmek | ICSIA robotu; Conceivable “pearl” sistemleri | Araştırma | Kavram kanıtı | 11 olgu, 5 canlı doğum | chavez_badiola_2026 |
| 7 | Embriyo seçimi | Transfer sırası için puanlama ve sıralama | iDAScore, CHLOE, Life Whisperer, Alife Embryo Predict | Ticari (yardımcı) | **RKÇ**, 14 klinik | 1.066 hasta; %46.5 vs %48.2 | illingworth_2024 |
| 8 | Ploidi tahmini | Biyopsi yapmadan öploidi tahmini | STORK-A, BELA | Araştırma | Retrospektif; tanısal meta-analiz | AUC 0.80 (12 çalışma) | xin_2024, rajendran_2024 |
| 9 | Endometriyum / transfer | USG radyomik ile FET sonrası gebelik tahmini | Akademik modeller | Araştırma | Prospektif kohort (tek merkez) | AUC 0.825 (n = 240) | liang_2023 |
| 10 | Lab KPI / kalite kontrol | Kültür koşulu ve embriyolog performansında erken uyarı | CNN tabanlı izleme | Araştırma | Retrospektif kavram kanıtı | (sayı yok; Vienna KPI’ları: ICSI fert, D3 kalite) | bormann_2021 |
| 11 | Kriyo izleme | Tank arızasını ısınmadan önce yakalamak | Sensör: vakum, ağırlık, sıcaklık (YZ değil) | YZ için kanıt yok | Deneysel simülasyon, tek tank | (YZ sayısı yok) | allen_2026 |
| 12 | Hasta iletişimi / LLM | Hasta sorularını yanıtlamak, danışmanlık, psikososyal destek | ChatGPT; tıbbi LLM’ler | Araştırma | Kesitsel değerlendirme; randomize olmayan fizibilite | 147 ifadeden 9’u hatalı (%6.12) | chervenak_2023 |

\* Otomatik semen analizörleri rutinde kullanılıyor, ama bu araçların çoğu klasik görüntü işlemeye dayanıyor, derin öğrenmeye değil. McCulloh 2026’ya göre bu analizörler “ön değerlendirme” için uygun; nitelikli manuel analizin tek başına yerini tutmuyorlar.

**Sayılar** (anahtarlar `01_sayilar.json`’da):
`yao_2025_hasta` 4635 · `yao_2025_merkez` 6 · `canon_2024_n` 291 · `canon_2024_mii_yz` 12.20 · `canon_2024_mii_kontrol` 11.24 · `canon_2024_p` 0.16 · `correa_2024_planlanan_n` 236 · `wygocki_2026_tarama` 5508 · `wygocki_2026_f1_10mm` 93.3 · `wygocki_2026_sure_kat` 2.5 · `cimadomo_2025_oosit` 1179 · `cimadomo_2025_auc` 0.6 · `montjean_2024_mii` 646 · `chavez_badiola_2026_olgu` 11 · `chavez_badiola_2026_canli_dogum` 5 · `chavez_badiola_2026_fert_oto` 64.3 · `chavez_badiola_2026_fert_manuel` 81 · `illingworth_2024_hasta` 1066 · `illingworth_2024_klinik` 14 · `illingworth_2024_gebelik_yz` 46.5 · `illingworth_2024_gebelik_morf` 48.2 · `xin_2024_calisma` 12 · `xin_2024_auc` 0.80 · `rajendran_2024_auc` 0.76 · `liang_2023_n` 240 · `liang_2023_auc` 0.825 · `chervenak_2023_ifade` 147 · `chervenak_2023_hatali` 9 · `chervenak_2023_hatali_yuzde` 6.12 · `liu_2026_halusinasyon_grpo` 15 · `liu_2026_halusinasyon_sft` 18.5 · `lee_2026_n` 37

**Sunucu notu** (≈ 150 sözcük):
Bir IVF siklusunu baştan sona bir hat gibi düşünelim. Bugün bu hattın neredeyse her durağında bir yapay zekâ uygulaması var. İlk görüşmede canlı doğum olasılığını hesaplayan modeller var. Stimülasyonda FSH dozunu ve tetik gününü öneren araçlar, ultrasonda folikülleri sayıp ölçen yazılımlar var. Laboratuvarda oositi fotoğrafından puanlayan, spermi seçen ve ICSI’yi robota yaptıran sistemler; embriyoyu sıralayan, hatta biyopsi yapmadan ploidiyi tahmin etmeye çalışan modeller var. Transfer tarafında endometriyum görüntüsünden gebelik tahmini, arka planda KPI’lar için erken uyarı, ön tarafta da hastaya yanıt veren dil modelleri var. Ama rozetlere bakın. Yayımlanmış randomize çalışmayı yalnız embriyo seçiminde bulduk. O çalışma da bin altmış altı hastada eşdeğerliği gösteremedi. Folikül sayımı ve oosit puanlaması ticari ürün oldu, ama kanıtları gözlemsel. ICSI robotu hâlâ kavram kanıtı aşamasında. Kriyo tanklarında ise konuşulan şey yapay zekâ değil, sensörle izleme. Yani doğru soru “nerede kullanılıyor” değil, “hangi durakta, ne kadar kanıtla kullanılıyor”.

**Süre (sn):** 66

**Künye satırı:**
Yao 2025 Nat Commun · Canon 2024 Sci Rep · Wygocki 2026 JARG · Cimadomo 2025 Hum Reprod · Montjean 2024 Med Sci · Chavez-Badiola 2026 Hum Reprod · Illingworth 2024 Nat Med · Xin 2024 eClinMed · Liang 2023 RBMO · Bormann 2021 JARG · Allen 2026 JARG · Chervenak 2023 Fertil Steril. Olgunluk sınıflaması bizim değerlendirmemizdir.

---

### Sahne 2: “İlkler” zaman çizgisi

**Eylem başlığı:** Otuz yılda tahminden robota; kırılma 2018–2019’da geldi
(9 sözcük)

**Ekranda** (aynen):
> 1997 sinir ağıyla IVF tahmini · 2010 kişiye özel canlı doğum modeli · 2018 kongrede 2 → 16 bildiri · 2019 derin öğrenme embriyoda · 2023 ilk otomatik ICSI bebekleri · 2024 ilk büyük RKÇ · 2025 uzaktan ICSI doğumu · 2025 FDA 510(k)*
> *ikincil kaynak

(40 sözcük)

**Görsel / etkileşim önerisi:**
- 1997’den 2026’ya uzanan yatay bir zaman ekseni ve üç **şerit** var: **Yayın** (model ve doğruluk), **Klinik ilk** (bebek ya da hasta), **Düzenleyici** (FDA, CE). Ölçek doğrusal; 1997–2017 arasındaki uzun boşluk bilinçli olarak görünür bırakıldı, çünkü 2018’den sonraki yığılmayı o boşluk anlatıyor.
- PubMed’de doğrulanan olaylar **dolu nokta**, yalnız ikincil kaynakta geçen olaylar **içi boş nokta** ve “ikincil kaynak” etiketiyle gösteriliyor (FDA 510(k) Eylül 2025, CE Ekim 2025).
- 2017 ve 2018’in üstünde küçük bir **çubuk çifti** var: ASRM ve ESHRE’deki yapay zekâ/ML bildirileri 2 ve 16. Bu “kırılma” anını sayıyla gösteriyor.
- Noktaya dokununca tek satırlık bilgi açılıyor: olay, sayı, künye. Örneğin “2019 · IVY · 10.638 embriyo, 8 klinik · Tran, Hum Reprod”.
- Sunum akışında noktalar soldan sağa sırayla yanıyor; şerit renkleri sahne 1’deki aşama renkleriyle eşleşiyor (embriyo = embriyo seçimi rengi vb.).

**Zaman çizgisi (yalnız PubMed’de doğrulanan olaylar dolu nokta):**

| Yıl | Şerit | Olay | Tek sayı | Kaynak | Durum |
|---|---|---|---|---|---|
| 1997 | Yayın | Yapay sinir ağı IVF sonucunu dört değişkenle tahmin ediyor (PubMed’de bulduğumuz en erken örnek) | Doğruluk %59 | kaufmann_1997 | Doğrulandı (özet) |
| 2010 | Yayın | Kişiye özel canlı doğum tahmini (boosted tree) | AUC 0.80 vs yaşa dayalı 0.68 | banerjee_2010 | Doğrulandı (özet) |
| 2018 | Yayın | ASRM ve ESHRE’de YZ/ML bildirisi: 2017’de 1 + 1 → 2018’de 9 + 7 | 2 → 16 | curchoe_2019 | Doğrulandı (özet) |
| 2019 | Yayın | Derin öğrenme blastokist görüntülerinde: STORK (~50.000 görüntü), IVY (10.638 embriyo, 8 klinik) | IVY AUC 0.93 (çapraz doğrulama) | khosravi_2019, tran_2019 | Doğrulandı (özet) |
| 2020 | Yayın | Statik mikroskop görüntüsünden canlılık (Life Whisperer); stimülasyonda günlük karar desteği | Durdur/devam doğruluğu 0.92 | vermilyea_2020, letterie_2020 | Doğrulandı (özet) |
| 2021 | Yayın | Lab KPI’ları için derin öğrenmeyle erken uyarı | (sayı yok) | bormann_2021 | Doğrulandı (özet) |
| 2023 | Yayın | Biyopsisiz ploidi tahmini (STORK-A) | Test AUC 0.737 | barnes_2023 | Önceki oturumda doğrulandı |
| 2023 | Klinik ilk | Otomatik ICSI (ICSIA) ile ilk bebekler | 2 bebek; döllenme 13/14 vs 16/18 | costa_borges_2023 | Doğrulandı (özet) |
| 2023 | Yayın | ChatGPT doğurganlık sorularında ilk sistematik değerlendirme | 147 ifadeden 9’u hatalı | chervenak_2023 | Doğrulandı (özet) |
| 2024 | Klinik ilk | Derin öğrenmeyle embriyo seçiminin ilk büyük RKÇ’si | 1.066 hasta, 14 klinik | illingworth_2024 | Doğrulandı (özet) |
| 2024 | Yayın | Oosit görüntüsünden derin öğrenme (MAGENTA modeli) | 37.133 görüntü; dış AUC 0.63 | fjeldstad_2024 | Doğrulandı (özet) |
| 2025 | Klinik ilk | Uzaktan kumandalı ICSI ile ilk canlı doğum | 115 adımın %49.6’sı otonom | mendizabal_ruiz_2025 | Doğrulandı (özet) |
| 2025 | Düzenleyici | İlk FDA 510(k) onaylı ML embriyo değerlendirme aracı (CHLOE Blast, Eylül 2025) | — | chang_2026 | **İkincil kaynak; birincil FDA kaydı görülmedi** |
| 2025 | Düzenleyici | Alife Embryo Predict CE (Ekim 2025) | — | chang_2026 | **İkincil kaynak** |
| 2026 | Klinik ilk | Day 0 (sperm hazırlığı, denüdasyon, ICSI) sıralı otomasyon | 5 canlı doğum | chavez_badiola_2026 | Doğrulandı (özet) |

**Sayılar:**
`kaufmann_1997_dogruluk` 59 · `kaufmann_1997_degisken` 4 · `banerjee_2010_auc_model` 0.80 · `banerjee_2010_auc_yas` 0.68 · `curchoe_2019_bildiri_2017` 2 · `curchoe_2019_bildiri_2018` 16 · `khosravi_2019_goruntu` 50000 · `tran_2019_embriyo` 10638 · `tran_2019_klinik` 8 · `tran_2019_auc` 0.93 · `letterie_2020_dogruluk_durdur` 0.92 · `barnes_2023_test_auc` 0.737 · `costa_borges_2023_bebek` 2 · `illingworth_2024_hasta` 1066 · `fjeldstad_2024_goruntu` 37133 · `fjeldstad_2024_dis_auc` 0.63 · `mendizabal_ruiz_2025_otonom_yuzde` 49.6 · `mendizabal_ruiz_2025_adim` 115 · `chavez_badiola_2026_canli_dogum` 5

**Sunucu notu** (≈ 125 sözcük):
Peki bu ne zaman başladı? PubMed’de bulabildiğimiz en erken örnek 1997’den. İngiltere’de bir yapay sinir ağı, yalnız dört değişkenle IVF sonucunu yüzde elli dokuz doğrulukla tahmin ediyor. 2010’da ABD’de kişiye özel canlı doğum tahmini geliyor. Asıl kırılma 2018’de oluyor: ASRM ve ESHRE’de yapay zekâ bildirisi bir yıl önce ikiyken on altıya çıkıyor. 2019’da derin öğrenme embriyo görüntülerine giriyor. 2023’te otomatik ICSI ile ilk bebekler doğuyor ve ChatGPT ilk kez doğurganlık sorularıyla sınanıyor. 2024’te ilk büyük randomize çalışma, 2025’te uzaktan ICSI ile ilk canlı doğum geliyor. İkincil bir kaynağa göre ilk FDA onaylı embriyo yazılımı da 2025 Eylül’ünde çıktı; bunu birincil kayıtta doğrulayamadık. Kısacası yayın hızlı, ürün daha hızlı, kanıt en yavaş ilerliyor.

**Süre (sn):** 54

**Künye satırı:**
Kaufmann 1997 Hum Reprod · Banerjee 2010 PNAS · Curchoe & Bormann 2019 JARG · Khosravi 2019 npj Digit Med · Tran 2019 Hum Reprod · Costa-Borges 2023 RBMO · Chervenak 2023 Fertil Steril · Illingworth 2024 Nat Med · Mendizabal-Ruiz 2025 RBMO · Chavez-Badiola 2026 Hum Reprod · *FDA/CE: Chang 2026 Front Endocrinol (ikincil)

**Bölüm toplamı:** 66 + 54 = 120 sn

---

## Kaynaklar

Okuma derinliği: “özet” = PubMed özeti bu oturumda (14 Kasım 2026) görüldü. “tam metin” = PMC tam metni görüldü.

| Anahtar | Künye | PMID | DOI | Okuma | Tasarım | Çıkar çatışması / sponsor |
|---|---|---|---|---|---|---|
| kaufmann_1997 | Kaufmann SJ ve ark. The application of neural networks in predicting the outcome of in-vitro fertilization. Hum Reprod 1997;12(7):1454–7 | 9262277 | 10.1093/humrep/12.7.1454 | özet | Retrospektif model geliştirme | Özette bildirilmemiş |
| banerjee_2010 | Banerjee P ve ark. Deep phenotyping to predict live birth outcomes in IVF. PNAS 2010;107(31):13570–5 | 20643955 | 10.1073/pnas.1002296107 | özet | Retrospektif + zamansal dış doğrulama | Son yazar Yao, 2025 makalesinde Univfy bağlantılı; 2010 özetinde ÇÇ bildirilmemiş |
| curchoe_2019 | Curchoe CL, Bormann CL. AI and ML for human reproduction and embryology presented at ASRM and ESHRE 2018. JARG 2019;36(4):591–600 | 30690654 | 10.1007/s10815-019-01408-x | özet | Kongre bildirisi derlemesi | — |
| khosravi_2019 | Khosravi P ve ark. Deep learning enables robust assessment and selection of human blastocysts after IVF. npj Digit Med 2019;2:21 | 31304368 | 10.1038/s41746-019-0096-y | özet | Retrospektif | Akademik; ÇÇ özette yok |
| tran_2019 | Tran D ve ark. Deep learning as a predictive tool for fetal heart pregnancy following time-lapse incubation and blastocyst transfer. Hum Reprod 2019;34(6):1011–8 | 31111884 | 10.1093/humrep/dez064 | özet | Retrospektif, 8 klinik | Harrison AI ortağı ve Virtus Health; patent |
| vermilyea_2020 | VerMilyea M ve ark. Development of an AI-based assessment model for prediction of embryo viability using static images. Hum Reprod 2020;35(4):770–84 | 32240301 | 10.1093/humrep/deaa013 | özet | Retrospektif, 11 klinik | Life Whisperer/Presagen sahipleri ve çalışanları; patent |
| letterie_2020 | Letterie G, Mac Donald A. AI in IVF: a computer decision support system for day-to-day management of ovarian stimulation. Fertil Steril 2020;114(5):1026–31 | 33012555 | 10.1016/j.fertnstert.2020.06.006 | özet | Retrospektif, yeni teknoloji tanımı | Ortak yazar analitik şirketinde |
| hariton_2021 | Hariton E ve ark. A machine learning algorithm can optimize the day of trigger. Fertil Steril 2021;116(5):1227–35 | 34256948 | 10.1016/j.fertnstert.2021.06.018 | özet | Retrospektif nedensel çıkarım | Akademik |
| bormann_2021 | Bormann CL ve ark. Deep learning early warning system for embryo culture conditions and embryologist performance. JARG 2021;38(7):1641–6 | 33904010 | 10.1007/s10815-021-02198-x | özet | Retrospektif kavram kanıtı | Özette bildirilmemiş |
| costa_borges_2023 | Costa-Borges N ve ark. First babies conceived with Automated ICSI. RBMO 2023;47(3):103237 | 37400320 | 10.1016/j.rbmo.2023.05.009 | özet | Klinik pilot (kavram kanıtı) | Yazarlar Overture Life ve Embryotools’ta |
| chervenak_2023 | Chervenak J ve ark. The promise and peril of using a LLM to obtain clinical information: ChatGPT … fertility counseling. Fertil Steril 2023;120(3 Pt 2):575–83 | 37217092 | 10.1016/j.fertnstert.2023.05.151 | özet | Kesitsel karşılaştırma (ChatGPT Şubat 2023 sürümü) | Akademik |
| barnes_2023 | Barnes J ve ark. Lancet Digit Health 2023;5(1):e28–e40 (STORK-A) | 36543475 | 10.1016/S2589-7500(22)00213-8 | özet (önceki oturum) | Retrospektif + dış doğrulama | Ortak bağlama bakınız |
| illingworth_2024 | Illingworth PJ ve ark. Deep learning versus manual morphology-based embryo selection in IVF: a randomized, double-blind noninferiority trial. Nat Med 2024;30(11):3114–20 | 39122964 | 10.1038/s41591-024-03166-5 | özet (bu oturum); tam metin önceki oturumda | **RKÇ**, çift kör, 14 klinik | Vitrolife yazarları ve finansmanı |
| canon_2024 | Canon C ve ark. Optimizing oocyte yield utilizing a ML model for dose and trigger decisions. Sci Rep 2024;14:18721 | 39164339 | 10.1038/s41598-024-69165-1 | özet | Prospektif + tarihsel kontrol, 2 merkez | Alife Health çalışanı yazarlar |
| correa_2024 | Correa N ve ark. Personalizing the first dose of FSH … IDoser: RKÇ protokolü. Trials 2024;25:38 | 38212837 | 10.1186/s13063-024-07907-2 | özet | RKÇ protokolü (sonuç yok); NCT05948293 | Eugin grubu ve akademik |
| montjean_2024 | Montjean D ve ark. Automated Single-Sperm Selection Software (SiD) during ICSI: a prospective sibling oocyte evaluation. Med Sci (Basel) 2024;12(2):19 | 38651413 | 10.3390/medsci12020019 | özet | Prospektif kardeş oosit | Özette bildirilmemiş |
| fjeldstad_2024 | Fjeldstad J ve ark. An AI tool predicts blastocyst development from static images of fresh mature oocytes. RBMO 2024;48(6):103842 | 38552566 | 10.1016/j.rbmo.2024.103842 | özet | Retrospektif + dış doğrulama | Future Fertility çalışanları |
| rajendran_2024 | Rajendran S ve ark. Automatic ploidy prediction and quality assessment of human blastocysts using time-lapse imaging (BELA). Nat Commun 2024;15:7756 | 39237547 | 10.1038/s41467-024-51823-7 | özet | Retrospektif | Akademik (NIH desteği) |
| xin_2024 | Xin X ve ark. eClinicalMedicine 2024;77:102897 | 39513188 | 10.1016/j.eclinm.2024.102897 | özet (önceki oturum) | Tanısal doğruluk meta-analizi | — |
| liang_2023 | Liang X ve ark. An ultrasound-based deep learning radiomic model … after FET: a pilot cohort study. RBMO 2023;47(2):103204 | 37248145 | 10.1016/j.rbmo.2023.03.015 | özet | Prospektif kohort, tek merkez (n = 240 analiz) | Akademik |
| xu_2024 | Xu F ve ark. An explainable ultrasound-based ML model for predicting reproductive outcomes after FET. RBMO 2025;50(5):104743 | 40199653 | 10.1016/j.rbmo.2024.104743 | özet | Prospektif (n = 787) | Akademik; AUC yalnız eğitim kohortunda verilmiş |
| mendizabal_ruiz_2025 | Mendizabal-Ruiz G ve ark. A digitally controlled, remotely operated ICSI system: case report of the first live birth. RBMO 2025;50(5):104943 | 40210512 | 10.1016/j.rbmo.2025.104943 | özet | Olgu sunumu | Conceivable Life Sciences |
| cimadomo_2025 | Cimadomo D ve ark. AI-based donor oocyte quality assessment moderately improves the prediction of blastocyst development. Hum Reprod 2025;40(10):1886–92 | 40759152 | 10.1093/humrep/deaf153 | özet | Prospektif gözlemsel, çok merkezli, kör | Dört yazar Future Fertility çalışanı/hissedarı |
| yao_2025 | Yao MWM ve ark. Machine learning center-specific models show improved IVF live birth predictions over US national registry-based model. Nat Commun 2025;16:3661 | 40246850 | 10.1038/s41467-025-58744-z | özet | Retrospektif dış doğrulama, 6 merkez | Univfy yazarları |
| bixby_2025 | Bixby CJ, Miller B. Real-world use of an AI-powered clinical decision support tool for ovarian stimulation. F S Rep 2025;6(2):140–6 | 40620368 | 10.1016/j.xfre.2025.01.015 | özet | Retrospektif, eşleştirilmiş tarihsel kontrol | Özette bildirilmemiş |
| wygocki_2026 | Wygocki P ve ark. An AI platform for automated measurement and count estimation of ovarian follicles: a multicenter study. JARG 2026;43(3):715–29 | 41485151 | 10.1007/s10815-025-03777-y | özet | Retrospektif çok merkezli + prospektif gerçek dünya kohortu (904 tarama) | MIM Fertility yazarları |
| chavez_badiola_2026 | Chavez-Badiola A ve ark. Automated oocyte retrieval, denudation, sperm preparation, and ICSI … first live births. Hum Reprod 2026;41(2):214–30 | 41453368 | 10.1093/humrep/deaf240 | özet | Kavram kanıtı, kardeş oosit prospektif dağıtım | Conceivable sponsorlu; çok sayıda patent |
| setti_2026 | Setti A ve ark. MAGENTA outperforms clinical predictors and boosts euploidy modeling. F S Sci 2026;7(3):196–208 | 41825691 | 10.1016/j.xfss.2026.03.002 | özet | Retrospektif, tek merkez | Bir yazar Future Fertility’de |
| liu_2026 | Liu D ve ark. The alignment paradox of medical LLMs in infertility care. J Med Internet Res 2026;28:e97221 | 42766421 | 10.2196/97221 | özet | Retrospektif, tek merkez, kör uzman değerlendirmesi | Akademik |
| lee_2026 | Lee J ve ark. AI chatbot-based psychosocial self-management program for women with infertility: a non-randomized feasibility study. Behav Sci (Basel) 2026;16(10) | 42938674 | 10.3390/bs16101956 | özet | Randomize olmayan fizibilite (n = 37) | Akademik |
| allen_2026 | Allen CS ve ark. Tracking cryogenic tank failure from inception to critical warming. JARG 2026 (çevrimiçi 9 Ekim) | 42850541 | 10.1007/s10815-026-04051-5 | özet | Deneysel simülasyon (tek dewar); **YZ çalışması değil** | Danışmanlık ve sensör şirketi bağlantılı yazarlar |
| go_hudson_2023 | Go KJ, Hudson C. Deep technology for the optimization of cryostorage. JARG 2023;40(8):1829–34 | 37171740 | 10.1007/s10815-023-02814-y | özet | Görüş yazısı | Bir yazar TMRW Life Sciences’ta |
| mcculloh_2026 | McCulloh DH ve ark. Waived semen analyzers in clinical practice … limits of automated assessment. JARG 2026 (mektup) | 42932108 | 10.1007/s10815-026-04057-z | özet | Mektup/derleme | Bir yazar danışmanlık şirketinde |
| chang_2026 | Chang 2026, Front Endocrinol (ortak bağlamdaki derleme) | 42769651 | 10.3389/fendo.2026.1910448 | tam metin (anahtar sözcük taraması: 510, FDA, CE) | Anlatı derlemesi | **İkincil kaynak**: düzenleyici bilgiler buradan; birincil kayıt görülmedi |

---

## Doğrulanamayanlar ve uyarılar

1. **FDA 510(k), CHLOE Blast, Eylül 2025:** Bu bilgi yalnız Chang 2026’nın tam metninde geçiyor (“the first FDA-cleared ML clinical decision support tool for embryo assessment”). FDA veritabanına erişemedik, web kapalı. Zaman çizgisinde içi boş nokta ve “ikincil kaynak” etiketiyle gösterilmeli. Sunucu notunda da “doğrulayamadık” deniyor. Durum: **DOĞRULANAMADI (birincil)**.
2. **Alife Embryo Predict CE, Ekim 2025; FOLLISCAN ve CycleClarity FDA onayı:** Bunların kaynağı da yalnız Chang 2026. CycleClarity için derleme “company data” diyor. Durum: **DOĞRULANAMADI (birincil)**. CycleClarity karta konmadı.
3. **“İlk” iddiaları:** 1997, PubMed’de bulduğumuz *en erken* örnek; dünyadaki ilk olduğu iddia edilmiyor. Daha eski, PubMed dışı mühendislik yayınları olabilir. Sunucu notunda da “bulabildiğimiz en erken” deniyor.
4. **“RKÇ yalnız embriyo seçiminde”:** Bu ifade 14 Kasım 2026’daki PubMed taramamıza dayanıyor (“artificial intelligence/deep learning AND embryo selection AND RCT[pt]” iki kayıt döndürdü; biri ilgisiz). Sistematik bir tarama değil. Stimülasyonda RKÇ yalnız protokol düzeyinde (IDoser). Embriyo seçiminde morfokinetik algoritma RKÇ’leri de var (SelecTIMO, Bhide IPD; bkz. Bölüm 3), ama bunlar derin öğrenme değil. Chang 2026, LOTUS adlı ikinci bir RKÇ’nin konferansta “non-inferiority” bildirdiğini yazıyor; hakemli yayın olmadığı için kullanılmadı.
5. **Kriyo düzeltmesi:** Ortak bağlamda kriyo izleme kaynağı olarak verilen doi:10.1007/s10815-026-04051-5 (PMID 42850541) bir YZ çalışması değil. Tek tankta vakum, ağırlık ve sıcaklık sensörlerinin denendiği deneysel bir simülasyon. Kriyo depolamada YZ’ye ilişkin hakemli klinik kanıt bulamadık; yalnız görüş yazısı var (Go & Hudson 2023, yazarlardan biri TMRW’de). Kart bu yüzden “YZ için kanıt yok” diyor.
6. **Sperm “rutin” etiketi:** Rutin olan, otomatik semen analizörleri (CASA). Bunların çoğu klasik görüntü işlemeye dayanıyor, YZ değil. McCulloh 2026 ABD CLIA bağlamında yazılmış bir mektup. Türkiye’deki kullanım için veri yok.
7. **Ürün adları özetlerde geçmiyor:** “Stim Assist” (Canon 2024) ve “FOLLISCAN” (Wygocki 2026) adları ortak bağlamdan ve Chang 2026’dan geliyor; ilgili özetlerde yalnız “AI platform” deniyor. Kartta ürün adı şirket adıyla birlikte veriliyor.
8. **Uzaktan ICSI’de “3.700 km”:** Bu yalnız Chang 2026’da geçiyor, özette yok; kullanılmadı. Conceivable’ın “yaklaşık 20 kümülatif canlı doğum” bilgisi de yalnız ikincil kaynakta ve şirket bildirimine dayanıyor; kullanılmadı.
9. **Endometriyum:** Xu 2024’teki AUC 0.861 *eğitim* kohortunda; özette test AUC’si verilmemiş, bu yüzden slayta konmadı. Liang 2023’ün tek merkezli prospektif kohortu (AUC 0.825) kullanıldı. ERA gibi transkriptomik sınıflayıcıların “YZ” sayılıp sayılmayacağı tartışmalı; dahil edilmedi. Chang 2026’ya göre Nisan 2026 itibarıyla onaylı bir endometriyum YZ aracı yok (ikincil).
10. **Ortak bağlamdaki küçük düzeltmeler:** Costa-Borges 2023’ün DOI’si 10.1016/j.rbmo.2023.05.009. Ortak bağlamda yalnız PMID vardı. Bixby 2025’te toplam FSH 4,181.77 vs 4,654.71 IU; bu yaklaşık %10.2 daha az anlamına geliyor (bizim hesabımız) ve ortak bağlamdaki “~%10” ile tutarlı. Bu sayı bu bölümde kullanılmadı.
11. **Olgunluk sınıflaması** (araştırma / ticari / rutin) bizim yargımızdır; bir kılavuzdan alınmadı. Künye satırında da bu belirtildi.
12. **Çıkar çatışması deseni:** Kartlardaki sayıların çoğu ürünü geliştiren şirketin yazarlarından geliyor (Univfy, Alife, MIM, Future Fertility, Conceivable, Vitrolife). Sunumda bunu Bölüm 3–4’e bir köprü olarak söylemek önerilir: [ONUR’A SOR] Bu notu sahne 1’de mi, sonraki bölümde mi vermek istersin?
