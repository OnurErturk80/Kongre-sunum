#!/usr/bin/env python3
"""
Görsel analizde kişiselleştirme demosu (SENTETİK görüntüler).

Soru: Başka bir laboratuvarın görüntüleriyle eğitilmiş "hazır" bir model bizim mikroskobumuzda
ne kadar iyi çalışır? Kendi embriyologlarımızın etiketlediği az sayıda yerel görüntüyle
ince ayar yapınca ne değişir? Ve model kullanılırken embriyolog onu nasıl denetler?

Görüntüler gerçek değildir: zona halkası, trofektoderm (TE) hücre dizisi ve iç hücre kitlesi (ICM)
kabaca çizilmiş 48x48 gri tonlu şekillerdir. "Kullanılabilir" etiketi ICM büyüklüğü ve TE
düzenliliğinden türetilir; etiketlere %8 gözlemci gürültüsü eklenir.
Laboratuvarlar arası fark: kontrast, parlaklık, aydınlatma eğimi, bulanıklık, ölçek.

Yöntem: "omurga" sabit bir özellik çıkarıcıdır (başka yerde öğrenilmiş derin ağın analoğu); kişiselleştirme\nyalnız ölçeklemeyi ve son katmanı yerel etiketlerle yeniden eğitir (transfer öğrenme / ince ayar).\n\nÇıktılar: sonuclar_gorsel.json, fig_ince_ayar, ornek_A/B/C.png, fig_kalite_kontrol
Kullanım:  python3 gorsel_demo.py --cikti-dir sonuc_gorsel [--slayt]
"""
import argparse, json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score

RENK = {"mürekkep": "#14213D", "vurgu": "#E4572E", "mavi": "#2A6F97", "gri": "#8D99AE"}
N = 48
LAB = {   # görüntüleme koşulları (mikroskop/kamera)
    "A": dict(kontrast=1.00, parlaklik=0.00, egim=0.00, bulaniklik=0.7, olcek=1.00, gurultu=0.05),
    "B": dict(kontrast=0.65, parlaklik=0.18, egim=0.35, bulaniklik=1.3, olcek=1.12, gurultu=0.08),
    "C": dict(kontrast=0.55, parlaklik=-0.05, egim=-0.45, bulaniklik=1.0, olcek=0.95, gurultu=0.10),  # kamera değişimi
}
ETIKET_GURULTUSU = 0.08


def embriyo(rng, lab):
    L = LAB[lab]
    yy, xx = np.mgrid[0:N, 0:N] - (N - 1) / 2
    r = np.hypot(xx, yy) / L["olcek"]; th = np.arctan2(yy, xx)
    icm = rng.uniform(0.15, 1.0)            # ICM büyüklüğü (gizli)
    te = rng.uniform(0.0, 1.0)              # TE düzensizliği (gizli)
    img = 0.35 * np.ones((N, N))
    img += 0.55 * np.exp(-((r - 19) ** 2) / 1.5)                                     # zona
    teh = 16 + (0.6 + 2.2 * te) * np.sin(10 * th + rng.uniform(0, 6.3)) * rng.uniform(0.5, 1, 1)
    img += 0.35 * np.exp(-((r - teh) ** 2) / 2.0)                                   # TE
    a0 = rng.uniform(0, 2 * np.pi)
    cx, cy = 10 * np.cos(a0), 10 * np.sin(a0)
    d = np.hypot(xx / L["olcek"] - cx, yy / L["olcek"] - cy)
    img += 0.45 * np.exp(-(d ** 2) / (2 * (1.5 + 4.5 * icm) ** 2))                  # ICM
    img -= 0.12 * (r < 15)                                                            # blastosöl
    img = gaussian_filter(img, L["bulaniklik"])
    img = L["kontrast"] * (img - 0.5) + 0.5 + L["parlaklik"] + L["egim"] * xx / N
    img += rng.normal(0, L["gurultu"], img.shape)
    gercek = int((icm > 0.55) and (te < 0.55))
    y = gercek if rng.random() > ETIKET_GURULTUSU else 1 - gercek               # embriyolog etiketi
    return np.clip(img, 0, 1), y, gercek


def veri(rng, lab, n):
    X, Y, G = [], [], []
    for _ in range(n):
        i, y, g = embriyo(rng, lab); X.append(i.ravel()); Y.append(y); G.append(g)
    return np.array(X), np.array(Y), np.array(G)


# --- "Omurga": başka yerde öğrenilmiş, SABİT özellik çıkarıcı (transfer öğrenmenin analoğu) ---------
_yy, _xx = np.mgrid[0:N, 0:N] - (N - 1) / 2
_RB = np.clip(np.hypot(_xx, _yy).astype(int), 0, 23)
_AB = ((np.arctan2(_yy, _xx) + np.pi) / (2 * np.pi) * 16).astype(int) % 16


