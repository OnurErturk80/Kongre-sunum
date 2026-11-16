#!/usr/bin/env python3
"""
Sunumu üretir: assets/deck_iskelet.html motoru + bu dosyadaki sahneler.
Sayılar yalnız analiz/sonuc_slayt/sonuclar.json ve git log'dan gelir.
Çalıştır:  python3 kur_sunum.py   ->  sunum.html
"""
import json, re, subprocess, collections, pathlib

KOK = pathlib.Path(__file__).parent
ISKELET = pathlib.Path("/home/claude/embriyoloji-ai-kongre-sunumu/assets/deck_iskelet.html")
REPO = pathlib.Path("/home/claude/Patient-Data-Center")
S = json.load(open(KOK / "analiz/sonuc_slayt/sonuclar.json", encoding="utf-8"))
NB = "\u202f"  # dar boşluk: binlik ayırıcı (ondalık nokta ile karışmasın)


def binlik(n):
    return f"{int(round(n)):,}".replace(",", NB)


def f(x, d=3):
    return f"{x:.{d}f}"


g, l = S["auc"]["gbm"], S["auc"]["lr"]
V = dict(
    N_EMB=binlik(S["n_embriyo"]), N_SIK=binlik(S["n_siklus"]), N_HASTA=binlik(S["n_hasta"]),
    M_ORT=f(S["embriyo_basina_hasta_ort"], 2), RHO=f(S["icc_yaklasik_gee_rho"], 3),
    RHO2=f(S["icc_yaklasik_gee_rho"], 2),
    DEFF=f(S["tasarim_etkisi"], 2), ETKIN=binlik(S["etkin_n_embriyo"]),
    G_R=f(g["rastgele"]), G_G=f(g["hasta_gruplu"]), G_Z=f(g["zamansal"]),
    G_GA=f"{g['hasta_gruplu_ga'][0]:.3f}–{g['hasta_gruplu_ga'][1]:.3f}",
    L_R=f(l["rastgele"]), L_G=f(l["hasta_gruplu"]), L_Z=f(l["zamansal"]),
    L_GA=f"{l['hasta_gruplu_ga'][0]:.3f}–{l['hasta_gruplu_ga'][1]:.3f}",
    FARK=f(g["rastgele"] - g["hasta_gruplu"]),
    EGIM=f(S["kalibrasyon_zamansal_lr"]["egim"], 2),
    OFSET=f(S["kalibrasyon_zamansal_lr"]["kesisim_offset"], 2),
    BRIER=f(S["kalibrasyon_zamansal_lr"]["brier"]),
    KAYMA=f(S["gercek_parametreler"]["zaman_kaymasi_2023_sonrasi"], 2),
    YAS_ORAN=f(S["ci"]["yas_c"]["genislik_orani"], 2),
    FRAG_ORAN=f(S["ci"]["d3_fragmantasyon"]["genislik_orani"], 2),
    MORF_ORAN=f(S["ci"]["d3_morfoloji"]["genislik_orani"], 2),
    DCA_MIN=f(S["dca"]["model_ustun_esik_min"], 2), DCA_MAX=f(S["dca"]["model_ustun_esik_max"], 2),
    SEED="2027",
    RHO_TAM=repr(S["icc_yaklasik_gee_rho"]), M_TAM=repr(S["embriyo_basina_hasta_ort"]),
)

# ---------- Depodan (git) gerçek zaman çizgisi: günlük commit sayısı ----------
gun = subprocess.run(["git", "-C", str(REPO), "log", "--format=%ad", "--date=short"],
                     capture_output=True, text=True).stdout.split()
sayac = collections.Counter(gun)
gunler = sorted(sayac)
import datetime as dt
d0, d1 = dt.date.fromisoformat(gunler[0]), dt.date.fromisoformat(gunler[-1])
tum = [(d0 + dt.timedelta(days=i)) for i in range((d1 - d0).days + 1)]
mx = max(sayac.values())
W, H = 1000, 300
bw = W / len(tum)
cubuk = []
for i, d in enumerate(tum):
    n = sayac.get(d.isoformat(), 0)
    h = (n / mx) * (H - 30)
    cubuk.append(f'<rect x="{i*bw+2:.1f}" y="{H-h:.1f}" width="{bw-4:.1f}" height="{h:.1f}" rx="3" fill="var(--vurgu)" opacity="{0.35 if n==0 else 1}"/>')
GIT_SVG = (f'<svg viewBox="0 0 {W} {H+34}" class="sekil" style="background:transparent" role="img" '
           f'aria-label="Günlük commit sayısı">{"".join(cubuk)}'
           f'<text x="0" y="{H+26}" fill="var(--soluk)" font-size="22">{d0.day} Eylül</text>'
           f'<text x="{W}" y="{H+26}" text-anchor="end" fill="var(--soluk)" font-size="22">{d1.day} Ekim 2026</text></svg>')
V["COMMIT"] = str(len(gun))
V["GUN"] = str((d1 - d0).days + 1)
V["ZIRVE"] = str(mx)
sm = subprocess.run(["bash", "-c", f"wc -l < {REPO}/CLAUDE.md; ls {REPO} | grep -c '^goc_'; grep -c '^# v[0-9]' {REPO}/README.md; wc -l < {REPO}/app.py"],
                    capture_output=True, text=True).stdout.split()
V["CLAUDE_SATIR"] = binlik(int(sm[0])); V["GOC"] = sm[1]; V["SURUM"] = sm[2]; V["APP_SATIR"] = binlik(int(sm[3]))

KUNYE = (f"SENTETİK VERİ · {V['N_EMB']} embriyo / {V['N_SIK']} siklus / {V['N_HASTA']} hasta · "
         f"küme: hasta · seed {V['SEED']}")

