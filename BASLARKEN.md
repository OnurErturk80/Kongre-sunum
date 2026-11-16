# Claude Code'da devam etmek için

1. Bu zip dosyasını açın, örneğin `Belgeler/kongre-sunumu` klasörüne.
2. Patient Data Center deponuz zaten bilgisayarınızdaysa yerini not edin. Değilse bu klasörün yanına klonlayın:
   `git clone https://github.com/OnurErturk80/Patient-Data-Center`
3. Terminali bu klasörde açıp `claude` yazın.
4. İlk mesaj olarak şunu yazabilirsiniz:
   "CLAUDE.md dosyasını oku. Sunumda şu değişiklikleri yapmak istiyorum: ..."

Claude Code `CLAUDE.md`'yi okuyunca şimdiye kadarki kararları (beş soru, merkez adı yok, sentetik veri, 15 dk,
"önce HTML sonra PowerPoint") bilir.

**Gerekli programlar** (Claude Code isterse kurdurur): Python 3.10+, `pip install python-pptx fonttools playwright lxml pillow`,
`python -m playwright install chromium`. Görsel kontrol için isteğe bağlı: LibreOffice.

**Son dosyalar** `teslim/` klasöründe: `sunum_salon.html` (ana sunum, Chrome/Edge'de açın; F tam ekran, P sunucu
görünümü, T süre, G genel bakış), `sunum.pdf`, `sunum_animasyonlu.pptx` (düzenlenebilir), `sunum_yedek.pptx`
(görüntü tabanlı), `sunucu_notlari.md`.
