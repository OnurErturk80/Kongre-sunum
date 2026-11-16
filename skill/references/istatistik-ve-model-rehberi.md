# İleri istatistik ve model eğitimi rehberi (klinik embriyoloji)

Hedef: dergi (Human Reproduction, Fertility and Sterility, RBMO, JARG düzeyi) hakemini
tatmin edecek metodoloji, 15-20 dakikalık sözlü sunuma sığacak biçimde. Sunumda hepsini
anlatma; bu dosya senin **arka plan bilgin**. Slaytta yalnızca 3-4 fikir taşınır.

İçindekiler: 1 Analiz birimi · 2 Yöntem seçimi · 3 Sonuç tanımları · 4 Yanlılıklar ·
5 Eksik veri · 6 Model eğitimi · 7 Metrikler · 8 Raporlama kılavuzları · 9 Demo betikleri ·
10 Kod disiplini

---

## 1. Analiz birimi: embriyolar bağımsız değildir

Hiyerarşi: **hasta → siklus → oosit/embriyo** (ve hastanın birden fazla siklusu olabilir).
Aynı hastanın embriyoları aynı yaşı, AMH'yi, protokolü, uyarım yanıtını, kültür koşulunu,
sperm örneğini paylaşır. Gözlenmeyen hasta düzeyi etki varsa gözlemler korelasyonludur.

Bunu yok saymanın iki sonucu (demo bunu gösterir):
1. **Yapay olarak dar güven aralıkları, abartılı anlamlılık.** En çok hasta düzeyinde sabit
   değişkenlerde (yaş, AMH) olur; embriyo içi değişkenlerde (morfoloji) etki daha küçüktür.
   Bunu "her zaman çok büyük" diye anlatma; demo çıktısı ne diyorsa onu söyle.
2. **Makine öğrenmesinde doğrulama sızıntısı.** Embriyoları rastgele eğitim/test'e bölersen
   aynı hastanın kardeş embriyoları iki tarafa düşer; esnek model hastanın "parmak izini"
   (ör. BMI gibi hastaya özgü sürekli değişkenler) ezberler. AUC şişer. Basit modeller
   (lojistik regresyon) bundan genellikle daha az etkilenir.

Birim seçimini tablo haline getir: araştırma sorusu → birim → neden.
- "Bu embriyo blastokist olur mu?" → embriyo düzeyi, hasta kümeli.
- "Bu protokol daha çok MII verir mi?" → siklus düzeyi (hasta kümeli).
- "Bu hasta kaç siklusta canlı doğuma ulaşır?" → hasta düzeyi, kümülatif sonuç.

## 2. Yöntem seçimi

| Durum | Yöntem | Not |
|---|---|---|
| Popülasyon ortalaması etkisi, kümeli ikili sonuç | **GEE** (exchangeable), hasta kümesi | Dayanıklı (sandwich) SE; küme sayısı < ~30-40 ise küçük örnek düzeltmesi |
| Hasta/siklus'a özgü (koşullu) etki, iç içe düzey | **GLMM** (hasta ve siklus rastgele kesişim) | Yorum koşulludur; OR'lar GEE'den farklı olabilir; ikisinin farkını açıkla |
| Sadece güven aralığı lazım, model karmaşık | **Küme (hasta) bootstrap** | Embriyoları değil hastaları yeniden örnekle |
| Birkaç embriyo transferi, sonuç embriyoya atfedilemiyor | Siklus/transfer düzeyi analiz | Embriyo düzeyi implantasyon yalnızca SET'te (tek embriyo transferi) temiz |
| Kümülatif canlı doğum | Zaman-olay (Kaplan-Meier, Cox, rekabetçi riskler) | Tedaviyi bırakma (drop-out) bilgilendirici sansür olabilir |
| Küçük örnek / ön bilgi var | Bayesci hiyerarşik model | Ön dağılımı açıkça raporla |
| Gözlemciler arası uyum (embriyolog vs embriyolog / yapay zekâ) | Cohen/Fleiss kappa (ağırlıklı), ICC, Bland-Altman | Referans standart sorunu: "gerçek" etiket kimin? |

Çoklu karşılaştırma: önceden tanımlı birincil sonuç; ikincilleri keşif olarak etiketle;
gerekirse Holm/FDR. p-değeriyle birlikte **etki büyüklüğü ve GA** ver. Tek başına p yok.

## 3. Sonuç tanımları ve paydalar

