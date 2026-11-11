# SPDX-License-Identifier: Apache-2.0
"""Verifica los artefactos de la publicación abriéndolos y contando lo que llevan dentro.

Un build en verde no prueba que el artefacto esté completo: aquí se comprueba el contenido real.
Uso: python herramientas/publicacion/verificar.py
Sale con código 1 si algo no cuadra.
"""
from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: E402,F401,F403
import generar_rutas_por_rol as gr  # noqa: E402

FALLOS: list[str] = []


def ok(cond: bool, mensaje: str):
    print(("OK    " if cond else "FALLA ") + mensaje)
    if not cond:
        FALLOS.append(mensaje)


def verificar_pdfs():
    import fitz
    areas, bloques = bloques_y_areas()
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    bloque_d, uso, fund = gr.datos()
    # --- general
    f = DIST / "Programa-General.pdf"
    ok(f.exists(), f"existe {f.name}")
    if f.exists():
        d = fitz.open(f)
        toc = d.get_toc()
        ok(len(d) > 1000, f"{f.name}: {len(d)} páginas")
        titulos = " ".join(t[1] for t in toc)
        ok(sum(1 for t in toc if re.match(r"^R\d\d · ", t[1])) == 24, "general: 24 guías de rol")
        ok(sum(1 for t in toc if re.match(r"^B\d+ · ", t[1])) == 133, "general: 133 guías de bloque")
        ok(sum(1 for t in toc if t[1].startswith("Anexo ")) >= 20, "general: 20 anexos")
        ok("Glosario" in titulos, "general: contiene glosarios")
        # texto real en páginas clave
        for t in toc:
            if t[1].startswith("Anexo T"):
                txt = d[t[2] - 1].get_text()
                ok("Datos" in txt or "fuentes" in txt.lower(), "general: el Anexo T tiene texto en su primera página")
                break
    # --- áreas
    for a, ta in areas.items():
        esperado = sum(len(clases_de_bloque(b)) for b, x in bloques.items() if x["area"] == a)
        ff = next(DIST.glob(f"Area-{a}-*.pdf"), None)
        ok(ff is not None, f"existe PDF del área {a}")
        if ff:
            d = fitz.open(ff)
            toc = d.get_toc()
            n_clases = sum(1 for t in toc if re.match(r"^B\d+-C\d+ · ", t[1]))
            ok(n_clases == esperado, f"{ff.name}: {n_clases} de {esperado} clases en el índice ({len(d)} págs.)")
            # cada clase: la página del marcador debe contener su identificador
            malas = 0
            for t in toc:
                m = re.match(r"^(B\d+-C\d+) · ", t[1])
                if m and m.group(1) not in d[t[2] - 1].get_text():
                    malas += 1
            ok(malas == 0, f"{ff.name}: cada clase empieza en su página ({malas} desajustes)")
    # --- roles
    for r in rutas:
        rid = r["id"]
        ff = next(DIST.glob(f"Rol-{rid}-*.pdf"), None)
        ok(ff is not None, f"existe PDF del rol {rid}")
        if ff:
            d = fitz.open(ff)
            toc = d.get_toc()
            n_clases = sum(1 for t in toc if re.match(r"^B\d+-C\d+ · ", t[1]))
            ok(n_clases == len(uso[rid]), f"{ff.name}: {n_clases} de {len(uso[rid])} clases del rol ({len(d)} págs.)")


def verificar_apk():
    apk = DIST / f"Programa-Aeroespacial_v{VERSION}_Android.apk"
    ok(apk.exists(), f"existe {apk.name}")
    if not apk.exists():
        return
    with zipfile.ZipFile(apk) as z:
        nombres = z.namelist()
        n_clases = sum(1 for n in nombres if n.startswith("assets/web/programa/clases/") and n.endswith("CLASE.html"))
        ok(n_clases == 2077, f"APK: {n_clases} de 2077 páginas de clase")
        ok("assets/web/index.html" in nombres, "APK: index.html")
        ok("assets/web/indice-busqueda.js" in nombres, "APK: índice de búsqueda")
        ok("classes.dex" in nombres and "AndroidManifest.xml" in nombres, "APK: classes.dex y manifiesto")
        n_html = sum(1 for n in nombres if n.startswith("assets/web/") and n.endswith(".html"))
        esperado = sum(1 for _ in WEB.rglob("*.html"))
        ok(n_html == esperado, f"APK: {n_html} páginas HTML de {esperado}")
    from android import SDK
    bt = sorted((SDK / "build-tools").iterdir())[-1]
    r = subprocess.run(["cmd", "/c", str(bt / "apksigner.bat"), "verify", "--verbose", str(apk)], capture_output=True, text=True)
    ok(r.returncode == 0 and "Verified using v2 scheme (APK Signature Scheme v2): true" in r.stdout, "APK: firma v2 verificada")
    r = subprocess.run([str(bt / "aapt2.exe"), "dump", "badging", str(apk)], capture_output=True, text=True)
    ok("package: name='io.github.vladimiracunadev.programa'" in r.stdout and f"versionName='{VERSION}'" in r.stdout, "APK: paquete y versión correctos")


