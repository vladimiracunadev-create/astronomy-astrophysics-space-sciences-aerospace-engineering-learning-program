#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C03: SciPy para integrar, resolver raíces e integrar áreas.

Datos: GM de la Tierra = 3.986004e14 m3/s2 (valor nominal de la documentación
de astropy.constants) y radio 6378.137 km (NASA NSSDC Earth Fact Sheet 2024).
La órbita inicial es SINTÉTICA: circular a 400 km de altitud.
Modelo: dos cuerpos, r'' = -GM r / |r|^3 en un plano (x, y) de un sistema
inercial centrado en la Tierra; unidades SI (m, s).
Se usan: scipy.integrate.solve_ivp (DOP853 y RK45), scipy.optimize.brentq
(ecuación de Kepler M = E - e sin E) y scipy.integrate.quad.
Supuestos: masa puntual central, sin perturbaciones, sin rotación terrestre.
Validez: demostración numérica, no propagación operacional de órbitas.
Tolerancia: la órbita circular debe cerrar tras un período con error de
posición < 1e-3 m con DOP853 (rtol=1e-12, atol=1e-9); la energía específica
debe conservarse con deriva relativa < 1e-10; la raíz de Kepler cumple la
ecuación a 1e-12; quad contra integral exacta a 1e-10.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

GM = 3.986004e14
R_T = 6378.137e3


def dos_cuerpos(t, y):
    x, yy, vx, vy = y
    r3 = (x * x + yy * yy) ** 1.5
    return [vx, vy, -GM * x / r3, -GM * yy / r3]


def energia(y):
    r = math.hypot(y[0], y[1])
    return 0.5 * (y[2] ** 2 + y[3] ** 2) - GM / r


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    a = R_T + 400e3
    v = math.sqrt(GM / a)
    T = 2 * math.pi * math.sqrt(a**3 / GM)
    y0 = [a, 0.0, 0.0, v]
    print(f"a = {a/1e3:.3f} km, v = {v:.3f} m/s, T = {T:.3f} s")

    resultados = {}
    for metodo, rtol, atol in (("RK45", 1e-3, 1e-6), ("RK45", 1e-9, 1e-6), ("DOP853", 1e-12, 1e-9)):
        sol = solve_ivp(dos_cuerpos, (0, T), y0, method=metodo, rtol=rtol, atol=atol)
        yf = sol.y[:, -1]
        err_pos = math.hypot(yf[0] - a, yf[1])
        deriva = abs(energia(yf) - energia(y0)) / abs(energia(y0))
        resultados[(metodo, rtol)] = (err_pos, deriva, sol.nfev)
        print(f"{metodo:7s} rtol={rtol:g}: error de cierre = {err_pos:.3e} m, "
              f"deriva de energía = {deriva:.2e}, evaluaciones = {sol.nfev}")
    err_pos, deriva, _ = resultados[("DOP853", 1e-12)]
    prueba(err_pos < 1e-3, "cierre de la órbita (DOP853)")
    prueba(deriva < 1e-10, "conservación de energía (DOP853)")
    prueba(resultados[("RK45", 1e-3)][0] > 100 * err_pos, "la tolerancia por defecto debe ser peor")

    # salida densa: posición a T/4 frente a la solución analítica
    sol = solve_ivp(dos_cuerpos, (0, T), y0, method="DOP853", rtol=1e-12, atol=1e-9, dense_output=True)
    yq = sol.sol(T / 4)
    prueba(math.hypot(yq[0] - 0.0, yq[1] - a) < 1e-3, "posición a T/4")
    print(f"a T/4: (x, y) = ({yq[0]:.4f}, {yq[1]:.3f}) m  (esperado (0, {a:.3f}))")

    # ecuación de Kepler con brentq (e = 0.7, M = 1 rad)
    e, M = 0.7, 1.0
    E = brentq(lambda E: E - e * math.sin(E) - M, 0.0, math.pi, xtol=1e-14, rtol=1e-14)
    res = E - e * math.sin(E) - M
    print(f"Kepler: E = {E:.12f} rad, residuo = {res:.2e}")
    prueba(abs(res) < 1e-12, "residuo de Kepler")

    # quad: integral de sin(x) de 0 a pi = 2; y de exp(-x^2) = sqrt(pi)/2 de 0 a inf
    q1, err1 = quad(math.sin, 0, math.pi)
    q2, err2 = quad(lambda x: math.exp(-x * x), 0, math.inf)
    print(f"quad sin: {q1:.12f} (error estimado {err1:.1e}); gauss: {q2:.12f} (exacto {math.sqrt(math.pi)/2:.12f})")
    prueba(abs(q1 - 2) < 1e-10 and abs(q2 - math.sqrt(math.pi) / 2) < 1e-10, "quad")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
