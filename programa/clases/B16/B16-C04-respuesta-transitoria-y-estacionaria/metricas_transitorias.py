#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C04: métricas de la respuesta transitoria y error estacionario.

Datos: SINTÉTICOS. Lazo de apuntamiento ideal de segundo orden
theta'' + 2 zeta wn theta' + wn^2 theta = wn^2 r, con wn = 0.5 rad/s.
Modelo: respuesta a un escalón de 1 (adimensional, normalizado).
Referencia independiente: fórmulas cerradas
  Mp = exp(-pi zeta / sqrt(1 - zeta^2)),  tp = pi / (wn sqrt(1 - zeta^2)),
  ts(2 %) ~ 4 / (zeta wn)  (aproximación, no identidad).
Supuestos: 0 < zeta < 1 (subamortiguado), condiciones iniciales nulas.
Tolerancia: Mp y tp 1e-4 relativa (rejilla dt = 1e-4 s); ts dentro del 15 %.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def escalon(t, z, wn):
    wd = wn * math.sqrt(1 - z * z)
    ph = math.acos(z)
    return 1 - np.exp(-z * wn * t) / math.sqrt(1 - z * z) * np.sin(wd * t + ph)


def metricas(z, wn, T=80.0, dt=1e-4):
    t = np.arange(0, T, dt)
    y = escalon(t, z, wn)
    mp = y.max() - 1
    tp = t[y.argmax()]
    fuera = np.nonzero(np.abs(y - 1) > 0.02)[0]
    ts = t[fuera[-1]] + dt
    tr = t[np.argmax(y >= 0.9)] - t[np.argmax(y >= 0.1)]
    return mp, tp, ts, tr


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    wn = 0.5
    print(" zeta |  Mp medido  Mp fórmula | tp medido tp fórmula | ts medido  4/(z wn) | tr (10-90 %)")
    for z in (0.2, 0.5, 0.7, 0.9):
        mp, tp, ts, tr = metricas(z, wn)
        mp_f = math.exp(-math.pi * z / math.sqrt(1 - z * z))
        tp_f = math.pi / (wn * math.sqrt(1 - z * z))
        ts_f = 4 / (z * wn)
        print(f" {z:4.1f} | {mp:10.6f} {mp_f:11.6f} | {tp:8.4f} {tp_f:9.4f} | {ts:8.3f} {ts_f:9.3f} | {tr:7.3f}")
        prueba(abs(mp - mp_f) <= 1e-4 * max(mp_f, 1e-3) + 1e-6, f"Mp zeta={z}")
        prueba(abs(tp - tp_f) <= 1e-4 * tp_f + 2e-4, f"tp zeta={z}")
        if z <= 0.7:
            prueba(abs(ts - ts_f) <= 0.15 * ts_f, f"ts zeta={z}")
    # error estacionario de un lazo con control PD sobre la planta 1/(J s^2):
    J, Kp, Kd, d = 50.0, 20.0, 40.0, 0.5       # d: par perturbador constante (N m)
    e_ss = d / Kp
    wn_l, z_l = math.sqrt(Kp / J), Kd / (2 * math.sqrt(Kp * J))
    print(f"lazo PD: wn = {wn_l:.4f} rad/s, zeta = {z_l:.4f}; error estacionario con d = {d} N m: d/Kp = {e_ss*1e3:.1f} mrad")
    prueba(abs(e_ss - 0.025) < 1e-15, "error estacionario d/Kp")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
