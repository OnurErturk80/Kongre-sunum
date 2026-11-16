#!/usr/bin/env python3
"""
Slayttaki istatistik benzeri sayıların sonuclar.json'da karşılığı var mı?

Amaç: "tek kaynak" kuralını mekanik olarak denetlemek. Slayta elle yazılmış, koddan
gelmeyen bir AUC/GA/oran sunumun en sinsi hatasıdır.

Kullanım:
    python3 sayi_denetle.py sunum.html sonuc_slayt/sonuclar.json

Çıktı: KAYNAKSIZ sayılar listesi (kontrol et: gerçekten koddan mı geliyor, yoksa
bağlam/tasarım sayısı mı?). Hata değil, inceleme listesidir. Bilerek sabit sayılar
(slider varsayılanı, sürüm numarası, yıl) için slayttaki öğeye data-sayi-ok="1" ekle.
"""
import json, re, sys, html as H


def duzlestir(x, out):
    if isinstance(x, dict):
        for v in x.values():
            duzlestir(v, out)
    elif isinstance(x, list):
        for v in x:
            duzlestir(v, out)
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        out.add(float(x))


def varyantlar(v):
    s = set()
    for d in (0, 1, 2, 3, 4):
        s.add(round(v, d)); s.add(round(abs(v), d))
        s.add(round(v * 100, d)); s.add(round(abs(v) * 100, d))   # yüzde gösterimi
    return s


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    metin = open(sys.argv[1], encoding="utf-8").read()
    kaynak = set(); duzlestir(json.load(open(sys.argv[2], encoding="utf-8")), kaynak)
    izinli = set()
    for v in kaynak:
        izinli |= varyantlar(v)
    # HTML yorumlarını önce at (içlerinde <script> gibi sözcükler geçebilir), sonra script/style
    metin = re.sub(r"<!--.*?-->", " ", metin, flags=re.S)
    metin = re.sub(r"<(script|style)\b.*?</\1>", " ", metin, flags=re.S | re.I)
    metin = re.sub(r"<[^>]*data-sayi-ok=\"1\"[^>]*>.*?</[^>]+>", " ", metin, flags=re.S)
    metin = re.sub(r"<aside class=\"not\">.*?</aside>", " ", metin, flags=re.S)  # notlar ayrıca gözden geçirilir
    metin = re.sub(r"data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+", " ", metin)
    duz = H.unescape(re.sub(r"<[^>]+>", " ", metin))
    adaylar = re.findall(r"(?<![\w.])[-−]?\d+[.,]\d+%?|(?<![\w.])\d{1,3}\s?%", duz)
    bulunmayan = []
    for a in adaylar:
        s = a.replace("−", "-").replace(",", ".").replace("%", "").strip()
        try:
            v = float(s)
        except ValueError:
            continue
        if not any(abs(v - k) < 1e-9 for k in izinli):
            bulunmayan.append(a)
    if bulunmayan:
        print("KAYNAKSIZ olabilecek sayılar (incele):")
        for a in sorted(set(bulunmayan)):
            print("  -", a)
        sys.exit(1)
    print(f"Tamam: {len(adaylar)} sayı adayı, hepsinin sonuclar.json'da karşılığı var.")


if __name__ == "__main__":
    main()
