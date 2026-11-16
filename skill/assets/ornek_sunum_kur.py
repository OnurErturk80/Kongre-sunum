#!/usr/bin/env python3
"""
Sunum v2: "Ham değil, kişisel yapay zekâ" — embriyoloğun kendi tecrübesiyle kişiselleştirdiği yapay zekâ.
Sayılar yalnızca analiz/*.json, analiz/literatur_sayilar.json ve git log'dan gelir.
Çalıştır:  python3 kur_sunum_v2.py  ->  sunum.html, sunucu_notlari.md, analiz/tum_sayilar.json
"""
import json, re, subprocess, collections, pathlib, datetime as dt

KOK = pathlib.Path(__file__).parent
ISKELET = pathlib.Path("/home/claude/embriyoloji-ai-kongre-sunumu/assets/deck_iskelet.html")
REPO = pathlib.Path("/home/claude/Patient-Data-Center")
A = KOK / "analiz"
SZ = json.load(open(A / "sonuc_slayt/sonuclar.json", encoding="utf-8"))
KP = json.load(open(A / "sonuc_kpi/sonuclar_kpi.json", encoding="utf-8"))
GR = json.load(open(A / "sonuc_gorsel/sonuclar_gorsel.json", encoding="utf-8"))
LT = json.load(open(A / "literatur_sayilar.json", encoding="utf-8"))
NB = "\u202f"


def binlik(n): return f"{int(round(n)):,}".replace(",", NB)
def f(x, d=2): return f"{x:.{d}f}"
def yz(x, d=1): return f"%{x*100:.{d}f}"          # 0.966 -> %96.6


# ---------- depo (git) ----------
gun = subprocess.run(["git", "-C", str(REPO), "log", "--format=%ad", "--date=short"], capture_output=True, text=True).stdout.split()
say = collections.Counter(gun); gl = sorted(say)
d0, d1 = dt.date.fromisoformat(gl[0]), dt.date.fromisoformat(gl[-1])
tum = [d0 + dt.timedelta(days=i) for i in range((d1 - d0).days + 1)]
mx = max(say.values()); W, H = 1000, 260; bw = W / len(tum)
cub = "".join(f'<rect x="{i*bw+2:.1f}" y="{H-(say.get(d.isoformat(),0)/mx)*(H-20):.1f}" width="{bw-4:.1f}" height="{(say.get(d.isoformat(),0)/mx)*(H-20):.1f}" rx="3" fill="var(--vurgu)"/>' for i, d in enumerate(tum))
GIT_SVG = (f'<svg viewBox="0 0 {W} {H+34}" style="width:100%;height:auto" role="img" aria-label="Günlük commit">{cub}'
           f'<text x="0" y="{H+28}" fill="var(--soluk)" font-size="24">{d0.day} Eylül</text>'
           f'<text x="{W}" y="{H+28}" text-anchor="end" fill="var(--soluk)" font-size="24">{d1.day} Ekim 2026</text></svg>')
sm = subprocess.run(["bash", "-c", f"wc -l < {REPO}/CLAUDE.md; grep -c '^# v[0-9]' {REPO}/README.md"], capture_output=True, text=True).stdout.split()
DEPO = dict(commit=len(gun), gun=(d1 - d0).days + 1, claude_satir=int(sm[0]), surum=int(sm[1]))

eu, mc, fu = KP["erken_uyari"], KP["monte_carlo"], KP["funnel"]
ia, qc = GR["ince_ayar"], GR["kalite_kontrol"]
il, sa, ba, bm, hu, al = (LT[k] for k in ["illingworth_2024", "salih_2023", "barnes_2023", "bamford_2023", "huang_2023", "alsaad_2025"])
E_, F_ = fu["embriyologlar"]["E"], fu["embriyologlar"]["F"]

V = dict(
    COMMIT=str(DEPO["commit"]), GUN=str(DEPO["gun"]), CLAUDE_SATIR=binlik(DEPO["claude_satir"]), SURUM=str(DEPO["surum"]),
    # KPI
    DUSUS=f(eu["dusus_puan"], 0), TABAN=yz(eu["gercek_taban"], 0), KAYMA=yz(eu["gercek_kayma_sonrasi"], 0),
    IZLEME=str(mc["izleme_suresi_hafta"]), TEKRAR=str(mc["tekrar"]),
    SH_YAK=yz(mc["shewhart"]["yakalama_orani"]), SH_MED=f(mc["shewhart"]["medyan_gecikme_hafta"], 0),
    CU_YAK=yz(mc["cusum"]["yakalama_orani"]), CU_MED=f(mc["cusum"]["medyan_gecikme_hafta"], 0),
    SH_YA=yz(mc["shewhart_yanlis_alarm_orani"]), CU_YA=yz(mc["cusum_yanlis_alarm_orani"]),
    ORNEK_CU=str(eu["cusum_gecikme_hafta"]),
    E_HAM=f(E_["ham"], 3), E_AY=f(E_["ayarli"], 3), F_HAM=f(F_["ham"], 3), F_AY=f(F_["ayarli"], 3), F_N=str(F_["n"]),
    F_YAS=f(F_["yas_ort"], 1), GENEL=f(fu["genel_oran"], 3),
    # görsel
    HAZIR_EV=f(ia["hazir_model_kendi_labinda_auc"]), HAZIR_BIZ=f(ia["auc"][0]),
    Y25=f(ia["auc"][1]), Y100=f(ia["auc"][3]), Y400=f(ia["auc"][5]),
    AUC_DIZI=json.dumps([round(x, 2) for x in ia["auc"]]), N_DIZI=json.dumps(ia["yerel_n"]),
    QC_DEG=str(qc["kamera_degisim_haftasi"]), QC_AL=str(qc["alarm_haftasi"]), QC_IA=str(qc["ince_ayar_haftasi"]),
    QC_ET=str(qc["ince_ayar_etiket_sayisi"]), QC_TAB=f(qc["taban_uyum"]), QC_SON=f(qc["son_8_hafta_uyum"]),
    QC_MIN=f(qc["degisim_sonrasi_en_dusuk"]),
    # sızıntı (ilk demo)
    G_R=f(SZ["auc"]["gbm"]["rastgele"], 3), G_G=f(SZ["auc"]["gbm"]["hasta_gruplu"], 3),
    # literatür
    IL_N=binlik(il["hasta"]), IL_K=str(il["klinik"]), IL_YZ=f"%{il['gebelik_yz']}", IL_MO=f"%{il['gebelik_morfoloji']}",
    IL_RD=f"{il['risk_farki']}".replace("-", "−"), IL_GA=f"{il['ga_alt']} ile {il['ga_ust']}".replace("-", "−"),
    SA_N=str(sa["calisma"]), SA_YZ=f"%{sa['yz_morfoloji_dogruluk']}", SA_EM=f"%{sa['embriyolog_morfoloji_dogruluk']}",
    BA_IC=f"%{ba['ic_dogruluk']}", BA_D1=f"%{ba['dis_dogruluk_1']}", BA_D2=f"%{ba['dis_dogruluk_2']}",
    BM_N=binlik(bm["embriyo"]), BM_LR=f(bm["auc_lojistik"]), BM_RF=f(bm["auc_rf"]), BM_DL=f(bm["auc_derin"]),
    HU_S=f(hu["duyarlilik"]), HU_O=f(hu["ozgulluk"]), HU_N=str(hu["calisma"]),
    AL_N=str(al["calisma"]), AL_D=f"%{al['dogruluk_olcutu_yuzde']}", AL_Y=f"%{al['anne_yasi_yok_yuzde']}",
)

