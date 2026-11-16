// Etkin slayttaki görünür öğeleri toplar: kutular, metin blokları, resim bölgeleri, sözde öğeler.
// Koordinatlar 1920x1080 sahne çerçevesinde.
(() => {
  const sahne = document.getElementById('sahne');
  const sR = sahne.getBoundingClientRect();
  const olcek = sR.width / 1920;
  const slayt = document.querySelector('.slayt.aktif');
  const out = [];
  document.querySelectorAll('[data-pptx]').forEach(e => e.removeAttribute('data-pptx'));
  const R = r => ({x: (r.left - sR.left) / olcek, y: (r.top - sR.top) / olcek, w: r.width / olcek, h: r.height / olcek});

  const parseC = s => {
    const m = s && s.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number);
    return {r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1};
  };
  const opak = el => { let o = 1; for (let e = el; e && e !== document.body; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const arkaplan = el => {
    for (let e = el; e; e = e.parentElement) {
      const c = parseC(getComputedStyle(e).backgroundColor); if (c && c.a > 0.5) return c;
    }
    return {r: 246, g: 243, b: 236, a: 1};
  };
  const karis = (c, alfa, alt) => {
    const a = Math.max(0, Math.min(1, alfa));
    const h = v => Math.round(v).toString(16).padStart(2, '0');
    return h(c.r * a + alt.r * (1 - a)) + h(c.g * a + alt.g * (1 - a)) + h(c.b * a + alt.b * (1 - a));
  };
  const renk = (s, el, ekstraAlfa = 1) => {
    const c = parseC(s); if (!c || c.a === 0) return null;
    const alt = arkaplan(el.parentElement || el);
    return karis(c, c.a * opak(el) * ekstraAlfa, alt);
  };
  const gradRenk = (bgi, el) => {
    const m = (bgi || '').match(/rgba?\([^)]+\)/g) || [];
    for (const c of m) { const p = parseC(c); if (p && p.a > 0) return renk(c, el); }
    return null;
  };
  const icGolge = cs => {
    const m = (cs.boxShadow || '').match(/(rgba?\([^)]+\))\s+0px\s+0px\s+0px\s+([\d.]+)px\s+inset/);
    return m ? {c: m[1], w: parseFloat(m[2])} : null;
  };
  const adimOf = el => { const a = el.closest('[data-adim]'); return a ? +a.dataset.adim : 0; };
  const satirIci = cs => cs.display === 'inline';
  const gorunur = (el, cs) => cs.display !== 'none' && cs.visibility !== 'hidden' && opak(el) > 0.02;

  function kenar(el, cs, r) {
    const yan = ['Top', 'Right', 'Bottom', 'Left'].map(s => ({
      w: parseFloat(cs['border' + s + 'Width']) || 0, st: cs['border' + s + 'Style'], c: cs['border' + s + 'Color']}));
    return yan;
  }

  function vurguRengi(p) {
    for (let e = p; e && e !== document.body; e = e.parentElement) {
      const ecs = getComputedStyle(e);
      if (ecs.display !== 'inline') break;
      if (ecs.backgroundImage && ecs.backgroundImage !== 'none') return gradRenk(ecs.backgroundImage, e) || 'FFD43B';
      const bc = parseC(ecs.backgroundColor); if (bc && bc.a > 0) return renk(ecs.backgroundColor, e);
    }
    return null;
  }

  function metinBlok(el, cs) {
    const runs = []; const rects = []; const ek = [];
    const pre = /pre/.test(cs.whiteSpace);
    function yuru(n, stil) {
      for (const c of n.childNodes) {
        if (c.nodeType === 3) {
          let t = c.data;
          const pcs = getComputedStyle(c.parentElement);
          if (!/pre/.test(pcs.whiteSpace)) t = t.replace(/\s+/g, ' ');
          if (!t) continue;
          if (pcs.textTransform === 'uppercase') t = t.toLocaleUpperCase('tr');
          const rg = document.createRange(); rg.selectNodeContents(c);
          for (const rr of rg.getClientRects()) if (rr.width > 0) rects.push(rr);
          const p = c.parentElement;
          runs.push({t, font: pcs.fontFamily.split(',')[0].replace(/["']/g, '').trim(), boy: parseFloat(pcs.fontSize),
            kalin: parseInt(pcs.fontWeight) >= 600, italik: pcs.fontStyle === 'italic',
            renk: renk(pcs.color, p) || '111A27', ls: parseFloat(pcs.letterSpacing) || 0,
            vurgu: vurguRengi(p), mono: /mono|Consolas|DejaVu Sans Mono/i.test(pcs.fontFamily)});
        } else if (c.nodeType === 1) {
          const ccs = getComputedStyle(c);
          if (!gorunur(c, ccs)) continue;
          if (c.tagName === 'BR') { runs.push({br: true}); continue; }
          if (['svg', 'IMG', 'CANVAS'].includes(c.tagName) && satirIci(ccs) || /^inline-/.test(ccs.display)) {
            const w = c.getBoundingClientRect().width / olcek, fs = parseFloat(ccs.fontSize) || 20;
            const cx = (window.__cx = window.__cx || document.createElement('canvas').getContext('2d'));
            cx.font = fs + 'px Inter'; const bw = cx.measureText('\u00a0').width || fs * 0.28;
            runs.push({t: '\u00a0'.repeat(Math.max(1, Math.round((w + (parseFloat(ccs.marginLeft) || 0) + (parseFloat(ccs.marginRight) || 0)) / bw))),
              font: 'Inter', boy: fs, kalin: false, italik: false, renk: '111A27', ls: 0, vurgu: null});
            continue;
          }
          if (satirIci(ccs)) {
            const bg = renk(ccs.backgroundColor, c), ig = icGolge(ccs);
            const yan = ['Top', 'Right', 'Bottom', 'Left'].map(sd => ({w: (parseFloat(ccs['border' + sd + 'Width']) || 0) / olcek,
              kesik: /dash|dot/.test(ccs['border' + sd + 'Style']),
              c: (parseFloat(ccs['border' + sd + 'Width']) || 0) > 0 && ccs['border' + sd + 'Style'] !== 'none' ? renk(ccs['border' + sd + 'Color'], c) : null}));
            if (ig && !yan.some(y => y.c)) yan.forEach(y => { y.w = ig.w / olcek; y.c = renk(ig.c, c); y.kesik = false; });
            if (yan.some(y => y.c))
              for (const rr of c.getClientRects()) ek.push({tip: 'kutu', r: R(rr), dolgu: bg, yuvarlak: (parseFloat(ccs.borderTopLeftRadius) || 0) / olcek, yan, adim: adimOf(c)});
            yuru(c);
          }
        }
      }
    }
    yuru(el);
    if (!runs.some(r => r.t && r.t.trim())) return ek.length ? {ek} : null;
    // baştaki/sondaki boşlukları kırp
    const ilk = runs.find(r => r.t); if (ilk) ilk.t = ilk.t.replace(/^\s+/, '');
    const son = [...runs].reverse().find(r => r.t); if (son) son.t = son.t.replace(/\s+$/, '');
    let L = 1e9, T = 1e9, Rr = -1e9, B = -1e9;
    for (const rr of rects) { L = Math.min(L, rr.left); T = Math.min(T, rr.top); Rr = Math.max(Rr, rr.right); B = Math.max(B, rr.bottom); }
    const lh = cs.lineHeight === 'normal' ? parseFloat(cs.fontSize) * 1.2 : parseFloat(cs.lineHeight);
    const er = el.getBoundingClientRect();
    const pl = parseFloat(cs.paddingLeft) + parseFloat(cs.borderLeftWidth), pr = parseFloat(cs.paddingRight) + parseFloat(cs.borderRightWidth);
    const icerik = {left: er.left + pl, right: er.right - pr};
    const yaz = R({left: L, top: T, width: Rr - L, height: B - T});
    const kap = R({left: icerik.left, top: T, width: icerik.right - icerik.left, height: B - T});
    const satirSay = Math.max(1, Math.round((B - T) / lh));
    return {ek, tip: 'metin', yaz, kap, runs, hiza: cs.textAlign, lh: lh / olcek, satir: satirSay,
      dikey: /vertical/.test(cs.writingMode), adim: adimOf(el)};
  }

  function yuru(el) {
    const cs = getComputedStyle(el);
    if (!gorunur(el, cs)) return;
    if (el.tagName === 'ASIDE') return;
    const r = el.getBoundingClientRect();
    const tag = el.tagName.toLowerCase();
    if (tag === 'svg' || tag === 'img' || tag === 'canvas') {
      if (r.width > 2 && r.height > 2) out.push({tip: 'resim', r: R(r), adim: adimOf(el), sira: out.length, sec: '[data-pptx="' + out.length + '"]'});
      el.setAttribute('data-pptx', out.length - 1);
      return;
    }
    if (!satirIci(cs) && el !== slayt) {
      const bg = renk(cs.backgroundColor, el);
      const yan = kenar(el, cs, r);
      const ig = icGolge(cs);
      if (ig && !yan.some(y => y.w > 0 && y.st !== 'none')) yan.forEach(y => { y.w = ig.w; y.st = 'solid'; y.c = ig.c; });
      if (cs.backgroundImage && cs.backgroundImage !== 'none' && el.tagName !== 'MARK') {
        const gr = gradRenk(cs.backgroundImage, el);
        const bs = (cs.backgroundSize || '').split(' ');
        if (gr && bs.length === 2 && /px$/.test(bs[1])) {
          const hh = parseFloat(bs[1]), ww = /%$/.test(bs[0]) ? r.width * parseFloat(bs[0]) / 100 : parseFloat(bs[0]) || r.width;
          out.push({tip: 'kutu', r: R({left: r.left + (r.width - ww) / 2, top: r.top + (r.height - hh) / 2, width: ww, height: hh}),
            dolgu: gr, yuvarlak: 0, yan: [], adim: adimOf(el)});
        }
      }
      const bgi = cs.backgroundImage !== 'none' && el.tagName !== 'MARK';
      const yuvarlak = parseFloat(cs.borderTopLeftRadius) || 0;
      if ((bg || yan.some(y => y.w > 0 && y.st !== 'none')) && r.width > 0.5 && r.height > 0.5) {
        out.push({tip: 'kutu', r: R(r), dolgu: bg, yuvarlak: yuvarlak / olcek,
          yan: yan.map(y => ({w: y.w / olcek, kesik: /dash|dot/.test(y.st), c: y.w > 0 && y.st !== 'none' ? renk(y.c, el) : null})),
          adim: adimOf(el)});
      }
      for (const ps of ['::before', '::after']) {
        const p = getComputedStyle(el, ps);
        if (p.content && p.content !== 'none' && p.display !== 'none' && p.position === 'absolute') {
          const pb = renk(p.backgroundColor, el);
          if (pb) out.push({tip: 'kutu', r: {x: (r.left - sR.left) / olcek + parseFloat(p.left), y: (r.top - sR.top) / olcek + parseFloat(p.top),
            w: parseFloat(p.width), h: parseFloat(p.height)}, dolgu: pb, yuvarlak: 0, yan: [], adim: adimOf(el)});
        }
      }
      const m = metinBlok(el, cs);
      if (m) { out.push(...m.ek); if (m.tip) { delete m.ek; out.push(m); } }
    }
    for (const c of el.children) {
      const ccs = getComputedStyle(c);
      if (!satirIci(ccs) || ['svg', 'IMG', 'CANVAS'].includes(c.tagName)) yuru(c);
      else {   // satır içi öğenin içindeki blok/resim öğeleri
        for (const cc of c.querySelectorAll('svg, img, canvas')) if (!cc.parentElement.closest('svg')) yuru(cc);
      }
    }
  }
  // slayt arka planı
  out.push({tip: 'zemin', renk: renk(getComputedStyle(sahne).backgroundColor, sahne) || 'F6F3EC'});
  yuru(slayt);
  const not = slayt.querySelector('aside.not');
  return {ogeler: out, not: not ? not.textContent.trim() : '', baslik: slayt.dataset.baslik, sure: +slayt.dataset.sure,
          adimSay: Math.max(0, ...[...slayt.querySelectorAll('[data-adim]')].map(e => +e.dataset.adim))};
})()
