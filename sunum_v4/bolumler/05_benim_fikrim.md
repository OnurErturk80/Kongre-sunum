# Bölüm 5: Benim bu konudaki fikrim

> Süre ≈ 4 dk (240 sn), 5 sahne: uygulama 2 · KPI/istatistik 2 · fikir 1.
> Patient Data Center (PDC) **bir kayıt ve betimsel istatistik aracıdır; içinde makine öğrenmesi modeli YOKTUR.** Yapay zekâ (Claude Code) onu yazmak için kullanıldı. Sahne 4–5’teki CUSUM, funnel ve görsel model ince ayarı **programda yok**; programın tuttuğu türden veriyle yapılabileceğini gösteren **sentetik** demolardır.
> Kullanıcının daha önce onaylamadığı her yeni görüş **[ONUR’A SOR]** ile işaretlidir.

## Tek cümlelik cevap

Hazır yapay zekâ ürünleri yaygınlaştı ama canlı doğumu artırdığı gösterilemedi ve doğruluğu orta; benim yolum yapay zekâyı **ham değil, kişisel** kullanmak: ihtiyacı ben söyledim, yapay zekâ 32 günde 341 commit’lik bir kayıt programı kodladı, ben doğruladım — bugün program beş oranı her ay kendiliğinden hesaplıyor ve aynı veriyle erken uyarı ile adil karşılaştırma yapılabiliyor.

---

## Sahneler

### Sahne 5.1 — Uygulama: elle yapılan iş

**Eylem başlığı:** Elle yapılan altı iş, kayıt girilirken kendiliğinden oluyor (9 sözcük)

**Ekranda** (kartlar, aynen):
- Fotoğraf → tek dokunuşla doğru oosite ve aşamaya *(v3.8)*
- Cryo haritası kayıttan türer; boş yer önerilir *(v3.0, v6.190)*
- Resmî formlar ve Bakanlık tablosu kayıttan basılır *(v6.37, v6.201)*
- İşlemi yapan seçilir; her değişiklik izlenir *(v6.99, v0.2)*
- Oranlar her ay kendiliğinden *(v6.123)*
- Yedek yoksa uyarı *(v1.2)*

**Görsel / etkileşim önerisi:** İki sütunlu “önce → şimdi” ızgarası. Sol sütun gri, kısa fiil (“klasörden kare bul, oosite eşle”, “harita defterini güncelle”, “formu elle doldur”); sağ sütun koyu, sürüm rozetli. Her tıklamada bir satır açılır (6 adım). Sağ alt köşede programın **test veritabanından** alınmış cryo haritası ekran görüntüsü; köşede kırmızı “TEST VERİSİ” etiketi. Resmî form görüntüsü **kullanılmaz** (form başlığında kurum adı ve kalite kodu var; bkz. uyarılar). Stok görsel, robot/beyin ikonu yok.

**Sayılar:** sayı yok (yalnız sürüm numaraları; kaynak: `depo_*` anahtarları).

**Sunucu notu** (≈ 115 sözcük, 50 sn):
“Önceki dört bölümde başkalarının ürettiği yapay zekâyı konuştuk. Şimdi kendi laboratuvarıma dönüyorum. Kayıtlarımız kâğıttan Excel’e ve Access’e, oradan da kendi yazdığım programa geçti. Programın amacı tek: elle yaptığım işleri kayıt anına taşımak. Mikroskoptan aldığım kareyi artık klasörde arayıp eşlemiyorum; ekranda ‘bu kareyi şu oosite ekle’ diyorum. Cryo haritasını ayrıca güncellemiyorum; harita vitrifikasyon kaydından türüyor, dondururken program bana boş yer öneriyor. Doldurmak zorunda olduğum resmî formlar ve Bakanlığın aylık tablosu kayıttan basılıyor. Kimin hangi işlemi yaptığı ve hangi alanın kim tarafından değiştirildiği kendiliğinden kayda geçiyor. Ne kadar zaman kazandırdığını ayrıca ölçmedik; [ONUR’A SOR: kendi deneyiminizden bir süre örneği var mı?]”

**Süre (sn):** 50

**Künye satırı:** Patient Data Center README sürüm notları v0.2, v1.2, v3.0, v3.8, v6.37, v6.99, v6.123, v6.190, v6.201 · ekran görüntüsü test veritabanından.

---

### Sahne 5.2 — Uygulama: nasıl geliştirildi, hangi hatalara karşı korunuyor

