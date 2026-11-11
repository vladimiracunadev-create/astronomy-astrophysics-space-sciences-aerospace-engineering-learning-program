#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C08: analisis de items de una prueba formativa SINTETICA (dificultad, discriminacion, fiabilidad KR-20, decision).

CONTENIDO EDUCATIVO. Sin datos consultados: 40 estudiantes y 10 items de opcion multiple generados con un modelo logistico de un parametro
(habilidad ~ N(0,1), dificultad del item b_i, semilla 131). Los umbrales de revision (dificultad fuera de 0.2-0.9, discriminacion < 0.2) y la regla
de decision (reensenar si el acierto del item es < 0.6) son ILUSTRATIVOS, no tomados de una norma.
Relaciones estandar NO consultadas en una fuente concreta: indice de dificultad p, correlacion punto-biserial corregida (item frente al resto), KR-20,
error estandar de medida SEM = sd * sqrt(1 - KR20).
Tolerancias: punto-biserial por dos formulas (Pearson y formula biserial puntual) coincide a 1e-9; KR-20 igual a alfa de Cronbach a 1e-9.
"""
from __future__ import annotations
import math, platform, random, statistics

N, K = 40, 10
B = [-1.5, -1.0, -0.6, -0.2, 0.0, 0.3, 0.6, 1.0, 1.6, 2.2]  # dificultades sinteticas


def generar(seed=131):
    rng = random.Random(seed)
    habil = [rng.gauss(0, 1) for _ in range(N)]
    datos = []
    for th in habil:
        datos.append([1 if rng.random() < 1 / (1 + math.exp(-(th - b))) else 0 for b in B])
    return datos


def pearson(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sx = math.sqrt(sum((a - mx) ** 2 for a in x))
    sy = math.sqrt(sum((b - my) ** 2 for b in y))
    return sxy / (sx * sy) if sx and sy else 0.0


def punto_biserial(item, resto):
    g1 = [r for i, r in zip(item, resto) if i == 1]
    g0 = [r for i, r in zip(item, resto) if i == 0]
    if not g1 or not g0:
        return 0.0
    p = len(g1) / len(item)
    s = statistics.pstdev(resto)
    return (statistics.mean(g1) - statistics.mean(g0)) / s * math.sqrt(p * (1 - p))


def kr20(datos):
    k = len(datos[0])
    tot = [sum(f) for f in datos]
    var = statistics.pvariance(tot)
    pq = sum((sum(f[j] for f in datos) / len(datos)) * (1 - sum(f[j] for f in datos) / len(datos)) for j in range(k))
    return k / (k - 1) * (1 - pq / var)


def alfa(datos):
    k = len(datos[0])
    tot = [sum(f) for f in datos]
    var_t = statistics.pvariance(tot)
    var_i = sum(statistics.pvariance([f[j] for f in datos]) for j in range(k))
    return k / (k - 1) * (1 - var_i / var_t)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Prueba SINTETICA (modelo logistico, semilla 131); umbrales y regla de decision ILUSTRATIVOS; ningun dato consultado.")
    datos = generar()
    tot = [sum(f) for f in datos]
    print(f"{N} estudiantes, {K} items ; media {statistics.mean(tot):.2f} ; desviacion {statistics.pstdev(tot):.2f}")
    print("item  p(dificultad)  disc. (r punto-biserial corregida)  revision          decision")
    maxdif = 0.0
    for j in range(K):
        item = [f[j] for f in datos]
        resto = [t - f[j] for t, f in zip(tot, datos)]
        p = sum(item) / N
        r1, r2 = pearson(item, resto), punto_biserial(item, resto)
        maxdif = max(maxdif, abs(r1 - r2))
        rev = []
        if p < 0.2 or p > 0.9:
            rev.append("dificultad")
        if r1 < 0.2:
            rev.append("discrimina poco")
        dec = "reensenar" if p < 0.6 else "avanzar"
        print(f"{j + 1:3d}   {p:9.3f}      {r1:9.3f}                           {', '.join(rev) or 'ok':16s}  {dec}")
    k20, al = kr20(datos), alfa(datos)
    sem = statistics.pstdev(tot) * math.sqrt(1 - k20)
    print(f"KR-20 = {k20:.3f} (alfa de Cronbach {al:.3f}) ; SEM = {sem:.2f} puntos")
    print(f"Mayor diferencia punto-biserial entre formulas = {maxdif:.1e}")
    ant = sum(1 for j in range(K) if sum(f[j] for f in datos) / N < 0.6)
    print(f"Items con acierto < 0.6 (a reensenar): {ant} de {K}")
    # que pasa con una prueba de 5 items (los primeros): fiabilidad menor
    k5 = kr20([f[:5] for f in datos])
    print(f"KR-20 con solo los 5 primeros items = {k5:.3f} (menos items, menor fiabilidad)")
    assert abs(k20 - al) < 1e-9
    assert maxdif < 1e-9
    assert k5 < k20
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
