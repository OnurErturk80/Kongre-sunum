#!/usr/bin/env python3
"""
Sunum v4 (15 dk): "Yapay zekânın iş akışına entegrasyonu ve ileri istatistik".
Omurga kullanıcının beş sorusu; her sahne bir sorunun cevabıdır.
Sayılar yalnız JSON'lardan gelir: bolumler/0N_sayilar.json, /home/claude/sunum/analiz/ demo JSON'ları, git log.
Çalıştır:  python3 kur_sunum_v4.py  ->  sunum.html, sunucu_notlari.md, analiz/tum_sayilar.json
"""
import os, json, re, subprocess, collections, pathlib, datetime as dt, math, random, sys, shutil

KOK = pathlib.Path(__file__).parent
SKILL = KOK.parent / "skill"
ISKELET = SKILL / "assets/deck_iskelet.html"
REPO = pathlib.Path(os.environ.get("PDC_REPO", str(KOK.parent / "Patient-Data-Center")))
ESKI = KOK.parent / "analiz_demolari"
A = KOK / "analiz"; A.mkdir(exist_ok=True)
sys.path.insert(0, str(SKILL / "scripts"))
import sunum_derle  # font alt kümesi için

NB = " "
yukle = lambda p: json.load(open(p, encoding="utf-8"))
B1, B2, B3, B4, B5 = (yukle(KOK / f"bolumler/0{i}_sayilar.json") for i in range(1, 6))
KP = yukle(ESKI / "sonuc_kpi/sonuclar_kpi.json")
GR = yukle(ESKI / "sonuc_gorsel/sonuclar_gorsel.json")
SZ = yukle(ESKI / "sonuc_slayt/sonuclar.json")


def d(B, k): return B[k]["deger"]
def n(x): return f"{int(round(x)):,}".replace(",", NB)            # 1 066
def nd(x): return f"{int(round(x)):,}".replace(",", "\u00a0")       # başlık yazı tipinde dar boşluk kayboluyor
def f(x, k=2): return f"{x:.{k}f}".replace("-", "−")
def y(x, k=1): return "%" + f"{x:.{k}f}"                           # 46.5 -> %46.5
def yo(x, k=1): return "%" + f"{x*100:.{k}f}"                      # 0.966 -> %96.6


# ---------- depo (git) ----------
gun = subprocess.run(["git", "-C", str(REPO), "log", "--format=%ad", "--date=short"], capture_output=True, text=True).stdout.split()
say = collections.Counter(gun); gl = sorted(say)
d0, d1 = dt.date.fromisoformat(gl[0]), dt.date.fromisoformat(gl[-1])
tum = [d0 + dt.timedelta(days=i) for i in range((d1 - d0).days + 1)]
DEPO = dict(commit=len(gun), gun=(d1 - d0).days + 1, commit_gunu=len(gl),
            surum_notu=int(subprocess.run(["grep", "-c", "^# v", str(REPO / "README.md")], capture_output=True, text=True).stdout))
assert DEPO["commit"] == d(B5, "depo_commit") and DEPO["gun"] == d(B5, "depo_gun") and DEPO["surum_notu"] == d(B5, "depo_surum_notu"), DEPO


def git_svg():
    mx = max(say.values()); W, H = 760, 150; bw = W / len(tum)
    o = [f'<rect x="{i*bw+2:.1f}" y="{H-(say.get(g.isoformat(),0)/mx)*(H-8):.1f}" width="{bw-4:.1f}" height="{(say.get(g.isoformat(),0)/mx)*(H-8):.1f}" fill="var(--metin)"/>' for i, g in enumerate(tum)]
    o.append(f'<line x1="0" x2="{W}" y1="{H}" y2="{H}" stroke="var(--metin)" stroke-width="2"/>')
    o.append(f'<text x="0" y="{H+30}" fill="var(--soluk)" font-size="22">{d0.day} Eylül</text>')
    o.append(f'<text x="{W/2}" y="{H+30}" fill="var(--soluk)" font-size="22" text-anchor="middle">günlük commit sayısı</text>')
    o.append(f'<text x="{W}" y="{H+30}" text-anchor="end" fill="var(--soluk)" font-size="22">{d1.day} Ekim 2026</text>')
    return f'<svg viewBox="0 0 {W} {H+38}" style="width:100%;height:auto;display:block" role="img" aria-label="Günlük commit sayısı">{"".join(o)}</svg>'


# ---------- şekiller (hepsi sayılardan çizilir) ----------
def T(x, yy, s, boy=26, ag=400, renk="var(--metin)", capa="start", ek=""):
    return f'<text x="{x:.1f}" y="{yy:.1f}" font-size="{boy}" font-weight="{ag}" fill="{renk}" text-anchor="{capa}" {ek}>{s}</text>'


def zaman_cizgisi():
    W, H = 1624, 624
    X = lambda yil: 70 + (yil - 1997) / 29 * 1480
    YA, KL, DZ, EK = 190, 420, 528, 580
    o = []
    # eksen
    o.append(f'<line x1="70" x2="1550" y1="{EK}" y2="{EK}" stroke="var(--metin)" stroke-width="3"/>')
    for yil in (1997, 2000, 2005, 2010, 2015, 2020, 2025):
        o.append(f'<line x1="{X(yil):.1f}" x2="{X(yil):.1f}" y1="{EK}" y2="{EK+12}" stroke="var(--metin)" stroke-width="3"/>')
        o.append(T(X(yil), EK + 40, str(yil), 24, 600, "var(--soluk)", "middle"))
    for yy, ad in ((YA, "YAYIN"), (KL, "KLİNİK İLK"), (DZ, "DÜZENLEYİCİ")):
        o.append(f'<line x1="70" x2="1550" y1="{yy}" y2="{yy}" stroke="var(--cizgi)" stroke-width="3"/>')
        o.append(T(70, yy + 32, ad, 19, 700, "var(--soluk)", ek='letter-spacing="2.6"'))
    nokta = lambda x, yy, bos=False: f'<circle cx="{x:.1f}" cy="{yy}" r="12" fill="{"var(--zemin)" if bos else "var(--metin)"}" stroke="var(--metin)" stroke-width="4"/>'
    yb = lambda yil, s: f'<tspan font-weight="800">{yil}</tspan> · {s}'
    # adım 1: 1997, 2010
    g = [nokta(X(1997), YA), T(70, YA - 32, yb(1997, 'sinir ağıyla IVF tahmini')),
         nokta(X(2010), YA), T(X(2010), YA - 32, yb(2010, "kişiye özel canlı doğum modeli"), capa="middle")]
    o.append(f'<g data-adim="1">{"".join(g)}</g>')
    # adım 2: 2018 kırılma, 2019
    b17, b18 = d(B1, "curchoe_2019_bildiri_2017"), d(B1, "curchoe_2019_bildiri_2018")
    k = 5.2
    g = [f'<rect x="{X(2017)-16:.1f}" y="{YA-b17*k:.1f}" width="32" height="{b17*k:.1f}" fill="var(--metin)"/>',
         T(X(2017), YA - b17 * k - 10, str(b17), 26, 800, capa="middle"),
         f'<rect x="{X(2018)-16:.1f}" y="{YA-b18*k:.1f}" width="32" height="{b18*k:.1f}" fill="var(--sari)" stroke="var(--metin)" stroke-width="3"/>',
         T(X(2018), YA - b18 * k - 10, str(b18), 26, 800, capa="middle"),
         T(X(2018) + 34, YA - 52, yb(2018, f"kongre bildirisi {b17} → {b18}")),
         nokta(X(2019), YA), f'<line x1="{X(2019):.1f}" x2="{X(2019):.1f}" y1="{YA+14}" y2="{YA+38}" stroke="var(--metin)" stroke-width="2.5"/>',
         T(1560, YA + 66, yb(2019, "derin öğrenme embriyo görüntüsünde"), capa="end")]
    o.append(f'<g data-adim="2">{"".join(g)}</g>')
    # adım 3: klinik ilkler + düzenleyici
    g = []
    for yil, s, yy in ((2023, "ilk otomatik ICSI bebekleri", KL - 34), (2024, f'ilk büyük RKÇ, {n(d(B1,"illingworth_2024_hasta"))} hasta', KL - 74), (2025, "uzaktan ICSI ile ilk doğum", KL - 114)):
        g.append(f'<line x1="{X(yil):.1f}" x2="{X(yil):.1f}" y1="{KL}" y2="{yy-9}" stroke="var(--metin)" stroke-width="2.5"/>')
        g.append(nokta(X(yil), KL)); g.append(T(X(yil) - 12, yy, yb(yil, s), capa="end"))
    g.append(nokta(X(2025.7), DZ, True))
    g.append(T(X(2025.7) - 24, DZ - 20, yb(2025, 'FDA 510(k)* <tspan fill="var(--vurgu)" font-weight="700">ikincil kaynak</tspan>'), capa="end"))
    o.append(f'<g data-adim="3">{"".join(g)}</g>')
    return f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block" role="img" aria-label="İlkler zaman çizgisi, 1997–2026">{"".join(o)}</svg>'


def orman():
    gv = B3["_grafik_verisi"]["orman_ARD"]["satirlar"]
    W, H = 1150, 610
    px0, olc = 520, 19.0                               # −12 → 520 ; +8 → 900
    X = lambda v: px0 + (v + 12) * olc
    ys = [102, 172, 242, 388, 458]
    ad = [f'Time-lapse genel · {d(B3,"bhide_TLI_genel")["rkc"]} RKÇ · n={n(d(B3,"bhide_TLI_genel")["n"])}',
          f'Kesintisiz kültür · {d(B3,"bhide_kesintisiz_kultur")["rkc"]} RKÇ · n={n(d(B3,"bhide_kesintisiz_kultur")["n"])}',
          f'Morfokinetik seçim · {d(B3,"bhide_morfokinetik_secim")["rkc"]} RKÇ · n={n(d(B3,"bhide_morfokinetik_secim")["n"])}',
          f'Canlı doğum · 1 RKÇ · n={n(d(B3,"illingworth_n_hasta"))}',
          f'Klinik gebelik (birincil sonlanım)']
    o = []
    o.append(f'<rect x="0" y="8" width="{W}" height="40" fill="var(--metin)"/>' + T(14, 36, "TIME-LAPSE / MORFOKİNETİK · derin öğrenme değil · hasta düzeyinde meta-analiz", 21, 700, "var(--zemin)", ek='letter-spacing="1.2"'))
    o.append(f'<rect x="0" y="294" width="{W}" height="40" fill="var(--metin)"/>' + T(14, 322, "DERİN ÖĞRENME · bugüne kadarki tek büyük RKÇ", 21, 700, "var(--zemin)", ek='letter-spacing="1.2"'))
    o.append(f'<line x1="{X(0):.1f}" x2="{X(0):.1f}" y1="56" y2="530" stroke="var(--metin)" stroke-width="3"/>')
    for i, r in enumerate(gv):
        yy = ys[i]
        o.append(T(14, yy + 9, ad[i], 27, 600))
        o.append(f'<line x1="{X(r["alt"]):.1f}" x2="{X(r["ust"]):.1f}" y1="{yy}" y2="{yy}" stroke="var(--metin)" stroke-width="5"/>')
        for u in (r["alt"], r["ust"]):
            o.append(f'<line x1="{X(u):.1f}" x2="{X(u):.1f}" y1="{yy-10}" y2="{yy+10}" stroke="var(--metin)" stroke-width="5"/>')
        o.append(f'<rect x="{X(r["nokta"])-12:.1f}" y="{yy-12}" width="24" height="24" fill="var(--sari)" stroke="var(--metin)" stroke-width="4"/>')
        o.append(T(926, yy + 9, f'{f(r["nokta"],1)} ({f(r["alt"],1)} ile {f(r["ust"],1)})', 26, 600))
    ni = d(B3, "illingworth_noninferiority_siniri")
    o.append(f'<line x1="{X(ni):.1f}" x2="{X(ni):.1f}" y1="{ys[4]-28}" y2="{ys[4]+26}" stroke="var(--vurgu)" stroke-width="4" stroke-dasharray="7 6"/>')
    o.append(T(X(ni) - 12, ys[4] + 48, f"güven aralığı eşdeğerlik sınırını ({f(ni,0)}) aşıyor", 22, 700, "var(--vurgu)", "end"))
    o.append(f'<line x1="{X(-12):.1f}" x2="{X(8):.1f}" y1="530" y2="530" stroke="var(--metin)" stroke-width="2.5"/>')
    for v in (-12, -8, -4, 0, 4, 8):
        o.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="530" y2="540" stroke="var(--metin)" stroke-width="2.5"/>')
        o.append(T(X(v), 566, f(v, 0), 22, 600, "var(--soluk)", "middle"))
    o.append(T(X(0) - 16, 598, "← standart lehine", 21, 400, "var(--soluk)", "end"))
    o.append(T(X(0) + 16, 598, "YZ / time-lapse lehine →", 21, 400, "var(--soluk)"))
    o.append(T(14, 566, "Canlı doğumda mutlak risk farkı", 22, 600, "var(--soluk)"))
    o.append(T(14, 596, "(yüzde puan, %95 GA)", 21, 400, "var(--soluk)"))
    return f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block" role="img" aria-label="Canlı doğum için mutlak risk farkları">{"".join(o)}</svg>'


