# SPDX-License-Identifier: Apache-2.0
"""Valida los simuladores interactivos (`simuladores/`).

Comprueba:
  - que cada `datos/<sistema>.json` describe exactamente su `.bin` (desplazamientos, longitudes, formatos) y que ningún cuerpo
    supera su tolerancia de interpolación medida contra JPL Horizons;
  - que las pruebas del motor en Node (`pruebas/ejecutar.mjs`) pasan: interpolación, tiempo, orientación y eclipses frente al
    catálogo de la NASA;
  - que cada página HTML carga módulos y hojas de estilo que existen y que todo `import` relativo de los módulos se resuelve;
  - que los simuladores no cargan nada de internet (sólo datos y código propios, para que funcionen sin red en GitHub Pages);
  - que los enlaces relativos de los .md de `simuladores/` y las imágenes SVG que citan existen, y que los SVG versionados son
    exactamente los que regenera `herramientas/efemerides/generar_svg.py` a partir de los datos.
Uso: python herramientas/validar_simuladores.py
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[1]
SIM = RAIZ / "simuladores"
errores: list[str] = []
ENTORNO = {**os.environ, "PYTHONIOENCODING": "utf-8"}
SISTEMAS = ["sol", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]


def err(msg: str) -> None:
    errores.append(msg)
    print("ERROR", msg)


def datos() -> None:
    d = SIM / "datos"
    for n in SISTEMAS:
        j, b = d / f"{n}.json", d / f"{n}.bin"
        if not j.exists() and not b.exists():
            continue  # sistema aún no incorporado
        if not (j.exists() and b.exists()):
            err(f"datos/{n}: falta {'json' if not j.exists() else 'bin'}")
            continue
        meta = json.loads(j.read_text(encoding="utf-8"))
        tam = b.stat().st_size
        fin = 0
        ids = set()
        for c in meta["cuerpos"]:
            ids.add(c["id"])
            bytes_ = {"f64": 8, "f32": 4, "i16": 2}[c["fmt"]]
            if c["longitud"] != c["n"] * 3 * bytes_:
                err(f"datos/{n}/{c['nombre']}: longitud {c['longitud']} != n*3*{bytes_}")
            if c["offset"] != fin:
                err(f"datos/{n}/{c['nombre']}: desplazamiento no contiguo")
            fin = c["offset"] + c["longitud"]
            if c["jd_valido_ini"] > 2461406.5 + 1e-6:
                err(f"datos/{n}/{c['nombre']}: no cubre el 2027-01-01")
        if fin != tam:
            err(f"datos/{n}.bin: {tam} bytes y el json describe {fin}")
        if len(ids) != len(meta["cuerpos"]):
            err(f"datos/{n}: identificadores repetidos")
    if not (d / "verificacion.json").exists():
        err("datos/verificacion.json: falta")


def node() -> None:
    if not shutil.which("node"):
        err("Node.js no está instalado: no se pueden ejecutar las pruebas del motor")
        return
    r = subprocess.run(["node", str(SIM / "pruebas" / "ejecutar.mjs")], capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENTORNO)
    print(r.stdout.strip())
    if r.returncode != 0:
        err("pruebas del motor en Node: fallaron\n" + r.stdout[-1500:] + r.stderr[-800:])


def paginas() -> None:
    for h in sorted(SIM.glob("*.html")):
        t = h.read_text(encoding="utf-8")
        for m in re.finditer(r'(?:src|href)="([^"#]+)"', t):
            u = m.group(1)
            if "${" in u:
                continue  # plantilla de JavaScript
            if re.match(r"(https?:|mailto:|data:)", u):
                err(f"{h.name}: referencia externa {u} (los simuladores no cargan nada de internet)")
            elif not (SIM / u).exists() and not (u.endswith(".html") and (SIM / (u[:-5] + ".md")).exists()):
                err(f"{h.name}: no existe {u}")
        if "lang=" not in t or "<title>" not in t or 'name="viewport"' not in t:
            err(f"{h.name}: faltan lang, title o viewport")
    for js in list((SIM / "motor").glob("*.js")) + list((SIM / "paginas").glob("*.js")):
        t = js.read_text(encoding="utf-8")
        for m in re.finditer(r'from\s+"(\.[^"]+)"', t):
            if not (js.parent / m.group(1)).resolve().exists():
                err(f"{js.relative_to(RAIZ)}: import {m.group(1)} no existe")
        if re.search(r"https?://", re.sub(r"//.*|/\*.*?\*/", "", t, flags=re.S)) and "SPDX" in t:
            # sólo se permite una URL de licencia/documentación en comentarios, nunca en código
            code = "\n".join(l for l in t.splitlines() if not l.strip().startswith("//"))
            if re.search(r"""["'`]https?://""", code):
                err(f"{js.relative_to(RAIZ)}: URL externa en el código")
    css = SIM / "estilos.css"
    if re.search(r"url\(\s*['\"]?https?:", css.read_text(encoding="utf-8")):
        err("estilos.css: recurso externo")


