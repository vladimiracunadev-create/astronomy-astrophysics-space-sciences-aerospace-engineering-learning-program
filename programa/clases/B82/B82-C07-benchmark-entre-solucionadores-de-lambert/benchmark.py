#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B82-C07: banco de pruebas de solucionadores de Lambert (M = 0, prograda).

Datos: GM del Sol y UA del JPL SSD (2026-11-10). SINTETICOS: 1000 casos aleatorios (semilla 82), radios 0.5-3 UA, angulos al azar
(se excluyen los que estan a menos de 3 deg de 0 o 180), tiempo de vuelo entre 0.05 y 1.5 veces el periodo de la orbita circular media.
Solucionadores: variables universales con biseccion y con Newton; x de Lancaster-Blanchard con Newton, Halley y Householder.
Metrica de exactitud: residuo de propagacion kepleriana |r(tof) - r2| / |r2| (propagador independiente). Costo: iteraciones y tiempo.
El TIEMPO depende del equipo, de Python 3.12.9 y de numpy 2.4.4; no es una medida absoluta. Tolerancia: residuo relativo < 1e-8 para contar un exito.
"""
import math, platform, sys, time
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lambert_comun import *

print("Python", platform.python_version(), "| numpy", np.__version__, "| plataforma", platform.system())
print("Datos SINTETICOS: 1000 casos, semilla 82")
rng = np.random.default_rng(82)
casos = []
while len(casos) < 1000:
    ra, rb = rng.uniform(0.5, 3.0, 2); a1, a2 = rng.uniform(0, 2 * math.pi, 2)
    th = (a2 - a1) % (2 * math.pi)
    if min(abs(th - math.pi), th, 2 * math.pi - th) < math.radians(3):
        continue
    p1 = ra * np.array([math.cos(a1), math.sin(a1), 0.0]); p2 = rb * np.array([math.cos(a2), math.sin(a2), 0.0])
    am = (ra + rb) / 2
    casos.append((p1, p2, rng.uniform(0.05, 1.5) * 2 * math.pi * am ** 1.5))
solv = {
    "universal-biseccion": lambda a, b, t: lambert_universal(a, b, t, metodo="biseccion"),
    "universal-newton": lambda a, b, t: lambert_universal(a, b, t, metodo="newton"),
    "izzo-newton": lambda a, b, t: lambert_izzo(a, b, t, metodo="newton"),
    "izzo-halley": lambda a, b, t: lambert_izzo(a, b, t, metodo="halley"),
    "izzo-householder": lambda a, b, t: lambert_izzo(a, b, t, metodo="householder"),
}
print("solucionador          exitos  fallos  iter media  iter max   residuo rel. mediano   max       t/llamada [us]")
res_global = {}
for nombre, f in solv.items():
    errs = []; its = []; fallos = 0
    t0 = time.perf_counter()
    sol = []
    for a, b, t in casos:
        try:
            sol.append(f(a, b, t))
        except Exception:
            sol.append(None)
    dt = time.perf_counter() - t0
    for (a, b, t), v in zip(casos, sol):
        if v is None or not np.all(np.isfinite(v[0])):
            fallos += 1; continue
        e = residuo(a, v[0], b, t) / np.linalg.norm(b)
        if e < 1e-8:
            errs.append(e); its.append(v[3])
        else:
            fallos += 1
    res_global[nombre] = (len(errs), fallos)
    print(f"{nombre:20s}  {len(errs):6d}  {fallos:6d}  {np.mean(its):9.2f}  {max(its):8d}   {np.median(errs):.2e}   {max(errs):.2e}   {dt/len(casos)*1e6:9.1f}")
ok = res_global["izzo-householder"][0]
assert ok >= 990, "Householder debe resolver casi todos"
assert res_global["universal-newton"][0] >= 900
print("Acuerdo de velocidades izzo-householder frente a universal-newton (casos de ambos):")
d = []
for a, b, t in casos[:500]:
    p = lambert_izzo(a, b, t); q = lambert_universal(a, b, t, metodo="newton")
    if p is not None and q is not None and np.all(np.isfinite(q[0])):
        d.append(np.linalg.norm(p[0] - q[0]) / np.linalg.norm(p[0]))
print(f"  casos comparados = {len(d)}, diferencia relativa mediana = {np.median(d):.1e}, max = {max(d):.1e}")
print("Pruebas superadas.")
