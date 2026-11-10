#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C13: algoritmo genetico y enjambre de particulas frente a arranque multiple sobre una superficie con muchos minimos locales.

Sin fuentes externas. Funcion SINTETICA (ILUSTRATIVA) que imita un delta-v frente a (dia de salida, tiempo de vuelo) con muchos minimos locales: la funcion de Rastrigin
en 2 variables, f(x) = 20 + sum (x_i^2 - 10 cos(2 pi x_i)), con minimo global f = 0 en x = (0, 0) (conocido) y minimos locales en los enteros; dominio [-5,12; 5,12]^2.
No es un delta-v real.
Algoritmos (semilla fija por repeticion): GA con poblacion 40, 60 generaciones, torneo de 3, cruce aritmetico (probabilidad 0,9), mutacion gaussiana (sigma 0,3, probabilidad 0,2), elitismo 2.
PSO con 30 particulas, 80 iteraciones, w = 0,72, c1 = c2 = 1,49. Arranque multiple: 20 inicios aleatorios con L-BFGS-B. 30 repeticiones por metodo (semillas 0..29).
Exito: mejor valor < 1e-3. Se cuentan las evaluaciones de la funcion (para L-BFGS-B, nfev).
Tolerancias: f(0,0) = 0 exacto; el arranque multiple y los heuristicos se comparan solo con estas semillas y esta funcion (no generalizan).
"""
from __future__ import annotations
import math, platform, random
import numpy as np
import scipy
from scipy.optimize import minimize

LO, HI = -5.12, 5.12


def f(x):
    return 20.0 + sum(xi * xi - 10.0 * math.cos(2 * math.pi * xi) for xi in x)


def ga(seed):
    rng = random.Random(seed)
    n, gens = 40, 60
    pop = [[rng.uniform(LO, HI), rng.uniform(LO, HI)] for _ in range(n)]
    ev = 0
    fit = [f(p) for p in pop]; ev += n
    for _ in range(gens):
        orden = sorted(range(n), key=lambda i: fit[i])
        nueva = [pop[orden[0]][:], pop[orden[1]][:]]
        while len(nueva) < n:
            def torneo():
                c = rng.sample(range(n), 3)
                return pop[min(c, key=lambda i: fit[i])]
            p1, p2 = torneo(), torneo()
            if rng.random() < 0.9:
                w = rng.random()
                h = [w * p1[0] + (1 - w) * p2[0], w * p1[1] + (1 - w) * p2[1]]
            else:
                h = p1[:]
            for j in range(2):
                if rng.random() < 0.2:
                    h[j] += rng.gauss(0, 0.3)
                h[j] = min(max(h[j], LO), HI)
            nueva.append(h)
        pop = nueva
        fit = [f(p) for p in pop]; ev += n
    return min(fit), ev


def pso(seed):
    rng = random.Random(seed)
    n, its = 30, 80
    x = [[rng.uniform(LO, HI), rng.uniform(LO, HI)] for _ in range(n)]
    v = [[0.0, 0.0] for _ in range(n)]
    pb = [p[:] for p in x]
    pf = [f(p) for p in x]
    ev = n
    g = min(range(n), key=lambda i: pf[i])
    gb, gf = pb[g][:], pf[g]
    for _ in range(its):
        for i in range(n):
            for j in range(2):
                v[i][j] = 0.72 * v[i][j] + 1.49 * rng.random() * (pb[i][j] - x[i][j]) + 1.49 * rng.random() * (gb[j] - x[i][j])
                x[i][j] = min(max(x[i][j] + v[i][j], LO), HI)
            fx = f(x[i]); ev += 1
            if fx < pf[i]:
                pf[i], pb[i] = fx, x[i][:]
                if fx < gf:
                    gf, gb = fx, x[i][:]
    return gf, ev


def multistart(seed, k=20):
    rng = random.Random(seed)
    mejor, ev = 1e18, 0
    for _ in range(k):
        x0 = [rng.uniform(LO, HI), rng.uniform(LO, HI)]
        r = minimize(lambda z: f(z), x0, method="L-BFGS-B", bounds=[(LO, HI)] * 2)
        ev += r.nfev
        mejor = min(mejor, r.fun)
    return mejor, ev


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    print("Funcion SINTETICA (Rastrigin 2D): minimo global f = 0 en (0,0) ; dominio [-5,12; 5,12]^2 ; 30 repeticiones (semillas 0..29)")
    print(f"f(0,0) = {f([0.0, 0.0]):.1f}")
    print(" metodo               exitos/30   evaluaciones medias   mejor valor medio")
    res = {}
    for nombre, fn in (("GA (40 x 60)", ga), ("PSO (30 x 80)", pso), ("Multiarranque (20)", multistart)):
        vals = [fn(s) for s in range(30)]
        ok = sum(1 for v, _ in vals if v < 1e-3)
        evm = sum(e for _, e in vals) / len(vals)
        medio = sum(v for v, _ in vals) / len(vals)
        res[nombre] = ok
        print(f" {nombre:20s} {ok:6d}      {evm:14.0f}       {medio:12.4f}")
    # un solo arranque local
    un = [minimize(lambda z: f(z), [random.Random(s).uniform(LO, HI), random.Random(s + 100).uniform(LO, HI)], method="L-BFGS-B", bounds=[(LO, HI)] * 2).fun for s in range(30)]
    print(f" {'Un arranque local':20s} {sum(1 for v in un if v < 1e-3):6d}                  (referencia)")
    assert f([0.0, 0.0]) == 0.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