**Eylem başlığı:** İhtiyacı embriyolog söyledi, yapay zekâ kodladı, embriyolog doğruladı (8 sözcük)

**Ekranda** (aynen):
İhtiyaç → YZ kodlar → test → embriyolog doğrular → sürüm notu
341 commit · 32 gün · 296 sürüm notu
“Oosit sayısı klinik bir sayıdır.” *(v6.19)*
- MII dışı yumurtada enjeksiyon “yapılmadı” *(v1.4)*
- Taşıyıcı etiketi benzersiz *(v3.0)*
- Dejenere yumurta kilitli *(v6.139)*

**Görsel / etkileşim önerisi:** Üstte beş kutulu yatay döngü şeridi (oklar soldan sağa, son kutudan ilk kutuya dönüş oku). Altında üç sayı, büyük puntoyla, `git log`’dan. Ortada tırnaklı alıntı kartı. Altta üç kural kartı; kart tıklanınca o sürüm notundaki kullanıcı cümlesi açılır (ör. v6.139: “ICSI veya Fertilizasyon ekranında dejenere işaretlenen yumurta … işlem yapılamasın”). İsteğe bağlı: 26 commit gününü gösteren küçük takvim şeridi (8 Eylül–9 Ekim 2026).

**Sayılar:**
- 341 commit `[depo_commit]`; 32 takvim günü, 8 Eylül–9 Ekim 2026 `[depo_gun]`; commit atılan gün 26 `[depo_commit_gunu]`
- 296 sürüm notu `[depo_surum_notu]` (34’ü git öncesi v0.1–v5.8; 262’si v6.1–v6.266)
- 341 commit’in 341’inde “Co-Authored-By: Claude” satırı `[depo_claude_ortak]`
- 61 göç betiği `[depo_goc]`; `app.py` 14 214 satır `[depo_app_satir]`

**Sunucu notu** (≈ 105 sözcük, 45 sn):
“Programı ben yazmadım; yapay zekâ yazdı. Ben ne istediğimi embriyolog diliyle söyledim, yapay zekâ kodladı ve kendi testini yaptı, ben ekranda kendi klinik bilgimle doğruladım, her değişiklik neden yapıldığıyla birlikte sürüm notuna yazıldı. Git kaydına göre 32 günde 341 commit, toplamda 296 sürüm notu var. Kuralların çoğu benim bir cümlemden doğdu. Bir gün aynı kare iki kez kaydedilince fotoğrafsız, hayalet bir oosit oluştu; kural şu oldu: oosit sayısı klinik bir sayıdır, şişemez. MII olmayan yumurtada enjeksiyon varsayılan olarak ‘yapılmadı’ gelir, taşıyıcı etiketi iki kez kullanılamaz, dejenere yumurtaya embriyo kaydı girilemez. Sorunu en iyi, o işi yıllarca yapan bilir.”

**Süre (sn):** 45

**Künye satırı:** Patient Data Center git kaydı (14 Kasım 2026’da sayıldı) · README v1.4, v3.0, v6.19, v6.139.

---

### Sahne 5.3 — KPI: program bugün ne hesaplıyor

**Eylem başlığı:** Program beş oranı her ay hesaplıyor; Vienna’yla eşleşmesi kısmi (10 sözcük)

**Ekranda** (tablo, aynen):
| Program (v6.123, v6.241) | Vienna 2017 |
|---|---|
| M2 = MII / yumurta | RI: %75–90 |
| Fertilizasyon = 2PN / ICSI | KPI: ≥%65 · ≥%80 |
| Blastokist = blastokist / 2PN | KPI (5. gün): ≥%40 · ≥%60 |
| Beta hCG (+), klinik gebelik / transfer | lab KPI’sı değil |

Vienna: “ideally on a monthly basis”

**Görsel / etkileşim önerisi:** Solda programın `/istatistik` ekranının **test veritabanıyla** alınmış görüntüsü (ay/yıl seçici, “seçilen ay | tüm zamanlar” sütunları, payı/paydası yazılı). README v6.123’teki test verisi örneği kullanılabilir: 2026-09, M2 20/32 = %62.5, PN 12/20 = %60, blastokist 4/12 = %33.3, klinik gebelik 1/3 = %33.3 — **“TEST VERİSİ” etiketiyle**. Sağda eşleme tablosu; Vienna sütunu “competency · benchmark” biçiminde. Tıklanınca altta tek satır açılır: “Payda sıfırsa oran basılmaz: ‘%0’ değil ‘—’.” Gerçek hasta verisinden ekran görüntüsü **yok**.

