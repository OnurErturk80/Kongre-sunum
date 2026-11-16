(function(){
"use strict";
var statik=(/[?&]k=/.test(location.search)||navigator.webdriver===true)&&!/[?&]canli=1/.test(location.search);   /* dışa aktarımda animasyon yok */
function bl(e){if(e&&e.currentTarget&&e.currentTarget.blur)e.currentTarget.blur();}
function el(id){return document.getElementById(id);}

/* 1.1 — aşama hattı ve kanıt × olgunluk matrisi */
var D=%%DURAK%%;
var hk=el('hatk');
if(hk){
  var SEKIL={
    rkc:'<rect x="8" y="8" width="32" height="32" fill="var(--sari)" stroke="var(--metin)" stroke-width="5"/>',
    pro:'<circle cx="24" cy="24" r="16" fill="var(--metin)"/>',
    ret:'<circle cx="24" cy="24" r="14" fill="var(--zemin)" stroke="var(--metin)" stroke-width="5"/>',
    kav:'<polygon points="24,6 43,40 5,40" fill="var(--zemin)" stroke="var(--metin)" stroke-width="5"/>',
    yok:'<rect x="6" y="14" width="36" height="20" fill="var(--zemin)"/><line x1="8" x2="40" y1="24" y2="24" stroke="var(--metin)" stroke-width="6"/>'};
  var SATIR={rkc:100,pro:214,ret:328,kav:442,yok:556}, say={}, kap=el('duraklar');
  var dg=D.map(function(a,k){
    var b=document.createElement('div');b.className='dr'+(k%2?' tek':'');
    b.innerHTML='<svg viewBox="0 0 48 48">'+SEKIL[a.s]+'</svg><span>'+a.ad+'</span>';
    var an=a.s+a.c; say[an]=(say[an]||0);
    b._hat='translate('+(68+k*(1488/11)).toFixed(1)+'px,20px)';
    b._mat='translate('+((a.c?980:320)+100+say[an]*165)+'px,'+(SATIR[a.s]-48)+'px)';
    say[an]++;
    b.style.transform=b._hat;
    b.onclick=function(){sec(k);};
    kap.appendChild(b);return b;});
  var sec=function(k){
    dg.forEach(function(c,j){c.classList.toggle('sec',j===k);});
    var a=D[k];
    el('hkAd').textContent=a.ad;el('hkAmac').textContent=a.amac;el('hkArac').textContent=a.arac;
    el('hkOlg').textContent=a.olg;el('hkKanit').textContent=a.kanit;el('hkSayi').textContent=a.sayi;};
  var gorunum=function(m,e){
    hk.classList.toggle('mat',m);
    dg.forEach(function(c){c.style.transform=m?c._mat:c._hat;});
    el('gHat').className=m?'dugme ikincil':'dugme';el('gMat').className=m?'dugme':'dugme ikincil';bl(e);};
  el('gHat').onclick=function(e){gorunum(false,e);};
  el('gMat').onclick=function(e){gorunum(true,e);};
  /* → / ← tuşlarıyla da duraklar mouse tıklamasıyla aynı sırayla açılsın */
  var adimEls=[].slice.call(hk.querySelectorAll('.adimler [data-adim]'));
  adimEls.forEach(function(mk,idx){
    new MutationObserver(function(){
      if(mk.classList.contains('goster'))sec(idx);
      else if(idx>0)sec(idx-1);else sec(6);
    }).observe(mk,{attributes:true,attributeFilter:['class']});
  });
  sec(6);
}

/* 2.1 — tür süzgeci */
var lj=el('lej2');
if(lj){
  var secili=null, dug=[].slice.call(lj.querySelectorAll('button')), ulk=[].slice.call(document.querySelectorAll('.ulke'));
  dug.forEach(function(b){b.onclick=function(e){
    secili=(secili===b.dataset.t)?null:b.dataset.t;
    dug.forEach(function(x){x.classList.toggle('sec',x.dataset.t===secili);});
    ulk.forEach(function(u){u.classList.toggle('sonuk',!!secili&&u.dataset.tur.indexOf(secili)<0);});
    bl(e);};});
}

/* 3.2 — kronometre çubukları: 1 gerçek saniye = 40 sn */
var kr=el('krono');
if(kr&&!statik){
  var HED={krEs:parseFloat('%%KR_E%%'),krAs:parseFloat('%%KR_A%%')}, SON={krEs:'%%KR_E%%',krAs:'%%KR_A%%'}, SUR={krEs:5000,krAs:520}, kare=null;
  var oyna=function(){
    kr.classList.remove('oyna');void kr.offsetWidth;kr.classList.add('oyna');
    var t0=performance.now();cancelAnimationFrame(kare);
    (function adim(t){
      var bitti=true;
      Object.keys(HED).forEach(function(id){
        var o=Math.min(1,(t-t0)/SUR[id]);
        el(id).textContent=o<1?(HED[id]*o).toFixed(1):SON[id];
        if(o<1)bitti=false;});
      if(!bitti)kare=requestAnimationFrame(adim);
    })(t0);};
  el('krT').onclick=function(e){oyna();bl(e);};
  var sl=kr.closest('.slayt'), onceki=sl.classList.contains('aktif');
  new MutationObserver(function(){
    var simdi=sl.classList.contains('aktif');
    if(simdi&&!onceki&&!document.body.classList.contains('genel'))oyna();
    onceki=simdi;}).observe(sl,{attributes:true,attributeFilter:['class']});
}

/* 4.2 — aynı model, iki sayı */
var D4=%%DURUM%%;
var d4=el('d4');
if(d4){
  var bt=[].slice.call(d4.querySelectorAll('button'));
  var kur=function(i,e){
    var a=D4[i], s=el('d4sayi');
    bt.forEach(function(b,j){b.classList.toggle('sec',j===i);});
    el('d4et').textContent=a.et;
    s.textContent=a.sayi;
    s.className='rk'+(a.sayi.length<=4?'':(a.sayi.length<=9?' b2':(a.sayi.length<=11?' b3':' b4')));
    el('d4ek').innerHTML=(a.sentetik?'<span class="sent">SENTETİK VERİ · klinik bulgu değildir</span>':'')+(a.ek||'');
    el('d4ac').textContent=a.ac;
    el('bulut').classList.toggle('sonuk',i>0);
    bl(e);};
  bt.forEach(function(b,i){b.onclick=function(e){kur(i,e);};});
}

/* 5.4 — funnel: ham ↔ yaşa göre ayarlı */
var fh=el('fuHam'),fa=el('fuAy');
if(fh&&fa){
  var nk=[].slice.call(document.querySelectorAll('#funnel .fn'));
  var fu=function(ay,e){
    nk.forEach(function(g){g.style.transform=ay?g.dataset.ay:g.dataset.ham;});
    fh.className=ay?'dugme ikincil':'dugme';fa.className=ay?'dugme':'dugme ikincil';bl(e);};
  fh.onclick=function(e){fu(false,e);};fa.onclick=function(e){fu(true,e);};
}
})();
