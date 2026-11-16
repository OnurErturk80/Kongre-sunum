#!/usr/bin/env python3
"""HTML sunumdan her slaytın öğelerini ve durumlarını toplar -> yakala/sahneler.json + yakala/img/*.png"""
import json, hashlib, pathlib
from playwright.sync_api import sync_playwright

KOK = pathlib.Path(__file__).parent
HTML = (pathlib.Path(__file__).parent.parent / "sunum_v4/cikti/sunum_salon.html").resolve().as_uri()
OUT = KOK / "yakala"; (OUT / "img").mkdir(parents=True, exist_ok=True)
JS = (KOK / "topla.js").read_text(encoding="utf-8")

# slayt no (1'den) -> durum değiştiren tıklamalar (her biri bir PowerPoint tıklaması)
DURUMLAR = {
    2: [("ICSI", "#duraklar .dr:nth-child(6)"), ("Ploidi", "#duraklar .dr:nth-child(8)"),
        ("Kriyo", "#duraklar .dr:nth-child(11)"), ("Embriyo seçimi", "#duraklar .dr:nth-child(7)"),
        ("Kanıt × olgunluk matrisi", "#gMat")],
    4: [("Süzgeç: embriyo seçimi", '#lej2 button[data-t="E"]'), ("Süzgeç: sperm / ICSI", '#lej2 button[data-t="S"]'),
        ("Süzgeç kapalı", '#lej2 button[data-t="S"]')],
    10: [(f"Durum {i}", f'#d4 button[data-i="{i}"]') for i in range(1, 5)],
    15: [("Yaşa göre ayarlı", "#fuAy")],
}
KAPAT = "*{transition:none!important;animation:none!important}"


def main():
    sahneler = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        pg.goto(HTML); pg.wait_for_timeout(500)
        n = pg.evaluate("document.querySelectorAll('.slayt').length")
        for k in range(1, n + 1):
            pg.goto(f"{HTML}#s{k}"); pg.reload(); pg.wait_for_timeout(350)
            pg.add_style_tag(content=KAPAT)
            pg.evaluate("document.querySelectorAll('.slayt.aktif [data-adim]').forEach(e=>e.classList.add('goster'))")
            pg.wait_for_timeout(150)
            durumlar = []
            adlar = ["varsayılan"] + [a for a, _ in DURUMLAR.get(k, [])]
            for si, ad in enumerate(adlar):
                if si > 0:
                    pg.click(DURUMLAR[k][si - 1][1]); pg.wait_for_timeout(250)
                    pg.evaluate("document.activeElement && document.activeElement.blur && document.activeElement.blur()")
                v = pg.evaluate(JS)
                # resim bölgelerini yalıtarak çek
                for o in v["ogeler"]:
                    if o["tip"] != "resim": continue
                    i = o["sira"]
                    st = pg.add_style_tag(content=(
                        "html,body,#sahne,.slayt{background:transparent!important}"
                        "#sahne *{visibility:hidden!important}"
                        f'#sahne [data-pptx="{i}"], #sahne [data-pptx="{i}"] *{{visibility:visible!important}}'))
                    kutu = pg.evaluate(f'(()=>{{const r=document.querySelector(\'[data-pptx="{i}"]\').getBoundingClientRect();return {{x:r.left,y:r.top,width:r.width,height:r.height}}}})()')
                    veri = pg.screenshot(clip=kutu, omit_background=True)
                    pg.evaluate("(s)=>s.remove()", st)
                    h = hashlib.md5(veri).hexdigest()[:12]
                    yol = OUT / "img" / f"{h}.png"
                    if not yol.exists(): yol.write_bytes(veri)
                    o["dosya"] = str(yol); o["hash"] = h
                durumlar.append({"ad": ad, **v})
            sahneler.append({"no": k, "durumlar": durumlar})
            print(k, durumlar[0]["baslik"], [len(d["ogeler"]) for d in durumlar])
        b.close()
    json.dump(sahneler, open(OUT / "sahneler.json", "w", encoding="utf-8"), ensure_ascii=False)


if __name__ == "__main__":
    main()