Oranlar paydaya göre anlam değiştirir; slayta yazmadan paydayı yaz. Örnekler: fertilizasyon
(2PN / enjekte edilen MII veya inseminasyon yapılan oosit), blastulasyon (blastokist / 2PN
veya / gün 3 gelişen embriyo), kullanılabilir blastokist (hangi derece, hangi gün),
implantasyon (gebelik kesesi / transfer edilen embriyo), klinik gebelik, devam eden gebelik,
canlı doğum (transfer başına, başlanan siklus başına, kümülatif). Tanım kaynağı olarak
Istanbul Consensus (2011) ve Vienna Consensus (2017) laboratuvar gösterge tanımlarını kullan;
**tam künyeyi PubMed ile doğrula** (`kaynak-dogrulama.md`).

## 4. Yanlılıklar (hakem bunları sorar)

- **Seçim (selection) yanlılığı / sonuç yalnızca transfer edilenlerde bilinir.** Embriyo
  seçim modeli yalnızca transfer edilmiş embriyolarda eğitilirse, seçilmeyenlerin kaderi
  bilinmez; model embriyologun seçimini öğrenir. Bunu açıkça belirt, "tüm embriyolar için
  geçerli" iddiası kurma. PGT sonuçlu ve transfer edilmeyen embriyolar ayrı bir bilgi kaynağıdır.
- **Karıştırıcılar:** maternal yaş, AMH, protokol, sperm kalitesi, endikasyon, merkez/operatör, dönem.
- **Aracı (mediator) ve çarpışan (collider) değişkenler:** gün 3 morfolojisi yaşın etkisini
  aracılar; ona kontrol etmek toplam etkiyi değiştirir. Nedensel soru varsa DAG çiz.
