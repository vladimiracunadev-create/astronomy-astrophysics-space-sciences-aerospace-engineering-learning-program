#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C01: un modelo dinámico, su estado y su integración numérica.

Datos: SINTÉTICOS (simulados). Telescopio de un eje con inercia J = 50 kg m^2,
par de control constante tau = 0.2 N m y rueda de reacción con constante de
tiempo 1/a = 2 s. No son datos de ninguna misión.
Modelo: J theta'' = tau  (estado x = [theta, omega]);  wheel: w' = -a w + b u.
Ambos tienen solución exacta (polinomio cuadrático y exponencial).
Se integra con Runge-Kutta de cuarto orden propio (B11-C07), paso fijo.
Supuestos: cuerpo rígido, eje principal fijo, sin perturbaciones, par exacto.
Validez: ángulos pequeños no se requieren aquí (el modelo es lineal en el eje).
Tolerancia: 1e-9 relativa para ambos casos con paso 0.01 s; el error del
péndulo linealizado es un resultado, no una prueba.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np


def rk4(f, x0, t0, t1, h):
    """Integra x' = f(t, x) de t0 a t1 con paso h (RK4 clásico)."""
    n = int(round((t1 - t0) / h))
    x = np.array(x0, dtype=float)
    t = t0
    for _ in range(n):
        k1 = f(t, x)
        k2 = f(t + h / 2, x + h / 2 * k1)
        k3 = f(t + h / 2, x + h / 2 * k2)
        k4 = f(t + h, x + h * k3)
        x = x + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return x


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    J, tau = 50.0, 0.2
    th0, w0, T = 0.01, 0.002, 60.0          # rad, rad/s, s

    f = lambda t, x: np.array([x[1], tau / J])
    x = rk4(f, [th0, w0], 0.0, T, 0.01)
    th_ex = th0 + w0 * T + 0.5 * (tau / J) * T**2
    w_ex = w0 + (tau / J) * T
    print(f"theta(60 s) = {x[0]:.9f} rad (exacto {th_ex:.9f});  omega = {x[1]:.9f} rad/s (exacto {w_ex:.9f})")
    prueba(abs(x[0] - th_ex) <= 1e-9 * abs(th_ex), "ángulo de deriva con par constante")
    prueba(abs(x[1] - w_ex) <= 1e-9 * abs(w_ex), "velocidad con par constante")

    # rueda de primer orden: w' = -a w + b u, u = 1 (escalón)
    a, b, u = 0.5, 0.5, 1.0
    g = lambda t, w: np.array([-a * w[0] + b * u])
    w = rk4(g, [0.0], 0.0, 6.0, 0.01)[0]
    w_ex = (b * u / a) * (1 - math.exp(-a * 6.0))
    print(f"rueda: w(6 s) = {w:.9f} (exacto {w_ex:.9f}); fracción del valor final = {w / (b*u/a):.4f}")
    prueba(abs(w - w_ex) <= 1e-9 * abs(w_ex), "primer orden")

    # ¿hasta dónde sirve el modelo lineal? péndulo: sin(th) ~ th
    print("error relativo de sin(th) ~ th:")
    for th in (0.05, 0.1, 0.2, 0.5, 1.0):
        print(f"  th = {th:4.2f} rad -> {abs(math.sin(th) - th) / math.sin(th) * 100:6.3f} %")
    e1 = abs(math.sin(0.1) - 0.1) / math.sin(0.1)
    prueba(abs(e1 - 1.6683e-3) < 1e-6, "error de sin a 0.1 rad")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
