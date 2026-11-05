#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Genera RECORRIDO.md de cada ruta a partir de metadatos/recorridos.json.

El JSON es la fuente de verdad; los RECORRIDO.md son derivados y no se editan a mano.
Uso:
    python herramientas/generar_recorridos.py          # reescribe
    python herramientas/generar_recorridos.py --check  # falla si algo está desactualizado
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validar_recorridos import expandir  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RUTAS = ROOT / "programa" / "rutas-profesionales"
ETIQUETA = {"fundamentos": "Fundamentos", "tronco": "Tronco común", "ruta": "Ruta", "integracion": "Integración"}


def titulos() -> dict[str, str]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        return {r["id"]: r["titulo"] for r in map(json.loads, (x for x in f if x.strip()))}


def formatear(tokens: list[str], t: dict[str, str]) -> str:
    partes = []
    for tok in tokens:
        ids = expandir(tok)
        if len(ids) == 1:
            partes.append(f"`{ids[0]}` {t.get(ids[0], '')}")
        else:
            partes.append(f"`{ids[0]}`–`{ids[-1].split('-')[-1]}` ({len(ids)} clases)")
    return "<br>".join(partes)


def carpeta(ruta_id: str) -> Path:
    return next(RUTAS.glob(f"{ruta_id}-*"))


def render(rol: dict, t: dict[str, str]) -> str:
    rid = rol["ruta_id"]
    out = [f"# {rid} — Recorrido del rol: {rol['rol']}", ""]
    if rol["estado"] != "definido":
        out += ["**Estado:** recorrido en definición. Todavía no se indica qué clases del tronco común y de la ruta usa este rol ni en qué orden.", "",
                f"[⬅️ Índice de la ruta](INDICE.md)", ""]
        return "\n".join(out)
    todas: list[str] = []
    for p in rol["pasos"]:
        for tok in p["clases"]:
            todas.extend(expandir(tok))
    tronco = [c for c in todas if c.startswith("B")]
    ruta = [c for c in todas if c.startswith("R")]
    oblig = []
    for p in rol["pasos"]:
        if p["tipo"] == "obligatoria":
            for tok in p["clases"]:
                oblig.extend(expandir(tok))
    out += [
        f"> {rol['resumen']}", "",
        f"- **Decide:** {rol['decide']}",
        f"- **Entrega:** {rol['entrega']}", "",
        f"**Alcance del recorrido:** {len(todas)} clases ({len(tronco)} del tronco común y {len(ruta)} de la ruta); {len(oblig)} obligatorias. "
        "No es una titulación: el avance se demuestra con evidencias, no cursando en orden por obligación.", "",
        "## Pasos en orden", "",
        "| # | Fase | Tipo | Clases | Capacidad que aporta | Nota |", "|---:|---|---|---|---|---|",
    ]
    for p in rol["pasos"]:
        nota = p.get("nota", "")
        if p.get("omitible_si"):
            nota = (nota + " " if nota else "") + f"Omitible si {p['omitible_si']}."
        out.append(f"| {p['orden']} | {ETIQUETA[p['fase']]} | {p['tipo']} | **{p['titulo']}**<br>{formatear(p['clases'], t)} | {p['capacidad']} | {nota} |")
    out += ["", "## Huecos detectados en el catálogo", ""]
    if rol["huecos"]:
        out += ["Temas que este rol necesita y que el catálogo `0.1.0` no cubre. Alimentan las [ampliaciones aditivas](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md); no cambian ningún ID existente.", ""]
        for h in rol["huecos"]:
            out.append(f"- **{h['tema']}.** {h['motivo']} *Propuesta:* {h['propuesta']}.")
    else:
        out.append("Ninguno detectado.")
    out += ["", "[⬅️ Índice de la ruta](INDICE.md)", ""]
    return "\n".join(out)


def main() -> int:
    check = "--check" in sys.argv
    datos = json.loads((ROOT / "metadatos" / "recorridos.json").read_text(encoding="utf-8"))
    t = titulos()
    desactualizados = []
    for rol in datos["roles"]:
        destino = carpeta(rol["ruta_id"]) / "RECORRIDO.md"
        nuevo = render(rol, t)
        actual = destino.read_text(encoding="utf-8").replace("\r\n", "\n") if destino.exists() else ""
        if actual != nuevo:
            desactualizados.append(destino)
            if not check:
                destino.write_text(nuevo, encoding="utf-8", newline="\n")
        indice = carpeta(rol["ruta_id"]) / "INDICE.md"
        txt = indice.read_text(encoding="utf-8").replace("\r\n", "\n")
        enlace = "- [Recorrido del rol: qué clases usar y en qué orden](RECORRIDO.md)"
        if enlace not in txt:
            desactualizados.append(indice)
            if not check:
                indice.write_text(txt.replace("\n## Módulos", f"\n## Recorrido\n\n{enlace}\n\n## Módulos", 1), encoding="utf-8", newline="\n")
    if check and desactualizados:
        print("Recorridos desactualizados en:")
        for d in desactualizados:
            print(" -", d.relative_to(ROOT).as_posix())
        return 1
    print("Recorridos al día." if check else f"Recorridos actualizados ({len(desactualizados)} archivos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
