#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C13: criterios de entrada y salida de SRR y PDR con umbrales explicitos.

Datos: SINTETICOS. Los valores del «estado actual» provienen de las clases anteriores del bloque (C02, C04, C05, C08, C09, C10, C11,
C18 y C13 propia); los del «estado tras acciones» son hipoteticos. Los UMBRALES son reglas del proyecto sintetico (no de NASA,
ECSS ni de ninguna agencia). Modelo: cada criterio compara un valor con un umbral (>= o <=); una revision se declara «lista» si pasan
todos los criterios criticos. Segunda via: evaluacion vectorizada con numpy frente a bucles. RIDs sinteticas: 10 acciones, 3 criticas;
capacidad de cierre 2 por semana. Sin constantes fisicas.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

# (revision, criterio, operador, umbral, critico, valor actual, valor tras acciones, clase de origen)
CRIT = [
    ("SRR", "Requisitos verificables [%]", ">=", 95.0, True, 50.0, 100.0, "C04"),
    ("SRR", "Necesidades con requisito [%]", ">=", 100.0, True, 83.3, 100.0, "C05"),
    ("SRR", "Requisitos con origen [%]", ">=", 100.0, True, 87.5, 100.0, "C05"),
    ("SRR", "CONOPS documentado [0/1]", ">=", 1.0, True, 1.0, 1.0, "C03"),
    ("SRR", "Estabilidad del orden de necesidades [%]", ">=", 70.0, False, 76.0, 76.0, "C02"),
    ("PDR", "Margen de masa [%]", ">=", 10.0, True, 9.80, 12.0, "C09"),
    ("PDR", "Margen de energia [%]", ">=", 20.0, True, 27.58, 27.58, "C10"),
    ("PDR", "Margen de datos [%]", ">=", 25.0, True, 43.38, 43.38, "C11"),
    ("PDR", "Interfaces verificadas [%]", ">=", 100.0, True, 50.0, 100.0, "C08"),
    ("PDR", "TRL minimo de los elementos", ">=", 5.0, True, 4.0, 5.0, "C18"),
    ("PDR", "Plan de verificacion con linea base [0/1]", ">=", 1.0, True, 0.0, 1.0, "C14"),
    ("PDR", "Acciones criticas abiertas", "<=", 0.0, True, 3.0, 0.0, "C13"),
]
RIDS_TOTAL, RIDS_CRITICAS, CAPACIDAD_SEMANA = 10, 3, 2


def cumple(op, v, u):
    return v >= u if op == ">=" else v <= u


def estado(col):
    res = []
    for c in CRIT:
        v = c[5] if col == 0 else c[6]
        res.append((c[0], c[1], cumple(c[2], v, c[3]), c[4], v, c[3], c[7]))
    return res


def listo(res, rev):
    return all(ok for r, _, ok, crit, *_ in res if r == rev and crit)


def calcular():
    V = {}
    for col, nom in ((0, "a"), (1, "d")):
        res = estado(col)
        for rev in ("SRR", "PDR"):
            sub = [r for r in res if r[0] == rev]
            V[f"pasan_{rev}_{nom}"] = sum(1 for r in sub if r[2]); V[f"total_{rev}"] = len(sub)
            V[f"listo_{rev}_{nom}"] = listo(res, rev)
            V[f"fallan_{rev}_{nom}"] = [r[1] for r in sub if not r[2] and r[3]]
        V[f"res_{nom}"] = res
    # segunda via vectorizada
    op = np.array([c[2] == ">=" for c in CRIT]); u = np.array([c[3] for c in CRIT]); va = np.array([c[5] for c in CRIT])
    vec = np.where(op, va >= u, va <= u)
    V["coincide_vec"] = bool(all(bool(vec[i]) == V["res_a"][i][2] for i in range(len(CRIT))))
    V["semanas_rids"] = math.ceil(RIDS_TOTAL / CAPACIDAD_SEMANA)
    V["semanas_criticas"] = math.ceil(RIDS_CRITICAS / CAPACIDAD_SEMANA)
    V["n_fallan_a"] = len(V["fallan_SRR_a"]) + len(V["fallan_PDR_a"])
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS; umbrales = reglas del proyecto de ejemplo (no de una agencia); valores actuales vienen de C02-C11")
    for nom, tit in (("a", "ESTADO ACTUAL"), ("d", "ESTADO TRAS ACCIONES (hipotetico)")):
        print(tit)
        for r in V[f"res_{nom}"]:
            print(f"  {r[0]} {r[1]:44s} valor {r[4]:7.2f} umbral {r[5]:6.2f} {'CUMPLE' if r[2] else 'NO CUMPLE'}{' (critico)' if r[3] else ''} [{r[6]}]")
        for rev in ("SRR", "PDR"):
            print(f"  {rev}: {V[f'pasan_{rev}_{nom}']} de {V[f'total_{rev}']} criterios; criticos fallidos: {len(V[f'fallan_{rev}_{nom}'])} -> {'LISTA' if V[f'listo_{rev}_{nom}'] else 'NO LISTA'}")
    print(f"Acciones (RID): {RIDS_TOTAL} en total, {RIDS_CRITICAS} criticas, capacidad {CAPACIDAD_SEMANA} por semana -> {V['semanas_rids']} semanas para cerrar todas, {V['semanas_criticas']} para las criticas")
    comprobar(V["coincide_vec"], "evaluacion vectorizada y por bucles coinciden")
    comprobar(not V["listo_SRR_a"] and not V["listo_PDR_a"], "el estado actual no esta listo")
    comprobar(V["listo_SRR_d"] and V["listo_PDR_d"], "el estado tras acciones esta listo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