# ======================================================================
SLAYTLAR = r'''
<!-- 1 BAŞLIK -->
<section class="slayt" data-sure="20" data-baslik="Başlık">
  <div class="kicker">Klinik Embriyoloji Kongresi 2027</div>
  <h1>Embriyolar<br><span class="vurgu">bağımsız değildir.</span></h1>
  <p style="margin-top:36px;font-size:44px;max-width:1300px">Laboratuvar verisinde yapay zekâ ve ileri istatistik için güvenli yol</p>
  <div class="ayrac"></div>
  <p class="soluk">[Ad Soyad] · [Kurum]</p>
  <aside class="not">(20 sn) Kısa tanış. Başlığı tekrar etme; “bu cümlenin neden doğru olduğunu on altı dakikada göstereceğim” de ve soruya geç.</aside>
</section>

<!-- 2 KANCA -->
<section class="slayt" data-sure="40" data-baslik="Kanca">
  <div class="kicker">Önce bir soru</div>
  <h1 style="font-size:132px">Bir hastanın<br>6 embriyosu.</h1>
  <h1 class="vurgu" style="font-size:132px;margin-top:28px" data-adim="1">Altı bağımsız<br>gözlem mi?</h1>
  <p class="soluk" style="margin-top:40px" data-adim="2">Evet diyenler elini kaldırsın. Cevabı dokuzuncu sahnede veriyle göreceğiz.</p>
  <aside class="not">(40 sn) Salona sor. “Evet” diyenleri say, “hayır” diyenleri say, sonucu yüksek sesle söyle. Cevabı VERME; “dokuzuncu sahnede veriyle bakacağız” de. Bu söz tutulmalı.</aside>
</section>

<!-- 3 PROBLEM -->
<section class="slayt" data-sure="50" data-baslik="Veri doğası">
  <div class="kicker">Problem</div>
  <h2>Embriyoloji verisi, standart istatistiğin dört varsayımına uymaz</h2>
  <div class="izgara i2" style="gap:36px;align-content:center">
    <div class="kart" data-adim="1"><h3 class="vurgu">İç içe</h3><p>Hasta → siklus → embriyo. Aynı hastanın embriyoları yaşı, uyarım yanıtını ve kültürü paylaşır.</p></div>
    <div class="kart" data-adim="2"><h3 class="vurgu">Seçilmiş</h3><p>Sonuç çoğunlukla yalnız transfer edilen embriyoda bilinir. Seçilmeyenin kaderi bilinmez.</p></div>
    <div class="kart" data-adim="3"><h3 class="vurgu">Eksik ≠ normal</h3><p>Boş alan “yapılmadı”, “kaydedilmedi” ya da “sıfır” olabilir. Üçü ayrı şeydir.</p></div>
    <div class="kart" data-adim="4"><h3 class="vurgu">Zamanla değişen</h3><p>Kültür sistemi, protokol, personel değişir. Model sabit kalır, dünya kalmaz.</p></div>
  </div>
  <aside class="not">(50 sn) Dört kartı sırayla aç, her birine tek cümle. Vurgu: bunlar yazılım sorunu değil, verinin doğası. Bu dört özellik sonraki sahnelerin dördüne karşılık geliyor: iç içe → 9, seçilmiş → 5, eksik → 5 ve 8, zamanla değişen → 12.</aside>
</section>

<!-- 4 İŞ AKIŞI HATTI -->
<section class="slayt" data-sure="75" data-baslik="İş akışı hattı">
  <div class="kicker">Patient Data Center</div>
  <h2>Tahmin anında yalnız o ana kadar bilinenler kullanılabilir</h2>
  <div class="hat" id="hat"></div>
  <div class="izgara i2" style="align-items:start;margin-top:44px;gap:40px">
    <div class="kart" style="padding:44px"><h3 class="vurgu" id="hatBaslik" style="font-size:40px"></h3><ul id="hatAlan" style="margin-top:12px;padding-left:30px"></ul></div>
    <div class="kart" style="border-color:var(--vurgu);padding:44px"><h3 style="font-size:40px">Bu noktada henüz bilinmeyen</h3>
      <p id="hatSonra" style="margin-top:16px;font-size:36px"></p>
      <p class="soluk" style="font-size:26px;margin-top:12px">Bunlardan biri özellik olarak kullanılırsa: sızıntı.</p></div>
  </div>
  <p class="soluk" style="font-size:24px;margin-top:20px">Bir aşamaya dokun.</p>
  <div class="alt"><span>Kaynak: Patient Data Center sürüm günlüğü (v1.4, v2.0, v2.5, v2.6, v3.0, v3.2, v3.6, v5.3)</span><span>4 / 17</span></div>
  <aside class="not">(75 sn) Programı bir iş akışı olarak tanıt: OPU’dan gebelik sonucuna on aşama, her biri bir ekran, her ekran bir kayıt. Sonra istatistiğe bağla: Gün 2/3’e tıkla. “Bir gün 3 embriyosu için blastokist olup olmayacağını tahmin ediyorsam, blastokist skorunu kullanamam.” Sağdaki kutu sönük aşamaları sayıyor. Sızıntının kökeni çoğu zaman kötü niyet değil, zaman çizelgesini bilmemek. Bu program zaman çizelgesini veriye işliyor.</aside>
</section>

<!-- 5 ALTI TASARIM KARARI -->
<section class="slayt" data-sure="80" data-baslik="Tasarım kararları">
  <div class="kicker">Veri altyapısı</div>
  <h2>Program, istatistiğin sorularını veri tasarımına işledi</h2>
  <div class="kararlar">
    <div data-adim="1">
      <div class="karar"><div class="sol">hCG <b>ham değer</b> saklanır; pozitif/negatif sonradan<em>v5.3</em></div><div class="sag">Geç dikotomizasyon: bilgi kaybı yok, eşik analizde seçilir</div></div>
      <div class="karar"><div class="sol">Embriyo geldiği siklusa bağlı kalır; transfer ve çözme <b>ayrı siklusa</b> bağlanır<em>v3.6 · v6.7</em></div><div class="sag">Küme yapısı ve karıştırıcılar veriden okunabilir</div></div>
    </div>
    <div data-adim="2">
      <div class="karar"><div class="sol">Transfere ulaşmayan <b>başarısız çözme</b> de iz bırakır<em>v6.7</em></div><div class="sag">Seçilmiş veri yanlılığına karşı: başarısızlık paydada kalır</div></div>
      <div class="karar"><div class="sol">“Dejenere” ile “0PN” karışmaz; işlem yapılmayan ay “sıfır” değil, <b>boş</b><em>v2.0 · CLAUDE.md</em></div><div class="sag">Eksik veri mekanizması ayrıştırılabilir</div></div>
    </div>
    <div data-adim="3">
      <div class="karar"><div class="sol">Skor elle girildiyse <b>“elle”</b> işaretlenir; otomatikse kuralı bellidir<em>v2.5 · v2.6</em></div><div class="sag">Ölçüm kaynağı ve gözlemci değişkenliği izlenir</div></div>
      <div class="karar"><div class="sol">Sonlanma güncellenir; <b>“takip kaybı”</b> ayrı kategori<em>v5.3</em></div><div class="sag">Sansür: zaman-olay analizi için ham madde</div></div>
    </div>
  </div>
  <div class="alt"><span>Her satır depodaki bir sürüm notuna dayanır</span><span>5 / 17</span></div>
  <aside class="not">(80 sn) Sol sütun ne yaptığımız, sağ sütun istatistiksel karşılığı. İlk çift: hCG’yi pozitif/negatif yazsaydık eşik bir daha geri gelmezdi. Eşiği analizde sonradan seçiyoruz. İkinci çift: başarısız çözme izsiz kalırsa sağkalım oranını hesaplayamazsınız; bu klasik seçilmiş veri yanlılığı, v6.7’de bunu yakaladık. Üçüncü çift: “elle” işareti ve “takip kaybı” kategorisi; ikincisi sansürün ta kendisi. Mesaj: istatistik analizden önce, veri tasarımında başlar. Önemli: bunlar embriyoloğun klinik içgüdüsüyle konulmuş kararlar; yapay zekâ kodladı, soruyu embriyolog sordu.</aside>
</section>

<!-- 6 YZ İLE GELİŞTİRME -->
<section class="slayt" data-sure="75" data-baslik="YZ ile geliştirme">
  <div class="kicker">Yapay zekâ ile geliştirme</div>
  <h2>Yapay zekâya talimat yazmak, protokol yazmaktır</h2>
  <div class="izgara i2" style="align-items:center;gap:56px">
    <div>
      <div style="display:flex;align-items:baseline;gap:20px"><span class="rakam" data-sayi-ok="1" style="font-size:140px">%%COMMIT%%</span><span class="soluk" style="font-size:34px">commit<br>%%GUN%% günde</span></div>
      %%GIT_SVG%%
      <p class="soluk" style="font-size:26px;margin-top:10px">Günlük commit sayısı</p>
    </div>
    <div style="display:grid;gap:22px">
      <div class="kart" data-adim="1"><h3 class="vurgu">CLAUDE.md · %%CLAUDE_SATIR%% satır</h3><p style="font-size:30px">Her oturumda okunan çalışma kuralları. Laboratuvarda SOP neyse, kod için o. İş bölümü yazılı: teknik karar açıklanır, klinik karar embriyoloğa sorulur.</p></div>
      <div class="kart" data-adim="2"><h3 class="vurgu">README · %%SURUM%% sürüm girişi</h3><p style="font-size:30px">Her sürümde ne değişti ve neden. Denetim izi.</p></div>
      <div class="kart" data-adim="3"><h3 class="vurgu">%%GOC%% numaralı veri göçü betiği</h3><p style="font-size:30px">Şema değişikliği tek tek, sırayla, tekrar çalıştırılabilir.</p></div>
    </div>
  </div>
  <div class="alt"><span>Kaynak: depo git geçmişi, CLAUDE.md, README.md · ana dosya app.py: %%APP_SATIR%% satır</span><span>6 / 17</span></div>
  <aside class="not">(75 sn) Önce grafik: bu yaklaşımın hızını göstermek için, övünmek için değil. Git geçmişi %%GUN%% gün, %%COMMIT%% commit. [DOĞRULA: bu tarihlerden önceki sürümler git dışında geliştirildiyse bunu söyle.] Sonra asıl mesaj: hız tehlikeli. Hız denetimle birlikte gelmezse hata da hızlı birikir. Denetimi sağlayan üç şey: CLAUDE.md, yani yapay zekâya yazılmış SOP; sürüm günlüğü, yani izlenebilirlik; numaralı göçler, yani tekrarlanabilirlik. Embriyolog bu üçünü zaten biliyor; adları değişti. [DOĞRULA: yapay zekâ aracının adı ve hangi sürümden itibaren kullanıldığı; CLAUDE.md v6.1’i “Claude Code dönemi” olarak işaretliyor.]</aside>
</section>

<!-- 7 HATA: HAYALET OOSİT -->
<section class="slayt" data-sure="60" data-baslik="Sessiz hata">
  <div class="kicker">Yakalanan hata · v6.19</div>
  <h2>Sessiz hata: hayalet oosit, oranın paydasını şişirir</h2>
  <div class="izgara i2" style="align-items:center;gap:48px">
    <div>
<pre>sid = goruntuler.specimen_olustur(...)   <span class="h"># önce oosit açılır</span>
goruntuler.goruntu_bagla(im, ..., sid)   <span class="h"># sonra kare bağlanır</span></pre>
      <p style="margin-top:34px;font-size:36px">Aynı kare iki kez gönderilince ikinci bağlama reddediliyor, ama açılmış oosit kalıyordu. Ne hata, ne uyarı.</p>
      <p class="soluk" style="margin-top:22px;font-size:30px">«Oosit sayısı klinik bir sayıdır.» · sürüm günlüğü</p>
    </div>
    <div class="kart">
      <div class="soluk" style="font-size:24px;letter-spacing:.1em;font-weight:700">ÖRNEK HESAP · kurgusal sayılar</div>
      <div id="ooSahne" class="ooo"></div>
      <div class="lej"><span><i style="background:var(--vurgu)"></i>2PN</span><span><i style="background:var(--metin)"></i>2PN değil</span><span><i style="border:3px dashed var(--soluk)"></i>hayalet</span></div>
      <div style="display:flex;gap:16px;margin:18px 0"><button class="dugme ikincil" id="ooEksi">− hayalet</button><button class="dugme" id="ooArti">+ hayalet oosit</button></div>
      <div class="soluk" style="font-size:26px">Fertilizasyon oranı = 2PN / oosit</div>
      <div class="rakam" id="ooOran" data-sayi-ok="1" style="font-size:120px">70.0 %</div>
    </div>
  </div>
  <div class="alt"><span>Düzeltme: bağlanamayan kare açılan oositi geri alır; sebep ekranda yazar</span><span>7 / 17</span></div>
  <aside class="not">(60 sn) Hata ne? Çift dokunmada fotoğrafsız bir oosit kalıyordu. Neden önemli? Bu bir güvenlik açığı değil, bir istatistik hatası: payda şişiyor, oran sessizce düşüyor. Düğmeye bas: 10 gerçek oosit, 7 tanesi 2PN; iki hayalet gelince %70, %58’e iniyor. Hiç hata mesajı yok. Bu yüzden düzeltme sadece hatayı kapatmadı; sebebi ekrana yazdı ve yalnızca fotoğrafsız VE olaysız oositi geri aldı, bilerek açılmış boş oosite dokunmadı. Ders: yapay zekâ kodu hızlı yazar ama bu hatayı kullanıcı, yani klinik bilgisi olan biri, yakaladı ve “oosit sayısı klinik bir sayıdır” diye yaptırdı. Yani doğrulayan insan klinik uzmanıydı. (İstersen v6.15 rol açığını da bir cümleyle an: tanımsız rol, tek tıkla yönetici.)</aside>
</section>

<!-- 8 GÖÇ DOĞRULAMASI -->
<section class="slayt" data-sure="45" data-baslik="Göç doğrulaması">
  <div class="kicker">Veri göçü · Access → SQLite</div>
  <h2>Doğrulanmamış veri modellenmez</h2>
  <div class="izgara i3" style="gap:32px;align-items:start">
    <div class="kart" data-adim="1"><div class="rakam" style="font-size:96px">1</div><h3>Deneme kopyası</h3><p style="font-size:34px">Önce kopyada çalıştır, sonra gerçek makinede.</p></div>
    <div class="kart" data-adim="2"><div class="rakam" style="font-size:96px">2</div><h3>Birebir sayım</h3><p style="font-size:34px">2018 aktarımı: <b data-sayi-ok="1">918</b> tedavi, <b data-sayi-ok="1">0</b> hata, <b data-sayi-ok="1">11</b> uyarı; deneme kopyasıyla birebir.</p></div>
    <div class="kart" data-adim="3"><div class="rakam" style="font-size:96px">3</div><h3>Uyarılar tek tek</h3><p style="font-size:34px">2019–2023 (<b data-sayi-ok="1">53</b> aylık dosya): <b data-sayi-ok="1">5 494</b> tedavi, <b data-sayi-ok="1">18</b> uyarı. Her uyarı elle incelendi.</p></div>
  </div>
  <div class="kart" data-adim="4" style="margin-top:40px;border-color:var(--vurgu)"><p style="font-size:40px">Ağustos 2018’de laboratuvarda işlem yapılmadı: veri <span class="vurgu">“0” değil, “boş ay”</span> olarak kodlandı.</p></div>
  <div class="alt"><span>Kaynak: CLAUDE.md ve README (v6.172, v6.173, v6.174)</span><span>8 / 17</span></div>
  <aside class="not">(45 sn) Bu sahne “bu veriyle model eğitmeden önce veriye güvenmek gerek” der. Üç adım, iki sayı. Asıl cümle son satır: eksik ile sıfır ayrımı; üçüncü sahnedeki “eksik ≠ normal” kartının canlı örneği. [DOĞRULA: bu sayıları README’deki sürüm notlarından tekrar oku; sunumdan hemen önce.]</aside>
</section>

<!-- 9 HİYERARŞİ -->
<section class="slayt" data-sure="90" data-baslik="Hiyerarşi">
  <div class="kicker">İstatistik · kancanın cevabı</div>
  <h2>Hayır: %%N_EMB%% embriyo, yaklaşık %%ETKIN%% bağımsız gözlem kadar bilgi taşıyor</h2>
  <div class="izgara i2" style="align-items:start;gap:48px">
    <div>
      <div class="kart">
        <label style="font-size:28px">Hasta içi korelasyon ρ = <b id="rhoD">%%RHO%%</b></label><br>
        <input id="rho" type="range" min="0" max="0.5" step="any" value="%%RHO_TAM%%" style="margin:14px 0 26px"><br>
        <label style="font-size:28px">Hasta başına embriyo m = <b id="mD">%%M_ORT%%</b></label><br>
        <input id="m" type="range" min="1" max="12" step="any" value="%%M_TAM%%" style="margin-top:14px">
      </div>
      <div class="soluk" style="font-size:26px;margin-top:26px">Tasarım etkisi = 1 + (m − 1) · ρ</div>
      <div class="rakam" id="deff" data-sayi-ok="1">%%DEFF%%</div>
      <p class="soluk" style="font-size:26px">Etkin örneklem ≈ n / tasarım etkisi</p>
    </div>
    <div data-adim="1">
      <img class="sekil" src="analiz/sonuc_slayt/fig_ci_naif_vs_gee.svg" alt="Naif ve GEE güven aralıkları">
      <p style="font-size:28px;margin-top:14px">Yaşta GEE aralığı <b>%%YAS_ORAN%%×</b> geniş. Embriyo içi değişkenlerde fark yok (%%FRAG_ORAN%%×, %%MORF_ORAN%%×).</p>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  <div class="alt"><span>%%KUNYE%% · naif lojistik vs GEE (exchangeable)</span><span>9 / 17</span></div>
  <aside class="not">(90 sn) Kancanın cevabı: bağımsız değil. Sliderlara dokun: bu veride ρ yaklaşık %%RHO2%%, hasta başına %%M_ORT%% embriyo; tasarım etkisi %%DEFF%%. Yani %%N_EMB%% embriyo, yaklaşık %%ETKIN%% bağımsız embriyo kadar bilgi. ρ ve m arttıkça etki büyür; IVF’de m genelde birden büyük, çünkü çok embriyo üretiyoruz. Sonra şekli aç: aynı veri, iki varsayım. Dürüst nüans: GEE güven aralığı yalnız hasta düzeyinde sabit olan değişkende, yaşta, geniş çıkıyor (%%YAS_ORAN%% kat). Embriyo içi değişkenlerde fark yok. Yani “her şey şişer” demiyoruz, “hangisinin şiştiğini bilmek gerekir” diyoruz. Bu sentetik veri; gerçek etki büyüklüğü verinize bağlı.</aside>
</section>

<!-- 10 SIZINTI -->
<section class="slayt" data-sure="90" data-baslik="Sızıntı">
  <div class="kicker">Model eğitme · gradyan artırma</div>
  <h2>İki satır değişti, AUC’nin anlamı değişti</h2>
  <div class="izgara i2" style="align-items:center;gap:48px">
    <div>
<pre id="kodA">cv = <span class="h">KFold(5, shuffle=True)</span>
for tr, te in cv.split(X, y):
    model.fit(X[tr], y[tr])
    p[te] = model.predict_proba(X[te])[:, 1]</pre>
<pre id="kodB" style="display:none">cv = <span class="h">GroupKFold(5)</span>
for tr, te in cv.split(X, y, <span class="h">groups=hasta_id</span>):
    model.fit(X[tr], y[tr])
    p[te] = model.predict_proba(X[te])[:, 1]</pre>
      <div style="display:flex;gap:16px;margin-top:28px"><button class="dugme" id="bolA">Rastgele bölme</button><button class="dugme ikincil" id="bolB">Hasta-gruplu bölme</button></div>
    </div>
    <div>
      <div class="soluk" style="font-size:28px" id="aucEtiket">Rastgele bölme: aynı hastanın embriyoları iki tarafta</div>
      <div class="rakam" id="aucDeger" data-sayi-ok="1" style="font-size:200px">%%G_R%%</div>
      <p class="soluk" style="font-size:28px" id="aucNot">AUC · fark: yok, sızıntılı</p>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  <div class="alt"><span>%%KUNYE%% · gradyan artırma</span><span>10 / 17</span></div>
  <aside class="not">(90 sn) Soldaki kod: standart rastgele bölme, her kütüphanenin örneği. Sağda AUC %%G_R%%. Düğmeye bas: aynı model, aynı veri, bölme hastaya göre: AUC %%G_G%%, aradaki fark %%FARK%%. Neden? BMI hastaya özgü bir sayı ve nedensel etkisi yok. Rastgele bölmede aynı hastanın kardeş embriyoları hem eğitimde hem testte; gradyan artırma BMI’dan hastayı tanıyıp onun gizli kalitesini ezberliyor. Gerçek dünyada yeni hasta geldiğinde bu bilgi yok. Bu AUC hastanın kendisini bilen bir modelin AUC’si, yeni hastayı değil. Hasta düzeyinde sızıntıyı kapatan tek şey groups=hasta_id.</aside>
</section>

<!-- 11 BASİT MODEL -->
<section class="slayt" data-sure="45" data-baslik="Basit model">
  <div class="kicker">Model eğitme · baseline</div>
  <h2>Basit model, doğru doğrulamada karmaşık olanı geçti</h2>
  <div class="izgara i2" style="align-items:center;gap:48px;grid-template-columns:1.25fr 1fr">
    <img class="sekil" src="analiz/sonuc_slayt/fig_auc_dogrulama.svg" alt="AUC doğrulama şeması karşılaştırması">
    <div style="display:grid;gap:18px">
      <div class="kart" data-adim="1"><h3>Lojistik regresyon</h3><p style="font-size:30px">%%L_R%% → <b>%%L_G%%</b> (GA %%L_GA%%)</p></div>
      <div class="kart" data-adim="2"><h3>Gradyan artırma</h3><p style="font-size:30px">%%G_R%% → <b>%%G_G%%</b> (GA %%G_GA%%)</p></div>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  <div class="alt"><span>%%KUNYE%% · GA: hasta düzeyinde küme bootstrap (300 tekrar), hasta-gruplu tahminler</span><span>11 / 17</span></div>
  <aside class="not">(45 sn) Üç doğrulama şeması, iki model. Lojistik regresyon sızıntıdan neredeyse etkilenmiyor (%%L_R%%, %%L_G%%); gradyan artırma etkileniyor ve gruplu doğrulamada lojistiğin gerisinde (%%G_G%%, %%L_G%%; aralıklar ayrışıyor). Zamansal bölmede de aynı sıra. Mesaj: karmaşık model bir şey kazandırıyorsa bunu doğru doğrulamada göstermek zorunda. Yoksa baseline’ı seç. Bu, sentetik bir senaryoda; verinin yapısı doğrusal olduğu için lojistik avantajlı olabilir. Gerçek veride sonuç farklı çıkabilir, soru aynı kalır.</aside>
</section>

<!-- 12 KALİBRASYON -->
<section class="slayt" data-sure="75" data-baslik="Kalibrasyon">
  <div class="kicker">Model eğitme · zamansal doğrulama</div>
  <h2>Ayırt etme iyi kalır, kalibrasyon bozulur: model 2023 sonrasını düşük tahmin ediyor</h2>
  <div class="izgara i2" style="align-items:center;gap:56px;grid-template-columns:.85fr 1fr">
    <img class="sekil" src="analiz/sonuc_slayt/fig_kalibrasyon.svg" alt="Kalibrasyon eğrisi" style="max-height:600px;width:auto">
    <div style="display:grid;gap:20px">
      <div class="kart" data-adim="1"><h3>Kalibrasyon eğimi %%EGIM%% · ofset +%%OFSET%%</h3><p style="font-size:30px">Eğri çizginin üstünde: gözlenen oran, öngörülenden yüksek.</p></div>
      <div class="kart" data-adim="2"><h3 class="vurgu">Bilinen gerçek: +%%KAYMA%%</h3><p style="font-size:30px">Sentetik veride 2023 sonrası kültür iyileşmesini biz koyduk (log-odds). Model bunu bilmiyor.</p></div>
      <div class="kart" data-adim="3"><h3>Zamansal AUC %%L_Z%%</h3><p style="font-size:30px">Sıralama korunuyor; olasılıklar yanlış.</p></div>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  <div class="alt"><span>%%KUNYE%% · eğitim: 2023.5 öncesi, test: sonrası · lojistik regresyon · Brier %%BRIER%%</span><span>12 / 17</span></div>
  <aside class="not">(75 sn) Kalibrasyon en çok ihmal edilen metrik. Model ürettiği %%L_Z%% AUC ile iyi sıralıyor ama “%%OFSET%%” ofset sistematik bir düşük tahmin demek: kültür sistemi iyileşti, model eski dünyayı biliyor. Sentetik verinin güzelliği şu: gerçek kayma %%KAYMA%% ve bunu biz biliyoruz; kalibrasyon ofseti yaklaşık o büyüklükte. Yöntem doğru çalışıyor. Klinik sonuç: embriyoya olasılık veriyorsanız ve bu olasılık “gebelik şansı” olarak okunuyorsa, kayma varken tehlikelidir; AUC bunu söylemez, kalibrasyon söyler. İnkübatör değişince modeli yeniden doğrulayın.</aside>
</section>

<!-- 13 KARAR EĞRİSİ -->
<section class="slayt" data-sure="45" data-baslik="Karar eğrisi">
  <div class="kicker">Model eğitme · klinik fayda</div>
  <h2>Doğruluk değil, fayda: hangi eşikte hangi eylem?</h2>
  <div class="izgara i2" style="align-items:center;gap:56px;grid-template-columns:1.1fr 1fr">
    <img class="sekil" src="analiz/sonuc_slayt/fig_dca.svg" alt="Karar eğrisi analizi">
    <div style="display:grid;gap:20px">
      <div class="kart" data-adim="1"><p>Bu veride model, “hepsini seç” stratejisinin üstünde: eşik <b>%%DCA_MIN%%–%%DCA_MAX%%</b> aralığının tamamında.</p></div>
      <div class="kart" data-adim="2"><p>Eşik matematikten değil, <span class="vurgu">klinikten</span> gelir: kaçırılan blastokist ile gereksiz çözme arasındaki takas.</p></div>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  <div class="alt"><span>%%KUNYE%% · hasta-gruplu tahminler · lojistik regresyon</span><span>13 / 17</span></div>
  <aside class="not">(45 sn) Karar eğrisi analizi net fayda hesaplar: doğru pozitifler eksi yanlış pozitifler çarpı eşik oranı. Üç strateji: modeli kullan, hepsini seç, hiçbirini seçme. Bu sentetik veride model her eşikte üstte; gerçek veride böyle olmak zorunda değil. Asıl soru: kliniğin kabul edeceği eşik ne? Bunu istatistikçi değil embriyolog ve hasta belirler. Model eşik söylemez; eşik koyunca fayda hesaplanır.</aside>
</section>

<!-- 14 ÖZERKLİK MERDİVENİ -->
<section class="slayt" data-sure="75" data-baslik="Entegrasyon">
  <div class="kicker">Laboratuvar iş akışına entegrasyon</div>
  <h2>Entegrasyon, merdivende bir basamak seçmektir</h2>
  <div class="merdiven" id="mer"></div>
  <p class="soluk" style="font-size:24px;margin-top:22px">Bir basamağa dokun.</p>
  <div class="kart" id="merDetay" style="margin-top:12px"></div>
  <div class="alt"><span>Çerçeve: bu sunumun önerisi · Patient Data Center programda: 1–3. basamaklar</span><span>14 / 17</span></div>
  <aside class="not">(75 sn) Beş basamak. Her basamak için üç soru: kabul kriteri ne, denetim izi nerede, kimin sorumluluğu. Patient Data Center bugün 1’den 3’e: kayıt, betimsel istatistik ve kural tabanlı uyarı, örneğin fertilizasyon kontrolünde hedef saatten iki saatten fazla sapınca ekran turuncuya dönüyor ya da gün 2/3 otomatik skoru. Model önerisi, 4. basamak, bu sunumun araştırma katmanı; programda yok. 5. basamak, yani otomatik karar, önerilmiyor. Basamak yükseldikçe kabul kriteri ağırlaşır: 4. basamak için hasta-gruplu ve zamansal doğrulama, kalibrasyon, alt grup performansı gerekir; bunu sahne 10-13’te gördünüz.</aside>
</section>

<!-- 15 SINIRLAR VE ETİK -->
<section class="slayt" data-sure="50" data-baslik="Sınırlar ve etik">
  <div class="kicker">Sınırlar</div>
  <h2>Bu sunumun söylemediği şeyler de var</h2>
  <div class="sinir">
    <p data-adim="1"><b>Sentetik ≠ klinik.</b> Her şekil sentetik veridir; bulgu değil, yöntem doğrulaması.</p>
    <p data-adim="2"><b>Program karar vermez.</b> Patient Data Center bir kayıt ve betimsel istatistik aracıdır. Araştırma amaçlıdır, klinik kararı yönlendirmez.</p>
    <p data-adim="3"><b>Yapay zekâ kodu yanılır.</b> Hataları insan buldu (sahne 7). Kod ve analiz yapay zekâ yardımıyla yazıldı, insan tarafından çalıştırıldı ve doğrulandı.</p>
    <p data-adim="4"><b>Hasta verisi yok.</b> Bu sunumda hiçbir gerçek hasta verisi, görüntü ya da kimlik bilgisi kullanılmadı.</p>
  </div>
  <div class="alt"><span>Mevzuat (KVKK, tıbbi cihaz, yapay zekâ düzenlemeleri) için kurumunuzun etik kurulu ve hukuk birimine danışın</span><span>15 / 17</span></div>
  <aside class="not">(50 sn) Sakin, düz bir slayt. Her satır tek cümle. Üçüncü satır aynı zamanda yapay zekâ kullanım beyanı. Dördüncü satır: hiçbir gerçek hasta verisi yok; dinleyici “bunu kendi verimde denesem” diye düşünürse cevap: etik onay ve veri sorumlusu süreci; ben burada onu yapmadım. Mevzuat konusunda kesin konuşma, çerçeve çiz.</aside>
</section>

<!-- 16 ÜÇ MESAJ -->
<section class="slayt" data-sure="45" data-baslik="Üç mesaj">
  <div class="kicker">Eve götürülecekler</div>
  <h2>Üç cümle</h2>
  <div class="mesajlar">
    <div data-adim="1"><span class="no">1</span><p>Embriyo bağımsız değildir: birimi ve kümeyi <b>baştan</b> tanımla.</p></div>
    <div data-adim="2"><span class="no">2</span><p>Doğrulama şeması sonucu belirler: <b>hasta düzeyinde, zamansal, kalibrasyonla.</b></p></div>
    <div data-adim="3"><span class="no">3</span><p>Önce veri, sonra model. Yapay zekâya <b>SOP yaz</b>, çıktısını doğrula.</p></div>
  </div>
  <div class="alt"><span>Sonraki adım: gerçek veride uygulama ayrı bir çalışmadır; etik onay ve harici doğrulama gerektirir</span><span>16 / 17</span></div>
  <aside class="not">(45 sn) Üç cümleyi sırayla oku, her birinin hangi sahneden geldiğini söyle: 1 → 9, 2 → 10-12, 3 → 6-7. Yol haritası tek cümle: bu yöntemi gerçek veride denemek ayrı bir çalışma, etik onay ve çok merkezli doğrulama ister.</aside>
</section>

<!-- 17 TEKRARLANABİLİRLİK -->
<section class="slayt" data-sure="25" data-baslik="Tekrarlanabilirlik">
  <div class="kicker">Tekrarlanabilirlik</div>
  <h2>Bu sunumdaki her sayı bir betikten gelir</h2>
  <div class="izgara i2" style="align-items:start;gap:56px">
    <div>
<pre>python3 sentetik_veri.py --seed %%SEED%%
python3 analiz_demo.py --slayt</pre>
      <p class="soluk" style="margin-top:24px;font-size:28px">Sentetik kohort, analiz kodu ve <code>sonuclar.json</code> kodla birlikte paylaşılır. Gerçek parametreler kodda yazılıdır; yöntemin doğruluğu sınanabilir.</p>
    </div>
    <div class="kart"><h3>Teşekkürler</h3><p class="soluk" style="margin-top:12px">[Ad Soyad] · [Kurum]<br>[e-posta]<br>[kod deposu bağlantısı]</p></div>
  </div>
  <div class="alt"><span>Soru ve tartışma</span><span>17 / 17</span></div>
  <aside class="not">(25 sn) Kod ve veri bağlantısını göster, teşekkür et, soruya geç. [YAPILACAK: depo bağlantısı ve iletişim bilgileri. Kod deposunu yayımlamadan önce sentetik veriyi ve betikleri ayrı bir depoya koy; Patient Data Center deposuyla karıştırma.]</aside>
</section>

<!-- YEDEK A -->
<section class="slayt" data-sure="0" data-baslik="Yedek: GEE ve GLMM">
  <div class="kicker">Yedek · soru gelirse</div>
  <h2>Neden GEE? GLMM ile farkı ne?</h2>
  <div class="izgara i2" style="align-items:start;gap:40px">
    <div class="kart"><h3 class="vurgu">GEE</h3><ul><li>Popülasyon ortalaması etkisi</li><li>Çalışma korelasyonu yanlış olsa bile dayanıklı SE</li><li>Az küme (&lt;30-40) için düzeltme gerekir</li></ul></div>
    <div class="kart"><h3 class="vurgu">GLMM</h3><ul><li>Hasta/siklus’a özgü (koşullu) etki</li><li>İç içe düzeyler doğal (hasta ⊃ siklus)</li><li>OR yorumu koşullu; GEE’den farklı olabilir</li></ul></div>
  </div>
  <aside class="not">Yedek. “Neden GEE seçtiniz?” sorusuna: soru popülasyon düzeyindeyse (“yaş arttıkça ortalama blastulasyon nasıl değişir”) GEE; hastaya özgü soruysa GLMM. İkisini karşılaştırmak sağlamlık analizidir. Bu demoda yalnız GEE var; GLMM sonuçları hazır değil.</aside>
</section>

<!-- YEDEK B -->
<section class="slayt" data-sure="0" data-baslik="Yedek: hakem soruları">
  <div class="kicker">Yedek · soru gelirse</div>
  <h2>Beklenen beş soru</h2>
  <div class="sinir" style="font-size:30px">
    <p><b>Gerçek veride denediniz mi?</b> Hayır; bu sunum yöntem doğrulamasıdır, gerçek veri ayrı çalışma.</p>
    <p><b>Program klinik karar veriyor mu?</b> Hayır; kayıt ve betimsel istatistik.</p>
    <p><b>Yapay zekâ yazdığı koda nasıl güveniyorsunuz?</b> Güvenmiyoruz; SOP, sürüm günlüğü, test ve klinik doğrulama.</p>
    <p><b>Başka merkezde çalışır mı?</b> Ölçmedik; tek merkez, harici doğrulama yok.</p>
    <p><b>Eksik veri?</b> Mekanizma ayrımı veri tasarımında; çoklu atama ayrı çalışmada.</p>
  </div>
  <aside class="not">Yedek. Bilmediğin yerde “bunu ölçmedik” demek doğru cevaptır.</aside>
</section>
'''