def documentacion() -> None:
    enlace = re.compile(r"\]\(([^)#\s][^)\s]*)\)")
    mds = list(SIM.rglob("*.md"))
    for f in mds:
        for m in enlace.finditer(f.read_text(encoding="utf-8")):
            u = m.group(1)
            if re.match(r"(https?:|mailto:)", u):
                continue
            if u.split("#")[0].endswith(".html"):
                err(f"{f.relative_to(RAIZ)}: enlace relativo a .html ({u}); use la URL de GitHub Pages para la página funcional")
                continue
            if not (f.parent / u.split("#")[0]).resolve().exists():
                err(f"{f.relative_to(RAIZ)}: enlace roto {u}")


def svg() -> None:
    gen = RAIZ / "herramientas" / "efemerides" / "generar_svg.py"
    if not gen.exists():
        return
    r = subprocess.run([sys.executable, str(gen), "--check"], capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENTORNO)
    print(r.stdout.strip())
    if r.returncode != 0:
        err("figuras SVG desfasadas respecto de los datos:\n" + r.stdout[-800:] + r.stderr[-400:])


def tabla() -> None:
    t = RAIZ / "herramientas" / "efemerides" / "tabla_precision.py"
    r = subprocess.run([sys.executable, str(t), "--check"], capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENTORNO)
    print(r.stdout.strip())
    if r.returncode != 0:
        err("TABLA_DE_PRECISION.md desfasada respecto de los datos")


def coherencia() -> None:
    """La lista de simuladores es única: navegacion.js (barra y concentrador), sitio.py (menú y búsqueda), páginas, imágenes y documentos."""
    nav = re.findall(r'clave: "(\w+)", imagen: "([\w-]+)", href: "([\w.-]+)"', (SIM / "motor" / "navegacion.js").read_text(encoding="utf-8"))
    sitio = re.findall(r'\("[^"]+", "([\w.-]+\.html)"\)', (RAIZ / "herramientas" / "publicacion" / "sitio.py").read_text(encoding="utf-8").split("SIMULADORES = [", 1)[1].split("]", 1)[0])
    if [h for _, _, h in nav] != sitio:
        err(f"simuladores/motor/navegacion.js y herramientas/publicacion/sitio.py no listan los mismos simuladores: {[h for _, _, h in nav]} vs {sitio}")
    for clave, imagen, href in nav:
        for ruta in (SIM / href, SIM / "img" / f"{imagen}.svg", SIM / "paginas" / f"{href[:-5]}.js", SIM / "documentacion" / f"{href[:-5]}.md"):
            if not ruta.exists():
                err(f"simulador {clave}: falta {ruta.relative_to(RAIZ)}")
        if clave != "sol" and not (SIM / "datos" / f"{clave}.bin").exists():
            err(f"simulador {clave}: faltan datos/{clave}.bin")
    doc = (SIM / "documentacion" / "README.md").read_text(encoding="utf-8")
    for _, _, href in nav:
        if f"{href[:-5]}.md" not in doc:
            err(f"documentacion/README.md no enlaza {href[:-5]}.md")


def main() -> int:
    if not SIM.exists():
        err("falta simuladores/")
    else:
        datos()
        paginas()
        documentacion()
        coherencia()
        node()
        tabla()
        svg()
    print(f"\n{len(errores)} errores")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
