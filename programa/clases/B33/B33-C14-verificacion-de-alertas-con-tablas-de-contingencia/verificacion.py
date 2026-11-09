#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B33-C14: tabla de contingencia, curva ROC y area bajo la curva por dos vias.

Datos: ninguna constante fisica. Las puntuaciones de un pronostico binario sintetico (sucesos ~ N(1.2, 1), no sucesos ~ N(0, 1)), la tasa base (8 %), los 5000 casos y la semilla fija son ILUSTRATIVOS (sinteticos).
Modelo: umbrales sobre la puntuacion; tabla (a, b, c, d); POD, FAR, CSI, sesgo de frecuencia (a + b)/(a + c), Heidke; curva ROC (POD frente a la tasa de falsas alarmas b/(b + d)) y area bajo la curva por la regla
del trapecio y por el estadistico de Mann-Whitney U (probabilidad de que una puntuacion de suceso supere a una de no suceso), que deben coincidir; valor teorico Phi(d'/sqrt(2)) con d' = 1.2.
Supuestos: dos distribuciones normales de igual varianza. Validez: ilustrativa.
Tolerancia: AUC por trapecio y por U coinciden a 1e-12; AUC dentro de 4 errores estandar de la teoria.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 5000
    obs = [1 if rng.random() < 0.08 else 0 for _ in range(n)]
    sc = [rng.gauss(1.2 if o else 0.0, 1.0) for o in obs]
    pos = [s for s, o in zip(sc, obs) if o]
    neg = [s for s, o in zip(sc, obs) if not o]
    print(f"casos = {n} ; sucesos = {len(pos)} ; no sucesos = {len(neg)}")
    print(f"{'umbral':>7} {'a':>5} {'b':>5} {'c':>5} {'d':>6} {'POD':>6} {'FAR':>6} {'CSI':>6} {'sesgo':>6} {'Heidke':>7}")
    for u in (0.0, 0.5, 1.0, 1.5, 2.0):
        a = sum(1 for s in pos if s >= u); c = len(pos) - a
        b = sum(1 for s in neg if s >= u); d = len(neg) - b
        pod = a / (a + c); far = b / (a + b) if a + b else float("nan"); csi = a / (a + b + c)
        hss = 2 * (a * d - b * c) / ((a + c) * (c + d) + (a + b) * (b + d))
        print(f"{u:7.1f} {a:5d} {b:5d} {c:5d} {d:6d} {pod:6.3f} {far:6.3f} {csi:6.3f} {(a + b) / (a + c):6.2f} {hss:7.3f}")
    # ROC por barrido de todos los umbrales
    orden = sorted(set(sc), reverse=True)
    pts = [(0.0, 0.0)]
    for u in orden:
        tp = sum(1 for s in pos if s >= u) / len(pos)
        fp = sum(1 for s in neg if s >= u) / len(neg)
        pts.append((fp, tp))
    pts.append((1.0, 1.0))
    auc_t = sum((pts[i + 1][0] - pts[i][0]) * (pts[i + 1][1] + pts[i][1]) / 2 for i in range(len(pts) - 1))
    # Mann-Whitney por rangos
    todos = sorted([(s, 1) for s in pos] + [(s, 0) for s in neg])
    rango = {}
    for i, (s, _) in enumerate(todos):
        rango.setdefault(s, []).append(i + 1)
    rsum = sum(sum(rango[s]) / len(rango[s]) for s in pos)
    u = rsum - len(pos) * (len(pos) + 1) / 2
    auc_u = u / (len(pos) * len(neg))
    teo = 0.5 * (1 + math.erf((1.2 / math.sqrt(2)) / math.sqrt(2)))
    err = math.sqrt(auc_u * (1 - auc_u) / min(len(pos), len(neg))) / 1.5
    print(f"AUC por trapecio = {auc_t:.6f} ; AUC por Mann-Whitney = {auc_u:.6f} ; teoria Phi(d'/sqrt2) = {teo:.6f}")
    assert abs(auc_t - auc_u) < 1e-12
    assert abs(auc_u - teo) < 4 * err
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