- **Hedef sızıntısı (leakage):** tahmin anında bilinmeyen değişkeni özellik olarak kullanmak
  (ör. gün 5 morfolojisi ile gün 3'te blastokist tahmini). Her özellik için "ne zaman bilinir"
  zaman damgası tablosu tut.
- **Zaman kayması (dataset shift):** kültür ortamı, inkübatör, protokol, personel değişir;
  model sabitken dünya değişir. Zamansal doğrulama bunu yakalar, rastgele bölme yakalamaz.
- **Tek merkez:** dış geçerlik iddiası kurma; harici doğrulama yoksa sınırlılık olarak yaz.

## 5. Eksik veri

Eski kayıtlar (Access dönemi) alan alan eksik olabilir. "Boş = 0" ya da "boş = normal"
varsaymak sessiz yanlılıktır. Eksiklik mekanizmasını sınıflandır (MCAR/MAR/MNAR), eksiklik
oranını tablo yap, çoklu atama (MICE) ya da tam-olgu duyarlılık analizi ile sonucun
dayanıklılığını göster. Sistemde "kaydedilmedi" ile "yapılmadı" ayrımı varsa (ör. Ağustos 2018
laboratuvarda hiç işlem yapılmadı) bunu kodla ayır.

## 6. Model eğitimi: dürüst yöntem

Sıra: (1) soru ve tahmin anı tanımı → (2) özellik zaman tablosu → (3) bölme stratejisi →
(4) temel (baseline) model → (5) karmaşık model → (6) kalibrasyon → (7) iç ve dış doğrulama → (8) rapor.

- **Bölme:** hasta düzeyinde gruplu (GroupKFold / aynı hastanın tüm siklusları aynı katlama),
  ayrıca zamansal bölme (eski → yeni). Hiperparametre ayarı gerekiyorsa **iç içe (nested)**
  çapraz doğrulama; test kümesine hiç bakma.
- **Ön işleme sızıntısı:** ölçekleme/atama/özellik seçimi her katlama içinde, yalnızca eğitim
  verisiyle fit edilir (sklearn `Pipeline`).
- **Baseline her zaman:** yaş + birkaç klinik değişkenli lojistik regresyon. Karmaşık model
  bunu **anlamlı biçimde** geçmiyorsa karmaşıklığı savunamazsın. Demo bunu gösteriyor:
  rastgele bölmede esnek model iyi görünür, gruplu bölmede lojistik regresyonun gerisine düşebilir.
- **Örneklem büyüklüğü:** tahmin modeli için minimum örneklem hesabı (Riley ve ark. yaklaşımı;
  künyeyi doğrula). "Olay/değişken ≥ 10" kaba bir kuraldır, yeterli değildir.
- **Açıklanabilirlik:** SHAP/permütasyon önemi *model* davranışını açıklar, *biyolojiyi*
  açıklamaz; nedensellik iddiası taşımaz. Görüntü modellerinde ısı haritaları (Grad-CAM vb.)
  güvenilir kanıt değil, hata ayıklama aracıdır; öyle anlat.
- **Görüntü / time-lapse:** etiket (ground truth) nedir, kim koydu, gözlemciler arası uyum
  nedir? Veri artırma ve aynı embriyonun birden fazla karesi de kümeleme sızıntısıdır:
  bölmeyi embriyo/hasta düzeyinde yap, kare düzeyinde değil.
- **Alt grup ve adalet:** yaş bandı, endikasyon, merkez/dönem bazında performans ve
  kalibrasyon. Genel AUC alt grupta çökmüş olabilir.

## 7. Metrikler (tek sayıyla yetinme)

- **Ayırt edicilik:** AUC (küme bootstrap GA ile). Nadir olayda PR-AUC.
- **Kalibrasyon (en çok ihmal edilen):** kalibrasyon eğimi (ideal 1), "içinde-kalibrasyon"
  kesişimi (ideal 0), kalibrasyon eğrisi, Brier. Zaman kaymasında önce bozulan genelde kalibrasyondur.
- **Klinik fayda:** karar eğrisi analizi (net fayda) ve eşik tartışması: "hangi olasılıkta
  hangi eylem?" Doğruluk (accuracy) tek başına yanıltıcıdır.
- **Belirsizlik:** her metriğe GA. Nokta tahmin tek başına sunulmaz.

## 8. Raporlama kılavuzları (sunumun son slaytında ve özette ad ver)

- **TRIPOD+AI (2024):** tahmin modeli geliştirme/doğrulama raporlama (TRIPOD'un yapay zekâyı kapsayan güncellemesi).
- **PROBAST+AI:** tahmin modeli yanlılık riski değerlendirmesi.
- **STROBE / RECORD:** gözlemsel ve rutin toplanan sağlık verisi çalışmaları.
- **CONSORT-AI / SPIRIT-AI / DECIDE-AI:** müdahale olarak yapay zekâ içeren çalışmalar (RCT, erken klinik değerlendirme).
- **CLAIM:** tıbbi görüntüleme yapay zekâsı.
Her kılavuzun güncel künyesini ve kapsamını kullanmadan önce doğrula.

## 9. Demo betikleri (`scripts/`)

1. `sentetik_veri.py` hasta → siklus → embriyo hiyerarşisi; gerçek parametreler kodda yazılı
   (yaş etkisi −0.09/yıl, embriyo kalitesi 0.80, hasta SD 0.80, siklus SD 0.40, 2023 sonrası +0.35 kayma).
2. `analiz_demo.py` üç gösterim: (a) naif lojistik vs GEE güven aralıkları, (b) rastgele vs
   hasta-gruplu vs zamansal doğrulama (gradyan artırma ve lojistik), (c) zamansal test kümesinde
   kalibrasyon, (d) karar eğrisi. Tüm sayılar `sonuc/sonuclar.json`'a yazılır.

Seed 2027, 700 hasta ile **tipik** çıktı (her çalıştırmada `sonuclar.json`'dan yeniden oku):
gradyan artırma AUC ≈ 0.69 (rastgele) → ≈ 0.65 (hasta-gruplu); lojistik ≈ 0.70 hemen hemen
değişmez; yaş katsayısında GEE güven aralığı naife göre ≈ %18 daha geniş, embriyo içi
değişkenlerde ≈ aynı.

**Dürüstlük kuralı:** demoyu "daha çarpıcı görünsün" diye ayarlama. Parametreleri değiştirirsen
(ör. daha büyük hasta SD) bunu slayt notunda ve yöntemde belirt; çünkü sızıntı şiddeti
senaryoya bağlıdır. Sentetik veriyle elde edilen sayı klinik bulgu değildir; her şekilde
"SENTETİK VERİ" etiketi bulunmalıdır (betik bunu otomatik koyar).

Gerçek (anonim, etik onaylı) veriye uygularken: sütun adlarını eşle, `OZELLIKLER` listesini
özellik zaman tablosuna göre değiştir, `--etiket` değerini veri açıklamasıyla değiştir
(ör. "Tek merkez, 2019-2025, n=…, retrospektif").

## 10. Kod disiplini (yapay zekâ ile istatistik yaparken)

- Hiçbir sayıyı elle yazma: slayttaki her sayı koddan gelsin (`sonuclar.json`), kod sürümlü olsun.
- `seed`, kütüphane sürümleri (`pip freeze`), veri özeti (satır sayısı, hash) kaydet.
- Yapay zekânın yazdığı analiz kodunu **çalıştır ve çıktıyı kontrol et**; makul görünen kod
  yanlış olabilir. Basit bir kontrol: bilinen gerçeği olan sentetik veriyle önce yöntemi sına.
- Slayta koymadan önce sonucu **bağımsız yoldan bir kez daha** doğrula (ör. GEE sonucunu
  küme bootstrap ile çapraz kontrol).
