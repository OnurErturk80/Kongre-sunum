# Ortak bağlam: IVF laboratuvarında yapay zekâ — kongre sunumu v4

Bu dosyayı her ajan önce okur. Kullanıcı: Onur Ertürk, 22 yıllık klinik embriyolog (Türkiye). Python'a yeni,
klinik doğrulukta uzman. Dil: Türkçe; klinik terimler İngilizce kalır (blastocyst, ICSI, PN, ICM, TE, FET, PGT-A).

## Kullanıcının yeni sunum yapısı (14 Kasım 2026, önceki sürümü beğenmedi)

Sunum 15 dakika (soru-cevap hariç). Beş ana başlık, kullanıcının kendi sözleriyle:

1. **Yapay zekâ labda hangi aşamalarda kullanılmaya başlandı?**  (≈ 2 dk)
2. **Ne kadar yaygınlaştı? Nerede, ne kadar kullanılıyor?** Önceki oturumdaki ülke/merkez taraması kullanılacak. (≈ 2 dk)
3. **Bu kadar kullanılması sonuçları nasıl etkiliyor? Yapay zekâ kullanımı neye etki ediyor?** Yayınlar kullanılacak. (≈ 3 dk)
4. **Yapay zekâ ne kadar doğru sonuç veriyor?** (≈ 3 dk)
5. **Benim bu konudaki fikrim.** Yaptığım küçük bir uygulama (Patient Data Center) ile iş akışını nasıl rahatlattığımı; KPI takibi ve ileri istatistik yapabildiğimi gösterebilirim. (≈ 4 dk)

Artı başlık ve kapanış (≈ 1 dk).

## Sert kurallar (hepsi için)

- **Uydurma sayı ve atıf yok.** Her sayı PubMed kaydında (özet veya tam metin) görülüp aynen aktarılır. Her kaynağın yanına PMID ve DOI ile **okuma derinliği** (tam metin / yalnız özet) yaz. Doğrulayamadığını "DOĞRULANAMADI" diye ayrı listele.
- **Web araması kurumda kapalı (HTTP 403).** PubMed araçlarını kullan: `ToolSearch` ile "pubmed" ara ve yükle
  (`mcp__PubMed__search_articles`, `get_article_metadata`, `get_full_text_article`, `convert_article_ids`). WebFetch denenebilir; başarısız olursa ısrar etme.
- **Gerçek hasta verisi yok.** Bütün demolar sentetik; sentetik sonuç klinik bulgu gibi sunulmaz.
- **Merkez adı yok (kullanıcı kararı).** Yaygınlık sahnesinde yalnız ülke ve firmaların kendi açıkladığı toplam sayılar; Türkiye dahil hiçbir tüp bebek merkezinin adı slayta girmez. Ürün adları (iDAScore, CHLOE vb.) bilimsel bağlamda kullanılabilir.
- **Programa olmayan yetenek atfetme.** Patient Data Center içinde makine öğrenmesi modeli YOK. Kayıt ve betimsel istatistik aracıdır; yapay zekâ (Claude Code) onu yazmak için kullanıldı.
- **Kullanıcının fikrini uydurma.** 5. bölümde kullanıcının daha önce onayladığı tezleri kullan (aşağıda); yeni bir görüş eklersen "[ONUR'A SOR]" diye işaretle.
- Türkçe tipografi: “ ” tırnak, ’ kesme işareti, − eksi işareti. Ondalık ayırıcı **nokta** (şekillerle tutarlı).

## Önceki oturumdan doğrulanmış bulgular (PubMed'e göre, 10–14 Kasım 2026)

