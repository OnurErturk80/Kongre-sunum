#!/usr/bin/env python3
"""yakala/sahneler.json -> düzenlenebilir, animasyonlu PowerPoint.
python3 kur.py            -> sunum_animasyonlu.pptx
python3 kur.py --onizleme -> onizleme.pptx (yalnız varsayılan durum, animasyonsuz; görsel kontrol için)
"""
import json, sys, collections, pathlib
from lxml import etree
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_LINE
from pptx.oxml.ns import qn

KOK = pathlib.Path(__file__).parent
S = json.load(open(KOK / "yakala/sahneler.json", encoding="utf-8"))
ONIZLEME = "--onizleme" in sys.argv
PX = 6350
def px(v): return Emu(int(round(v * PX)))
def pt(v): return Pt(v * 0.5)
FONT = {"Lora": "Georgia", "Georgia": "Georgia", "Inter Display": "Inter Display", "Inter": "Inter",
        "JetBrains Mono": "Consolas", "DejaVu Sans Mono": "Consolas"}
# satır yüksekliği: Chrome'un metin kutusu (yazı tipi içerik alanı) ~1.21 em
ICERIK = 1.21

prs = Presentation()
prs.slide_width, prs.slide_height = px(1920), px(1080)
BOS = prs.slide_layouts[6]


def rgb(h): return RGBColor.from_string(h.upper())


def kutu_ciz(sl, o):
    r = o["r"]; yan = o.get("yan") or []
    ws = [y["w"] for y in yan] if yan else [0, 0, 0, 0]
    renkler = [y["c"] for y in yan] if yan else [None] * 4
    esit = len(set(round(w, 1) for w in ws)) == 1 and len(set(renkler)) == 1 and ws[0] > 0 and renkler[0]
    rad = o.get("yuvarlak", 0); m = min(r["w"], r["h"])
    if rad >= m / 2 - 0.5 and m > 0 and abs(r["w"] - r["h"]) < 1.5: tur = MSO_SHAPE.OVAL
    elif rad > 0.5: tur = MSO_SHAPE.ROUNDED_RECTANGLE
    else: tur = MSO_SHAPE.RECTANGLE
    cikan = []
    if o.get("dolgu") or esit:
        s = sl.shapes.add_shape(tur, px(r["x"]), px(r["y"]), px(r["w"]), px(r["h"]))
        if tur == MSO_SHAPE.ROUNDED_RECTANGLE: s.adjustments[0] = min(0.5, rad / m)
        if o.get("dolgu"): s.fill.solid(); s.fill.fore_color.rgb = rgb(o["dolgu"])
        else: s.fill.background()
        if esit:
            s.line.color.rgb = rgb(renkler[0]); s.line.width = pt(ws[0])
            if yan[0]["kesik"]: s.line.dash_style = MSO_LINE.DASH
        else: s.line.fill.background()
        s.shadow.inherit = False
        cikan.append(s)
    if not esit and yan:
        x, y, w, h = r["x"], r["y"], r["w"], r["h"]
        uclar = [(x, y + ws[0] / 2, x + w, y + ws[0] / 2), (x + w - ws[1] / 2, y, x + w - ws[1] / 2, y + h),
                 (x, y + h - ws[2] / 2, x + w, y + h - ws[2] / 2), (x + ws[3] / 2, y, x + ws[3] / 2, y + h)]
        for (x1, y1, x2, y2), yy in zip(uclar, yan):
            if yy["w"] > 0 and yy["c"]:
                c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, px(x1), px(y1), px(x2), px(y2))
                c.line.color.rgb = rgb(yy["c"]); c.line.width = pt(yy["w"])
                st = c._element.find(qn("p:style"))
                if st is not None: c._element.remove(st)
                if yy["kesik"]: c.line.dash_style = MSO_LINE.DASH
                cikan.append(c)
    return cikan