# ======================================================================
EK_CSS = r'''
/* --- Bu sunuma özgü bileşenler --- */
.hat{display:flex;gap:8px;margin-top:34px}
.asama{flex:1;padding:26px 2px;border:2px solid var(--cizgi);border-radius:14px;font:600 22px var(--font-metin);text-align:center;cursor:pointer;background:var(--kart);color:var(--metin);transition:all .2s;white-space:nowrap}
.asama.bilinen{background:var(--metin);color:var(--zemin);border-color:var(--metin)}
.asama.simdi{background:var(--vurgu);border-color:var(--vurgu);color:#fff}
.asama.sonra{opacity:.42}
.kararlar{display:grid;gap:0;margin-top:0}
.karar{display:grid;grid-template-columns:1.25fr 1fr;gap:56px;padding:13px 0;border-top:2px solid var(--cizgi);align-items:center}
.karar .sol{font-size:29px;line-height:1.3}.karar .sol em{display:block;font:600 20px var(--font-metin);color:var(--soluk);margin-top:6px;font-style:normal;letter-spacing:.04em}
.karar .sag{font-size:29px;line-height:1.3;color:var(--vurgu);font-weight:600}
.ooo{display:flex;flex-wrap:wrap;gap:12px;margin:20px 0;min-height:140px}
.ooo i{width:62px;height:62px;border-radius:50%;background:var(--metin);display:inline-block;position:relative}
.ooo i.ikipn{background:var(--vurgu)}
.ooo i.hayalet{background:transparent;border:3px dashed var(--soluk)}
.merdiven{display:grid;gap:10px;margin-top:22px}
.basamak{display:grid;grid-template-columns:70px 1fr auto;gap:22px;align-items:center;padding:11px 22px;border:2px solid var(--cizgi);border-radius:14px;background:var(--kart);cursor:pointer;font-size:30px;transition:all .2s}
.basamak .n{font:700 34px var(--font-baslik);color:var(--vurgu)}
.basamak .pdc{font:700 20px var(--font-metin);letter-spacing:.08em;padding:4px 12px;border-radius:8px;border:2px solid var(--metin)}
.basamak.sec{background:var(--metin);color:var(--zemin);border-color:var(--metin)}
.basamak.sec .n{color:var(--zemin)}.basamak.sec .pdc{border-color:var(--zemin)}
.sinir p{margin-bottom:26px;font-size:34px}
.mesajlar{display:grid;gap:34px;margin-top:30px}
.mesajlar>div{display:grid;grid-template-columns:100px 1fr;align-items:center;gap:24px}
.mesajlar .no{font:700 120px/1 var(--font-baslik);color:var(--vurgu)}
.mesajlar p{font-size:46px;line-height:1.25;max-width:1400px}
ul{padding-left:30px}
h2{margin-bottom:30px}
img.sekil{width:100%;height:auto}
.sinir{margin-top:36px}
.lej{display:flex;gap:26px;font-size:24px;color:var(--soluk);margin-top:6px;flex-wrap:wrap}
.lej i{display:inline-block;width:22px;height:22px;border-radius:50%;vertical-align:-4px;margin-right:8px}
code{font:500 .85em var(--font-kod);background:var(--kod);padding:2px 8px;border-radius:6px}
'''

