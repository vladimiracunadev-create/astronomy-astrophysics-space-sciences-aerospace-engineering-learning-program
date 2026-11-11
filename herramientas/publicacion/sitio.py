# SPDX-License-Identifier: Apache-2.0
"""Construye el sitio HTML sin conexión (lo usan las aplicaciones de Windows y Android).

Salida: build/web/  (misma estructura que el repositorio; .md -> .html; páginas de inicio, áreas, roles y búsqueda).
Uso: python herramientas/publicacion/sitio.py
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: E402,F401,F403
import generar_rutas_por_rol as gr  # noqa: E402

CSS = """
:root{--bg:#fff;--fg:#1b1f24;--mut:#59636e;--lin:#d0d7de;--ac:#0b57d0;--sup:#f6f8fa;--cod:#eff1f3}
@media (prefers-color-scheme:dark){:root{--bg:#0d1117;--fg:#e6edf3;--mut:#9da7b3;--lin:#30363d;--ac:#79b8ff;--sup:#161b22;--cod:#1f2630}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.barra{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:4px 14px;padding:8px 16px;background:var(--sup);border-bottom:1px solid var(--lin)}
.barra a{color:var(--fg);text-decoration:none;font-weight:600;padding:4px 2px}
.barra a:hover{color:var(--ac)}
.contenido{max-width:60rem;margin:0 auto;padding:16px 16px 56px;overflow-wrap:anywhere}
h1,h2,h3,h4{line-height:1.25;margin:1.6em 0 .5em}h1{font-size:1.75rem;border-bottom:1px solid var(--lin);padding-bottom:.3em;margin-top:.6em}
h2{font-size:1.4rem;border-bottom:1px solid var(--lin);padding-bottom:.25em}h3{font-size:1.18rem}
a{color:var(--ac)}img{max-width:100%;height:auto}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;margin:1em 0}
th,td{border:1px solid var(--lin);padding:6px 10px;vertical-align:top}th{background:var(--sup)}
code{background:var(--cod);padding:.1em .35em;border-radius:4px;font:0.9em Consolas,"Cascadia Mono",monospace}
pre{background:var(--cod);padding:12px;border-radius:6px;overflow-x:auto}pre code{background:none;padding:0}
blockquote{margin:1em 0;padding:.2em 1em;border-left:4px solid var(--lin);color:var(--mut)}
.enlace-ausente{border-bottom:1px dotted var(--mut);cursor:help}
footer.pie{max-width:60rem;margin:0 auto;padding:12px 16px 32px;color:var(--mut);font-size:.85rem;border-top:1px solid var(--lin)}
.tarjetas{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:12px;margin:1em 0}
.tarjetas a{display:block;padding:14px;border:1px solid var(--lin);border-radius:10px;background:var(--sup);text-decoration:none;color:var(--fg)}
.tarjetas a:hover{border-color:var(--ac)}.tarjetas b{display:block;margin-bottom:4px}.tarjetas span{color:var(--mut);font-size:.9rem}
#q{width:100%;padding:12px;font-size:1.05rem;border:1px solid var(--lin);border-radius:8px;background:var(--bg);color:var(--fg)}
.res{list-style:none;padding:0}.res li{padding:8px 0;border-bottom:1px solid var(--lin)}.res small{color:var(--mut);margin-left:8px}
.filtros button{margin:4px 6px 4px 0;padding:6px 12px;border:1px solid var(--lin);border-radius:20px;background:var(--sup);color:var(--fg);cursor:pointer}
.filtros button.on{background:var(--ac);color:#fff;border-color:var(--ac)}
@media print{.barra,footer.pie{display:none}}
"""

BUSCAR_JS = """
(function(){
 var q=document.getElementById('q'),out=document.getElementById('out'),cnt=document.getElementById('cnt'),tipo='Todo';
 function n(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}
 var I=(window.INDICE||[]).map(function(r){return {t:r[0],u:r[1],k:r[2],n:n(r[0])}});
 var tipos=['Todo'];I.forEach(function(r){if(tipos.indexOf(r.k)<0)tipos.push(r.k)});
 var f=document.getElementById('filtros');
 tipos.forEach(function(k){var b=document.createElement('button');b.textContent=k;if(k==='Todo')b.className='on';
  b.onclick=function(){tipo=k;[].forEach.call(f.children,function(x){x.className=(x===b)?'on':''});run()};f.appendChild(b)});
 function run(){var v=n(q.value.trim()).split(/\\s+/).filter(Boolean);out.innerHTML='';
  if(!v.length){cnt.textContent=I.length+' entradas indexadas';return}
  var r=[];for(var i=0;i<I.length&&r.length<300;i++){var e=I[i];if(tipo!=='Todo'&&e.k!==tipo)continue;
   var ok=true;for(var j=0;j<v.length;j++){if(e.n.indexOf(v[j])<0){ok=false;break}}if(ok)r.push(e)}
  cnt.textContent=r.length+(r.length>=300?'+':'')+' resultados';
  r.forEach(function(e){var li=document.createElement('li'),a=document.createElement('a');a.href=e.u;a.textContent=e.t;
   var s=document.createElement('small');s.textContent=e.k;li.appendChild(a);li.appendChild(s);out.appendChild(li)})}
 q.addEventListener('input',run);run();q.focus();
})();
"""


def prefijo(ruta_rel: Path) -> str:
    return "../" * (len(ruta_rel.parts) - 1)


def pagina(titulo: str, cuerpo: str, rel: Path) -> str:
    p = prefijo(rel)
    barra = (f'<header class="barra"><a href="{p}index.html">🏠 Inicio</a><a href="{p}buscar.html">🔎 Buscar</a>'
             f'<a href="{p}areas.html">📚 Áreas</a><a href="{p}roles.html">🧭 Roles</a>'
             f'<a href="{p}anexos/README.html">📎 Anexos</a><a href="{p}glosario/README.html">🔤 Glosario</a>'
             f'<a href="{p}README.html">ℹ️ Acerca</a></header>')
    pie = f'<footer class="pie">{esc(TITULO)} · v{VERSION} · {esc(AVISO)}</footer>'
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(titulo)}</title>'
            f'<link rel="stylesheet" href="{p}estilos.css"></head><body>{barra}<main class="contenido">{cuerpo}</main>{pie}</body></html>')


def reescribir_enlaces(cuerpo: str, rel: Path, existentes: set[str]) -> str:
    base = (WEB / rel).parent

    def sub(m):
        href = m.group(1)
        if re.match(r"^(https?:|mailto:|#|data:|tel:)", href):
            return m.group(0)
        ruta, _, ancla = href.partition("#")
        ruta_dec = unquote(ruta)
        destino = (base / ruta_dec).resolve() if ruta_dec else None
        if destino is None:
            return m.group(0)
        try:
            relativo = destino.relative_to(WEB.resolve()).as_posix()
        except ValueError:
            return m.group(0)
        posible = [relativo, re.sub(r"\.md$", ".html", relativo)]
        for pz in posible:
            if pz in existentes:
                nuevo = re.sub(r"\.md$", ".html", ruta)
                return f'href="{nuevo}{"#" + ancla if ancla else ""}"'
        return 'data-ausente="1" href="#"'

    cuerpo = re.sub(r'href="([^"]*)"', sub, cuerpo)
    cuerpo = re.sub(r'<a data-ausente="1" href="#"', '<a class="enlace-ausente" title="Disponible en el repositorio de código" data-ausente="1"', cuerpo)
    return cuerpo


def construir():
    t0 = time.time()
    if WEB.exists():
        shutil.rmtree(WEB)
    WEB.mkdir(parents=True)
    (WEB / "estilos.css").write_text(CSS, encoding="utf-8")
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

    indice = []
    n = 0
    for rel_s, p in rels_md.items():
        rel = Path(rel_s)
        texto = p.read_text(encoding="utf-8")
        tit = titulo_de(texto, rel.stem)
        cuerpo = reescribir_enlaces(md_a_html(texto), rel.with_suffix(".html"), existentes)
        salida = WEB / rel.with_suffix(".html")
        salida.parent.mkdir(parents=True, exist_ok=True)
        salida.write_text(pagina(tit, cuerpo, rel.with_suffix(".html")), encoding="utf-8")
        n += 1
        # índice de búsqueda
        ruta_html = rel.with_suffix(".html").as_posix()
        if rel.parts[:2] == ("programa", "clases"):
            if p.name == "CLASE.md":
                indice.append([tit, ruta_html, "Clase"])
        elif rel.parts[:2] == ("programa", "tronco-comun"):
            indice.append([tit, ruta_html, "Bloque"])
        elif rel.parts[0] == "anexos":
            indice.append([tit, ruta_html, "Anexo"])
        elif rel.parts[0] == "rutas":
            indice.append([tit, ruta_html, "Rol"])
        elif rel.parts[0] == "glosario":
            if re.match(r"(terminos|siglas|mas-usados|simbolos)", rel.name) or "esencial" in rel.parts:
                for h in re.findall(r"^### (.+)$", texto, re.M):
                    term = re.sub(r"[`\\]", "", h).strip()
                    esenc = "esencial" in rel.parts
                    indice.append([term, f"{ruta_html}#{slug_github(h.replace(chr(92), ''))}", "Glosario esencial" if esenc else "Glosario"])
        elif rel.parts[0] == "documentacion" or len(rel.parts) == 1:
            indice.append([tit, ruta_html, "Documento"])

    # páginas propias
    areas, bloques = bloques_y_areas()
    titulos_clase = {}
    for bid in bloques:
        for c in clases_de_bloque(bid):
            titulos_clase[c.parent.name] = titulo_de(c.read_text(encoding="utf-8"), c.parent.name).split("—", 1)[-1].strip()

    import landing
    landing.escribir(WEB)

    cuerpo = "<h1>Áreas, bloques y clases</h1>"
    for a, ta in areas.items():
        cuerpo += f"<h2>{a} · {esc(ta)}</h2>"
        for bid, b in bloques.items():
            if b["area"] != a:
                continue
            g = guia_bloque(bid)
            enlace_g = f'programa/tronco-comun/{g.stem}.html' if g else "#"
            cuerpo += f'<h3><a href="{enlace_g}">{bid} · {esc(b["titulo"])}</a></h3><ul>'
            for c in clases_de_bloque(bid):
                cid = c.parent.name
                cuerpo += f'<li><a href="programa/clases/{bid}/{cid}/CLASE.html">{esc(cid.split("-")[0])}-{esc(cid.split("-")[1])}</a> · {esc(titulos_clase.get(cid, cid))}</li>'
            cuerpo += "</ul>"
    (WEB / "areas.html").write_text(pagina("Áreas y bloques", cuerpo, Path("areas.html")), encoding="utf-8")

    cuerpo = "<h1>Roles profesionales</h1><p>Cada rol es una ruta sobre áreas y bloques; su guía indica qué clases usar.</p><ul>"
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    for r in rutas:
        slug = gr.slug_de(r["id"])
        cuerpo += f'<li><a href="rutas/{slug}.html"><b>{r["id"]}</b> · {esc(r["nombre"])}</a></li>'
    cuerpo += "</ul>"
    (WEB / "roles.html").write_text(pagina("Roles", cuerpo, Path("roles.html")), encoding="utf-8")

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