SAHNE_SAY = 18
def alt(sol, no): return f'<div class="alt"><span>{sol}</span><span>{no} / {SAHNE_SAY}</span></div>'

SLAYTLAR = r'''
<!-- 1 BAŞLIK -->
<section class="slayt dz" data-sure="20" data-baslik="Başlık">
  <div class="kicker">Klinik Embriyoloji Kongresi 2027</div>
  <h1>Ham değil,<br><span class="vurgu">kişisel yapay zekâ.</span></h1>
  <p style="margin-top:36px;font-size:44px;max-width:1400px">Embriyoloji laboratuvarında yapay zekâyı kendi tecrübemizle iş akışına katmak</p>
  <div class="ayrac"></div>
  <p class="soluk">[Ad Soyad] · [Kurum]</p>
  <aside class="not">(20 sn) Kısa tanış. “Yirmi yıldır bu laboratuvardayım; bugün size yapay zekâyı nasıl kendi işime göre şekillendirdiğimi anlatacağım” de. Alternatif başlıklar: “Embriyoloğun kendi yapay zekâsı” / “Yapay zekâ embriyoloğun yerini mi alacak, elinde mi büyüyecek?”</aside>
</section>

<!-- 2 YOLCULUK -->
<section class="slayt" data-sure="45" data-baslik="Kâğıttan yapay zekâya">
  <div class="kicker">Yolculuk</div>
  <h2>Her adımda değişen şey: veriyle ne yapabildiğimiz</h2>
  <div class="yol">
    <div class="durak" data-adim="1"><div class="ikon">✎</div><h3>Kâğıt</h3><p>Formlar ve defterler. KPI yıl sonunda elle sayılır.</p></div>
    <div class="durak" data-adim="2"><div class="ikon">▦</div><h3>Bilgisayar</h3><p>Excel ve Access. Veri dijital ama dağınık.</p></div>
    <div class="durak" data-adim="3"><div class="ikon">◎</div><h3>Kendi programımız</h3><p>Aşamaya bağlı kayıt, fotoğraf, iz. KPI her ay otomatik.</p></div>
    <div class="durak vurgu-durak" data-adim="4"><div class="ikon">✦</div><h3>Yapay zekâ</h3><p>Aynı veriyle daha derin istatistik, görüntü analizi, erken uyarı.</p></div>
  </div>
  <aside class="not">(50 sn) Kendi laboratuvarınızın hikâyesi: kâğıt, sonra bilgisayar, sonra kendi programınız. Her duraktan sonra tek cümle: kâğıtta KPI’ya ancak yıl sonunda bakılabiliyordu; bilgisayarda veri vardı ama dağınıktı; şimdi her kayıt aşamasına bağlı ve her ay otomatik oran çıkıyor. Son durak bu konuşmanın konusu: aynı veriyle yapay zekâ ne kadar derine inebilir? [DOĞRULA: kâğıttan bilgisayara geçiş yılını ve Access döneminin başlangıcını kendi cümlenle söyle.]</aside>
</section>

<!-- 3 NEDEN KENDİ ARACIM -->
<section class="slayt" data-sure="50" data-baslik="Neden kendi aracım?">
  <div class="kicker">Neden kendi aracım?</div>
  <h2>Sorunu en iyi, işi yıllarca yapan kişi bilir</h2>
  <div class="izgara i3" style="gap:32px;align-items:start">
    <div class="kart" data-adim="1"><h3 class="vurgu">Sessiz kayıt hatası</h3><p>Hata mesajı vermeyen yanlış sayı en tehlikelisidir.</p></div>
    <div class="kart" data-adim="2"><h3 class="vurgu">İzlenebilirlik</h3><p>Kim, ne zaman, hangi embriyoya, hangi tüpe?</p></div>
    <div class="kart" data-adim="3"><h3 class="vurgu">Güvenlik</h3><p>Erişim, yedek, iki makine arasında kayıpsız taşıma.</p></div>
  </div>
  <p style="margin-top:44px;font-size:40px;max-width:1600px" data-adim="4">Hazır yazılım genel bir laboratuvar için yazılır. Yapay zekâ ile embriyolog, <span class="vurgu">kendi laboratuvarının</span> aracını yapabilir.</p>
  <aside class="not">(50 sn) Üç sorun: bunları hepimiz yaşadık. Vurgu: önlemi en iyi, sorunu yaşayan kişi tanımlar. Yapay zekâ burada kod yazan el; aklı ve ihtiyacı embriyolog getiriyor.</aside>
</section>

<!-- 4 İŞ AKIŞI HATTI -->
<section class="slayt" data-sure="55" data-baslik="İş akışı">
  <div class="kicker">Patient Data Center</div>
  <h2>Her aşama bir kayıt, her kayıt bir önlem</h2>
  <div class="hat" id="hat"></div>
  <div class="izgara i2" style="align-items:start;margin-top:40px;gap:40px">
    <div class="kart" style="padding:40px"><h3 class="vurgu" id="hatBaslik" style="font-size:38px"></h3><ul id="hatAlan" style="margin-top:12px"></ul></div>
    <div class="kart" style="border-color:var(--vurgu);padding:40px"><h3 style="font-size:38px">Bu aşamada önlenen hata</h3><p id="hatOnlem" style="margin-top:16px;font-size:34px"></p></div>
  </div>
  <p class="soluk" style="font-size:24px;margin-top:18px">Bir aşamaya dokun.</p>
  %%ALT4%%
  <aside class="not">(60 sn) Programı on aşamalı bir iş akışı olarak göster. İki aşamaya dokun: ICSI (MII dışında enjeksiyon kendiliğinden “yapılmadı”ya döner) ve Vitrifikasyon (etiket laboratuvar genelinde benzersiz; aynı etiket ikinci kez kullanılamaz). Mesaj: her ekran hem kayıt hem önlem.</aside>
</section>

<!-- 5 KAYIT VE GÜVENLİK -->
<section class="slayt" data-sure="50" data-baslik="Kayıt ve güvenlik">
  <div class="kicker">Kayıt ve güvenlik</div>
  <h2>Güvenlik bir özellik değil, tasarımın kendisi</h2>
  <div class="izgara i3" style="gap:26px;align-items:stretch">
    <div class="kart kucuk"><h3>Rol ve modül izni</h3><p>Kim hangi ekrana girer, ayrı ayrı tanımlı.</p><em>v6.14</em></div>
    <div class="kart kucuk"><h3>Değişiklik günlüğü</h3><p>Sonradan yapılan düzeltme kayda geçer.</p><em>v5.0</em></div>
    <div class="kart kucuk"><h3>İşlemi yapan</h3><p>Her aşamada işlemi kimin yaptığı yazılır.</p><em>v6.3</em></div>
    <div class="kart kucuk"><h3>Benzersiz taşıyıcı etiketi</h3><p>Cryo haritası: tank, kanister, goblet, pozisyon.</p><em>v3.0</em></div>
    <div class="kart kucuk"><h3>Otomatik yedekleme</h3><p>Veri kaybına karşı düzenli yedek.</p><em>v1.2</em></div>
    <div class="kart kucuk"><h3>Güvenli taşıma</h3><p>İki makine arasında kayıpsız veri aktarımı.</p><em>v6.16</em></div>
  </div>
  %%ALT5%%
  <aside class="not">(60 sn) Altı kartı tek tek okuma; ikisini seç ve kendi deneyiminle anlat. Öneri: “işlemi yapan” alanı ve benzersiz taşıyıcı etiketi; ikisi de kriyo güvenliğinin doğrudan karşılığı. [DOĞRULA: her kartın sürüm numarası README’de.]</aside>
</section>

<!-- 6 NASIL YAPTIM -->
<section class="slayt" data-sure="60" data-baslik="Nasıl yaptım?">
  <div class="kicker">Yapay zekâ ile geliştirme</div>
  <h2>Embriyolog ihtiyacı söyler, yapay zekâ kodlar, embriyolog doğrular</h2>
  <div class="izgara i2" style="gap:56px;align-items:center;grid-template-columns:1.1fr 1fr">
    <div class="dongu">
      <div data-adim="1"><b>1</b><span><b>İhtiyaç</b> embriyoloğun cümlesiyle: «kaydediyor ama listede görünmüyor»</span></div>
      <div data-adim="2"><b>2</b><span><b>Yapay zekâ</b> kodu yazar, değişikliği açıklar</span></div>
      <div data-adim="3"><b>3</b><span><b>Test</b> deneme kopyasında</span></div>
      <div data-adim="4"><b>4</b><span><b>Embriyolog doğrular:</b> klinik doğruluk insan kararıdır</span></div>
      <div data-adim="5"><b>5</b><span><b>Sürüm notu:</b> ne değişti, neden</span></div>
    </div>
    <div>
      <div style="display:flex;align-items:baseline;gap:20px"><span class="rakam" data-sayi-ok="1" style="font-size:130px">%%COMMIT%%</span><span class="soluk" style="font-size:32px">commit<br>%%GUN%% günde</span></div>
      %%GIT_SVG%%
      <p class="soluk" style="font-size:26px;margin-top:12px">Çalışma kuralları dosyası (CLAUDE.md, %%CLAUDE_SATIR%% satır) = <b>kod için SOP</b> · %%SURUM%% sürüm notu</p>
    </div>
  </div>
  %%ALT6%%
  <aside class="not">(70 sn) Döngüyü sırayla aç. Birinci adımdaki cümle gerçek: v6.19’da kullanıcının, yani benim, kurduğum cümle. Vurgu dördüncü adım: klinik doğruluk kararını yapay zekâ vermez. Sağda git geçmişi: %%GUN%% günde %%COMMIT%% commit. Bu hızı denetleyen şey CLAUDE.md: yapay zekânın her oturumda okuduğu çalışma kuralları; laboratuvarda SOP neyse, kod için o. [DOĞRULA: git geçmişi 8 Eylül 2026’da başlıyor; önceki sürümler git dışında geliştirildiyse belirt. Kullandığın aracın adını söyle.]</aside>
</section>

<!-- 7 HAYALET OOSİT -->
<section class="slayt" data-sure="60" data-baslik="Önlem örneği">
  <div class="kicker">Problem → önlem · v6.19</div>
  <h2>Sessiz hata: hayalet oosit, oranın paydasını şişirir</h2>
  <div class="izgara i2" style="align-items:center;gap:48px">
    <div>
      <p style="font-size:36px">Aynı kare iki kez kaydedilince fotoğrafsız bir oosit kalıyordu. Ne hata, ne uyarı.</p>
      <p style="font-size:36px;margin-top:24px"><b>Önlem:</b> bağlanamayan kare açılan oositi geri alır, sebep ekranda yazar.</p>
      <p class="soluk" style="margin-top:24px;font-size:30px">«Oosit sayısı klinik bir sayıdır.» · sürüm notu</p>
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
  %%ALT7%%
  <aside class="not">(60 sn) Düğmeye iki kez bas: 10 oositten 7’si 2PN, iki hayalet gelince oran 70’ten 58’e düşer. Bu hatayı bir yazılımcı değil, sorunu yaşayan embriyolog yakaladı. Yapay zekânın hızı, embriyoloğun dikkatiyle birleşince işe yarıyor.</aside>
</section>

<!-- 8 KPI DÜNDEN BUGÜNE -->
<section class="slayt" data-sure="45" data-baslik="KPI: dünden bugüne">
  <div class="kicker">KPI takibi</div>
  <h2>Kâğıtta yıllık hesap, programda aylık oran; yapay zekâ ile erken uyarı</h2>
  <div class="izgara i3" style="gap:32px;align-items:start">
    <div class="kart" data-adim="1"><h3>Dün</h3><p>Yıl sonunda elle sayım. Sorun fark edildiğinde aylar geçmiş.</p></div>
    <div class="kart" data-adim="2"><h3>Bugün</h3><p>Programda aylık oranlar otomatik, yıl ve ay seçilebilir.</p></div>
    <div class="kart" data-adim="3" style="border-color:var(--vurgu)"><h3 class="vurgu">Yarın</h3><p>Haftalık izleme, istatistiksel alarm, adil karşılaştırma, yaşa göre ayar.</p></div>
  </div>
  <p class="soluk" style="margin-top:40px;font-size:30px" data-adim="4">Hangi KPI olduğu önemli değil; yöntem her orana uygulanır.</p>
  %%ALT8%%
  <aside class="not">(45 sn) Bugün programın istatistik ekranı aylık oranları otomatik veriyor (v6.123). Yarın: aynı veriyle yapay zekânın yazdığı analizler. Hangi KPI olduğu önemli değil; fertilizasyon, blastulasyon, çözme sağkalımı fark etmez.</aside>
</section>

<!-- 9 ERKEN UYARI -->
<section class="slayt" data-sure="80" data-baslik="Erken uyarı">
  <div class="kicker">KPI + yapay zekâ · erken uyarı</div>
  <h2>Küçük düşüşü aylık ortalama geç, CUSUM erken görür</h2>
  <div class="izgara i2" style="gap:44px;align-items:center;grid-template-columns:1.15fr 1fr">
    <img class="sekil" src="analiz/sonuc_kpi/fig_kpi_erken_uyari.svg" alt="Aylık oran ve CUSUM">
    <div style="display:grid;gap:16px">
      <div class="kart" data-adim="1" style="padding:26px 30px"><p style="font-size:28px">Senaryo: oran <b>%%TABAN%% → %%KAYMA%%</b> (%%DUSUS%% puan), ör. sarf malzemesi lot değişimi.</p></div>
      <div class="kart" data-adim="2" style="padding:26px 30px"><p style="font-size:28px"><b>%%TEKRAR%% simülasyon</b>, %%IZLEME%% hafta: CUSUM <b class="vurgu">%%CU_YAK%%</b> yakalar (medyan %%CU_MED%% hafta), aylık ortalama %%SH_YAK%% (%%SH_MED%% hafta). Bedeli: yanlış alarm %%CU_YA%% / %%SH_YA%%.</p></div>
      <div class="kart" data-adim="3" style="padding:26px 30px;border-color:var(--vurgu)"><p style="font-size:28px"><b class="vurgu">Yapay zekâ desteği:</b> embriyolog soruyu sorar, yapay zekâ CUSUM kodunu yazar ve açıklar, embriyolog lot kaydıyla karşılaştırıp karar verir.</p></div>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  %%ALT9%%
  <aside class="not">(90 sn) Üst panel: aylık oran ve klasik 3-sigma sınırı; düşüş başladığı halde sınırın altına inmiyor. Alt panel: CUSUM her haftanın küçük kanıtını biriktiriyor ve bu örnekte %%ORNEK_CU%% hafta sonra alarm veriyor. Tek örneğe güvenmeyelim: %%TEKRAR%% simülasyonda CUSUM %%CU_YAK%% oranında yakalıyor, aylık ortalama %%SH_YAK%%. Dürüst olalım: yanlış alarm biraz daha fazla. Son kart asıl mesaj: bu analizi yazmak için istatistikçi olmak gerekmiyor; soruyu embriyolog sorar, kodu yapay zekâ yazar, kararı embriyolog verir.</aside>
</section>

<!-- 10 ADİL KARŞILAŞTIRMA -->
<section class="slayt" data-sure="65" data-baslik="Adil karşılaştırma">
  <div class="kicker">KPI + yapay zekâ · adil karşılaştırma</div>
  <h2>Sıralama değil: funnel grafiği ve yaşa göre ayar</h2>
  <div class="izgara i2" style="gap:44px;align-items:center;grid-template-columns:1.15fr 1fr">
    <div>
      <img class="sekil" id="funnelHam" src="analiz/sonuc_kpi/fig_funnel_ham.svg" alt="Ham oran funnel">
      <img class="sekil" id="funnelAy" src="analiz/sonuc_kpi/fig_funnel_ayarli.svg" alt="Yaşa göre ayarlı funnel" style="display:none">
      <div style="display:flex;gap:16px;margin-top:16px"><button class="dugme" id="fuHam">Ham oran</button><button class="dugme ikincil" id="fuAy">Yaşa göre ayarlı</button></div>
    </div>
    <div style="display:grid;gap:18px">
      <div class="kart" data-adim="1"><h3>F: az vaka, ileri yaş hastalar</h3><p style="font-size:30px">Ham %%F_HAM%% → ayarlı <b>%%F_AY%%</b>. Sıralama tablosu F’yi suçlardı.</p></div>
      <div class="kart" data-adim="2" style="border-color:var(--vurgu)"><h3 class="vurgu">E: sınırların dışında</h3><p style="font-size:30px">Ham %%E_HAM%%, ayarlı %%E_AY%%. Gerçek fark: destek ve eğitim için inceleme.</p></div>
    </div>
  </div>
  <div class="etiket">SENTETİK VERİ</div>
  %%ALT10%%
  <aside class="not">(75 sn) Altı embriyolog, kurgusal. Huni şeklindeki çizgiler: vaka sayısı azaldıkça rastlantının izin verdiği aralık genişler. Ham oranda F düşük görünüyor ama sınırların içinde; üstelik hastaları ortalama %%F_YAS%% yaşında. Yaşa göre ayara bas: F ortalamanın üstüne çıkıyor. E ise iki görünümde de dışarıda; sentetik veride ona gerçekten düşük bir etki koyduk. Mesaj: amaç kimseyi suçlamak değil, gerçek farkı rastlantıdan ayırıp destek vermek.</aside>
</section>

<!-- 11 YZ'NİN DİĞER ALANLARI -->
<section class="slayt" data-sure="60" data-baslik="Labda yapay zekâ">
  <div class="kicker">Laboratuvarda yapay zekâ</div>
  <h2>Yapay zekâ laboratuvarda dört alanda araştırılıyor; kanıt düzeyleri farklı</h2>
  <div class="alanlar">
    <div class="alan" data-adim="1"><h3>Embriyo değerlendirme</h3><p>Morfoloji ve time-lapse görüntülerinden seçim</p><span class="kanit k3">Randomize çalışma var</span></div>
    <div class="alan" data-adim="2"><h3>Ploidi tahmini (görüntü)</h3><p>Biyopsisiz öploidi tahmini</p><span class="kanit k2">Harici doğrulama</span></div>
    <div class="alan" data-adim="3"><h3>niPGT-A</h3><p>Kültür ortamındaki hücresiz DNA; yapay zekâ ile birleşimi araştırılıyor</p><span class="kanit k2">Meta-analiz; büyük çalışma gerekli</span></div>
    <div class="alan" data-adim="4"><h3>Laboratuvar yönetimi</h3><p>KPI izleme, kalite kontrol, iş akışı</p><span class="kanit k1">Derleme, öneri</span></div>
  </div>
  %%ALT11%%
  <aside class="not">(60 sn) Dört alan, dört farklı kanıt düzeyi. Embriyo değerlendirmede randomize çalışma var (bir sonraki slayt). Ploidi tahmininde harici doğrulamalı retrospektif çalışmalar. niPGT-A’da meta-analiz düzeyinde tanısal doğruluk verisi var (havuzlanmış duyarlılık %%HU_S%%, özgüllük %%HU_O%%, %%HU_N%% çalışma) ama meta-analizin kendisi büyük ölçekli çalışmalara ihtiyaç olduğunu söylüyor; tekrarlayan düşük ve implantasyon başarısızlığı gruplarında canlı doğumu gösteren randomize kanıt olmadığı da bir derlemede vurgulanıyor. Laboratuvar yönetiminde ise çoğunlukla derleme ve öneri düzeyinde. [KAYNAK: aday makale listesinden seçiminize göre güncellenecek.]</aside>
</section>

<!-- 12 NE KADAR GÜVENLİ -->
<section class="slayt" data-sure="80" data-baslik="Ne kadar güvenli?">
  <div class="kicker">Ne kadar güvenli?</div>
  <h2>Geriye dönük çalışmada parlak, randomize çalışmada henüz kanıtlanmamış</h2>
  <div class="izgara i2" style="gap:36px;align-items:stretch">
    <div class="kart" data-adim="1"><div class="soluk" style="font-size:22px;font-weight:700;letter-spacing:.08em">SİSTEMATİK DERLEME · %%SA_N%% ÇALIŞMA</div>
      <p style="font-size:32px;margin-top:10px">Morfolojide yapay zekâ <b>%%SA_YZ%%</b>, embriyolog <b>%%SA_EM%%</b> doğruluk; çalışmalar geriye dönük.</p>
      <p class="kaynakk">Salih ve ark., Hum Reprod Open 2023</p></div>
    <div class="kart" data-adim="2" style="border-color:var(--vurgu)"><div class="soluk" style="font-size:22px;font-weight:700;letter-spacing:.08em">RANDOMİZE · %%IL_N%% HASTA · %%IL_K%% KLİNİK</div>
      <p style="font-size:32px;margin-top:10px">Klinik gebelik: yapay zekâ <b>%%IL_YZ%%</b>, morfoloji <b>%%IL_MO%%</b>. Eşdeğerlik <b class="vurgu">gösterilemedi</b>.</p>
      <p class="kaynakk">Illingworth ve ark., Nat Med 2024</p></div>
    <div class="kart" data-adim="3"><p style="font-size:30px">Ploidi modeli: iç testte %%BA_IC%%, iki dış merkezde %%BA_D1%% ve %%BA_D2%% doğruluk.</p><p class="kaynakk">Barnes ve ark., Lancet Digit Health 2023</p></div>
    <div class="kart" data-adim="4"><p style="font-size:30px">%%BM_N%% embriyo, 9 klinik: karma etkili lojistik regresyon AUC %%BM_LR%%; derin öğrenme %%BM_DL%%.</p><p class="kaynakk">Bamford ve ark., Hum Reprod 2023</p></div>
  </div>
  %%ALT12%%
  <aside class="not">(90 sn) Sol üst ile sağ üstü karşılaştır: geriye dönük çalışmalarda yapay zekâ embriyologdan iyi görünüyor; ama randomize, çift kör, %%IL_K%% klinikli çalışmada klinik gebelik %%IL_YZ%% ve %%IL_MO%%, risk farkı %%IL_RD%% (%%IL_GA%%) ve önceden belirlenen eşdeğerlik gösterilemedi. Not: çalışmada üretici firma çalışanları yazar. Alt sıra: model başka kliniğe gidince doğruluk düşüyor; ve 9 klinikli veride basit bir karma model derin öğrenmeyi geçti. Kendi demomuzda da gördük: yanlış doğrulamada AUC %%G_R%%, doğru doğrulamada %%G_G%%. Güven kontrol listesi: harici doğrulama, randomize kanıt, kendi popülasyonunda yerel doğrulama, kalibrasyon, sürekli izleme. [Yalnız özetler okundu; tam metinleri sunumdan önce doğrula.]</aside>
</section>

<!-- 13 EMBRİYOLOG İŞSİZ Mİ -->
<section class="slayt" data-sure="70" data-baslik="Embriyoloğun rolü">
  <div class="kicker">Embriyolog işsiz mi kalacak?</div>
  <h2>Hayır: embriyolog yapay zekânın kalite kontrolcüsü olur</h2>
  <div class="izgara i2" style="gap:44px;align-items:center;grid-template-columns:1fr 1.2fr">
    <div class="roller">
      <div data-adim="1"><b>Etiketleyen</b><span>Modelin “doğru cevabı” embriyoloğun değerlendirmesidir</span></div>
      <div data-adim="2"><b>Doğrulayan</b><span>Model kendi laboratuvarında sınanmadan kullanılmaz</span></div>
      <div data-adim="3"><b>İzleyen</b><span>Uyum haftalık izlenir; kayma alarm verir</span></div>
      <div data-adim="4"><b>Karar veren</b><span>Son söz klinik sorumluluğu taşıyanındır</span></div>
    </div>
    <div>
      <img class="sekil" src="analiz/sonuc_gorsel/fig_kalite_kontrol.svg" alt="Model-embriyolog uyumu izlemi">
      <p style="font-size:28px;margin-top:10px">Kamera %%QC_DEG%%. haftada değişti, alarm <b>aynı hafta</b>; %%QC_ET%% yerel etiketle ince ayar, uyum geri döndü.</p>
    </div>
  </div>
  <div class="etiket">SENTETİK GÖRÜNTÜ</div>
  %%ALT13%%
  <aside class="not">(80 sn) Dört rol. Etiketleyen: literatürdeki modellerin çoğunda “doğru cevap” embriyoloğun değerlendirmesi; yani model embriyologdan öğreniyor. İzleyen: sağdaki grafik. Her hafta 30 embriyoda modelin dediği ile embriyoloğun dediği karşılaştırılıyor. Kamera değişince uyum %%QC_MIN%%’e düşüyor ve EWMA alarm veriyor; iki hafta yerel etiket toplayıp ince ayar yapınca geri dönüyor. Bu işi yapacak kişi, embriyoloğun kendisi. Meslek bitmiyor, bir görev ekleniyor: yapay zekânın kalite kontrolü.</aside>
</section>

<!-- 14 YEREL MODEL -->
<section class="slayt" data-sure="80" data-baslik="Yerel model">
  <div class="kicker">Görsel analiz · kişiselleştirme</div>
  <h2>Hazır model bizim mikroskobumuzda yazı-tura; az sayıda yerel etiket yetiyor</h2>
  <div class="izgara i2" style="gap:44px;align-items:center;grid-template-columns:1fr 1.05fr">
    <div>
      <div class="ornekler"><figure><img src="analiz/sonuc_gorsel/ornek_A.png" alt="Başka lab"><figcaption>Modelin eğitildiği lab</figcaption></figure>
        <figure><img src="analiz/sonuc_gorsel/ornek_B.png" alt="Bizim lab"><figcaption>Bizim mikroskobumuz</figcaption></figure></div>
      <div class="kart" style="margin-top:20px">
        <label style="font-size:28px">Embriyoloğun etiketlediği yerel görüntü: <b id="ynD">0</b></label>
        <input id="yn" type="range" min="0" max="5" step="1" value="0" style="width:100%;margin-top:14px">
      </div>
    </div>
    <div>
      <div class="soluk" style="font-size:28px">Bizim labımızda AUC</div>
      <div class="rakam" id="ynAuc" data-sayi-ok="1" style="font-size:200px">%%HAZIR_BIZ%%</div>
      <p style="font-size:30px">Kendi labında: <b>%%HAZIR_EV%%</b>. Yöntem: başka yerde öğrenilmiş omurga sabit; son katman yerel etiketlerle yeniden eğitilir.</p>
    </div>
  </div>
  <div class="etiket">SENTETİK GÖRÜNTÜ</div>
  %%ALT14%%
  <aside class="not">(90 sn) Görüntüler sentetik: zona, trofektoderm ve iç hücre kitlesi kabaca çizildi; ikinci laboratuvarın kontrastı, parlaklığı, büyütmesi farklı. Sliderı 0’da tut: kendi labında %%HAZIR_EV%% AUC’li model bizde %%HAZIR_BIZ%%, yani yazı-tura; hiçbir embriyoya “kullanılabilir” demiyor. Sliderı aç: 25 yerel etiketle %%Y25%%, 100 ile %%Y100%%, 400 ile %%Y400%%. Bu, yapay zekâyı ham kullanmak ile kendi tecrübenle eğitmek arasındaki fark. Gerçek hayatta bu omurga büyük bir derin ağdır; mantık aynı. Kendi görüntülerinizle yapmak etik onay ister.</aside>
</section>

<!-- 15 ÜÇ YOL -->
<section class="slayt" data-sure="50" data-baslik="Üç yol">
  <div class="kicker">Kişiselleştirmenin üç yolu</div>
  <h2>Yapay zekâyı kendi ihtiyacına göre şekillendirmek</h2>
  <div class="izgara i3" style="gap:32px;align-items:start">
    <div class="kart" data-adim="1"><div class="rakam" style="font-size:90px">1</div><h3>Kendi aracını yap</h3><p>Kayıt, iz, önlem: Patient Data Center gibi.</p></div>
    <div class="kart" data-adim="2"><div class="rakam" style="font-size:90px">2</div><h3>KPI’yı derin izle</h3><p>Erken uyarı, funnel, yaşa göre ayar.</p></div>
    <div class="kart" data-adim="3"><div class="rakam" style="font-size:90px">3</div><h3>Modeli yerelde eğit</h3><p>Hazır omurga, kendi etiketin. Program zaten aşamaya bağlı fotoğraf topluyor.</p></div>
  </div>
  <p class="soluk" style="margin-top:36px;font-size:28px" data-adim="4">Her yolun ortak şartı: veri kalitesi, etik onay, yerel doğrulama, sürekli izleme.</p>
  %%ALT15%%
  <aside class="not">(50 sn) Üç yolu özetle; üçüncüde vurgu: Patient Data Center her fotoğrafı ilgili oosite ve aşamaya bağlıyor (v3.8). Yani etiketli bir görüntü arşivi kendiliğinden oluşuyor. Bu arşivle model eğitmek ayrı bir çalışma ve etik onay gerektirir.</aside>
</section>

<!-- 16 SINIRLAR -->
<section class="slayt" data-sure="45" data-baslik="Sınırlar">
  <div class="kicker">Sınırlar</div>
  <h2>Bu sunumun söylemediği şeyler de var</h2>
  <div class="sinir">
    <p data-adim="1"><b>Sentetik ≠ klinik.</b> Demoların hepsi sentetik veri ve görüntüdür; yöntem gösterimidir.</p>
    <p data-adim="2"><b>Program karar vermez.</b> Kayıt ve betimsel istatistik aracıdır; araştırma amaçlıdır.</p>
    <p data-adim="3"><b>Yapay zekâ kodu yanılır.</b> Kod ve analiz yapay zekâ yardımıyla yazıldı; insan çalıştırdı ve doğruladı.</p>
    <p data-adim="4"><b>Hasta verisi yok.</b> Bu sunumda hiçbir gerçek hasta verisi, görüntü ya da kimlik bilgisi yoktur.</p>
  </div>
  %%ALT16%%
  <aside class="not">(45 sn) Sakin, düz. Üçüncü satır aynı zamanda yapay zekâ kullanım beyanı.</aside>
</section>

<!-- 17 ÜÇ MESAJ -->
<section class="slayt" data-sure="40" data-baslik="Üç mesaj">
  <div class="kicker">Eve götürülecekler</div>
  <h2>Üç cümle</h2>
  <div class="mesajlar">
    <div data-adim="1"><span class="no">1</span><p>Yapay zekâyı <b>ham değil</b>, kendi tecrübenle eğiterek kullan.</p></div>
    <div data-adim="2"><span class="no">2</span><p>KPI’yı ay sonunda değil, <b>istatistiksel erken uyarıyla</b> izle.</p></div>
    <div data-adim="3"><span class="no">3</span><p>Embriyolog işsiz kalmaz: <b>yapay zekânın kalite kontrolcüsü</b> olur.</p></div>
  </div>
  %%ALT17%%
  <aside class="not">(40 sn) Üç cümleyi oku. Kapanış cümlesi: “Yapay zekâ laboratuvarımıza gelecek; onu kimin eğiteceğine biz karar verebiliriz.”</aside>
</section>

<!-- 18 TEŞEKKÜR -->
<section class="slayt dz" data-sure="20" data-baslik="Teşekkür">
  <div class="kicker">Teşekkürler</div>
  <h1 style="font-size:96px">Soru ve tartışma</h1>
  <div class="ayrac"></div>
  <div class="izgara i2" style="align-items:start;gap:56px">
    <p class="soluk">[Ad Soyad] · [Kurum]<br>[e-posta]</p>
    <p class="soluk" style="font-size:28px">Demolar, sentetik veri ve analiz kodu paylaşılacaktır: [bağlantı]. Slaytlardaki her sayı bu kodlardan ve makale özetlerinden gelir.</p>
  </div>
  %%ALT18%%
  <aside class="not">(20 sn) Teşekkür, soruya geç.</aside>
</section>

<!-- YEDEK A -->
<section class="slayt" data-sure="0" data-baslik="Yedek: yöntem">
  <div class="kicker">Yedek · yöntem notları</div>
  <h2>Demolar nasıl yapıldı?</h2>
  <div class="izgara i3" style="gap:28px;align-items:start">
    <div class="kart kucuk"><h3>Erken uyarı</h3><p>Haftalık binom CUSUM (alternatif oran 0.70, eşik 4.5), 52 haftalık taban. Karşılaştırma: 4 haftalık p-grafiği, 3σ.</p></div>
    <div class="kart kucuk"><h3>Funnel</h3><p>Dolaylı standardizasyon: yaş-yalnız lojistik modelle beklenen; gözlenen/beklenen × genel oran. Sınırlar %95 ve %99.8.</p></div>
    <div class="kart kucuk"><h3>Görsel model</h3><p>Sabit omurga (halka-açı özellikleri), lojistik son katman; yerel ölçekleme ve ağırlıklı yeniden eğitim. Etiket gürültüsü %8.</p></div>
  </div>
  <aside class="not">Yedek. Sorulursa göster.</aside>
</section>

<!-- YEDEK B -->
<section class="slayt" data-sure="0" data-baslik="Yedek: sorular">
  <div class="kicker">Yedek · beklenen sorular</div>
  <h2>Beklenen beş soru</h2>
  <div class="sinir" style="font-size:30px">
    <p><b>Kendi verinizde denediniz mi?</b> Hayır; bunlar yöntem gösterimi. Gerçek veride uygulama etik onaylı ayrı çalışma.</p>
    <p><b>Program yapay zekâ modeli içeriyor mu?</b> Hayır; yapay zekâ geliştirme aracı. Program kayıt ve betimsel istatistik yapar.</p>
    <p><b>Yapay zekânın yazdığı koda nasıl güveniyorsunuz?</b> Güvenmiyoruz: SOP, sürüm notu, deneme kopyası, klinik doğrulama.</p>
    <p><b>Embriyolog karşılaştırması kişileri hedef almaz mı?</b> Amaç destek; funnel rastlantıyı ayırır, yaş ayarı adalet sağlar.</p>
    <p><b>Ticari yapay zekâ ürünleri?</b> Kendi popülasyonunda yerel doğrulama yapılmadan kullanılmamalı.</p>
  </div>
  <aside class="not">Yedek. Bilmediğin yerde “bunu ölçmedik” demek doğru cevaptır.</aside>
</section>
'''

