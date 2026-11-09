#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C04: escalas de severidad G, S y R de NOAA y frecuencia esperada por nivel.

Datos: umbrales de las escalas de NOAA (spaceweather.gov, pagina de escalas, consultada 2026-11-09): G1-G5 = Kp 5, 6, 7, 8 (incluido 9-) y 9; S1-S5 = protones >= 10 MeV de 10, 1e2, 1e3, 1e4, 1e5 pfu;
R1-R5 = flujo de rayos X de 1e-5, 5e-5, 1e-4, 1e-3, 2e-3 W/m2 (M1, M5, X1, X10, X20). El indice de la ley de potencias (alpha = 1.8), el piso (1e-6 W/m2; 1 pfu) y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: clasificacion por umbral; para una cola P(X > x) = (x/x_min)^-(alpha - 1) el numero esperado de eventos con nivel k de entre N es N [P(X > u_k) - P(X > u_{k+1})]; Monte Carlo (200 000 valores)
de las frecuencias; razon entre umbrales sucesivos y exponente local entre niveles.
Supuestos: valores independientes con cola de potencias. Validez: ilustrativa.
Tolerancia: conteos simulados dentro de 4 desviaciones tipicas multinomiales de los esperados.
"""
from __future__ import annotations
import math, platform, random, sys
R = (1e-5, 5e-5, 1e-4, 1e-3, 2e-3)
S = (10.0, 1e2, 1e3, 1e4, 1e5)

def nivel(x, u):
    k = 0
    for i, v in enumerate(u):
        if x >= v:
            k = i + 1
    return k

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("umbrales R: " + ", ".join(f"R{i + 1} >= {u:g}" for i, u in enumerate(R)) + " W/m2")
    print("razones sucesivas de R: " + ", ".join(f"{R[i + 1] / R[i]:g}" for i in range(4)) + " ; de S: " + ", ".join(f"{S[i + 1] / S[i]:g}" for i in range(4)))
    alpha, n = 1.8, 200000
    rng = random.Random(20261109)
    for nombre, u, xmin in (("R", R, 1e-6), ("S", S, 1.0)):
        cola = lambda x: (x / xmin) ** -(alpha - 1)
        esp = [n * (cola(u[k - 1]) - (cola(u[k]) if k < 5 else 0.0)) if k else n * (1 - cola(u[0])) for k in range(6)]
        xs = [xmin * (1 - rng.random()) ** (-1 / (alpha - 1)) for _ in range(n)]
        cnt = [0] * 6
        for x in xs:
            cnt[nivel(x, u)] += 1
        print(f"{nombre}: {'nivel':>6}" + "".join(f"{k:>10}" for k in range(6)))
        print(f"   {'esperado':>8}" + "".join(f"{e:10.1f}" for e in esp))
        print(f"   {'simulado':>8}" + "".join(f"{c:10d}" for c in cnt))
        for e, c in zip(esp, cnt):
            p = e / n
            assert abs(c - e) < 4 * math.sqrt(n * p * (1 - p)) + 1, (nombre, e, c)
    print(f"exponente local de la cola entre R1 y R3: log10(N_R1+/N_R3+)/log10(R3/R1) = {(alpha - 1):.2f} por construccion")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
