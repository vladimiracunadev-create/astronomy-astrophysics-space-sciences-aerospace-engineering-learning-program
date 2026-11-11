# SPDX-License-Identifier: Apache-2.0
"""Genera los PDF del programa: general, por área y por rol.

Cada unidad (clase, guía de bloque, anexo, archivo del glosario…) se imprime una sola vez a PDF con un
navegador Chromium (Playwright) y después se ensamblan los volúmenes con marcadores y numeración.

Uso:
    python herramientas/publicacion/pdf.py unidades     # imprime las unidades (reanuda si se interrumpe)
    python herramientas/publicacion/pdf.py ensamblar    # arma general, áreas y roles
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from comun import *  # noqa: E402,F401,F403
import generar_rutas_por_rol as gr  # noqa: E402

CSS_PDF = """
@page{size:A4;margin:18mm 16mm 20mm 16mm}
html{font:10.5pt/1.5 "Segoe UI",Arial,"Noto Sans",sans-serif;color:#111}
body{margin:0}
h1{font-size:19pt;margin:0 0 .5em;padding-bottom:.25em;border-bottom:2px solid #444;break-after:avoid}
h2{font-size:14.5pt;margin:1.3em 0 .4em;border-bottom:1px solid #aaa;padding-bottom:.15em;break-after:avoid}
h3{font-size:12pt;margin:1.1em 0 .3em;break-after:avoid}h4{font-size:10.8pt;break-after:avoid}
p,li{orphans:3;widows:3}
a{color:#0b3d91;text-decoration:none}
table{border-collapse:collapse;width:100%;margin:.7em 0;font-size:9pt;table-layout:auto}
th,td{border:1px solid #999;padding:3px 6px;vertical-align:top;overflow-wrap:anywhere;word-break:break-word}
th{background:#eee}tr{break-inside:avoid}
code{font:9pt Consolas,"Cascadia Mono",monospace;background:#f0f0f0;padding:0 2px;border-radius:2px}
pre{background:#f4f4f4;padding:6px 8px;border:1px solid #ddd;font-size:8.6pt;white-space:pre-wrap;word-break:break-word;break-inside:auto}
pre code{background:none;padding:0}
blockquote{margin:.8em 0;padding:.1em 1em;border-left:3px solid #999;color:#333;background:#fafafa}
img{max-width:100%;height:auto}
.unidad{break-before:page}.unidad:first-child{break-before:auto}
.portada{text-align:center;padding-top:60mm}
.portada h1{border:none;font-size:26pt}.portada .sub{font-size:15pt;margin:.8em 0}.portada .meta{margin-top:2em;color:#444}
.portada .aviso{margin:3em auto 0;max-width:140mm;font-size:9.5pt;color:#444;border:1px solid #bbb;padding:8px 12px}
.portada ul{display:inline-block;text-align:left;margin-top:1.5em}
"""


def html_unidad(rutas: list[Path], titulos_extra: list[str] | None = None) -> str:
    partes = []
    for i, p in enumerate(rutas):
        texto = p.read_text(encoding="utf-8")
        cuerpo = md_a_html(texto)
        # sin enlaces internos: texto plano; se conservan los enlaces http(s)
        cuerpo = re.sub(r'<a href="(?!https?:)[^"]*"[^>]*>(.*?)</a>', r"\1", cuerpo, flags=re.S)
        if i and titulos_extra:
            cuerpo = f"<h2>{esc(titulos_extra[i])}</h2>" + cuerpo
        partes.append(f'<section class="unidad">{cuerpo}</section>')
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS_PDF}</style></head><body>{"".join(partes)}</body></html>'


def html_portada(titulo: str, subtitulo: str, lineas: list[str], items: list[str] | None = None) -> str:
    lista = "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>" if items else ""
    cuerpo = (f'<div class="portada"><h1>{esc(titulo)}</h1><div class="sub">{esc(subtitulo)}</div>'
              f'<div class="meta">{"<br>".join(esc(x) for x in lineas)}</div>{lista}'
              f'<div class="aviso">{esc(AVISO)}</div></div>')
    return f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{CSS_PDF}</style></head><body>{cuerpo}</body></html>'


def registro_unidades():
    """Devuelve {id: (lista de rutas md, títulos extra)} de todo lo que se imprime."""
    U: dict[str, tuple[list[Path], list[str] | None]] = {}
    for f in ("README.md", "PROGRAMA_ACADEMICO_COMPLETO.md"):
        U["raiz-" + f[:-3]] = ([ROOT / f], None)
    for p in sorted((ROOT / "rutas").glob("*.md")):
        U["rutas-" + p.stem] = ([p], None)
    for p in sorted((ROOT / "anexos").glob("*.md")):
        U["anexos-" + p.stem] = ([p], None)
    for p in sorted((ROOT / "documentacion").glob("*.md")):
        U["doc-" + p.stem] = ([p], None)
    for p in sorted((ROOT / "glosario").rglob("*.md")):
        rel = p.relative_to(ROOT / "glosario").as_posix()
        if rel.startswith("por-area"):
            continue
        U["glosario-" + rel[:-3].replace("/", "-")] = ([p], None)
    areas, bloques = bloques_y_areas()
    for bid in bloques:
        g = guia_bloque(bid)
        if g:
            U["bloque-" + bid] = ([g], None)
        for c in clases_de_bloque(bid):
            fich = c.parent / "FICHA_EDITORIAL.md"
            rutas = [c] + ([fich] if fich.exists() else [])
            U["clase-" + c.parent.name.split("-")[0] + "-" + c.parent.name.split("-")[1]] = (rutas, ["", "Ficha editorial"] if fich.exists() else None)
    return U


async def imprimir(U, solo_faltantes=True, paralelo=6):
    from playwright.async_api import async_playwright
    UNIDADES.mkdir(parents=True, exist_ok=True)
    pend = []
    for uid, (rutas, extra) in U.items():
        destino = UNIDADES / f"{uid}.pdf"
        if solo_faltantes and destino.exists() and destino.stat().st_size > 1000 and destino.stat().st_mtime >= max(r.stat().st_mtime for r in rutas):
            continue
        pend.append((uid, rutas, extra, destino))
    print(f"Unidades por imprimir: {len(pend)} de {len(U)}", flush=True)
    if not pend:
        return
    cola: asyncio.Queue = asyncio.Queue()
    for x in pend:
        cola.put_nowait(x)
    hechos = 0
    t0 = time.time()
    errores = []
    async with async_playwright() as pw:
        try:
            nav = await pw.chromium.launch()
        except Exception:
            nav = await pw.chromium.launch(channel="msedge")

        async def trabajador():
            nonlocal hechos
            ctx = await nav.new_context()
            page = await ctx.new_page()
            while True:
                try:
                    uid, rutas, extra, destino = cola.get_nowait()
                except asyncio.QueueEmpty:
                    break
                try:
                    await page.set_content(html_unidad(rutas, extra), wait_until="load")
                    await page.pdf(path=str(destino), format="A4", print_background=True, prefer_css_page_size=True)
                except Exception as e:  # reintenta una vez
                    try:
                        await page.set_content(html_unidad(rutas, extra), wait_until="load")
                        await page.pdf(path=str(destino), format="A4", print_background=True, prefer_css_page_size=True)
                    except Exception as e2:
                        errores.append((uid, str(e2)[:120]))
                hechos += 1
                if hechos % 100 == 0:
                    print(f"  {hechos}/{len(pend)} ({time.time()-t0:.0f} s)", flush=True)
            await ctx.close()

        await asyncio.gather(*[trabajador() for _ in range(paralelo)])
        await nav.close()
    print(f"Impresas {hechos} unidades en {time.time()-t0:.0f} s; errores: {len(errores)}", flush=True)
    for e in errores[:10]:
        print("  ERROR", e)


async def imprimir_portada(nombre: str, html: str):
    from playwright.async_api import async_playwright
    UNIDADES.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        try:
            nav = await pw.chromium.launch()
        except Exception:
            nav = await pw.chromium.launch(channel="msedge")
        page = await nav.new_page()
        await page.set_content(html, wait_until="load")
        await page.pdf(path=str(UNIDADES / f"{nombre}.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
        await nav.close()


def ensamblar_volumen(salida: Path, entradas: list[tuple[int, str, str | None]], pie: str, bloque_paginas: int = 300):
    """entradas: (nivel, título del marcador, id de unidad o None si solo es encabezado).

    Cada unidad ya es un PDF con sus propias fuentes incrustadas. Para no repetirlas miles de veces sin pagar el
    coste cuadrático de `garbage=4` sobre todo el volumen, se agrupan las unidades en tramos de ~300 páginas,
    se deduplica cada tramo y después se concatenan los tramos.
    """
    import tempfile
    import fitz
    # 1) páginas de cada unidad
    paginas: dict[str, int] = {}
    for _, _, uid in entradas:
        if uid and uid not in paginas:
            f = UNIDADES / f"{uid}.pdf"
            if not f.exists():
                raise FileNotFoundError(f)
            with fitz.open(f) as s:
                paginas[uid] = len(s)
    # 2) marcadores con la página final de cada entrada
    toc, acum = [], 0
    for nivel, titulo, uid in entradas:
        toc.append([nivel, titulo, acum + 1])
        if uid:
            acum += paginas[uid]
    total = acum
    # 3) tramos deduplicados
    tmp = Path(tempfile.mkdtemp(prefix="vol-"))
    tramos: list[Path] = []
    actual, cuenta = [], 0

    def cerrar_tramo():
        nonlocal actual, cuenta
        if not actual:
            return
        d = fitz.open()
        for uid in actual:
            with fitz.open(UNIDADES / f"{uid}.pdf") as s:
                d.insert_pdf(s)
        ruta = tmp / f"t{len(tramos):04d}.pdf"
        d.save(ruta, garbage=4, deflate=True)
        d.close()
        tramos.append(ruta)
        actual, cuenta = [], 0

    for _, _, uid in entradas:
        if not uid:
            continue
        if actual and cuenta + paginas[uid] > bloque_paginas:
            cerrar_tramo()
        actual.append(uid)
        cuenta += paginas[uid]
    cerrar_tramo()
    # 4) volumen final
    doc = fitz.open()
    for r in tramos:
        with fitz.open(r) as s:
            doc.insert_pdf(s)
    assert len(doc) == total, (len(doc), total)
    ok, prev = [], 0
    for nv, tt, pg in toc:
        nv = min(nv, prev + 1)
        ok.append([nv, tt, min(pg, total)])
        prev = nv
    if ok and ok[0][0] != 1:
        ok[0][0] = 1
    doc.set_toc(ok)
    for i, page in enumerate(doc):
        if i == 0:
            continue
        r = page.rect
        texto = f"{pie}  -  Pag. {i + 1} de {total}"
        page.insert_text((r.width / 2 - 1.9 * len(texto), r.height - 20), texto, fontsize=7.5, fontname="helv", color=(0.35, 0.35, 0.35))
    doc.set_metadata({"title": pie, "author": "Programa Integral de Astronomia y Ciencias Espaciales", "subject": f"Version {VERSION}"})
    salida.parent.mkdir(parents=True, exist_ok=True)
    doc.save(salida, garbage=0, deflate=True)
    doc.close()
    for r in tramos:
        r.unlink(missing_ok=True)
    try:
        tmp.rmdir()
    except OSError:
        pass
    return total


def nombre_slug(s: str) -> str:
    s = sin_acentos(s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60]


def plan_volumenes():
    areas, bloques = bloques_y_areas()
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    bloque_d, uso, fund = gr.datos()
    vols = {}

    # --- General ---
    ent = [(1, "Portada", "portada-general"), (1, "Acerca del programa (README)", "raiz-README"),
           (1, "Programa completo: áreas, bloques y clases", "raiz-PROGRAMA_ACADEMICO_COMPLETO"),
           (1, "Guías de los 24 roles profesionales", None)]
    for r in rutas:
        ent.append((2, f"{r['id']} · {r['nombre']}", "rutas-" + gr.slug_de(r["id"])))
    ent.append((1, "Guías de los 133 bloques", None))
    for a, ta in areas.items():
        ent.append((2, f"{a} · {ta}", None))
        for bid, b in bloques.items():
            if b["area"] == a and guia_bloque(bid):
                ent.append((3, f"{bid} · {b['titulo']}", "bloque-" + bid))
    ent.append((1, "Anexos", None))
    for p in sorted((ROOT / "anexos").glob("*.md")):
        ent.append((2, titulo_de(p.read_text(encoding="utf-8"), p.stem), "anexos-" + p.stem))
    ent.append((1, "Documentación del programa", None))
    for p in sorted((ROOT / "documentacion").glob("*.md")):
        ent.append((2, titulo_de(p.read_text(encoding="utf-8"), p.stem), "doc-" + p.stem))
    ent.append((1, "Glosarios", None))
    for p in sorted((ROOT / "glosario").rglob("*.md")):
        rel = p.relative_to(ROOT / "glosario").as_posix()
        if rel.startswith("por-area"):
            continue
        ent.append((2, titulo_de(p.read_text(encoding="utf-8"), p.stem), "glosario-" + rel[:-3].replace("/", "-")))
    vols["Programa-General.pdf"] = ("Programa general con anexos y glosarios", ent)

    # --- Por área ---
    for a, ta in areas.items():
        ent = [(1, "Portada", f"portada-area-{a}")]
        for bid, b in bloques.items():
            if b["area"] != a:
                continue
            if guia_bloque(bid):
                ent.append((1, f"{bid} · {b['titulo']}", "bloque-" + bid))
            for c in clases_de_bloque(bid):
                cid = "-".join(c.parent.name.split("-")[:2])
                ent.append((2, f"{cid} · {titulo_de(c.read_text(encoding='utf-8'), cid).split('—', 1)[-1].strip()}", "clase-" + cid))
        vols[f"Area-{a}-{nombre_slug(ta)}.pdf"] = (f"Área {a} · {ta}", ent)

    # --- Por rol ---
    for r in rutas:
        rid = r["id"]
        ent = [(1, "Portada", f"portada-rol-{rid}"), (1, "Guía del rol", "rutas-" + gr.slug_de(rid))]
        por_bloque: dict[str, list[int]] = {}
        for cid in uso[rid]:
            por_bloque.setdefault(cid.split("-")[0], []).append(int(cid.split("-C")[1]))
        nucleo = sorted(por_bloque, key=lambda b: (gr.ORDEN_AREA.index(bloque_d[b]["area"]), int(b[1:])))
        fundamentos = [b for b in fund.get(rid, []) if b in bloque_d and b not in por_bloque]
        if fundamentos:
            ent.append((1, "Fundamentos (guías de los bloques)", None))
            for bid in fundamentos:
                if guia_bloque(bid):
                    ent.append((2, f"{bid} · {bloques[bid]['titulo']}", "bloque-" + bid))
        ent.append((1, "Núcleo del rol: bloques y clases", None))
        for bid in nucleo:
            if guia_bloque(bid):
                ent.append((2, f"{bid} · {bloques[bid]['titulo']}", "bloque-" + bid))
            for n in sorted(por_bloque[bid]):
                cid = f"{bid}-C{n:02d}"
                p = next((x for x in clases_de_bloque(bid) if x.parent.name.startswith(cid + "-")), None)
                if p:
                    ent.append((3, f"{cid} · {titulo_de(p.read_text(encoding='utf-8'), cid).split('—', 1)[-1].strip()}", "clase-" + cid))
        vols[f"Rol-{rid}-{nombre_slug(r['nombre'])}.pdf"] = (f"Rol {rid} · {r['nombre']}", ent)
    return vols, rutas, uso, fund, areas, bloques


def portadas(vols, rutas, uso, areas, bloques):
    """Genera (HTML) las portadas de cada volumen."""
    hoy = date.today().isoformat()
    res = {}
    res["portada-general"] = html_portada(TITULO, "Programa general con anexos y glosarios",
                                          [f"Versión {VERSION} · {hoy}", "12 áreas · 133 bloques · 2.077 clases · 24 roles",
                                           "Incluye: guías de roles y bloques, 20 anexos, documentación y glosarios (esencial y completo)",
                                           "Las clases están en los volúmenes por área y por rol"])
    for a, ta in areas.items():
        bl = [f"{bid} · {b['titulo']} ({len(clases_de_bloque(bid))} clases)" for bid, b in bloques.items() if b["area"] == a]
        res[f"portada-area-{a}"] = html_portada(TITULO, f"Área {a} · {ta}", [f"Versión {VERSION} · {hoy}", f"{len(bl)} bloques"], bl)
    for r in rutas:
        rid = r["id"]
        pb = {}
        for cid in uso[rid]:
            pb.setdefault(cid.split("-")[0], 0)
            pb[cid.split("-")[0]] += 1
        items = [f"{b} · {bloques[b]['titulo']}: {n} clases" for b, n in sorted(pb.items(), key=lambda x: int(x[0][1:]))]
        res[f"portada-rol-{rid}"] = html_portada(TITULO, f"Rol {rid} · {r['nombre']}",
                                                 [f"Versión {VERSION} · {hoy}", f"{len(uso[rid])} clases en {len(pb)} bloques"], items)
    return res


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    U = registro_unidades()
    if cmd == "unidades":
        asyncio.run(imprimir(U))
    elif cmd == "ensamblar":
        vols, rutas, uso, fund, areas, bloques = plan_volumenes()
        port = portadas(vols, rutas, uso, areas, bloques)
        pendientes = {k: v for k, v in port.items() if not (UNIDADES / f"{k}.pdf").exists()}
        if pendientes:
            async def hacer():
                for k, v in pendientes.items():
                    await imprimir_portada(k, v)
            asyncio.run(hacer())
        DIST.mkdir(parents=True, exist_ok=True)
        solo = sys.argv[2:]
        for nombre, (titulo, ent) in vols.items():
            if solo and not any(s in nombre for s in solo):
                continue
            t0 = time.time()
            total = ensamblar_volumen(DIST / nombre, ent, titulo)
            tam = (DIST / nombre).stat().st_size / 1e6
            print(f"{nombre}: {total} págs., {tam:.1f} MB ({time.time()-t0:.0f} s)", flush=True)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
