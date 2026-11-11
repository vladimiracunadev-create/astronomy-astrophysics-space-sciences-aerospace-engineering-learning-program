# SPDX-License-Identifier: Apache-2.0
"""Genera la página de inicio (landing) y los archivos de la aplicación web instalable (PWA).

Sigue la lógica de los demás programas de aprendizaje: cabecera con versión, cifras, accesos, descargas de la
última release, tarjetas por área y bloque con progreso local, búsqueda y filtro, manifiesto PWA y service worker.
Se invoca desde sitio.py; no tiene estado propio.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: F401,F403

REPO = "vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program"
URL_REPO = f"https://github.com/{REPO}"
URL_PAGES = "https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/"
URL_RELEASE = f"{URL_REPO}/releases/latest"


def url_descarga(nombre: str) -> str:
    return f"{URL_REPO}/releases/latest/download/{nombre}"


def nombre_slug(s: str) -> str:
    s = sin_acentos(s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def limpiar_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*`_>#]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def primera_frase(texto: str, limite: int = 230) -> str:
    texto = limpiar_md(texto)
    m = re.match(r"(.+?[.!?])(\s|$)", texto)
    f = m.group(1) if m else texto
    return f if len(f) <= limite else f[: limite - 1].rsplit(" ", 1)[0] + "…"


def resumen_bloque(guia: Path | None) -> str:
    if not guia:
        return ""
    t = guia.read_text(encoding="utf-8")
    m = re.search(r"^##\s+[^\n]*Propósito[^\n]*\n+(.+?)(?:\n\n|\Z)", t, re.S | re.M)
    return primera_frase(m.group(1)) if m else ""


def resumen_rol(p: Path) -> str:
    for linea in p.read_text(encoding="utf-8").splitlines():
        if linea.startswith("> ") and "Nivel de entrada" not in linea and len(linea) > 12:
            return primera_frase(linea[2:])
    return ""


def nombres_pdf(areas, rutas):
    """Nombres estables (sin versión) de los PDF, para enlaces .../releases/latest/download/<nombre>."""
    a = {k: f"Area-{k}-{nombre_slug(v)}.pdf" for k, v in areas.items()}
    r = {x["id"]: f"Rol-{x['id']}-{nombre_slug(x['nombre'])}.pdf" for x in rutas}
    return a, r


def datos_landing():
    import generar_rutas_por_rol as gr
    areas, bloques = bloques_y_areas()
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    pdf_area, pdf_rol = nombres_pdf(areas, rutas)
    out_areas = []
    n_clases = 0
    for a, ta in areas.items():
        bl = []
        for bid, b in bloques.items():
            if b["area"] != a:
                continue
            g = guia_bloque(bid)
            cl = clases_de_bloque(bid)
            n_clases += len(cl)
            bl.append({"id": bid, "titulo": b["titulo"], "n": len(cl), "resumen": resumen_bloque(g),
                       "guia": f"programa/tronco-comun/{g.stem}.html" if g else "",
                       "clase1": f"programa/clases/{bid}/{cl[0].parent.name}/CLASE.html" if cl else ""})
        out_areas.append({"id": a, "titulo": ta, "pdf": pdf_area[a], "bloques": bl})
    roles = []
    for r in rutas:
        slug = gr.slug_de(r["id"])
        roles.append({"id": r["id"], "nombre": r["nombre"], "resumen": resumen_rol(ROOT / "rutas" / f"{slug}.md"),
                      "guia": f"rutas/{slug}.html", "pdf": pdf_rol[r["id"]]})
    anexos = []
    for p in sorted((ROOT / "anexos").glob("ANEXO-*.md")):
        anexos.append({"titulo": titulo_de(p.read_text(encoding="utf-8"), p.stem), "href": f"anexos/{p.stem}.html"})
    gl = (ROOT / "glosario" / "README.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*([\d.]+)\*\* términos distintos, \*\*([\d.]+)\*\* siglas y \*\*([\d.]+)\*\* símbolos", gl)
    terminos, siglas, simbolos = (m.groups() if m else ("", "", ""))
    return {
        "version": VERSION, "titulo": TITULO,
        "stats": {"areas": len(areas), "bloques": len(bloques), "clases": n_clases, "roles": len(rutas),
                  "anexos": len(anexos), "terminos": terminos, "siglas": siglas, "simbolos": simbolos},
        "areas": out_areas, "roles": roles, "anexos": anexos,
        "descargas": {
            "release": URL_RELEASE, "repo": URL_REPO,
            "general": url_descarga("Programa-General.pdf"),
            "windows": f"Programa-Aeroespacial_v{VERSION}_Windows.zip",
            "android": f"Programa-Aeroespacial_v{VERSION}_Android.apk",
            "base": f"{URL_REPO}/releases/latest/download/",
        },
    }


CSS = """
:root{--bg:#070b17;--fg:#e8edf7;--mut:#9aa8c2;--lin:#1f2a44;--card:#0f1730;--ac:#7cc4ff;--ac2:#a78bfa;--ok:#4ade80}
@media (prefers-color-scheme:light){:root{--bg:#f4f7fb;--fg:#142335;--mut:#567089;--lin:#d8e1e8;--card:#ffffff;--ac:#205e8d;--ac2:#6d4fc2;--ok:#1f8a4c}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:var(--ac)}
.hero{padding:56px 20px 36px;text-align:center;background:radial-gradient(60rem 24rem at 50% -10%,rgba(124,196,255,.18),transparent)}
.eyebrow{display:inline-block;font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
.hero h1{font-size:clamp(1.7rem,4.5vw,2.8rem);line-height:1.15;margin:.4em auto;max-width:56rem}
.gradient{background:linear-gradient(90deg,var(--ac),var(--ac2));-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{max-width:48rem;margin:0 auto 1.2em;color:var(--mut);font-size:1.08rem}
.stats{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:1.2em 0}
.stat{min-width:7.5rem;padding:10px 14px;border:1px solid var(--lin);border-radius:12px;background:var(--card);color:var(--mut);font-size:.85rem}
.stat strong{display:block;font-size:1.5rem;color:var(--fg)}
.cta{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:1.2em}
.btn{display:inline-block;padding:11px 18px;border-radius:10px;border:1px solid var(--lin);text-decoration:none;font-weight:600;color:var(--fg)}
.btn-primary{background:linear-gradient(90deg,var(--ac),var(--ac2));color:#06101f;border:none}
.aviso{max-width:52rem;margin:1.6em auto 0;padding:10px 14px;border:1px solid var(--lin);border-radius:10px;color:var(--mut);font-size:.9rem;background:var(--card)}
.sec{max-width:72rem;margin:0 auto;padding:28px 18px}
.sec h2{font-size:1.5rem;margin:.2em 0 .3em}.sec>p{color:var(--mut);margin-top:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:12px;margin:14px 0}
.card{display:flex;flex-direction:column;gap:6px;padding:14px;border:1px solid var(--lin);border-radius:12px;background:var(--card)}
.card .meta{display:flex;justify-content:space-between;font-size:.78rem;color:var(--mut)}
.card h3{font-size:1.02rem;margin:0}.card p{margin:0;color:var(--mut);font-size:.9rem;flex:1}
.card .act{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:.88rem;margin-top:4px}
.card.done{border-color:var(--ok)}
.descargas .card b{font-size:1.02rem}.descargas .card small{color:var(--mut)}
.controles{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}
.controles input,.controles select{padding:10px 12px;border:1px solid var(--lin);border-radius:8px;background:var(--card);color:var(--fg);font-size:1rem}
.controles input{flex:1;min-width:14rem}
.area-cab{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px;align-items:baseline;margin-top:22px}
.area-cab h3{margin:0;font-size:1.25rem}.area-cab a{font-size:.9rem}
details.lista{margin:8px 0;border:1px solid var(--lin);border-radius:10px;background:var(--card);padding:6px 12px}
details.lista summary{cursor:pointer;font-weight:600;padding:4px 0}
details.lista ul{columns:2 16rem;margin:6px 0;padding-left:1.2em}
footer{max-width:72rem;margin:0 auto;padding:22px 18px 48px;color:var(--mut);font-size:.88rem;border-top:1px solid var(--lin)}
.oculto{display:none!important}
"""

JS = r"""
(function(){
 var D=window.DATOS,KEY='astro-programa-progreso',en_linea=location.protocol!=='file:';
 var hecho=new Set();try{hecho=new Set(JSON.parse(localStorage.getItem(KEY)||'[]'))}catch(e){}
 function guardar(){try{localStorage.setItem(KEY,JSON.stringify(Array.from(hecho)))}catch(e){}pintaProgreso()}
 function $(s){return document.querySelector(s)}
 function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function norm(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()}
 var total=D.stats.bloques;
 function pintaProgreso(){var n=hecho.size,p=total?Math.round(n*100/total):0;$('#progreso').textContent=n+'/'+total+' · '+p+'%'}
 // estadísticas
 var S=D.stats,st=[[S.areas,'áreas'],[S.bloques,'bloques'],[S.clases,'clases'],[S.roles,'roles'],[S.anexos,'anexos'],[S.terminos,'términos']];
 $('#stats').innerHTML=st.map(function(x){var v=(typeof x[0]==='number')?String(x[0]).replace(/\B(?=(\d{3})+(?!\d))/g,'.'):x[0];return '<div class="stat"><strong>'+esc(v)+'</strong>'+x[1]+'</div>'}).join('')+'<div class="stat"><strong id="progreso">0</strong>bloques completados</div>';
 // descargas (solo en línea)
 var d=D.descargas;
 if(en_linea){
  $('#descargas').innerHTML=
   '<div class="grid descargas">'+
   '<a class="card" href="'+d.general+'"><b>📕 Programa general (PDF)</b><small>Guías de roles y bloques, anexos y glosarios</small></a>'+
   '<a class="card" href="'+d.release+'"><b>🖥️ Windows</b><small>ZIP portable · '+esc(d.windows)+'</small></a>'+
   '<a class="card" href="'+d.release+'"><b>📱 Android</b><small>APK · '+esc(d.android)+'</small></a>'+
   '<a class="card" href="'+d.release+'"><b>🔐 Verificación</b><small>SHA256SUMS.txt y notas de la versión</small></a></div>'+
   '<details class="lista"><summary>📕 PDF por área (12)</summary><ul>'+D.areas.map(function(a){return '<li><a href="'+d.base+a.pdf+'">'+esc(a.id+' · '+a.titulo)+'</a></li>'}).join('')+'</ul></details>'+
   '<details class="lista"><summary>📕 PDF por rol (24)</summary><ul>'+D.roles.map(function(r){return '<li><a href="'+d.base+r.pdf+'">'+esc(r.id+' · '+r.nombre)+'</a></li>'}).join('')+'</ul></details>';
 }else{$('#sec-descargas').classList.add('oculto');$('#btn-desc').classList.add('oculto')}
 // roles
 $('#roles').innerHTML=D.roles.map(function(r){return '<article class="card"><div class="meta"><span>'+r.id+'</span>'+(en_linea?'<a href="'+d.base+r.pdf+'">PDF</a>':'')+'</div><h3>'+esc(r.nombre)+'</h3><p>'+esc(r.resumen)+'</p><div class="act"><a href="'+r.guia+'">Abrir la guía del rol</a></div></article>'}).join('');
 // anexos y glosarios
 $('#anexos').innerHTML='<div class="grid">'+D.anexos.map(function(a){return '<a class="card" href="'+a.href+'"><h3>'+esc(a.titulo)+'</h3></a>'}).join('')+'</div>';
 // áreas y bloques
 var sel=$('#area');D.areas.forEach(function(a){var o=document.createElement('option');o.value=a.id;o.textContent=a.id+' · '+a.titulo;sel.appendChild(o)});
 function render(){
  var q=norm($('#q').value.trim()),af=sel.value,html='';
  D.areas.forEach(function(a){
   if(af&&a.id!==af)return;
   var bl=a.bloques.filter(function(b){return !q||norm(b.id+' '+b.titulo+' '+b.resumen).indexOf(q)>=0});
   if(!bl.length)return;
   html+='<div class="area-cab"><h3>'+a.id+' · '+esc(a.titulo)+'</h3>'+(en_linea?'<a href="'+d.base+a.pdf+'">📕 PDF del área</a>':'')+'</div><div class="grid">';
   bl.forEach(function(b){var ok=hecho.has(b.id);
    html+='<article class="card'+(ok?' done':'')+'"><div class="meta"><span>'+b.id+'</span><span>'+b.n+' clases</span></div><h3>'+esc(b.titulo)+'</h3><p>'+esc(b.resumen)+'</p>'+
     '<div class="act"><span><a href="'+b.guia+'">Guía del bloque</a>'+(b.clase1?' · <a href="'+b.clase1+'">Primera clase</a>':'')+'</span>'+
     '<label><input type="checkbox" class="hecho" data-id="'+b.id+'"'+(ok?' checked':'')+'> completado</label></div></article>'});
   html+='</div>'});
  $('#catalogo').innerHTML=html||'<p>Sin resultados.</p>';
  [].forEach.call(document.querySelectorAll('.hecho'),function(c){c.addEventListener('change',function(){if(c.checked)hecho.add(c.dataset.id);else hecho.delete(c.dataset.id);guardar();c.closest('.card').classList.toggle('done',c.checked)})});
 }
 $('#q').addEventListener('input',render);sel.addEventListener('change',render);render();pintaProgreso();
 if('serviceWorker' in navigator&&en_linea){navigator.serviceWorker.register('service-worker.js').catch(function(){})}
})();
"""


def pagina_inicio(d: dict) -> str:
    s = d["stats"]
    cl = f"{s['clases']:,}".replace(",", ".")
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#070b17">
<meta name="application-version" content="{d['version']}">
<meta name="description" content="Programa de formación independiente: {s['areas']} áreas, {s['bloques']} bloques, {cl} clases y {s['roles']} rutas profesionales de astronomía, astrofísica, ciencias espaciales e ingeniería aeroespacial.">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(TITULO)}">
<meta property="og:description" content="{s['areas']} áreas · {s['bloques']} bloques · {cl} clases · {s['roles']} roles — del cielo observable a la ingeniería de misiones.">
<meta property="og:url" content="{URL_PAGES}">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/svg+xml" href="assets/icon.svg">
<link rel="apple-touch-icon" href="assets/icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<link rel="stylesheet" href="assets/landing.css">
<title>{esc(TITULO)}</title>
</head>
<body>
<header class="hero">
  <span class="eyebrow">Programa de formación independiente · v{d['version']} · 2026</span>
  <h1>Del cielo observable a la <span class="gradient">ingeniería de misiones</span></h1>
  <p class="lead">Un solo programa de {s['areas']} áreas, {s['bloques']} bloques y {cl} clases: astronomía, astrofísica, ciencias planetarias, mecánica orbital, ingeniería de sistemas espaciales, operaciones, astronáutica, derecho y gestión. Los {s['roles']} roles profesionales son rutas sobre el mismo contenido.</p>
  <div class="stats" id="stats"></div>
  <div class="cta">
    <a class="btn btn-primary" href="#catalogo-sec">🚀 Explorar áreas y bloques</a>
    <a class="btn" href="#roles-sec">🧭 Roles profesionales</a>
    <a class="btn" href="buscar.html">🔎 Buscar</a>
    <a class="btn" href="#sec-descargas" id="btn-desc">⬇️ Descargas y PDF</a>
    <a class="btn" href="{URL_REPO}" rel="noopener">⭐ Repositorio</a>
  </div>
  <div class="aviso">{esc(AVISO)}</div>
</header>
<section class="sec" id="sec-descargas"><h2>⬇️ Descargas</h2>
  <p>Los enlaces apuntan siempre a la <b>última versión</b> publicada. Funcionan sin conexión una vez descargados.</p>
  <div id="descargas"></div></section>
<section class="sec" id="catalogo-sec"><h2>📚 Áreas, bloques y clases</h2>
  <p>Marca los bloques que completas: el progreso se guarda solo en tu navegador.</p>
  <div class="controles"><input id="q" type="search" placeholder="Buscar bloque o tema…"><select id="area"><option value="">Todas las áreas</option></select></div>
  <div id="catalogo"></div></section>
<section class="sec" id="roles-sec"><h2>🧭 Roles profesionales</h2>
  <p>Cada rol es una ruta ordenada sobre áreas y bloques; su guía indica qué clases usar.</p>
  <div class="grid" id="roles"></div></section>
<section class="sec"><h2>📎 Anexos y glosarios</h2>
  <p>Lecturas de contexto históricas, pedagógicas y de cálculo, y vocabulario explicado a fondo.</p>
  <div class="grid"><a class="card" href="glosario/esencial/README.html"><h3>🔤 Glosario esencial</h3><p>Conceptos clave con intuición, fórmula, ejemplo y errores frecuentes.</p></a>
  <a class="card" href="glosario/README.html"><h3>🔤 Glosario completo</h3><p>{s['terminos']} términos, {s['siglas']} siglas y {s['simbolos']} símbolos, con enlaces a sus clases.</p></a>
  <a class="card" href="PROGRAMA_ACADEMICO_COMPLETO.html"><h3>🗺️ Programa completo</h3><p>Índice unificado de todas las clases.</p></a>
  <a class="card" href="visor/index.html"><h3>🌐 Visor del catálogo</h3><p>Explorador del catálogo estructurado.</p></a></div>
  <div id="anexos"></div></section>
<footer>Código: Apache-2.0 · Contenido: CC BY-NC-SA 4.0 · Sin rastreo: el progreso permanece en tu navegador. ·
<a href="{URL_REPO}" rel="noopener">GitHub</a> · <a href="README.html">Acerca del programa</a></footer>
<script src="assets/datos.js"></script>
<script src="assets/landing.js"></script>
</body>
</html>
"""


def icono_svg() -> str:
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="96" fill="#0d1b3e"/>'
            '<circle cx="256" cy="256" r="170" fill="none" stroke="#79b8ff" stroke-width="18"/>'
            '<circle cx="256" cy="256" r="84" fill="#ffcd50"/><circle cx="378" cy="146" r="22" fill="#f0f0ff"/></svg>')


def service_worker(version: str) -> str:
    return f"""const CACHE = "programa-aeroespacial-v{version}";
const BASE = ["./", "./index.html", "./assets/landing.css", "./assets/landing.js", "./assets/datos.js", "./assets/icon.svg", "./buscar.html", "./estilos.css"];
self.addEventListener("install", e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(BASE))));
self.addEventListener("activate", e => e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== CACHE).map(x => caches.delete(x))))));
self.addEventListener("fetch", e => {{
  if (e.request.method !== "GET") return;
  e.respondWith(fetch(e.request).then(r => {{ const c = r.clone(); caches.open(CACHE).then(ch => ch.put(e.request, c)); return r; }}).catch(() => caches.match(e.request)));
}});
"""


def escribir(web: Path):
    from PIL import Image, ImageDraw
    d = datos_landing()
    (web / "assets").mkdir(exist_ok=True)
    (web / "assets" / "landing.css").write_text(CSS, encoding="utf-8")
    (web / "assets" / "landing.js").write_text(JS, encoding="utf-8")
    (web / "assets" / "datos.js").write_text("window.DATOS=" + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    (web / "assets" / "icon.svg").write_text(icono_svg(), encoding="utf-8")
    for n in (192, 512):
        im = Image.new("RGB", (n, n), (13, 27, 62))
        dr = ImageDraw.Draw(im)
        dr.ellipse((n * .17, n * .17, n * .83, n * .83), outline=(121, 184, 255), width=max(3, n // 28))
        dr.ellipse((n * .32, n * .32, n * .68, n * .68), fill=(255, 205, 80))
        dr.ellipse((n * .66, n * .22, n * .76, n * .32), fill=(240, 240, 255))
        im.save(web / "assets" / f"icon-{n}.png")
    (web / "manifest.webmanifest").write_text(json.dumps({
        "name": TITULO, "short_name": "Programa Aeroespacial", "start_url": "./index.html", "display": "standalone",
        "background_color": "#070b17", "theme_color": "#070b17", "lang": "es",
        "icons": [{"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": "assets/icon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"}]},
        ensure_ascii=False, indent=2), encoding="utf-8")
    (web / "service-worker.js").write_text(service_worker(d["version"]), encoding="utf-8")
    (web / "index.html").write_text(pagina_inicio(d), encoding="utf-8")
    # visor del catálogo (el explorador anterior se conserva en /visor/)
    import shutil
    (web / "visor").mkdir(exist_ok=True)
    shutil.copy2(ROOT / "visor" / "index.html", web / "visor" / "index.html")
    return d
