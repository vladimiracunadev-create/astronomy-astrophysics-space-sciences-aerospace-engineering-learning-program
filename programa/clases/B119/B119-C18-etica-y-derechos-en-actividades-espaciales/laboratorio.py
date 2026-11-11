#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C18: decision multicriterio con criterios eticos y sensibilidad a los pesos (opciones y puntajes SINTETICOS).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, nota de legal.un.org): art. I del Tratado del Espacio Ultraterrestre: la exploracion y el uso del espacio son "la provincia de toda la humanidad" y estan abiertos a todos los Estados
en igualdad; art. IX: cooperacion y consideracion de los intereses de los demas Estados. NO consultado: codigos de etica profesional, principios de la UNESCO ni literatura de etica espacial.
Modelo: suma ponderada v_j = sum_i w_i s_ij con puntajes s en [0, 10] y pesos que suman 1. Sensibilidad: pesos aleatorios Dirichlet(1,1,1,1,1) con semilla 119 y N = 100000.
SINTETICO: tres opciones de politica (A, B, C) para una operacion hipotetica y cinco criterios (seguridad, equidad, ambiente, costo, transparencia).
Tolerancia: probabilidades de ser la mejor opcion suman 1 (1e-12); el ganador con pesos base se recalcula por dos caminos.
"""
import json, platform, random

CRIT = ["seguridad", "equidad", "ambiente", "costo", "transparencia"]
W = [0.30, 0.25, 0.20, 0.15, 0.10]
S = {"A": [9, 3, 8, 7, 6], "B": [7, 8, 7, 5, 8], "C": [6, 6, 9, 9, 3]}
def valor(w, s):
    return sum(a * b for a, b in zip(w, s))
v = {k: valor(W, s) for k, s in S.items()}
v2 = {k: sum(W[i] * S[k][i] for i in range(5)) for k in S}
assert all(abs(v[k] - v2[k]) < 1e-12 for k in S)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Opciones y puntajes SINTETICOS; arts. I y IX del tratado consultados (2026-11-11); codigos de etica NO consultados.")
for k in S: print(f"  opcion {k}: valor {v[k]:.3f}")
ganador = max(v, key=v.get)
print("Ganador con pesos base:", ganador)
rng = random.Random(119)
N = 100000
gana = {k: 0 for k in S}
for _ in range(N):
    g = [rng.gammavariate(1.0, 1.0) for _ in range(5)]
    t = sum(g)
    w = [x / t for x in g]
    gana[max(S, key=lambda k: valor(w, S[k]))] += 1
p = {k: gana[k] / N for k in S}
assert abs(sum(p.values()) - 1) < 1e-12
print("Probabilidad de ser la mejor con pesos aleatorios:", {k: round(x, 3) for k, x in p.items()})
# umbral de peso de equidad para que B supere a A
for we in (0.0, 0.1, 0.2, 0.3, 0.4):
    rest = (1 - we) / 4
    w = [rest, we, rest, rest, rest]
    print(f"   peso de equidad {we:.1f}: valores " + ", ".join(f"{k}={valor(w, S[k]):.3f}" for k in S))
# punto de cruce A=B en el peso de equidad (los otros pesos iguales): lineal
def dif(we):
    rest = (1 - we) / 4
    w = [rest, we, rest, rest, rest]
    return valor(w, S["B"]) - valor(w, S["A"])
lo, hi = 0.0, 1.0
for _ in range(60):
    mid = (lo + hi) / 2
    if dif(mid) > 0: hi = mid
    else: lo = mid
print(f"Peso de equidad a partir del cual B supera a A (otros pesos iguales): {hi:.4f}")
assert abs(dif(hi)) < 1e-9
print("CLAVES " + json.dumps({"vA": "%.3f" % v["A"], "vB": "%.3f" % v["B"], "vC": "%.3f" % v["C"], "g": ganador, "pA": "%.3f" % p["A"], "pB": "%.3f" % p["B"], "pC": "%.3f" % p["C"], "cruce": "%.4f" % hi}))
print("Pruebas superadas.")