ALTLAR = {
    4: "Kaynak: Patient Data Center sürüm notları (v1.4, v2.0, v2.5, v2.6, v3.0, v3.2, v3.6, v5.3, v6.3, v6.19)",
    5: "Kaynak: Patient Data Center sürüm notları",
    6: "Kaynak: depo git geçmişi, CLAUDE.md, README.md",
    7: "Kaynak: sürüm notu v6.19 · örnek hesap kurgusaldır",
    8: "Bugünkü istatistik ekranı: v6.123",
    9: f"SENTETİK VERİ · haftalık ~40 vaka · seed {KP['seed']} · CUSUM eşiği {eu['cusum_esik']}",
    10: "SENTETİK VERİ · 6 kurgusal embriyolog · dolaylı standardizasyon (yaş) · sınırlar %95 ve %99.8",
    11: "Kanıt düzeyi: aday makale taramasına göre (PubMed); seçiminize göre güncellenecek",
    12: "Kaynaklar PubMed özetlerinden; DOI’ler kaynakça listesinde",
    13: "SENTETİK GÖRÜNTÜ · haftada 30 embriyo · EWMA (λ = 0.3)",
    14: f"SENTETİK GÖRÜNTÜ · {GR['ince_ayar']['tekrar']} tekrar ortalaması · ölçüt: AUC",
    15: "Fotoğrafın aşamaya bağlanması: sürüm notu v3.8",
    16: "Mevzuat (KVKK, tıbbi cihaz, yapay zekâ düzenlemeleri) için kurumunuzun etik kurulu ve hukuk birimine danışın",
    17: "Kişiselleştirme: ham model → yerel doğrulama → yerel ince ayar → sürekli izleme",
    18: "",
}
for k, v in ALTLAR.items():
    V[f"ALT{k}"] = alt(v, k)