**Sayılar:**
- Beş oran: `oran_mii`, `oran_fert`, `oran_blast`, `oran_beta`, `oran_gebelik` (disari.py 1095–1100) `[pdc_oran_sayisi]`
- Beta hCG pozitif eşiği ≥10 mIU/mL `[pdc_beta_esik]`
- Vienna: 19 gösterge = 12 KPI + 5 PI + 2 RI `[vienna_gosterge]`
- ICSI normal fertilizasyon: competence ≥%65, benchmark ≥%80 `[vienna_icsi_fert]`
- Blastokist gelişim (5. gün): competency ≥%40, benchmark ≥%60 `[vienna_blast]`
- ICSI’de MII oranı (RI): beklenen %75–90 `[vienna_mii]`
- Aylık izlem; başlangıç için 30 olgu `[vienna_aylik]`
- Test verisi örneği: M2 20/32 %62.5; PN 12/20 %60; blastokist 4/12 %33.3; klinik gebelik 1/3 %33.3 `[pdc_test_*]`

**Sunucu notu** (≈ 105 sözcük, 45 sn):
“KPI’yı nasıl takip ediyorum? Program bugün beş oranı hesaplıyor: M2, fertilizasyon, blastokist, beta hCG pozitifliği ve transfer başına klinik gebelik. Bunlar bir sayaçta tutulmuyor; ekran her açıldığında kayıtlardan yeniden hesaplanıyor, geçmiş bir kayıt düzeltilince o ayın oranı da düzeliyor. Ay ve yıl seçip bakıyorum, payı ve paydası yanında yazıyor. Vienna konsensüsü göstergelerin ideal olarak aylık izlenmesini öneriyor. Eşleşme kısmi: M2 oranı Vienna’da laboratuvar KPI’sı değil, stimülasyonu yansıtan bir referans gösterge; blastokist tanımı Vienna’da 5. güne bağlı; klinik gebelik ise laboratuvar göstergesi sayılmıyor. Implantasyon oranı ve ICSI hasar oranı için veri alanları programda var ama henüz hesaplanmıyor.”

**Süre (sn):** 45

**Künye satırı:** ESHRE Special Interest Group of Embryology & Alpha Scientists in Reproductive Medicine. Reprod Biomed Online 2017;35:494–510 (PMID 28784335) · Hum Reprod Open 2017;hox011 (PMID 31486806, tam metin) · PDC README v6.38, v6.123, v6.241.

---

### Sahne 5.4 — İleri istatistik: aynı veriyle neler yapılabilir (SENTETİK)

**Eylem başlığı:** CUSUM düşüşü aylık ortalamadan önce yakalıyor; yaş ayarı haksızlığı düzeltiyor (11 sözcük)

**Ekranda** (aynen):
SENTETİK VERİ — klinik bulgu değildir
Erken uyarı (500 simülasyon, %75 → %69):
CUSUM %96.6 yakaladı, medyan 10 hafta
Aylık ortalama %67.2, medyan 14 hafta
Adil karşılaştırma: F ham %68.9 → yaşa ayarlı %75.9

**Görsel / etkileşim önerisi:** İki panel, yan yana. Sol: `sonuc_kpi/fig_kpi_erken_uyari.svg` (haftalık oran, 70. haftada düşüş, CUSUM eşiği 4.5; tek örnekte CUSUM 6 haftada alarm verir, aylık grafik bu örnekte yakalayamaz). Sağ: `sonuc_kpi/fig_funnel_ham.svg` → düğmeyle `fig_funnel_ayarli.svg`’ye geçiş (“Ham / Yaşa göre ayarlı” anahtarı). F noktası huninin içinde yukarı kayar; E iki grafikte de %99.8 sınırının dışında kalır. Her şeklin köşesinde kırmızı “SENTETİK” etiketi. Altta tek satır: “Programda yok; programın tuttuğu türden veriyle yapılabilir.”

