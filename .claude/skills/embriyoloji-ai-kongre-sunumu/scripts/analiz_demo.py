#!/usr/bin/env python3
"""
Embriyolojide "hasta içi korelasyon" tuzağı: üç gösterim, tek veri seti.

Sunumun omurga bulgusu şudur: embriyolar bağımsız değildir (aynı hastanın / aynı
siklusun embriyoları). Bunu görmezden gelmek (1) güven aralıklarını yapay olarak
daraltır, (2) makine öğrenmesi doğrulamasında SIZINTI yaratıp AUC'yi şişirir.

Çıktılar (--cikti-dir):
    sonuclar.json                -> slayt sayılarının TEK kaynağı (elle sayı yazma)
    fig_ci_naif_vs_gee.png/.svg  -> güven aralığı karşılaştırması (forest)
    fig_auc_dogrulama.png/.svg   -> rastgele vs hasta-gruplu vs zamansal AUC
    fig_kalibrasyon.png/.svg     -> kalibrasyon eğrisi
    fig_dca.png/.svg             -> karar eğrisi analizi (net fayda)

Kullanım:
    python3 analiz_demo.py --veri sentetik_kohort.csv --cikti-dir sonuc/
Gerçek veriyle çalıştırırken: sütun adları aynı olmalı; veri ANONİM ve etik
onaylı olmalı; sentetik uyarı etiketini --etiket "" ile değil, gerçek veri
bilgisiyle (ör. "Merkez X, 2019-2025, n=...") değiştirin.
"""
import argparse, json, os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, brier_score_loss
from sklearn.model_selection import KFold, GroupKFold

# ---- Görsel stil: tek yerde tanımlı, tüm şekiller aynı dili konuşsun -----------
RENK = {"mürekkep": "#14213D", "vurgu": "#E4572E", "mavi": "#2A6F97",
        "gri": "#8D99AE", "açık": "#EDF2F4", "yeşil": "#3A7D44"}
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": RENK["mürekkep"], "axes.labelcolor": RENK["mürekkep"],
    "xtick.color": RENK["mürekkep"], "ytick.color": RENK["mürekkep"],
    "figure.facecolor": "white", "axes.facecolor": "white",
})

SLAYT = False  # --slayt: projeksiyon için büyük yazı, şekil içi başlık yok (başlık slayta ait)


def baslik(ax, metin):
    if not SLAYT:
        ax.set_title(metin, loc="left", color=RENK["mürekkep"], fontweight="bold")


OZELLIKLER = ["yas", "amh", "bmi", "oosit_sayisi", "d3_hucre",
              "d3_fragmantasyon", "d3_morfoloji"]
HEDEF = "kullanilabilir_blastokist"
ZAMAN_ESIK = 2023.5   # zamansal bölme: bu yıldan önce eğit, sonra test (JSON'a da yazılır)


def kaydet(fig, yol, etiket):
    if etiket:
        # üst-sağ köşe: eksen yazılarıyla çakışmaz, kırpılınca da şekilde kalır
        fig.text(0.99, 1.0, etiket, ha="right", va="bottom", fontsize=9,
                 color=RENK["vurgu"], fontweight="bold")
    fig.savefig(yol + ".png", dpi=200, bbox_inches="tight")
    fig.savefig(yol + ".svg", bbox_inches="tight")
    plt.close(fig)


def model_uret(tur):
    if tur == "gbm":
        return HistGradientBoostingClassifier(max_depth=6, learning_rate=0.08,
                                              max_iter=300, random_state=0)
    return LogisticRegression(max_iter=2000)


def cv_auc(df, tur, bolucu, gruplar=None):
    X, y = df[OZELLIKLER].values, df[HEDEF].values
    tahmin = np.zeros(len(df))
    for tr, te in bolucu.split(X, y, gruplar):
        m = model_uret(tur).fit(X[tr], y[tr])
        tahmin[te] = m.predict_proba(X[te])[:, 1]
    return roc_auc_score(y, tahmin), tahmin


