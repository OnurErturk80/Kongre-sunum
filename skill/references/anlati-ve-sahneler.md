# Anlatı kurgusu ve sahne planı (15-20 dk sözlü sunum)

## KULLANICININ SEÇTİĞİ ANLATI (varsayılan, 10 Kasım 2026)

**Tez:** “Ham değil, kişisel yapay zekâ.” Embriyoloji laboratuvarı çalışanları yapay zekâyı iş akışına
kendi ihtiyaçlarına göre katabilir; işi yıllarca yapan kişi, sorunlara önlem olacak araçları yapay zekâ ile
kendisi yapabilir. Kayıt ve güvenlik bunun merkezindedir. Kullanıcının kendi cümleleri: kayıtlar önce
kâğıttaydı, sonra bilgisayarla dijitalleşti, şimdi bu verilerle istatistiklere bakıp KPI’ları takip ediyoruz;
yapay zekâ ile bunu ileri istatistikle daha derin yapabiliriz. Yapay zekâ embriyo analizi ve niPGT-A gibi
alanlarda da araştırılıyor: ne kadar güvenli? Embriyolog işsiz mi kalacak, yoksa yapay zekânın kalite
kontrolcüsü mü olacak? Kişiselleştirme yolları: kendi programını yapmak, KPI’ları ileri istatistikle izlemek,
görsel modelleri yerelde kendi tecrübenle eğitmek.

**KPI’da mesaj:** belirli bir KPI öne çıkmaz; mesaj “KPI takibinde yapay zekâ desteği”dir.
**Görsel bölüm:** yöntem + sentetik görüntülerle küçük canlı demo. **Makaleler:** skill aday tarar, kullanıcı seçer.

| # | Sahne | sn | Demo / kanıt |
|---|---|---|---|
| 1 | Başlık | 20 | |
| 2 | Kâğıt → bilgisayar → kendi programı → yapay zekâ | 45 | adım adım yolculuk |
| 3 | Neden kendi aracım? (sessiz hata, izlenebilirlik, güvenlik) | 50 | |
| 4 | İş akışı: her aşama bir kayıt, her kayıt bir önlem | 55 | dokunulabilir hat, aşama başına doğrulanmış önlem |
| 5 | Kayıt ve güvenlik (rol/modül izni, değişiklik günlüğü, işlemi yapan, benzersiz etiket, yedek, taşıma) | 50 | sürüm numaralı kartlar |
| 6 | Nasıl yaptım? ihtiyaç → YZ kodlar → test → embriyolog doğrular → sürüm notu | 60 | git commit grafiği, CLAUDE.md = SOP |
| 7 | Önlem örneği: hayalet oosit | 60 | düğmeli örnek hesap |
| 8 | KPI dün / bugün / yarın | 45 | |
| 9 | KPI + YZ: erken uyarı (CUSUM vs aylık ortalama) | 80 | `kpi_demo.py`, 500 simülasyon |
| 10 | KPI + YZ: adil karşılaştırma (funnel, yaşa göre ayar) | 65 | ham/ayarlı düğmesi |
| 11 | Labda yapay zekânın dört alanı ve kanıt düzeyi | 60 | aday literatür |
| 12 | Ne kadar güvenli? geriye dönük parlak, randomize kanıtlanmamış | 80 | Illingworth 2024, Salih 2023, Barnes 2023, Bamford 2023 |
| 13 | Embriyolog işsiz mi? Hayır: kalite kontrolcü (4 rol) | 70 | `gorsel_demo.py` kalite kontrol izlemi |
| 14 | Yerel model: hazır model yazı-tura, yerel etiketle iyileşir | 80 | sentetik görüntüler, sürgü |
| 15 | Kişiselleştirmenin üç yolu | 50 | |
| 16 | Sınırlar | 45 | |
| 17 | Üç mesaj | 40 | |
| 18 | Teşekkür | 20 | |

Toplam ≈ 17 dk 45 sn. Uygulaması: `assets/ornek_sunum_kur.py`.

---

## Alternatif (ilk taslak, kullanıcı tarafından reddedildi): istatistik odaklı anlatı

## Önce tez cümlesi

