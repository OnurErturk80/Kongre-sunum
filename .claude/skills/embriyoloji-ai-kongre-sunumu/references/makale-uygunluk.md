# Makale uygunluk değerlendirmesi

Kullanıcı sunumda kullanılacak makaleleri **kendisi belirler**. Bu skill'in işi, her makalenin
sunum konusuna ve sahnelerine **uygun olup olmadığını** gerekçeyle değerlendirmek, kaynağın
gerçekten var olduğunu ve iddiayı desteklediğini doğrulamak, ve kaynakça boşluklarını göstermektir.
Makale seçme yetkisi kullanıcıdadır; sen karar önerirsin, o karar verir.

İçindekiler: 1 Girdi · 2 Kimlik ve statü doğrulama · 3 Okuma derinliği · 4 Dört eksenli değerlendirme ·
5 Karar ve çıktı biçimi · 6 İddia-kaynak matrisi · 7 Telif ve alıntı · 8 İsteğe bağlı: kaynak arama

---

## 1. Girdi: kullanıcı makaleyi nasıl verir?

Kabul edilen biçimler (hangisi gelirse onu işle, biçim dayatma):
- **PMID veya DOI listesi** → en güvenilir yol.
- **PDF yükleme** (`/mnt/user-data/uploads/`) → `file-reading`/`pdf-reading` skill'leriyle oku.
- **Yalnız başlık/yazar/yıl** → PubMed'de ara, bulunan eşleşmeyi kullanıcıya **teyit ettir** (yanlış makaleyi
  değerlendirmek sessiz hatadır).
- **Bağlantı** → sayfa açılabiliyorsa oku; açılamıyorsa kullanıcıdan PDF/özet iste. (Ağ yalnızca
  belirli alan adlarına açıktır; `doi.org` ve çoğu yayıncı sitesi erişilemeyebilir. Bunu kullanıcıya söyle.)

Değerlendirmeye başlamadan **sunumun sahne listesini ve her sahnenin iddiasını** bil
(`anlati-ve-sahneler.md`). Makale, yalnızca bir iddiaya/sahneye göre "uygun"dur; boşlukta uygunluk yoktur.
Sahne listesi henüz yoksa kullanıcıya üç aday tezi (`anlati-ve-sahneler.md`) göster ve önce tezi seçtir.

## 2. Kimlik ve statü doğrulama (her makale için, atlanmaz)

Araçlar: önce `tool_search` ile PubMed araçlarını yükle.
1. `convert_article_ids` (DOI↔PMID↔PMCID) → makale PubMed'de var mı, PMC tam metni var mı?
2. `get_article_metadata` → başlık, yazarlar, dergi, yıl, cilt/sayfa, DOI, özet, **`article_types`**.
3. Statü bayrakları (`article_types` ve başlıkta ara): *Retracted Publication*, *Retraction of Publication*,
   *Published Erratum*, *Comment*, *Preprint*, *Review*/*Systematic Review*/*Meta-Analysis*,
   *Randomized Controlled Trial*, *Clinical Trial*. Geri çekilmiş makale **otomatik "uygun değil"**dir.
4. `get_copyright_status` → şekil/tablo yeniden kullanım lisansı (CC BY mı?).
5. Ön baskı ise (`bioRxiv/medRxiv` araçları) hakem denetiminden geçmediğini işaretle; yayımlanmış
   sürümü var mı (`get_preprint` → published DOI) bak, varsa yayımlanmış sürümü kullan.
6. PubMed biyomedikal kapsamdadır. **İstatistik/makine öğrenmesi metodoloji makaleleri**
   (ör. Biometrika, arXiv, IEEE) PubMed'de bulunmayabilir. Bulunmuyorsa "PubMed'de doğrulanamadı"
   yaz, künyeyi kullanıcının verdiği PDF/sayfadan al, "kimlik doğrulanamadı" etiketiyle işaretle;
   bulunmuş gibi davranma.
7. PubMed sonucu kullandığın her yanıtta **"PubMed'e göre"** diye belirt ve her makalenin **DOI bağlantısını**
   ver (`https://doi.org/...`); araç bunu zorunlu kılar.

Künye eşleşmiyorsa (kullanıcının yazdığı yıl/yazar/dergi ile PubMed farklıysa) sessizce düzeltme;
farkı raporla.

## 3. Okuma derinliği (dürüstçe etiketle)

