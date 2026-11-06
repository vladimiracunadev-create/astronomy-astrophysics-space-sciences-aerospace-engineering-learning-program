#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C13: presupuesto de incertidumbre de una distancia por tiempo de vuelo.

Datos: SINTETICOS. Telemetro laser a un reflector a ~10 km:
  d = c * (t_med - t_0) / (2 n)
con c exacta (299 792 458 m/s), t_med = tiempo de ida y vuelta medido,
t_0 = retardo electronico (calibrado), n = indice de grupo del aire.
Valores de ejemplo: n = 1.000300 con u(n) = 3e-6; u(t_med) = 0.50 ns
(resolucion y jitter); u(t_0) = 0.30 ns.
Modelo (GUM 5.1.2, entradas independientes):
  u_c^2(d) = sum_i (df/dx_i)^2 u^2(x_i).
Coeficientes: df/dt = c/(2n); df/dt0 = -c/(2n); df/dn = -d/n.
Supuestos: entradas independientes y casi lineales en torno a su valor.
Validez: u_i pequenas frente a los valores. Tolerancia: propagacion analitica
frente a Monte Carlo (200000 muestras) dentro del 1 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

C = 299_792_458.0
N0, UN = 1.000300, 3e-6
D_NOM = 10_000.0
T_MED = 2 * N0 * D_NOM / C + 30e-9       # t0 nominal = 30 ns
T0 = 30e-9
UT, UT0 = 0.50e-9, 0.30e-9


def dist(t, t0, n):
    return C * (t - t0) / (2.0 * n)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    d = dist(T_MED, T0, N0)
    assert abs(d - D_NOM) < 1e-6
    cs = {"t_med": C / (2 * N0), "t_0": -C / (2 * N0), "n": -d / N0}
    us = {"t_med": UT, "t_0": UT0, "n": UN}
    print(f"d = {d:.4f} m")
    print("fuente    u_i          c_i              |c_i| u_i (m)   % de u_c^2")
    contrib = {k: abs(cs[k]) * us[k] for k in cs}
    uc2 = sum(v * v for v in contrib.values())
    for k in cs:
        print(f"{k:7s} {us[k]:10.3e} {cs[k]:16.6e} {contrib[k]:12.5f}   {100*contrib[k]**2/uc2:6.1f}")
    uc = math.sqrt(uc2)
    print(f"u_c = {uc:.5f} m ; U(k=2) = {2*uc:.5f} m")
    # Prueba 1: derivadas numericas = coeficientes analiticos
    h = {"t_med": 1e-12, "t_0": 1e-12, "n": 1e-9}
    base = {"t_med": T_MED, "t_0": T0, "n": N0}
    for k in cs:
        p, m = dict(base), dict(base)
        p[k] += h[k]
        m[k] -= h[k]
        num = (dist(p["t_med"], p["t_0"], p["n"]) - dist(m["t_med"], m["t_0"], m["n"])) / (2 * h[k])
        assert abs(num - cs[k]) / abs(cs[k]) < 1e-5, (k, num, cs[k])
    # Prueba 2: Monte Carlo
    rng = random.Random(5)
    M = 200000
    xs = [dist(T_MED + rng.gauss(0, UT), T0 + rng.gauss(0, UT0), N0 + rng.gauss(0, UN)) for _ in range(M)]
    mm = sum(xs) / M
    sd = math.sqrt(sum((v - mm) ** 2 for v in xs) / (M - 1))
    print(f"Monte Carlo: sd = {sd:.5f} m (analitico {uc:.5f}); sesgo = {mm - d:+.5f} m")
    assert abs(sd - uc) / uc < 0.01
    # Prueba 3: caso lineal exacto, suma de dos magnitudes -> cuadratura
    assert abs(math.sqrt(0.03 ** 2 + 0.04 ** 2) - 0.05) < 1e-15
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