def metin_ciz(sl, o):
    runs = o["runs"]; yaz, kap = o["yaz"], o["kap"]
    boy = max((r["boy"] for r in runs if r.get("t")), default=30)
    lh = o["lh"]; ust = (lh - ICERIK * boy) / 2
    tek = o["satir"] <= 1
    if tek:
        w = yaz["w"] * 1.06 + 12
        if o["hiza"] in ("center", "-webkit-center"): x = yaz["x"] + yaz["w"] / 2 - w / 2
        elif o["hiza"] in ("right", "end"): x = yaz["x"] + yaz["w"] - w
        else: x = yaz["x"]
    else:
        x, w = kap["x"], kap["w"] + 6
    y, h = yaz["y"] - ust, yaz["h"] + 2 * ust
    if o.get("dikey"):
        cx, cy = yaz["x"] + yaz["w"] / 2, yaz["y"] + yaz["h"] / 2
        ww, hh = yaz["h"] * 1.06 + 12, yaz["w"]
        s = sl.shapes.add_textbox(px(cx - ww / 2), px(cy - hh / 2), px(ww), px(hh)); s.rotation = 270
    else:
        s = sl.shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = s.text_frame; tf.word_wrap = not tek and not o.get("dikey"); tf.auto_size = MSO_AUTO_SIZE.NONE
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"): setattr(tf, m, 0)
    tf.vertical_anchor = MSO_ANCHOR.TOP
    p = tf.paragraphs[0]
    p.alignment = {"center": PP_ALIGN.CENTER, "-webkit-center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT,
                   "end": PP_ALIGN.RIGHT, "justify": PP_ALIGN.LEFT}.get(o["hiza"], PP_ALIGN.LEFT)
    p.line_spacing = pt(lh)
    for r in runs:
        if r.get("br"): p.add_line_break(); continue
        if not r["t"]: continue
        run = p.add_run(); run.text = r["t"]
        f = run.font; f.name = FONT.get(r["font"], "Consolas" if r.get("mono") else "Inter")
        f.size = pt(r["boy"] * (0.9 if r["font"] == "Lora" else 1)); f.bold = r["kalin"]; f.italic = r["italik"]; f.color.rgb = rgb(r["renk"])
        rPr = run._r.get_or_add_rPr()
        if r.get("ls"): rPr.set("spc", str(int(round(r["ls"] * 50))))
        if r.get("vurgu"):
            hl = etree.SubElement(rPr, qn("a:highlight")); etree.SubElement(hl, qn("a:srgbClr"), val=str(r["vurgu"]).upper())
    return [s]


def resim_ciz(sl, o):
    r = o["r"]
    return [sl.shapes.add_picture(str(KOK / "yakala/img" / pathlib.Path(o["dosya"]).name), px(r["x"]), px(r["y"]), px(r["w"]), px(r["h"]))]


def ciz(sl, o):
    return {"kutu": kutu_ciz, "metin": metin_ciz, "resim": resim_ciz}[o["tip"]](sl, o)


def anahtar(o):
    yuv = lambda r: tuple(round(r[k] / 2) for k in ("x", "y", "w", "h"))
    if o["tip"] == "kutu": return ("k", yuv(o["r"]), o.get("dolgu"), tuple((y["c"], round(y["w"], 1)) for y in o.get("yan") or []))
    if o["tip"] == "resim": return ("r", yuv(o["r"]), o["hash"])
    return ("m", yuv(o["yaz"]), tuple((r.get("t"), r.get("renk"), r.get("kalin"), r.get("vurgu")) for r in o["runs"]))


# ---------- animasyon XML ----------
def _etki(z, spid, giris, ilk):
    par = etree.Element(qn("p:par"))
    ctn = etree.SubElement(par, qn("p:cTn"), id=str(z()), presetID="10", presetClass="entr" if giris else "exit",
                           presetSubtype="0", fill="hold", grpId="0" if giris else "1",
                           nodeType="clickEffect" if ilk else "withEffect")
    etree.SubElement(etree.SubElement(ctn, qn("p:stCondLst")), qn("p:cond"), delay="0")
    ch = etree.SubElement(ctn, qn("p:childTnLst"))
    def hedef(cb): etree.SubElement(etree.SubElement(cb, qn("p:tgtEl")), qn("p:spTgt"), spid=str(spid))
    def gor(deger, gec):
        s = etree.SubElement(ch, qn("p:set")); cb = etree.SubElement(s, qn("p:cBhvr"))
        c = etree.SubElement(cb, qn("p:cTn"), id=str(z()), dur="1", fill="hold")
        etree.SubElement(etree.SubElement(c, qn("p:stCondLst")), qn("p:cond"), delay=str(gec))
        hedef(cb)
        etree.SubElement(etree.SubElement(cb, qn("p:attrNameLst")), qn("p:attrName")).text = "style.visibility"
        etree.SubElement(etree.SubElement(s, qn("p:to")), qn("p:strVal"), val=deger)
    def sol():
        ae = etree.SubElement(ch, qn("p:animEffect"), transition="in" if giris else "out", filter="fade")
        cb = etree.SubElement(ae, qn("p:cBhvr")); etree.SubElement(cb, qn("p:cTn"), id=str(z()), dur="300"); hedef(cb)
    if giris: gor("visible", 0); sol()
    else: sol(); gor("hidden", 299)
    return par