**Sayılar:**
- 500 Monte Carlo tekrarı; düşüş sonrası izlem 34 hafta `[cusum_tekrar]`
- Gerçek oran %75 → %69, 70. haftada `[kpi_taban]`, `[kpi_kayma]`
- CUSUM yakalama %96.6, medyan gecikme 10 hafta `[cusum_yakalama]`, `[cusum_gecikme]`
- Aylık (4 haftalık) Shewhart p-grafiği yakalama %67.2, medyan 14 hafta `[shewhart_yakalama]`, `[shewhart_gecikme]`
- Yanlış alarm: CUSUM %4.0, aylık %1.8 `[cusum_yanlis_alarm]`, `[shewhart_yanlis_alarm]`
- CUSUM aylık grafikten önce ya da aynı anda: %88.2 `[cusum_once]`
- Funnel genel oran %71.4; F (n = 90, yaş ort. 39.9): ham %68.9 → ayarlı %75.9 `[funnel_*]`
- E (n = 610): ham %62.8, ayarlı %62.5; iki grafikte de sınır dışı `[funnel_E_*]`
- Literatür bağlantısı: ≥40 yaşta iyi blastokist gelişim oranı %33.4 vs %45.5 (Zacà 2022) `[zaca_tgbdr]`

**Sunucu notu** (≈ 125 sözcük, 55 sn):
“Bu ekranlar programda yok; programın tuttuğu türden veriyle neler yapılabileceğini sentetik veriyle gösteriyorum. Soldaki grafikte bir oran 70. haftada %75’ten %69’a düşüyor; bir lot değişikliği gibi düşünün. Bunu 500 kez simüle ettik. Haftalık CUSUM düşüşü %96.6 oranında, ortanca 10 haftada yakaladı; aylık ortalamaya bakan klasik grafik %67.2 oranında ve 14 haftada. Bedeli biraz daha fazla yanlış alarm: %4’e karşı %1.8. Sağda adil karşılaştırma var. F’nin hastaları daha yaşlı; ham oranı %68.9 ile düşük görünüyor, yaşa göre ayarlayınca %75.9’a çıkıyor. Gerçekten düşük olan E ise iki grafikte de sınırın dışında. Literatür de ileri yaşta blastokist KPI’larının ayarlanması gerektiğini söylüyor. [ONUR’A SOR: kişi bazlı karşılaştırmayı slaytta harfle göstermek uygun mu?]”

**Süre (sn):** 55

**Künye satırı:** Sentetik demo, seed 2027 (`/home/claude/sunum/analiz/sonuc_kpi/sonuclar_kpi.json`) · Vienna istatistiksel süreç kontrolü önerisi ve doğrulaması: Bormann 2021, J Assist Reprod Genet (PMID 33904010) · Zacà 2022, J Assist Reprod Genet (PMID 35338418).

---

### Sahne 5.5 — Benim fikrim ve kapanış

**Eylem başlığı:** Ham değil, kişisel yapay zekâ; embriyolog onun kalite kontrolcüsü (10 sözcük)

**Ekranda** (aynen, üç cümle):
1. Yapay zekâ yaygın; ama hazır model canlı doğumu artırmadı, doğruluğu orta.
2. Ben onu ham değil, kişisel kullanıyorum: ihtiyacı ben söylüyorum, o kodluyor, ben doğruluyorum.
3. Embriyolog işsiz kalmaz; yapay zekânın kalite kontrolcüsü olur.

**Görsel / etkileşim önerisi:** Üç cümle tek tek belirir (tıklamayla). Sağ altta küçük, ikincil kutu: `sonuc_gorsel/fig_ince_ayar.svg` — “Hazır görsel model başka labda AUC 0.51 → 25 yerel etiketle 0.83 (SENTETİK)”. Son tıklamada üç cümle silikleşir, kapanışın üç mesajı (aşağıda) gelir. Arka plan düz; ikon yok.

**Sayılar:**
- Hazır model kendi labında AUC 0.954; başka labda 0.509; 25 yerel etiketle 0.835; 400 etiketle 0.886 (sentetik, 5 tekrar ortalaması) `[gorsel_*]`

**Sunucu notu** (≈ 105 sözcük, 45 sn):
“Benim fikrim şu. Yapay zekâ laboratuvara girdi ve yayıldı; ama gördüğümüz yayınlarda hazır bir model canlı doğumu artırmadı ve doğruluğu orta düzeyde kaldı. Bu yüzden ben onu ham değil, kişisel kullanıyorum: ihtiyacı ben söylüyorum, yapay zekâ kodluyor, ben doğruluyorum. Görsel modeller için de aynısı geçerli: sentetik denememizde başka bir labda yazı-tura düzeyine düşen hazır model, embriyoloğun etiketlediği 25 görüntüyle toparlandı. Embriyolog işsiz kalmayacak; yapay zekâyı etiketleyen, doğrulayan, izleyen ve son kararı veren kalite kontrolcüsü olacak. Üç mesajla bitiriyorum.” *(kapanış mesajları aşağıda; kapanış slaytı ana başlıktaki ≈1 dk’ya aittir)*

