#!/usr/bin/env python3
"""
KPI takibinde ileri istatistik: iki gösterim, SENTETİK veri.

1) Erken uyarı: haftalık bir laboratuvar KPI'sinde (genel bir başarı oranı) belirli bir haftada
   küçük bir düşüş olur (ör. bir sarf malzemesi lot değişimi). Klasik aylık ortalama + 3σ sınırı
   (Shewhart p-grafiği) ile Bernoulli/binom CUSUM'un düşüşü kaç hafta sonra yakaladığı karşılaştırılır.
2) Adil karşılaştırma: embriyolog bazında oranlar. Ham oran ile yaşa göre ayarlı (dolaylı
   standardizasyon, gözlenen/beklenen) oran funnel plot üzerinde karşılaştırılır.

Gerçek parametreler kodda yazılıdır; yöntemin doğru çalıştığı sınanabilir.
Kullanım:  python3 kpi_demo.py --cikti-dir sonuc_kpi [--slayt]
"""
import argparse, json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

RENK = {"mürekkep": "#14213D", "vurgu": "#E4572E", "mavi": "#2A6F97", "gri": "#8D99AE"}
GERCEK = dict(
    hafta_sayisi=104, haftalik_ort_vaka=40, taban_oran=0.75, kayma_haftasi=70, kayma_sonrasi_oran=0.69,
    cusum_alternatif=0.70, cusum_esik_h=4.5,
    embriyolog_dusuk_etki_logodds=-0.45,   # yalnız "E" gerçekten düşük
    yas_beta=-0.06,                        # her +1 yaş için log-odds
)


def stil(slayt):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 20 if slayt else 12,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": RENK["mürekkep"], "axes.labelcolor": RENK["mürekkep"],
                         "xtick.color": RENK["mürekkep"], "ytick.color": RENK["mürekkep"]})


def kaydet(fig, yol, etiket):
    fig.text(0.99, 1.0, etiket, ha="right", va="bottom", fontsize=9, color=RENK["vurgu"], fontweight="bold")
    fig.savefig(yol + ".png", dpi=200, bbox_inches="tight"); fig.savefig(yol + ".svg", bbox_inches="tight")
    plt.close(fig)


def erken_uyari(rng, S, out, etiket):
    g = GERCEK
    H = g["hafta_sayisi"]
    n = rng.poisson(g["haftalik_ort_vaka"], H)
    p = np.where(np.arange(H) < g["kayma_haftasi"], g["taban_oran"], g["kayma_sonrasi_oran"])
    x = rng.binomial(n, p)
    # --- aylık (4 haftalık) Shewhart p-grafiği, taban = ilk 52 hafta
    ay = np.arange(H) // 4
    n_ay = np.bincount(ay, n); x_ay = np.bincount(ay, x); p_ay = x_ay / n_ay
    p0 = x[:52].sum() / n[:52].sum()
    alt = p0 - 3 * np.sqrt(p0 * (1 - p0) / n_ay)
    kayma_ay = g["kayma_haftasi"] // 4
    alarm_ay = [i for i in range(len(p_ay)) if i >= 13 and p_ay[i] < alt[i]]
    ilk_ay = next((i for i in alarm_ay if i >= kayma_ay), None)
    shewhart_gecikme_hafta = None if ilk_ay is None else (ilk_ay + 1) * 4 - g["kayma_haftasi"]
    yanlis_alarm_ay = sum(1 for i in alarm_ay if i < kayma_ay)
    # --- haftalık binom CUSUM (düşüşü arar), başlangıç: 53. hafta (taban dönemi sonrası)
    p1 = g["cusum_alternatif"]
    a = np.log(p1 / p0); b = np.log((1 - p1) / (1 - p0))
    C = np.zeros(H); alarm_h = None
    for t in range(52, H):
        llr = x[t] * a + (n[t] - x[t]) * b
        C[t] = max(0.0, C[t - 1] + llr)
        if alarm_h is None and C[t] > g["cusum_esik_h"] and t >= g["kayma_haftasi"]:
            alarm_h = t
    cusum_yanlis = int(any(C[52:g["kayma_haftasi"]] > g["cusum_esik_h"]))
    cusum_gecikme = None if alarm_h is None else alarm_h + 1 - g["kayma_haftasi"]
    S["erken_uyari"] = dict(taban_oran_tahmini=float(p0), kayma_haftasi=g["kayma_haftasi"],
                            shewhart_gecikme_hafta=shewhart_gecikme_hafta, shewhart_yanlis_alarm_ay=int(yanlis_alarm_ay),
                            cusum_gecikme_hafta=cusum_gecikme, cusum_yanlis_alarm=cusum_yanlis,
                            cusum_esik=g["cusum_esik_h"], gercek_taban=g["taban_oran"],
                            gercek_kayma_sonrasi=g["kayma_sonrasi_oran"],
                            dusus_puan=float(round((g["taban_oran"] - g["kayma_sonrasi_oran"]) * 100, 1)))
    # şekil: üstte aylık oran + sınır, altta CUSUM
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 6.6), sharex=False, gridspec_kw={"height_ratios": [1, 1]})
    a1.plot(np.arange(len(p_ay)) * 4 + 2, p_ay, "o-", color=RENK["mavi"], lw=2, ms=5, label="Aylık oran")
    a1.plot(np.arange(len(p_ay)) * 4 + 2, alt, color=RENK["gri"], ls="--", lw=1.5, label="Alt kontrol sınırı (3σ)")
    a1.axvline(g["kayma_haftasi"], color=RENK["vurgu"], lw=1.5, ls=":")
    a1.set_ylabel("KPI oranı"); a1.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, fontsize="small")
    a2.plot(np.arange(H), C, color=RENK["vurgu"], lw=2.4, label="CUSUM (haftalık)")
    a2.axhline(g["cusum_esik_h"], color=RENK["mürekkep"], lw=1.2, ls="--", label="Alarm eşiği")
    a2.axvline(g["kayma_haftasi"], color=RENK["vurgu"], lw=1.5, ls=":")
    if alarm_h is not None:
        a2.plot(alarm_h, C[alarm_h], "o", color=RENK["vurgu"], ms=12)
    a2.set_xlabel("Hafta"); a2.set_ylabel("CUSUM"); a2.legend(frameon=False, loc="upper left", fontsize="small")
    a2.set_xlim(0, H); a1.set_xlim(0, H)
    fig.tight_layout()
    kaydet(fig, f"{out}/fig_kpi_erken_uyari", etiket)


