# SPDX-License-Identifier: Apache-2.0
"""Construye el sitio de documentación y lectura (también lo usan las aplicaciones sin conexión).

Salida: build/web/  — misma estructura que el repositorio, con .md -> .html, y:
  - navegación lateral en árbol (assets/nav.js), índice de cada página, migas, anterior/siguiente,
    enlace «Editar en GitHub», búsqueda y tema claro/oscuro;
  - página de inicio (landing.py), áreas, roles y búsqueda.
Uso: python herramientas/publicacion/sitio.py
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import time
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: E402,F401,F403
import generar_rutas_por_rol as gr  # noqa: E402
import landing  # noqa: E402

GH = f"https://github.com/{landing.REPO}"

# ------------------------------------------------------------------ estilos y scripts del sitio

CSS = r"""
:root{--bg:#f4f7fb;--fg:#142335;--mut:#567089;--lin:#d8e1e8;--card:#ffffff;--ac:#205e8d;--ac2:#6d4fc2;--cod:#eef2f6;--sup:#ffffff;--ok:#1f8a4c;--aviso:#fff7e6;--peli:#fdecec;--info:#e8f3fd}
:root[data-tema="oscuro"]{--bg:#070b17;--fg:#e8edf7;--mut:#9aa8c2;--lin:#1f2a44;--card:#0f1730;--ac:#7cc4ff;--ac2:#a78bfa;--cod:#141d38;--sup:#0b1226;--ok:#4ade80;--aviso:#2a2210;--peli:#2d1518;--info:#0f2236}
@media (prefers-color-scheme:dark){:root:not([data-tema="claro"]){--bg:#070b17;--fg:#e8edf7;--mut:#9aa8c2;--lin:#1f2a44;--card:#0f1730;--ac:#7cc4ff;--ac2:#a78bfa;--cod:#141d38;--sup:#0b1226;--ok:#4ade80;--aviso:#2a2210;--peli:#2d1518;--info:#0f2236}}
*{box-sizing:border-box}html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
a{color:var(--ac)}
.top{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;height:52px;padding:0 14px;background:var(--sup);border-bottom:1px solid var(--lin)}
.top .marca{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--fg);font-weight:700;white-space:nowrap}
.top .marca span{overflow:hidden;text-overflow:ellipsis}
.top button{border:1px solid var(--lin);background:var(--card);color:var(--fg);border-radius:8px;height:34px;min-width:34px;cursor:pointer;font-size:1rem}
#menu{display:none}
.buscador{flex:1;max-width:30rem;margin-left:auto}
.buscador input{width:100%;height:34px;padding:0 12px;border:1px solid var(--lin);border-radius:8px;background:var(--card);color:var(--fg);font-size:.95rem}
.top .gh{color:var(--mut);text-decoration:none;font-size:.9rem}
.marco{display:grid;grid-template-columns:19rem minmax(0,1fr) 15rem;max-width:96rem;margin:0 auto}
.lateral{position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto;padding:14px 10px 40px 14px;border-right:1px solid var(--lin);background:var(--sup);font-size:.9rem}
.lateral ul{list-style:none;margin:0;padding-left:.9rem}.lateral>ul{padding-left:0}
.lateral li{margin:1px 0}
.lateral a{display:block;padding:3px 8px;border-radius:6px;color:var(--fg);text-decoration:none;line-height:1.35}
.lateral a:hover{background:var(--cod)}
.lateral a[aria-current="page"]{background:var(--ac);color:#fff;font-weight:600}
.lateral details>summary{cursor:pointer;padding:3px 8px;border-radius:6px;font-weight:600;list-style:none;display:flex;gap:6px;align-items:baseline}
.lateral details>summary::before{content:"▸";color:var(--mut);font-size:.8em;transition:transform .15s}
.lateral details[open]>summary::before{transform:rotate(90deg)}
.lateral details>summary:hover{background:var(--cod)}
.lateral details>summary a{display:inline;padding:0;font-weight:600}
.lateral .sec>summary{text-transform:uppercase;letter-spacing:.05em;font-size:.74rem;color:var(--mut);margin-top:10px}
.cuerpo{min-width:0;padding:18px 28px 56px}
.migas{font-size:.82rem;color:var(--mut);margin-bottom:6px}.migas a{color:var(--mut)}
article{max-width:52rem;overflow-wrap:anywhere}
article h1{font-size:1.9rem;line-height:1.2;margin:.2em 0 .6em;padding-bottom:.3em;border-bottom:1px solid var(--lin)}
article h2{font-size:1.42rem;margin:1.9em 0 .5em;padding-bottom:.25em;border-bottom:1px solid var(--lin);scroll-margin-top:64px}
article h3{font-size:1.15rem;margin:1.5em 0 .4em;scroll-margin-top:64px}article h4{scroll-margin-top:64px}
article img{max-width:100%;height:auto}
article table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;margin:1em 0}
article th,article td{border:1px solid var(--lin);padding:6px 10px;vertical-align:top}article th{background:var(--card)}
article code{background:var(--cod);padding:.1em .35em;border-radius:4px;font:0.88em Consolas,"Cascadia Mono",monospace}
article pre{background:var(--cod);padding:12px 14px;border-radius:8px;overflow-x:auto;position:relative;border:1px solid var(--lin)}
article pre code{background:none;padding:0}
article blockquote{margin:1em 0;padding:.1em 1em;border-left:4px solid var(--lin);color:var(--mut)}
article details{margin:.8em 0;border:1px solid var(--lin);border-radius:8px;padding:6px 12px;background:var(--card)}
article summary{cursor:pointer}
.alerta{margin:1.1em 0;padding:10px 16px;border-radius:8px;border-left:5px solid var(--ac);background:var(--info);color:var(--fg)}
.alerta p{margin:.4em 0}.alerta .etiq{display:block;font-weight:700;text-transform:uppercase;font-size:.78rem;letter-spacing:.06em}
.alerta.a-important,.alerta.a-warning,.alerta.a-caution{background:var(--aviso);border-left-color:#e0a100}.alerta.a-caution{background:var(--peli);border-left-color:#d23}
.diagrama-svg{background:#fff;border:1px solid var(--bd,#ddd);border-radius:8px;padding:10px;overflow-x:auto;text-align:center}.diagrama-svg svg{max-width:100%;height:auto}.diagrama{margin:1em 0}.diagrama figcaption{font-size:.8rem;color:var(--mut)}
.enlace-ausente{border-bottom:1px dotted var(--mut);cursor:help}
.copiar{position:absolute;top:6px;right:6px;font-size:.72rem;padding:2px 8px;border:1px solid var(--lin);border-radius:6px;background:var(--card);color:var(--mut);cursor:pointer;opacity:0}
article pre:hover .copiar{opacity:1}
.indice{position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto;padding:18px 14px;font-size:.82rem}
.indice b{display:block;text-transform:uppercase;letter-spacing:.06em;font-size:.72rem;color:var(--mut);margin-bottom:6px}
.indice a{display:block;padding:2px 0 2px 8px;color:var(--mut);text-decoration:none;border-left:2px solid transparent}
.indice a.h3{padding-left:20px}.indice a.act{color:var(--ac);border-left-color:var(--ac)}
.pie-pag{max-width:52rem;margin-top:40px;padding-top:16px;border-top:1px solid var(--lin);display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;font-size:.9rem}
.pie-pag a.nav{display:block;padding:8px 12px;border:1px solid var(--lin);border-radius:8px;text-decoration:none;background:var(--card);max-width:100%}
.pie-pag small{display:block;color:var(--mut)}
.pie-pag .meta{flex-basis:100%;color:var(--mut);font-size:.8rem}
#q{width:100%;padding:12px;font-size:1.05rem;border:1px solid var(--lin);border-radius:8px;background:var(--card);color:var(--fg)}
.res{list-style:none;padding:0}.res li{padding:8px 0;border-bottom:1px solid var(--lin)}.res small{color:var(--mut);margin-left:8px}
.filtros button{margin:4px 6px 4px 0;padding:6px 12px;border:1px solid var(--lin);border-radius:20px;background:var(--card);color:var(--fg);cursor:pointer}
.filtros button.on{background:var(--ac);color:#fff;border-color:var(--ac)}
@media (max-width:1180px){.marco{grid-template-columns:18rem minmax(0,1fr)}.indice{display:none}}
@media (max-width:820px){
 #menu{display:inline-block}.top .gh{display:none}.top .marca span{max-width:9rem}
 .marco{display:block}
 .lateral{position:fixed;left:0;top:52px;bottom:0;width:min(21rem,88vw);height:auto;z-index:30;transform:translateX(-102%);transition:transform .2s;box-shadow:0 0 24px rgba(0,0,0,.35)}
 body.nav-abierta .lateral{transform:none}
 .cuerpo{padding:14px 14px 48px}
}
@media print{.top,.lateral,.indice,.pie-pag,.copiar{display:none!important}.marco{display:block}body{background:#fff;color:#000}}
"""

JS = r"""
(function(){
 var RAIZ=window.RAIZ||'',RUTA=window.RUTA||'',NAV=window.NAV||[];
 function $(s,c){return (c||document).querySelector(s)}
 var raiz=document.documentElement;
 var bt=$('#tema');if(bt)bt.addEventListener('click',function(){
  var oscuro=raiz.getAttribute('data-tema')==='oscuro'||(!raiz.getAttribute('data-tema')&&window.matchMedia('(prefers-color-scheme: dark)').matches);
  var n=oscuro?'claro':'oscuro';raiz.setAttribute('data-tema',n);try{localStorage.setItem('tema',n)}catch(e){}});
 var bm=$('#menu');if(bm)bm.addEventListener('click',function(){document.body.classList.toggle('nav-abierta')});
 var nav=$('#nav');
 function crea(nodo,pila){
  var li=document.createElement('li'),t=nodo[0],u=nodo[1],h=nodo[2];
  if(h&&h.length){
   var d=document.createElement('details'),s=document.createElement('summary');
   if(u){var a=document.createElement('a');a.href=RAIZ+u;a.textContent=t;if(u===RUTA)a.setAttribute('aria-current','page');s.appendChild(a)}else{s.textContent=t}
   d.appendChild(s);
   var abre=pila.indexOf(nodo)>=0;
   var llena=function(){if(d.dataset.listo)return;d.dataset.listo=1;var ul=document.createElement('ul');h.forEach(function(x){ul.appendChild(crea(x,pila))});d.appendChild(ul)};
   d.addEventListener('toggle',function(){if(d.open)llena()});
   if(abre){d.open=true;llena()}
   li.appendChild(d);
  }else{var a2=document.createElement('a');a2.href=RAIZ+u;a2.textContent=t;if(u===RUTA)a2.setAttribute('aria-current','page');li.appendChild(a2)}
  return li;
 }
 function camino(nodos,pila){for(var i=0;i<nodos.length;i++){var n=nodos[i];if(n[1]===RUTA&&!(n[2]&&n[2].length)){return true}
  if(n[2]&&camino(n[2],pila)){pila.push(n);return true}
  if(n[1]===RUTA){return true}}return false}
 if(nav){
  var pila=[];camino(NAV,pila);
  var ul=document.createElement('ul');
  NAV.forEach(function(sec){var li=document.createElement('li'),d=document.createElement('details'),s=document.createElement('summary');
   d.className='sec';s.textContent=sec[0];d.appendChild(s);var u2=document.createElement('ul');
   var abre=pila.indexOf(sec)>=0||(sec[3]===1&&!pila.length);
   var llena=function(){if(d.dataset.listo)return;d.dataset.listo=1;sec[2].forEach(function(x){u2.appendChild(crea(x,pila))});d.appendChild(u2)};
   d.addEventListener('toggle',function(){if(d.open)llena()});
   if(abre){d.open=true;llena()}li.appendChild(d);ul.appendChild(li)});
  nav.appendChild(ul);
  var act=$('a[aria-current="page"]',nav);if(act&&act.scrollIntoView)act.scrollIntoView({block:'center'});
 }
 var ind=$('#toc'),art=$('article');
 if(ind&&art){
  var hs=[].slice.call(art.querySelectorAll('h2[id],h3[id]'));
  if(hs.length>=2){
   var html='<b>En esta página</b>';hs.forEach(function(h){html+='<a class="'+h.tagName.toLowerCase()+'" href="#'+h.id+'">'+h.textContent+'</a>'});ind.innerHTML=html;
   if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){[].forEach.call(ind.querySelectorAll('a'),function(a){a.classList.toggle('act',a.getAttribute('href')==='#'+e.target.id)})}})},{rootMargin:'-60px 0px -70% 0px'});
    hs.forEach(function(h){io.observe(h)})}
  }else{ind.style.display='none'}
 }
 [].forEach.call(document.querySelectorAll('article pre'),function(p){var b=document.createElement('button');b.className='copiar';b.textContent='Copiar';
  b.addEventListener('click',function(){var c=p.querySelector('code');if(navigator.clipboard)navigator.clipboard.writeText((c||p).innerText).then(function(){b.textContent='Copiado';setTimeout(function(){b.textContent='Copiar'},1200)})});p.appendChild(b)});
 var q=$('.buscador input');document.addEventListener('keydown',function(e){if(e.key==='/'&&q&&document.activeElement.tagName!=='INPUT'){e.preventDefault();q.focus()}});
})();
"""

BUSCAR_JS = r"""
(function(){
 var q=document.getElementById('q'),out=document.getElementById('out'),cnt=document.getElementById('cnt'),tipo='Todo';
 function n(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();}
 var I=(window.INDICE||[]).map(function(r){return {t:r[0],u:r[1],k:r[2],n:n(r[0])}});
 var tipos=['Todo'];I.forEach(function(r){if(tipos.indexOf(r.k)<0)tipos.push(r.k)});
 var f=document.getElementById('filtros');
 tipos.forEach(function(k){var b=document.createElement('button');b.textContent=k;if(k==='Todo')b.className='on';
  b.onclick=function(){tipo=k;[].forEach.call(f.children,function(x){x.className=(x===b)?'on':''});run()};f.appendChild(b)});
 function run(){var v=n(q.value.trim()).split(/\s+/).filter(Boolean);out.innerHTML='';
  if(!v.length){cnt.textContent=I.length+' entradas indexadas';return}
  var r=[];for(var i=0;i<I.length&&r.length<300;i++){var e=I[i];if(tipo!=='Todo'&&e.k!==tipo)continue;
   var ok=true;for(var j=0;j<v.length;j++){if(e.n.indexOf(v[j])<0){ok=false;break}}if(ok)r.push(e)}
  cnt.textContent=r.length+(r.length>=300?'+':'')+' resultados';
  r.forEach(function(e){var li=document.createElement('li'),a=document.createElement('a');a.href=e.u;a.textContent=e.t;
   var s=document.createElement('small');s.textContent=e.k;li.appendChild(a);li.appendChild(s);out.appendChild(li)})}
 q.addEventListener('input',run);
 var m=/[?&]q=([^&]*)/.exec(location.search);if(m){try{q.value=decodeURIComponent(m[1].replace(/\+/g,' '))}catch(e){}}
 run();q.focus();
})();
"""

# ------------------------------------------------------------------ conversión

ALERTAS = {"NOTE": "Nota", "TIP": "Consejo", "IMPORTANT": "Importante", "WARNING": "Advertencia", "CAUTION": "Precaución"}


def md_a_html_sitio(texto: str) -> str:
    """Markdown -> HTML con alertas de GitHub, <details> con Markdown dentro y diagramas como texto."""
    marcas: list[str] = []

    def guarda(m):
        marcas.append(f"<details><summary>{m.group(1)}</summary>\n{md_a_html(m.group(2))}\n</details>")
        return f"\n\nDETALLESMARCA{len(marcas) - 1}FIN\n\n"

    texto = re.sub(r"<details>\s*<summary>(.*?)</summary>(.*?)</details>", guarda, texto, flags=re.S)
    html_ = md_a_html(texto)
    for i, bloque in enumerate(marcas):
        html_ = html_.replace(f"<p>DETALLESMARCA{i}FIN</p>", bloque)

    def alerta(m):
        tipo, resto = m.group(1), m.group(2)
        return f'<div class="alerta a-{tipo.lower()[:9]}"><p><span class="etiq">{ALERTAS[tipo]}</span>' + resto + "</div>"

    html_ = re.sub(r"<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*?)</blockquote>", alerta, html_, flags=re.S)
    html_ = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                   r'<figure class="diagrama"><pre><code>\1</code></pre><figcaption>Diagrama en texto: GitHub lo muestra dibujado.</figcaption></figure>', html_, flags=re.S)
    return html_


def prefijo(rel: Path) -> str:
    return "../" * (len(rel.parts) - 1)


def pagina(titulo: str, cuerpo: str, rel: Path, migas: str = "", pie: str = "") -> str:
    p = prefijo(rel)
    cabeza = (f'<header class="top"><button id="menu" aria-label="Abrir menú">☰</button>'
              f'<a class="marca" href="{p}index.html">🌌 <span>Programa Aeroespacial</span></a>'
              f'<form class="buscador" action="{p}buscar.html" method="get"><input name="q" type="search" placeholder="Buscar clases, bloques, términos…  ( / )" autocomplete="off" aria-label="Buscar"></form>'
              f'<a class="gh" href="{GH}" rel="noopener">GitHub</a><button id="tema" aria-label="Cambiar tema">◐</button></header>')
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(titulo)} · Programa Aeroespacial</title>'
            f'<script>try{{var t=localStorage.getItem("tema");if(t)document.documentElement.setAttribute("data-tema",t)}}catch(e){{}}</script>'
            f'<link rel="stylesheet" href="{p}assets/docs.css"></head><body>{cabeza}'
            f'<div class="marco"><nav id="nav" class="lateral" aria-label="Navegación del sitio"></nav>'
            f'<main class="cuerpo">{migas}<article>{cuerpo}</article>{pie}</main><aside id="toc" class="indice" aria-label="En esta página"></aside></div>'
            f'<script>window.RAIZ="{p}";window.RUTA="{rel.as_posix()}";</script>'
            f'<script src="{p}assets/nav.js"></script><script src="{p}assets/docs.js"></script></body></html>')


def reescribir_enlaces(cuerpo: str, rel: Path, existentes: set[str]) -> str:
    base = (WEB / rel).parent

    def sub(m):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#|data:|tel:)", href):
            return m.group(0)
        ruta, _, ancla = href.partition("#")
        ruta_dec = unquote(ruta)
        if not ruta_dec:
            return m.group(0)
        destino = (base / ruta_dec).resolve()
        try:
            relativo = destino.relative_to(WEB.resolve()).as_posix()
        except ValueError:
            return m.group(0)
        for pz in (relativo, re.sub(r"\.md$", ".html", relativo)):
            if pz in existentes:
                nuevo = re.sub(r"\.md$", ".html", ruta)
                return f'href="{nuevo}{"#" + ancla if ancla else ""}"'
        return 'data-ausente="1" href="#"'

    cuerpo = re.sub(r'href="([^"]*)"', sub, cuerpo)
    return re.sub(r'<a data-ausente="1" href="#"', '<a class="enlace-ausente" title="Disponible en el repositorio de código" data-ausente="1"', cuerpo)


# ------------------------------------------------------------------ navegación

GRUPOS_DOC = [
    ("Contrato y alcance", ["ALCANCE_Y_CONTRATO_DEL_REPOSITORIO", "ESTRUCTURA_Y_CONTEO_DEL_CATALOGO", "CONVENIOS_DE_IDENTIFICACION_Y_AMPLIACION", "MAPA_DEL_REPOSITORIO", "MAPA_DE_AREAS_Y_BLOQUES"]),
    ("Estándares", ["ESTANDAR_PARA_GENERAR_CONTENIDOS", "ESTANDAR_PEDAGOGICO_Y_DE_EVALUACION", "GUIA_DE_REDACCION_DE_CLASES", "ESTANDAR_DE_FUENTES", "ESTANDAR_VISUAL_Y_DE_EXPERIENCIA", "NIVELES_DE_VERIFICACION"]),
    ("Plan y estados", ["PLAN_DE_IMPLEMENTACION_Y_ESTADOS", "RESOLUCION_DE_CONTENIDOS_POR_ETAPAS", "PLAN_DE_REFINAMIENTO_CURRICULAR", "AMPLIACION_DEL_TRONCO_COMUN", "MATRIZ_DE_COBERTURA", "MAPA_DE_DEPENDENCIAS", "SYLLABUS_Y_CARGA"]),
    ("Roles y uso", ["MAPA_DE_RUTAS_PROFESIONALES", "GUIA_DE_RECORRIDOS_POR_ROL", "COMO_USAR_EL_PROGRAMA", "PORTAFOLIO_Y_EVIDENCIAS"]),
    ("Fuentes, seguridad y licencias", ["FUENTES_Y_EVIDENCIA", "SEGURIDAD_Y_ETICA_PROFESIONAL", "LICENCIAS_Y_PROCEDENCIA", "LICENSING_MATRIX", "LICENSING_HISTORY", "COMMERCIAL_USE"]),
]


def construir_nav(titulos: dict[str, str], areas, bloques, rutas) -> list:
    """Árbol [sección, None, hijos, abierta_por_defecto]; cada nodo [título, url, hijos|None]."""
    def hoja(rel_md: str, titulo: str | None = None):
        return [titulo or titulos.get(rel_md, Path(rel_md).stem), re.sub(r"\.md$", ".html", rel_md), None]

    existe = lambda r: r in titulos
    inicio = [["Portada", "index.html", None], ["Buscar", "buscar.html", None], ["Áreas, bloques y clases", "areas.html", None], ["Roles profesionales", "roles.html", None]]
    proyecto = [hoja(r) for r in ("README.md", "STATUS.md", "ROADMAP.md", "CHANGELOG.md", "SYLLABUS.md", "FILE_INDEX.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md") if existe(r)]
    lic = [hoja(r) for r in ("LICENSE-CONTENT.md", "DATA_LICENSES.md", "ASSET_LICENSES.md", "THIRD_PARTY_NOTICES.md", "TRADEMARKS.md", "LICENSING_AUDIT.md") if existe(r)]
    if lic:
        proyecto.append(["Licencias y marcas", None, lic])
    if existe("AGENTS.md"):
        proyecto.append(hoja("AGENTS.md"))

    doc = [hoja("documentacion/README.md")] if existe("documentacion/README.md") else []
    usados = {"documentacion/README.md"}
    for nombre, lista in GRUPOS_DOC:
        hs = []
        for s in lista:
            r = f"documentacion/{s}.md"
            if existe(r):
                hs.append(hoja(r))
                usados.add(r)
        if hs:
            doc.append([nombre, None, hs])
    otros = [hoja(r) for r in sorted(titulos) if r.startswith("documentacion/") and r not in usados]
    if otros:
        doc.append(["Otros", None, otros])

    prog = [hoja("PROGRAMA_ACADEMICO_COMPLETO.md")]
    for a, ta in areas.items():
        hb = []
        for bid, b in bloques.items():
            if b["area"] != a:
                continue
            g = guia_bloque(bid)
            hc = []
            for c in clases_de_bloque(bid):
                cid = c.parent.name
                num = cid.split("-")[1]
                nombre = titulos.get(c.relative_to(ROOT).as_posix(), cid).split("—", 1)[-1].strip()
                hc.append([f"{num} · {nombre}", f"programa/clases/{bid}/{cid}/CLASE.html", None])
            hb.append([f"{bid} · {b['titulo']}", f"programa/tronco-comun/{g.stem}.html" if g else None, hc])
        prog.append([f"{a} · {ta}", None, hb])

    rol = [hoja("rutas/README.md")] if existe("rutas/README.md") else []
    for r in rutas:
        rol.append([f"{r['id']} · {r['nombre']}", f"rutas/{gr.slug_de(r['id'])}.html", None])

    anex = [hoja(r) for r in sorted(titulos) if r.startswith("anexos/")]
    anex.sort(key=lambda n: (n[1] != "anexos/README.html", n[1]))

    tall = []
    if "talleres/README.md" in titulos:
        tall.append(hoja("talleres/README.md"))
    for td in sorted({Path(r).parts[1] for r in titulos if r.startswith("talleres/") and len(Path(r).parts) > 2}):
        hs = [hoja(r) for r in sorted(titulos, key=lambda x: (Path(x).name != "README.md", x)) if r.startswith(f"talleres/{td}/")]
        tall.append([td.split("-", 1)[0] + " · " + td.split("-", 1)[1].replace("-", " ").capitalize(), None, hs])

    sim = []
    if "simuladores/README.md" in titulos:
        sim.append(["Concentrador de simuladores", "simuladores/index.html", None])
        sim += [[t, f"simuladores/{h}", None] for t, h in SIMULADORES]
        sim.append(hoja("simuladores/README.md"))
        docs_sim = [hoja(r) for r in sorted(titulos, key=lambda x: (Path(x).name != "README.md", x)) if r.startswith("simuladores/documentacion/")]
        sim.append(["Documentación de los simuladores", None, docs_sim])

    glo = []
    gl_rel = sorted(r for r in titulos if r.startswith("glosario/"))

    def grupo(nombre, filtro):
        hs = [hoja(r) for r in gl_rel if filtro(r)]
        if hs:
            glo.append([nombre, None, hs])

    if "glosario/README.md" in titulos:
        glo.append(hoja("glosario/README.md"))
    grupo("Glosario esencial", lambda r: "/esencial/" in r)
    grupo("Términos más usados", lambda r: r.startswith("glosario/mas-usados"))
    grupo("Términos por letra", lambda r: r.startswith("glosario/terminos-"))
    grupo("Términos por área", lambda r: r.startswith("glosario/por-area"))
    grupo("Siglas", lambda r: r.startswith("glosario/siglas"))
    grupo("Símbolos y unidades", lambda r: r.startswith("glosario/simbolos"))

    tec = [hoja(r) for r in ("herramientas/publicacion/README.md", "catalogo/estructura/README.md", "fuentes/REFERENCIAS_INSTITUCIONALES_PRELIMINARES.md", "instrucciones/PROMPT_MAESTRO_DE_IMPLEMENTACION.md") if existe(r)]
    heredada = []
    for rid_dir in sorted({Path(r).parts[2] for r in titulos if r.startswith("programa/rutas-profesionales/") and len(Path(r).parts) > 3}):
        hs = [hoja(r) for r in sorted(titulos) if r.startswith(f"programa/rutas-profesionales/{rid_dir}/")]
        heredada.append([rid_dir, None, hs])
    if heredada:
        tec.append(["Capa heredada: módulos de ruta (línea base)", None, heredada])

    return [["Inicio", None, inicio, 1], ["Proyecto", None, proyecto], ["Documentación", None, doc], ["Programa", None, prog],
            ["Roles", None, rol], ["Anexos", None, anex], ["Talleres", None, tall], ["Simuladores", None, sim], ["Glosario", None, glo], ["Referencia técnica", None, tec]]


def hojas_planas(nodos, acum=None):
    acum = [] if acum is None else acum
    for n in nodos:
        if n[2]:
            hojas_planas(n[2], acum)
        elif n[1]:
            acum.append(n)
    return acum


def migas_de(rel_html: Path, rel_md: str) -> str:
    p = prefijo(rel_html)
    etiquetas = {"programa": "Programa", "clases": "Clases", "tronco-comun": "Guías de bloque", "rutas": "Roles", "anexos": "Anexos", "talleres": "Talleres", "simuladores": "Simuladores", "figuras": "Figuras", "glosario": "Glosario",
                 "documentacion": "Documentación", "esencial": "Esencial", "rutas-profesionales": "Capa heredada", "herramientas": "Herramientas", "catalogo": "Catálogo"}
    partes = [f'<a href="{p}index.html">Inicio</a>']
    for seg in Path(rel_md).parts[:-1]:
        if re.match(r"^B\d+$", seg):
            partes.append(seg)
        elif re.match(r"^B\d+-C\d+", seg) or re.match(r"^R\d\d-", seg):
            continue
        else:
            partes.append(etiquetas.get(seg, seg))
    return '<div class="migas">' + " › ".join(partes) + "</div>"


def pie_de(rel_md: str, anterior, siguiente, p: str) -> str:
    h = ""
    if anterior:
        h += f'<a class="nav" href="{p}{anterior[1]}"><small>← Anterior</small>{esc(anterior[0])}</a>'
    if siguiente:
        h += f'<a class="nav" href="{p}{siguiente[1]}" style="margin-left:auto;text-align:right"><small>Siguiente →</small>{esc(siguiente[0])}</a>'
    h += f'<div class="meta"><a href="{GH}/blob/main/{rel_md}" rel="noopener">✏️ Ver o editar este archivo en GitHub</a> · Publicación {VERSION}</div>'
    return f'<footer class="pie-pag">{h}</footer>'


# Simuladores interactivos (páginas HTML propias, fuera del generador de Markdown); el orden es el de simuladores/motor/navegacion.js
SIMULADORES = [("Sistema Solar", "sistema-solar.html"),
               ("Tierra · Sol · Luna", "tierra-sol-luna.html"),
               ("Marte y sus dos lunas", "marte.html"),
               ("Júpiter y sus lunas", "jupiter.html"),
               ("Saturno y sus lunas", "saturno.html"),
               ("Urano y sus lunas", "urano.html"),
               ("Neptuno y sus lunas", "neptuno.html"),
               ("Plutón y sus lunas", "pluton.html"),
               ("Cielo desde la Tierra", "cielo-tierra.html"),
               ("Cielo desde Marte", "cielo-marte.html"),
               ("Cielo desde Júpiter", "cielo-jupiter.html"),
               ("Cielo desde Saturno", "cielo-saturno.html"),
               ("Cielo desde Europa", "cielo-europa.html"),
               ("Cielo desde Titania", "cielo-titania.html"),
               ("Cielo desde Tritón", "cielo-triton.html"),
               ("Cielo desde Titán", "cielo-titan.html"),
               ("Trayectorias entre planetas", "trayectorias.html"),
               ("Eclipses solares", "eclipses-solares.html"),
               ("Misiones espaciales", "misiones.html"),
               ("Cinturón de asteroides", "asteroides.html")]


# ------------------------------------------------------------------ construcción

def construir():
    t0 = time.time()
    if WEB.exists():
        shutil.rmtree(WEB)
    (WEB / "assets").mkdir(parents=True)
    (WEB / "assets" / "docs.css").write_text(CSS, encoding="utf-8")
    (WEB / "assets" / "docs.js").write_text(JS, encoding="utf-8")
    (WEB / "buscar.js").write_text(BUSCAR_JS, encoding="utf-8")

    mds = archivos_md()
    rels_md = {p.relative_to(ROOT).as_posix(): p for p in mds}
    act = activos()
    existentes = set(re.sub(r"\.md$", ".html", r) for r in rels_md) | {a.relative_to(ROOT).as_posix() for a in act}
    existentes |= {"index.html", "buscar.html", "areas.html", "roles.html"}

    for a in act:
        d = WEB / a.relative_to(ROOT)
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(a, d)

    textos = {r: p.read_text(encoding="utf-8") for r, p in rels_md.items()}
    titulos = {r: titulo_de(t, Path(r).stem) for r, t in textos.items()}

    areas, bloques = bloques_y_areas()
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    nav = construir_nav(titulos, areas, bloques, rutas)
    (WEB / "assets" / "nav.js").write_text("window.NAV=" + json.dumps(nav, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")

    vecinos: dict[str, tuple] = {}
    for sec in nav:
        hs = hojas_planas(sec[2])
        for i, n_ in enumerate(hs):
            vecinos.setdefault(n_[1], (hs[i - 1] if i else None, hs[i + 1] if i + 1 < len(hs) else None))

    indice = []
    n = 0
    for rel_s, texto in textos.items():
        rel = Path(rel_s)
        rel_html = rel.with_suffix(".html")
        tit = titulos[rel_s]
        cuerpo = reescribir_enlaces(md_a_html_sitio(texto), rel_html, existentes)
        ant, sig = vecinos.get(rel_html.as_posix(), (None, None))
        salida = WEB / rel_html
        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_text(pagina(tit, cuerpo, rel_html, migas_de(rel_html, rel_s), pie_de(rel_s, ant, sig, prefijo(rel_html))), encoding="utf-8")
        n += 1
        ruta_html = rel_html.as_posix()
        if rel.parts[:2] == ("programa", "clases"):
            if rel.name == "CLASE.md":
                indice.append([tit, ruta_html, "Clase"])
        elif rel.parts[:2] == ("programa", "tronco-comun"):
            indice.append([tit, ruta_html, "Bloque"])
        elif rel.parts[0] == "anexos":
            indice.append([tit, ruta_html, "Anexo"])
        elif rel.parts[0] == "talleres":
            indice.append([tit, ruta_html, "Taller"])
        elif rel.parts[0] == "simuladores":
            indice.append([tit, ruta_html, "Simulador"])
        elif rel.parts[0] == "rutas":
            indice.append([tit, ruta_html, "Rol"])
        elif rel.parts[0] == "glosario":
            if re.match(r"(terminos|siglas|mas-usados|simbolos)", rel.name) or "esencial" in rel.parts:
                for h in re.findall(r"^### (.+)$", texto, re.M):
                    term = re.sub(r"[`\\]", "", h).strip()
                    indice.append([term, f"{ruta_html}#{slug_github(h.replace(chr(92), ''))}", "Glosario esencial" if "esencial" in rel.parts else "Glosario"])
        elif rel.parts[0] == "documentacion" or len(rel.parts) == 1:
            indice.append([tit, ruta_html, "Documento"])

    for t_, h_ in SIMULADORES:
        indice.append([t_, f"simuladores/{h_}", "Simulador"])
    landing.escribir(WEB)
    titulos_clase = {c.parent.name: titulos[c.relative_to(ROOT).as_posix()].split("—", 1)[-1].strip()
                     for bid in bloques for c in clases_de_bloque(bid)}
    cuerpo = "<h1>Áreas, bloques y clases</h1>"
    for a, ta in areas.items():
        cuerpo += f"<h2>{a} · {esc(ta)}</h2>"
        for bid, b in bloques.items():
            if b["area"] != a:
                continue
            g = guia_bloque(bid)
            enlace_g = f"programa/tronco-comun/{g.stem}.html" if g else "#"
            cuerpo += f'<h3><a href="{enlace_g}">{bid} · {esc(b["titulo"])}</a></h3><ul>'
            for c in clases_de_bloque(bid):
                cid = c.parent.name
                cuerpo += f'<li><a href="programa/clases/{bid}/{cid}/CLASE.html">{esc("-".join(cid.split("-")[:2]))}</a> · {esc(titulos_clase.get(cid, cid))}</li>'
            cuerpo += "</ul>"
    (WEB / "areas.html").write_text(pagina("Áreas, bloques y clases", cuerpo, Path("areas.html")), encoding="utf-8")

    cuerpo = "<h1>Roles profesionales</h1><p>Cada rol es una ruta sobre áreas y bloques; su guía indica qué clases usar.</p><ul>"
    for r in rutas:
        cuerpo += f'<li><a href="rutas/{gr.slug_de(r["id"])}.html"><b>{r["id"]}</b> · {esc(r["nombre"])}</a></li>'
    cuerpo += "</ul>"
    (WEB / "roles.html").write_text(pagina("Roles profesionales", cuerpo, Path("roles.html")), encoding="utf-8")

    cuerpo = ('<h1>Buscar</h1><input id="q" type="search" placeholder="Escribe un término, una clase, un bloque…" autocomplete="off">'
              '<div class="filtros" id="filtros"></div><p id="cnt"></p><ul class="res" id="out"></ul>'
              '<script src="indice-busqueda.js"></script><script src="buscar.js"></script>')
    (WEB / "buscar.html").write_text(pagina("Buscar", cuerpo, Path("buscar.html")), encoding="utf-8")
    indice.sort(key=lambda r: (r[2], sin_acentos(r[0])))
    (WEB / "indice-busqueda.js").write_text("window.INDICE=" + json.dumps(indice, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")

    tam = sum(f.stat().st_size for f in WEB.rglob("*") if f.is_file())
    print(f"Sitio: {n} páginas, {len(indice)} entradas de búsqueda, {tam/1e6:.1f} MB en {time.time()-t0:.0f} s")
    return n


if __name__ == "__main__":
    construir()
