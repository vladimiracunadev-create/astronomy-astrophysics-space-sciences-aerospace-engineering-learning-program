#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Mantiene la navegación anterior/siguiente de las clases redactadas.

Lee catalogo/clases.jsonl (solo lectura) y, para cada clase que ya tiene
programa/clases/<bloque>/<id>-<slug>/CLASE.md, reescribe los bloques delimitados por
    <!-- nav:top --> ... <!-- /nav -->
    <!-- nav:bottom --> ... <!-- /nav -->
También enlaza, en la guía de cada bloque, el ID de las clases ya redactadas.
Si la clase vecina aún no existe, el enlace apunta a su fila en la guía del bloque.

Uso:
    python herramientas/actualizar_navegacion.py          # reescribe
    python herramientas/actualizar_navegacion.py --check  # falla si algo está desactualizado
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASES = ROOT / "programa" / "clases"
TRONCO = ROOT / "programa" / "tronco-comun"


def slug(titulo: str) -> str:
    base = unicodedata.normalize("NFD", titulo.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", base).strip("-")


def cargar() -> list[dict]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        return [json.loads(x) for x in f if x.strip() and '"tipo": "tronco_comun"' in x]


def carpeta(c: dict) -> Path:
    return CLASES / c["bloque_id"] / f'{c["id"]}-{slug(c["titulo"])}'


def guia(bloque_id: str) -> Path:
    return next(TRONCO.glob(f"{bloque_id}-*.md"))


def rel(desde: Path, hasta: Path) -> str:
    import os
    return os.path.relpath(hasta, desde).replace("\\", "/")


def enlace_a(c: dict, desde: Path) -> str:
    """Ruta a la clase si existe; si no, a su fila en la guía del bloque."""
    destino = carpeta(c) / "CLASE.md"
    if destino.exists():
        return rel(desde, destino)
    return rel(desde, guia(c["bloque_id"])) + f'#{c["id"].lower()}'


def bloques_navegacion(todas: list[dict], i: int) -> tuple[str, str]:
    c = todas[i]
    d = carpeta(c)
    ant = todas[i - 1] if i > 0 else None
    sig = todas[i + 1] if i + 1 < len(todas) else None
    prog = rel(d, ROOT / "README.md")
    blq = rel(d, guia(c["bloque_id"]))

    def etiqueta(x: dict, flecha_izq: bool) -> str:
        t = f'{x["id"]} — {x["titulo"]}'
        return f"[← Anterior: {t}]" if flecha_izq else f"[Siguiente: {t} →]"

    partes_top = [f"[🏠 Programa]({prog})", f"[📚 Bloque {c['bloque_id']}]({blq})"]
    partes_bot = []
    if ant:
        a = f'{etiqueta(ant, True)}({enlace_a(ant, d)})'
        partes_top.append(a)
        partes_bot.append(a)
    else:
        partes_bot.append(f"[← Inicio del bloque]({blq})")
    partes_bot.append(f"[📚 Bloque {c['bloque_id']}]({blq})")
    if sig:
        s = f'{etiqueta(sig, False)}({enlace_a(sig, d)})'
        partes_top.append(s)
        partes_bot.append(s)
    else:
        partes_bot.append(f"[Fin del bloque]({blq})")
    return " · ".join(partes_top), "---\n\n" + " · ".join(partes_bot)


def reemplazar(texto: str, marca: str, contenido: str) -> str:
    patron = re.compile(rf"(<!-- nav:{marca} -->\n).*?(\n?<!-- /nav -->)", re.S)
    if not patron.search(texto):
        raise ValueError(f"falta el marcador nav:{marca}")
    return patron.sub(lambda m: m.group(1) + contenido + "\n" + "<!-- /nav -->", texto, count=1)


def main() -> int:
    check = "--check" in sys.argv
    todas = cargar()
    pendientes = []
    for i, c in enumerate(todas):
        archivo = carpeta(c) / "CLASE.md"
        if not archivo.exists():
            continue
        original = archivo.read_text(encoding="utf-8").replace("\r\n", "\n")
        top, bot = bloques_navegacion(todas, i)
        nuevo = reemplazar(reemplazar(original, "top", top), "bottom", bot)
        if nuevo != original:
            pendientes.append(archivo)
            if not check:
                archivo.write_text(nuevo, encoding="utf-8", newline="\n")
    # Enlazar IDs en las guías de bloque
    for g in sorted(TRONCO.glob("B*.md")):
        original = g.read_text(encoding="utf-8").replace("\r\n", "\n")
        nuevo = original
        for c in todas:
            if c["bloque_id"] != g.name[:3]:
                continue
            archivo = carpeta(c) / "CLASE.md"
            if not archivo.exists():
                continue
            ruta = rel(g.parent, archivo)
            cid = c["id"]
            nuevo = re.sub(
                rf'\| (?:<a id="{cid.lower()}"></a>)?(?:\[{cid}\]\([^)]*\)|{cid}) \|',
                f'| <a id="{cid.lower()}"></a>[{cid}]({ruta}) |',
                nuevo,
            )
        if nuevo != original:
            pendientes.append(g)
            if not check:
                g.write_text(nuevo, encoding="utf-8", newline="\n")
    if check and pendientes:
        print("Navegación desactualizada en:")
        for p in pendientes:
            print(" -", p.relative_to(ROOT).as_posix())
        return 1
    print("Navegación al día." if check else f"Navegación actualizada ({len(pendientes)} archivos).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