**Süre (sn):** 45

**Künye satırı:** Bölüm 3–4 kaynakları (Illingworth 2024 PMID 39122964; Bhide 2026 PMID 42955792; Berntsen 2022 PMID 35108306) · sentetik demo `sonuc_gorsel/sonuclar_gorsel.json`.

---

### Kapanış için önerilen üç mesaj (Onur seçer)

1. **Kendi verini kendin tut:** kaydı olmayan KPI izlenemez. *[ONUR’A SOR: ifade onayı — “kâğıt → Access → kendi programım” tezinden türetildi]*
2. **Hazır modeli ham alma:** kendi labında doğrula, gerekirse kendi etiketinle ayarla. *(onaylı tez: “ham değil, kişisel yapay zekâ”; “görsel modelleri yerelde kendi etiketleriyle eğitmek”)*
3. **Embriyolog yapay zekânın kalite kontrolcüsüdür:** ihtiyacı söyler, sonucu doğrular, kararı verir. *(onaylı tez)*

### Yedek sahneler (soru-cevap için; 4 dakikaya girmez)

- **Y1 — Kalite kontrol izlemi (sentetik):** model–embriyolog haftalık uyumu %76.7; 19. haftada kamera değişimiyle en düşük %23.3’e iniyor; EWMA alarmı 19. haftada; 90 yerel etiketle 21. haftada yeniden ince ayar; son 8 hafta %73.3. Şekil: `sonuc_gorsel/fig_kalite_kontrol.svg`.
- **Y2 — Sızıntı ve doğrulama (sentetik):** 700 hasta, 1 065 siklus, 4 428 embriyo; gradyan artırma rastgele bölmede AUC 0.686, hasta-gruplu bölmede 0.646 (%95 GA 0.629–0.660), zamansal bölmede 0.667; lojistik regresyon 0.706 / 0.704 / 0.699. Şekil: `sonuc_slayt/fig_auc_dogrulama.svg`. Mesaj: aynı hastanın embriyoları eğitim ve testte bölününce başarı olduğundan iyi görünür.

---

## Programın bugünkü KPI’ları — koddan doğrulama (sunucu için arka plan)

Kaynak: `disari.py` `istatistikler()` (satır 961–1101), `_oran()` (1104–1108), `istatistik_aylari()` (1111–1155); ekran `app.py` `istatistik_ekrani()` (5792–5832), şablon `templates/istatistik.html` (93–118).

| Oran (ekran etiketi) | Pay | Payda | Vienna 2017 karşılığı | Fark |
|---|---|---|---|---|
| M2 oranı (MII / kayıtlı yumurta) | maturasyon kontrolünde `mii`, FET tipleri hariç | kayıtlı oosit, FET tipleri hariç | RI “Proportion of MII oocytes at ICSI”, %75–90 | Vienna’da **laboratuvar KPI’sı değil**; stimülasyonun vekili |
| Fertilizasyon oranı (2PN / ICSI) | fert. kontrolünde `fert_pn_sayisi = '2'` | iptal edilmemiş `icsi` olayı olan örnek | KPI ICSI normal fert.: 2PN+2PB / enjekte MII; ≥%65 · ≥%80 | Payda “ICSI yapılan” (MII dışı enjeksiyon elle açılabilir, v1.4); 2PB aranmıyor; Vienna TESE spermini dışlar, program dışlamıyor |
| Blastokist oranı (blastokist / 2PN) | blastokist ekranında **herhangi bir** değerlendirme kaydı olan örnek | 2PN | KPI: 5. gün (116 ± 2 sa) blastokist / 2PN; ≥%40 · ≥%60 | **Önemli:** pay morula, kavitasyon ve arrest kayıtlarını da (gün 4–7) sayıyor (app.py 8253, 8412; disari.py 1020) → oran Vienna tanımından yüksek çıkabilir. **[ONUR’A SOR: düzeltilsin mi, slaytta “Vienna’ya uygun” denmesin]** |
| Beta hCG pozitif oranı | ≥10 mIU/mL değeri olan tedavi | transfer yapılan tedavi | yok | — |
| Klinik gebelik oranı (transfer başına) | elle işaretlenen klinik gebelik | transfer yapılan tedavi | Vienna: canlı doğum laboratuvar göstergesi olarak önerilmez; KPI implantasyon = kese / transfer edilen embriyo | Implantasyon hesaplanmıyor; `gebelik_kesesi_sayisi` alanı şemada var |

