---
name: "embriyoloji-ai-kongre-sunumu"
description: Klinik embriyoloji / IVF kongresi için, yapay zekânın laboratuvar iş akışına entegrasyonu ve ileri istatistik (kümeli veri, GEE, model eğitimi, sızıntısız doğrulama, kalibrasyon, karar eğrisi) konulu, dergi kalitesinde akademik sunum üretir; etkileşimli çevrimdışı HTML sunum, yedek PDF/PPTX, sunucu notları, soru-cevap. Patient-Data-Center (IVF kayıt programı) deposunu anlatıya bağlar. Kullanıcının seçtiği makalelerin sunuma uygun olup olmadığını gerekçeyle değerlendirir (kimlik doğrulama, iddia-kaynak eşlemesi, kapsam boşlukları). Kullanıcı makale, kaynak, atıf, literatür, "bu makale uygun mu", DOI/PMID listesi, kongre/akademik sunum, embriyoloji/IVF laboratuvarı, yapay zekâ ile yazılım geliştirme, embriyo seçimi modeli, istatistik, sızıntı, AUC, kalibrasyon, TRIPOD, özet bildiri, poster, slayt ya da "sıradan PowerPoint olmasın" dediğinde mutlaka kullan.
---

# Klinik embriyoloji kongresi: yapay zekâ ve ileri istatistik sunumu

Bu skill, Türkçe 15-20 dakikalık bir akademik sözlü sunumu **uçtan uca** üretir:
anlatı, çalışan istatistik demosu, etkileşimli HTML sunum, yedek PDF/PPTX, sunucu
notları ve soru-cevap hazırlığı. Hedef: dergi hakeminin ve salondaki embriyologun aynı anda
saygı duyacağı, ama sıradan bir PowerPoint gibi görünmeyen bir sunum.

## Bu skill'in dayandığı üç karar (neden böyle?)

1. **Çıktı: etkileşimli HTML + yedekler.** Kullanıcı hem web sunumu hem PDF/PPTX yedeği istedi.
   Kongre salonlarında internet ve font sorunu olur; bu yüzden HTML tek dosyada, çevrimdışı,
   fontları gömülü çalışır. PDF ve PPTX aynı kaynaktan türer, birbiriyle uyumsuz olmaz.
2. **Veri: yalnızca sentetik.** Kullanıcı gerçek hasta verisi kullanmayacağını açıkça belirtti
   (10 Kasım 2026). Bu yüzden tüm istatistik/model gösterimi sentetik kohorttan gelir: hasta riski
   sıfır, gerçek etki büyüklükleri bilinir, yöntem doğrulanabilir. Bu konuyu yeniden sorma; ekran
   görüntüsü gerekirse yalnızca kimliksiz test veritabanından alınır. Ayrıntı: `references/etik-ve-veri.md`.
3. **Anlatı: kişiselleştirilmiş yapay zekâ (kullanıcının seçimi, 10 Kasım 2026).** Tez: yapay zekâyı
   ham kullanmak yerine embriyoloğun tecrübesiyle kişiselleştirmek. Omurga: kâğıt → bilgisayar → kendi
   programı (PDC) → yapay zekâ; kayıt ve güvenlik; KPI takibinde yapay zekâ desteği (erken uyarı, adil
   karşılaştırma); laboratuvarda yapay zekânın diğer alanları ve ne kadar güvenli olduğu; embriyolog
   "yapay zekânın kalite kontrolcüsü"; görsel modeli yerelde eğitmek. İlk taslaktaki "istatistik
   tuzakları" anlatısı kullanıcı tarafından **reddedildi**; onu ana tez yapma (yalnız bir kanıt olarak
   sahne 12'de kısa yer alır). Ayrıntı: `references/anlati-ve-sahneler.md` başı.
4. **Dürüstlük kuralı.** Akademik sahnede en pahalı hata uydurulmuş sayı, uydurulmuş atıf ve
   programın olmadığı bir yeteneğe sahip gibi sunulmasıdır. Bu yüzden: sayılar koddan gelir,
   atıflar PubMed ile doğrulanır, program yalnızca gerçekte ne yapıyorsa o olarak anlatılır.

## Kullanıcı ve proje bağlamı

- Kullanıcı: 22 yıllık embriyolog, Python/yazılımda yeni; klinik doğrulukta uzman. Teknik
  kararları kısaca gerekçelendir; klinik kararları ona sor. Dil: Türkçe; klinik terimler İngilizce
  (blastocyst, ICSI, PN, ICM, TE, FET, PGT).
