#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C05: verificacion de un codigo de estructura y evolucion por orden de convergencia y control del paso de tiempo.

Datos: ninguna constante fisica. Todo es SINTETICO (ilustrativo): el problema de estructura es el politropo n = 1 (solucion analitica theta = sin(xi)/xi, xi_1 = pi) y la
"evolucion quimica" es dX/dt = -k X^2 (solucion analitica X = X0/(1 + k X0 t)) con k y X0 elegidos para la prueba.
Modelo: integradores de paso fijo de ordenes 1 (Euler), 2 (punto medio) y 4 (Runge-Kutta) para Lane-Emden con arranque en serie; orden observado p = log2(e(h)/e(h/2)).
Paso de tiempo: Euler implicito con paso dt = eta X/|dX/dt| (control relativo); error global a t_fin frente a la solucion analitica en funcion de eta.
Supuestos: problemas suaves, sin discontinuidades de fisica de entrada. Validez: solo sirve para verificar el codigo, no la fisica.
Tolerancia: orden observado dentro de 0,15 del teorico en los ordenes 1 y 2 y de 0,5 en el 4; error del paso adaptativo decreciente con eta y de primer orden.
"""
from __future__ import annotations
import math, platform, sys


def paso(xi, th, ph, h, orden):
    def f(x, t, p):
        return p, -2 * p / x - t

    k1 = f(xi, th, ph)
    if orden == 1:
        return th + h * k1[0], ph + h * k1[1]
    k2 = f(xi + h / 2, th + h / 2 * k1[0], ph + h / 2 * k1[1])
    if orden == 2:
        return th + h * k2[0], ph + h * k2[1]
    k3 = f(xi + h / 2, th + h / 2 * k2[0], ph + h / 2 * k2[1])
    k4 = f(xi + h, th + h * k3[0], ph + h * k3[1])
    return th + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), ph + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])


def xi1(h, orden):
    xi = h
    th = 1 - xi**2 / 6 + xi**4 / 120 - 3 * xi**6 / 15120
    ph = -xi / 3 + xi**3 / 30 - 18 * xi**5 / 15120
    while True:
        tn, pn = paso(xi, th, ph, h, orden)
        if tn <= 0:
            lo, hi = 0.0, h  # ultimo paso recortado hasta theta = 0
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if paso(xi, th, ph, mid, orden)[0] > 0:
                    lo = mid
                else:
                    hi = mid
            return xi + 0.5 * (lo + hi)
        xi, th, ph = xi + h, tn, pn


def evolucion(eta, k=1.0, X0=1.0, tfin=10.0):
    t, X, pasos = 0.0, X0, 0
    while t < tfin - 1e-15:
        dt = min(eta * X / (k * X * X), tfin - t)
        # Euler implicito: X1 = X + dt*(-k X1^2) -> k dt X1^2 + X1 - X = 0
        X = (-1 + math.sqrt(1 + 4 * k * dt * X)) / (2 * k * dt)
        t += dt
        pasos += 1
    return X, pasos


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'orden':>6} {'h':>9} {'error de xi_1':>15} {'p observado':>12}")
    for orden, hs in ((1, (0.02, 0.01, 0.005)), (2, (0.04, 0.02, 0.01)), (4, (0.2, 0.1, 0.05))):
        prev = None
        for h in hs:
            e = abs(xi1(h, orden) - math.pi)
            if prev is None:
                print(f"{orden:>6} {h:9.4f} {e:15.3e} {'-':>12}")
            else:
                p = math.log2(prev / e)
                print(f"{orden:>6} {h:9.4f} {e:15.3e} {p:12.2f}")
                assert abs(p - orden) < (0.15 if orden != 4 else 0.5)
            prev = e
    print(f"{'eta':>6} {'pasos':>6} {'error de X(10)':>16} {'cociente':>9}")
    exacto = 1.0 / (1 + 1.0 * 1.0 * 10.0)
    prev = None
    for eta in (0.2, 0.1, 0.05, 0.025):
        X, n = evolucion(eta)
        e = abs(X - exacto)
        print(f"{eta:6.3f} {n:6d} {e:16.4e} {'-' if prev is None else f'{prev / e:9.2f}':>9}")
        if prev is not None:
            assert 1.6 < prev / e < 2.4
        prev = e
    print(f"solucion analitica X(10) = {exacto:.6f}")
    # el paso demasiado grande no converge: con eta = 5 el error es grande
    X, n = evolucion(5.0)
    print(f"eta = 5 (paso excesivo): X(10) = {X:.4f} ; error relativo = {abs(X / exacto - 1):.2f}")
    assert abs(X / exacto - 1) > 0.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
