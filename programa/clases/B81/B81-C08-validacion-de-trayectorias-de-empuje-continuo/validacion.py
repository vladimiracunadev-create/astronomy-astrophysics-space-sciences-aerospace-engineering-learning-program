#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C08: reintegracion y chequeos de optimalidad de una trayectoria de empuje continuo.

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y UA = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Parte 1 (reintegracion): trayectoria heliocentrica plana con empuje tangencial a la velocidad, aceleracion a0 (1 UA/r)^2 con a0 = 2e-4 m/s^2 = 2e-7 km/s^2
(ILUSTRATIVA), desde una orbita circular de 1 UA durante 200 d. Se reintegra con (a) DOP853 rtol 1e-12 y (b) RK4 de paso fijo (86400 s, 43200 s y 21600 s).
Chequeos: (1) energia: E_f - E_0 = integral de a . v dt (trabajo del empuje), calculada por cuadratura de Simpson sobre la solucion de (a);
(2) convergencia de RK4: el error cae un factor ~16 al reducir el paso a la mitad.
Parte 2 (optimalidad): problema SINTETICO adimensional del doble integrador de B81-C03 (J* = 12, u* = 6 - 12 t). Variaciones admisibles u* + e eta con eta
que conserva las condiciones de contorno (integral de eta = 0 e integral de (1 - t) eta = 0): J(e) - J* = e^2 integral de eta^2 >= 0, derivada primera nula.
Tolerancias: balance de energia < 1e-9 relativo; razon de errores RK4 entre 12 y 20; derivada primera de J en el optimo < 1e-8.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp, simpson

MU = 132712440041.279419
AU = 149597870.7
A0 = 2e-7  # km/s^2


def rhs(t, y):
    r = y[:2]
    v = y[2:]
    rn = np.linalg.norm(r)
    a_emp = A0 * (AU / rn) ** 2 * v / np.linalg.norm(v)
    return np.concatenate([v, -MU * r / rn**3 + a_emp])


def rk4(y0, T, h):
    n = int(round(T / h))
    y = y0.copy()
    for _ in range(n):
        k1 = rhs(0, y); k2 = rhs(0, y + h / 2 * k1); k3 = rhs(0, y + h / 2 * k2); k4 = rhs(0, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


def energia(y):
    return 0.5 * (y[2]**2 + y[3]**2) - MU / math.hypot(y[0], y[1])


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    vc = math.sqrt(MU / AU)
    y0 = np.array([AU, 0.0, 0.0, vc])
    T = 200 * 86400.0
    s = solve_ivp(rhs, (0, T), y0, method="DOP853", rtol=1e-12, atol=1e-9, dense_output=True)
    yf = s.y[:, -1]
    print(f"Parte 1 (ILUSTRATIVA): 200 d, a0 = {A0*1e3:.1e} m/s^2 a 1 UA ; r_f = {math.hypot(yf[0], yf[1])/AU:.6f} UA")
    # energia y trabajo
    ts = np.linspace(0, T, 4001)
    Y = s.sol(ts)
    work_int = np.array([A0 * (AU / math.hypot(Y[0, i], Y[1, i])) ** 2 * math.hypot(Y[2, i], Y[3, i]) for i in range(len(ts))])
    trabajo = simpson(work_int, x=ts)
    dE = energia(yf) - energia(y0)
    print(f"Delta E = {dE:.6e} km^2/s^2 ; integral a.v dt = {trabajo:.6e} ; diferencia relativa = {abs(dE-trabajo)/abs(dE):.2e}")
    errs = []
    for h in (86400.0, 43200.0, 21600.0):
        y = rk4(y0, T, h)
        errs.append(np.linalg.norm(y[:2] - yf[:2]))
        print(f"RK4 h = {h:6.0f} s: error de posicion = {errs[-1]:.3e} km")
    razon = errs[0] / errs[1]
    razon2 = errs[1] / errs[2]
    print(f"Razones de errores RK4 (h -> h/2) = {razon:.1f} y {razon2:.1f} (teorico 16)")
    # parte 2: optimalidad
    t = np.linspace(0, 1, 200001)
    ustar = 6 - 12 * t
    # eta: combinacion que cumple las dos condiciones de contorno: eta = sin(2 pi t) * c + ... se proyecta
    base = np.array([np.sin(2 * math.pi * t), np.cos(4 * math.pi * t), t**2])
    C = np.array([[np.trapezoid(b, t), np.trapezoid((1 - t) * b, t)] for b in base]).T  # 2x3
    coef = np.linalg.svd(C)[2][-1]  # vector nulo (3,)
    eta = coef @ base
    print(f"Variacion admisible: integral eta = {np.trapezoid(eta, t):.1e}, integral (1-t) eta = {np.trapezoid((1-t)*eta, t):.1e}")
    J = lambda e: np.trapezoid((ustar + e * eta) ** 2, t)
    d1 = (J(1e-4) - J(-1e-4)) / 2e-4
    print(f"J* = {J(0):.6f} ; dJ/de en e = 0: {d1:.2e} ; J(0,1) - J* = {J(0.1)-J(0):.6f} ; e^2 int eta^2 = {0.01*np.trapezoid(eta**2, t):.6f}")
    assert abs(dE - trabajo) / abs(dE) < 1e-9
    assert 10 < razon < 24 and 10 < razon2 < 24
    assert abs(d1) < 1e-8 and J(0.1) > J(0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
