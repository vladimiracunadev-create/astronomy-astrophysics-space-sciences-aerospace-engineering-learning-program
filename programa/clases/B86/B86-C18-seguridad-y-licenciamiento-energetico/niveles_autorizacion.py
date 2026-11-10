#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C18: clasificacion de niveles de autorizacion de lanzamiento (NSPM-20) con un umbral A2 PARAMETRIZADO.

Datos consultados (2026-11-10): texto de la memoria presidencial NSPM-20 (2019, Registro de Documentos Presidenciales, govinfo.gov), seccion 4:
Nivel I = fuentes radiactivas hasta 100000 veces el valor A2 (IAEA SSR-6, Rev.1, Tabla 2); Nivel II = mas de 100000 veces A2, o un lanzamiento de Nivel I cuya probabilidad de un accidente con 5 a 25 rem
de dosis efectiva total para un miembro del publico es >= 1e-6, o sistemas de fision con uranio poco enriquecido (< 20 % U-235); Nivel III = probabilidad >= 1e-6 de mas de 25 rem, o fision con
cualquier otro combustible. Hoja del MMRTG y PRS FAQ de la NASA (4.8 kg de oxido de plutonio, ~71 % Pu-238 en peso).
NO CONSULTADOS: el valor A2 del Pu-238 (IAEA SSR-6) -> se PARAMETRIZA con un valor ILUSTRATIVO de 1e9 Bq y se barre entre 1e8 y 1e11 Bq; vida media 87.7 anos, masa molar 238.05 g/mol;
N_A = 6.02214076e23 /mol (exacto en el SI, no consultado en esta clase). NPR 8715.26 y la circular AC 450.45-1 de la FAA solo se vieron en resumenes de busqueda: no se abrieron.
Modelo: A = ln2 N_A m / (T_half M); razon = A / A2; reglas de nivel de NSPM-20 (seccion 4) codificadas en classify().
Segunda via: actividad por actividad especifica (Bq/g) frente a lambda N, y pruebas de tabla de verdad de classify() con los casos de la seccion 4.
Tolerancia: actividad por las dos vias con diferencia relativa < 1e-12; todas las pruebas de la tabla de verdad deben pasar.
Este script NO es una evaluacion de seguridad ni un analisis de licenciamiento.
"""
from __future__ import annotations
import math, platform

N_A, T_HALF, M_MOLAR = 6.02214076e23, 87.7, 238.05
YEAR = 365.25 * 86400.0
A2_ILUS = 1.0e9
UMBRAL = 1.0e5


def actividad(m_g):
    lam = math.log(2.0) / (T_HALF * YEAR)
    return lam * (m_g / M_MOLAR) * N_A


def actividad_especifica():
    return math.log(2.0) * N_A / (T_HALF * YEAR * M_MOLAR)      # Bq/g


def classify(activity, a2, p_5_25=0.0, p_25_mas=0.0, fision=False, leu=False):
    """Reglas de la seccion 4 de NSPM-20 (resumen): devuelve 1, 2 o 3."""
    if fision:
        return 2 if leu else 3
    if p_25_mas >= 1e-6:
        return 3
    if activity > UMBRAL * a2:
        return 2
    if p_5_25 >= 1e-6:
        return 2
    return 1


def resultados():
    r = {"sa": actividad_especifica()}
    r["sa_TBq_g"] = r["sa"] / 1e12
    casos = [("100 mg (fuente muy pequena)", 0.1), ("1 g", 1.0), ("100 g", 100.0), ("3408 g (Pu-238 de un MMRTG)", 3408.0)]
    filas = []
    for n, m in casos:
        a = actividad(m)
        filas.append((n, m, a, a / A2_ILUS, classify(a, A2_ILUS)))
    r["filas"] = filas
    r["dif_vias"] = abs(actividad(1.0) - r["sa"]) / r["sa"]
    r["m_nivel1_g"] = UMBRAL * A2_ILUS / r["sa"]
    # barrido de A2
    barr = []
    for a2 in (1e8, 1e9, 1e10, 1e11):
        barr.append((a2, classify(actividad(3408.0), a2), UMBRAL * a2 / r["sa"]))
    r["barrido"] = barr
    # decaimiento
    r["A_mmrtg"] = actividad(3408.0)
    r["A_mmrtg_PBq"] = r["A_mmrtg"] / 1e15
    r["A_mmrtg_17"] = r["A_mmrtg"] * math.exp(-math.log(2.0) * 17.0 / T_HALF)
    r["razon_mmrtg"] = r["A_mmrtg"] / A2_ILUS
    # casos de probabilidad
    r["t_prob"] = [
        classify(actividad(1.0), A2_ILUS, 0.0, 0.0),
        classify(actividad(1.0), A2_ILUS, 1e-6, 0.0),
        classify(actividad(1.0), A2_ILUS, 1e-7, 0.0),
        classify(actividad(1.0), A2_ILUS, 0.0, 1e-6),
        classify(0.0, A2_ILUS, fision=True, leu=True),
        classify(0.0, A2_ILUS, fision=True, leu=False),
    ]
    r["m1_g"] = r["m_nivel1_g"]
    for k, (n, m, a, rz, nv) in enumerate(filas):
        r[f"a{k+1}"], r[f"rz{k}"], r[f"n{k+1}"] = a, rz, nv
    for k, (a2, nv, m) in enumerate(barr):
        r[f"nb{k}"], r[f"mb{k}"] = nv, m
    for k, v in enumerate(r["t_prob"]):
        r[f"tp{k}"] = v
    r["A_17_PBq"] = r["A_mmrtg_17"] / 1e15
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print("Clasificacion de niveles de NSPM-20 con A2 PARAMETRIZADO (A2 de referencia ilustrativo = 1e9 Bq, NO consultado)")
    print(f"Actividad especifica del Pu-238 (calculada, vida media 87.7 a no consultada) = {r['sa']:.4e} Bq/g = {r['sa_TBq_g']:.3f} TBq/g ; diferencia entre las dos vias = {r['dif_vias']:.1e}")
    print(" fuente                               m [g]       A [Bq]       A/A2       nivel")
    for n, m, a, rz, nv in r["filas"]:
        print(f" {n:<34} {m:8.1f}  {a:11.3e}  {rz:11.3e}   {nv}")
    print(f"Masa de Pu-238 que cruza el umbral de 100000 x A2 (con A2 = 1e9 Bq) = {r['m1_g']:.1f} g")
    print("Sensibilidad al valor de A2 (fuente de 3408 g):")
    for a2, nv, m in r["barrido"]:
        print(f"  A2 = {a2:.0e} Bq -> nivel {nv} ; umbral del Nivel I = {m:.1f} g de Pu-238")
    print(f"Actividad de 3408 g: ahora = {r['A_mmrtg_PBq']:.3f} PBq ; a los 17 anos = {r['A_mmrtg_17']/1e15:.3f} PBq (el nivel se decide con la actividad al lanzamiento)")
    print("Tabla de verdad (1 g): sin probabilidades ->", r["t_prob"][0], "; p(5-25 rem) = 1e-6 ->", r["t_prob"][1], "; 1e-7 ->", r["t_prob"][2], "; p(>25 rem) = 1e-6 ->", r["t_prob"][3],
          "; fision LEU ->", r["t_prob"][4], "; fision otro combustible ->", r["t_prob"][5])
    assert r["dif_vias"] < 1e-12
    assert r["t_prob"] == [1, 2, 1, 3, 2, 3]
    assert r["filas"][0][4] == 1 and r["filas"][3][4] == 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