Sunumun omurgası **tek bir iddia**dir. Slaytlar bu iddianın kanıtıdır, konu listesi değildir.
Kullanıcıyla bir tez seç; üç aday (kullanıcı kendi cümlesini de yazabilir):

1. **"Yapay zekâdan önce veri, veriden önce istatistik: embriyolar bağımsız değildir."**
   (istatistik odaklı, hakem dostu; omurga bulgu: hiyerarşi → sızıntı → AUC şişmesi)
2. **"Klinik uzmanın yazılım yazdığı çağda, laboratuvar için asıl beceri doğrulamaktır."**
   (iş akışı odaklı; PDC hikâyesi + hata günlüğü + doğrulama kültürü)
3. **"Bir modeli laboratuvara koymak, bir SOP koymak gibidir: kabul kriteri, denetim izi, insan."**
   (entegrasyon odaklı; özerklik merdiveni + kalibrasyon + zaman kayması)

Önerilen: 1 ile 2'yi birleştir: PDC "veri altyapısı ve yapay zekâ ile geliştirme" hikâyesini
anlatır, istatistik/model bölümü "o veriyle ne yapılabilir ve nasıl yanlış yapılır" kanıtını verir.
Bu bileşim, kullanıcının gerçek programına dayanır ve akademik derinlik taşır.

**Kancayı sahnede kur (ilk 40 sn):** Salona soru sor: "Bir hastanın 6 embriyosu: altı bağımsız
gözlem mi?" El kaldırtma. Cevabı 7. sahnede bulgu olarak geri getir.
(Alternatif kanca: "Bu programdaki 14 bin satırın yazarı Python'a 2026'da başlayan bir embriyolog."
Önce kullanıcıdan doğrulat; CLAUDE.md "Python'a yeni başlamış" diyor, tarihi o söylesin.)

## Süre bütçesi

~16-17 dk anlatı + 2-3 dk tampon. Slayt sayısı değil **sahne sayısı** planla: 13-15 sahne,
sahne başına ortalama 60-90 sn. 20 dakikalık oturumda tampon konuşmacıyı korur. Soru-cevap
ayrıysa yedek (appendix) slaytları HTML'de `data-sure="0"` ile sona koy (yöntem ayrıntıları,
ek şekiller). Sorulduğunda göstermek için hazır olsun.

## Sahne planı (varsayılan; kullanıcıya göre uyarla)

| # | Sahne | sn | Ne gösterir | "Sıradan PPT"ten farkı |
|---|---|---|---|---|
| 1 | Kanca + tez | 40 | Salona soru; tez cümlesi | Canlı el kaldırma, sonuç 7'de açılır |
| 2 | Problem: veri nerede yaşıyor? | 60 | Dağınık Excel/Access → tek kayıt; veri doğası (hiyerarşik, seçilmiş, sansürlü) | Üç sorunu üç kart olarak sırayla (adım) |
| 3 | Patient Data Center: iş akışı haritası | 90 | OPU→denüdasyon→ICSI→fert→D2/3→blasto→vitrifikasyon→çözme→transfer→FET hattı; her aşamanın ürettiği değişkenler | **Tıklanabilir hat**: aşamaya tıkla, o aşamada bilinen değişkenler ve "tahmin anı" belirir |
| 4 | Yapay zekâ ile geliştirme: CLAUDE.md = SOP | 90 | CLAUDE.md'den birkaç satır + README sürüm zaman çizgisi (sürüm no vs tarih) | Gerçek depo parçaları, ekran değil canlı zaman çizgisi |
| 5 | Güvence: yakalanan hata | 60 | Tek hata hikâyesi (ör. v6.15 rol açığı): nasıl bulundu, nasıl kapandı, ne öğretti | Dürüstlük anı; reklam tonunu kırar |
| 6 | Veri göçü doğrulaması | 60 | Access → SQLite: deneme kopyası, birebir sayı, uyarı listesi | "Doğrulanmamış veri modellenmez" |
| 7 | İstatistik: hiyerarşi | 90 | Kancanın cevabı. Tasarım etkisi slider'ı + naif vs GEE şekli | **Slider canlı**; salon ρ ve m'yi oynatır |
| 8 | Model eğitme: sızıntı | 90 | 2 satırlık kod farkı + AUC (rastgele / hasta-gruplu / zamansal) | Geçiş düğmesi: aynı model iki doğrulama; kod 2 satır vurgulu |
| 9 | Basit model yeter mi? | 60 | Lojistik vs gradyan artırma, gruplu doğrulamada | "Karmaşık ≠ iyi" |
| 10 | Kalibrasyon ve zaman kayması | 90 | Zamansal test kalibrasyon eğrisi; 2023 sonrası sistematik sapma | Eğri üzerinde "kültür sistemi değişti" işareti (sentetik gerçek parametre) |
| 11 | Fayda: karar eğrisi | 60 | Net fayda; "hangi eşikte hangi eylem" | Eşik slider'ı (isteğe bağlı) |
| 12 | Entegrasyon çerçevesi: özerklik merdiveni | 90 | Kayıt → betimsel → uyarı → öneri → otomasyon; her basamak için denetim ve insan | Merdiven etkileşimli; PDC şu an hangi basamakta |
| 13 | Sınırlar ve etik | 60 | Hallüsinasyon, KVKK, etik kurul, mevzuat, YZ kullanım beyanı | Tek sakin slayt, az metin |
| 14 | Yol haritası + 3 mesaj | 60 | Retrospektif doğrulama → prospektif; 3 take-home | Her mesaj tek cümle |
| 15 | Tekrarlanabilirlik + teşekkür | 30 | Kod/sentetik veri deposu, QR, kaynakça kısa | "Bu sunumdaki her sayı bu betikten" |