### Aşamalar ve ürünler
- Danışmanlık: Univfy PreIVF (Nat Commun 2025, doi:10.1038/s41467-025-58744-z; yazarlar Univfy bağlantılı).
- Stimülasyon: Alife Stim Assist tipi doz önerisi; prospektif + tarihsel kontrol n=291, MII artışı anlamsız (doi:10.1038/s41598-024-69165-1); gerçek dünya verisinde toplam FSH ~%10 az (doi:10.1016/j.xfre.2025.01.015). IDoser RKÇ protokolü (Trials 2024, PMID 38212837), sonucu yayımlanmamış.
- Folikül USG: FOLLISCAN, 5.508 tarama, ≥10 mm F1 %93.3 (doi:10.1007/s10815-025-03777-y); CycleClarity.
- Oosit: MAGENTA (Future Fertility). Donör oositte katkısı orta (doi:10.1093/humrep/deaf153); öploidi AUC tek başına 0.542 (doi:10.1016/j.xfss.2026.03.002).
- Sperm: CASA rutin; SiD (IVF 2.0) kardeş-oosit çalışmasında fark yok (doi:10.3390/medsci12020019).
- ICSI otomasyonu: Chavez-Badiola 2026 Hum Reprod (PMID 41453368, doi:10.1093/humrep/deaf240): 11 olgu, 5 canlı doğum, döllenme otomatik %64.3 / manuel %81; Conceivable sponsorlu. İlk uzaktan ICSI doğumu: doi:10.1016/j.rbmo.2025.104943. Costa-Borges RBMO 2023 ilk bebekler (PMID 37400320).
- Embriyo seçimi: iDAScore, KIDScore (Vitrolife, CE), CHLOE (Fairtility; Chang 2026 derlemesine göre CHLOE Blast Eylül 2025 FDA 510(k)), Life Whisperer, ERICA, Alife Embryo Predict (CE, Ekim 2025).
- Ploidi tahmini: STORK-A (Barnes 2023), BELA, FEMI temel modeli (doi:10.1038/s41467-025-61116-2).
- Lab kalite kontrol: Bormann ve ark. derin öğrenmeye dayalı erken uyarı (doi:10.1007/s10815-021-02198-x).
- Kriyo izleme: doi:10.1007/s10815-026-04051-5.
- LLM: ChatGPT doğurganlık soruları %6.1 hatalı ifade (doi:10.1016/j.fertnstert.2023.05.151).
- Düzenleyici durumların çoğu tek ikincil kaynaktan: Chang 2026, doi:10.3389/fendo.2026.1910448 (doğrulanmalı).
- Benimseme anketi: Chang 2026'ya göre "herhangi bir YZ kullanımı" %24.8 (2022) → %53.2 (2025); asıl anket kaynağı DOĞRULANAMADI. 2023 uluslararası anket, 702 embriyolog (doi:10.1016/j.rbmo.2024.104435).

