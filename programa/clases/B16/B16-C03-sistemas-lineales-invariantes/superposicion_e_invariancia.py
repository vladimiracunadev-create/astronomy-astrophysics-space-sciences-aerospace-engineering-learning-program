#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C03: superposición, invariancia y convolución.

Datos: SINTÉTICOS. Eje con inercia J = 50 kg m^2 y amortiguamiento viscoso
c = 10 N m s/rad (modelo de fricción en la rueda): J omega' + c omega = tau.
Modelo: LTI de primer orden en omega; respuesta al impulso h(t) = e^{-c t/J}/J.
Referencia independiente: solve_ivp (Radau, rtol 1e-11) del mismo modelo.
Supuestos: sistema en reposo en t = 0; par de entrada u(t) = 0.3 sin(0.5 t)
(N m). Un contraejemplo no lineal (saturación del par a 0.2 N m).
Tolerancia: convolución vs ODE 1e-5 relativa (regla del trapecio, dt = 1e-3 s).
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


J, c = 50.0, 10.0
tm = J / c                                         # constante de tiempo (s)


def simula(u, T=40.0, t_eval=None, sat=None):
    def f(t, w):
        x = u(t)
        if sat is not None:
            x = np.clip(x, -sat, sat)
        return [(-c * w[0] + x) / J]
    s = solve_ivp(f, [0, T], [0.0], t_eval=t_eval, method="Radau", rtol=1e-11, atol=1e-13, max_step=0.05)
    return s.y[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    dt, T = 1e-3, 40.0
    t = np.arange(0, T + dt / 2, dt)
    u1 = lambda s: 0.3 * np.sin(0.5 * s)
    u2 = lambda s: 0.1 * (s > 5.0)                 # escalón desplazado

    y1 = simula(u1, T, t)
    y2 = simula(u2, T, t)
    ys = simula(lambda s: 2 * u1(s) + 3 * u2(s), T, t)
    err_sup = np.max(np.abs(ys - (2 * y1 + 3 * y2)))
    print(f"superposición: max|y(2u1+3u2) - (2y1+3y2)| = {err_sup:.2e} rad/s")
    prueba(err_sup < 1e-8, "superposición")

    # invariancia: retrasar la entrada 7 s retrasa la salida 7 s
    d = 7.0
    yd = simula(lambda s: u1(s - d) * (s >= d), T, t)
    k = int(round(d / dt))
    err_inv = np.max(np.abs(yd[k:] - y1[: len(y1) - k]))
    print(f"invariancia: max|y_retrasada - retraso(y)| = {err_inv:.2e} rad/s")
    prueba(err_inv < 1e-7, "invariancia temporal")

    # convolución con la respuesta al impulso
    h = np.exp(-t / tm) / J
    u = u1(t)
    conv = np.convolve(h, u)[: len(t)] * dt - 0.5 * dt * (h * u[0] + h[0] * u)  # trapecio
    err_c = np.max(np.abs(conv - y1)) / np.max(np.abs(y1))
    print(f"convolución vs ODE: error relativo máx = {err_c:.2e}")
    prueba(err_c < 1e-5, "convolución")

    # contraejemplo: con saturación deja de valer la superposición
    ya = simula(u1, T, t, sat=0.2)
    yb = simula(lambda s: 2 * u1(s), T, t, sat=0.2)
    viol = np.max(np.abs(yb - 2 * ya))
    print(f"con saturación a 0.2 N m: max|y(2u) - 2y(u)| = {viol:.3e} rad/s (≠ 0)")
    prueba(viol > 1e-3, "la saturación debe violar la superposición")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