EK_JS = r'''
<script>
(function(){
function bl(e){e.currentTarget.blur();}
/* Sahne 4: iş akışı hattı */
var ASAMA=[
 {ad:'OPU',alan:['Oositlerin toplanması, sikluse bağlanması']},
 {ad:'Denüdasyon',alan:['Oosit kaydı açılır','Kamera karesi oosite bağlanır','Toplandığı over (sağ/sol)']},
 {ad:'ICSI',alan:['Maturasyon: MII / MI / GV / dejenere / atretik','Oosit bulguları (kalın zona, SER kümesi…)','Enjeksiyon yapıldı/yapılmadı, geçiş zorluğu, sonuç']},
 {ad:'Fert. kontrol',alan:['Sonuç: normal / dejenere / kayıp','Pronükleus sayısı (0–4PN), PN skoru Z1–Z4','Zigot bulguları; ICSI’den bu yana geçen saat']},
 {ad:'Gün 2/3',alan:['Hücre sayısı, fragmantasyon (%), simetri','Bulgular: multinükleasyon, vakuol','Skor (otomatik ya da “elle”), işlem saati']},
 {ad:'Blastokist',alan:['Genişleme 1–6, ICM A/B/C, TE A/B/C','Skor (ör. 4AA); gün 5, 6, 7 ayrı kayıt','Morula / arrest durumları']},
 {ad:'Vitrifikasyon',alan:['Taşıyıcı: etiket, tip, renk','Konum: tank / kanister / goblet / pozisyon','Dondurma saati']},
 {ad:'Çözme',alan:['Embriyo başına sağkalım: canlı / dejenere / kısmi hasar','Re-expansion (%)','Hangi tedavi için çözüldüğü']},
 {ad:'Transfer',alan:['Taze / donmuş ayrımı kayıttan çıkar','Embriyonun geldiği siklus ≠ transfer siklusu']},
 {ad:'Gebelik',alan:['Beta hCG (ham değerler, zaman damgalı)','Klinik gebelik, kese sayısı, fetal kalp','Sonlanma: canlı doğum, abortus, biyokimyasal, ektopik, devam, takip kaybı']}
];
var hat=document.getElementById('hat');
if(hat){
  var chips=ASAMA.map(function(a,k){var b=document.createElement('div');b.className='asama';b.textContent=a.ad;b.onclick=function(){sec(k);};hat.appendChild(b);return b;});
  function sec(k){
    chips.forEach(function(c,j){c.className='asama '+(j<k?'bilinen':(j===k?'simdi':'sonra'));});
    document.getElementById('hatBaslik').textContent=ASAMA[k].ad+': bu aşamada kaydedilen';
    var ul=document.getElementById('hatAlan');ul.innerHTML='';
    ASAMA[k].alan.forEach(function(t){var li=document.createElement('li');li.textContent=t;li.style.fontSize='34px';li.style.marginBottom='12px';ul.appendChild(li);});
    var sonra=ASAMA.slice(k+1).map(function(a){return a.ad;});
    document.getElementById('hatSonra').textContent=sonra.length?sonra.join(' · '):'Hiçbir şey: sonuç da bilindi. Bu noktada artık tahmin değil, değerlendirme yapılır.';
  }
  sec(4);
}
/* Sahne 7: hayalet oosit */
var oo=document.getElementById('ooSahne');
if(oo){
  var gh=0,GERCEK=10,IKIPN=7;
  function ciz(){
    oo.innerHTML='';
    for(var i=0;i<GERCEK;i++){var e=document.createElement('i');if(i<IKIPN)e.className='ikipn';oo.appendChild(e);}
    for(var j=0;j<gh;j++){var h=document.createElement('i');h.className='hayalet';oo.appendChild(h);}
    document.getElementById('ooOran').textContent=(100*IKIPN/(GERCEK+gh)).toFixed(1)+' %';
  }
  document.getElementById('ooArti').onclick=function(e){if(gh<6)gh++;ciz();bl(e);};
  document.getElementById('ooEksi').onclick=function(e){if(gh>0)gh--;ciz();bl(e);};
  ciz();
}
/* Sahne 9: tasarım etkisi slider */
var rho=document.getElementById('rho'),m=document.getElementById('m');
if(rho&&m){
  function hes(){document.getElementById('rhoD').textContent=(+rho.value).toFixed(3);
    document.getElementById('mD').textContent=(+m.value).toFixed(2);
    document.getElementById('deff').textContent=(1+(m.value-1)*rho.value).toFixed(2);}
  rho.oninput=hes;m.oninput=hes;hes();
}
/* Sahne 10: bölme düğmesi */
var A=document.getElementById('bolA'),B=document.getElementById('bolB');
if(A&&B){
  function bolme(g,e){
    document.getElementById('kodA').style.display=g?'none':'block';
    document.getElementById('kodB').style.display=g?'block':'none';
    document.getElementById('aucDeger').textContent=g?'%%G_G%%':'%%G_R%%';
    document.getElementById('aucEtiket').textContent=g?'Hasta-gruplu bölme: hasta yalnız bir tarafta':'Rastgele bölme: aynı hastanın embriyoları iki tarafta';
    document.getElementById('aucNot').textContent=g?'AUC · aradaki fark %%FARK%%':'AUC · sızıntılı';
    A.className=g?'dugme ikincil':'dugme';B.className=g?'dugme':'dugme ikincil';
    if(e)e.currentTarget.blur();
  }
  A.onclick=function(e){bolme(false,e);};B.onclick=function(e){bolme(true,e);};
}
/* Sahne 14: özerklik merdiveni */
var BAS=[
 {ad:'Kayıt',pdc:'PROGRAMDA',kabul:'Alan tanımları, zorunlu alanlar, tutarlılık kontrolü',iz:'Değişiklik günlüğü (kim, ne zaman, neyi)',sor:'Laboratuvar sorumlusu'},
 {ad:'Betimsel istatistik',pdc:'PROGRAMDA',kabul:'Pay ve payda tanımı yazılı; oranlar kayıttan yeniden üretilebilir',iz:'Ay/yıl seçici, aynı kayıttan her açılışta aynı sayı',sor:'Laboratuvar sorumlusu'},
 {ad:'Kural tabanlı uyarı',pdc:'PROGRAMDA',kabul:'Kural açıkça yazılı ve değiştirilebilir (ör. hedef saatten sapma, otomatik skor kuralı)',iz:'“Otomatik” ve “elle” skor ayrı işaretlenir',sor:'Embriyolog'},
 {ad:'Model önerisi (insan karar verir)',pdc:'ARAŞTIRMA',kabul:'Hasta-gruplu ve zamansal doğrulama, kalibrasyon, alt grup performansı, baseline’ı geçmek',iz:'Öneri ve nihai karar ayrı kaydedilir; sapma izlenir',sor:'Embriyolog + etik kurul onayı'},
 {ad:'Otomatik karar',pdc:'ÖNERİLMEZ',kabul:'Prospektif klinik kanıt, mevzuat uyumu, sürekli izleme',iz:'Tam denetim izi, geri alma yolu',sor:'Kurumsal + yasal sorumluluk'}
];
var mer=document.getElementById('mer');
if(mer){
  var bl_=BAS.map(function(b,k){var d=document.createElement('div');d.className='basamak';
    d.innerHTML='<span class="n">'+(k+1)+'</span><span>'+b.ad+'</span><span class="pdc">'+b.pdc+'</span>';
    d.onclick=function(){bsec(k);};mer.appendChild(d);return d;});
  function bsec(k){
    bl_.forEach(function(d,j){d.classList.toggle('sec',j===k);});
    var b=BAS[k];
    document.getElementById('merDetay').innerHTML=
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:36px;font-size:28px;line-height:1.35">'+
      '<div><b class="vurgu">Kabul kriteri</b><br>'+b.kabul+'</div>'+
      '<div><b class="vurgu">Denetim izi</b><br>'+b.iz+'</div>'+
      '<div><b class="vurgu">Sorumluluk</b><br>'+b.sor+'</div></div>';
  }
  bsec(2);
}
})();
</script>
'''