def tespit_gecikmesi(rng):
    """Tek bir simülasyon: (shewhart_gecikme, cusum_gecikme, shewhart_yanlis, cusum_yanlis). None = yakalanmadı."""
    g = GERCEK; H = g["hafta_sayisi"]
    n = rng.poisson(g["haftalik_ort_vaka"], H)
    p = np.where(np.arange(H) < g["kayma_haftasi"], g["taban_oran"], g["kayma_sonrasi_oran"])
    x = rng.binomial(n, p)
    ay = np.arange(H) // 4; n_ay = np.bincount(ay, n); x_ay = np.bincount(ay, x); p_ay = x_ay / n_ay
    p0 = x[:52].sum() / n[:52].sum(); alt = p0 - 3 * np.sqrt(p0 * (1 - p0) / n_ay)
    k_ay = g["kayma_haftasi"] // 4
    al = [i for i in range(13, len(p_ay)) if p_ay[i] < alt[i]]
    sh = next(((i + 1) * 4 - g["kayma_haftasi"] for i in al if i >= k_ay), None)
    sh_y = any(i < k_ay for i in al)
    p1 = g["cusum_alternatif"]; a = np.log(p1 / p0); b = np.log((1 - p1) / (1 - p0))
    C = 0.0; cu = None; cu_y = False
    for t in range(52, H):
        C = max(0.0, C + x[t] * a + (n[t] - x[t]) * b)
        if C > g["cusum_esik_h"]:
            if t < g["kayma_haftasi"]:
                cu_y = True; C = 0.0          # yanlış alarm: incele ve sıfırla
            elif cu is None:
                cu = t + 1 - g["kayma_haftasi"]
    return sh, cu, sh_y, cu_y


def monte_carlo(S, tekrar=500, seed=11):
    rng = np.random.default_rng(seed)
    r = [tespit_gecikmesi(rng) for _ in range(tekrar)]
    kalan = GERCEK["hafta_sayisi"] - GERCEK["kayma_haftasi"]
    def ozet(i):
        d = [x[i] for x in r if x[i] is not None]
        return dict(yakalama_orani=len(d) / tekrar, medyan_gecikme_hafta=float(np.median(d)) if d else None)
    S["monte_carlo"] = dict(tekrar=tekrar, izleme_suresi_hafta=kalan,
                            shewhart=ozet(0), cusum=ozet(1),
                            shewhart_yanlis_alarm_orani=float(np.mean([x[2] for x in r])),
                            cusum_yanlis_alarm_orani=float(np.mean([x[3] for x in r])),
                            cusum_once_veya_ayni=float(np.mean([(x[1] is not None) and (x[0] is None or x[1] <= x[0]) for x in r])))


