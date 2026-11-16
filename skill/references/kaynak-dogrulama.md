# Kaynak doğrulama protokolü

Akademik sunumda uydurma atıf, tüm sunumu çökertir. Yapay zekâ modelleri makul görünen
ama var olmayan künyeler üretebilir. Bu protokol bu riski kapatır.

> Makalelerin sunuma **uygun olup olmadığı** (konu, iddia uyumu, kanıt kalitesi) ayrı bir
> değerlendirmedir: `makale-uygunluk.md`. Bu dosya yalnızca künyenin **var olup olmadığını ve doğru
> olup olmadığını** denetler. Makaleleri kullanıcı seçer; aşağıdaki "aday konu başlıkları" yalnızca
> kullanıcı kaynak aramanı isterse kullanılır.

## Kural

**Hiçbir atıf doğrulanmadan slayta girmez.** Hafızadan gelen her künye "aday"dır.

## Adımlar

1. `tool_search` ile `PubMed` araçlarını yükle (`search_articles`, `lookup_article_by_citation`,
   `get_article_metadata`; ön baskılar için `bioRxiv`; kayıtlı çalışmalar için `Clinical Trials`).
   Araçlar yoksa kullanıcıya söyle ve atıfları **"DOĞRULANMADI"** diye işaretle.
2. Her aday için: başlık + yazar + yıl ile ara → PMID/DOI bul → metaverisini oku → künyeyi
   (yazar, dergi, yıl, cilt, sayfa/makale no) araçtan al. Künyeyi hafızadan yazma.
3. Bir iddiayı bir kaynağa bağlarken, o iddianın kaynakta gerçekten geçtiğinden emin ol
   (özet/tam metin). "Bu makale şunu gösterdi" cümlesi yalnızca okuduğun içerik için kurulur.
4. Doğrulanamayanı sil ya da "doğrulanmadı" etiketiyle kullanıcıya ayrı listele. Asla "muhtemelen" künyeyle bırakma.
5. Son slaytta (kaynakça) her kayıt için DOI veya PMID bulunsun.

## Aday konu başlıkları (arayacağın şeyler; künyeleri ARAMADAN yazma)

- Embriyoloji gösterge/konsensus belgeleri: Istanbul Consensus (2011), Vienna Consensus (2017).
- Blastokist derecelendirme: Gardner ve Schoolcraft sistemi.
- Raporlama: TRIPOD+AI (2024), PROBAST+AI, CONSORT-AI, SPIRIT-AI, DECIDE-AI, STROBE, RECORD.
- Karar eğrisi analizi: Vickers ve Elkin; Vickers ve ark. güncel öğretici.
- Kalibrasyon: Van Calster ve ark. ("Calibration: the Achilles heel of predictive analytics").
- Tahmin modeli örneklem büyüklüğü: Riley ve ark.
- Kümeli veri / GEE: Liang ve Zeger (1986) ve küçük küme düzeltmeleri.
- Embriyo seçiminde yapay zekâ: sistematik derlemeler ve randomize çalışmalar (güncel olanı ara; alan hızlı değişiyor).
- Time-lapse seçimi: Cochrane derlemeleri ve randomize çalışmalar.
- Yapay zekâ destekli kod yazma ve doğrulama: yalnızca yayımlanmış, doğrulanmış çalışmalar.
- ESHRE iyi uygulama / add-on önerileri (güncel sürümü ara).

## Kullanıcıya her seferinde söylenecek uyarı

Atıflara dair şu notu yanıta ekle: "Hafızamdan öneri verdiğim atıfları PubMed aracıyla
doğrulayamadıysam hata içerebilir. Kongre sunumuna girmeden önce her künyeyi kendiniz de
kontrol edin."