Toplam ≈ 980 sn ≈ 16 dk 20 sn. Sahne 1-6 PDC/yapay zekâ hikâyesi, 7-11 istatistik/model, 12-15 entegrasyon ve sonuç.

## Sahne yazım kuralları

- **Eylem başlığı:** başlık bulguyu söyler ("Rastgele bölme AUC'yi şişiriyor"), konuyu etiketlemez ("Doğrulama").
- Her sonuç sahnesinde görünür **künye**: veri kaynağı (SENTETİK / gerçek), n (hasta, siklus,
  embriyo), birim, yöntem, belirsizlik (GA). Slayt altı küçük satır.
- Sayılar `sonuclar.json`'dan gelir; slaytlara elle sayı yazma. `scripts/sayi_denetle.py` ile doğrula.
- Bir sahne = bir fikir. 40 sözcükten fazla metin varsa sahneyi ikiye böl veya şekle devret.
- Sunucu notu **konuşma dilinde**, tam cümleler, geçiş cümlesi dahil, süre ile: 90 sn ≈ 200-220 sözcük.
  Türkçe sunum notlarında kısaltmaları ilk geçtiği yerde aç.
- Yedek slaytlar: yöntem ayrıntısı, hakem sorusu cevapları ("küme sayısı yeterli mi?",
  "neden GEE, GLMM değil?", "eksik veri?", "dış doğrulama?"). Soru-cevap için hazırlıktır.

## Başlık ve özet bildiri

Başlık: iddia + bağlam, 12 sözcüğü geçmesin. Üç öneri üret, kullanıcı seçsin. Örnek biçim:
"Embriyolar bağımsız değildir: laboratuvar verisinde yapay zekâ ve ileri istatistik için güvenli yol."
İstenirse yapılandırılmış özet (Amaç / Yöntem / Bulgular / Sonuç, ~250-300 sözcük); sentetik
veriyle yapılan demo "Bulgular"da **yöntem doğrulaması** olarak etiketlenir, klinik bulgu olarak değil.

## Soru-cevap hazırlığı (kullanıcıya ayrı bir sayfa olarak ver)

En olası 10 hakem/dinleyici sorusu ve kısa cevaplar: "Gerçek veride denediniz mi?",
"Program klinik karar veriyor mu?", "Yapay zekânın yazdığı koda nasıl güveniyorsunuz?",
"Etik kurul?", "Başka merkezde çalışır mı?", "Neden GEE?", "Eksik veri?", "Hasta verisi güvenli mi?",
"Maliyet/süre?", "Ticari çıkar var mı?" Cevaplar yalnızca doğrulanmış olgulara dayanır;
bilmediğin yerde "bunu ölçmedik" demek doğru cevaptır.