def kume_bootstrap_auc(df, tahmin, grup_kolon="hasta_id", B=300, seed=1):
    """Hasta düzeyinde (küme) bootstrap: embriyoları değil HASTALARI yeniden örnekler."""
    rng = np.random.default_rng(seed)
    d = df.assign(_p=tahmin)
    gruplar = {g: x for g, x in d.groupby(grup_kolon)}
    idler = np.array(list(gruplar))
    aucler = []
    for _ in range(B):
        sec = rng.choice(idler, size=len(idler), replace=True)
        x = pd.concat([gruplar[g] for g in sec])
        if x[HEDEF].nunique() == 2:
            aucler.append(roc_auc_score(x[HEDEF], x["_p"]))
    return np.percentile(aucler, [2.5, 97.5])


def kalibrasyon_ozeti(y, p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    lp = np.log(p / (1 - p))
    # kalibrasyon eğimi ve "içinde-kalibrasyon" (intercept, eğim sabitken)
    egim = sm.GLM(y, sm.add_constant(lp), family=sm.families.Binomial()).fit()
    inter = sm.GLM(y, np.ones_like(lp), offset=lp, family=sm.families.Binomial()).fit()
    return dict(egim=float(egim.params[1]), kesisim_offset=float(inter.params[0]),
                brier=float(brier_score_loss(y, p)))


def net_fayda(y, p, esikler):
    n = len(y)
    nb = []
    for t in esikler:
        tp = ((p >= t) & (y == 1)).sum()
        fp = ((p >= t) & (y == 0)).sum()
        nb.append(tp / n - fp / n * (t / (1 - t)))
    return np.array(nb)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--veri", required=True)
    ap.add_argument("--cikti-dir", default="sonuc")
    ap.add_argument("--etiket", default="SENTETİK VERİ — klinik bulgu değildir")
    ap.add_argument("--slayt", action="store_true",
                    help="projeksiyon modu: büyük yazı, şekil içi başlık yok")
    a = ap.parse_args()
    global SLAYT
    SLAYT = a.slayt
    if SLAYT:
        plt.rcParams.update({"font.size": 20, "axes.linewidth": 1.6,
                             "xtick.major.width": 1.6, "ytick.major.width": 1.6})
    os.makedirs(a.cikti_dir, exist_ok=True)
    df = pd.read_csv(a.veri)
    S = {"n_embriyo": int(len(df)), "n_siklus": int(df.siklus_id.nunique()),
         "n_hasta": int(df.hasta_id.nunique()),
         "olay_orani": float(df[HEDEF].mean()),
         "embriyo_basina_hasta_ort": float(len(df) / df.hasta_id.nunique())}

    # ---- A) Güven aralığı: naif lojistik vs küme-farkında GEE -----------------
    df["yas_c"] = df["yas"] - 34
    formul = f"{HEDEF} ~ yas_c + d3_fragmantasyon + d3_morfoloji"
    naif = smf.logit(formul, df).fit(disp=0)
    gee = smf.gee(formul, "hasta_id", df, family=sm.families.Binomial(),
                  cov_struct=sm.cov_struct.Exchangeable()).fit()
    S["ci"] = {}
    for terim in ["yas_c", "d3_fragmantasyon", "d3_morfoloji"]:
        n_ci, g_ci = naif.conf_int().loc[terim].values, gee.conf_int().loc[terim].values
        S["ci"][terim] = dict(
            beta_naif=float(naif.params[terim]), beta_gee=float(gee.params[terim]),
            ci_naif=[float(x) for x in n_ci], ci_gee=[float(x) for x in g_ci],
            genislik_orani=float((g_ci[1] - g_ci[0]) / (n_ci[1] - n_ci[0])))
    S["icc_yaklasik_gee_rho"] = float(gee.cov_struct.dep_params)

    fig, ax = plt.subplots(figsize=(8, 4.2))
    etk = {"yas_c": "Yaş (her +1 yıl)", "d3_fragmantasyon": "Fragmantasyon (+%1)",
           "d3_morfoloji": "Morfoloji skoru (+1)"}
    for i, t in enumerate(etk):
        c = S["ci"][t]
        ax.plot(c["ci_naif"], [i + .15] * 2, color=RENK["gri"], lw=5, solid_capstyle="round")
        ax.plot(c["beta_naif"], i + .15, "o", color=RENK["gri"], ms=8)
        ax.plot(c["ci_gee"], [i - .15] * 2, color=RENK["vurgu"], lw=5, solid_capstyle="round")
        ax.plot(c["beta_gee"], i - .15, "o", color=RENK["vurgu"], ms=8)
    ax.axvline(0, color=RENK["mürekkep"], lw=1, ls=":")
    ax.set_yticks(range(len(etk)), list(etk.values()))
    ax.set_xlabel("Log-odds katsayısı ve %95 GA")
    ax.legend(handles=[plt.Line2D([], [], color=RENK["gri"], lw=5, label="Naif (embriyolar bağımsız varsayılır)"),
                       plt.Line2D([], [], color=RENK["vurgu"], lw=5, label="GEE (hasta kümesi hesaba katılır)")],
              loc="upper center", bbox_to_anchor=(0.45, -0.22), frameon=False, ncol=1)
    baslik(ax, "Aynı veri, iki varsayım: hasta kümesi görmezden gelinirse GA yanıltır")
    kaydet(fig, f"{a.cikti_dir}/fig_ci_naif_vs_gee", a.etiket)

    # ---- B) Doğrulama şeması: rastgele vs hasta-gruplu vs zamansal ------------
    S["auc"] = {}
    tahminler = {}
    for tur, ad in [("gbm", "Gradyan artırma"), ("lr", "Lojistik regresyon")]:
        r_auc, r_p = cv_auc(df, tur, KFold(5, shuffle=True, random_state=0))
        g_auc, g_p = cv_auc(df, tur, GroupKFold(5), df["hasta_id"].values)
        # zamansal: 2023.5 öncesi eğit, sonrası test
        tr, te = df[df.tarih_yil < ZAMAN_ESIK], df[df.tarih_yil >= ZAMAN_ESIK]
        m = model_uret(tur).fit(tr[OZELLIKLER].values, tr[HEDEF].values)
        zp = m.predict_proba(te[OZELLIKLER].values)[:, 1]
        z_auc = roc_auc_score(te[HEDEF], zp)
        ci = kume_bootstrap_auc(df, g_p)
        S["auc"][tur] = dict(ad=ad, rastgele=float(r_auc), hasta_gruplu=float(g_auc),
                             hasta_gruplu_ga=[float(ci[0]), float(ci[1])], zamansal=float(z_auc))
        tahminler[tur] = dict(grup=g_p, zaman_y=te[HEDEF].values, zaman_p=zp)

    # Not: hasta-gruplu bölmede de aynı hastanın SİKLUSLARI ayrılmıyorsa sızıntı kalır;
    # burada GroupKFold hasta düzeyinde olduğu için siklus sızıntısı da kapanır.
    fig, ax = plt.subplots(figsize=(8, 4.4))
    w = .36
    for j, (tur, renk) in enumerate([("gbm", RENK["mavi"]), ("lr", RENK["gri"])]):
        v = [S["auc"][tur]["rastgele"], S["auc"][tur]["hasta_gruplu"], S["auc"][tur]["zamansal"]]
        b = ax.bar(np.arange(3) + (j - .5) * w, v, w, color=renk, label=S["auc"][tur]["ad"])
        for xi, vi in zip(b, v):
            ax.text(xi.get_x() + xi.get_width() / 2, vi + .005, f"{vi:.3f}", ha="center", fontsize="small",
                    color=RENK["mürekkep"])
    ax.set_xticks(range(3), ["Rastgele\nbölme", "Hasta-gruplu\nbölme", "Zamansal\nbölme"])
    ax.set_ylim(.5, max(.9, max(S["auc"][t]["rastgele"] for t in S["auc"]) + .06))
    ax.set_ylabel("AUC")
    ax.legend(frameon=False, loc="upper right")
    baslik(ax, "Doğrulama şeması sonucu belirler")
    kaydet(fig, f"{a.cikti_dir}/fig_auc_dogrulama", a.etiket)

    # ---- C) Kalibrasyon (zamansal test kümesi, lojistik) ------------------------
    t = tahminler["lr"]
    S["kalibrasyon_zamansal_lr"] = kalibrasyon_ozeti(t["zaman_y"], t["zaman_p"])
    fig, ax = plt.subplots(figsize=(5.6, 5.4))
    kutu = pd.qcut(t["zaman_p"], 8, duplicates="drop")
    g = pd.DataFrame({"p": t["zaman_p"], "y": t["zaman_y"], "k": kutu}).groupby("k", observed=True).mean()
    ax.plot([0, 1], [0, 1], color=RENK["gri"], ls="--", lw=1.2, label="Mükemmel kalibrasyon")
    ax.plot(g.p, g.y, "o-", color=RENK["vurgu"], lw=2.2, ms=7, label="Model (zamansal test)")
    ax.set_xlabel("Öngörülen olasılık"); ax.set_ylabel("Gözlenen oran")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.legend(frameon=False, loc="upper left")
    k = S["kalibrasyon_zamansal_lr"]
    baslik(ax, f"Eğim {k['egim']:.2f} · Brier {k['brier']:.3f}")
    kaydet(fig, f"{a.cikti_dir}/fig_kalibrasyon", a.etiket)

    # ---- D) Karar eğrisi analizi (hasta-gruplu tahminler, lojistik) ----------------
    y_all, p_all = df[HEDEF].values, tahminler["lr"]["grup"]
    es = np.linspace(.05, .85, 41)
    nb_model = net_fayda(y_all, p_all, es)
    nb_hepsi = net_fayda(y_all, np.ones_like(p_all), es)
    fig, ax = plt.subplots(figsize=(7, 4.4))
    ax.plot(es, nb_model, color=RENK["vurgu"], lw=2.4, label="Model")
    ax.plot(es, nb_hepsi, color=RENK["gri"], lw=1.6, label="Hepsini seç")
    ax.axhline(0, color=RENK["mürekkep"], lw=1, label="Hiçbirini seçme")
    ax.set_ylim(-.05, max(nb_model.max(), nb_hepsi.max()) * 1.1)
    ax.set_xlabel("Eşik olasılığı"); ax.set_ylabel("Net fayda")
    ax.legend(frameon=False)
    baslik(ax, "Doğruluk değil, fayda: karar eğrisi")
    kaydet(fig, f"{a.cikti_dir}/fig_dca", a.etiket)

    # ---- D2) Slayt için türetilmiş sayılar (tek kaynak: burada hesaplanır) ----------
    m_ort = S["embriyo_basina_hasta_ort"]; rho = S["icc_yaklasik_gee_rho"]
    S["zamansal_bolme_esik"] = ZAMAN_ESIK
    S["tasarim_etkisi"] = float(1 + (m_ort - 1) * rho)        # yaklaşık: ortalama küme büyüklüğüyle
    S["etkin_n_embriyo"] = float(S["n_embriyo"] / S["tasarim_etkisi"])
    ustun = es[nb_model > np.maximum(nb_hepsi, 0)]
    S["dca"] = dict(model_ustun_esik_min=float(ustun.min()) if len(ustun) else None,
                    model_ustun_esik_max=float(ustun.max()) if len(ustun) else None)
    try:
        from sentetik_veri import GERCEK
        S["gercek_parametreler"] = GERCEK
    except Exception:
        pass

    # ---- E) Özet cümle (slayta kopyalanacak sayılar buradan gelir) ----------------
    g = S["auc"]["gbm"]
    S["ozet"] = (f"Gradyan artırma: rastgele bölmede AUC {g['rastgele']:.3f}, hasta-gruplu bölmede "
                 f"{g['hasta_gruplu']:.3f} (%95 GA {g['hasta_gruplu_ga'][0]:.3f}–{g['hasta_gruplu_ga'][1]:.3f}), "
                 f"zamansal bölmede {g['zamansal']:.3f}.")
    json.dump(S, open(f"{a.cikti_dir}/sonuclar.json", "w"), ensure_ascii=False, indent=2)
    print(json.dumps({k: S[k] for k in ["n_embriyo", "n_hasta", "ozet"]}, ensure_ascii=False, indent=2))
    for t_, c in S["ci"].items():
        print(f"{t_:18s} GA genişlik oranı (GEE/naif) = {c['genislik_orani']:.2f}")


if __name__ == "__main__":
    main()