- Program: **Patient Data Center** (https://github.com/OnurErturk80/Patient-Data-Center),
  IVF laboratuvarı kayıt sistemi, Claude Code ile geliştirildi. İçinde makine öğrenmesi modeli
  **yok**; yapay zekâ burada geliştirme aracı ve veri altyapısının temelidir. Ayrıntılı ve
  doğrulanmış özet, anlatıya uygun gerçek parçalar ve depo hijyeni kontrolü:
  `references/proje-patient-data-center.md` (**önce oku**).

## İş akışı

Aşamaları sırayla yürüt. Kullanıcıdan yalnızca eksik ve gerçekten karar gerektiren şeyleri
sor (bir seferde en çok 2-3 soru, mümkünse seçenekli). Zaten bilinen bir şeyi tekrar sorma.

### 1. Bağlamı topla (kısa)
Kongre adı/tarihi/oturum süresi, hedef kitle (embriyologlar mı, klinisyenler mi, karışık), kendi
tez cümlesi ya da `references/anlati-ve-sahneler.md`'deki üç adaydan hangisi, ondalık ayırıcı
tercihi (nokta/virgül), kullanıcı adı-kurum-çıkar çatışması beyanı. Kongre duyurusunda
yapay zekâ ve görsel politikası varsa öğren. (Veri kararı verildi: sentetik; sorma.)

### 2. Depoyu yeniden oku ve hijyen kontrolü yap
`git clone --depth 1` ile güncel depoyu al (bash ağı GitHub'a açık), sürüm/modül sayılarını
**güncelle**, `references/proje-patient-data-center.md` içindeki hijyen komutlarını çalıştır.
Bulguyu kullanıcıya açıkça raporla (özellikle herkese açık depoda veri/kimlik bulursan).
Depo ulaşılamazsa referans dosyasındaki sayılara "9 Kasım 2026 itibarıyla" notu düşerek devam et.

### 3. Demoları üret ve oku
```bash
python3 scripts/kpi_demo.py --cikti-dir analiz/sonuc_kpi --slayt          # CUSUM vs aylık ortalama (500 simülasyon), funnel ham/ayarlı
python3 scripts/gorsel_demo.py --cikti-dir analiz/sonuc_gorsel --slayt    # sentetik embriyo görüntüleri: hazır model vs yerel ince ayar; kalite kontrol izlemi
python3 scripts/sentetik_veri.py --n-hasta 700 --seed 2027 --cikti analiz/sentetik_kohort.csv
python3 scripts/analiz_demo.py --veri analiz/sentetik_kohort.csv --cikti-dir analiz/sonuc
python3 scripts/analiz_demo.py --veri analiz/sentetik_kohort.csv --cikti-dir analiz/sonuc_slayt --slayt
```
`statsmodels`, `scikit-learn`, `matplotlib` gerekir (`pip install ... --break-system-packages`).
`sonuclar.json`'u oku ve ne bulunduğunu **olduğu gibi** anlat. Beklenmeyen çıkarsa (ör. sızıntı
görünmedi) bunu sakla/ayarla değil, sun: "bu senaryoda etki küçük" geçerli bir bulgudur.
Metodoloji arka planı ve hakem soruları: `references/istatistik-ve-model-rehberi.md`.

### 4. Makaleleri değerlendir ve atıfları doğrula
Makaleleri **kullanıcı belirler**; sen her birinin sunum konusuna ve sahnelerine **uygun olup
olmadığını** değerlendirirsin. `references/makale-uygunluk.md` protokolünü uygula: PubMed
araçlarını `tool_search` ile yükle; her makale için kimlik ve statü doğrula (geri çekilme, ön baskı,
düzeltme), ne kadarını okuduğunu etiketle (tam metin / yalnız özet), dört eksende değerlendir
(konu-sahne uygunluğu, iddia-kaynak uyumu, kanıt kalitesi, güncellik), her biri için ✅ / ◐ / ✖
kararı ve gerekçesi ver, sahne bazlı **iddia-kaynak matrisini** çıkar, kaynaksız kalan iddiaları
ve dengeli kaynakça eksiklerini göster. Karar kullanıcıdadır. Her PubMed kaynaklı yanıtta
"PubMed'e göre" de ve DOI bağlantısını ver. Künye doğrulamasının ayrıntısı: `references/kaynak-dogrulama.md`.
Kullanıcı henüz makale vermediyse biçimi söyle (PMID/DOI listesi en iyisi; PDF veya başlık da olur) ve
sahne listesini taslak olarak göster ki uygunluk sahneye göre ölçülebilsin.

### 5. Sanat yönü ve anlatı (önce onay, sonra üretim)
`references/anlati-ve-sahneler.md` ve `references/gorsel-yon-ve-teknik.md` dosyalarını oku;
`/mnt/skills/public/frontend-design/SKILL.md`'yi de oku. Tez cümlesini ve 13-15 sahneyi kurgula.
**Ders:** ilk taslak kullanıcıya brif onaylatılmadan üretildi ve anlatı reddedildi. Üretime geçmeden önce
**mutlaka kısa bir brif** göster ve açık onay al: tez, sahne listesi (süre ile),
her sahnenin "sıradan PPT'den farkı", veri katmanı kararı. Onay/düzeltme al, sonra üret.

### 6. Sunumu üret
`assets/deck_iskelet.html`'i `sunum.html` olarak kopyala; motoru (script + çekirdek CSS)
değiştirme, yalnızca sahneleri yaz. **Çalışan örnek (kullanıcının onayladığı anlatı):**
`assets/ornek_sunum_kur.py` (18 sahne + 2 yedek; sayıları demo JSON'larından, `literatur_sayilar.json`'dan
ve `git log`'dan okur; hat, hayalet oosit, funnel düğmesi, yerel etiket sürgüsü; `analiz/tum_sayilar.json`
yazar, `sayi_denetle.py` ona karşı çalışır). Eski istatistik odaklı örnek: `assets/ornek_sunum_kur_istatistik.py`.
Yeni sunumda onu kopyala, yollarını ve sahne metinlerini uyarla; sıfırdan yazma. Her sahnede: eylem başlığı, tek fikir, ≤ 40 sözcük, künye
satırı (veri kaynağı, n, birim, yöntem), `data-sure`, `data-baslik`, konuşma dilinde sunucu notu.
Sentetik veri şekilli her slayta `SENTETİK VERİ` etiketi koy. Slayt şekilleri `analiz/sonuc_slayt/`
altındaki SVG'ler. Programın ekran görüntüsü gerekiyorsa yalnızca **test veritabanından,
kimliksiz** görüntü kullan (`proje-patient-data-center.md`, "Ekran görüntüsü kuralı").

### 7. Denetle, derle, dışa aktar
```bash
python3 scripts/sayi_denetle.py sunum.html analiz/sonuc_slayt/sonuclar.json
python3 scripts/sunum_derle.py sunum.html cikti/sunum_salon.html
python3 scripts/disa_aktar.py cikti/sunum_salon.html --cikti-dir cikti --ad sunum
```
Her `cikti/png/NN.png` dosyasını `view` ile **gözle kontrol et**: taşma, kesik metin, okunmayan
şekil, Türkçe karakter, etiket, kimlik bilgisi. Sorun varsa düzelt ve yeniden derle. Taşma
uyarısı veya `sayi_denetle` listesini boş geçme: her satırı ya düzelt ya gerekçelendir.

### 8. Teslim et
Dosyaları `/mnt/user-data/outputs/` altına koy ve `present_files` ile sun: `sunum_salon.html`
(ana), `sunum.pdf`, `sunum_yedek.pptx`, `sunucu_notlari.md`, `soru_cevap.md`, `analiz/` betikleri.
Sunum çevrimdışı bir kongre dosyası olduğundan varsayılan olarak yayınlanan artifact **değil**,
dosyadır. Kullanıcıya kısa özet ver: ne üretildi, hangi tuşlar (`P` sunucu görünümü, `T` süre,
`G` genel bakış, `F` tam ekran), PPTX yedeğinin düzenlenemez olduğu, salon kontrol listesi,
henüz kullanıcıya ait kalan kararlar (etik onay durumu, çıkar çatışması beyanı, atıf kontrolü).

## Sert sınırlar (gerekçesiyle)

- **Gerçek hasta verisi/kimlik/ekran görüntüsü sunuma girmez** etik onay ve veri sorumlusu izni
  doğrulanmadan; isim, dosya no, tarih, kurum amblemi asla. Sebep: özel nitelikli kişisel veri
  (KVKK) ve geri döndürülemez sızıntı riski. Kullanıcı isterse "inandırıcı olsun" diye bile
  isim gösterme; sentetik ya da kimliksiz test verisi öner.
- **Programa olmayan yetenek atfetme.** "Yapay zekâ modeli entegre", "klinik karar destek",
  "doğruluğu X" gibi iddialar yalnızca kullanıcı belge/ölçüm sunarsa ve onaylarsa kullanılır.
- **Sentetik sonuç klinik bulgu olarak sunulmaz;** her şekil ve sahne etiketli.
- **Doğrulanmamış atıf yok.** Hafızadan künye yazılmaz; doğrulanamayan açıkça işaretlenir. Okunmamış makale için "uygun" kararı verilmez; yalnız özet okunduysa karar geçici etiketlenir. Slayta makaleden gelen her sayı kaynağında görülüp aynen aktarılır.
- **Sayı elle yazılmaz;** her istatistik `sonuclar.json`'dan gelir.
- **Reddederken ton:** bir şeyi yapmayacaksan madde işareti kullanma; sıcak, akıcı bir dille nedenini söyle ve hemen güvenli bir alternatif öner. Kullanıcı kötü niyetli değil, sunumunu güçlü yapmak istiyor.
- **Hukuki/etik kesinlik iddiası yok.** KVKK, etik kurul, mevzuat konularında çerçeve çiz ve
  kullanıcıyı kurumunun etik kurulu/hukuk birimine yönlendir.

## Referans dosyaları (ne zaman okunur)

| Dosya | Ne zaman |
|---|---|
| `references/proje-patient-data-center.md` | Aşama 2, 5, 6: programın doğrulanmış özeti, anlatı parçaları, hijyen |
| `references/istatistik-ve-model-rehberi.md` | Aşama 3, 5: yöntem seçimi, sızıntı, kalibrasyon, raporlama kılavuzları, hakem soruları |
| `references/etik-ve-veri.md` | Aşama 1, 6: veri katmanları, KVKK/etik kontrol listesi, YZ kullanım beyanı |
| `references/makale-uygunluk.md` | Aşama 4: makale uygunluk değerlendirmesi, iddia-kaynak matrisi, telif/alıntı |
| `references/kaynak-dogrulama.md` | Aşama 4: künye doğrulama ve uyarı metni |
| `references/anlati-ve-sahneler.md` | Aşama 5: tez adayları, süre bütçesi, 15 sahne planı, soru-cevap |
| `references/gorsel-yon-ve-teknik.md` | Aşama 5-8: sanat yönü, klişe testi, Türkçe tipografi, üretim hattı, salon riskleri |

## Betikler (`scripts/`) ve varlıklar (`assets/`)

`sentetik_veri.py` (hasta→siklus→embriyo kohortu, gerçek parametreler kodda) · `kpi_demo.py` (KPI erken uyarı + funnel) · `gorsel_demo.py` (sentetik görüntü, omurga + yerel son katman, kalite kontrol izlemi) ·
`analiz_demo.py` (GEE vs naif, rastgele/gruplu/zamansal doğrulama, kalibrasyon, karar eğrisi; `--slayt`) ·
`sayi_denetle.py` (slayt sayıları kaynakla örtüşüyor mu) · `sunum_derle.py` (font+görsel gömme) ·
`disa_aktar.py` (PDF, yedek PPTX, PNG, taşma uyarısı) · `assets/ornek_sunum_kur.py` (çalışan örnek sunum derleyicisi) · `assets/deck_iskelet.html` (sunum motoru:
adımlar, genel bakış, sunucu penceresi, zamanlayıcı, baskı stili, örnek sahne kalıpları).

## Kalite çıtası (teslimden önce kendine sor)

- Başlıklar bulguyu mu söylüyor, konuyu mu etiketliyor?
- Bir hakem "bu sayı nereden?" derse cevap `sonuclar.json` + kod satırı mı?
- Salondaki embriyolog 7-11. sahnede "bunu kendi verimde nasıl yaparım?" diye düşünüyor mu (kod 2 satır, yöntem net)?
- Sunum "yapay zekâ reklamı" gibi mi, yoksa sınırlarını söyleyen bir bilim sunumu gibi mi okunuyor?
- Hiçbir slaytta kimliklendirici bilgi, doğrulanmamış atıf ya da programda olmayan yetenek yok mu?
