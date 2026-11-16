#!/usr/bin/env python3
"""
HTML sunumu "salon-güvenli" tek dosyaya derler:
  * Yazı tiplerini (Türkçe karakterleri kapsayan alt küme) base64 olarak gömer
    -> kongre bilgisayarında font yoksa PowerPoint gibi kayma/yerine-geçme olmaz.
  * Yerel görselleri (png/jpg/svg) data: URI olarak gömer
    -> dosya tek başına taşınır, internet gerekmez.
  * Dış kaynak (http/https) kalmış mı denetler ve uyarır.

Kullanım:
    python3 sunum_derle.py sunum.html sunum_salon.html
    python3 sunum_derle.py sunum.html sunum_salon.html --yazi-dizini /usr/share/fonts/opentype/inter
Not: Gömülen fontların lisansını kontrol et (Inter: SIL OFL, gömmeye izinli).
"""
import pathlib, argparse, base64, mimetypes, os, re, sys, io
from fontTools import subset
from fontTools.ttLib import TTFont

# Basic Latin, Latin-1, Latin Ext-A (ğ Ğ ş Ş İ ı ç ö ü), noktalama, oklar, matematik, Yunan (ρ, β, χ...)
ARALIK = ("U+0020-007E,U+00A0-017F,U+02C6,U+02DC,U+0370-03FF,U+2010-2027,U+202F-203A,"
          "U+20AC,U+2122,U+2190-21FF,U+2200-22FF,U+25A0-25FF,U+2713")

VARSAYILAN_FONTLAR = [
    # (aile adı, ağırlık, dosya adı)
    ("Inter", 400, "Inter-Regular.otf"),
    ("Inter", 600, "Inter-SemiBold.otf"),
    ("Inter", 700, "Inter-Bold.otf"),
    ("Inter Display", 700, "InterDisplay-Bold.otf"),
]


def unicode_listesi(aralik):
    out = []
    for p in aralik.split(","):
        p = p.replace("U+", "")
        a, _, b = p.partition("-")
        out += list(range(int(a, 16), int(b or a, 16) + 1))
    return out


def alt_kume_b64(yol):
    opts = subset.Options()
    opts.flavor = "woff"                  # woff2 için brotli gerekir; woff her yerde çalışır
    opts.layout_features = ["kern", "liga", "calt", "tnum", "case"]
    opts.name_IDs = ["*"]
    f = TTFont(yol)
    s = subset.Subsetter(opts)
    s.populate(unicodes=unicode_listesi(ARALIK))
    s.subset(f)
    buf = io.BytesIO()
    f.flavor = "woff"
    f.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def font_css(dizin):
    css, toplam = [], 0
    for aile, agirlik, dosya in VARSAYILAN_FONTLAR:
        yol = os.path.join(dizin, dosya)
        if not os.path.exists(yol):
            print(f"  ! font yok, atlandı: {yol}", file=sys.stderr)
            continue
        b64 = alt_kume_b64(yol)
        toplam += len(b64)
        css.append(f'@font-face{{font-family:"{aile}";font-weight:{agirlik};font-style:normal;'
                   f'font-display:block;src:url(data:font/woff;base64,{b64}) format("woff");}}')
    # Kod yazı tipi
    mono = str(pathlib.Path(__file__).resolve().parents[2] / "fontlar/DejaVuSansMono.ttf")
    if os.path.exists(mono):
        b64 = alt_kume_b64(mono)
        toplam += len(b64)
        css.append('@font-face{font-family:"JetBrains Mono";font-weight:500;font-style:normal;'
                   f'font-display:block;src:url(data:font/woff;base64,{b64}) format("woff");}}')
    print(f"  fontlar gömüldü: ~{toplam//1024} KB")
    return "\n".join(css)


def gorselleri_gom(html, taban):
    def degistir(m):
        yol = m.group(2)
        if re.match(r"^(data:|https?:|#)", yol):
            return m.group(0)
        tam = os.path.normpath(os.path.join(taban, yol))
        if not os.path.exists(tam):
            print(f"  ! görsel bulunamadı: {yol}", file=sys.stderr)
            return m.group(0)
        mime = mimetypes.guess_type(tam)[0] or "application/octet-stream"
        veri = base64.b64encode(open(tam, "rb").read()).decode()
        return f'{m.group(1)}"data:{mime};base64,{veri}"'
    return re.sub(r'(<img[^>]*?\ssrc=)"([^"]+)"', degistir, html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("giris"); ap.add_argument("cikti")
    ap.add_argument("--yazi-dizini", default=str(pathlib.Path(__file__).resolve().parents[2] / "fontlar"))
    a = ap.parse_args()
    html = open(a.giris, encoding="utf-8").read()
    if "/*FONT_CSS*/" in html:
        html = html.replace("/*FONT_CSS*/", font_css(a.yazi_dizini))
    else:
        print("  ! /*FONT_CSS*/ işareti yok; font gömülmedi", file=sys.stderr)
    html = gorselleri_gom(html, os.path.dirname(os.path.abspath(a.giris)))
    dis = re.findall(r'(?:src|href)="(https?://[^"]+)"', html)
    if dis:
        print("  UYARI: dış kaynak kaldı (salonda internet yoksa çalışmaz):", *dis, sep="\n   - ")
    open(a.cikti, "w", encoding="utf-8").write(html)
    print(f"  yazıldı: {a.cikti} ({os.path.getsize(a.cikti)/1024/1024:.2f} MB)")


if __name__ == "__main__":
    main()