def verificar_windows():
    z = DIST / f"Programa-Aeroespacial_v{VERSION}_Windows.zip"
    ok(z.exists(), f"existe {z.name}")
    if not z.exists():
        return
    with zipfile.ZipFile(z) as zz:
        nombres = zz.namelist()
        ok(any(n.endswith("ProgramaAeroespacial.exe") for n in nombres), "Windows: lanzador .exe")
        n_clases = sum(1 for n in nombres if "/web/programa/clases/" in n and n.endswith("CLASE.html"))
        ok(n_clases == 2077, f"Windows: {n_clases} de 2077 páginas de clase")
        ok(zz.testzip() is None, "Windows: ZIP íntegro")


def verificar_sitio_en_navegador():
    """Abre el sitio en un navegador real: inicio, búsqueda y una clase."""
    from playwright.sync_api import sync_playwright
    errores_js = []
    with sync_playwright() as pw:
        try:
            nav = pw.chromium.launch()
        except Exception:
            nav = pw.chromium.launch(channel="msedge")
        pg = nav.new_page()
        pg.on("pageerror", lambda e: errores_js.append(str(e)))
        pg.goto((WEB / "index.html").as_uri())
        pg.wait_for_timeout(300)
        ok("ingeniería de misiones" in pg.inner_text("h1"), "sitio: el inicio muestra el título")
        ok(pg.locator("#catalogo .card").count() == 133, "sitio: el inicio lista los 133 bloques")
        ok(pg.locator("#roles .card").count() == 24, "sitio: el inicio lista los 24 roles")
        ok(pg.locator("#anexos .card").count() >= 20, "sitio: el inicio lista los anexos")
        pg.goto((WEB / "documentacion" / "MAPA_DEL_REPOSITORIO.html").as_uri())
        pg.wait_for_timeout(400)
        ok(pg.locator("#nav a[aria-current=page]").count() == 1, "docs: la navegación lateral marca la página actual")
        ok(pg.locator("#toc a").count() >= 3, "docs: la página tiene índice En esta página")
        ok(pg.locator(".migas").count() == 1, "docs: la página tiene migas")
        pg.goto((WEB / "buscar.html").as_uri())
        pg.fill("#q", "hohmann")
        pg.wait_for_timeout(300)
        n = pg.locator("#out li").count()
        ok(n >= 3, f"sitio: la búsqueda «hohmann» devuelve {n} resultados")
        pg.fill("#q", "ecuacion del cohete")
        pg.wait_for_timeout(300)
        ok(pg.locator("#out li").count() >= 1, "sitio: la búsqueda sin acentos encuentra «ecuación del cohete»")
        pg.goto((WEB / "programa" / "clases" / "B71" / "B71-C18-maniobra-de-hohmann" / "CLASE.html").as_uri())
        ok("Hohmann" in pg.inner_text("h1"), "sitio: la clase B71-C18 se abre")
        ok(pg.locator("table").count() >= 1, "sitio: la clase tiene tablas")
        nav.close()
    ok(not errores_js, f"sitio: sin errores de JavaScript ({len(errores_js)})")


if __name__ == "__main__":
    verificar_sitio_en_navegador()
    verificar_pdfs()
    verificar_apk()
    verificar_windows()
    print()
    if FALLOS:
        print(f"{len(FALLOS)} comprobaciones fallaron")
        sys.exit(1)
    print("Todas las comprobaciones pasaron")