def animasyon(sl, adimlar):
    adimlar = [a for a in adimlar if a.get("gir") or a.get("cik")]
    if not adimlar: return
    sayac = [2]
    def z(): sayac[0] += 1; return sayac[0]
    timing = etree.Element(qn("p:timing")); tn = etree.SubElement(timing, qn("p:tnLst"))
    kok = etree.SubElement(etree.SubElement(tn, qn("p:par")), qn("p:cTn"), id="1", dur="indefinite", restart="never", nodeType="tmRoot")
    seq = etree.SubElement(etree.SubElement(kok, qn("p:childTnLst")), qn("p:seq"), concurrent="1", nextAc="seek")
    sch = etree.SubElement(etree.SubElement(seq, qn("p:cTn"), id="2", dur="indefinite", nodeType="mainSeq"), qn("p:childTnLst"))
    giren, cikan = {}, {}
    for a in adimlar:
        dc = etree.SubElement(etree.SubElement(sch, qn("p:par")), qn("p:cTn"), id=str(z()), fill="hold")
        etree.SubElement(etree.SubElement(dc, qn("p:stCondLst")), qn("p:cond"), delay="indefinite")
        icc = etree.SubElement(etree.SubElement(etree.SubElement(dc, qn("p:childTnLst")), qn("p:par")), qn("p:cTn"), id=str(z()), fill="hold")
        etree.SubElement(etree.SubElement(icc, qn("p:stCondLst")), qn("p:cond"), delay="0")
        ich = etree.SubElement(icc, qn("p:childTnLst"))
        ilk = True
        for s in a.get("cik", []): ich.append(_etki(z, s.shape_id, False, ilk)); ilk = False; cikan[s.shape_id] = s
        for s in a.get("gir", []): ich.append(_etki(z, s.shape_id, True, ilk)); ilk = False; giren[s.shape_id] = s
    for ad in ("p:prevCondLst", "p:nextCondLst"):
        c = etree.SubElement(etree.SubElement(seq, qn(ad)), qn("p:cond"), evt="onPrev" if "prev" in ad else "onNext", delay="0")
        etree.SubElement(etree.SubElement(c, qn("p:tgtEl")), qn("p:sldTgt"))
    bld = etree.SubElement(timing, qn("p:bldLst"))
    for s, g in [(s, "0") for s in giren.values()] + [(s, "1") for s in cikan.values()]:
        if s._element.tag == qn("p:sp"): etree.SubElement(bld, qn("p:bldP"), spid=str(s.shape_id), grpId=g, animBg="1")
    sl._element.append(timing)


# ---------- slaytlar ----------
for sahne in S:
    D = sahne["durumlar"]; d0 = D[0]
    if "--durum" in sys.argv:
        k = int(sys.argv[sys.argv.index("--durum") + 1]); d0 = dict(D[min(k, len(D) - 1)]); D = [d0]
    sl = prs.slides.add_slide(BOS)
    zem = next(o for o in d0["ogeler"] if o["tip"] == "zemin")
    sl.background.fill.solid(); sl.background.fill.fore_color.rgb = rgb(zem["renk"])
    ogeler0 = [o for o in d0["ogeler"] if o["tip"] != "zemin"]
    aktif = collections.defaultdict(list)          # anahtar -> [şekil listesi]
    adim_sekil = collections.defaultdict(list)
    for o in ogeler0:
        sek = ciz(sl, o)
        aktif[anahtar(o)].append(sek)
        if o.get("adim"): adim_sekil[o["adim"]].extend(sek)
    adimlar = [{"gir": adim_sekil[k]} for k in sorted(adim_sekil)]
    if not ONIZLEME:
        onceki = ogeler0
        for d in D[1:]:
            simdi = [o for o in d["ogeler"] if o["tip"] != "zemin"]
            ca, cb = collections.Counter(map(anahtar, onceki)), collections.Counter(map(anahtar, simdi))
            cik, gir = [], []
            for k, n in (ca - cb).items():
                for _ in range(n): cik.extend(aktif[k].pop())
            kalan = cb - ca
            for o in simdi:
                k = anahtar(o)
                if kalan[k] > 0:
                    kalan[k] -= 1; sek = ciz(sl, o); aktif[k].append(sek); gir.extend(sek)
            adimlar.append({"cik": cik, "gir": gir})
            onceki = simdi
        animasyon(sl, adimlar)
    # notlar
    ipucu = ""
    if len(D) > 1:
        ipucu = "\n\n[Tıklama sırası: " + " → ".join(d["ad"] for d in D[1:]) + "]"
    if d0["adimSay"]:
        ipucu = f"\n\n[Önce {d0['adimSay']} tıklamada öğeler sırayla belirir.]" + ipucu
    sl.notes_slide.notes_text_frame.text = (d0["not"] or "") + ipucu
    if not ONIZLEME and d0["sure"] == 0 and d0["baslik"].startswith("Yedek"):
        sl._element.set("show", "0")        # yedek slayt: gösteride atlanır, gerekince açılır

cikti = KOK / ("onizleme.pptx" if ONIZLEME else "sunum_animasyonlu.pptx")
prs.save(cikti); print("yazıldı:", cikti, len(prs.slides), "slayt")