EK_CSS = r'''
ul{padding-left:30px} h2{margin-bottom:30px} img.sekil{width:100%;height:auto}
.izgara{flex:0 0 auto}
.slayt>*{order:2}.slayt>.kicker,.slayt>h1,.slayt>h2{order:0}
.slayt::before{content:"";order:1;flex:1 1 0}.slayt::after{content:"";order:3;flex:1.3 1 0}
.slayt.dz::before,.slayt.dz::after{display:none}
.durak .ikon{width:150px!important;height:150px!important;font-size:66px!important}.yol:before{top:75px!important}
.durak h3{font-size:42px}.durak p{font-size:32px!important}
.hat{display:flex;gap:8px;margin-top:10px}
.asama{flex:1;padding:24px 2px;border:2px solid var(--cizgi);border-radius:14px;font:600 22px var(--font-metin);text-align:center;cursor:pointer;background:var(--kart);color:var(--metin);white-space:nowrap}
.asama.simdi{background:var(--vurgu);border-color:var(--vurgu);color:#fff}
.yol{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-top:40px;position:relative}
.yol:before{content:"";position:absolute;left:4%;right:4%;top:62px;height:4px;background:var(--cizgi)}
.durak{position:relative;text-align:center}
.durak .ikon{width:124px;height:124px;margin:0 auto 22px;border-radius:50%;background:var(--kart);border:4px solid var(--metin);display:flex;align-items:center;justify-content:center;font-size:56px;color:var(--metin)}
.vurgu-durak .ikon{border-color:var(--vurgu);color:var(--vurgu)}
.durak p{font-size:30px;margin:12px auto 0;max-width:380px}
.kart.kucuk h3{font-size:32px}.kart.kucuk p{font-size:28px;margin-top:8px}
.kart.kucuk em{display:block;font:600 20px var(--font-metin);color:var(--soluk);font-style:normal;margin-top:10px}
.dongu{display:grid;gap:14px}
.dongu>div{display:grid;grid-template-columns:64px 1fr;gap:18px;align-items:center;font-size:30px;line-height:1.3}
.dongu>div>b{width:64px;height:64px;border-radius:50%;background:var(--metin);color:var(--zemin);display:flex;align-items:center;justify-content:center;font:700 30px var(--font-baslik)}
.ooo{display:flex;flex-wrap:wrap;gap:12px;margin:20px 0;min-height:140px}
.ooo i{width:62px;height:62px;border-radius:50%;background:var(--metin);display:inline-block}
.ooo i.ikipn{background:var(--vurgu)} .ooo i.hayalet{background:transparent;border:3px dashed var(--soluk)}
.lej{display:flex;gap:26px;font-size:24px;color:var(--soluk);flex-wrap:wrap}
.lej i{display:inline-block;width:22px;height:22px;border-radius:50%;vertical-align:-4px;margin-right:8px}
.istek{margin-top:22px;padding:20px 28px;border-left:6px solid var(--vurgu);background:var(--kart);font-size:27px;line-height:1.4;border-radius:0 14px 14px 0}
.alanlar{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;margin-top:20px}
.alan{background:var(--kart);border:2px solid var(--cizgi);border-radius:18px;padding:32px;display:flex;flex-direction:column;gap:14px;min-height:380px}
.alan h3{font-size:34px}.alan p{font-size:28px;flex:1}
.kanit{align-self:flex-start;font:700 21px var(--font-metin);padding:8px 14px;border-radius:10px;letter-spacing:.03em}
.k3{background:var(--metin);color:var(--zemin)} .k2{border:2px solid var(--metin)} .k1{border:2px dashed var(--soluk);color:var(--soluk)}
.kaynakk{font-size:21px;color:var(--soluk);margin-top:10px}
.roller{display:grid;gap:18px}
.roller>div{display:grid;gap:4px;padding:16px 22px;border-left:6px solid var(--vurgu);background:var(--kart);border-radius:0 14px 14px 0}
.roller b{font:700 34px var(--font-baslik)} .roller span{font-size:26px;color:var(--soluk)}
.ornekler{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.ornekler figure{margin:0} .ornekler img{width:100%;border-radius:10px;display:block}
.ornekler figcaption{font-size:22px;color:var(--soluk);margin-top:6px}
.sinir{margin-top:20px}.sinir p{margin-bottom:26px;font-size:34px}
.mesajlar{display:grid;gap:34px;margin-top:20px}
.mesajlar>div{display:grid;grid-template-columns:100px 1fr;align-items:center;gap:24px}
.mesajlar .no{font:700 120px/1 var(--font-baslik);color:var(--vurgu)} .mesajlar p{font-size:46px;line-height:1.25;max-width:1450px}
'''

