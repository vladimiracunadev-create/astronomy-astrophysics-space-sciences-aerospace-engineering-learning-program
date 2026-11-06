#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B18-C04: perfilado de rendimiento con cProfile.

Datos: SINTÉTICOS. Puntos (x, y, z) pseudoaleatorios en un cubo de lado 1
(unidades canónicas) generados con random.Random(semilla): reproducibles.
Modelo: separación mínima entre N objetos = mínimo de las distancias
euclídeas de los N(N-1)/2 pares (problema de proximidad, p. ej. detritos).
Versión A: doble bucle en Python puro llamando a distancia(). Versión B:
NumPy por filas (difusión). Se perfila A y se decide por la evidencia.
Supuestos: puntos distintos; geometría plana euclídea.
Validez: ejemplo didáctico; el orden de magnitud de N es el de una tarea
pequeña, no el de un catálogo real.
Tolerancias: A y B coinciden con error relativo < 1e-12; el número de
llamadas a distancia() debe ser EXACTAMENTE N(N-1)/2; un caso con
respuesta conocida (puntos en una recta de paso 1) da exactamente 1.
"""
from __future__ import annotations
import cProfile, io, math, platform, pstats, random, sys, time
import numpy as np


def generar(n: int, semilla: int = 20261105):
    rng = random.Random(semilla)
    return [(rng.random(), rng.random(), rng.random()) for _ in range(n)]


def distancia(p, q) -> float:
    dx, dy, dz = p[0] - q[0], p[1] - q[1], p[2] - q[2]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def separacion_minima_python(pts) -> float:
    mejor = math.inf
    n = len(pts)
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia(pts[i], pts[j])
            if d < mejor:
                mejor = d
    return mejor


def separacion_minima_numpy(pts) -> float:
    a = np.asarray(pts)
    mejor = np.inf
    for i in range(len(a) - 1):
        d2 = ((a[i + 1:] - a[i]) ** 2).sum(axis=1)
        mejor = min(mejor, d2.min())
    return float(np.sqrt(mejor))


def prueba(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def mejor_tiempo(f, rep=3):
    t = []
    for _ in range(rep):
        t0 = time.perf_counter(); f(); t.append(time.perf_counter() - t0)
    return min(t)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    recta = [(float(k), 0.0, 0.0) for k in range(50)]
    prueba(separacion_minima_python(recta) == 1.0, "recta de paso 1 -> 1")
    prueba(separacion_minima_numpy(recta) == 1.0, "recta de paso 1 (NumPy) -> 1")

    n = 600
    pts = generar(n)
    # Perfil de la versión A
    pr = cProfile.Profile()
    pr.enable()
    resA = separacion_minima_python(pts)
    pr.disable()
    st = pstats.Stats(pr)
    llamadas = None
    for (arch, lin, nombre), (cc, nc, tt, ct, _) in st.stats.items():
        if nombre == "distancia":
            llamadas = nc
    esperado = n * (n - 1) // 2
    print(f"N={n}: llamadas a distancia() = {llamadas} (esperado N(N-1)/2 = {esperado})")
    prueba(llamadas == esperado, "número de llamadas")

    filas = sorted(st.stats.items(), key=lambda kv: kv[1][2], reverse=True)[:4]
    print(f"--- cProfile: {st.total_calls} llamadas, {st.total_tt:.3f} s en total (4 filas con más tottime) ---")
    print(f"{'ncalls':>8} {'tottime':>8} {'cumtime':>8}  función")
    for (arch, lin, nombre), (cc, nc, tt, ct, _) in filas:
        print(f"{nc:8d} {tt:8.3f} {ct:8.3f}  {nombre}")

    # Comparación con la versión B y coste del propio profiler
    resB = separacion_minima_numpy(pts)
    prueba(abs(resA - resB) <= 1e-12 * resA, "A y B deben coincidir")
    tA = mejor_tiempo(lambda: separacion_minima_python(pts))
    tB = mejor_tiempo(lambda: separacion_minima_numpy(pts))
    def con_perfil():
        p = cProfile.Profile(); p.enable(); separacion_minima_python(pts); p.disable()
    tP = mejor_tiempo(con_perfil)
    print(f"separación mínima = {resA:.6f}")
    print(f"A (Python puro): {tA:6.3f} s | con cProfile: {tP:6.3f} s (sobrecoste x{tP/tA:4.2f}) | B (NumPy): {tB*1e3:7.2f} ms | razón A/B = {tA/tB:5.1f}")

    # Perfil de B: el trabajo se concentra en muy pocas funciones de Python
    pr2 = cProfile.Profile(); pr2.enable(); separacion_minima_numpy(pts); pr2.disable()
    total_llamadas = pstats.Stats(pr2).total_calls
    print(f"llamadas totales perfiladas: A = {st.total_calls} ; B = {total_llamadas}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
