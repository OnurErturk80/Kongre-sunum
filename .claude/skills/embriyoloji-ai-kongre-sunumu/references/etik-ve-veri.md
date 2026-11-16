# Etik, gizlilik ve veri kaynağı kararı

> **Karar (10 Kasım 2026):** Kullanıcı gerçek veri kullanmayacak. Sunumdaki tüm istatistik/model
> gösterimi **Katman 1 (sentetik)** ile yapılır. Aşağıdaki Katman 2-3 ve etik onay bölümleri,
> kullanıcı fikrini değiştirirse veya ekran görüntüsü/veri paylaşımı gündeme gelirse başvuru
> amaçlıdır; kendiliğinden gündeme getirme.

Kullanıcı "hangi veriyi kullanmalıyım" sorusunu skill'e bıraktı. Bu dosya o kararın
çerçevesidir. Hukuki tavsiye vermiyoruz; kullanıcıyı kurumunun etik kurulu ve veri sorumlusuna
yönlendiriyoruz. Ama **kararı açık, gerekçeli ve varsayılanı güvenli** biçimde öneriyoruz.

## Önerilen varsayılan: katmanlı veri stratejisi

| Katman | Veri | Sunumda rolü | Onay ihtiyacı |
|---|---|---|---|
| 1 (omurga) | **Sentetik kohort** (`sentetik_veri.py`) | Yöntemi, tuzakları ve doğrulama mantığını göstermek | Yok; her şekilde "SENTETİK" etiketi |
| 2 (isteğe bağlı) | **Toplu, anonim, küçük hücresiz betimsel sayılar** (ör. yıllık fertilizasyon/blastulasyon oranları) | Programın veri altyapısının *çalıştığını* göstermek | Kurum politikasına bağlı; yazılı onay al |
| 3 (yalnız etik onayla) | **Anonimleştirilmiş hasta düzeyi çıkarım** | Gerçek veride yöntemi uygulamak | Etik kurul onayı + veri sorumlusu izni |

Neden sentetik omurga: (a) hasta verisi riski sıfırdır; (b) gerçek etki büyüklükleri
bilindiği için yöntemin doğru çalıştığı *kanıtlanabilir*; (c) kongre salonunda canlı demo
güvenle yapılır; (d) dergi hakemi "yöntem doğrulaması" olarak değerli bulur. Gerçek veri
analizi ayrı bir makale/çalışmadır, 15-20 dakikalık anlatının içine tıkıştırılmamalı.

Sunumda katman 3 yoksa bunu **saklama, öne çıkar**: "Yöntemi bilinen gerçeğin olduğu veride
doğruladık; gerçek veride uygulama etik onay sürecindedir." Bu, zayıflık değil metodolojik
olgunluktur.

## Kontrol listesi (kullanıcıya sor, kayda geç)

1. Gerçek veriden *herhangi* bir sayı/şekil/ekran sunuma girecek mi? Evet ise hangi katman?
2. Kurumun etik kurulu/klinik araştırma kurulu bu kullanımı kapsıyor mu? Retrospektif
   çalışma onayı ve (gerekirse) bilgilendirilmiş onam muafiyeti belgeli mi?
3. Veri sorumlusu (klinik) ve KVKK kapsamında özel nitelikli kişisel veri (sağlık) için
   hukuki dayanak/izin var mı? (6698 sayılı KVKK, sağlık verisi özel nitelikli; kurum
   hukuk müşaviri/KVKK sorumlusuna danış.)
3b. Anonimleştirme gerçekten anonimleştirme mi? İsim/dosya no silmek yeterli olmayabilir:
   nadir kombinasyonlar (yaş + tarih + merkez + nadir endikasyon) yeniden kimliklendirebilir.
   Küçük hücre kuralı: n < 5 olan hücreleri raporlama.
4. Görüntü (embriyo fotoğrafı, ekran görüntüsü) kimlik, tarih, kurum ve personel bilgisi taşıyor mu?
5. Kongre sunum dosyası (PDF/PPTX/HTML) dağıtılacak mı? Yayımlanan dosyada ne kalır
   (gizli notlar, gömülü veri, meta veri, `sonuclar.json`)?
6. Kongrenin kendi politikası: çıkar çatışması beyanı, yapay zekâ kullanım beyanı,
   görüntü/hasta verisi koşulları. (Kongre duyurusunu oku, 2027 kuralları farklı olabilir.)

## Yapay zekâ kullanımı beyanı

Sunumda ve bildiri özetinde şu bilgileri açıkça yaz:
- Programın geliştirilmesinde yapay zekâ kodlama asistanı kullanıldı (hangi araç, hangi dönem).
- Sunumdaki analiz kodu yapay zekâ yardımıyla yazıldı **ve** insan tarafından çalıştırılıp doğrulandı.
- Sunumdaki içeriğin (metin/şekil) üretiminde yapay zekâ kullanıldıysa bunu belirt.
Bu, akademik açıdan hem dürüstlük hem savunma: hakem "bunu kim yazdı?" diye sorar.

## Düzenleyici çerçeve (tek slayt, abartmadan)

- Yazılım klinik karar için kullanılıyorsa tıbbi cihaz yazılımı (MDR/SaMD) ve yüksek riskli
  yapay zekâ (AB Yapay Zekâ Yasası) tartışması başlar. Bu program bugün **kayıt ve betimsel
  istatistik** aracıdır; karar destek iddiası yoktur. Bu sınırı sunumda net çiz.
- Doğru ifade: "Araştırma amaçlı; klinik kararı yönlendirmez." Yanlış: "Klinik karar destek sistemi."
- Güncel mevzuatı kullanmadan önce doğrula; kesin hukuki iddiada bulunma.

## Depo açıksa

Depo herkese açıksa (bu proje öyle): hasta verisi, ekran görüntüsü, yedek, log ve CSV'lerin
git geçmişine hiç girmediğini kontrol et (`proje-patient-data-center.md` içindeki komutlar).
Bir kez commit edilmiş veri silinse de geçmişte kalır; bulursan kullanıcıya açıkça söyle,
geçmiş temizliğini (ör. `git filter-repo`) ve olası ihlal bildirimi yükümlülüğünü kurumuyla görüşmesini öner.
