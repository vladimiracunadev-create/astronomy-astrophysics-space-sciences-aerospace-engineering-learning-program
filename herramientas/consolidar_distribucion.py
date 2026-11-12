#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Consolida la distribución de los módulos de las rutas en el tronco común.

Lee el campo `modulos` de metadatos/recorridos/Rxx.json (solo lectura) y escribe, en
catalogo/ampliaciones/estructura/, la propuesta aditiva:
  - distribucion_modulos.json : para cada par de clases de ruta (Rxx-Mxx-Cnn..Cmm) dónde vive su contenido;
  - clases_nuevas.jsonl       : temas sin clase en el tronco, con ID propuesto y solo título (no se redacta contenido);
  - bloques_nuevos.json       : bloques que la ampliación necesita crear;
  - TAMANOS_DE_AREA.md        : cuántas clases tendría cada área (no son iguales).
No toca catalogo/clases.* ni ningún ID existente. Uso:
    python herramientas/consolidar_distribucion.py          # reescribe
    python herramientas/consolidar_distribucion.py --check  # falla si está desactualizado
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import OrderedDict, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validar_recorridos import cargar_roles  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "catalogo" / "ampliaciones" / "estructura"
PAT_NUEVO = re.compile(r"^nuevo: (.+)$")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def cargar_base() -> tuple[dict[str, dict], dict[str, str], dict[str, str]]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        filas = [json.loads(x) for x in f if x.strip()]
    bloques = {r["bloque_id"]: r["area"] for r in filas if r["tipo"] == "tronco_comun"}
    nombres = {r["bloque_id"]: r["bloque_titulo"] for r in filas if r["tipo"] == "tronco_comun"}
    return {r["id"]: r for r in filas}, bloques, nombres


def construir() -> dict:
    _, area_de_bloque, nombre_bloque = cargar_base()
    nuevos_bloques: "OrderedDict[str, dict]" = OrderedDict()     # clave: (area, nombre normalizado)
    clases_nuevas: "OrderedDict[tuple, dict]" = OrderedDict()    # clave: (destino, título normalizado)
    siguiente_en_bloque: dict[str, int] = defaultdict(lambda: 21)
    distribucion: dict[str, dict] = {}
    claves_bloque: dict[tuple, str] = {}
    n_bloque = 1
    # primer paso: registrar los bloques nuevos en orden determinista (área, nombre)
    pendientes = []
    for rol in cargar_roles():
        for m in rol.get("modulos", []):
            for t in m["temas"]:
                if t["destino"] == "nueva":
                    mt = PAT_NUEVO.match(t["propuesta"]["bloque"])
                    if mt:
                        pendientes.append((t["propuesta"]["area"], mt.group(1)))
    for area, nombre in sorted(set((a, n) for a, n in pendientes), key=lambda x: (x[0], norm(x[1]))):
        bid = f"BP{n_bloque:02d}"
        n_bloque += 1
        claves_bloque[(area, norm(nombre))] = bid
        nuevos_bloques[bid] = {"id": bid, "nombre": nombre, "area": area, "estado": "propuesta", "clases": 0}
    siguiente_en_nuevo: dict[str, int] = defaultdict(lambda: 1)
    for rol in cargar_roles():
        for m in rol.get("modulos", []):
            for t in m["temas"]:
                if t["destino"] == "existente":
                    distribucion[t["clases_ruta"]] = {"tema": t["tema"], "destino": "existente", "tronco": t["tronco"]}
                    continue
                pr = t["propuesta"]
                mt = PAT_NUEVO.match(pr["bloque"])
                bloque = claves_bloque[(pr["area"], norm(mt.group(1)))] if mt else pr["bloque"]
                clave = (bloque, norm(pr["titulo"]))
                if clave not in clases_nuevas:
                    if mt:
                        n = siguiente_en_nuevo[bloque]
                        siguiente_en_nuevo[bloque] += 1
                        nuevos_bloques[bloque]["clases"] += 1
                    else:
                        n = siguiente_en_bloque[bloque]
                        siguiente_en_bloque[bloque] += 1
                    cid = f"{bloque}-C{n:02d}"
                    clases_nuevas[clave] = {
                        "id": cid, "tipo": "tronco_comun_ampliacion", "area": pr["area"], "bloque_id": bloque,
                        "bloque_titulo": nuevos_bloques[bloque]["nombre"] if mt else nombre_bloque.get(bloque, ""),
                        "titulo": pr["titulo"], "estado": "solo_titulo_y_referencia_preliminar",
                        "origen": [], "roles": [],
                    }
                c = clases_nuevas[clave]
                c["origen"].append(t["clases_ruta"])
                if rol["ruta_id"] not in c["roles"]:
                    c["roles"].append(rol["ruta_id"])
                distribucion[t["clases_ruta"]] = {"tema": t["tema"], "destino": "nueva", "tronco": [c["id"]]}
    return {"distribucion": distribucion, "clases": list(clases_nuevas.values()), "bloques": list(nuevos_bloques.values())}


def tamanos(datos: dict) -> str:
    _, area_de_bloque, _ = cargar_base()
    base = defaultdict(int)
    for b, a in area_de_bloque.items():
        base[a] += 20
    nuevas = defaultdict(int)
    for c in datos["clases"]:
        nuevas[c["area"]] += 1
    out = ["# Tamaños de área tras la distribución de los módulos de las rutas", "",
           "Generado por `herramientas/consolidar_distribucion.py`. Cada tema de un módulo de ruta que no tiene clase en el tronco común aparece como clase nueva (solo título, estado E0). Las áreas **no** tienen el mismo tamaño: crecen según lo que los roles necesitan. La línea base inicial no cambia.", "",
           "| Área | Clases base | Clases nuevas propuestas | Total |", "|---|---:|---:|---:|"]
    for a in sorted(base):
        out.append(f"| {a} | {base[a]} | {nuevas.get(a, 0)} | {base[a] + nuevas.get(a, 0)} |")
    out.append(f"| **Total** | **{sum(base.values())}** | **{sum(nuevas.values())}** | **{sum(base.values()) + sum(nuevas.values())}** |")
    out += ["", f"Temas de módulos de ruta ubicados hasta ahora: {len(datos['distribucion'])} de 1.920. "
            "Los roles sin mapa de módulos todavía no aportan a esta tabla.", ""]
    return "\n".join(out)


def main() -> int:
    check = "--check" in sys.argv
    datos = construir()
    archivos = {
        "distribucion_modulos.json": json.dumps(datos["distribucion"], ensure_ascii=False, indent=2) + "\n",
        "clases_nuevas.jsonl": "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in datos["clases"]),
        "bloques_nuevos.json": json.dumps(datos["bloques"], ensure_ascii=False, indent=2) + "\n",
        "TAMANOS_DE_AREA.md": tamanos(datos),
    }
    SALIDA.mkdir(parents=True, exist_ok=True)
    viejos = []
    for nombre, texto in archivos.items():
        destino = SALIDA / nombre
        actual = destino.read_text(encoding="utf-8").replace("\r\n", "\n") if destino.exists() else None
        if actual != texto:
            viejos.append(nombre)
            if not check:
                destino.write_text(texto, encoding="utf-8", newline="\n")
    if check and viejos:
        print("Distribución desactualizada:", ", ".join(viejos))
        return 1
    print("Distribución al día." if check else f"Distribución actualizada ({len(datos['clases'])} clases nuevas, {len(datos['bloques'])} bloques nuevos).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
