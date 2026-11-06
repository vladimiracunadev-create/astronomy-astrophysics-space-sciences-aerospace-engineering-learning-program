#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Valida metadatos/recorridos/Rxx.json (un archivo por rol): qué clases usa cada rol y en qué orden.

Comprueba contra catalogo/clases.jsonl (solo lectura) que:
- están las 24 rutas, una vez cada una;
- cada recorrido «definido» tiene pasos con orden consecutivo, fase, tipo y capacidad;
- todos los IDs y rangos existen en el catálogo y no se repite ninguna clase en un rol;
- las fases respetan el orden fundamentos -> (tronco | ruta) -> integracion;
- el mapa de módulos ubica cada tema de los 8 módulos en una clase del tronco (existente) o propone una clase nueva,
  y los pasos incluyen todo lo que ese mapa exige.
No valida corrección pedagógica: eso requiere revisión humana.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FASES = ["fundamentos", "tronco", "ruta", "integracion"]
TIPOS = {"obligatoria", "recomendada", "opcional"}
PAT_B = re.compile(r"^(B\d{2,3})-C(\d{2})(?:\.\.C(\d{2}))?$")
PAT_M = re.compile(r"^(R\d{2}-M\d{2})-C(\d{2})(?:\.\.C(\d{2}))?$")


def cargar_catalogo() -> set[str]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        return {json.loads(x)["id"] for x in f if x.strip()}


def expandir(token: str) -> list[str]:
    m = PAT_B.match(token) or PAT_M.match(token)
    if not m:
        raise ValueError(f"formato inválido: {token!r}")
    pref, a, b = m.group(1), int(m.group(2)), m.group(3)
    b = int(b) if b else a
    if a > b:
        raise ValueError(f"rango invertido: {token!r}")
    return [f"{pref}-C{n:02d}" for n in range(a, b + 1)]


def cargar_roles() -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "metadatos" / "recorridos").glob("R*.json"))]


