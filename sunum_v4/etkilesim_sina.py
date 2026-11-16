#!/usr/bin/env python3
"""Etkileşimleri tıklayarak sınar; konsol hatası varsa bildirir. Görüntüler cikti/etkilesim/ altına."""
import pathlib
from playwright.sync_api import sync_playwright
url = pathlib.Path('cikti/sunum_salon.html').resolve().as_uri(); out = pathlib.Path('cikti/etkilesim'); out.mkdir(exist_ok=True)
hata = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.on("console", lambda m: hata.append(m.text) if m.type == "error" else None); pg.on("pageerror", lambda e: hata.append(str(e)))
    def git(k): pg.goto(f"{url}?canli=1#s{k}"); pg.reload(); pg.wait_for_timeout(400)
    def cek(ad): pg.wait_for_timeout(1100); pg.screenshot(path=str(out / f"{ad}.png"))
    git(2); pg.click('.dr:nth-child(4)'); cek('02_oosit'); pg.click('#gMat'); cek('02_matris'); pg.click('#gHat'); cek('02_hat_geri')
    git(4); pg.click('#lej2 button[data-t="S"]'); cek('04_S'); pg.click('#lej2 button[data-t="S"]'); pg.click('#lej2 button[data-t="E"]'); cek('04_E')
    git(7); pg.wait_for_timeout(300); pg.click('#krT'); pg.wait_for_timeout(1500); pg.screenshot(path=str(out / '07_oynarken.png')); pg.wait_for_timeout(4500); cek('07_bitti')
    assert pg.inner_text('#krEs') and pg.inner_text('#krAs')
    print('krono son değerler:', pg.inner_text('#krEs'), pg.inner_text('#krAs'))
    git(10)
    for i in range(1, 5): pg.click(f'#d4 button[data-i="{i}"]'); cek(f'10_durum{i}')
    git(15); pg.click('#fuAy'); cek('15_ayarli')
    # klavyeyle baştan sona yürü (adımlar dahil), genel bakış ve tema
    git(1)
    for _ in range(80): pg.keyboard.press('ArrowRight')
    print('son konum:', pg.evaluate('location.hash'))
    for _ in range(200): pg.keyboard.press('ArrowLeft')
    print('başa dönüş:', pg.evaluate('location.hash'))
    pg.keyboard.press('g'); pg.wait_for_timeout(300); pg.screenshot(path=str(out / 'genel_bakis.png')); pg.keyboard.press('g')
    pg.keyboard.press('d'); git(8); pg.keyboard.press('d'); 
    for _ in range(5): pg.keyboard.press('ArrowRight')
    cek('08_koyu')
    b.close()
print('KONSOL HATASI:', hata if hata else 'yok')
