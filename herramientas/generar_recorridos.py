#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Genera RECORRIDO.md de cada ruta a partir de metadatos/recorridos/Rxx.json.

El JSON es la fuente de verdad; RECORRIDO.md es el documento vinculante del proceso del rol:
enlaza cada clase (a su página si ya está redactada, o a la guía de su bloque) en el orden
del recorrido y muestra dónde vive el contenido de cada módulo de la ruta.
Uso:
    python herramientas/generar_recorridos.py          # reescribe
    python herramientas/generar_recorridos.py --check  # falla si algo está desactualizado
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from actualizar_navegacion import carpeta as carpeta_clase, guia as guia_bloque, rel  # noqa: E402
from validar_recorridos import cargar_roles, expandir  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RUTAS = ROOT / "programa" / "rutas-profesionales"
ETIQUETA = {"fundamentos": "Fundamentos", "tronco": "Tronco común", "ruta": "Ruta", "integracion": "Integración"}


def catalogo() -> dict[str, dict]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        return {r["id"]: r for r in map(json.loads, (x for x in f if x.strip()))}


def dir_ruta(ruta_id: str) -> Path:
    return next(RUTAS.glob(f"{ruta_id}-*"))


def enlace(cid: str, cat: dict[str, dict], desde: Path) -> str:
    """Ruta a la página de la clase si existe; si no, a la guía del bloque (tronco) o al módulo (ruta)."""
    r = cat[cid]
    if cid.startswith("B"):
        pagina = carpeta_clase(r) / "CLASE.md"
        destino = pagina if pagina.exists() else guia_bloque(r["bloque_id"])
    else:
        destino = next(desde.glob(f"{r['modulo_id']}-*.md"))
    return rel(desde, destino)


def un_id(cid: str, cat: dict, desde: Path) -> str:
    return f"[`{cid}`]({enlace(cid, cat, desde)})"


def formatear(tokens: list[str], cat: dict, desde: Path) -> str:
    partes = []
    for tok in tokens:
        ids = expandir(tok)
        if len(ids) == 1:
            partes.append(f"{un_id(ids[0], cat, desde)} {cat[ids[0]]['titulo']}")
        else:
            partes.append(f"{un_id(ids[0], cat, desde)}–{un_id(ids[-1], cat, desde)} ({len(ids)} clases)")
    return "<br>".join(partes)


def lista_ids(ids: list[str], cat: dict, desde: Path) -> str:
    return ", ".join(un_id(i, cat, desde) for i in ids)


