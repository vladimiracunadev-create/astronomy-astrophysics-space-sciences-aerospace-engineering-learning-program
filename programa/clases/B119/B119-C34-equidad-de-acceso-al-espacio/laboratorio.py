#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C34: equidad de acceso al espacio: desigualdad de capacidad de lanzamiento entre 20 Estados GENERICOS (indice de Gini, Lorenz, Atkinson) y efecto de un fondo compartido.

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no describe ningun pais real.
Texto consultado (2026-11-11, nota de legal.un.org): art. I del Tratado del Espacio Ultraterrestre: la exploracion y el uso del espacio estan abiertos a todos los Estados en igualdad y son "la provincia de toda la humanidad";
Acuerdo sobre la Luna (UNOOSA), art. 11: reparto equitativo de beneficios con especial consideracion a los paises en desarrollo. NO consultado: datos de lanzamientos ni de acceso de ningun Estado real;
las formulas de desigualdad (Gini, Lorenz, Atkinson) son estandar y NO se consultaron en una fuente concreta (se verifican por dos formulas del Gini y los casos limite).
Datos SINTETICOS: 20 Estados genericos; 10 sin capacidad propia (0) y 10 con capacidad lognormal (semilla 119, mediana 4 lanzamientos/ano, sigma_ln = 1.0). Indice de acceso a_i = 1 + capacidad_i (acceso base 1).
Fondo compartido: una fraccion q de la capacidad total se reparte por igual entre los 20 Estados. Atkinson con aversion e (e = 0.5 y 1).
Tolerancia: Gini por diferencia media == Gini por formula ordenada (1e-12); Gini de distribucion igual = 0; Gini con un solo poseedor -> (n-1)/n.
"""
import json, math, platform, random

rng = random.Random(119)
cap = [0.0] * 10 + [rng.lognormvariate(math.log(4.0), 1.0) for _ in range(10)]
rng.shuffle(cap)
def gini_dif(x):
    n = len(x); mu = sum(x) / n
    return sum(abs(a - b) for a in x for b in x) / (2 * n * n * mu)
def gini_ord(x):
    y = sorted(x); n = len(y)
    return sum((2 * (i + 1) - n - 1) * v for i, v in enumerate(y)) / (n * sum(y))
def atkinson(x, e):
    n = len(x); mu = sum(x) / n
    if e == 1:
        eq = math.exp(sum(math.log(v) for v in x) / n)
    else:
        eq = (sum(v ** (1 - e) for v in x) / n) ** (1 / (1 - e))
    return 1 - eq / mu
def lorenz(x):
    y = sorted(x); tot = sum(y); acc = 0.0; pts = [(0.0, 0.0)]
    for i, v in enumerate(y):
        acc += v; pts.append(((i + 1) / len(y), acc / tot))
    return pts
acceso = [1.0 + c for c in cap]
g1, g2 = gini_dif(acceso), gini_ord(acceso)
assert abs(g1 - g2) < 1e-12
assert gini_dif([5.0] * 20) == 0.0
uno = [0.0] * 19 + [1.0]
assert abs(gini_dif(uno) - 19 / 20) < 1e-12
print("Python", platform.python_version(), "(biblioteca estandar)")
print("20 Estados GENERICOS con capacidad SINTETICA; art. I y art. 11 (Luna) consultados 2026-11-11; datos reales de lanzamientos NO consultados.")
print(f"Capacidad total = {sum(cap):.1f} lanzamientos/ano ; Estados sin capacidad = {sum(1 for c in cap if c == 0)}")
print(f"Gini del acceso (1 + capacidad): {g1:.4f} (dos formulas coinciden) ; Atkinson e=0.5: {atkinson(acceso, 0.5):.4f} ; e=1: {atkinson(acceso, 1):.4f}")
y = sorted(acceso); tot = sum(y)
mitad_baja = sum(y[:10]) / tot
print(f"La mitad de Estados con menor acceso recibe el {100 * mitad_baja:.1f} % del acceso total")
print("Efecto de un fondo compartido (fraccion q de la capacidad total repartida por igual):")
res = {}
for q in (0.0, 0.1, 0.25, 0.5):
    T = sum(cap)
    nuevo = [1.0 + (1 - q) * c + q * T / 20 for c in cap]
    res[q] = (gini_dif(nuevo), atkinson(nuevo, 1))
    print(f"   q = {q:4.2f}: Gini {res[q][0]:.4f} ; Atkinson(e=1) {res[q][1]:.4f}")
assert res[0.5][0] < res[0.25][0] < res[0.1][0] < res[0.0][0]
print("CLAVES " + json.dumps({"g": "%.4f" % g1, "a05": "%.4f" % atkinson(acceso, 0.5), "a1": "%.4f" % atkinson(acceso, 1), "mb": "%.1f" % (100 * mitad_baja), "g10": "%.4f" % res[0.1][0], "g25": "%.4f" % res[0.25][0], "g50": "%.4f" % res[0.5][0], "tot": "%.1f" % sum(cap)}))
print("Pruebas superadas.")