def omurga(X):
    """Halka x açı ortalamaları; halka başına ortalama, açısal std ve tepe (max - medyan). Dönmeden etkilenmez."""
    out = []
    for x in X.reshape(-1, N, N):
        M = np.zeros((24, 16)); C = np.zeros((24, 16))
        np.add.at(M, (_RB, _AB), x); np.add.at(C, (_RB, _AB), 1); M /= np.maximum(C, 1)
        out.append(np.r_[M.mean(1), M.std(1), M.max(1) - np.median(M, 1)])
    return np.array(out)


class Model:
    """Sabit omurga + ölçekleme + son katman (lojistik). ince_ayar(): ölçeklemeyi ve son katmanı yerel etiketlerle günceller."""
    def __init__(self, FA, yA, C=0.1):
        self.FA, self.yA, self.C = FA, yA, C
        self.mu, self.sd = FA.mean(0), FA.std(0) + 1e-9
        self.bas = LogisticRegression(C=C, max_iter=4000).fit((FA - self.mu) / self.sd, yA)

    def olasilik(self, F):
        return self.bas.predict_proba((F - self.mu) / self.sd)[:, 1]

    def ince_ayar(self, F_yerel, y_yerel, agirlik=10.0):
        mu_y, sd_y = F_yerel.mean(0), F_yerel.std(0) + 1e-9
        FA_n = (self.FA - self.FA.mean(0)) / (self.FA.std(0) + 1e-9)
        w = np.r_[np.ones(len(self.yA)), np.full(len(y_yerel), agirlik)]
        self.bas = LogisticRegression(C=self.C, max_iter=4000).fit(
            np.r_[FA_n, (F_yerel - mu_y) / sd_y], np.r_[self.yA, y_yerel], sample_weight=w)
        self.mu, self.sd = mu_y, sd_y
        return self


def stil(slayt):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 20 if slayt else 12,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.edgecolor": RENK["mürekkep"], "axes.labelcolor": RENK["mürekkep"],
                         "xtick.color": RENK["mürekkep"], "ytick.color": RENK["mürekkep"]})


def kaydet(fig, yol, etiket):
    fig.text(0.99, 1.0, etiket, ha="right", va="bottom", fontsize=9, color=RENK["vurgu"], fontweight="bold")
    fig.savefig(yol + ".png", dpi=200, bbox_inches="tight"); fig.savefig(yol + ".svg", bbox_inches="tight"); plt.close(fig)