Ek: ay ölçüsü OPU tarihi, yoksa tedavinin açılış tarihi; Cryo Excel’inden açılan program öncesi tedaviler oranlara girmez; payda sıfırsa oran `None` → ekranda “—” (v6.38). Programda **kişi bazlı (embriyolog) KPI ekranı yok**; ancak “işlemi yapan” aşama başına kayıtlı (v6.3, v6.99), funnel’ın verisi bu alandan türetilebilir. ICSI hasar oranı (`icsi_sonuc = 'degenere'`) için veri var, oran yok.

---

## Kaynaklar

### A. Depo kaynakları (Patient Data Center, `/home/claude/Patient-Data-Center`, 14 Kasım 2026 klonu, son commit 487f86a, 9 Ekim 2026)

| Anahtar | Sürüm | README satırı | İddia |
|---|---|---|---|
| depo_v0.2 | v0.2 | 181 (başlık), 213 | `degisiklik_log`: hangi alan, eski/yeni değer, kim, ne zaman |
| depo_v1.2 | v1.2 | 465, 517 | Otomatik yedek; son yedek 3 günden eskiyse turuncu uyarı |
| depo_v1.4 | v1.4 | 596, 614 | MII dışı maturasyonda enjeksiyon kendiliğinden “yapılmadı”; elle açılabilir |
| depo_v3.0 | v3.0 | 875, 895, 911 | Taşıyıcı etiketi lab genelinde benzersiz; cryo haritası türetilir, elle güncelleme yok |
| depo_v3.8 | v3.8 | 1050, 1063, 1068 | Snapshot → “Bu kareyi oosit N’e ekle”; klasör izleme/aşama/oosit seçme adımları kalktı |
| depo_v6.1 | v6.1 | 1452 | Claude Code’a geçiş, git deposu |
| depo_v6.3 | v6.3 | 1551, 1559 | “İşlemi yapan” her aşamada, kaydı girenden ayrı |
| depo_v6.19 | v6.19 | 2637, 2660 | Hayalet oosit; “Oosit sayısı klinik bir sayıdır.” |
| depo_v6.37 | v6.37 | 3899, 3902 | Resmî formlar kayıttan basılıyor (yazdırma + Excel) |
| depo_v6.38 | v6.38 | 4000, 4006, 4024 | İstatistik hesaplanır, saklanmaz; paydası sıfır oran basılmaz |
| depo_v6.55 | v6.55 | 5529, 5553 | Aynı kaydı iki kişi düzenlerse uyarı (engellemez) |
| depo_v6.92 | v6.92 | 7741 | Fotoğraf kimliği yeniden kullanılıyordu → yanlış eşleşme düzeltildi |
| depo_v6.99 | v6.99 | 8100, 8103 | İşlemi yapan, şifreli kullanıcılardan seçiliyor |
| depo_v6.110 | v6.110 | 8660 | Tedavi ekranında türetilmiş embriyoloji özeti |
| depo_v6.123 | v6.123 | 9476, 9479, 9493, 9576, 9579 | Aylık dört oran, yıl/ay seçici; test verisi örneği |
| depo_v6.125 | v6.125 | 9698, 9716 | Dosya no ile eşleştirme; isimle eşleştirme bilerek yok |
| depo_v6.130 | v6.130 | 9965, 9971 | Program öncesi Access kayıtlarının aktarımı |
| depo_v6.139 | v6.139 | 10942, 10965 | Dejenere yumurta görünür ama kilitli |
| depo_v6.179 | v6.179 | 14036 | Cryo Excel’inden 2011–2017 hastaları |
| depo_v6.190 | v6.190 | 14955, 14958 | Dondururken boş yer önerisi (“ben kendim aramayım”) |
| depo_v6.201 | v6.201 | 15633, 15640 | Sağlık Bakanlığı aylık verileri, kayıttan türetilir |
| depo_v6.219 | v6.219 | 17133, 17137 | Bulaş hastalığı: kimlik bandında kırmızı uyarı |
| depo_v6.227 | v6.227 | 17742, 17765 | Tüp imha kaydı; tüp haritadan çıkar |
| depo_v6.241 | v6.241 | 19047, 19051 | Beta hCG ≥10 mIU/mL → gebelik testi pozitif (türetilir) |
| depo_v6.251 | v6.251 | 20127 | Kasım–aralık 2017 Access kayıtları |
| depo_v6.266 | v6.266 | 20585 | Son sürüm |
| depo_kod_istatistik | — | `disari.py` 961–1155; `app.py` 5766–5832; `templates/istatistik.html` 93–118; `metinler.py` 2892–2898 | Beş oranın tanımı |
| depo_kod_blast | — | `app.py` 8253 (`BLAST_DISI`), 8412 (kayıt); `disari.py` 1020 | Blastokist payı morula/kavitasyon/arrest’i de sayıyor |
| depo_claude_md | — | `CLAUDE.md` 9–20 (proje, kullanıcı), 746 (kimlik her ekranda), 5173–5181 (çalışma kuralı: “Klinik bir varsayım yapman gerekiyorsa yapma — kullanıcıya sor.”) | Geliştirme döngüsü |
| depo_git | — | `git log` (14 Kasım 2026’da sayıldı) | 341 commit; ilk 8 Eylül, son 9 Ekim 2026; 26 commit günü; yazar alanı 330 “Claude”, 11 kullanıcı; 341’inde Claude ortak yazar satırı; +110 132 / −13 440 satır |