EK_JS = r'''
<script>
(function(){
function bl(e){if(e&&e.currentTarget)e.currentTarget.blur();}
var ASAMA=[
 {ad:'OPU',alan:['Toplanan oositler siklusa bağlanır','İşlemi yapan kaydedilir'],onlem:'Her aşamada işlemi kimin yaptığı yazılır (v6.3).'},
 {ad:'Denüdasyon',alan:['Oosit kaydı, kamera karesi','Toplandığı over (sağ/sol)'],onlem:'Aynı kare iki kez kaydedilirse hayalet oosit oluşmaz (v6.19).'},
 {ad:'ICSI',alan:['Maturasyon: MII / MI / GV','Oosit bulguları, enjeksiyon sonucu'],onlem:'MII dışında enjeksiyon kendiliğinden “yapılmadı”ya döner (v1.4).'},
 {ad:'Fert. kontrol',alan:['Sonuç, PN sayısı, PN skoru','ICSI’den bu yana geçen saat'],onlem:'“Dejenere” ile “0PN” karışmaz; hedef saatten sapma turuncu uyarı verir (v2.0).'},
 {ad:'Gün 2/3',alan:['Hücre sayısı, fragmantasyon, simetri','Skor: otomatik ya da “elle”'],onlem:'Elle girilen skor işaretlenir; otomatik kuralın üzerine yazılmaz (v2.5).'},
 {ad:'Blastokist',alan:['Genişleme, ICM, TE','Gün 5, 6, 7 ayrı kayıt'],onlem:'Morula/arrest seçilince ICM ve TE kaydedilmez; tanımsız değer oluşmaz (v2.6).'},
 {ad:'Vitrifikasyon',alan:['Taşıyıcı: etiket, tip, renk','Konum: tank, kanister, goblet'],onlem:'Etiket laboratuvar genelinde benzersiz; ikinci kez kullanılamaz (v3.0).'},
 {ad:'Çözme',alan:['Embriyo başına sağkalım','Re-expansion (%)'],onlem:'Her embriyonun sağkalımı girilmeden kaydetmez (v3.2).'},
 {ad:'Transfer',alan:['Taze / donmuş ayrımı','Geldiği siklus ≠ transfer siklusu'],onlem:'Taze/donmuş ayrımı elle değil, kayıttan çıkar (v3.6).'},
 {ad:'Gebelik',alan:['Beta hCG ham değerleri','Klinik gebelik, sonlanma'],onlem:'hCG pozitif/negatif değil ham değer olarak saklanır; eşik sonradan uygulanır (v5.3).'}
];
var hat=document.getElementById('hat');
if(hat){var ch=ASAMA.map(function(a,k){var b=document.createElement('div');b.className='asama';b.textContent=a.ad;b.onclick=function(){sec(k);};hat.appendChild(b);return b;});
 function sec(k){ch.forEach(function(c,j){c.className='asama'+(j===k?' simdi':'');});
  document.getElementById('hatBaslik').textContent=ASAMA[k].ad+': kaydedilen';
  var ul=document.getElementById('hatAlan');ul.innerHTML='';ASAMA[k].alan.forEach(function(t){var li=document.createElement('li');li.textContent=t;li.style.fontSize='34px';li.style.marginBottom='10px';ul.appendChild(li);});
  document.getElementById('hatOnlem').textContent=ASAMA[k].onlem;}
 sec(2);}
var oo=document.getElementById('ooSahne');
if(oo){var gh=0;function ciz(){oo.innerHTML='';for(var i=0;i<10;i++){var e=document.createElement('i');if(i<7)e.className='ikipn';oo.appendChild(e);}
 for(var j=0;j<gh;j++){var h=document.createElement('i');h.className='hayalet';oo.appendChild(h);}
 document.getElementById('ooOran').textContent=(700/(10+gh)).toFixed(1)+' %';}
 document.getElementById('ooArti').onclick=function(e){if(gh<6)gh++;ciz();bl(e);};
 document.getElementById('ooEksi').onclick=function(e){if(gh>0)gh--;ciz();bl(e);};ciz();}
var fh=document.getElementById('fuHam'),fa=document.getElementById('fuAy');
if(fh&&fa){function fu(a,e){document.getElementById('funnelHam').style.display=a?'none':'block';document.getElementById('funnelAy').style.display=a?'block':'none';
 fh.className=a?'dugme ikincil':'dugme';fa.className=a?'dugme':'dugme ikincil';bl(e);}
 fh.onclick=function(e){fu(false,e);};fa.onclick=function(e){fu(true,e);};}
var yn=document.getElementById('yn');
if(yn){var AUC=%%AUC_DIZI%%,NN=%%N_DIZI%%;
 yn.oninput=function(){document.getElementById('ynD').textContent=NN[+yn.value];document.getElementById('ynAuc').textContent=AUC[+yn.value].toFixed(2);};yn.oninput();}
})();
</script>
'''


