#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C14: medir antes de optimizar y vectorizar.

Datos: SINTÉTICOS. 200 000 posiciones de satélites en una órbita circular de
radio 7000 km (anomalías verdaderas aleatorias, semilla 20261105) y una
estación en (6378.137 km, 0, 0), en un sistema fijo a la Tierra, esférico.
Tarea: distancia estación-satélite para cada posición.
Modelo: d = ||r_sat - r_est||. Tres implementaciones: bucle de Python,
vectorizada con NumPy y vectorizada en float32.
Supuestos: los tiempos se miden con time.perf_counter, el mejor de 5; las
mediciones dependen de la máquina y de su carga.
Validez: demostración; los factores de aceleración son de ESTA máquina.
Tolerancia: la versión vectorizada coincide con el bucle a 1e-9 relativa;
la de float32 a 1e-5 relativa; las distancias están acotadas por
[7000-6378.137, 7000+6378.137] km (desigualdad triangular).
"""
from __future__ import annotations
import cProfile, io, math, platform, pstats, sys, time
import numpy as np

R_EST, R_SAT = 6378.137, 7000.0


def datos(n):
    rng = np.random.default_rng(20261105)
    nu = rng.uniform(0.0, 2 * math.pi, n)
    return R_SAT * np.cos(nu), R_SAT * np.sin(nu)


def dist_bucle(x, y):
    out = []
    for i in range(len(x)):
        dx = x[i] - R_EST
        out.append(math.sqrt(dx * dx + y[i] * y[i]))
    return out


def dist_vec(x, y):
    return np.sqrt((x - R_EST) ** 2 + y**2)


def mejor(f, *a, n=5):
    t = 1e9
    for _ in range(n):
        t0 = time.perf_counter()
        f(*a)
        t = min(t, time.perf_counter() - t0)
    return t


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    n = 200_000
    x, y = datos(n)
    xl, yl = x.tolist(), y.tolist()
    d_b = np.array(dist_bucle(xl, yl))
    d_v = dist_vec(x, y)
    d_32 = dist_vec(x.astype(np.float32), y.astype(np.float32))
    prueba(np.allclose(d_v, d_b, rtol=1e-9, atol=0), "vectorizada = bucle")
    prueba(np.allclose(d_32, d_b, rtol=1e-5, atol=0), "float32 = bucle a 1e-5")
    prueba(d_v.min() >= R_SAT - R_EST - 1e-9 and d_v.max() <= R_SAT + R_EST + 1e-9, "cotas triangulares")
    print(f"distancias: mín = {d_v.min():.1f} km, máx = {d_v.max():.1f} km (cotas {R_SAT-R_EST:.1f} y {R_SAT+R_EST:.1f})")
    err32 = np.max(np.abs(d_32 - d_b) / d_b)
    print(f"error relativo máximo de float32 = {err32:.2e}")

    tb, tv = mejor(dist_bucle, xl, yl), mejor(dist_vec, x, y)
    x32, y32 = x.astype(np.float32), y.astype(np.float32)
    t32 = mejor(dist_vec, x32, y32)
    print(f"tiempos (mejor de 5): bucle = {tb*1e3:.1f} ms; vectorizada = {tv*1e3:.2f} ms; float32 = {t32*1e3:.2f} ms")
    print(f"aceleración vectorizada = {tb/tv:.0f}x; float32 frente a float64 = {tv/t32:.2f}x")
    prueba(tb / tv > 5, "la vectorización debe ganar con 200 000 elementos")

    # perfilado: dónde se va el tiempo del bucle
    pr = cProfile.Profile()
    pr.enable()
    dist_bucle(xl, yl)
    pr.disable()
    s = io.StringIO()
    pstats.Stats(pr, stream=s).sort_stats("cumulative").print_stats(4)
    lineas = [l for l in s.getvalue().splitlines() if "dist_bucle" in l or "sqrt" in l or "append" in l]
    print("perfilado (cProfile), líneas relevantes:")
    for l in lineas[:3]:
        print("  ", l.strip())
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
