#!/usr/bin/env python3
"""
SENTETİK embriyoloji kohortu üretici (hasta -> siklus -> embriyo hiyerarşisi).

NEDEN VAR: Kongre sunumunda yöntemi göstermek için gerçek hasta verisine
dokunmak gerekmez. Bu veri "doğruluğu bilinen" bir dünyadan gelir: gerçek etki
büyüklükleri kodda yazılıdır, böylece yöntemin gerçeği ne kadar iyi
yakaladığı kanıtlanabilir. Gerçek veriyle yapılamayacak bir şey.

ÖNEMLİ: Bu veri SENTETİKTİR. Sunumda her grafikte/tabloda "SENTETİK VERİ"
ibaresi bulunmalıdır. Klinik bir bulgu olarak sunulamaz.

Kullanım:
    python3 sentetik_veri.py --n-hasta 700 --seed 2027 --cikti sentetik_kohort.csv
"""
import argparse, json
import numpy as np
import pandas as pd

# Gerçek (bilinen) parametreler: analiz bunları geri bulabilmeli.
GERCEK = {
    "kesisim": -0.15,
    "yas_beta_yil_basina": -0.09,       # her +1 yaş için log-odds değişimi
    "embriyo_kalitesi_beta": 0.80,      # gizli embriyo kalitesi (gözlenmez)
    "hasta_sd": 0.80,                   # gözlenmeyen hasta düzeyi etki (gizli)
    "siklus_sd": 0.40,                  # gözlenmeyen siklus düzeyi etki
    "zaman_kaymasi_2023_sonrasi": 0.35  # kültür sistemi iyileşmesi: taban oran artar
}


def uret(n_hasta=700, seed=2027):
    rng = np.random.default_rng(seed)
    satirlar = []
    for h in range(n_hasta):
        yas = float(np.clip(rng.normal(34, 4.5), 22, 44))
        amh = float(np.clip(rng.lognormal(0.4, 0.8), 0.1, 15))
        # BMI: hastaya özgü, nedensel etkisi YOK. Ama hastayı "parmak izi" gibi
        # tanımlar -> rastgele bölmede modelin ezberlemesine (sızıntıya) yol açar.
        bmi = float(np.round(rng.normal(25, 4), 2))
        protokol = rng.choice(["antagonist", "agonist", "mild"], p=[.6, .25, .15])
        u_h = rng.normal(0, GERCEK["hasta_sd"])
        n_sik = rng.choice([1, 2, 3], p=[.6, .3, .1])
        for s in range(n_sik):
            yil = rng.uniform(2019, 2026)
            v_s = rng.normal(0, GERCEK["siklus_sd"])
            lam = np.clip(5.5 * np.exp(-0.05 * (yas - 30)) * (0.6 + 0.3 * np.log1p(amh)), 1.2, 12)
            n_emb = max(1, int(rng.poisson(lam)))
            oosit = int(n_emb + rng.integers(1, 6))
            for e in range(n_emb):
                q = rng.normal(0, 1)  # gizli embriyo kalitesi
                d3_hucre = int(np.clip(round(7.5 + 1.0 * q + 0.5 * u_h + rng.normal(0, 1.2)), 3, 12))
                frag = float(np.clip(12 - 4 * q - 2 * u_h + rng.normal(0, 4), 0, 40))
                morf_ham = 2.5 + 0.9 * q + rng.normal(0, 0.8)
                morf = int(np.clip(np.round(morf_ham), 1, 4))   # 1 kötü ... 4 iyi
                kayma = GERCEK["zaman_kaymasi_2023_sonrasi"] if yil >= 2023.5 else 0.0
                lp = (GERCEK["kesisim"] + GERCEK["yas_beta_yil_basina"] * (yas - 34)
                      + GERCEK["embriyo_kalitesi_beta"] * q + u_h + v_s + kayma)
                p = 1 / (1 + np.exp(-lp))
                y = int(rng.random() < p)
                satirlar.append(dict(
                    hasta_id=f"H{h:04d}", siklus_id=f"H{h:04d}-S{s+1}",
                    embriyo_id=f"H{h:04d}-S{s+1}-E{e+1}",
                    tarih_yil=round(yil, 3), yas=round(yas, 1), amh=round(amh, 2), bmi=bmi,
                    protokol=protokol, oosit_sayisi=oosit, d3_hucre=d3_hucre,
                    d3_fragmantasyon=round(frag, 1), d3_morfoloji=morf,
                    kullanilabilir_blastokist=y, gercek_olasilik=round(float(p), 4),
                    veri_kaynagi="SENTETIK"))
    return pd.DataFrame(satirlar)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-hasta", type=int, default=700)
    ap.add_argument("--seed", type=int, default=2027)
    ap.add_argument("--cikti", default="sentetik_kohort.csv")
    a = ap.parse_args()
    df = uret(a.n_hasta, a.seed)
    df.to_csv(a.cikti, index=False)
    meta = {"veri_kaynagi": "SENTETIK", "seed": a.seed, "n_hasta": a.n_hasta,
            "n_siklus": int(df.siklus_id.nunique()), "n_embriyo": len(df),
            "gercek_parametreler": GERCEK}
    json.dump(meta, open(a.cikti.replace(".csv", "_meta.json"), "w"),
              ensure_ascii=False, indent=2)
    print(f"{len(df)} embriyo / {df.siklus_id.nunique()} siklus / "
          f"{df.hasta_id.nunique()} hasta -> {a.cikti}")