def render(rol: dict, cat: dict) -> str:
    rid = rol["ruta_id"]
    desde = dir_ruta(rid)
    out = [f"# {rid} — Recorrido del rol: {rol['rol']}", ""]
    if rol["estado"] != "definido":
        out += ["**Estado:** recorrido en definición. Todavía no se indica qué clases del tronco común usa este rol ni en qué orden.", "",
                "[⬅️ Índice de la ruta](INDICE.md)", ""]
        return "\n".join(out)
    todas: list[str] = []
    oblig: list[str] = []
    for p in rol["pasos"]:
        ids = [i for tok in p["clases"] for i in expandir(tok)]
        todas += ids
        if p["tipo"] == "obligatoria":
            oblig += ids
    tronco = [c for c in todas if c.startswith("B")]
    ruta = [c for c in todas if c.startswith("R")]
    out += [f"> {rol['resumen']}", "",
            f"- **Decide:** {rol['decide']}",
            f"- **Entrega:** {rol['entrega']}"]
    if (desde / "GUIA_DEL_ROL.md").exists():
        out.append("- **Guía del rol:** [qué es, qué no es y cómo es el trabajo](GUIA_DEL_ROL.md)")
    out += ["",
            f"**Alcance del recorrido:** {len(todas)} clases: {len(tronco)} del tronco común y {len(ruta)} propias de la ruta "
            f"(temas que aún no tienen clase en el tronco); {len(oblig)} obligatorias. "
            "Las clases del tronco se redactan una sola vez y se reutilizan; los módulos de la ruta no duplican contenido. "
            "No es una titulación: el avance se demuestra con evidencias.", "",
            "## Pasos en orden", "",
            "| # | Fase | Tipo | Clases | Capacidad que aporta | Nota |", "|---:|---|---|---|---|---|"]
    for p in rol["pasos"]:
        nota = p.get("nota", "")
        if p.get("omitible_si"):
            nota = (nota + " " if nota else "") + f"Omitible si {p['omitible_si']}."
        out.append(f"| {p['orden']} | {ETIQUETA[p['fase']]} | {p['tipo']} | **{p['titulo']}**<br>{formatear(p['clases'], cat, desde)} | {p['capacidad']} | {nota} |")
    out += ["", "## Dónde vive el contenido de cada módulo de la ruta", "",
            "Cada módulo de la ruta es una lista de 10 temas. Su contenido pertenece al área y bloque del tronco común que corresponde; cuando el tema aún no existe allí, se propone una clase nueva (ver [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md)).", ""]
    if "modulos" not in rol:
        out += ["*Pendiente:* todavía no se ha ubicado cada tema de los módulos de esta ruta en el tronco común. Mientras tanto, el recorrido usa los módulos de la ruta como referencia (ver el [índice de la ruta](INDICE.md)).", ""]
    for m in rol.get("modulos", []):
        out += [f"### {m['modulo']} — {m['nombre']}", "", "| Clases de la ruta | Tema | Contenido en el tronco común |", "|---|---|---|"]
        for t in m["temas"]:
            if t["destino"] == "existente":
                donde = lista_ids(t["tronco"], cat, desde)
            else:
                pr = t["propuesta"]
                donde = f"**Clase nueva propuesta** en {pr['area']} · {pr['bloque']}: {pr['titulo']}"
            out.append(f"| `{t['clases_ruta']}` | {t['tema']} | {donde} |")
        out.append("")
    out += ["## Huecos detectados en el catálogo", ""]
    if rol["huecos"]:
        out += ["Temas que este rol necesita y que el catálogo `0.1.0` no cubre. Alimentan la [ampliación del tronco común](../../../documentacion/AMPLIACION_DEL_TRONCO_COMUN.md); no cambian ningún ID existente.", ""]
        for h in rol["huecos"]:
            out.append(f"- **{h['tema']}.** {h['motivo']} *Propuesta:* {h['propuesta']}.")
    else:
        out.append("Ninguno detectado.")
    out += ["", "[⬅️ Índice de la ruta](INDICE.md)", ""]
    return "\n".join(out)


def main() -> int:
    check = "--check" in sys.argv
    cat = catalogo()
    desactualizados = []
    for rol in cargar_roles():
        d = dir_ruta(rol["ruta_id"])
        destino = d / "RECORRIDO.md"
        nuevo = render(rol, cat)
        actual = destino.read_text(encoding="utf-8").replace("\r\n", "\n") if destino.exists() else ""
        if actual != nuevo:
            desactualizados.append(destino)
            if not check:
                destino.write_text(nuevo, encoding="utf-8", newline="\n")
        indice = d / "INDICE.md"
        txt = indice.read_text(encoding="utf-8").replace("\r\n", "\n")
        enlace_ind = "- [Recorrido del rol: qué clases usar y en qué orden](RECORRIDO.md)"
        if enlace_ind not in txt:
            desactualizados.append(indice)
            if not check:
                indice.write_text(txt.replace("\n## Módulos", f"\n## Recorrido\n\n{enlace_ind}\n\n## Módulos", 1), encoding="utf-8", newline="\n")
    if check and desactualizados:
        print("Recorridos desactualizados en:")
        for d in desactualizados:
            print(" -", d.relative_to(ROOT).as_posix())
        return 1
    print("Recorridos al día." if check else f"Recorridos actualizados ({len(desactualizados)} archivos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