def ornek_izgara(rng, lab, yol):
    fig, axs = plt.subplots(2, 4, figsize=(6, 3.1))
    for ax in axs.ravel():
        i, _, _ = embriyo(rng, lab); ax.imshow(i, cmap="gray", vmin=0, vmax=1); ax.axis("off")
    fig.subplots_adjust(wspace=0.04, hspace=0.04)
    fig.savefig(yol, dpi=110, bbox_inches="tight", facecolor="black"); plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cikti-dir", default="sonuc_gorsel"); ap.add_argument("--slayt", action="store_true")
    ap.add_argument("--seed", type=int, default=2027); ap.add_argument("--tekrar", type=int, default=5)
    ap.add_argument("--etiket", default="SENTETİK GÖRÜNTÜLER — klinik bulgu değildir")
    a = ap.parse_args(); os.makedirs(a.cikti_dir, exist_ok=True); stil(a.slayt)
    rng = np.random.default_rng(a.seed)
    S = {"veri_kaynagi": "SENTETIK", "seed": a.seed, "etiket_gurultusu": ETIKET_GURULTUSU, "lab_kosullari": LAB}

    # --- 1) Hazır model (Lab A) vs omurga sabit + son katman yerel etiketlerle (Lab B)
    yerel_n = [0, 25, 50, 100, 200, 400]
    auc = {k: [] for k in yerel_n}; ba = {k: [] for k in yerel_n}; a_auc, poz0 = [], []
    for t in range(a.tekrar):
        XA, yA, _ = veri(rng, "A", 2000); XAt, _, gAt = veri(rng, "A", 800)
        XBt, _, gBt = veri(rng, "B", 800); XBh, yBh, _ = veri(rng, "B", max(yerel_n))
        FA, FAt, FBt, FBh = omurga(XA), omurga(XAt), omurga(XBt), omurga(XBh)
        mA = Model(FA, yA); a_auc.append(roc_auc_score(gAt, mA.olasilik(FAt)))
        for k in yerel_n:
            m = mA if k == 0 else Model(FA, yA).ince_ayar(FBh[:k], yBh[:k])
            p = m.olasilik(FBt)
            auc[k].append(roc_auc_score(gBt, p)); ba[k].append(balanced_accuracy_score(gBt, p > 0.5))
            if k == 0: poz0.append(float(np.mean(p > 0.5)))
    S["ince_ayar"] = dict(hazir_model_kendi_labinda_auc=float(np.mean(a_auc)), yerel_n=yerel_n,
                          auc=[float(np.mean(auc[k])) for k in yerel_n],
                          dengeli_dogruluk=[float(np.mean(ba[k])) for k in yerel_n],
                          hazir_model_pozitif_orani=float(np.mean(poz0)), tekrar=a.tekrar,
                          not_="ölçütler gürültüsüz gerçek etikete göre; eğitim etiketleri %8 gözlemci gürültülü")
    ia = S["ince_ayar"]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.axhline(ia["hazir_model_kendi_labinda_auc"], color=RENK["gri"], ls="--", lw=1.6, label="Hazır model, kendi labında")
    ax.axhline(0.5, color=RENK["mürekkep"], ls=":", lw=1.2, label="Yazı-tura")
    ax.plot(yerel_n, ia["auc"], "o-", color=RENK["vurgu"], lw=2.8, ms=10, label="Bizim labımızda")
    ax.set_xlabel("Embriyoloğun etiketlediği yerel görüntü sayısı"); ax.set_ylabel("AUC")
    ax.set_ylim(0.4, 1.0); ax.legend(frameon=False, loc="lower right", fontsize="small")
    kaydet(fig, f"{a.cikti_dir}/fig_ince_ayar", a.etiket)
    ornek_izgara(rng, "A", f"{a.cikti_dir}/ornek_A.png"); ornek_izgara(rng, "B", f"{a.cikti_dir}/ornek_B.png")
    ornek_izgara(rng, "C", f"{a.cikti_dir}/ornek_C.png")

    # --- 2) Embriyolog = kalite kontrolcü: haftalık uyum izlemi, kamera değişimi, yeniden ince ayar
    XA, yA, _ = veri(rng, "A", 2000); XB, yB, _ = veri(rng, "B", 200)
    FA = omurga(XA); m = Model(FA, yA).ince_ayar(omurga(XB), yB)
    hafta, degisim, lam, pay = 40, 18, 0.3, 0.08
    uyum, ewl, ew, alarm, ince = [], [], None, None, None
    Fc, yc = [], []
    for h in range(hafta):
        lab = "B" if h < degisim else "C"
        X, y, _ = veri(rng, lab, 30); F = omurga(X)                 # haftada 30 embriyo, embriyolog etiketler
        u = float(np.mean((m.olasilik(F) > 0.5) == y)); uyum.append(u)
        ew = u if ew is None else lam * u + (1 - lam) * ew; ewl.append(ew)
        if h >= degisim: Fc.append(F); yc.append(y)
        taban = float(np.mean(uyum[:min(max(h, 1), degisim)]))
        if alarm is None and h >= 4 and ew < taban - pay:
            alarm = h; ince = h + 2                                  # iki hafta yerel etiket topla
        if ince is not None and h == ince:
            m = Model(FA, yA).ince_ayar(np.vstack(Fc[-3:]), np.concatenate(yc[-3:]))
    taban = float(np.mean(uyum[:degisim]))
    S["kalite_kontrol"] = dict(hafta=hafta, kamera_degisim_haftasi=degisim + 1,
                               alarm_haftasi=None if alarm is None else alarm + 1,
                               ince_ayar_haftasi=None if ince is None else ince + 1,
                               taban_uyum=taban, degisim_sonrasi_en_dusuk=float(min(uyum[degisim:])),
                               son_8_hafta_uyum=float(np.mean(uyum[-8:])), haftalik_embriyo=30,
                               ince_ayar_etiket_sayisi=90, ewma_lambda=lam, alarm_payi=pay)
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(np.arange(1, hafta + 1), uyum, "o", color=RENK["gri"], ms=6, label="Haftalık uyum")
    ax.plot(np.arange(1, hafta + 1), ewl, color=RENK["mavi"], lw=2.6, label="EWMA")
    ax.axhline(taban - pay, color=RENK["mürekkep"], ls="--", lw=1.2, label="Alarm sınırı")
    ax.axvline(degisim + 0.5, color=RENK["vurgu"], ls=":", lw=1.8)
    ax.annotate("kamera değişti", (degisim + 0.2, 0.95), color=RENK["vurgu"], fontsize="small", ha="right")
    if ince is not None:
        ax.axvline(ince + 1.5, color=RENK["vurgu"], lw=1.8)
        ax.annotate("yerel ince ayar", (ince + 1.9, 0.47), color=RENK["vurgu"], fontsize="small")
    ax.set_ylim(0.4, 1.0); ax.set_xlabel("Hafta"); ax.set_ylabel("Model–embriyolog uyumu")
    ax.legend(frameon=False, loc="lower left", fontsize="small", ncol=3, bbox_to_anchor=(0, -0.45))
    kaydet(fig, f"{a.cikti_dir}/fig_kalite_kontrol", a.etiket)
    json.dump(S, open(f"{a.cikti_dir}/sonuclar_gorsel.json", "w"), ensure_ascii=False, indent=2)
    print(json.dumps({"ince_ayar": S["ince_ayar"], "kalite_kontrol": S["kalite_kontrol"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