def main() -> int:
    errores: list[str] = []
    avisos: list[str] = []
    ids = cargar_catalogo()
    datos = {"roles": cargar_roles()}
    rutas = json.loads((ROOT / "metadatos" / "rutas.json").read_text(encoding="utf-8"))
    esperadas = {r["id"]: r for r in rutas}
    vistas = [r["ruta_id"] for r in datos["roles"]]
    if sorted(vistas) != sorted(esperadas):
        errores.append(f"las rutas del recorrido no coinciden con metadatos/rutas.json: {sorted(set(esperadas) ^ set(vistas))}")
    definidos = 0
    conjuntos: dict[str, set[str]] = {}
    resumen = []
    for rol in datos["roles"]:
        rid = rol["ruta_id"]
        if rol.get("estado") == "pendiente":
            continue
        if rol.get("estado") != "definido":
            errores.append(f"{rid}: estado debe ser 'definido' o 'pendiente'")
            continue
        definidos += 1
        for campo in ("rol", "resumen", "decide", "entrega", "pasos"):
            if not rol.get(campo):
                errores.append(f"{rid}: falta {campo}")
        if "huecos" not in rol:
            errores.append(f"{rid}: falta el campo huecos (puede ser una lista vacía)")
        for h in rol.get("huecos", []):
            if not (h.get("tema") and h.get("motivo") and h.get("propuesta")):
                errores.append(f"{rid}: cada hueco requiere tema, motivo y propuesta")
        pasos = rol.get("pasos", [])
        if [p.get("orden") for p in pasos] != list(range(1, len(pasos) + 1)):
            errores.append(f"{rid}: el campo orden no es consecutivo desde 1")
        usadas: set[str] = set()
        ult_fase = -1
        for p in pasos:
            n = p.get("orden")
            if p.get("fase") not in FASES:
                errores.append(f"{rid} paso {n}: fase inválida")
                continue
            f = FASES.index(p["fase"])
            if p["fase"] == "fundamentos" and ult_fase > 0:
                errores.append(f"{rid} paso {n}: 'fundamentos' no puede venir después de tronco, ruta o integracion")
            if ult_fase == 3 and p["fase"] != "integracion":
                errores.append(f"{rid} paso {n}: nada puede seguir a 'integracion' salvo más integracion")
            ult_fase = max(ult_fase, f)
            if p.get("tipo") not in TIPOS:
                errores.append(f"{rid} paso {n}: tipo inválido")
            if len(p.get("capacidad", "")) < 15:
                errores.append(f"{rid} paso {n}: falta la capacidad que aporta el paso")
            if not p.get("titulo"):
                errores.append(f"{rid} paso {n}: falta titulo")
            if not p.get("clases"):
                errores.append(f"{rid} paso {n}: sin clases")
            for tok in p.get("clases", []):
                try:
                    for cid in expandir(tok):
                        if cid not in ids and not re.match(r"^R\d{2}-M\d{2}-C\d{2}$", cid):
                            errores.append(f"{rid} paso {n}: {cid} no existe en el catálogo")
                        if cid in usadas:
                            errores.append(f"{rid} paso {n}: {cid} repetida en el rol")
                        usadas.add(cid)
                except ValueError as e:
                    errores.append(f"{rid} paso {n}: {e}")
        if "modulos" in rol:
            # Mapa de módulos: el contenido de cada módulo vive en el tronco (o es una clase nueva propuesta)
            esperadas_ruta: set[str] = set()
            esperadas_tronco: set[str] = set()
            nuevas_ruta: set[str] = set()
            mods = rol.get("modulos", [])
            if sorted(m.get("modulo", "") for m in mods) != [f"{rid}-M{i:02d}" for i in range(1, 9)]:
                errores.append(f"{rid}: 'modulos' debe describir exactamente los 8 módulos de la ruta")
            for m in mods:
                pares = []
                for t in m.get("temas", []):
                    pares.append(t.get("clases_ruta", ""))
                    dest = t.get("destino")
                    if dest == "existente":
                        if not t.get("tronco"):
                            errores.append(f"{m['modulo']} {t.get('clases_ruta')}: destino existente sin clases del tronco")
                        for c in t.get("tronco", []):
                            if not re.match(r"^B\d{2,3}-C\d{2}$", c) or c not in ids:
                                errores.append(f"{m['modulo']} {t.get('clases_ruta')}: {c} no es una clase del tronco existente")
                            esperadas_tronco.add(c)
                    elif dest == "nueva":
                        prop = t.get("propuesta", {})
                        if not (prop.get("area") and prop.get("bloque") and prop.get("titulo")):
                            errores.append(f"{m['modulo']} {t.get('clases_ruta')}: destino nueva requiere propuesta con area, bloque y titulo")
                        try:
                            for c in expandir(t.get("clases_ruta", "")):
                                nuevas_ruta.add(c)
                                esperadas_ruta.add(c)
                        except ValueError as e:
                            errores.append(f"{m['modulo']}: {e}")
                    else:
                        errores.append(f"{m['modulo']} {t.get('clases_ruta')}: destino debe ser 'existente' o 'nueva'")
                esperados = [f"{m['modulo']}-C{n:02d}..C{n + 1:02d}" for n in range(1, 20, 2)]
                if sorted(pares) != esperados:
                    errores.append(f"{m['modulo']}: los temas no cubren exactamente los 10 pares de clases C01..C20")
            # un ID de ruta en los pasos solo se admite como referencia provisional de un tema nuevo
            for c in sorted(usadas):
                if c.startswith("R") and c not in nuevas_ruta:
                    errores.append(f"{rid}: {c} está en los pasos pero su tema existe en el tronco; usa la clase del tronco")
            faltan = (esperadas_tronco | esperadas_ruta) - usadas
            if faltan:
                errores.append(f"{rid}: los pasos no incluyen {len(faltan)} clases que exige el mapa de módulos, p. ej. {sorted(faltan)[:5]}")
        else:
            avisos.append(f"{rid}: sin mapa de módulos (pendiente): falta ubicar sus 10 temas por módulo en el tronco común")
        tronco = {c for c in usadas if c.startswith("B")}
        ruta = {c for c in usadas if c.startswith("R")}
        for c in usadas:
            if c.startswith("R") and c not in ids:
                errores.append(f"{rid}: {c} no existe en el catálogo")
        conjuntos[rid] = usadas
        resumen.append((rid, len(tronco), len(ruta), len(pasos)))
    claves = sorted(conjuntos)
    for i, a in enumerate(claves):
        for b in claves[i + 1:]:
            inter = len(conjuntos[a] & conjuntos[b])
            union = len(conjuntos[a] | conjuntos[b])
            if union and inter / union > 0.9:
                errores.append(f"{a} y {b} usan casi las mismas clases (Jaccard {inter / union:.2f})")
    print(f"Recorridos por rol: {definidos} definidos de {len(datos['roles'])}")
    for rid, t, r, n in resumen:
        print(f"  {rid}: {n} pasos · {t} clases del tronco · {r} de la ruta")
    for a_ in avisos:
        print("  aviso:", a_)
    if errores:
        print("VALIDACIÓN CON ERRORES:", len(errores))
        for e in errores:
            print(" -", e)
        return 1
    print("RECORRIDOS VÁLIDOS (estructura; la pertinencia pedagógica requiere revisión humana).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