def funnel(rng, S, out, etiket):
    g = GERCEK
    adlar = list("ABCDEF")
    nler = [420, 380, 300, 520, 610, 90]          # yıllık vaka
    yas_ort = [34, 34, 33, 35, 34, 39.5]          # F: ağırlıkla ileri yaş hastalar
    etki = {"E": g["embriyolog_dusuk_etki_logodds"]}
    satir = []
    for ad, nn, ya in zip(adlar, nler, yas_ort):
        yas = np.clip(rng.normal(ya, 3.5, nn), 22, 45)
        lp = np.log(g["taban_oran"] / (1 - g["taban_oran"])) + g["yas_beta"] * (yas - 34) + etki.get(ad, 0)
        y = (rng.random(nn) < 1 / (1 + np.exp(-lp))).astype(int)
        satir += [(ad, a_, y_) for a_, y_ in zip(yas, y)]
    A = np.array([s[1] for s in satir]).reshape(-1, 1); Y = np.array([s[2] for s in satir]); E = np.array([s[0] for s in satir])
    m = LogisticRegression().fit(A, Y)              # yalnız yaş: vaka karması modeli
    beklenen = m.predict_proba(A)[:, 1]
    genel = Y.mean()
    tablo = {}
    for ad in adlar:
        k = E == ad
        O, Eb, nn = Y[k].sum(), beklenen[k].sum(), k.sum()
        tablo[ad] = dict(n=int(nn), ham=float(O / nn), ayarli=float(O / Eb * genel), yas_ort=float(A[k].mean()))
    S["funnel"] = dict(genel_oran=float(genel), embriyologlar=tablo, sinirlar_yuzde=[95, 99.8], sinir_z=[1.96, 3.09],
                       gercek_dusuk="E", ileri_yas_hasta="F")
    for tur in ["ham", "ayarli"]:
        fig, ax = plt.subplots(figsize=(8.6, 5.4))
        nn = np.linspace(40, 700, 300)
        for z, ls in [(1.96, "--"), (3.09, ":")]:
            ax.plot(nn, genel - z * np.sqrt(genel * (1 - genel) / nn), color=RENK["gri"], ls=ls, lw=1.4)
            ax.plot(nn, genel + z * np.sqrt(genel * (1 - genel) / nn), color=RENK["gri"], ls=ls, lw=1.4)
        ax.axhline(genel, color=RENK["mürekkep"], lw=1)
        for ad in adlar:
            v = tablo[ad]; val = v[tur]
            dis = abs(val - genel) > 3.09 * np.sqrt(genel * (1 - genel) / v["n"])
            ax.plot(v["n"], val, "o", ms=16, color=RENK["vurgu"] if dis else RENK["mavi"])
            ax.annotate(ad, (v["n"], val), xytext=(12, -6), textcoords="offset points", fontsize="medium", fontweight="bold")
        ax.set_xlabel("Vaka sayısı (yıllık)"); ax.set_ylabel("Oran" + (" (yaşa göre ayarlı)" if tur == "ayarli" else " (ham)"))
        ax.set_ylim(0.45, 0.95)
        kaydet(fig, f"{out}/fig_funnel_{tur}", etiket)
        S["funnel"][f"sinir_disi_{tur}"] = [ad for ad in adlar if abs(tablo[ad][tur] - genel) > 3.09 * np.sqrt(genel * (1 - genel) / tablo[ad]["n"])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti-dir", default="sonuc_kpi"); ap.add_argument("--slayt", action="store_true")
    ap.add_argument("--seed", type=int, default=2027)
    ap.add_argument("--etiket", default="SENTETİK VERİ — klinik bulgu değildir")
    a = ap.parse_args(); os.makedirs(a.cikti_dir, exist_ok=True); stil(a.slayt)
    rng = np.random.default_rng(a.seed)
    S = {"veri_kaynagi": "SENTETIK", "seed": a.seed, "gercek_parametreler": GERCEK}
    erken_uyari(rng, S, a.cikti_dir, a.etiket)
    monte_carlo(S)
    funnel(rng, S, a.cikti_dir, a.etiket)
    json.dump(S, open(f"{a.cikti_dir}/sonuclar_kpi.json", "w"), ensure_ascii=False, indent=2)
    print(json.dumps(S["erken_uyari"], ensure_ascii=False)); print(json.dumps(S["monte_carlo"], ensure_ascii=False))
    print({k: (v["n"], round(v["ham"], 3), round(v["ayarli"], 3)) for k, v in S["funnel"]["embriyologlar"].items()},
          "ham dışı:", S["funnel"]["sinir_disi_ham"], "ayarlı dışı:", S["funnel"]["sinir_disi_ayarli"])


if __name__ == "__main__":
    main()
