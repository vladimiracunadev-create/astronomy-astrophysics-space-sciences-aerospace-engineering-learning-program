#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C06: COPUOS y UNOOSA: crecimiento de miembros y probabilidad de que el consenso se bloquee (modelo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Resumen de busqueda consultado (2026-11-11, paginas de UNOOSA): COPUOS se creo como organo ad hoc por la res. 1348 (XIII) de la AG (13-12-1958) con 18 miembros y
pasó a ser organo permanente por la res. 1472 (XIV) (12-12-1959); tiene dos subcomites (Cientifico y Tecnico; Juridico); UNOOSA actua como secretaria.
La cifra de miembros hoy es discrepante entre fuentes (100 en 2021, 102 en otra presentacion): se usa 100 como valor ILUSTRATIVO y se rotula no verificado.
SINTETICO: probabilidad p de que cada miembro bloquee un asunto concreto; supuesto de independencia (falso en la realidad).
Modelo: el consenso falla si al menos un miembro bloquea: P = 1 - (1 - p)^n. Semilla 119; N = 200000; tolerancia Monte Carlo 3 sigma.
"""
import json, math, platform, random

n0, n1, y0, y1 = 18, 100, 1958, 2021
cagr = (n1 / n0) ** (1 / (y1 - y0)) - 1
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Miembros: 18 en 1958 (consultado, resumen de busqueda); 100 en 2021 (cifra discrepante, ILUSTRATIVA); p de bloqueo SINTETICA.")
print(f"Crecimiento medio anual 1958-2021: {100 * cagr:.2f} % ; factor {n1 / n0:.2f}")
assert abs((1 + cagr) ** (y1 - y0) - n1 / n0) < 1e-9
rng = random.Random(119)
N = 200000
filas = []
print("  n    p      P(bloqueo) analitica   Monte Carlo")
for n in (18, 100):
    for p in (0.005, 0.02):
        an = 1 - (1 - p) ** n
        mc = sum(1 for _ in range(N) if any(rng.random() < p for _ in range(n))) / N
        sig = math.sqrt(an * (1 - an) / N)
        assert abs(mc - an) < 3 * sig + 1e-12, (n, p)
        filas.append((n, p, an, mc))
        print(f"{n:4d} {p:6.3f}   {an:10.4f}          {mc:10.4f}")
# p maximo para tener consenso con probabilidad >= 0.5
for n in (18, 100):
    pmax = 1 - 0.5 ** (1 / n)
    print(f"n = {n:3d}: p maxima por miembro para consenso con prob. >= 0.5: {pmax:.5f}")
p18 = 1 - 0.5 ** (1 / 18); p100 = 1 - 0.5 ** (1 / 100)
assert abs((1 - p100) ** 100 - 0.5) < 1e-12
print("CLAVES " + json.dumps({"cagr": "%.2f" % (100 * cagr), "f": "%.2f" % (n1 / n0), "b18": "%.4f" % filas[1][2], "b100": "%.4f" % filas[3][2], "b18s": "%.4f" % filas[0][2], "b100s": "%.4f" % filas[2][2], "pmax18": "%.5f" % p18, "pmax100": "%.5f" % p100}))
print("Pruebas superadas.")
