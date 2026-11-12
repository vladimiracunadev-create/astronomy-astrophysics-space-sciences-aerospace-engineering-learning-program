# SPDX-License-Identifier: Apache-2.0
"""Dibuja los diagramas Mermaid de los .md como SVG incrustable (sitio, apps y PDF).

Los .md no cambian: GitHub sigue dibujando Mermaid. Aquí cada diagrama se dibuja una sola vez con la librería
`mermaid` (instalada con pnpm en build/mermaid, fuera del repositorio) dentro de Chromium y se guarda en una caché
por huella del texto: build/mermaid/cache/<sha1>.svg. `comun.md_a_html` lee esa caché.

Uso:
  python herramientas/publicacion/mermaid_svg.py        # dibuja los que falten
  python herramientas/publicacion/mermaid_svg.py --check  # solo cuenta
"""
from __future__ import annotations

import hashlib
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERR = ROOT / "build" / "mermaid"
CACHE = HERR / "cache"
LIB = HERR / "node_modules" / "mermaid" / "dist" / "mermaid.min.js"
PAT = re.compile(r"```mermaid[ \t]*\r?\n(.*?)```", re.S)


def huella(fuente: str) -> str:
    return hashlib.sha1(fuente.strip().replace("\r\n", "\n").encode("utf-8")).hexdigest()[:20]


def leer(fuente: str) -> str | None:
    f = CACHE / (huella(fuente) + ".svg")
    return f.read_text(encoding="utf-8") if f.exists() else None


def fuentes() -> dict[str, str]:
    import subprocess
    res: dict[str, str] = {}
    lista = subprocess.check_output(["git", "ls-files", "*.md"], cwd=ROOT, text=True, encoding="utf-8").split("\n")
    for rel in lista:
        if not rel or rel.startswith((".claude", "build")):
            continue
        t = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        for m in PAT.finditer(t):
            res[huella(m.group(1))] = m.group(1).strip()
    return res


PAGINA = r"""<!doctype html><meta charset="utf-8"><body><script>%s</script><script>
mermaid.initialize({startOnLoad:false, theme:'neutral', themeVariables:{fontSize:'17px'}, securityLevel:'strict', flowchart:{htmlLabels:false, useMaxWidth:true},
  sequence:{useMaxWidth:true}, fontFamily:'Segoe UI, Arial, sans-serif'});
const ancho = svg => { const m = svg.match(/viewBox="[-\d.]+ [-\d.]+ ([\d.]+)/); return m ? parseFloat(m[1]) : 0; };
window.dibujar = async (id, src) => { try {
  let r = await mermaid.render('m'+id, src);
  if (ancho(r.svg) > 720 && /^\s*(flowchart|graph)\s+LR/.test(src)) {
    r = await mermaid.render('n'+id, src.replace(/^(\s*)(flowchart|graph)(\s+)LR/, '$1$2$3TB')); }
  return {ok:true, svg:r.svg, ancho:ancho(r.svg)}; }
  catch(e){ return {ok:false, error:String(e && e.message || e).slice(0,300)}; } };
</script></body>"""


def main() -> int:
    todos = fuentes()
    CACHE.mkdir(parents=True, exist_ok=True)
    faltan = {h: s for h, s in todos.items() if not (CACHE / (h + ".svg")).exists()}
    print(f"Diagramas distintos: {len(todos)} | por dibujar: {len(faltan)}")
    if "--check" in sys.argv or not faltan:
        return 1 if faltan and "--check" in sys.argv else 0
    if not LIB.exists():
        print("Falta la librería: cd build/mermaid && pnpm add mermaid@10.9.3 --ignore-scripts")
        return 2
    from playwright.sync_api import sync_playwright
    errores = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page()
        pag.set_content(PAGINA % LIB.read_text(encoding="utf-8").replace("</script", "<\\/script"))
        for i, (h, s) in enumerate(faltan.items(), 1):
            r = pag.evaluate("([i, s]) => window.dibujar(i, s)", [h, s])
            if r["ok"]:
                (CACHE / (h + ".svg")).write_text(r["svg"], encoding="utf-8")
            else:
                errores.append((h, r["error"], s[:60]))
            if i % 200 == 0:
                print(f"  {i}/{len(faltan)}", flush=True)
        nav.close()
    print(f"Dibujados: {len(faltan) - len(errores)} | con error: {len(errores)}")
    for e in errores[:15]:
        print("  ERROR", e)
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
