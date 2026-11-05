#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Valida catalogo/v0.2.0/colocacion/Rxx.json: dónde vive en áreas (A) y bloques (B) el contenido de cada módulo M.

Cada archivo describe los 8 módulos de una ruta y, para cada uno de sus 10 temas (pares de clases
C01..C02, ..., C19..C20), una de dos cosas:
  - "existente": clases del tronco común que ya cubren el tema (IDs Bnn-Cnn, incluida A01 si corresponde);
  - "nueva": clase PROGRAMADA (no redactada) con área, bloque, título y la necesidad que resuelve.
Reglas: las clases programadas no pueden ir en A01 (B01-B08); el área es A02..A08 o 'nueva: <nombre>';
el bloque es Bnn (existente, con su misma área) o 'nuevo: <nombre>'.
No valida la pertinencia pedagógica: eso requiere revisión humana.

Uso:
    python herramientas/validar_colocacion.py            # avisa de rutas pendientes
    python herramientas/validar_colocacion.py --completo # exige las 24 rutas
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "catalogo" / "v0.2.0" / "colocacion"
AREAS_OK = {f"A0{i}" for i in range(2, 9)}


def cargar_base() -> tuple[set[str], dict[str, str]]:
    with (ROOT / "catalogo" / "clases.jsonl").open(encoding="utf-8") as f:
        filas = [json.loads(x) for x in f if x.strip()]
    ids = {r["id"] for r in filas}
    area_bloque = {r["bloque_id"]: r["area"] for r in filas if r["tipo"] == "tronco_comun"}
    return ids, area_bloque


def validar_archivo(ruta: Path, ids: set[str], area_bloque: dict[str, str], errores: list[str]) -> tuple[int, int]:
    rid = ruta.stem
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    if datos.get("ruta_id") != rid:
        errores.append(f"{rid}: ruta_id no coincide con el nombre del archivo")
    esperados = [f"{rid}-M{i:02d}" for i in range(1, 9)]
    mods = datos.get("modulos", [])
    if [m.get("modulo") for m in mods] != esperados:
        errores.append(f"{rid}: 'modulos' debe describir los 8 módulos en orden {esperados[0]}..{esperados[-1]}")
    existentes = nuevas = 0
    for m in mods:
        mid = m.get("modulo", "?")
        pares = [t.get("clases_ruta") for t in m.get("temas", [])]
        if pares != [f"{mid}-C{n:02d}..C{n + 1:02d}" for n in range(1, 20, 2)]:
            errores.append(f"{mid}: los temas deben cubrir en orden los 10 pares C01..C02 a C19..C20")
        for t in m.get("temas", []):
            clave = f"{mid} {t.get('clases_ruta')}"
            if not t.get("tema"):
                errores.append(f"{clave}: falta 'tema'")
            dest = t.get("destino")
            if dest == "existente":
                existentes += 1
                tr = t.get("tronco") or []
                if not tr:
                    errores.append(f"{clave}: destino existente sin clases del tronco")
                for c in tr:
                    if not re.match(r"^B\d{2}-C\d{2}$", c) or c not in ids:
                        errores.append(f"{clave}: {c} no es una clase existente del tronco")
            elif dest == "nueva":
                nuevas += 1
                p = t.get("propuesta") or {}
                if len(p.get("titulo", "")) < 8:
                    errores.append(f"{clave}: la clase programada necesita titulo")
                if len(p.get("necesidad", "")) < 25:
                    errores.append(f"{clave}: la clase programada necesita 'necesidad' (qué resuelve y por qué no está cubierto)")
                area = p.get("area", "")
                bloque = p.get("bloque", "")
                if not (area in AREAS_OK or re.match(r"^nueva: .{4,}$", area)):
                    errores.append(f"{clave}: area debe ser A02..A08 o 'nueva: <nombre>' (A01 no admite clases programadas)")
                if re.match(r"^B0[1-8]$", bloque):
                    errores.append(f"{clave}: las clases programadas no pueden ir en B01-B08 (A01)")
                elif re.match(r"^B\d{2}$", bloque):
                    if bloque not in area_bloque:
                        errores.append(f"{clave}: el bloque {bloque} no existe")
                    elif area_bloque[bloque] != area:
                        errores.append(f"{clave}: el bloque {bloque} pertenece a {area_bloque[bloque]}, no a {area}")
                elif not re.match(r"^nuevo: .{4,}$", bloque):
                    errores.append(f"{clave}: bloque debe ser Bnn o 'nuevo: <nombre>'")
            else:
                errores.append(f"{clave}: destino debe ser 'existente' o 'nueva'")
    return existentes, nuevas


def main() -> int:
    completo = "--completo" in sys.argv
    ids, area_bloque = cargar_base()
    errores: list[str] = []
    archivos = sorted(DIR.glob("R*.json"))
    hechas = {a.stem for a in archivos}
    tot_e = tot_n = 0
    for a in archivos:
        e, n = validar_archivo(a, ids, area_bloque, errores)
        tot_e += e
        tot_n += n
    pendientes = sorted({f"R{i:02d}" for i in range(1, 25)} - hechas)
    if completo and pendientes:
        errores.append(f"faltan rutas por ubicar: {', '.join(pendientes)}")
    print(f"Colocación: {len(hechas)} de 24 rutas · {tot_e + tot_n} temas · {tot_e} en clases existentes · {tot_n} clases programadas")
    if pendientes and not completo:
        print(f"  pendientes: {', '.join(pendientes)}")
    if errores:
        print("VALIDACIÓN CON ERRORES:", len(errores))
        for e in errores:
            print(" -", e)
        return 1
    print("COLOCACIÓN VÁLIDA (estructura; la pertinencia pedagógica requiere revisión humana).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