Her makalenin yanına **ne okuduğunu** yaz:
- **Tam metin okundu** (PMC `get_full_text_article` veya kullanıcının PDF'i)
- **Yalnız özet okundu** → "uygun" kararı **geçici**dir; sayısal iddia, yöntem ayrıntısı ve sınırlılık
  için tam metin gerekir. Bunu açıkça söyle.
- **Okunamadı** (erişim yok) → değerlendirme yapma; "okunamadı, kimlik doğrulandı" de.

Sunum slaytına makaleden bir **sayı** yazılacaksa o sayıyı tam metinde/özette gör ve aynen aktar;
hafızadan, yuvarlayarak ya da başka makaleyle karıştırarak yazma.

## 4. Dört eksenli değerlendirme

**A. Konu ve sahne uygunluğu.** Makale hangi rolü oynuyor?
(1) *Çerçeve/arka plan* · (2) *Yöntem referansı* (istatistik, raporlama kılavuzu) ·
(3) *Kanıt* (embriyoloji + yapay zekâ sonuçları) · (4) *Karşı kanıt / sınırlılık* ·
(5) *Yazılım, yapay zekâ ile geliştirme, düzenleme, etik*.
Hangi sahneye hizmet ediyor? Hiçbir sahneye hizmet etmiyorsa "uygun değil" (iyi makale olması yetmez).

**B. İddia-kaynak uyumu (en kritik).** Slaytta o makaleye dayanarak yazacağın cümle nedir? Makale
bunu *gerçekten* gösteriyor mu, yoksa yalnız ima mı ediyor, ya da tartışma bölümünde spekülasyon mu?
Yaygın hatalar: derleme makalesinin başka çalışmaya atfını birincil bulgu gibi sunmak; "in silico/retrospektif"
sonucu klinik fayda diye sunmak; dar popülasyon bulgusunu genele yaymak.

**C. Kanıt kalitesi.** Çalışma tasarımı (SR/MA > RCT > prospektif kohort > retrospektif > in silico >
uzman görüşü; preprint ayrı işaret). Örneklem, **tek merkez mi**, **harici doğrulama var mı**,
**hasta-düzeyi bölme / sızıntı kontrolü** yapılmış mı, kalibrasyon raporlanmış mı, raporlama kılavuzuna
(TRIPOD+AI, CONSORT-AI, STROBE…) uyum, çıkar çatışması/sponsor (ticari sistem üreticisi finansmanı).
Bu sunumun omurgası "sızıntısız doğrulama ve kalibrasyon" olduğundan, **modelin kendi
doğrulamasının bu kriterlere uyup uymadığı** özellikle not edilir: uymayan çalışma "kanıt" olarak
değil, **"sunumun savunduğu sorunun örneği"** olarak kullanılabilir. Bu meşru ve güçlü bir kullanımdır.

**D. Güncellik ve statü.** Yıl (alan hızlı değişiyor; 3 yıldan eski yapay zekâ sonucu için daha yeni
çalışma var mı bak), düzeltme/geri çekilme, ön baskı→yayın durumu. Tanım/konsensus belgesiyse güncel sürüm mü.

**(E) Sunumda kullanım biçimi.** Tek cümle atıf mı, bir sayı mı, bir figür mü? Figür için telif (bölüm 7).

## 5. Karar ve çıktı biçimi

Her makale için üç karardan biri:
- **✅ Uygun:** hedef sahnede ve iddiada doğrudan kullanılabilir.
- **◐ Koşullu:** kullanılabilir ama belirli sınırla (ör. "yalnızca arka plan cümlesinde", "sonucu
  'retrospektif, tek merkez' kaydıyla", "yalnız özet okundu, tam metni doğrula", "ticari finansman belirtilmeli").
- **✖ Uygun değil:** neden (konu dışı, iddiayı desteklemiyor, geri çekilmiş, çok eski, düşük kanıt ve
  iddia güçlü, kimlik doğrulanamadı).

Yanıt biçimi (sohbette; kullanıcı dosya isterse `makale_degerlendirme.md`):

1. **Özet tablo:** `# | Künye (yazar, dergi, yıl, DOI bağlantısı) | Tür | Okuma | Rol | Hedef sahne | Karar`
2. **Her makale için 3-5 cümle gerekçe:** sunumda hangi cümleyi destekler, kanıt kalitesi, risk,
   önerilen kullanım biçimi. Kısa tut; kullanıcı embriyolog, makale içeriğini yeniden öğretme.
3. **Kapsam boşlukları:** hangi sahne/iddia için destekleyici makale **yok** (aşağıdaki matris).
4. **Dengeli kaynakça kontrolü:** olumlu *ve* temkinli/olumsuz sonuçlar var mı? Yalnızca ticari
   sistem çalışmaları mı? Yalnızca tek merkez mi? Çok eski/çok yeni dengesi.
5. **Sonraki adım önerisi:** hangi 1-3 makalenin tam metni okunmalı, hangi iddia yeniden ifade edilmeli.

Gerekçeni kanıtla yaz, ölçüsüz övme veya yargılama yok. "Zayıf makale" demek yerine "bu iddiayı
desteklemiyor, çünkü…" de.

## 6. İddia-kaynak matrisi (sahne bazlı)

Sunumun her sahnesi için kaynak gerektiren iddiaları çıkar ve eşle. Şablon:

| Sahne | Slayttaki iddia (tam cümle) | Kaynak gerekli mi? | Eşleşen makale | Durum |
|---|---|---|---|---|
| 7 | "Embriyolar hasta içinde korelasyonludur" | Yöntem (kümeli veri) | Kullanıcı seçimi | ✅ / ◐ / ✖ / **boşluk** |
| 10 | "Zaman kayması kalibrasyonu bozar" | Evet | … | … |

Kaynak **gerektirmeyen** iddialar da var: kendi sentetik demonun bulguları (kaynak: kod ve
`sonuclar.json`), programın kendi özellikleri (kaynak: depo/README sürümü). Bunları makaleyle
"desteklemeye" çalışma; kaynağını doğru yaz.

Bir iddia için hiç makale yoksa seçenekler: (a) iddiayı yumuşat, (b) iddiayı kaldır, (c) kullanıcıdan
kaynak iste, (d) kaynak aramayı öner (bölüm 8). Makale "uydurma" (olmayan makale, olmayan bulgu) bir seçenek **değildir**.

## 7. Telif ve alıntı

- Makale metnini sunumda **uzun alıntılama**. En çok tek kısa alıntı (<15 sözcük), tırnak içinde, atıfla;
  genelde kendi cümlenle özetle.
- **Şekil/tablo kopyalama:** lisans CC BY ise atıfla kullanılabilir (`get_copyright_status`); değilse
  yayıncıdan izin gerekir. Güvenli yol: **kendi verinle/sentetik demonla yeniden çiz** ve "… çalışmasından uyarlanmıştır"
  de; bu sunumun zaten yaklaşımıdır.
- Slayt altında kısa atıf (Yazar ve ark., Dergi, Yıl) ve son slaytta tam künye + DOI.

## 8. İsteğe bağlı: kaynak arama (yalnız kullanıcı isterse)

Kullanıcı "şu iddia için kaynak bul" derse aday liste üret; **seçimi kullanıcı yapar**, her aday yukarıdaki
doğrulamadan geçer. Sorgu kalıpları (PubMed sözdizimi; sonuç boşsa terimleri gevşet):

- `artificial intelligence AND embryo selection AND (systematic review[Publication Type] OR randomized controlled trial[Publication Type])`
- `deep learning AND time-lapse AND blastocyst AND external validation`
- `machine learning AND IVF AND calibration AND (prediction model)`
- `TRIPOD AND artificial intelligence` (raporlama kılavuzu)
- `clustered data AND generalized estimating equations AND IVF` (kümeli veri, embriyolar)
- `multiple embryos per patient AND statistical analysis AND IVF` (hasta içi korelasyon)
- `dataset shift OR temporal validation AND clinical prediction model`
- `large language model OR AI coding assistant AND laboratory software` (yapay zekâ ile yazılım; PubMed'de zayıf olabilir)

Arama sonucunu "şu makaleleri öneririm" diye değil, "şu adaylar bulundu, kimlikleri doğrulandı, okuma
derinliği şu, uygunluk önerisi şu" diye ver. Hiç uygun aday yoksa bunu söyle.


## 9. Önceden doğrulanmış aday havuzu (10 Kasım 2026, yalnız özetler okundu)

Yeniden kullanmadan önce statüyü (geri çekilme, düzeltme) tekrar kontrol et. PMID: konu · not.
- 28784335: Vienna consensus (RBMO 2017) · KPI tanımları
- 35338418: Zacà 2022 JARG · KPI'ları yaşa göre ayarlama
- 39733809: Olawade 2025 JGOHR · anlatı derlemesi, YZ ile KPI izleme önerisi
- 39122964: Illingworth 2024 Nat Med · RCT, 1066 hasta, eşdeğerlik gösterilemedi; üretici yazarlar
- 37588797: Salih 2023 Hum Reprod Open · SR, YZ vs embriyolog, geriye dönük, harici doğrulama eksik
- 40264925: AlSaad 2025 Front Reprod Health · kapsam derlemesi, %58 doğruluk ölçütü, %82 anne yaşı yok
- 38997251: Sun 2024 Chin Med J · YZ > embriyolog iddiası, temkinli
- 39455054: Coticchio 2024 Hum Reprod · time-lapse + YZ ile gelişemeyecek embriyo eşikleri
- 36543475: Barnes 2023 Lancet Digit Health · STORK-A ploidi, dış doğrulamada düşüş
- 36825452: Bamford 2023 Hum Reprod · karma lojistik regresyon > ML (ploidi)
- 36952146: Huang 2023 JARG · niPGT meta-analizi, duyarlılık 0.84, özgüllük 0.85
- 37356468: Cinnioglu 2023 Fertil Steril · niPGT-A SR, firma yazarları
- 39059790: Sakkas 2024 Hum Reprod · niPGT-A kültür protokolü klinik sonucu etkilemedi; Igenomix finansmanı
- 41148806: Mrugacz 2025 Cells · niPGT derlemesi, amplifikasyon başarısızlığı %10-50
Boşluklar: sperm/oosit YZ; IVF laboratuvarında CUSUM/EWMA ile KPI izleme (PubMed'de doğrudan bulunamadı).
