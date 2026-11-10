#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C20: campana conceptual de calificacion/protovuelo de un CubeSat SINTETICO: calendario con fallas y reintentos.

Cada ensayo i dura d_i dias; falla con probabilidad p_i; una falla exige retrabajo r_i y repetir el ensayo (hasta exito).
E[T_i] = d_i + p_i/(1-p_i) (r_i + d_i). Se compara con Monte Carlo (semilla fija). Flujo basado en la secuencia tipica de la CubeSat Design
Specification Rev. 14.1 (vibracion, choque si se exige, termovacio con bakeout), con tareas y probabilidades SINTETICAS.
Unidades: dias. Tolerancia: media MC frente a analitica < 4 errores estandar.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: campana de protovuelo de un CubeSat 3U")
ensayos = [  # nombre, duracion d, prob. de falla p, retrabajo r, exigido
    ("Inspeccion y ajuste (fit check)", 1, 0.02, 1, True),
    ("Funcional de referencia", 2, 0.05, 2, True),
    ("Vibracion aleatoria", 3, 0.10, 4, True),
    ("Choque", 2, 0.05, 3, False),
    ("Termovacio y bakeout", 5, 0.12, 5, True),
    ("Funcional posensayo", 2, 0.05, 2, True),
    ("Prueba de dia en la vida (DITL)", 2, 0.08, 3, True),
]
req = [e for e in ensayos if e[4]]
E = lambda d, p, r: d + p / (1 - p) * (r + d)
print("ensayo                              d    p     r   E[T] (d)")
tot_det, tot_E = 0.0, 0.0
for n, d, p, r, ex in ensayos:
    flag = "" if ex else "  (no exigido: depende del proveedor de lanzamiento)"
    print(f"{n:34s} {d:2d}  {p:4.2f}  {r:2d}  {E(d, p, r):6.3f}{flag}")
for n, d, p, r, ex in req:
    tot_det += d
    tot_E += E(d, p, r)
print(f"Flujo exigido: {len(req)} ensayos ; duracion sin fallas = {tot_det} d ; esperada con fallas = {tot_E:.3f} d")
rng = np.random.default_rng(90)
N = 400_000
T = np.zeros(N)
for n, d, p, r, ex in req:
    k = rng.geometric(1 - p, N) - 1              # fallas antes del exito
    T += d + k * (r + d)
se = T.std() / math.sqrt(N)
print(f"Monte Carlo ({N} campanas): media = {T.mean():.3f} d (error estandar {se:.3f}) ; desviacion = {T.std():.3f} d")
comprobar(abs(T.mean() - tot_E) < 4 * se, "la media simulada debe coincidir con la analitica")
for q in (50, 80, 90, 95):
    print(f"   percentil {q}: {np.percentile(T, q):.1f} d")
for plazo in (20, 25, 30, 35):
    print(f"P(terminar en {plazo} d) = {np.mean(T <= plazo) * 100:.1f} %")
comprobar(np.mean(T <= 40) > 0.95, "con 40 d la campana debe terminar casi siempre")
print(f"Contingencia para 90 % de confianza = {np.percentile(T, 90) - tot_det:.1f} d sobre la duracion sin fallas")
fin()
