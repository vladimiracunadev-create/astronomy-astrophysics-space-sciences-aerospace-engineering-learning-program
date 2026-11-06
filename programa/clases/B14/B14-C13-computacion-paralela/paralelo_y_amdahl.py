#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C13: paralelismo con procesos y ley de Amdahl.

Datos: SINTÉTICOS. Tarea: estimar pi por Monte Carlo con 8 trozos de 6 000 000
puntos cada uno; cada trozo usa su propia semilla (20261105 + indice), de modo
que el resultado total no depende de cuántos procesos se usen.
Modelo: tiempo con p procesos T(p) = T_serie + T_par/p (ley de Amdahl, con
fraccion serie s = T_serie/(T_serie+T_par)); aceleracion S(p) = T(1)/T(p) <= 1/s.
Se mide T(p) con multiprocessing.Pool y se estima s ajustando
S(p) = 1/(s + (1-s)/p) por minimos cuadrados simples sobre las mediciones.
Supuestos: la maquina ejecuta otras tareas; los tiempos varian entre corridas.
Validez: demostracion; las ACELERACIONES SON MEDICIONES DE ESTA MAQUINA y no se
trasladan a otra. Los cuatro trozos de la parte serie (generar y combinar) son
parte de la fraccion serie estimada.
Tolerancia: el resultado paralelo debe ser IDENTICO al serie (suma de enteros);
la aceleracion medida no puede superar p*1.05 (lo contrario indicaria un error
de medicion); el valor de pi debe estar a 5e-3 del exacto.
"""
from __future__ import annotations
import math, os, platform, sys, time
from multiprocessing import Pool
import numpy as np

N_TROZOS = 8
N_PUNTOS = 6_000_000


def trozo(i: int) -> int:
    rng = np.random.default_rng(20261105 + i)
    x = rng.random(N_PUNTOS)
    y = rng.random(N_PUNTOS)
    return int(np.count_nonzero(x * x + y * y <= 1.0))


def trozo_pequeno(i: int) -> int:
    rng = np.random.default_rng(20261105 + i)
    x = rng.random(50_000)
    y = rng.random(50_000)
    return int(np.count_nonzero(x * x + y * y <= 1.0))


def ejecutar(p: int):
    t0 = time.perf_counter()
    if p == 1:
        res = [trozo(i) for i in range(N_TROZOS)]
    else:
        with Pool(p) as pool:
            res = pool.map(trozo, range(N_TROZOS))
    return sum(res), time.perf_counter() - t0


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  CPU logicas = {os.cpu_count()}  SO = {platform.system()}")
    ps = [p for p in (1, 2, 4) if p <= (os.cpu_count() or 1)]
    ref = None
    medidas = {}
    for p in ps:
        mejor, total = 1e9, None
        for _ in range(3):                       # el mejor de 3 reduce el ruido
            total, t = ejecutar(p)
            mejor = min(mejor, t)
        medidas[p] = mejor
        if ref is None:
            ref = total
        prueba(total == ref, f"el resultado con p={p} debe ser idéntico al serie")
        print(f"p={p}: tiempo = {mejor:.3f} s; aciertos = {total}")
    # tarea PEQUEÑA: el coste de crear procesos y copiar datos supera al trabajo
    t0 = time.perf_counter(); r1 = [trozo_pequeno(i) for i in range(N_TROZOS)]; ts = time.perf_counter() - t0
    t0 = time.perf_counter()
    with Pool(2) as pool:
        r2 = pool.map(trozo_pequeno, range(N_TROZOS))
    tp = time.perf_counter() - t0
    prueba(r1 == r2, "tarea pequeña: mismo resultado")
    print(f"tarea pequeña (8 x 50 000 puntos): serie = {ts*1e3:.1f} ms; 2 procesos = {tp*1e3:.0f} ms; aceleración = {ts/tp:.3f} (menor que 1: el reparto cuesta más que el trabajo)")
    n = N_TROZOS * N_PUNTOS
    pi_est = 4.0 * ref / n
    print(f"pi estimado = {pi_est:.6f} (exacto {math.pi:.6f}); error = {abs(pi_est - math.pi):.2e}")
    prueba(abs(pi_est - math.pi) < 5e-3, "pi")
    S = {p: medidas[1] / medidas[p] for p in ps}
    for p in ps:
        print(f"aceleración S({p}) = {S[p]:.2f}  (eficiencia {S[p]/p:.2f})")
        prueba(S[p] <= p * 1.05, "la aceleración no puede superar p")
    # ajuste de la fraccion serie por busqueda en rejilla
    mejor_s, mejor_e = None, 1e9
    for s in np.linspace(0.0, 1.0, 1001):
        e = sum((1.0 / (s + (1 - s) / p) - S[p]) ** 2 for p in ps)
        if e < mejor_e:
            mejor_s, mejor_e = float(s), e
    print(f"fracción serie estimada s = {mejor_s:.3f}; cota teórica 1/s = {1/mejor_s if mejor_s>0 else float('inf'):.1f}")
    # propiedades analiticas de la ley (independientes de la medicion)
    amdahl = lambda s, p: 1.0 / (s + (1 - s) / p)
    prueba(abs(amdahl(0.1, 10) - 1 / 0.19) < 1e-12, "Amdahl s=0.1, p=10")
    prueba(abs(amdahl(0.0, 8) - 8) < 1e-12 and abs(amdahl(1.0, 8) - 1) < 1e-12, "extremos de Amdahl")
    prueba(amdahl(0.05, 10**9) < 20.0 + 1e-6, "con s=0.05 nunca se supera 20")
    print(f"Amdahl analítica: s=0.10, p=10 -> {amdahl(0.1,10):.4f}; s=0.05, p->infinito -> {1/0.05:.0f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
