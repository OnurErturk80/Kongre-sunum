# Patient Data Center — sunum için proje özeti

Kaynak: https://github.com/OnurErturk80/Patient-Data-Center (herkese açık depo).
Bu özet 9 Kasım 2026'daki depo durumundan çıkarıldı. **Sunumdan önce depoyu yeniden
çek (`git clone --depth 1`) ve sayıları güncelle**: sürüm numaraları ve sayılar
sürekli artıyor. Sunuma yazılan her sayı depodan veya `sonuclar.json`'dan gelmeli,
bu dosyadaki rakamlardan değil.

## Ne olduğu (doğrulanmış)

- IVF laboratuvarı için hasta / cycle / oosit kayıt sistemi. Kliniğin mini PC'sinde yerel
  sunucu olarak çalışır; personel iç ağdan telefonla girer. İnternete bağlı bulut hizmeti değil.
- Mikroskop kamerası bir klasöre snapshot atar; program kareleri oositlere bağlar ve arşivler.
- İş akışı kapsamı: OPU, denüdasyon, ICSI, fertilizasyon kontrolü, gün 2/3, blastokist
  değerlendirme, vitrifikasyon + Cryo haritası, çözme (thaw), transfer, FET, gebelik sonucu,
  PGT, androloji (sperm) modülü, resmî form çıktıları (revizyon numaralı).
- Altyapı: Python, SQLite (`lab.db`), ağırlıklı olarak tek `app.py` (~14 bin satır) + yardımcı
  modüller, HTML şablonları, 60'tan fazla numaralı veri göçü betiği (`goc_*.py`), otomatik
  yedekleme, iki makine arasında güvenli taşıma (`tasi.py`), rol/modül bazlı erişim,
  eş zamanlı çok personelli kullanım.
- Eski Access kayıtları (2018 → 2026) `aktar_access.py` / `aktar_toplu.py` ile aktarıldı.
  README'ye göre bir toplu aktarım 5.494 tedavi, 18 uyarı; 2018 aktarımı 918 tedavi, 0 hata
  ve deneme kopyasıyla birebir. (Güncel sayıları depodan oku.)
- İstatistik ekranı **betimsel**: aylık/yıllık oranlar (yıl/ay seçici). İçinde makine
  öğrenmesi modeli, tahmin motoru veya yapay zekâ çağrısı **yok** (README'de "yapay zek",
  "model" geçmiyor; yeniden kontrol et: `grep -ci "yapay zek" README.md`).

## Sunumdaki doğru çerçeve

Yapay zekâ bu projede iki yerde var ve ikisi de gerçek:

1. **Geliştirme aracı olarak.** Programı 22 yıllık bir embriyolog, Claude Code ile yazdı.
   Kod konusunda yeni, klinik doğruluk konusunda uzman. Bu, "klinik uzman + yapay zekâ ile
   yazılım geliştirme" modelinin canlı örneği.
2. **Veri temeli olarak.** Yapılandırılmış, tutarlı, aşamaya bağlı kayıt, istatistik ve
   model eğitiminin ön koşuludur. Program bu yüzden bir "model" değil bir "veri altyapısı"
   olarak sunulmalı.

**Yapılmayacaklar:** Programa yapay zekâ modeli entegre edilmiş gibi sunmak; "klinik karar
destek" demek; bu programın çıktısı için doğruluk/AUC iddiası kurmak. Modeller ayrı bir
araştırma katmanıdır ve bu sunumda sentetik veriyle ya da etik onaylı anonim çıkarımla
gösterilir (bkz. `etik-ve-veri.md`).

## Anlatıya uygun gerçek hikâye parçaları (depodan, doğrulayarak kullan)

- **`CLAUDE.md` = kod için SOP.** 370 KB'lık proje belleği: her oturumda okunan çalışma
  kuralları. Embriyoloji laboratuvarında SOP ne ise, yapay zekâ destekli geliştirmede bu odur.
  Güçlü bir benzetme: "yapay zekâya talimat vermek protokol yazmaktır."