Sayım yöntemi: sürüm notu = README’de `^# v` ile başlayan başlık (296; 34’ü satır 1452’den önce). Göç betiği = `goc.py` + `goc_0XX.py` (61; `goc_hepsi.py` hariç).

### B. Sentetik demo dosyaları (hepsi `veri_kaynagi: SENTETIK`, seed 2027)

| Anahtar | Yol | İçerik |
|---|---|---|
| demo_kpi | `/home/claude/sunum/analiz/sonuc_kpi/sonuclar_kpi.json` | CUSUM / Shewhart tek örnek ve 500 tekrar; funnel A–F |
| demo_kpi_sekil | `/home/claude/sunum/analiz/sonuc_kpi/fig_kpi_erken_uyari.svg`, `fig_funnel_ham.svg`, `fig_funnel_ayarli.svg` | Sahne 5.4 şekilleri |
| demo_gorsel | `/home/claude/sunum/analiz/sonuc_gorsel/sonuclar_gorsel.json` | İnce ayar eğrisi; kalite kontrol izlemi |
| demo_gorsel_sekil | `/home/claude/sunum/analiz/sonuc_gorsel/fig_ince_ayar.svg`, `fig_kalite_kontrol.svg` | Sahne 5.5 ve Y1 |
| demo_dogrulama | `/home/claude/sunum/analiz/sonuc_slayt/sonuclar.json` (`sonuc/sonuclar.json` ile aynı) | Y2: rastgele / hasta-gruplu / zamansal AUC |
| demo_betik | `/home/claude/sunum/paket/scripts/kpi_demo.py`, `gorsel_demo.py` | Gerçek parametreler kodda yazılı |

### C. Literatür

| Anahtar | Künye | PMID | DOI | Okuma | Tasarım | Çıkar / sponsor |
|---|---|---|---|---|---|---|
| vienna_rbmo | ESHRE SIG Embryology & Alpha Scientists in Reproductive Medicine. The Vienna consensus: report of an expert meeting on the development of ART laboratory performance indicators. Reprod Biomed Online 2017;35(5):494–510 | 28784335 | 10.1016/j.rbmo.2017.06.015 | yalnız özet (PMC’de yok) | Uzman konsensüsü | ESHRE ve Alpha destekli çalıştay |
| vienna_hro | Aynı rapor, Hum Reprod Open 2017;hox011 | 31486806 (PMC6276649) | 10.1093/hropen/hox011 | tam metin (PMC; tablolar metne gelmedi) | Uzman konsensüsü | Aynı |
| bormann_2021 | Bormann CL ve ark. Deep learning early warning system for embryo culture conditions and embryologist performance in the ART laboratory. J Assist Reprod Genet 2021;38(7):1641–6 | 33904010 | 10.1007/s10815-021-02198-x | yalnız özet | Retrospektif, yöntem gösterimi | Çıkar beyanı bu oturumda okunmadı |
| zaca_2022 | Zacà C ve ark. Fine-tuning IVF laboratory key performance indicators of the Vienna consensus according to female age. J Assist Reprod Genet 2022;39(4):945–52 | 35338418 | 10.1007/s10815-022-02468-2 | yalnız özet (PMC kaydı tam metin döndürmedi) | Retrospektif kohort, 862 siklus | Tek merkez (özel) |
| illingworth_2024, bhide_2026, berntsen_2022 | Ortak bağlamda doğrulanmış; Bölüm 3–4’ün kaynakları | 39122964; 42955792; 35108306 | ortak bağlamda | ortak bağlama göre | — | Illingworth: Vitrolife finansmanı; Berntsen: Vitrolife yazarlar |

