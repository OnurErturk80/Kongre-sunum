#!/usr/bin/env python3
"""
Derlenmiş HTML sunumdan yedek çıktılar üretir:
  * sunum.pdf        -> vektör metin, tüm adımlar açık, 1 slayt = 1 sayfa (16:9)
  * sunum_yedek.pptx -> her slayt tam ekran görüntü + sunucu notları
                        (GÖRSEL YEDEK: metin düzenlenemez. Düzenlenebilir PPTX gerekiyorsa
                        pptx skill'iyle yerel nesnelerden ayrıca üret.)
  * png/NN.png       -> slayt görüntüleri (özet, poster, sosyal medya için)

Neden görüntü tabanlı PPTX yedeği? Kongre bilgisayarı HTML'i açamazsa bile, görsel olarak
BİREBİR aynı sunum, her yerde açılan bir dosyadan gösterilebilsin.

Kullanım:
    python3 disa_aktar.py sunum_salon.html --cikti-dir cikti/
Gereksinim: playwright (chromium), python-pptx
"""
import argparse, os, pathlib
from playwright.sync_api import sync_playwright
from pptx import Presentation
from pptx.util import Inches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--cikti-dir", default="cikti")
    ap.add_argument("--ad", default="sunum")
    a = ap.parse_args()
    out = pathlib.Path(a.cikti_dir); (out / "png").mkdir(parents=True, exist_ok=True)
    url = pathlib.Path(a.html).resolve().as_uri()

    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080})
        pg.goto(url); pg.wait_for_timeout(500)
        n = pg.evaluate("document.querySelectorAll('.slayt').length")
        notlar, basliklar = [], []
        for k in range(n):
            pg.goto(f"{url}?k={k}#s{k+1}"); pg.wait_for_timeout(350)
            pg.add_style_tag(content="#ilerleme{display:none!important}")  # dışa aktarımda gerekmez
            pg.evaluate("document.querySelectorAll('[data-adim]').forEach(e=>e.classList.add('goster'))")
            pg.wait_for_timeout(450)  # geçiş animasyonu bitsin
            tasan = pg.evaluate("""(()=>{const out=[];
              document.querySelectorAll('.slayt.aktif *').forEach(e=>{
                if(e.closest('aside.not')) return;
                const r=e.getBoundingClientRect();
                if(r.width>0 && (r.bottom>1080.5 || r.right>1920.5 || r.left<-0.5 || r.top<-0.5))
                  out.push((e.tagName+'.'+(e.className||'')).slice(0,40)+' sınır dışı');
              });
              return out.slice(0,4);})()""")
            if tasan:
                print(f"  UYARI slayt {k+1}: taşma -> {tasan}")
            notlar.append(pg.evaluate("(()=>{const n=document.querySelector('.slayt.aktif .not');return n?n.textContent.trim():''})()"))
            basliklar.append(pg.evaluate("document.querySelector('.slayt.aktif').dataset.baslik||''"))
            pg.screenshot(path=str(out / "png" / f"{k+1:02d}.png"))
        # PDF (print CSS ile)
        pg.goto(url); pg.wait_for_timeout(500)
        pg.pdf(path=str(out / f"{a.ad}.pdf"), width="1920px", height="1080px",
               print_background=True, prefer_css_page_size=True)
        b.close()

    prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    for k in range(n):
        s = prs.slides.add_slide(prs.slide_layouts[6])
        s.shapes.add_picture(str(out / "png" / f"{k+1:02d}.png"), 0, 0, prs.slide_width, prs.slide_height)
        if notlar[k]:
            s.notes_slide.notes_text_frame.text = notlar[k]
    prs.save(str(out / f"{a.ad}_yedek.pptx"))
    print(f"{n} slayt -> {out}/{a.ad}.pdf, {a.ad}_yedek.pptx, png/")


if __name__ == "__main__":
    main()