- **README = sürüm günlüğü**, her sürümde "ne değişti ve neden". 260'tan fazla sürüm.
  Denetim izi / izlenebilirlik (traceability) benzetmesi.
- **Hataların dürüstçe belgelenmesi.** Örnekler: v6.15 "tanımsız rol tek tıkla yönetici
  yapıyordu" (güvenlik açığı bulundu ve kapatıldı); v6.19 "denüdasyonda hayalet oosit".
  Sunumda tek bir "yakalanan hata" öyküsü anlatmak, sunumu reklamdan akademik tartışmaya
  çevirir. Kullanmadan önce README'deki ilgili bölümü oku ve olguyu aynen aktar.
- **İnsan-döngüde doğrulama.** CLAUDE.md'ye göre teknik kararlar açıklanarak verilir,
  klinik kararlar kullanıcıya sorulur. Bu, "yapay zekâ nerede karar vermemeli" sorusunun
  somut cevabı.
- **Veri göçü doğrulaması.** Access aktarımı deneme kopyasında önce çalıştırılmış, sonra
  gerçek makinede; sayılar birebir tutmuş. Bu bir "doğrulama protokolü" hikâyesi.
- **İki makine, yedekleme, eş zamanlı kullanım.** Laboratuvar bilgi güvenliğinin pratiği.

## Sunumdan önce yapılacak depo hijyeni kontrolü

Depo herkese açık olduğu için sunum öncesi şunları yap ve kullanıcıya raporla:

```bash
git ls-files | grep -Ei '\.(db|sqlite|csv|xlsx|mdb|accdb|zip|rar|bak|jpg|tif)$'
git grep -nEi 'tc ?kimlik|\b[0-9]{11}\b|telefon|@[a-z0-9.-]+\.[a-z]{2,}' | head
git log --all --diff-filter=D --name-only | grep -Ei '\.(db|csv|xlsx|accdb)$'   # geçmişte silinen veri
```

Beklenen durum (9 Kasım 2026 itibarıyla): `.gitignore` veri dosyalarını dışarıda tutuyor;
izlenen risk taşıyabilecek dosyalar yalnızca iki kurumsal form şablonu (`.xls`) ve amblem.
Ancak `CLAUDE.md`/`README.md` içinde kayıt numaraları (`MAYIS2025#25`, dosya no `2022-0135`)
ve kullanıcı alıntıları geçiyor. Tek başına kimlik belirlemeyebilir; yine de **slayta ekran
görüntüsü koymadan önce** bu metinlerin görünmediğinden emin ol. Git geçmişinde silinmiş veri
varsa onu da bildir; yalnızca dosyayı silmek veriyi geçmişten kaldırmaz.

## Ekran görüntüsü kuralı

Programdan slayta girecek her ekran görüntüsünde: hasta adı, dosya numarası, tarih,
kurum amblemi/adı, personel adı, kayıt numarası yok edilmiş ya da test verisiyle üretilmiş
olmalı. En güvenlisi: `yerel_kur.py` ile boş bir test veritabanı kurup, uydurma kayıtla
ekran görüntüsü almak. Gerçek kayıttan alınan görüntüyü "bulanıklaştırmak" yeterli sayma;
görüntü meta verisi ve çevresindeki bağlam sızdırabilir.

## Ağız dolusu iddialardan kaçınma listesi

- "Yapay zekâ ile geliştirilmiş, bu yüzden hatasızdır" → hayır; hata günlüğü zaten bunun tersini gösterir.
- "Programı X kişi kullanıyor / klinik verimi arttırdı" → ölçülmemiş bir sonuç iddiası; yalnızca ölçtüğün şeyi söyle.
- "Tüm 2018–2026 verisi doğrulandı" → yalnızca README'de belgelenen doğrulamaları söyle.
