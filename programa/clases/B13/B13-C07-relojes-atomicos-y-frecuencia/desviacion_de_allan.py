#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C07: desviacion de Allan de un reloj simulado.

Datos: SINTETICOS (semilla fija). Serie de desviaciones relativas de
frecuencia y_k, promediadas cada tau0 = 1 s.
Modelo: desviacion de Allan no solapada (varianza de dos muestras):
  sigma_y^2(tau) = (1/2) <(ybar_{i+1} - ybar_i)^2>,  tau = m tau0,
donde ybar_i es el promedio de m muestras consecutivas.
Casos con solucion conocida:
 (a) rampa de frecuencia y_k = D k tau0 (deriva lineal): sigma_y(tau) =
     D tau / sqrt(2) EXACTAMENTE (diferencia de promedios contiguos = D m tau0);
 (b) ruido blanco de frecuencia y_k ~ N(0, s^2): sigma_y(tau) = s / sqrt(m)
     (pendiente -1/2 en escala log-log);
 (c) paseo aleatorio de frecuencia: pendiente +1/2.
Supuestos: muestras sin tiempo muerto. Validez: m <= N/4 para tener al menos
unas 4 parejas. Tolerancia: (a) 1e-12 relativa; (b) pendiente -0.5 +/- 0.08;
(c) +0.5 +/- 0.12.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def adev(y, m):
    k = len(y) // m
    prom = [sum(y[i * m:(i + 1) * m]) / m for i in range(k)]
    d = [(prom[i + 1] - prom[i]) ** 2 for i in range(k - 1)]
    return math.sqrt(sum(d) / (2 * len(d)))


def pendiente(ms, vals):
    xs = [math.log(m) for m in ms]
    ys = [math.log(v) for v in vals]
    xm, ym = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - xm) * (b - ym) for a, b in zip(xs, ys)) / sum((a - xm) ** 2 for a in xs)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    N = 2 ** 16
    ms = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    # (a) rampa
    D = 1e-17   # 1/s
    y = [D * k for k in range(N)]
    for m in (1, 10, 100):
        assert abs(adev(y, m) - D * m / math.sqrt(2)) / (D * m / math.sqrt(2)) < 1e-12
    # (b) ruido blanco de frecuencia
    rng = random.Random(3)
    s = 1e-12
    y = [rng.gauss(0, s) for _ in range(N)]
    av = [adev(y, m) for m in ms]
    pb = pendiente(ms, av)
    print("tau (s)   ADEV (blanco)   s/sqrt(tau)")
    for m, v in zip(ms, av):
        print(f"{m:6d}   {v:.4e}     {s / math.sqrt(m):.4e}")
    print(f"pendiente log-log (blanco) = {pb:.3f} (teorica -0.5)")
    assert abs(pb + 0.5) < 0.08
    # (c) paseo aleatorio de frecuencia
    y, acc = [], 0.0
    for _ in range(N):
        acc += rng.gauss(0, 1e-14)
        y.append(acc)
    pc = pendiente(ms, [adev(y, m) for m in ms])
    print(f"pendiente log-log (paseo aleatorio) = {pc:.3f} (teorica +0.5)")
    assert abs(pc - 0.5) < 0.12
    # Pruebas de la rampa como referencia exacta
    print(f"rampa: ADEV(tau=100 s) = {adev([D*k for k in range(N)], 100):.4e} (exacta {D*100/math.sqrt(2):.4e})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("FALLO: una prueba no se cumple")
        sys.exit(1)