def derle():
    html = ISKELET.read_text(encoding="utf-8")
    govde = html.index("</head>")                       # başlık yorumundaki etiket adlarına takılma
    bas = html.index('<main id="sahne">', govde) + len('<main id="sahne">')
    son = html.index('<div id="ilerleme">', bas)
    html = html[:bas] + "\n" + SLAYTLAR + "\n" + html[son:]
    html = html.replace("</style>", EK_CSS + "\n</style>", 1)
    # iskeletin örnek slider kodu (sahne 4 örneği) yeni sahnelerde yok; motorun sonundaki blok boş geçer
    html = html.replace("</body>", EK_JS + "\n</body>")
    html = html.replace("<title>SUNUM BAŞLIĞI — Klinik Embriyoloji Kongresi 2027</title>",
                        "<title>Embriyolar bağımsız değildir — Klinik Embriyoloji Kongresi 2027</title>")
    html = html.replace("%%GIT_SVG%%", GIT_SVG).replace("%%KUNYE%%", KUNYE)
    def rep(m):
        k = m.group(1)
        if k not in V:
            raise KeyError(f"tanımsız jeton: {k}")
        return V[k]
    html = re.sub(r"%%([A-Z_0-9]+)%%", rep, html)
    (KOK / "sunum.html").write_text(html, encoding="utf-8")
    # sunucu notları
    notlar = []
    for i, m in enumerate(re.finditer(r'<section class="slayt" data-sure="(\d+)" data-baslik="([^"]*)">.*?<aside class="not">(.*?)</aside>', html, re.S), 1):
        notlar.append(f"## {i}. {m.group(2)}  ({m.group(1)} sn)\n\n{re.sub('<[^>]+>', '', m.group(3)).strip()}\n")
    (KOK / "sunucu_notlari.md").write_text("# Sunucu notları\n\nKonuşma dilinde; köşeli parantezli [DOĞRULA]/[YAPILACAK] satırları sunumdan önce kapatılmalı.\n\n" + "\n".join(notlar), encoding="utf-8")
    print("sunum.html yazıldı;", len(notlar), "sahne notu")


if __name__ == "__main__":
    derle()