def orman_oran():
    gv = B3["_grafik_verisi"]["orman_oran"]["satirlar"]
    W, lo, hi, xl, xr = 1500, 0.70, 1.35, 760, 1180
    X = lambda v: xl + (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (xr - xl)
    o = []; yb = 40 + len(gv) * 84
    o.append(f'<line x1="{X(1):.1f}" x2="{X(1):.1f}" y1="10" y2="{yb-10}" stroke="var(--metin)" stroke-width="3"/>')
    for i, r in enumerate(gv):
        yy = 56 + i * 84
        o.append(T(0, yy + 9, r["etiket"], 28, 600))
        o.append(f'<line x1="{X(r["alt"]):.1f}" x2="{X(r["ust"]):.1f}" y1="{yy}" y2="{yy}" stroke="var(--metin)" stroke-width="5"/>')
        o.append(f'<rect x="{X(r["nokta"])-12:.1f}" y="{yy-12}" width="24" height="24" fill="var(--sari)" stroke="var(--metin)" stroke-width="4"/>')
        o.append(T(1220, yy + 9, f'{f(r["nokta"])} ({f(r["alt"])}–{f(r["ust"])})', 28, 600))
    for v in (0.8, 1.0, 1.2):
        o.append(T(X(v), yb + 26, f"{v:.1f}", 22, 600, "var(--soluk)", "middle", 'data-sayi-ok="1"'))
    o.append(T(X(1), yb + 58, "1 = fark yok (log ölçek)", 21, 400, "var(--soluk)", "middle"))
    return f'<svg viewBox="0 0 {W} {yb+70}" style="width:100%;height:auto;display:block" role="img" aria-label="Oran ölçeğinde etki büyüklükleri">{"".join(o)}</svg>'


def auc_cetveli():
    W, x0, x1 = 1624, 470, 1250
    X = lambda v: x0 + (v - 0.5) / 0.5 * (x1 - x0)
    dolu = lambda v, o_=0: (lambda yy: f'<circle cx="{X(v):.1f}" cy="{yy+o_}" r="11" fill="var(--metin)"/>')
    bos = lambda v, o_=0: (lambda yy: f'<circle cx="{X(v):.1f}" cy="{yy+o_}" r="10" fill="var(--zemin)" stroke="var(--metin)" stroke-width="4"/>')
    elmas = lambda v, o_=0: (lambda yy: f'<rect x="{X(v)-10:.1f}" y="{yy+o_-10}" width="20" height="20" fill="var(--sari)" stroke="var(--metin)" stroke-width="3.5" transform="rotate(45 {X(v):.1f} {yy+o_})"/>')
    ara = lambda a_, b_, o_=0: (lambda yy: f'<line x1="{X(a_):.1f}" x2="{X(b_):.1f}" y1="{yy+o_}" y2="{yy+o_}" stroke="var(--metin)" stroke-width="12" opacity=".2" stroke-linecap="round"/>')
    g = lambda k: d(B4, k)
    satir = [
        ("Embriyo → kalp atımı", "transfer edilen embriyolar",
         [ara(g("berntsen_klinik_alt"), g("berntsen_klinik_ust"), -9), ara(g("ueno_auc_min"), g("ueno_auc_max"), 9),
          dolu(g("thirumalaraju_auc"), 0), dolu(g("berntsen_kid"), 0), elmas(g("mina_auc"), 0)],
         f'{f(min(g("berntsen_klinik_alt"), g("thirumalaraju_auc")))}–{f(g("ueno_auc_max"))}', ""),
        ("Görüntüden ploidi", "biyopsisiz tahmin",
         [dolu(g("ma_idascore_tek"), 0), dolu(g("ma_idascore_klinik"), 0), bos(g("barnes_dis1"), 0), bos(g("bamford_lr"), -17), bos(g("barnes_dis2"), 17),
          dolu(g("barnes_test"), 0), elmas(g("xin_auc"), 0)],
         f'{f(g("ma_idascore_tek"))}–{f(g("barnes_test"))}', f'meta-analiz {f(g("xin_auc"))}'),
        ("Oosit → öploidi", "oosit görüntü skoru",
         [dolu(g("magenta_tek"), 0), bos(g("magenta_donor_blast"), 17), dolu(g("magenta_robust"), 0), dolu(g("magenta_tam"), 0)],
         f'{f(g("magenta_tek"))}–{f(g("magenta_tam"))}', f'tek başına {f(g("magenta_tek"))}'),
        ("Tedavi öncesi canlı doğum", "hasta düzeyinde modeller",
         [ara(g("cai_dis_min"), g("cai_dis_max"), 0), bos(g("ratna_on"), -17), dolu(g("cai_merkez"), 0), bos(g("ratna_sonra"), 0)],
         f'{f(g("cai_dis_min"))}–{f(g("ratna_sonra"))}', ""),
    ]
    o = []; dy = 104
    yb = 30 + len(satir) * dy
    o.append(f'<line x1="{X(.5):.1f}" x2="{X(.5):.1f}" y1="10" y2="{yb}" stroke="var(--vurgu)" stroke-width="3" stroke-dasharray="6 6"/>')
    for i, (ad, alt, icerik, ozet, ek) in enumerate(satir):
        yy = 56 + i * dy
        o.append(T(0, yy - 2, ad, 30, 700)); o.append(T(0, yy + 28, alt, 22, 400, "var(--soluk)"))
        o.append(f'<line x1="{x0}" x2="{x1}" y1="{yy}" y2="{yy}" stroke="var(--cizgi)" stroke-width="3"/>')
        for ciz in icerik:
            o.append(ciz(yy))
        o.append(T(1290, yy + 12, ozet, 44, 800, ek='font-family="Inter Display,Inter,sans-serif" letter-spacing="-1"'))
        if ek: o.append(T(1290, yy + 40, ek, 21, 600, "var(--soluk)"))
    o.append(f'<line x1="{x0}" x2="{x1}" y1="{yb}" y2="{yb}" stroke="var(--metin)" stroke-width="3"/>')
    for v in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        o.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{yb}" y2="{yb+12}" stroke="var(--metin)" stroke-width="3"/>')
        o.append(T(X(v), yb + 40, f"{v:.1f}", 24, 600, "var(--soluk)", "middle", 'data-sayi-ok="1"'))
    o.append(T(X(.5), yb + 68, "yazı-tura", 22, 700, "var(--vurgu)", "middle"))
    o.append(T(X(1), yb + 68, "kusursuz", 22, 700, "var(--soluk)", "middle"))
    lx = 0; ly = yb + 50
    o.append(f'<circle cx="{lx+12}" cy="{ly-7}" r="10" fill="var(--metin)"/>' + T(lx + 30, ly, "iç doğrulama", 21, 400, "var(--soluk)"))
    o.append(f'<circle cx="{lx+190}" cy="{ly-7}" r="9" fill="var(--zemin)" stroke="var(--metin)" stroke-width="4"/>' + T(lx + 208, ly, "dış / prospektif", 21, 400, "var(--soluk)"))
    o.append(f'<rect x="{lx+4}" y="{ly+20}" width="16" height="16" fill="var(--sari)" stroke="var(--metin)" stroke-width="3" transform="rotate(45 {lx+12} {ly+28})"/>' + T(lx + 30, ly + 35, "meta-analiz", 21, 400, "var(--soluk)"))
    o.append(f'<line x1="{lx+180}" x2="{lx+204}" y1="{ly+28}" y2="{ly+28}" stroke="var(--metin)" stroke-width="12" opacity=".2" stroke-linecap="round"/>' + T(lx + 214, ly + 35, "bildirilen aralık", 21, 400, "var(--soluk)"))
    return f'<svg viewBox="0 0 {W} {yb+92}" style="width:100%;height:auto;display:block" role="img" aria-label="Görev başına yayımlanmış AUC değerleri">{"".join(o)}</svg>'


def nokta_bulutu():
    N = round(d(B4, "berntsen_test_embriyo") / 100); K = round(d(B4, "berntsen_test_kid") / 100)
    sec = set(random.Random(11).sample(range(N), K)); sut = 15; ar = 34
    o = [f'<circle class="{"kid" if i in sec else "atik"}" cx="{17+(i%sut)*ar}" cy="{17+(i//sut)*ar}" r="12"/>' for i in range(N)]
    return f'<svg id="bulut" viewBox="0 0 {sut*ar} {math.ceil(N/sut)*ar}" style="width:100%;height:auto;display:block" role="img" aria-label="Test setindeki embriyolar">{"".join(o)}</svg>'


def merkez_seridi():
    L = sorted(d(B4, "berntsen_klinik_listesi")); W = 520
    X = lambda v: 40 + (v - 0.55) / 0.25 * (W - 80)
    o = [f'<line x1="20" x2="{W-20}" y1="80" y2="80" stroke="var(--metin)" stroke-width="3"/>']
    gor = collections.Counter()
    for v in L:
        gor[v] += 1
        o.append(f'<circle cx="{X(v):.1f}" cy="{80-(gor[v]-1)*24}" r="11" fill="var(--sari)" stroke="var(--metin)" stroke-width="3.5"/>')
    for v in (0.60, 0.70, 0.80):
        o.append(T(X(v), 122, f"{v:.2f}", 22, 600, "var(--soluk)", "middle", 'data-sayi-ok="1"'))
    return f'<svg viewBox="0 0 {W} 130" style="width:100%;height:auto;display:block">{"".join(o)}</svg>'


def funnel():
    fu = KP["funnel"]; p = fu["genel_oran"]; W, H = 800, 500
    X = lambda nn: 80 + nn / 700 * 640
    Y = lambda v: 440 - (v - 0.55) / 0.35 * 400
    o = []
    for z, kalin, ad in ((fu["sinir_z"][0], 2.5, f'%{fu["sinirlar_yuzde"][0]}'), (fu["sinir_z"][1], 4, f'%{fu["sinirlar_yuzde"][1]}')):
        for isr in (1, -1):
            pts = " ".join(f'{X(nn):.1f},{Y(min(.9, max(.55, p + isr*z*math.sqrt(p*(1-p)/nn)))):.1f}' for nn in range(40, 701, 10))
            o.append(f'<polyline points="{pts}" fill="none" stroke="var(--metin)" stroke-width="{kalin}" {"stroke-dasharray=\"8 7\"" if kalin < 3 else ""}/>')
        isr = 1 if kalin < 3 else -1
        o.append(T(X(700) + 6, Y(p + isr * z * math.sqrt(p * (1 - p) / 700)) + 8, ad, 21, 600, "var(--soluk)"))
    o.append(f'<line x1="{X(0)}" x2="{X(700)}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" stroke="var(--soluk)" stroke-width="2.5"/>')
    o.append(T(X(0) + 8, Y(p) - 10, f"genel oran {yo(p)}", 21, 600, "var(--soluk)"))
    o.append(f'<line x1="{X(0)}" x2="{X(700)}" y1="440" y2="440" stroke="var(--metin)" stroke-width="2.5"/><line x1="{X(0)}" x2="{X(0)}" y1="40" y2="440" stroke="var(--metin)" stroke-width="2.5"/>')
    for v in (0.6, 0.7, 0.8, 0.9):
        o.append(T(X(0) - 12, Y(v) + 8, f"%{int(v*100)}", 22, 600, "var(--soluk)", "end"))
    for nn in (0, 200, 400, 600):
        o.append(T(X(nn), 470, str(nn), 22, 600, "var(--soluk)", "middle"))
    o.append(T(X(350), 498, "olgu sayısı (n)", 21, 400, "var(--soluk)", "middle"))
    for ad, e in fu["embriyologlar"].items():
        ozel = ad in ("E", "F")
        o.append(f'<g class="fn" data-ham="translate({X(e["n"]):.1f}px,{Y(e["ham"]):.1f}px)" data-ay="translate({X(e["n"]):.1f}px,{Y(e["ayarli"]):.1f}px)" style="transform:translate({X(e["n"]):.1f}px,{Y(e["ham"]):.1f}px)">'
                 f'<circle r="{17 if ozel else 13}" fill="{"var(--sari)" if ad=="F" else ("var(--vurgu)" if ad=="E" else "var(--metin)")}" stroke="var(--metin)" stroke-width="3.5"/>'
                 f'<text x="{dict(A=6, B=-8, C=-36, D=20).get(ad, 26)}" y="{dict(A=38, B=-20, C=-12, D=-14).get(ad, 10)}" font-size="{32 if ozel else 25}" font-weight="800" fill="var(--metin)">{ad}</text></g>')
    return f'<svg id="funnel" viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block" role="img" aria-label="Funnel grafiği">{"".join(o)}</svg>'


def kpi_seri():
    """kpi_demo.py'nin erken_uyari() adımlarını aynı tohumla yeniden üretir (şekli sunum paletinde çizebilmek için); sonuç JSON ile sınanır."""
    import numpy as np
    g = KP["gercek_parametreler"]; H = g["hafta_sayisi"]; rng = np.random.default_rng(KP["seed"])
    nn = rng.poisson(g["haftalik_ort_vaka"], H)
    pp = np.where(np.arange(H) < g["kayma_haftasi"], g["taban_oran"], g["kayma_sonrasi_oran"])
    x = rng.binomial(nn, pp)
    ay = np.arange(H) // 4; n_ay = np.bincount(ay, nn); p_ay = np.bincount(ay, x) / n_ay
    p0 = x[:52].sum() / nn[:52].sum(); alt = p0 - 3 * np.sqrt(p0 * (1 - p0) / n_ay)
    a_ = np.log(g["cusum_alternatif"] / p0); b_ = np.log((1 - g["cusum_alternatif"]) / (1 - p0))
    C = np.zeros(H); alarm = None
    for t in range(52, H):
        C[t] = max(0.0, C[t - 1] + x[t] * a_ + (nn[t] - x[t]) * b_)
        if alarm is None and C[t] > g["cusum_esik_h"] and t >= g["kayma_haftasi"]: alarm = t
    eu = KP["erken_uyari"]
    assert abs(p0 - eu["taban_oran_tahmini"]) < 1e-12 and alarm + 1 - g["kayma_haftasi"] == eu["cusum_gecikme_hafta"], "seri JSON ile uyuşmuyor"
    return p_ay, alt, C, alarm


def cusum_sekli():
    p_ay, alt, C, alarm = kpi_seri(); g = KP["gercek_parametreler"]; H = g["hafta_sayisi"]
    W, Ht = 777, 446
    X = lambda t: 76 + t / H * 680
    Y1 = lambda v: 176 - (v - 0.58) / 0.24 * 150          # üst panel: 0.60–0.82
    cmax = max(C) * 1.05; Y2 = lambda v: 392 - v / cmax * 160
    o = []
    for yy0, yy1 in ((20, 180), (228, 392)):
        o.append(f'<line x1="{X(0)}" x2="{X(0)}" y1="{yy0}" y2="{yy1}" stroke="var(--metin)" stroke-width="2.5"/><line x1="{X(0)}" x2="{X(H)}" y1="{yy1}" y2="{yy1}" stroke="var(--metin)" stroke-width="2.5"/>')
    k = g["kayma_haftasi"]
    o.append(f'<line x1="{X(k):.1f}" x2="{X(k):.1f}" y1="14" y2="392" stroke="var(--vurgu)" stroke-width="3" stroke-dasharray="4 6"/>')
    o.append(T(X(k) + 8, 30, "düşüş başlıyor", 21, 700, "var(--vurgu)"))
    for v in (0.65, 0.70, 0.75, 0.80):
        o.append(T(X(0) - 10, Y1(v) + 7, f"%{round(v*100)}", 21, 600, "var(--soluk)", "end"))
    xs = [i * 4 + 2 for i in range(len(p_ay))]
    o.append(f'<polyline points="{" ".join(f"{X(t):.1f},{Y1(v):.1f}" for t, v in zip(xs, alt))}" fill="none" stroke="var(--soluk)" stroke-width="2.5" stroke-dasharray="7 6"/>')
    o.append(f'<polyline points="{" ".join(f"{X(t):.1f},{Y1(v):.1f}" for t, v in zip(xs, p_ay))}" fill="none" stroke="var(--mavi)" stroke-width="3.5"/>')
    o += [f'<circle cx="{X(t):.1f}" cy="{Y1(v):.1f}" r="6" fill="var(--mavi)"/>' for t, v in zip(xs, p_ay)]
    o.append(T(X(2), 30, "Aylık ortalama", 22, 700, "var(--mavi)"))
    o.append(T(X(2), Y1(alt[0]) + 28, "alt kontrol sınırı (3σ)", 20, 400, "var(--soluk)"))
    esik = g["cusum_esik_h"]
    o.append(f'<line x1="{X(0)}" x2="{X(H)}" y1="{Y2(esik):.1f}" y2="{Y2(esik):.1f}" stroke="var(--metin)" stroke-width="2.5" stroke-dasharray="7 6"/>')
    o.append(T(X(2), Y2(esik) + 26, f"alarm eşiği {f(esik,1)}", 20, 400, "var(--soluk)"))
    o.append(f'<polyline points="{" ".join(f"{X(t):.1f},{Y2(v):.1f}" for t, v in enumerate(C))}" fill="none" stroke="var(--metin)" stroke-width="4"/>')
    o.append(f'<circle cx="{X(alarm):.1f}" cy="{Y2(C[alarm]):.1f}" r="13" fill="var(--sari)" stroke="var(--metin)" stroke-width="4"/>')
    o.append(T(X(k) - 12, Y2(esik) - 14, f"alarm: {KP['erken_uyari']['cusum_gecikme_hafta']} hafta sonra", 21, 700, capa="end"))
    o.append(T(X(2), 252, "Haftalık CUSUM", 22, 700))
    for t in (0, 20, 40, 60, 80, 100):
        o.append(T(X(t), 420, str(t), 21, 600, "var(--soluk)", "middle"))
    o.append(T(X(H), 444, "hafta", 20, 400, "var(--soluk)", "end"))
    return f'<svg viewBox="0 0 {W} {Ht}" style="width:100%;height:auto;display:block" role="img" aria-label="Aylık ortalama ve haftalık CUSUM, sentetik veri">{"".join(o)}</svg>'


def ince_ayar():
    ia = GR["ince_ayar"]; W, H = 620, 330
    X = lambda i: 80 + i * 100
    Y = lambda v: 270 - (v - 0.5) / 0.5 * 230
    o = [f'<line x1="60" x2="600" y1="270" y2="270" stroke="var(--metin)" stroke-width="2.5"/>']
    ev = ia["hazir_model_kendi_labinda_auc"]
    o.append(f'<line x1="60" x2="600" y1="{Y(ev):.1f}" y2="{Y(ev):.1f}" stroke="var(--soluk)" stroke-width="2.5" stroke-dasharray="7 6"/>')
    o.append(T(600, Y(ev) - 9, f"kendi labında {f(ev)}", 20, 600, "var(--soluk)", "end"))
    o.append(f'<polyline points="{" ".join(f"{X(i)},{Y(v):.1f}" for i, v in enumerate(ia["auc"]))}" fill="none" stroke="var(--metin)" stroke-width="4"/>')
    for i, v in enumerate(ia["auc"]):
        o.append(f'<circle cx="{X(i)}" cy="{Y(v):.1f}" r="{13 if i < 2 else 9}" fill="{"var(--sari)" if i < 2 else "var(--metin)"}" stroke="var(--metin)" stroke-width="3.5"/>')
        o.append(T(X(i), 300, str(ia["yerel_n"][i]), 21, 600, "var(--soluk)", "middle"))
    o.append(T(X(0) + 20, Y(ia["auc"][0]) - 8, f(ia["auc"][0]), 30, 800))
    o.append(T(X(1) + 6, Y(ia["auc"][1]) + 44, f(ia["auc"][1]), 30, 800))
    o.append(T(330, 326, "yerel etiket sayısı", 20, 400, "var(--soluk)", "middle"))
    return f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block" role="img" aria-label="Yerel etiketle ince ayar">{"".join(o)}</svg>'


def sizinti():
    W = 1624; X = lambda v: 360 + (v - 0.60) / 0.14 * 520
    o = []
    for i, (kod, ad) in enumerate((("gbm", "Gradyan artırma"), ("lr", "Lojistik regresyon"))):
        a = SZ["auc"][kod]; yy = 60 + i * 120
        o.append(T(0, yy + 10, ad, 32, 700))
        o.append(f'<line x1="{X(.60)}" x2="{X(.74)}" y1="{yy}" y2="{yy}" stroke="var(--cizgi)" stroke-width="3"/>')
        for tur, renk in (("zamansal", "var(--zemin)"), ("hasta_gruplu", "var(--metin)"), ("rastgele", "var(--vurgu)")):
            o.append(f'<circle cx="{X(a[tur]):.1f}" cy="{yy}" r="13" fill="{renk}" stroke="var(--metin)" stroke-width="4"/>')
        o.append(T(940, yy + 10, f'rastgele {f(a["rastgele"],3)} · hasta-gruplu {f(a["hasta_gruplu"],3)} · zamansal {f(a["zamansal"],3)}', 26, 600))
    for v in (0.60, 0.65, 0.70):
        o.append(T(X(v), 250, f"{v:.2f}", 22, 600, "var(--soluk)", "middle", 'data-sayi-ok="1"'))
    return f'<svg viewBox="0 0 {W} 262" style="width:100%;height:auto;display:block">{"".join(o)}</svg>'


# ---------- eski matplotlib şekillerini yeni palete çevir ----------
def renk_cevir(kaynak, hedef):
    s = open(kaynak, encoding="utf-8").read()
    for a, b in (("#e4572e", "#c7361f"), ("#2a6f97", "#1f5faf"), ("#14213d", "#111a27"), ("fill: #ffffff", "fill: none")):
        s = s.replace(a, b)
    open(hedef, "w", encoding="utf-8").write(s)


renk_cevir(ESKI / "sonuc_gorsel/fig_kalite_kontrol.svg", A / "fig_kalite_kontrol.svg")


# ---------- yazı tipleri (motorun gömdüğü Inter'e ek: soru sesi için Lora italik, cevap için Inter Display 800/900) ----------
def ek_font():
    css = []
    for aile, ag, stil, yol in (("Lora", "400 700", "italic", str(KOK.parent / "fontlar/Lora-Italic-Variable.ttf")),
                                ("Inter Display", "800", "normal", str(KOK.parent / "fontlar/InterDisplay-ExtraBold.otf")),
                                ("Inter Display", "900", "normal", str(KOK.parent / "fontlar/InterDisplay-Black.otf"))):
        css.append(f'@font-face{{font-family:"{aile}";font-weight:{ag};font-style:{stil};font-display:block;src:url(data:font/woff;base64,{sunum_derle.alt_kume_b64(yol)}) format("woff");}}')
    return "\n".join(css)


# ---------- kaynakça: PMID'ler bölüm dosyalarındaki tablolardan okunur (elle yazılmaz) ----------
PM = {}
for dosya in sorted((KOK / "bolumler").glob("0*_*.md")):
    for satir in dosya.read_text(encoding="utf-8").splitlines():
        h = [c.strip() for c in satir.split("|")]
        if len(h) >= 6 and re.fullmatch(r"[a-z_0-9]+", h[1] or "") and re.match(r"\d{7,8}", h[3] or ""):
            PM.setdefault(h[1], re.match(r"\d{7,8}", h[3]).group(0))
PM.update(yamada_2024=re.search(r"\d+", B2["japonya_yanit_tesis"]["kaynak"]).group(0),
          palmer_2024=re.search(r"\d+", B2["uluslararasi_anket_yanit"]["kaynak"]).group(0),
          du_2026=re.search(r"\d+", B2["firma_sitesi_sayisi"]["kaynak"]).group(0))
KAYNAK = [  # (kısa künye, anahtar)
    [("Kaufmann 1997 Hum Reprod", "kaufmann_1997"), ("Banerjee 2010 PNAS", "banerjee_2010"), ("Curchoe &amp; Bormann 2019 JARG", "curchoe_2019"),
     ("Khosravi 2019 npj Digit Med", "khosravi_2019"), ("Tran 2019 Hum Reprod", "tran_2019"), ("Costa-Borges 2023 RBMO", "costa_borges_2023"),
     ("Mendizabal-Ruiz 2025 RBMO", "mendizabal_ruiz_2025"), ("Chavez-Badiola 2026 Hum Reprod", "chavez_badiola_2026"), ("Yao 2025 Nat Commun", "yao_2025"),
     ("Canon 2024 Sci Rep", "canon_2024"), ("Wygocki 2026 JARG", "wygocki_2026"), ("Cimadomo 2025 Hum Reprod", "cimadomo_2025"),
     ("Montjean 2024 Med Sci", "montjean_2024"), ("Liang 2023 RBMO", "liang_2023"), ("Bormann 2021 JARG", "bormann_2021"),
     ("Allen 2026 JARG (YZ çalışması değil)", "allen_2026"), ("Chervenak 2023 Fertil Steril", "chervenak_2023"), ("Chang 2026 Front Endocrinol (ikincil)", "chang_2026"),
     ("Yamada 2024 AJOG Glob Rep", "yamada_2024"), ("Palmer 2024 RBMO", "palmer_2024"), ("Du &amp; Zhang 2026 Hum Reprod Open", "du_2026")],
    [("Illingworth 2024 Nat Med", "illingworth2024"), ("Bhide 2026 Hum Reprod Update", "bhide2026"), ("Kieslinger 2023 Lancet (SelecTIMO)", "selectimo_lancet2023"),
     ("Kieslinger 2026 Hum Reprod Open (maliyet)", "selectimo_cea2026"), ("Kieslinger 2026 Hum Reprod (perinatal)", "selectimo_perinatal2026"),
     ("Yaghi 2026 Eur J Obstet Gynecol", "yaghi2026"), ("Bormann 2020 Fertil Steril", "bormann2020"), ("Zaninovic 2023 F S Sci", "zaninovic2023"),
     ("Thirumalaraju 2025 Fertil Steril", "thirumalaraju2025"), ("Bixby &amp; Miller 2025 F S Rep", "bixby2025"), ("Cromack 2025 JARG", "cromack2025"),
     ("Koplin 2025 Hum Reprod", "koplin2025"), ("Berntsen 2022 PLoS One", "berntsen_2022"), ("Kragh &amp; Karstoft 2021 JARG", "kragh_2021"),
     ("Ueno 2021 Fertil Steril", "ueno_2021"), ("Mina 2025 Contracept Reprod Med", "mina_2025"), ("Barnes 2023 Lancet Digit Health", "barnes_2023"),
     ("Bamford 2023 Hum Reprod", "bamford_2023"), ("Ma 2024 Reprod Biol Endocrinol", "ma_2024"), ("Xin 2024 eClinicalMedicine", "xin_2024"),
     ("Setti 2026 F S Sci", "setti_2026"), ("Cai 2024 Hum Reprod", "cai_2024"), ("Ratna 2023 Hum Reprod", "ratna_2023"),
     ("Wilkinson 2025 RBMO", "wilkinson_2025"), ("Berman 2023 AJOG", "berman_2023"), ("Varzaneh 2026 Int J Med Inform", "varzaneh_2026"),
     ("Vienna konsensüsü 2017 RBMO / Hum Reprod Open", "vienna_rbmo"), ("Zacà 2022 JARG", "zaca_2022")],
]


def kaynakca(i):
    return "".join(f'<p data-sayi-ok="1">{ad} · PMID {PM[k]}</p>' for ad, k in KAYNAK[i])


# ---------- sahne iskeleti ----------
SORU = {1: ("Yapay zekâ labda hangi aşamalarda kullanılmaya başlandı?", "Hangi aşamalarda kullanılmaya başlandı?"),
        2: ("Ne kadar yaygınlaştı? Nerede, ne kadar kullanılıyor?", "Ne kadar yaygınlaştı?"),
        3: ("Bu kadar kullanılması sonuçları nasıl etkiliyor? Neye etki ediyor?", "Sonuçları nasıl etkiliyor, neye etki ediyor?"),
        4: ("Yapay zekâ ne kadar doğru sonuç veriyor?", "Ne kadar doğru sonuç veriyor?"),
        5: ("Benim bu konudaki fikrim", "Benim fikrim")}
KOPRU = {2: "Her durakta var. Peki ne kadar yaygın?", 3: "Peki bu kadar kullanım sonuçları değiştirdi mi?",
         4: "Peki yapay zekâ ne kadar doğru?", 5: "Peki ben kendi labımda ne yapıyorum?"}
SLAYT = []


def omurga(q):
    return '<nav class="omurga">' + "".join(f'<b class="{"ak" if k == q else ("gc" if q and k < q else "")}">{k}</b>' for k in range(1, 6)) + '<span>IVF LABORATUVARINDA YAPAY ZEKÂ</span></nav>'


def kopru(q):
    return f'<div class="kopru" data-adim="9"><span>SORU {q}</span><i>{KOPRU[q]}</i><em>→</em></div>'


def sahne(q, sure, kisa, h2, govde, notu, kunye, ilk=False, etiket="", sinif="", yedek=False):
    bas = ""
    if q:
        bas = f'<header class="sr"><span class="no">SORU {q} / 5</span><span class="q">{SORU[q][0] if ilk else SORU[q][1]}</span></header>'
    elif yedek:
        bas = '<header class="sr"><span class="no ydk">YEDEK</span></header>'
    et = f'<div class="etiket">{etiket}</div>' if etiket else ""
    SLAYT.append(dict(sure=sure, kisa=kisa, yedek=yedek, q=q, h2=re.sub("<[^>]+>", "", h2), notu=notu, html=
        f'<section class="slayt {"ilk" if ilk else ""} {sinif}" data-sure="{sure}" data-baslik="{kisa}">\n{omurga(q)}\n{bas}\n<h2>{h2}</h2>\n{govde}\n{et}\n'
        f'<div class="alt"><span>{kunye}</span><span>%%NO%%</span></div>\n<aside class="not">{notu}</aside>\n</section>'))


M = lambda s: f'<mark>{s}</mark>'

# ===================== 0 BAŞLIK =====================
SLAYT.append(dict(sure=15, kisa="Başlık", yedek=False, q=0, h2="Yapay zekânın iş akışına entegrasyonu ve ileri istatistik", notu=
    "Merhaba, ben Onur Kadir Ertürk, Akdeniz Üniversitesi Hastanesi’nde embriyoloğum. Konumu beş soruyla anlatacağım; beşincisi benim fikrim. İlk soru: yapay zekâ laboratuvarda hangi aşamalara girdi?",
    html=f'''<section class="slayt kapak" data-sure="15" data-baslik="Başlık">
{omurga(0)}
<div class="kunyeust">Klinik Embriyoloji Kongresi 2027</div>
<h1>Yapay zekânın iş akışına entegrasyonu<br>ve <mark>ileri istatistik</mark></h1>
<p class="altbaslik">IVF laboratuvarında beş soru</p>
<ol class="sorular">
<li><b>1</b><i>Hangi aşamalarda kullanılmaya başlandı?</i></li>
<li><b>2</b><i>Ne kadar yaygınlaştı? Nerede, ne kadar kullanılıyor?</i></li>
<li><b>3</b><i>Sonuçları nasıl etkiliyor? Neye etki ediyor?</i></li>
<li><b>4</b><i>Ne kadar doğru sonuç veriyor?</i></li>
<li><b>5</b><i>Benim fikrim: küçük bir uygulama, KPI takibi, ileri istatistik</i></li>
</ol>
<p class="konusmaci"><b>Onur Kadir Ertürk</b> · Akdeniz Üniversitesi Hastanesi</p>
<aside class="not">%%NOT0%%</aside>
</section>'''))
SLAYT[0]["html"] = SLAYT[0]["html"].replace("%%NOT0%%", SLAYT[0]["notu"])

# ===================== 1.1 HAT =====================
DURAK = [
    dict(ad="Danışmanlık", s="ret", c=1, amac="Kişiye özel canlı doğum olasılığı", arac="Univfy (merkeze özgü model)", olg="Ticari ürün",
         kanit="Retrospektif dış doğrulama", sayi=f'{d(B1,"yao_2025_merkez")} merkez · {nd(d(B1,"yao_2025_hasta"))} hasta'),
    dict(ad="Stimülasyon", s="pro", c=1, amac="FSH başlangıç dozu ve tetik günü önerisi", arac="Alife Stim Assist, IDoser", olg="Ticari ürün",
         kanit="Prospektif + tarihsel kontrol; RKÇ yalnız protokol", sayi=f'MII {f(d(B1,"canon_2024_mii_yz"))} vs {f(d(B1,"canon_2024_mii_kontrol"))} · p = {f(d(B1,"canon_2024_p"))}'),
    dict(ad="Folikül USG", s="pro", c=1, amac="Folikülleri otomatik sayıp ölçmek", arac="FOLLISCAN (MIM Fertility)", olg="Ticari ürün",
         kanit="Retrospektif çok merkezli + prospektif kohort", sayi=f'≥ 10 mm F1 {y(d(B1,"wygocki_2026_f1_10mm"))}'),
    dict(ad="Oosit", s="pro", c=1, amac="MII oositin blastokiste gelişme şansı", arac="MAGENTA (Future Fertility)", olg="Ticari ürün",
         kanit="Prospektif gözlemsel, 3 merkez", sayi=f'AUC {f(d(B1,"cimadomo_2025_auc"))} · {nd(d(B1,"cimadomo_2025_oosit"))} donör oositi'),
    dict(ad="Sperm", s="pro", c=0, amac="ICSI için tek sperm seçimi", arac="SiD; otomatik semen analizörleri", olg="Seçim araştırma; analiz rutin (çoğu klasik görüntü işleme)",
         kanit="Prospektif kardeş oosit çalışması", sayi=f'{d(B1,"montjean_2024_mii")} MII · fark anlamsız'),
    dict(ad="ICSI", s="kav", c=0, amac="Enjeksiyonu robota ya da uzaktan kumandaya devretmek", arac="ICSIA; Conceivable sistemleri", olg="Araştırma",
         kanit="Kavram kanıtı (üretici sponsorlu)", sayi=f'{d(B1,"chavez_badiola_2026_olgu")} olgu · {d(B1,"chavez_badiola_2026_canli_dogum")} canlı doğum'),
    dict(ad="Embriyo seçimi", s="rkc", c=1, amac="Transfer sırası için puanlama ve sıralama", arac="iDAScore, CHLOE, Life Whisperer, Embryo Predict", olg="Ticari ürün (yardımcı)",
         kanit=f'RKÇ, {d(B1,"illingworth_2024_klinik")} klinik: eşdeğerlik gösterilemedi', sayi=f'{nd(d(B1,"illingworth_2024_hasta"))} hasta · {y(d(B1,"illingworth_2024_gebelik_yz"))} vs {y(d(B1,"illingworth_2024_gebelik_morf"))}'),
    dict(ad="Ploidi", s="ret", c=0, amac="Biyopsi yapmadan öploidi tahmini", arac="STORK-A, BELA", olg="Araştırma",
         kanit="Retrospektif; tanısal meta-analiz", sayi=f'AUC {f(d(B1,"xin_2024_auc"))} · {d(B1,"xin_2024_calisma")} çalışma'),
    dict(ad="Endometriyum", s="pro", c=0, amac="USG görüntüsünden FET sonrası gebelik tahmini", arac="Akademik modeller", olg="Araştırma",
         kanit="Prospektif kohort, tek merkez", sayi=f'AUC {f(d(B1,"liang_2023_auc"),3)} · n = {d(B1,"liang_2023_n")}'),
    dict(ad="Lab KPI", s="ret", c=0, amac="Kültür koşulu ve performansta erken uyarı", arac="CNN tabanlı izleme", olg="Araştırma",
         kanit="Retrospektif kavram kanıtı", sayi="sayı bildirilmemiş"),
    dict(ad="Kriyo", s="yok", c=0, amac="Tank arızasını ısınmadan önce yakalamak", arac="Sensörle izleme (YZ değil)", olg="YZ ürünü için kanıt yok",
         kanit="YZ için hakemli kanıt bulunamadı", sayi="yalnız sensör deneyi"),
    dict(ad="Hasta iletişimi", s="ret", c=0, amac="Hasta sorularını yanıtlamak, danışmanlık", arac="ChatGPT; tıbbi dil modelleri", olg="Araştırma",
         kanit="Kesitsel değerlendirme", sayi=f'{d(B1,"chervenak_2023_ifade")} ifadeden {d(B1,"chervenak_2023_hatali")}’u hatalı'),
]
HAT_ADIM = "".join(f'<i data-adim="{i+1}"></i>' for i in range(len(DURAK)))
sahne(1, 66, "1 · Aşama Hattı", f'Yapay zekâ hattın her durağında; {M("RKÇ yalnız embriyo seçiminde")}', '''
<div class="hatk" id="hatk">
  <div class="hatcizgi"></div>
  <div class="matris">
    <span class="mk" style="left:320px">ARAŞTIRMA</span><span class="mk" style="left:980px">TİCARİ ÜRÜN</span>
    <span class="ms" style="top:100px">RKÇ</span><span class="ms" style="top:214px">Prospektif gözlemsel</span><span class="ms" style="top:328px">Retrospektif / kesitsel</span><span class="ms" style="top:442px">Kavram kanıtı</span><span class="ms" style="top:556px">YZ için kanıt yok</span>
    <i style="top:157px"></i><i style="top:271px"></i><i style="top:385px"></i><i style="top:499px"></i><i class="dik"></i>
    <em>eşdeğerlik gösterilemedi</em>
  </div>
  <div id="duraklar"></div>
  <div class="adimler" aria-hidden="true">''' + HAT_ADIM + '''</div>
  <div class="hatkart" id="hatkart">
    <div><h3 id="hkAd"></h3><p id="hkAmac"></p></div>
    <div><small>ÖRNEK ARAÇ</small><p id="hkArac"></p><small style="margin-top:14px">OLGUNLUK</small><p id="hkOlg"></p></div>
    <div><small>EN GÜÇLÜ KANIT</small><p id="hkKanit"></p><p class="hksayi" id="hkSayi"></p></div>
  </div>
  <div class="hatlej">
    <span><svg viewBox="0 0 44 44"><rect x="7" y="7" width="30" height="30" fill="var(--sari)" stroke="var(--metin)" stroke-width="5"/></svg>RKÇ</span>
    <span><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="15" fill="var(--metin)"/></svg>prospektif</span>
    <span><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="13" fill="var(--zemin)" stroke="var(--metin)" stroke-width="5"/></svg>retrospektif</span>
    <span><svg viewBox="0 0 44 44"><polygon points="22,6 39,36 5,36" fill="var(--zemin)" stroke="var(--metin)" stroke-width="5"/></svg>kavram kanıtı</span>
    <span><svg viewBox="0 0 44 44"><line x1="7" x2="37" y1="22" y2="22" stroke="var(--metin)" stroke-width="6"/></svg>kanıt yok</span>
    <span class="sag"><button class="dugme" id="gHat">Hat</button><button class="dugme ikincil" id="gMat">Kanıt × olgunluk</button></span>
  </div>
</div>''',
      "Bir IVF siklusunu baştan sona bir hat gibi düşünelim. Bugün bu hattın neredeyse her durağında bir yapay zekâ uygulaması var. İlk görüşmede canlı doğum olasılığını hesaplayan modeller var. Stimülasyonda FSH dozunu ve tetik gününü öneren araçlar, ultrasonda folikülleri sayıp ölçen yazılımlar var. Laboratuvarda oositi fotoğrafından puanlayan, spermi seçen ve ICSI’yi robota yaptıran sistemler; embriyoyu sıralayan, hatta biyopsi yapmadan ploidiyi tahmin etmeye çalışan modeller var. Transfer tarafında endometriyum görüntüsünden gebelik tahmini, arka planda KPI’lar için erken uyarı, ön tarafta da hastaya yanıt veren dil modelleri var. Ama şekillere bakın; her şekil o duraktaki en güçlü kanıtın türü. Yayımlanmış randomize çalışmayı yalnız embriyo seçiminde bulduk; o da bin altmış altı hastada eşdeğerliği gösteremedi. [“Kanıt × olgunluk” düğmesi] Folikül sayımı ve oosit puanlaması ticari ürün oldu, ama kanıtları gözlemsel. ICSI robotu kavram kanıtı aşamasında. Kriyo tanklarında konuşulan şey yapay zekâ değil, sensörle izleme. Yani doğru soru “nerede kullanılıyor” değil, “hangi durakta, ne kadar kanıtla kullanılıyor”.",
      "12 durağın kaynakları yedek kaynakçada · PubMed taraması 14 Kasım 2026 (sistematik değil) · olgunluk sınıflaması bizim değerlendirmemizdir · RKÇ = randomize kontrollü çalışma", ilk=True)

# ===================== 1.2 İLKLER =====================
sahne(1, 54, "1 · İlkler", f'Otuz yılda tahminden robota; {M("kırılma 2018–2019’da")} geldi', f'''
<div class="sekilk">{zaman_cizgisi()}</div>
<p class="soz" data-adim="4">Yayın hızlı, ürün daha hızlı, <b>kanıt en yavaş.</b></p>
{kopru(2)}''',
      "Peki bu ne zaman başladı? PubMed’de bulabildiğim en erken örnek 1997’den: bir yapay sinir ağı, yalnız dört değişkenle IVF sonucunu yüzde elli dokuz doğrulukla tahmin ediyor. 2010’da kişiye özel canlı doğum tahmini geliyor. Asıl kırılma 2018’de: ASRM ve ESHRE’deki yapay zekâ bildirisi bir yıl önce ikiyken on altıya çıkıyor. 2019’da derin öğrenme embriyo görüntülerine giriyor. 2023’te otomatik ICSI ile ilk bebekler doğuyor. 2024’te ilk büyük randomize çalışma, 2025’te uzaktan kumandalı ICSI ile ilk canlı doğum geliyor. İkincil bir kaynağa göre ilk FDA izinli embriyo yazılımı da 2025 Eylül’ünde çıktı; bunu birincil kayıtta doğrulayamadım, o yüzden içi boş nokta. Kısacası yayın hızlı, ürün daha hızlı, kanıt en yavaş ilerliyor. Her durakta bir uygulama var; peki bunlar gerçekten ne kadar yaygın?",
      "Kaufmann 1997 · Banerjee 2010 · Curchoe &amp; Bormann 2019 · Khosravi 2019 · Tran 2019 · Costa-Borges 2023 · Illingworth 2024 · Mendizabal-Ruiz 2025 · *FDA: Chang 2026 (ikincil kaynak; birincil kayıt görülmedi). 1997 = PubMed’de bulduğumuz en erken örnek", sinif="son")

# ===================== 2.1 ÜLKE IZGARASI =====================
TUR = dict(E="Embriyo seçimi", O="Oosit", S="Sperm / ICSI", U="Stimülasyon / USG", P="Prognoz")


def ulke(ad, tur, liste="", sinif=""):
    nk = "".join(f'<i class="t{t}">{t}</i>' for t in tur) + "".join(f'<i class="t{t} l">{t}</i>' for t in liste)
    return f'<div class="ulke {sinif}" data-tur="{tur}{liste}"><b>{ad}</b><div class="nk">{nk}</div></div>'


sahne(2, 60, "2 · Ülke Izgarası", f'YZ yazılımları {M("30’dan fazla ülkede")}, yüzlerce klinikte duyuruluyor', f'''
<div class="yay">
  <div>
    <div class="bolgeler">
      <div class="bolge"><h4>Amerika</h4>{ulke("ABD","EUP","O")}{ulke("Meksika","S","O")}{ulke("Kolombiya","U","O")}</div>
      <div class="bolge"><h4>Avrupa</h4>{ulke("İspanya","EO")}{ulke("İngiltere","OP")}{ulke("İsviçre","P","O")}</div>
      <div class="bolge orta"><h4>&nbsp;</h4><div class="ulke tr" data-tur="ES"><b>Türkiye</b><div class="nk"><i class="tE">E</i><i class="tS">S</i></div>
        <p>Embriyo seçimi: {d(B2,"turkiye_embriyo_secimi_baslangic")}’den beri, bir merkez</p><p>YZ ile sperm seçimi: iki merkez</p></div></div>
      <div class="bolge"><h4>Asya-Pasifik</h4>{ulke("Hindistan","E","O")}{ulke("Japonya","E")}{ulke("Endonezya","E")}{ulke("Avustralya","E")}</div>
    </div>
    <div class="lej2" id="lej2">{"".join(f'<button data-t="{k}"><i class="t{k}">{k}</i>{v}</button>' for k, v in TUR.items())}<span><i class="tO l">O</i>yalnız ortak klinik listesinde</span></div>
  </div>
  <div class="beyanlar">
    <div><b>100+</b><p><strong>klinik, {d(B2,"chloe_bolge_sayisi")} bölge</strong><br>bir embriyo seçimi yazılımı · Temmuz 2026</p></div>
    <div><b>300+</b><p><strong>klinik, {d(B2,"magenta_ulke_listesi")} ülke</strong><br>bir oosit yazılımının ortak klinik sayfası</p></div>
    <div><b>{d(B2,"ag_klinik_sayisi")}</b><p><strong>klinik, {d(B2,"ag_ulke_sayisi")} ülke</strong><br>bir klinik ağı, yılda 77{NB}000’den fazla siklus · Mayıs 2026</p></div>
  </div>
</div>''',
      "Önce şunu söyleyeyim: bu sahnedeki sayıların hiçbiri hakemli bir dergiden gelmiyor; hepsi firmaların ya da kliniklerin kendi duyuruları. Yine de tablo oldukça net. Bir embriyo seçimi yazılımı yüzden fazla klinikte kullanıldığını söylüyor: Kuzey Amerika’da, Avrupa’da, Asya-Pasifik’te ve Latin Amerika’da. Bir oosit kalite yazılımının ortak klinik sayfası üç yüzden fazla klinik ve otuz iki ülke sayıyor. Bir klinik ağı da on altı ülkedeki altmış kliniğinde, yılda yetmiş yedi binden fazla siklusta embriyo seçimi ve prognoz araçlarını devreye aldığını bu yıl mayısta duyurdu. Harflere bakarsanız en yoğun alan embriyo seçimi; onu oosit ve prognoz izliyor. [S’ye tıkla] Sperm seçimi ve ICSI otomasyonu ise hâlâ birkaç merkezle sınırlı. Türkiye de bu haritada: bir merkez 2022’den beri embriyo seçiminde yapay zekâ kullandığını duyuruyor, iki merkez de farklı ürünlerle yapay zekâ destekli sperm seçimi sunuyor. Merkez adı vermiyorum; konu merkezler değil, eğilim.",
      "Firma ve klinik beyanları, hakemli değil · Fairtility basın bülteni 29 Temmuz 2026 · Future Fertility ortak klinik sayfası · Alife ortaklık bülteni 5 Mayıs 2026 (erişim 14 Kasım 2026) · ülke kareleri: firma/klinik siteleri, 10 Kasım 2026 · sayılar toplanamaz",
      ilk=True, etiket="FİRMA / KLİNİK BEYANI · hakemli değil")

# ===================== 2.2 JAPONYA HUNİSİ =====================
hn = [(d(B2, "japonya_davet_tesis"), "tesise anket gönderildi (2022–23)"), (d(B2, "japonya_yanit_tesis"), "tesis yanıt verdi"),
      (d(B2, "japonya_tlt_tesis"), "tesiste time-lapse var"), (d(B2, "japonya_tlt_ile_embriyo_degerlendirme"), "tesis embriyoyu time-lapse ile değerlendiriyor"),
      (d(B2, "japonya_tlt_artı_yz_skor_tesis"), "tesis buna YZ skoru ekliyor")]
sahne(2, 60, "2 · Ölçülen Kullanım", f'Hakemli veride ölçüm az: Japonya’da {hn[1][0]} tesisten {M(str(hn[4][0]) + "’si")} YZ skoru kullanıyor', f'''
<div class="olc">
  <div class="huni">{"".join(f'<div class="{"son" if i == 4 else ""}"><b>{v}</b><i style="width:{v/hn[0][0]*540:.0f}px"></i><span>{ad}</span></div>' for i, (v, ad) in enumerate(hn))}
    <p class="kaynakk">Japonya ulusal anketi · ham sayılar; yüzde yok, çünkü paydalar değişiyor</p></div>
  <div class="yan">
    <div data-adim="1"><b>{d(B2,"uluslararasi_anket_yanit")}</b><p>embriyolog, uluslararası anket (2023): çoğu olumlu; etik ve iş kaygısı var.<small>Yazarların bir kısmı YZ firmalarıyla bağlantılı.</small></p></div>
    <div data-adim="2"><b>{d(B2,"firma_sitesi_sayisi")} → {d(B2,"firma_risk_acikca_belirten")}</b><p>{d(B2,"firma_sitesi_sayisi")} firma sitesinin hepsi fayda anlatıyor; riski açıkça yazan yok.</p></div>
  </div>
</div>
<p class="soz" data-adim="3">Yaygın kullanım <b>kanıt değildir.</b></p>
{kopru(3)}''',
      "Peki hakemli literatür ne diyor? Kullanımı ulusal ölçekte ölçen, bulabildiğim tek çalışma Japonya’dan. Japonya Üreme Tıbbı Derneği 2022 sonunda ülkedeki 616 tesise anket gönderdi; 345 tesis yanıt verdi. Bunların 195’inde time-lapse vardı, 184’ü embriyoyu time-lapse görüntüsüyle değerlendiriyordu ve 57 tesis buna bir yapay zekâ skorunu ekliyordu. Kabaca söylersek, yanıt veren her altı tesisten biri. 2023’te yapılan uluslararası ankete 702 embriyolog katıldı; çoğu yapay zekâya olumlu bakıyor, ama etik, iş güvencesi ve hasta ilişkisi konusunda çekinceleri var. Şunu da not edeyim: bu anketin yazarlarının bir kısmı yapay zekâ firmalarıyla bağlantılı. Bir de arz tarafına bakalım: 21 firmanın web sitesi incelenmiş; hepsi fayda anlatıyor, hiçbiri riski açıkça yazmıyor. Yani kullanım hızla yayılıyor, ama yaygın kullanım kanıt değildir. Bu yüzden bir sonraki soru önemli: bu kadar kullanım sonuçları değiştirdi mi?",
      "Yamada ve ark. AJOG Glob Rep 2024 (tam metin) · Palmer ve ark. RBMO 2024 (özet) · Du &amp; Zhang Hum Reprod Open 2026 (özet). PMID’ler yedek kaynakçada", sinif="son")

# ===================== 3.1 ORMAN =====================
fa = B3["_grafik_verisi"]["freezeall_ic_grafik"]
cubuk = lambda v, sinif="": f'<i class="{sinif}" style="width:{v*3.3:.0f}px"></i><b>{y(v)}</b>'
sahne(3, 65, "3 · Canlı Doğum", f'Canlı doğumda {M("fark yok")}: en güçlü kanıt bunu söylüyor', f'''
<div class="orm">
  <div class="sekilk">{orman()}</div>
  <div class="altgrup" data-adim="1">
    <h3>Alt grup: klinik gebelik</h3>
    <div class="ag"><span>Taze transfer</span><div><em>YZ</em>{cubuk(fa["taze"]["YZ"],"v")}</div><div><em>Embriyolog</em>{cubuk(fa["taze"]["kontrol"])}</div></div>
    <div class="ag"><span>Freeze-all</span><div><em>YZ</em>{cubuk(fa["freeze_all"]["YZ"],"v")}</div><div><em>Embriyolog</em>{cubuk(fa["freeze_all"]["kontrol"])}</div></div>
    <p class="uyari">Alt grup analizi: dikkatle yorumlayın.</p>
  </div>
</div>
<p class="soz kck">Time-lapse için <b>yüksek kesinlik</b>. Derin öğrenme için <b>tek RKÇ</b>: ne küçük bir yarar ne de zarar dışlanabiliyor.</p>''',
      f"Önce asıl soruyu soralım: bu kadar yaygın kullanım daha çok bebek getirdi mi? Ekrandaki her çizgi bir karşılaştırma; ortadaki dikey çizgi “fark yok” demek. Üstteki üç satır, sekiz randomize çalışmanın hasta düzeyindeki verisini birleştiren 2026 meta-analizinden geliyor: 5{NB}642 hasta, yüksek kesinlik ve canlı doğumda klinik olarak önemli bir fark yok. Bir şeye dikkat edin: bunlar time-lapse ve morfokinetik algoritmalar, derin öğrenme değil. Derin öğrenmenin bugüne kadarki tek büyük randomize çalışması 2024’te yayımlandı: 14 klinik, 1{NB}066 hasta. Klinik gebelik yüzde 46.5’e karşı 48.2; çalışma “daha kötü değil” sonucunu bile gösteremedi, çünkü güven aralığı eşdeğerlik sınırını aşıyor. Canlı doğum yüzde 39.8’e karşı 43.5. [tıkla] Bir uyarı daha var: freeze-all hastalarında algoritmanın seçtiği embriyolarla gebelik yüzde 49.5, embriyoloğun seçtikleriyle yüzde 61.3. Bu bir alt grup bulgusu, kesin değil; ama göz ardı da edilmemeli. Kısacası seçim yazılımının, deneyimli bir embriyoloğun seçiminden daha çok bebek getirdiği gösterilmedi.",
      "Bhide ve ark. Hum Reprod Update 2026 (8 RKÇ, n=5 642; özet) · Illingworth ve ark. Nat Med 2024 (RKÇ; tam metin; Vitrolife finansmanı) · alt grup: yazarlar tartışmada “post hoc” diyor".replace("5 642", f"5{NB}642"),
      ilk=True)

# ===================== 3.2 DEĞİŞEN NE =====================
sm, sy = d(B3, "illingworth_sure_morfoloji_sn"), d(B3, "illingworth_sure_yz_sn")
fs = d(B3, "bixby_toplam_FSH_IU"); mi = d(B3, "bixby_MII"); al = d(B3, "bormann_alfa")
SMAX = 370
sahne(3, 55, "3 · Değişen Ne", f'Değişen bebek sayısı değil: {M("süre")}, tutarlılık, ilaç', f'''
<div class="degisen">
  <div class="krono" id="krono">
    <h3>Embriyo değerlendirme süresi <small>hasta başına, saniye · 3 laboratuvar</small></h3>
    <div class="kr"><span>Embriyolog</span><div class="iz"><i id="krE" style="--w:{sm["ort"]/SMAX*100:.1f}%;--t:5s"></i><u style="left:{(sm["ort"]-sm["sd"])/SMAX*100:.1f}%;width:{2*sm["sd"]/SMAX*100:.1f}%"></u></div><b id="krEs">{f(sm["ort"],1)}</b></div>
    <div class="kr"><span>Algoritma</span><div class="iz"><i id="krA" class="v" style="--w:{sy["ort"]/SMAX*100:.1f}%;--t:.52s"></i><u style="left:{(sy["ort"]-sy["sd"])/SMAX*100:.1f}%;width:{2*sy["sd"]/SMAX*100:.1f}%"></u></div><b id="krAs">{f(sy["ort"],1)}</b></div>
    <p><b>Yaklaşık 10 kat hızlı.</b> Klinik sonucu değiştirmedi. <button class="dugme ikincil kucuk" id="krT">Tekrar oynat</button></p>
  </div>
  <div class="ikili">
    <div data-adim="1"><h3>Tutarlılık</h3>
      <p>Tek model kendine tutarlı: α <b>{f(al["ag"])}</b> (embriyologlar <b>{f(al["embriyolog"])}</b>).</p>
      <p>Ama {d(B4,"thirumalaraju_kopya")} kopya model birbirine değil: W ≈ <b>{f(d(B3,"thirumalaraju_kendall_W"))}</b>.</p><em class="rz">retrospektif</em></div>
    <div data-adim="2"><h3>İlaç</h3>
      <p>Toplam FSH <b>{n(fs["kontrol"])} → {n(fs["YZ"])} IU</b> (yaklaşık %10 az); MII değişmedi ({f(mi["kontrol"])} → {f(mi["YZ"])}).</p><em class="rz">tarihsel kontrol · tek merkez · canlı doğum ölçülmedi</em></div>
  </div>
</div>''',
      "Peki değişen ne? Birincisi zaman. Aynı randomize çalışmada üç laboratuvarda kronometre tutuldu. Embriyolog bir hastanın embriyolarını ortalama 208 saniyede değerlendirdi, algoritma 21 saniyede: yaklaşık on kat fark. [tıkla] İkincisi tutarlılık. Tek bir model aynı görüntüye her seferinde aynı puanı veriyor; biz embriyologlar arasında ise belirgin bir değişkenlik var. Ama madalyonun öbür yüzü de var: aynı mimariyle eğitilmiş elli kopya model, embriyoları birbirinden farklı sıralıyor; uyum katsayısı 0.35 civarında. Yani “yapay zekâ tutarlıdır” sözü yalnızca tek bir model için doğru. [tıkla] Üçüncüsü ilaç. Gerçek dünya verisinde, yapay zekâ destekli doz seçimiyle toplam FSH yaklaşık yüzde on daha az kullanıldı ve MII sayısı değişmedi. Ama bu tek merkezli, tarihsel kontrollü bir çalışma ve canlı doğum hiç ölçülmedi.",
      "Illingworth 2024 Nat Med (süre: RKÇ alt çalışması, ort. ± SS çubukta) · Bormann 2020 Fertil Steril · Thirumalaraju 2025 Fertil Steril · Bixby &amp; Miller 2025 F S Rep (292’ye 292 hasta)")

# ===================== 3.3 PANO =====================
PANO = [("Klinik", [("Canlı doğum, gebelik, düşük", "= fark yok", "esit", "d", "IPD meta-analizi · RKÇ"), ("Perinatal güvenlik", "= fark yok", "esit", "y", "RKÇ takibi"), ("Gebeliğe kadar süre", "ölçülmedi", "yok", "b", "RKÇ verisi yok")]),
        ("Lab · ilaç · maliyet", [("Değerlendirme süresi", "↓ yaklaşık 10 kat", "var", "d", "RKÇ alt çalışması"), ("Tutarlılık", "karışık", "isaret", "b", "retrospektif"), ("FSH miktarı", "↓ yaklaşık %10", "isaret", "b", "tarihsel kontrol"), ("Maliyet", "↑ artıyor", "olumsuz", "y", "ekonomik analiz")]),
        ("Hasta · meslek", [("Hasta güveni", f'%{d(B3,"cromack_guven_yuzde")} güveniyor', "isaret", "b", f'anket, {d(B3,"cromack_n")} hasta'), ("Beceri kaybı, sorumluluk", "ölçülmedi", "yok", "b", "etik yazın")])]
pano = "".join(f'<div class="pg" {"" if gi == 0 else f"data-adim=\"{gi}\""}><h4>{ad}</h4><div>' + "".join(f'<div class="ps"><span>{c}</span><b class="e-{s}">{e}</b><em><i class="g{g}"></i>{k}</em></div>' for c, e, s, g, k in sat) + '</div></div>' for gi, (ad, sat) in enumerate(PANO))
sahne(3, 60, "3 · Etki Panosu", f'Neye etki ediyor? Kanıtla gösterilen tek kazanç {M("hız")}', f'''
<div class="pano">{pano}</div>
<div class="plej"><span><b class="e-var">kanıtla gösterildi</b></span><span><b class="e-esit">fark yok</b></span><span><b class="e-isaret">işaret var, kontrolsüz</b></span><span><b class="e-olumsuz">olumsuz</b></span><span><b class="e-yok">ölçülmedi</b></span><span class="g">kanıt gücü: <i class="gd"></i>güçlü <i class="gy"></i>orta <i class="gb"></i>zayıf</span></div>
<p class="soz" data-adim="3">Daha çok bebek getirdiği gösterilmedi; değişen <b>hız ve iş akışı.</b></p>
{kopru(4)}''',
      "Şimdi hepsini tek panoda toplayalım. Sarı işaretli koyu kutu “kanıtla gösterilmiş etki”, gri “fark yok”, mavi çerçeve “işaret var ama kontrolsüz”, kesik çerçeve ise “hiç ölçülmemiş” demek. Klinik sonuçlarda tablo gri: canlı doğum, gebelik, düşük ve perinatal güvenlikte fark yok. Gebeliğe kadar geçen süre ise randomize çalışmalarda hiç ölçülmemiş. [tıkla] Laboratuvarda tek koyu satır var: süre kısalıyor. Maliyette elimizdeki tek ekonomik analiz, time-lapse ve seçim algoritmasının maliyeti artırdığını ve muhtemelen maliyet-etkin olmadığını söylüyor. [tıkla] Hastalar tarafında, iki yüz hastalık bir ankette yalnızca yüzde 46’sı yapay zekâ destekli tedaviye güveniyor ve anlaşmazlık olursa hekimi tercih ediyor. Etik tarafta beceri kaybı ve sorumluluk tanımlanmış ama ölçülmemiş riskler. Özetle: yapay zekânın daha çok bebek getirdiği gösterilmedi; değiştirdiği şey hız ve iş akışı. Peki bu modeller ne kadar doğru? Bu da bir sonraki soru.",
      "Bhide 2026 · Illingworth 2024 · Kieslinger 2026 (perinatal; maliyet-etkinlik: time-lapse + 3. gün algoritması) · Bixby &amp; Miller 2025 · Cromack 2025 JARG (tek merkez, ABD) · Koplin 2025. Çoğu özet düzeyinde okundu",
      sinif="son")

# ===================== 4.1 AUC CETVELİ =====================
sahne(4, 75, "4 · AUC Cetveli", f'Görmede güçlü, kehanette orta: AUC çoğunlukla {M(f(d(B4,"berntsen_klinik_alt"),1) + "–" + f(d(B4,"mina_auc"),1))}', f'''
<div class="goz"><span class="bant">GÖZ İŞİ<small>uzman etiketine uyum</small></span>
  <p><i></i>Folikül ölçümü (≥ 10 mm): <b>F1 {y(d(B4,"follis_f1_10mm"))}</b></p>
  <p><i></i>Sperm morfolojisi: çoğu çalışmada <b>&gt; %90 doğruluk</b></p></div>
<div class="keh"><span class="bant sari">KEHANET İŞİ<small>sonuca göre AUC</small></span><div class="sekilk">{auc_cetveli()}</div></div>
<p class="acik">AUC {f(d(B4,"berntsen_kid"))} = rastgele bir tutan ve bir tutmayan embriyodan, tutanı %67 olasılıkla üste koyar.</p>''',
      "Doğruluk sorusuna tek bir sayıyla cevap veremiyoruz, çünkü yapay zekâ labda iki ayrı iş yapıyor. Birincisi göz işi: bizim gördüğümüzü ölçmek, saymak, sınıflamak. Folikül ölçümünde on milimetrenin üstündeki foliküllerde F1 skoru yüzde doksan üç. Sperm morfolojisinde çalışmaların çoğu yüzde doksanın üstünde doğruluk bildiriyor. Burada referans, uzmanın kendi etiketi. İkinci iş kehanet: bu embriyo tutacak mı, öploid mi, bu hasta bebek sahibi olacak mı? Burada referans biyolojinin kendisi ve sayılar belirgin biçimde düşüyor. Cetveli şöyle okuyun: 0.5 yazı-tura, 1 kusursuz. AUC, yani eğri altında kalan alan, bir ayırt edicilik ölçüsü; 0.67 şu demek: transfer edilmiş embriyolardan rastgele bir tutan ve bir tutmayan seçersek, model tutana yüzde altmış yedi olasılıkla daha yüksek puan veriyor. Transfer edilen embriyolarda kalp atımı tahmini 0.60 ile 0.76 arasında. Ploidi tahmini başka merkezlerde 0.70 civarında; meta-analiz 0.80 diyor, ama çalışmaların çoğu kendi verisinde test edilmiş. Oositten öploidi tahmini tek başına 0.54, yani yazı-turaya çok yakın. Tedavi öncesi canlı doğum tahmini de, klasik modelle de yapay zekâyla da 0.67 ile 0.75 arasında kalıyor.",
      "Wygocki 2026 · Varzaneh 2026 · Berntsen 2022 · Ueno 2021 · Mina 2025 · Thirumalaraju 2025 · Barnes 2023 · Bamford 2023 · Ma 2024 · Xin 2024 · Setti 2026 · Cimadomo 2025 · Cai 2024 · Ratna 2023. Çoğunda üretici firma yazarı var; PMID’ler yedek kaynakçada · AUC = eğri altında kalan alan, ayırt edicilik ölçüsü",
      ilk=True, sinif="s41")

# ===================== 4.2 AYNI MODEL İKİ SAYI =====================
g4 = lambda k: d(B4, k)
DURUM = [
    dict(et="Tüm embriyolar · atılanlar dahil", sayi=f(g4("berntsen_tum")), ac="Durmuş embriyoyu ayırmak kolay."),
    dict(et="Yalnız transfer edilenler", sayi=f(g4("berntsen_kid")), ac="Zor olan, iyi blastokistler arasında seçmek."),
    dict(et=f'Yeni merkez · {len(g4("berntsen_klinik_listesi"))} merkez tek tek dışarıda bırakıldı', sayi=f'{f(g4("berntsen_klinik_alt"))}–{f(g4("berntsen_klinik_ust"))}', ac="Aynı model, merkeze göre değişiyor.", ek=merkez_seridi()),
    dict(et="Embriyoyu kim seçti? · simülasyon", sayi=f'{f(g4("kragh_sim_model1"))} / {f(g4("kragh_sim_model2"))}', ac=f'Tüm havuzda eşit iki model ({f(g4("kragh_sim_genel"))}). Seçimi yapan, kendi seçtikleri arasında haksız biçimde kötü görünür.'),
    dict(et="Hastayı ayır", sayi=f'{f(g4("demo_gbm_rastgele"),3)} → {f(g4("demo_gbm_hasta"),3)}', ac="Aynı hastanın embriyoları hem eğitimde hem testte olunca başarı olduğundan iyi görünür.", sentetik=1),
]
dg = "".join(f'<button class="dr4{" sec" if i == 0 else ""}" data-i="{i}"><span>{dd["et"].split(" · ")[0]}{" <u>SENTETİK</u>" if dd.get("sentetik") else ""}</span><b>{dd["sayi"]}</b></button>' for i, dd in enumerate(DURUM))
sahne(4, 60, "4 · Aynı Model, İki Sayı", f'Aynı model, iki sayı: parlaklığı {M("payda ve doğrulama")} belirliyor', f'''
<div class="ikisayi">
  <div class="bulutk">{nokta_bulutu()}<p class="kaynakk">Her nokta ≈ 100 embriyo · test seti {n(g4("berntsen_test_embriyo"))} · <span class="kidl">sarı: transfer edilen {n(g4("berntsen_test_kid"))}</span></p></div>
  <div class="buyuk"><small id="d4et">{DURUM[0]["et"]}</small><div class="rk" id="d4sayi">{DURUM[0]["sayi"]}</div><div id="d4ek"></div><p id="d4ac">{DURUM[0]["ac"]}</p></div>
  <div class="dugmeler" id="d4">{dg}</div>
</div>
<p class="soz">Parlaklık çoğu zaman <b>paydada, seçimde ve doğrulama biçiminde.</b></p>''',
      "Peki 0.95 gibi parlak sayılar nereden geliyor? Aynı model, aynı makale: on sekiz merkez, yüz on beş bin embriyo. Bütün embriyolar arasında AUC 0.95. Ama bu havuzda durmuş ve atılmış embriyolar da var; onları ayırmak bizim için de kolay. [düğme] Bizim asıl sorumuz, transfere aday iyi blastokistler arasında hangisinin tutacağı. Orada AUC 0.67. [düğme] Merkez değişince bu sayı 0.60 ile 0.75 arasında oynuyor. [düğme] Retrospektif veride bir tuzak daha var: transfer edilecek embriyoyu biz seçtiğimiz için, embriyoloğun skoru kendi seçtiği embriyolar arasında haksız biçimde kötü görünüyor. Bir simülasyonda eşit güçteki iki model 0.59’a karşı 0.74 çıkıyor. [düğme] Son düğme kendi sentetik verimden: aynı hastanın embriyoları hem eğitimde hem testte olunca AUC 0.686; hastayı ayırınca 0.646. Kısacası parlaklık çoğu zaman paydada, seçimde ve doğrulama biçiminde.",
      "Berntsen ve ark. PLoS One 2022 (tam metin; yazarlar Vitrolife) · Kragh &amp; Karstoft JARG 2021 (simülasyon) · “Hastayı ayır”: kendi sentetik demom, gerçek hasta verisi değildir")

# ===================== 4.3 BEŞ KONTROL =====================
KONTROL = [("Başka merkezde test edildi mi?", f'Oosit sayısı tahmini: <b>{g4("wilkinson_model")} modelin {g4("wilkinson_dis")}’ı</b> dış doğrulanmış'),
           ("Prospektif mi, randomize mi?", f'Time-lapse derin öğrenme: <b>{g4("berman_calisma")} çalışmanın {g4("berman_calisma")}’si</b> retrospektif'),
           ("Kalibre mi? %40 dediği %40 mı?", f'Oosit skoru tek başına: eğim <b>{f(g4("magenta_egim_tek"),3)}</b> · ideal 1'),
           ("Benim labımda doğrulandı mı?", f'Aynı model, {len(g4("berntsen_klinik_listesi"))} merkezde <b>{f(g4("berntsen_klinik_alt"))}–{f(g4("berntsen_klinik_ust"))}</b>'),
           ("Zamanla izleniyor mu?", f'{g4("thirumalaraju_kopya")} kopya model: sıralama uyumu <b>W ≈ {f(g4("thirumalaraju_w"))}</b>')]
sahne(4, 45, "4 · Beş Kontrol", f'Bir sayıya güvenmeden önce {M("beş kontrol")}', f'''
<div class="kontrol">{"".join(f'<div><b>{i}</b><h3>{s}</h3><p data-adim="{i}">{k}</p></div>' for i, (s, k) in enumerate(KONTROL, 1))}</div>
<p class="soz kck" data-adim="6">Basit model ≥ derin öğrenme: ploidide lojistik regresyon <b>{f(g4("bamford_lr"))}</b>, derin öğrenme <b>{f(g4("bamford_derin"))}</b>.</p>
{kopru(5)}''',
      "O yüzden bir firma ya da makale bana bir sayı gösterdiğinde beş şeyi kontrol ediyorum. Bir: başka merkezde test edildi mi? Oosit sayısını tahmin eden dokuz modelin hiçbiri dış doğrulanmamış. İki: prospektif mi, randomize mi? Time-lapse derin öğrenme derlemesindeki yirmi iki çalışmanın hepsi retrospektif. Üç: kalibre mi, yani yüzde kırk dediğinde gerçekten yüzde kırk mı? Bir oosit skoru tek başına kullanıldığında kalibrasyon eğimi 0.26; ideal değer 1. Dört: benim labımda doğrulandı mı? Beş: zamanla izleniyor mu? Aynı mimariyle eğitilen elli kopya model embriyoları farklı sıralıyor. Bir de not: basit lojistik regresyon, derin öğrenmeyi geçebiliyor. Buraya kadar başkalarının ürettiği yapay zekâyı konuştuk. Peki ben kendi laboratuvarımda ne yapıyorum?",
      "Wilkinson 2025 RBMO · Berman 2023 AJOG · Setti 2026 F S Sci · Berntsen 2022 PLoS One · Thirumalaraju 2025 Fertil Steril · Bamford 2023 Hum Reprod. Hepsi özet düzeyinde (Berntsen tam metin)", sinif="son")

# ===================== 5.1 ELLE YAPILAN İŞ =====================
ISLER = [("Fotoğraf", "tek dokunuşla doğru oosite ve aşamaya", "v3.8"), ("Cryo haritası", "kayıttan türer; boş yer önerilir", "v3.0 · v6.190"),
         ("Resmî formlar", "ve Bakanlık tablosu kayıttan basılır", "v6.37 · v6.201"), ("İşlemi yapan", "seçilir; her değişiklik izlenir", "v6.99 · v0.2"),
         ("Oranlar", "her ay kendiliğinden hesaplanır", "v6.123"), ("Yedek", "yoksa program uyarır", "v1.2")]
sahne(5, 50, "5 · Elle Yapılan İş", f'Elle yapılan altı iş, {M("kayıt girilirken")} kendiliğinden oluyor', f'''
<div class="yolc"><span>Kâğıt</span><em>→</em><span>Excel / Access</span><em>→</em><span class="sim">Kendi programım</span><em>→</em><span>Yapay zekâ ile derin istatistik</span></div>
<div class="defter">{"".join(f'<div {"" if i < 2 else f"data-adim=\"{i//2}\""}><b>{a}</b><p>{b}</p><code>{c}</code></div>' for i, (a, b, c) in enumerate(ISLER))}</div>
<p class="acik">Patient Data Center: kayıt ve betimsel istatistik aracı. İçinde makine öğrenmesi modeli yok.</p>''',
      "Önceki dört soruda başkalarının ürettiği yapay zekâyı konuştuk. Şimdi kendi laboratuvarıma dönüyorum. Kayıtlarımız kâğıttan Excel’e ve Access’e, oradan da kendi programıma geçti. Programın amacı tek: elle yaptığım işleri kayıt anına taşımak. Mikroskoptan aldığım kareyi artık klasörde arayıp eşlemiyorum; ekranda “bu kareyi şu oosite ekle” diyorum. Cryo haritasını ayrıca güncellemiyorum; harita vitrifikasyon kaydından türüyor, dondururken program bana boş yer öneriyor. [tıkla] Doldurmak zorunda olduğum resmî formlar ve Bakanlığın aylık tablosu kayıttan basılıyor. Kimin hangi işlemi yaptığı ve hangi alanın kim tarafından değiştirildiği kendiliğinden kayda geçiyor. [tıkla] Oranlar her ay kendiliğinden hesaplanıyor, yedek alınmamışsa program uyarıyor. Ne kadar zaman kazandırdığını ayrıca ölçmedim; o yüzden size bir dakika sayısı vermeyeceğim. Şunu da açıkça söyleyeyim: bu programın içinde yapay zekâ modeli yok.",
      "Patient Data Center README sürüm notları (v0.2 – v6.201) · ekranda gerçek hasta verisi yok", ilk=True)

# ===================== 5.2 GELİŞTİRME DÖNGÜSÜ =====================
sahne(5, 45, "5 · Geliştirme Döngüsü", f'İhtiyacı embriyolog söyledi, yapay zekâ kodladı, {M("embriyolog doğruladı")}', f'''
<div class="dongu"><span class="ben">İhtiyaç</span><em>→</em><span>YZ kodlar</span><em>→</em><span>Test</span><em>→</em><span class="ben">Embriyolog doğrular</span><em>→</em><span>Sürüm notu</span><em class="don">↺</em>
  <small><i class="ben"></i>embriyolog <i></i>yapay zekâ</small></div>
<div class="gel">
  <div>
    <div class="uclu"><div><b>{DEPO["commit"]}</b><span>commit</span></div><div><b>{DEPO["gun"]}</b><span>gün</span></div><div><b>{DEPO["surum_notu"]}</b><span>sürüm notu</span></div></div>
    {git_svg()}
  </div>
  <div>
    <blockquote>“Oosit sayısı klinik bir sayıdır.”<cite>v6.19 · hayalet oosit hatasından doğan kural</cite></blockquote>
    <ul data-adim="1"><li>MII dışı yumurtada enjeksiyon “yapılmadı” <code>v1.4</code></li><li>Taşıyıcı etiketi benzersiz <code>v3.0</code></li><li>Dejenere yumurta kilitli <code>v6.139</code></li></ul>
  </div>
</div>''',
      "Programı ben yazmadım; yapay zekâ yazdı. Ben ne istediğimi embriyolog diliyle söyledim, yapay zekâ kodladı ve kendi testini yaptı, ben ekranda kendi klinik bilgimle doğruladım; her değişiklik, neden yapıldığıyla birlikte sürüm notuna yazıldı. Git kaydına göre 32 günde 341 commit, toplamda 296 sürüm notu var. Kuralların çoğu benim bir cümlemden doğdu. Bir gün aynı kare iki kez kaydedilince fotoğrafsız, hayalet bir oosit oluştu; kural şu oldu: oosit sayısı klinik bir sayıdır, şişemez. [tıkla] MII olmayan yumurtada enjeksiyon varsayılan olarak “yapılmadı” gelir, taşıyıcı etiketi iki kez kullanılamaz, dejenere yumurtaya embriyo kaydı girilemez. Sorunu en iyi, o işi yıllarca yapan bilir.",
      f'Patient Data Center git kaydı, {d0.day} Eylül – {d1.day} Ekim 2026 (14 Kasım 2026’da sayıldı) · README v1.4, v3.0, v6.19, v6.139 · geliştirme aracı: Claude Code')

# ===================== 5.3 KPI TABLOSU =====================
vi, vb, vm = d(B5, "vienna_icsi_fert"), d(B5, "vienna_blast"), d(B5, "vienna_mii")
sahne(5, 45, "5 · KPI Takibi", f'Program {d(B5,"pdc_oran_sayisi")} oranı her ay hesaplıyor; Vienna’yla eşleşmesi {M("kısmi")}', f'''
<div class="kpi">
  <div class="kb"><span>Programın oranı</span><span>Vienna 2017 karşılığı</span><span>Eşleşme</span></div>
  <div><b>M2</b><i>MII / yumurta</i><p>Referans gösterge: %{vm["alt_yuzde"]}–{vm["ust_yuzde"]}</p><em>lab KPI’sı değil</em></div>
  <div><b>Fertilizasyon</b><i>2PN / ICSI</i><p>KPI: ≥ %{vi["competence_min_yuzde"]} yeterlik · ≥ %{vi["benchmark_min_yuzde"]} hedef</p><em>tanım birebir değil</em></div>
  <div><b>Blastokist</b><i>blastokist / 2PN</i><p>KPI ({vb["gun"]}. gün): ≥ %{vb["competency_min_yuzde"]} yeterlik · ≥ %{vb["benchmark_min_yuzde"]} hedef</p><em>tanım birebir değil*</em></div>
  <div><b>Beta hCG (+) · klinik gebelik</b><i>/ transfer</i><p>—</p><em>lab göstergesi sayılmıyor</em></div>
</div>
<p style="font-size:24px;color:var(--soluk);margin-top:14px;max-width:none">* Blastokist oranının payı: blastokist ekranında değerlendirilen her embriyo (morula, kavitasyon ve arrest dahil).</p>
<div class="kpialt"><p>Vienna: göstergeler <b>“ideally on a monthly basis”</b> izlenir.</p><p data-adim="1">Oranlar saklanmaz, kayıtlardan yeniden hesaplanır. Payda sıfırsa “%0” değil <b>“—”</b>.</p></div>''',
      "KPI’yı nasıl takip ediyorum? Program bugün beş oranı hesaplıyor: M2, fertilizasyon, blastokist, beta hCG pozitifliği ve transfer başına klinik gebelik. Bunlar bir sayaçta tutulmuyor; ekran her açıldığında kayıtlardan yeniden hesaplanıyor, geçmiş bir kayıt düzeltilince o ayın oranı da düzeliyor. Ay ve yıl seçip bakıyorum, payı ve paydası yanında yazıyor. Vienna konsensüsü göstergelerin ideal olarak aylık izlenmesini öneriyor. Ama dürüst olayım, eşleşme kısmi: M2 oranı Vienna’da laboratuvar KPI’sı değil, stimülasyonu yansıtan bir referans gösterge; fertilizasyon ve blastokist tanımlarım Vienna’nınkiyle birebir aynı değil; örneğin blastokist oranının payına blastokist ekranında değerlendirilen her embriyo giriyor, morula ve arrest dahil; klinik gebelik ise laboratuvar göstergesi sayılmıyor. Yani bugün yaptığım şey Vienna KPI’larını hesaplamak değil, kendi oranlarımı düzenli izlemek.",
      "ESHRE SIG Embryology &amp; Alpha Scientists, Vienna konsensüsü: RBMO 2017;35:494–510 · Hum Reprod Open 2017 (tam metin) · Patient Data Center README v6.38, v6.123, v6.241 ve istatistik kodu")

# ===================== 5.4 CUSUM + FUNNEL =====================
mc, fu = KP["monte_carlo"], KP["funnel"]; E_, F_ = fu["embriyologlar"]["E"], fu["embriyologlar"]["F"]
sahne(5, 55, "5 · İleri İstatistik", f'{M("CUSUM")} düşüşü aylık ortalamadan önce yakalıyor; {M("yaş ayarı")} haksızlığı düzeltiyor', f'''
<div class="ileri">
  <div>
    <h3>Erken uyarı <small>{mc["tekrar"]} simülasyon · oran {yo(KP["gercek_parametreler"]["taban_oran"],0)} → {yo(KP["gercek_parametreler"]["kayma_sonrasi_oran"],0)}</small></h3>
    {cusum_sekli()}
    <div class="kars"><div><b>{yo(mc["cusum"]["yakalama_orani"])}</b><span><strong>CUSUM</strong> yakaladı<br>medyan {f(mc["cusum"]["medyan_gecikme_hafta"],0)} hafta</span></div>
      <div class="ik"><b>{yo(mc["shewhart"]["yakalama_orani"])}</b><span><strong>aylık ortalama</strong><br>medyan {f(mc["shewhart"]["medyan_gecikme_hafta"],0)} hafta</span></div></div>
    <p class="kaynakk">Bedeli: yanlış alarm {yo(mc["cusum_yanlis_alarm_orani"])} (aylık ortalamada {yo(mc["shewhart_yanlis_alarm_orani"])})</p>
  </div>
  <div>
    <h3>Adil karşılaştırma <span class="sag"><button class="dugme" id="fuHam">Ham</button><button class="dugme ikincil" id="fuAy">Yaşa göre ayarlı</button></span></h3>
    {funnel()}
    <p class="fuyazi"><b>F</b> (yaş ort. {f(F_["yas_ort"],1)}): ham {yo(F_["ham"])} → ayarlı <b>{yo(F_["ayarli"])}</b>. <b>E</b> iki grafikte de %{fu["sinirlar_yuzde"][1]} sınırının dışında.</p>
  </div>
</div>
<p class="acik">Bu iki analiz programda yok; programın tuttuğu türden veriyle yapılabilir. A–F sentetik birimlerdir.</p>''',
      "Bu ekranlar programda yok; programın tuttuğu türden veriyle neler yapılabileceğini sentetik veriyle gösteriyorum. Soldaki grafikte bir oran yetmişinci haftada yüzde 75’ten yüzde 69’a düşüyor; bir lot değişikliği gibi düşünün. Bunu 500 kez simüle ettim. Haftalık CUSUM düşüşü yüzde 96.6 oranında, ortanca 10 haftada yakaladı; aylık ortalamaya bakan klasik grafik yüzde 67.2 oranında ve 14 haftada. Bedeli biraz daha fazla yanlış alarm: yüzde 4’e karşı 1.8. Sağda adil karşılaştırma var. [“Yaşa göre ayarlı” düğmesi] F’nin hastaları daha yaşlı; ham oranı yüzde 68.9 ile düşük görünüyor, yaşa göre ayarlayınca yüzde 75.9’a çıkıyor. Gerçekten düşük olan E ise iki grafikte de sınırın dışında. Yani doğru soru sorulursa, aynı kayıt hem erken uyarı verir hem de haksız karşılaştırmayı düzeltir.",
      f'Sentetik demo, seed {KP["seed"]}: haftalık ≈ {KP["gercek_parametreler"]["haftalik_ort_vaka"]} olgu, {KP["gercek_parametreler"]["kayma_haftasi"]}. haftada düşüş, izlem {mc["izleme_suresi_hafta"]} hafta · funnel: genel orana göre %95 ve %{fu["sinirlar_yuzde"][1]} sınırları · yöntem: Bormann 2021 JARG, Zacà 2022 JARG',
      etiket="SENTETİK VERİ · klinik bulgu değildir", sinif="s54")

# ===================== 5.5 FİKRİM =====================
ia = GR["ince_ayar"]
sahne(5, 45, "5 · Benim fikrim", f'{M("Ham değil, kişisel")} yapay zekâ; embriyolog onun kalite kontrolcüsü', f'''
<div class="fikir">
  <ol>
    <li><b>1</b><p>Yapay zekâ yaygın; ama daha çok bebek getirdiği gösterilmedi, doğruluğu orta.</p></li>
    <li data-adim="1"><b>2</b><p>Ben onu ham değil, kişisel kullanıyorum: ihtiyacı ben söylüyorum, o kodluyor, ben doğruluyorum.</p></li>
    <li data-adim="2"><b>3</b><p>Embriyolog işsiz kalmaz; yapay zekânın kalite kontrolcüsü olur.</p></li>
  </ol>
  <figure data-adim="3"><span class="mini">SENTETİK GÖRÜNTÜ · klinik bulgu değildir</span>{ince_ayar()}
    <figcaption>Hazır görsel model başka labda <b>{f(ia["auc"][0])}</b>; {ia["yerel_n"][1]} yerel etiketle <b>{f(ia["auc"][1])}</b>.</figcaption></figure>
</div>''',
      "Benim fikrim şu. Yapay zekâ laboratuvara girdi ve yayıldı; ama gördüğümüz yayınlarda hazır bir modelin daha çok bebek getirdiği gösterilmedi ve doğruluğu orta düzeyde kaldı. [tıkla] Bu yüzden ben onu ham değil, kişisel kullanıyorum: ihtiyacı ben söylüyorum, yapay zekâ kodluyor, ben doğruluyorum. [tıkla] Embriyolog işsiz kalmayacak; yapay zekâyı etiketleyen, doğrulayan, izleyen ve son kararı veren kalite kontrolcüsü olacak. [tıkla] Görsel modeller için de aynısı geçerli: sentetik denememde, başka bir labda yazı-tura düzeyine düşen hazır model, embriyoloğun etiketlediği 25 görüntüyle toparlandı. Beş soruyu beş kısa cevapla toparlayayım.",
      f'Sentetik görüntü demosu, seed {GR["seed"]}, {ia["tekrar"]} tekrar ortalaması (AUC) · dayanak: Illingworth 2024, Bhide 2026, Berntsen 2022')

# ===================== KAPANIŞ =====================
CEVAP = ["Hattın her durağında; RKÇ yalnız embriyo seçiminde.", "30’dan fazla ülkede duyuruluyor; ölçen hakemli veri az.", "Daha çok bebek gösterilmedi; değişen hız ve iş akışı.",
         f'Görmede güçlü, kehanette orta: AUC çoğunlukla {f(d(B4,"berntsen_klinik_alt"),1)}–{f(d(B4,"mina_auc"),1)}.', "Ham değil, kişisel: embriyolog söyler, doğrular, karar verir."]
SLAYT.append(dict(sure=15, kisa="Kapanış", yedek=False, q=0, h2="Beş soru, beş kısa cevap", notu=
    "Beş sorunun kısa cevapları ekranda. Tek cümleyle: yapay zekâ laboratuvarda, ama kanıtını ve doğruluğunu bizim denetlememiz gerekiyor; ben de onu kendi işime göre, kendi denetimimle kullanıyorum. Dinlediğiniz için teşekkür ederim; sorularınızı memnuniyetle alırım.",
    html=f'''<section class="slayt kapak kapanis" data-sure="15" data-baslik="Kapanış">
{omurga(6)}
<div class="kunyeust">Beş soru, beş kısa cevap</div>
<ol class="sorular cevap">{"".join(f'<li><b>{i}</b><i>{SORU[i][1]}</i><p>{c}</p></li>' for i, c in enumerate(CEVAP, 1))}</ol>
<p class="konusmaci"><mark>Teşekkür ederim.</mark> &nbsp; <b>Onur Kadir Ertürk</b> · Akdeniz Üniversitesi Hastanesi</p>
<div class="alt"><span>Sunumdaki bütün demolar sentetiktir; gerçek hasta verisi kullanılmadı. Kaynaklar ve yöntem yedek slaytlarda.</span><span>%%NO%%</span></div>
<aside class="not">%%NOTK%%</aside>
</section>'''))
SLAYT[-1]["html"] = SLAYT[-1]["html"].replace("%%NOTK%%", SLAYT[-1]["notu"])

# ===================== YEDEKLER =====================
sahne(0, 0, "Yedek · Yöntem ve Sınırlar", "Yöntem: her sayı nereden geliyor, ne kadar okundu?", f'''
<div class="yontem">
  <div><b>Literatür</b><p>PubMed kaydında görülüp aynen aktarıldı (14 Kasım 2026). Künyede okuma derinliği yazıyor: tam metin ya da yalnız özet. Tarama sistematik değil.</p></div>
  <div><b>Yaygınlık</b><p>Firma ve klinik beyanları; hakemli değil, toplanamaz. Merkez adı verilmedi.</p></div>
  <div><b>İkincil kaynak</b><p>FDA 510(k) bilgisi tek bir derlemeden; birincil kayıt görülmedi.</p></div>
  <div><b>Demolar</b><p>Hepsi sentetik veri ve sentetik görüntü; klinik bulgu değildir. Gerçek hasta verisi kullanılmadı.</p></div>
  <div><b>Program</b><p>Patient Data Center kayıt ve betimsel istatistik aracıdır; içinde makine öğrenmesi modeli yok. Claude Code ile yazıldı.</p></div>
  <div><b>Beyan</b><p>Çıkar çatışması: [beyan]. Sunumun analiz kodu ve taslağı yapay zekâ yardımıyla hazırlandı.</p></div>
</div>''', "Soru gelirse: sayıların kaynağı, okuma derinliği ve sentetik veri kararı. Çıkar çatışması beyanını sunumdan önce doldur.", "Yedek slayt", yedek=True)
sahne(0, 0, "Yedek · Kaynakça 1", "Kaynakça (1): aşamalar ve yaygınlık", f'<div class="kaynakca">{kaynakca(0)}</div>',
      "Kaynakça, soru 1 ve 2.", "Künyeler kısaltılmıştır; PMID’ler bölüm dosyalarındaki doğrulama tablolarından alındı", yedek=True)
sahne(0, 0, "Yedek · Kaynakça 2", "Kaynakça (2): etki, doğruluk, KPI", f'<div class="kaynakca">{kaynakca(1)}</div>',
      "Kaynakça, soru 3, 4 ve 5.", "Künyeler kısaltılmıştır; PMID’ler bölüm dosyalarındaki doğrulama tablolarından alındı", yedek=True)
sahne(0, 0, "Yedek · Beklenen Sorular", "Beklenen sorular", f'''
<div class="sss">
  <div><b>“AUC {f(g4("berntsen_kid"))} iyi mi, kötü mü?”</b><p>Gardner aynı tür veride {f(g4("ueno_genc_gardner"))} dolayında. Fark yalnız 35 yaş altında anlamlı: {f(g4("ueno_genc_idascore"))}’ye karşı {f(g4("ueno_genc_gardner"))}.</p></div>
  <div><b>“Yüksek AUC, yüksek gebelik oranı mı demek?”</b><p>Hayır. AUC bir havuz içindeki sıralamayı ölçer, implantasyon oranını değil.</p></div>
  <div><b>“Freeze-all bulgusu kesin mi?”</b><p>Hayır; alt grup analizi. Yazarlar şans eseri olabileceğini de yazıyor.</p></div>
  <div><b>“Programınız yapay zekâ ile karar veriyor mu?”</b><p>Hayır. İçinde model yok; kayıt tutuyor ve oran hesaplıyor.</p></div>
  <div><b>“CUSUM ve funnel programda var mı?”</b><p>Hayır. Sentetik veriyle yöntem gösterimi.</p></div>
  <div><b>“Gerçek hasta verisi kullandınız mı?”</b><p>Hayır. Bütün demolar sentetik.</p></div>
</div>''', "Soru-cevap için hazır kısa cevaplar.", "Ueno 2021 Fertil Steril (özet) · Berntsen 2022 PLoS One (tam metin) · Illingworth 2024 Nat Med (tam metin)", yedek=True)
sahne(0, 0, "Yedek · Oran Ölçeği", "Oran ölçeğinde de tablo aynı: güven aralıkları 1’i içeriyor", f'<div class="sekilk" style="margin-top:20px">{orman_oran()}</div>',
      "Ana grafikte mutlak risk farkı vardı; burada aynı çalışmaların oran ölçeğindeki değerleri var. aOR ve RR aynı eksende, yalnız karşılaştırma için.",
      "Bhide 2026 Hum Reprod Update (aOR, özet) · Illingworth 2024 Nat Med (RR, tam metin) · Yaghi 2026 Eur J Obstet Gynecol (RR, yalnız 2 çalışma havuzlandı; özet)", yedek=True)
sahne(0, 0, "Yedek · Sızıntı", "Hastayı ayırınca esnek modelin başarısı düşüyor, basit model yerinde kalıyor", f'''
<div class="sekilk" style="margin-top:30px">{sizinti()}</div>
<div class="lej3"><span><i style="background:var(--vurgu)"></i>rastgele bölme</span><span><i style="background:var(--metin)"></i>hasta-gruplu bölme</span><span><i style="background:var(--zemin)"></i>zamansal bölme</span></div>
<p class="acik">{n(SZ["n_hasta"])} sentetik hasta, {n(SZ["n_siklus"])} siklus, {n(SZ["n_embriyo"])} embriyo. Aynı hastanın embriyoları eğitim ve teste bölününce başarı olduğundan iyi görünür.</p>''',
      "Sızıntı sorusu gelirse: gradyan artırma rastgele bölmede 0.686, hasta-gruplu bölmede 0.646; lojistik regresyon neredeyse değişmiyor.",
      "Sentetik kohort, seed 2027 · AUC · kendi analizim; gerçek hasta verisi değildir", etiket="SENTETİK VERİ · klinik bulgu değildir", yedek=True)
qc = GR["kalite_kontrol"]
sahne(0, 0, "Yedek · Kalite Kontrol İzlemi", "Model de izlenir: kamera değişince uyum düşer, yerel etiketle toparlanır", f'''
<div class="qc"><img class="sekil" src="analiz/fig_kalite_kontrol.svg" alt="Model–embriyolog uyumu, sentetik">
<div><p>Haftalık model–embriyolog uyumu <b>{yo(qc["taban_uyum"])}</b>.</p><p>{qc["kamera_degisim_haftasi"]}. haftada kamera değişimi: en düşük <b>{yo(qc["degisim_sonrasi_en_dusuk"])}</b>; alarm aynı hafta.</p><p>{qc["ince_ayar_etiket_sayisi"]} yerel etiketle {qc["ince_ayar_haftasi"]}. haftada ince ayar: son 8 hafta <b>{yo(qc["son_8_hafta_uyum"])}</b>.</p></div></div>''',
      "Embriyoloğun kalite kontrolcü rolü sorulursa: model de bir KPI gibi izlenir.",
      f'Sentetik görüntü demosu, seed {GR["seed"]} · haftada {qc["haftalik_embriyo"]} embriyo · EWMA izlemi', etiket="SENTETİK GÖRÜNTÜ · klinik bulgu değildir", yedek=True)

# kapanış, yedeklerden önce gelmeli: sıralamayı düzelt
ana = [s for s in SLAYT if not s["yedek"]]; ydk = [s for s in SLAYT if s["yedek"]]
SLAYT = ana + ydk
for i, s in enumerate(SLAYT):
    s["html"] = s["html"].replace("%%NO%%", "yedek" if s["yedek"] else (f"{i+1} / {len(ana)}" if 0 < i else ""))

EK_CSS = (KOK / "v4.css").read_text(encoding="utf-8")
EK_JS = (KOK / "v4.js").read_text(encoding="utf-8")
JSV = dict(DURAK=json.dumps(DURAK, ensure_ascii=False), DURUM=json.dumps(DURUM, ensure_ascii=False),
           KR_E=f(sm["ort"], 1), KR_A=f(sy["ort"], 1))


def derle():
    html = ISKELET.read_text(encoding="utf-8")
    g = html.index("</head>")
    bas = html.index('<main id="sahne">', g) + len('<main id="sahne">'); son = html.index('<div id="ilerleme">', bas)
    html = html[:bas] + "\n" + "\n\n".join(s["html"] for s in SLAYT) + "\n" + html[son:]
    js = EK_JS
    for k, v in JSV.items(): js = js.replace(f"%%{k}%%", v)
    html = html.replace("</style>", ek_font() + "\n" + EK_CSS + "\n</style>", 1).replace("</body>", "<script>\n" + js + "\n</script>\n</body>")
    html = html.replace("<title>SUNUM BAŞLIĞI — Klinik Embriyoloji Kongresi 2027</title>", "<title>Yapay zekânın iş akışına entegrasyonu ve ileri istatistik</title>")
    html = html.replace("var HEDEF_SN=18*60;", "var HEDEF_SN=15*60;")
    assert "%%" not in html, re.findall(r"%%[A-Z_0-9]+%%", html)
    (KOK / "sunum.html").write_text(html, encoding="utf-8")
    toplam = sum(s["sure"] for s in SLAYT)
    satir = [f"# Sunucu notları (TASLAK v4)\n\nPlanlanan süre: {toplam//60} dk {toplam%60} sn ({toplam} sn), {len(ana)} ana sahne + {len(ydk)} yedek. Hız ≈ 2.3 sözcük/sn. Köşeli parantez = ekranda yapılacak hareket.\n"]
    for i, s in enumerate(SLAYT, 1):
        soz = len(re.sub(r"\[[^\]]*\]", "", s["notu"]).split())
        satir.append(f"## {i}. {s['kisa']}  ({s['sure']} sn · {soz} sözcük)\n\n**{s['h2']}**\n\n{s['notu']}\n")
    (KOK / "sunucu_notlari.md").write_text("\n".join(satir), encoding="utf-8")

    # tek sayı kaynağı: bölüm JSON'ları + demo JSON'ları + depo; metin biçimindeki değerlerin içindeki sayılar ayrıca çıkarılır
    def metin_sayilari(x, out):
        if isinstance(x, dict):
            for v in x.values(): metin_sayilari(v, out)
        elif isinstance(x, list):
            for v in x: metin_sayilari(v, out)
        elif isinstance(x, str):
            out += [float(m.replace(",", ".")) for m in re.findall(r"\d+[.,]\d+", x) if not re.search(r"10\.\d{4}", m)]
    ms = {}
    for ad, B in (("bolum1", B1), ("bolum2", B2), ("bolum3", B3), ("bolum4", B4), ("bolum5", B5)):
        for k, v in B.items():
            if isinstance(v, dict) and isinstance(v.get("deger"), (str, list, dict)):
                o = []; metin_sayilari(v["deger"], o)
                if o: ms[f"{ad}.{k}"] = o
    json.dump(dict(_not="Sunum v4 için tek sayı kaynağı. bolumN = bolumler/0N_sayilar.json (aynen); demo_* = /home/claude/sunum/analiz altındaki sentetik demo sonuçları (aynen); depo = git log'dan bu derlemede sayıldı; metinden_sayilar = bölüm JSON'larında metin olarak duran değerlerin içindeki sayılar.",
                   bolum1=B1, bolum2=B2, bolum3=B3, bolum4=B4, bolum5=B5, demo_kpi=KP, demo_gorsel=GR, demo_dogrulama=SZ, depo=DEPO, metinden_sayilar=ms),
              open(A / "tum_sayilar.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    (KOK / "sahne_listesi.json").write_text(json.dumps([dict(no=i, soru=s["q"] if s["q"] in (1, 2, 3, 4, 5) else None, kisa=s["kisa"], baslik=s["h2"], sure=s["sure"], yedek=s["yedek"]) for i, s in enumerate(SLAYT, 1)], ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"sunum.html: {len(ana)} ana sahne + {len(ydk)} yedek, planlanan {toplam//60} dk {toplam%60} sn ({toplam} sn)")
    for i, s in enumerate(SLAYT, 1):
        soz = len(re.sub(r"\[[^\]]*\]", "", s["notu"]).split())
        if s["sure"]: print(f"  {i:2d} {s['kisa']:<28} {s['sure']:3d} sn  not {soz:3d} sözcük  ({soz/s['sure']:.2f}/sn)")


if __name__ == "__main__":
    derle()
