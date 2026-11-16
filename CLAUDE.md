# Kongre sunumu: Yapay zekânın iş akışına entegrasyonu ve ileri istatistik

Bu dosyayı her oturumun başında oku. Proje, Claude Cowork'te (bulut) 10–15 Kasım 2026 arasında hazırlandı ve
Claude Code'a taşındı. Kararların gerekçeleri aşağıda; bir kararı değiştirmeden önce kullanıcıya sor.

## Kullanıcı

**Onur Kadir Ertürk**, Akdeniz Üniversitesi Hastanesi, 22 yıllık klinik embriyolog. Klinik doğrulukta uzman,
Python'a yeni. Dil Türkçe; klinik terimler İngilizce (blastocyst, ICSI, PN, ICM, TE, FET, PGT-A).
Teknik kararları kısaca gerekçelendir, klinik kararları ona sor.

## Sunum (son onaylı hali: v4)

- Başlık: "Yapay zekânın iş akışına entegrasyonu ve ileri istatistik", alt başlık "IVF laboratuvarında beş soru".
- Süre 15 dk (planlanan 14 dk 30 sn). 17 ana sahne + 7 yedek (yedekler `data-sure="0"`, PowerPoint'te gizli).
- Omurga kullanıcının beş sorusu (bu sıra ve sözler kullanıcının; değiştirme):
  1. Yapay zekâ labda hangi aşamalarda kullanılmaya başlandı? (2 sahne)
  2. Ne kadar yaygınlaştı? Nerede, ne kadar kullanılıyor? (2 sahne)
  3. Bu kadar kullanılması sonuçları nasıl etkiliyor / neye etki ediyor? (3 sahne)
  4. Yapay zekâ ne kadar doğru sonuç veriyor? (3 sahne)
  5. Benim fikrim: küçük uygulamam (Patient Data Center), KPI takibi, ileri istatistik (5 sahne)
- Görsel dil (kullanıcı "tarzı hoşuma gitti" dedi): kemik zemin #F6F3EC, mürekkep #111A27, fosforlu sarı #FFD43B,
  kırmızı uyarı #C7361F; solda koyu 1–5 soru omurgası; soru Lora italik, cevap Inter Display ağır.
- Tam sahne listesi: `sunum_v4/KARARLAR.md` (a) ve `sunum_v4/sahne_listesi.json`.
- Slayt başlıkları (genel bakış/sunucu panelindeki `data-baslik`, ör. "1 · Aşama Hattı") Title Case
  (16 Kasım 2026, kullanıcı isteği). Sahnelerin görünür h2 bulgu cümleleri buna dahil değil; onlar
  halen cümle biçiminde ("başlık bulguyu söyler, konuyu etiketlemez" kuralı geçerli).
- Sahne "1 · Aşama Hattı"ndaki durak kartları artık → / ← tuşlarıyla da mouse tıklamasıyla aynı
  sırada tek tek seçiliyor (16 Kasım 2026). `v4.js`'teki gizli `data-adim` işaretçileri `statik`
  modda (disa_aktar.py dışa aktarımı) devre dışı kalır; aksi halde PDF/PPTX'te yanlış durak
  (son durak) görünür kalırdı — bkz. `v4.js` içindeki `if(!statik)` bloğu.
- **5.5 "Benim fikrim" tezi değişti (16 Kasım 2026, kullanıcı kararı).** Eski tez ("ham değil,
  kişisel yapay zekâ; embriyolog kalite kontrolcüsü") kullanıcı tarafından reddedildi. Yeni tez:
  **"geliştirici embriyolog"** — "Yapay zekâ bana embriyo seçmeyi değil, yazılım yazmayı öğretti."
  Kapanış artık öğüt değil davet/soru: "siz de kendi ihtiyacınızı yazılığa çevirebilir misiniz?"
  Kapanış slaytındaki 5. kısa cevap da buna göre güncellendi. Bu tezi tekrar değiştirmeden önce
  kullanıcıya sor.

## Değişmeyen kurallar (gerekçeli)

1. **Gerçek hasta verisi yok.** Bütün demolar sentetik ve slaytta "SENTETİK VERİ/GÖRÜNTÜ" etiketli (KVKK, etik onay yok).
2. **Merkez adı yok** (kullanıcı kararı, Türkiye dahil). Yaygınlık sahnesinde yalnız ülke ve firmanın açıkladığı toplam sayı,
   "FİRMA / KLİNİK BEYANI · hakemli değil" etiketiyle. Ürün adları bilimsel bağlamda serbest.
3. **Uydurma sayı/atıf yok.** Slayttaki her sayı bir JSON'dan gelir (`sunum_v4/analiz/tum_sayilar.json` birleşik kaynak).
   Derlemede `sayi_denetle.py` temiz geçmeli (şu an 102 sayı, hepsi kaynaklı). Yeni makale/sayı → önce PubMed'de doğrula,
   okuma derinliğini (tam metin / yalnız özet) yaz, sonra ilgili `bolumler/0N_sayilar.json`'a ekle.
4. **Patient Data Center'a olmayan yetenek atfetme.** İçinde makine öğrenmesi modeli yok; kayıt ve betimsel istatistik aracı.
   Zaman tasarrufu ölçülmedi; slaytta süre iddiası yok. CUSUM/funnel programda yok ("programın tuttuğu türden veriyle yapılabilir").
5. **Blastokist oranı** programda "blastokist ekranında değerlendirilen her embriyo / 2PN" (morula, kavitasyon, arrest dahil);
   Vienna'nın 5. gün tanımıyla birebir değil. Slaytta "tanım birebir değil*" + dipnot. Kullanıcı: 6–7. güne hiç gitmiyorlar.
6. **Funnel'daki A–F "sentetik birimler"** (kullanıcı kararı; "embriyolog" deme).
7. **Önce HTML, sonra PowerPoint.** İçerik değişikliği her zaman `sunum_v4/kur_sunum_v4.py`'de yapılır; PowerPoint ondan üretilir.
   İki dosyayı elle ayrı ayrı düzenleme, birbirinden ayrılırlar.
8. **Son hali kesinleştirmeden kullanıcıya sor** (kullanıcının isteği).

## Açık işler (kullanıcıdan bekleniyor)

- Kongrenin doğru adı (şu an "Klinik Embriyoloji Kongresi 2027", kapakta).
- Çıkar çatışması beyanı (yöntem yedeğinde "[beyan]").
- Kullanıcının söylediği "bazı değişiklikler" — henüz gelmedi.
- İsteğe bağlı: programdan önce KPI'ların nasıl sayıldığı, programın kazandırdığı süre (slayta ancak kullanıcı verirse girer).
- PowerPoint animasyonları PowerPoint'te denenmedi (bulutta yalnız LibreOffice vardı). Kullanıcının denemesi bekleniyor:
  onarma uyarısı, 2/4/10/15. slaytlarda tıklama sırası, Inter yazı tipi yoksa başlık kayması.
- Tam liste: `sunum_v4/KARARLAR.md` (b).

## Klasörler

```
CLAUDE.md                 bu dosya
BASLARKEN.md              kullanıcı için kurulum adımları
teslim/                   son teslim edilen dosyalar (15 Kasım 2026): sunum_salon.html (ana), sunum.pdf,
                          sunum_yedek.pptx (görüntü tabanlı), sunum_animasyonlu.pptx (düzenlenebilir), sunucu_notlari.md
sunum_v4/                 SUNUMUN KAYNAĞI
  kur_sunum_v4.py         bütün sahneler, metinler, sunucu notları burada (değişiklik buraya)
  v4.css, v4.js           görsel dil ve etkileşimler (aşama hattı, ülke süzgeci, kronometre, "aynı model" düğmeleri, funnel)
  derle.sh                kur -> sayı denetimi -> salon HTML (fontlar gömülü) -> PDF/PPTX/PNG -> temas sayfaları
  ORTAK_BAGLAM.md         beş araştırma ajanına verilen bağlam ve önceki bulgular
  bolumler/0N_*.md        beş bölümün araştırması (kaynaklar, PMID/DOI, okuma derinliği, doğrulanamayanlar)
  bolumler/0N_sayilar.json  slayta giren literatür sayıları
  KARARLAR.md             sahne listesi, açık kararlar, çıkarılan/doğrulanamayan içerik
pptx/                     HTML -> düzenlenebilir, animasyonlu PowerPoint dönüştürücüsü
  yakala.py + topla.js    Playwright ile her slaytın kutularını, metinlerini, resim bölgelerini ve tıklama durumlarını toplar
  kur.py                  yakalanandan .pptx kurar (data-adim -> tıklamayla belirme; düğme durumları -> çıkış/giriş)
  karsilastir.py          HTML ve PPTX görüntülerini yan yana koyar (görsel kontrol)
analiz_demolari/          sentetik demoların sonuçları (KPI/CUSUM/funnel, görsel model, sızıntı) ve şekiller
skill/                    "embriyoloji-ai-kongre-sunumu" skill'i (iş akışı, kurallar, betikler, sunum motoru)
fontlar/                  gömülen yazı tipleri (OFL)
```

Patient Data Center deposu pakette yok: https://github.com/OnurErturk80/Patient-Data-Center . `kur_sunum_v4.py`
git kaydından commit sayısını ve günleri sayıyor; yolu `PDC_REPO` ortam değişkeniyle ver
(varsayılan: bu klasörün yanında `Patient-Data-Center/`). Depo son halinde: 341 commit, 8 Eylül–9 Ekim 2026, v6.266.
Yeni commit eklenirse slayttaki sayılar değişir — bu bilerek böyle; kullanıcıya söyle.

## Nasıl derlenir

```bash
pip install python-pptx fonttools playwright lxml pillow
python -m playwright install chromium
# HTML + PDF + görüntü yedek PPTX
cd sunum_v4 && PDC_REPO=/yol/Patient-Data-Center ./derle.sh          # Windows'ta: bash ile ya da adımları tek tek çalıştır
# Düzenlenebilir animasyonlu PowerPoint (HTML derlendikten sonra)
cd ../pptx && python yakala.py && python kur.py                        # -> pptx/sunum_animasyonlu.pptx
# Görsel kontrol (LibreOffice gerekir): python kur.py --onizleme ; soffice ile PDF'e çevir ; python karsilastir.py 1 2 3 ...
```

Teslimden önce her zaman: `sayi_denetle` temiz mi, `cikti/png/` ve temas sayfaları gözle kontrol (taşma, kesik metin,
etiketler, künye satırı), etkileşimler `etkilesim_sina.py` ile.

## Dönüştürücü notları (pptx/)

- Lora → PowerPoint'te Georgia (boy ×0.9, Georgia daha geniş); Inter ve Inter Display aynı adla (kullanıcının
  bilgisayarında yoksa "yazı tiplerini katıştır" ile kaydetmesi önerildi).
- SVG/IMG bölgeleri yalıtılarak (diğer her şey gizli, saydam zemin) 2x PNG çekilir; içlerindeki yazı düzenlenemez.
- Satır içi arka planlar PowerPoint metin vurgusu (a:highlight) olur; kenarlıklı satır içi rozetler kutu olarak çizilir;
  satır içi blok/ikonlar metinde bölünmez boşlukla yer tutar.
- Durum değişimi = önceki durumla anahtar farkı (konum+metin+renk); farklı öğeler çıkış/giriş efektiyle değişir.
  Yeni bir düğmeli slayt eklersen `yakala.py` içindeki `DURUMLAR`'a tıklama sırasını ekle.

## Araçlar

Bulutta PubMed araçları (MCP) vardı; web araması kurumda kapalıydı. Claude Code'da literatür doğrulaması için PubMed MCP
bağlı değilse kullanıcıya söyle; künyeyi hafızadan yazma. Skill'in bir kopyası `.claude/skills/embriyoloji-ai-kongre-sunumu/` altında; Claude Code bu klasör açıldığında
onu proje skill'i olarak bulur (betikler `skill/` altındakiyle aynı) (skill içindeki örnek betiklerin yolları eski bulut yollarıdır; asıl
kaynak `sunum_v4/`).
