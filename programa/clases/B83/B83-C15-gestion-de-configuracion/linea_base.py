#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C15: gestion de configuracion: linea base con huella, deriva y control de cambios.

Datos: SINTETICOS (seis elementos de configuracion de ESTRELLA-S con version, contenido de ejemplo y dependencias). Modelo: cada elemento
tiene una huella SHA-256 de su contenido; la linea base es la lista ordenada (nombre, version, huella) y tiene su propia huella. Deriva =
elemento cuyo contenido actual difiere del de la linea base. Impacto de una solicitud de cambio = descendientes en el grafo de
dependencias. Clase del cambio (regla del ejemplo): I si afecta a 3 o mas elementos o a una interfaz; II en otro caso. Segunda via: la
huella de la linea base se recalcula con otra serializacion (JSON ordenado) y se compara la deteccion de deriva por comparacion directa
de textos. Sin constantes fisicas; SHA-256 de la biblioteca estandar hashlib.
"""
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

CI = {
    "REQ-DOC": ("1.2", "Requisitos R01-R08 de ESTRELLA-S (sintetico)"),
    "ICD": ("1.0", "Interfaces I1-I6 con tensiones y tasas (sintetico)"),
    "MASS-BUDGET": ("2.1", "Presupuesto de masa MEV 67.31 kg (sintetico)"),
    "CAD-STRUCT": ("0.9", "Estructura primaria 14.0 kg (sintetico)"),
    "SW-OBC": ("0.3", "Software de a bordo: comandos y telemetria (sintetico)"),
    "TEST-PLAN": ("0.1", "Plan de ensayos E1-E5 (sintetico)"),
}
DEPS = {"ICD": ["REQ-DOC"], "TEST-PLAN": ["REQ-DOC", "ICD"], "SW-OBC": ["ICD"], "MASS-BUDGET": ["CAD-STRUCT", "REQ-DOC"]}


def huella(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()


def linea_base(ci):
    items = [(n, v, huella(c)) for n, (v, c) in sorted(ci.items())]
    return items, huella("|".join(f"{n}:{v}:{h}" for n, v, h in items))


def linea_base_via2(ci):
    d = {n: {"version": v, "sha256": hashlib.sha256(c.encode()).hexdigest()} for n, (v, c) in ci.items()}
    items = [(n, d[n]["version"], d[n]["sha256"]) for n in sorted(d)]
    return huella("|".join(f"{n}:{v}:{h}" for n, v, h in items))


def descendientes(raiz):
    out, cambio = set(), True
    while cambio:
        cambio = False
        for k, ds in DEPS.items():
            if k not in out and (raiz in ds or out & set(ds)):
                out.add(k); cambio = True
    return out


def calcular():
    items, h0 = linea_base(CI)
    ci2 = dict(CI); ci2["CAD-STRUCT"] = ("0.10", "Estructura primaria 14.6 kg (sintetico)")     # cambio sin aprobar
    items2, h1 = linea_base(ci2)
    deriva = [n for (n, v, h), (n2, v2, h2) in zip(items, items2) if h != h2]
    deriva_dir = [n for n in CI if CI[n][1] != ci2[n][1]]
    imp_cr1 = descendientes("REQ-DOC"); imp_cr2 = descendientes("CAD-STRUCT")
    clase = lambda imp, interfaz: "I" if len(imp) >= 3 or interfaz else "II"
    return dict(n=len(CI), h0=h0, h1=h1, h0_via2=linea_base_via2(CI), deriva=deriva, deriva_dir=deriva_dir, items=items,
                imp1=sorted(imp_cr1), imp2=sorted(imp_cr2), n_imp1=len(imp_cr1), n_imp2=len(imp_cr2),
                clase1=clase(imp_cr1, "ICD" in imp_cr1), clase2=clase(imp_cr2, "ICD" in imp_cr2), distintas=h0 != h1,
                h0c=h0[:12], h1c=h1[:12])


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 6 elementos de configuracion; SHA-256 (hashlib)")
    for n, v, h in V["items"]:
        print(f"  {n:12s} v{v:5s} {h[:16]}")
    print(f"Huella de la linea base = {V['h0c']}... ; por segunda serializacion = {V['h0_via2'][:12]}...")
    print(f"Tras editar CAD-STRUCT sin aprobacion: huella = {V['h1c']}... ; distinta de la base: {V['distintas']} ; deriva detectada en {V['deriva']} (comparacion directa: {V['deriva_dir']})")
    print(f"CR-01 (cambiar REQ-DOC): afecta a {V['n_imp1']} -> {V['imp1']} ; clase {V['clase1']}")
    print(f"CR-02 (cambiar CAD-STRUCT): afecta a {V['n_imp2']} -> {V['imp2']} ; clase {V['clase2']}")
    comprobar(V["h0"] == V["h0_via2"], "huella de la linea base por dos serializaciones")
    comprobar(V["deriva"] == V["deriva_dir"] == ["CAD-STRUCT"], "deriva detectada por huella y por comparacion directa")
    comprobar(V["distintas"], "la huella cambia al cambiar un elemento")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