---

## Doğrulanamayanlar ve uyarılar

1. **Zaman tasarrufu ölçülmedi.** “Şu kadar dakika kazandık” iddiası yok. [ONUR’A SOR: kendi deneyiminizden bir süre örneği? (ör. aylık Bakanlık tablosu veya yıl sonu KPI sayımı eskiden ne kadar sürüyordu?)]
2. **“KPI’yı yıl sonunda elle saymak”** önceki durumunu depo belgelemiyor; Sahne 5.1’de bu yüzden yalnız “oranlar her ay kendiliğinden” dendi. [ONUR’A SOR: program öncesi KPI nasıl, ne sıklıkla sayılıyordu?]
3. **Blastokist oranı tanımı Vienna’dan geniş** (morula/kavitasyon/arrest ve gün 4–7 dahil). Slaytta “Vienna KPI’sı hesaplanıyor” denmemeli; “Vienna’yla eşleşme kısmi” dendi. [ONUR’A SOR: pay yalnız 5. gün gerçek blastokistle sınırlansın mı?]
4. **Fertilizasyon paydası** “ICSI yapılan”dır, “enjekte edilen MII” değil; TESE dışlanmıyor; 2PB aranmıyor. Fark küçük olabilir ama tanım birebir değil.
5. **Vienna tam metninde tablolar metne gelmedi.** Implantasyon eşiklerinin (≥%25/≥%35 ve ≥%35/≥%60) hangi transfer gününe ait olduğu etiketler kesildiği için metindeki sıradan çıkarıldı (önce gün 2–3, sonra blastokist); bu yüzden slayta konmadı. 12 KPI’nın tam listesi tablodan doğrulanamadı → DOĞRULANAMADI.
6. **Kurum adı uyarısı:** README v6.37 (satır 3899–3910) resmî formların ait olduğu kurumu ve form kodlarını adıyla yazıyor. Ortak kurala göre merkez adı slayta girmez: form ekran görüntüsü kullanılmamalı, form kodu yazılmamalı.
7. **Programda olmayanlar:** CUSUM, funnel, yaşa göre ayar, görsel model ince ayarı, kalite kontrol izlemi ve sızıntı analizi **programda yoktur**; sentetik demolardır. [ONUR’A SOR: “programa eklemeyi planlıyorum” denebilir mi?]
8. **Kişi bazlı karşılaştırma:** funnel A–F “embriyolog” harfleri sentetiktir; gerçek ekip verisi gösterilmemeli. [ONUR’A SOR: slaytta “embriyolog” yerine “operatör/vardiya” denmesi tercih edilir mi?]
9. **Git öncesi dönem:** v0.1–v5.8 (34 sürüm notu) git kaydından önce; bu dönemin de yapay zekâyla yazılıp yazılmadığı depoda açık değil (v6 başlığı “Claude Code dönemi”). “32 günde 341 commit” yalnız git dönemini anlatır. [ONUR’A SOR: v0.1’in başlangıç tarihi ve o dönemde hangi araç kullanıldı?]
10. Commit sayısı, gün sayısı ve sürüm notu sayısı bu oturumda yeniden hesaplandı ve ortak bağlamla (341 / 8 Eylül–9 Ekim / 296) aynı çıktı. “Test edildi/Denendi” ibaresi 296 sürüm notunun 155’inde geçiyor (kendi düzenli ifade sayımımız, yaklaşık); slayta konmadı.
11. Sentetik sonuçlar klinik bulgu değildir; her şeklin köşesinde “SENTETİK” etiketi bulunmalı. Programdan alınacak ekran görüntüsü yalnız test veritabanından olmalı.