### Yaygınlık (web; hakemli DEĞİL; tarayıcıyla 10 Kasım 2026'da görüldü)
- CHLOE: "100'den fazla klinik, Kuzey Amerika, Avrupa, Asya-Pasifik, Latin Amerika" (Fairtility–First Fertility basın bülteni, 27 Temmuz 2026).
- MAGENTA: "300+ clinics worldwide" (futurefertility.com/en/partner-fertility-clinics/).
- FutureLife × Alife: 16 ülkede 60 klinik, yılda ~77.000 IVF siklusu, 5 Mayıs 2026 (futurelifegroup.com/en/press/18-futurelife-in-partnership-with-alife-health/).
- Indira IVF (Hindistan) 100+ klinikte Life Whisperer, Kasım 2022 duyurusu (güncel durumu bilinmiyor).
- Life Whisperer: Astec 2024'te satın aldı; Japonya ve Endonezya'da sunuluyor.
- Vitrolife: "75% of fertility clinics worldwide" hizmet (tüm ürünler; YZ'ye özgü değil).
- Univfy: ABD, İngiltere, İsviçre merkezleri.
- Conceivable AURA: Meksika (Mexico City, Guadalajara); ABD'de 2027 planı.
- FOLLISCAN: Kolombiya (tek merkez); 11 klinik 7 ülke doğrulama.
- ABD: First Fertility (CHLOE + Alife), Boston IVF (25+ şube, Stim Assist), US Fertility (pilot).
- İspanya: bir grup 7 klinik CHLOE; Eugin MAGENTA. İngiltere: MAGENTA/VIOLET, Univfy. Japonya: MAGENTA, Life Whisperer. Avustralya: kendi geliştirdiği "IVY" + iDAScore RKÇ merkezi.
- **Türkiye:** CHLOE 2022'den beri (bir merkez, "Türkiye'de ilk"); YZ ile sperm seçimi (iki merkez, farklı ürünler); iDAScore'un Türkçe kılavuzu var. Merkez ADI VERİLMEYECEK.
- Ülke listesi (en az bir merkezin duyurduğu): ABD, Meksika, Kolombiya, İspanya, İngiltere, İsviçre, Avustralya, Japonya, Endonezya, Hindistan, Türkiye; ayrıca FutureLife'ın 16 Avrupa ülkesi.

### Sonuçlara etki (yüksek kaliteli yayınlar)
- Illingworth 2024 Nat Med (PMID 39122964, doi:10.1038/s41591-024-03166-5): RKÇ, 14 klinik, 1.066 hasta; klinik gebelik %46.5 vs %48.2, RD −1.7 (%95 GA −7.7 ile 4.3), non-inferiority gösterilemedi. Tam metinden: değerlendirme 21.3 sn vs 208.3 sn; canlı doğum %39.8 vs %43.5; freeze-all alt grubu %49.5 vs %61.3 (post hoc). Vitrolife finansmanı.
- Bhide 2026 Hum Reprod Update (PMID 42955792, doi:10.1093/humupd/dmag035): IPD meta-analizi, 8 RKÇ, n=5.642; canlı doğum aOR genel TLI 0.97 (0.81–1.15), kesintisiz kültür 1.02 (0.84–1.23), morfokinetik seçim 0.92 (0.78–1.07); yüksek kesinlik. Derin öğrenme değil, TLI/morfokinetik.
- SelecTIMO (Kieslinger, Lancet 2023, PMID 37004670) ve 2026 maliyet-etkinlik (Hum Reprod Open, PMID 42130487, doi:10.1093/hropen/hoag034): 12 aylık kümülatif canlı doğum %48.7 / %48.4 / %48.2; algoritma muhtemelen maliyet-etkin değil. Perinatal güvenlik fark yok (PMID 41139424).
- Yaghi 2026 Eur J Obstet Gynecol (PMID 42914619): klinik gebelik RR 0.99 (0.87–1.12), yalnız 2 çalışma havuzlanabildi.
- ESHRE add-ons 2023 Hum Reprod (PMID 37747409, doi:10.1093/humrep/dead184): 42 önerinin hiçbiri yüksek kaliteli kanıta dayanmıyor; TLI ± seçim yazılımı canlı doğumu artırmak için önerilmez (tam metin).
- ASRM 2026 komite görüşü Fertil Steril 126(3):494–8 (PMID 42285874): yalnız özet görüldü.
- Kieslinger 2024 Nat Med yorum "The inconvenient reality of AI-assisted embryo selection in IVF" (PMID 39354198): içerik okunmadı.
- Etik: Afnan 2021 Hum Reprod Open (PMID 34938903), Koplin 2025 Hum Reprod (PMID 39657965), Du 2026 Hum Reprod Open şirket siteleri (PMID 42923733), Webb 2026 JARG nitel (PMID 42303882).
- Raporlama: TRIPOD+AI (PMID 38626948), CONSORT-AI (PMID 32908283), SPIRIT-AI (PMID 32908284).

### Doğruluk
- Berntsen 2022 PLoS One (PMID 35108306): 18 merkez, 115.832 embriyo; transfer edilen (KID) AUC 0.67, tüm embriyolar 0.95; yeni klinikte 0.60–0.75. Vitrolife yazarlar.
- Ueno 2021 Fertil Steril (doi:10.1016/j.fertnstert.2021.06.001): <35 yaş FHB AUC iDAScore 0.72 / KIDScore 0.66 / Gardner 0.64.
- Barnes 2023 Lancet Digit Health (PMID 36543475): STORK-A AUC 0.761 iç; test 0.737; dış 0.702 ve 0.715 (yazarlar "genellenebilir" diyor).
- Bamford 2023 Hum Reprod (PMID 36825452): 8.147 embriyo, 9 klinik; karma lojistik regresyon AUC 0.71 > RF 0.68, XGB 0.63, derin öğrenme 0.63.
- Xin 2024 eClinicalMedicine (PMID 39513188): ploidi meta-analizi, 12 çalışma, 6.879 embriyo; duyarlılık 0.71, özgüllük 0.75, AUC 0.80.
- Salih 2023 Hum Reprod Open (PMID 37588797): 20 çalışma; morfoloji tahmininde YZ %75.5 vs embriyolog %65.4; klinik gebelik tahmininde %77.8 vs %64; hiçbiri prospektif değil.
- Thirumalaraju 2025 Fertil Steril (PMID 40876725): 50 kopya model, Kendall W ≈ 0.35, kritik hata ≈ %15, AUC ≈ 0.60; başka merkezde kararsızlık artıyor.
- Cimadomo 2026 Fertil Steril (PMID 42546812): YZ sıralaması geleneksele eşit ya da biraz iyi; anöploidi engellenemiyor.
- Berman 2023 AJOG (PMID 37116822): 22 çalışmanın tamamı retrospektif, 10'unda yüksek yanlılık riski.
- Kragh & Karstoft 2021 JARG (PMID 34173914): retrospektif karşılaştırmada seçim yanlılığı kaçınılmaz.
- MAGENTA öploidi AUC 0.542 tek başına; kalibrasyon eğimi 0.259 → 0.645 (doi:10.1016/j.xfss.2026.03.002).

## Kullanıcının daha önce onayladığı tezler (5. bölüm için)
- "Ham değil, kişisel yapay zekâ": yapay zekâyı hazır/ham değil, embriyoloğun tecrübesiyle kişiselleştirerek kullanmak.
- Kayıtlar: kâğıt → bilgisayar (Excel/Access) → kendi programım → yapay zekâ ile derin istatistik.
- Sorunu en iyi işi yıllarca yapan bilir; embriyolog ihtiyacı söyler, yapay zekâ kodlar, embriyolog doğrular.
- Embriyolog işsiz kalmaz; yapay zekânın kalite kontrolcüsü olur (etiketleyen, doğrulayan, izleyen, karar veren).
- KPI takibinde yapay zekâ desteği: erken uyarı (CUSUM), adil karşılaştırma (funnel, yaşa göre ayar). Belirli bir KPI öne çıkmaz.
- Görsel modelleri yerelde kendi etiketleriyle eğitmek (sentetik demo ile).

## Hazır kaynaklar (bulut çalışma alanında)
- Patient Data Center deposu: `/home/claude/Patient-Data-Center` (14 Kasım'da klonlandı; 341 commit, 8 Eylül–9 Ekim 2026, 296 sürüm notu, son v6.266; `app.py` 14.214 satır; `CLAUDE.md` 5.212 satır; 61 göç betiği). README sürüm başlıkları: v0.2 değişiklik geçmişi (`degisiklik_log`: hangi alan, eski/yeni değer, kim, ne zaman), v1.2 otomatik yedekleme, v1.4 ICSI, v2.0 fert kontrol, v2.5 gün2/3, v2.6 blastokist, v3.0 vitrifikasyon + cryo haritası, v3.2 çözme, v3.6 transfer, v3.8 aşamaya bağlı fotoğraf, v5.3 gebelik, v6.3 işlemi yapan, v6.14 modül izni, v6.15 rol güvenlik açığı kapatıldı, v6.16 iki makine arası taşıma, v6.19 hayalet oosit (“Oosit sayısı klinik bir sayıdır.”), v6.123 aylık oranlar ve yıl/ay seçici.
- Sentetik demolar ve sonuçları: `/home/claude/sunum/analiz/` (`sonuc_kpi/sonuclar_kpi.json`, `sonuc_gorsel/sonuclar_gorsel.json`, `sonuc_slayt/sonuclar.json`, SVG şekiller). Örn. 500 simülasyonda CUSUM düşüşü %96.6 (medyan 10 hafta), aylık ortalama %67.2 (14 hafta); yanlış alarm %4.0 / %1.8; funnel'da F ham 0.689 → yaşa ayarlı 0.759; E dışarıda; hazır görsel model başka labda AUC 0.51, 25 yerel etiketle 0.83; yanlış (rastgele) doğrulamada GBM AUC 0.686, hasta-gruplu 0.646.
- Literatür sayıları JSON: `/home/claude/sunum/analiz/literatur_sayilar.json`.
- Önceki sunum derleyicisi (çalışıyor): `/home/claude/sunum/kur_sunum.py`; skill: `/home/claude/embriyoloji-ai-kongre-sunumu/` (SKILL.md, references/, scripts/, assets/deck_iskelet.html).

## Bölüm ajanlarının çıktı biçimi

Her bölüm ajanı iki dosya yazar:

1. `/home/claude/sunum_v4/bolumler/0N_<kisa_ad>.md` — şu yapıda:
   - `# Bölüm N: <kullanıcının sorusu>`
   - `## Tek cümlelik cevap` (bölümün bulgusu)
   - `## Sahneler` — 2–3 sahne. Her sahne için: **Eylem başlığı** (bulguyu söyler, ≤ 12 sözcük) · **Ekranda** (≤ 40 sözcük; kart/madde metni aynen) · **Görsel / etkileşim önerisi** (somut: hangi grafik, hangi düğme, hangi veri; stok görsel ve robot/beyin ikonu yok) · **Sayılar** (her biri kaynak anahtarıyla) · **Sunucu notu** (konuşma dilinde, tam cümleler, sürenin sözcük karşılığı ≈ 2.3 sözcük/sn) · **Süre (sn)** · **Künye satırı** (slayt altı küçük kaynak satırı).
   - `## Kaynaklar` — her biri: anahtar, künye, PMID, DOI, okuma derinliği, çalışma tasarımı, çıkar çatışması/sponsor notu.
   - `## Doğrulanamayanlar ve uyarılar`
2. `/home/claude/sunum_v4/bolumler/0N_sayilar.json` — slayta giren her sayı: `{"anahtar": {"deger": ..., "kaynak": "PMID ...", "okuma": "ozet|tam_metin|web"}}`.

Raporun sonunda (ajanın son mesajı) 10 satırı geçmeyen Türkçe özet ver: hangi sahneler, en önemli 3 bulgu, doğrulanamayanlar.