def derle():
    html = ISKELET.read_text(encoding="utf-8")
    g = html.index("</head>")
    bas = html.index('<main id="sahne">', g) + len('<main id="sahne">'); son = html.index('<div id="ilerleme">', bas)
    html = html[:bas] + "\n" + SLAYTLAR + "\n" + html[son:]
    html = html.replace("</style>", EK_CSS + "\n</style>", 1).replace("</body>", EK_JS + "\n</body>")
    html = html.replace("<title>SUNUM BAŞLIĞI — Klinik Embriyoloji Kongresi 2027</title>", "<title>Ham değil, kişisel yapay zekâ — Klinik Embriyoloji Kongresi 2027</title>")
    html = html.replace("var HEDEF_SN=18*60;", "var HEDEF_SN=18*60;")
    html = html.replace("%%GIT_SVG%%", GIT_SVG)
    def rep(m):
        k = m.group(1)
        if k not in V: raise KeyError(k)
        return V[k]
    html = re.sub(r"%%([A-Z_0-9]+)%%", rep, html)
    html = re.sub(r"%%([A-Z_0-9]+)%%", rep, html)   # ALT içindeki jetonlar için ikinci geçiş
    (KOK / "sunum.html").write_text(html, encoding="utf-8")
    notlar = []
    for i, m in enumerate(re.finditer(r'<section class="slayt[^"]*" data-sure="(\d+)" data-baslik="([^"]*)">.*?<aside class="not">(.*?)</aside>', html, re.S), 1):
        notlar.append(f"## {i}. {m.group(2)}  ({m.group(1)} sn)\n\n{re.sub('<[^>]+>', '', m.group(3)).strip()}\n")
    toplam = sum(int(x) for x in re.findall(r'data-sure="(\d+)"', html))
    (KOK / "sunucu_notlari.md").write_text(f"# Sunucu notları\n\nPlanlanan süre: {toplam//60} dk {toplam%60} sn. [DOĞRULA]/[KAYNAK] satırları sunumdan önce kapatılmalı.\n\n" + "\n".join(notlar), encoding="utf-8")
    json.dump(dict(analiz=SZ, kpi=KP, gorsel=GR, literatur=LT, depo=DEPO), open(A / "tum_sayilar.json", "w"), ensure_ascii=False, indent=1)
    print(f"sunum.html: {len(notlar)} sahne, planlanan {toplam//60} dk {toplam%60} sn")


if __name__ == "__main__":
    derle()
