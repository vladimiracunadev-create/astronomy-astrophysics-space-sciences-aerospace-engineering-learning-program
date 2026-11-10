#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C12: cota de control (restriccion de trayectoria) en un problema de minimo esfuerzo, por conjunto activo.

Sin fuentes externas: problema SINTETICO adimensional, el de B81-C03 (doble integrador, x(0)=v(0)=0, x(1)=1, v(1)=0, T=1, minimizar integral de u^2),
con la restriccion |u(t)| <= U. Control constante a trozos en N = 200 tramos de duracion h = T/N.
Efecto lineal de u_k: v(T) = sum h u_k ; x(T) = sum h (T - t_mid,k) u_k, con t_mid,k el punto medio del tramo.
Sin cota: u* = 6 - 12 t (J* = 12, max |u| = 6). Con cota, la solucion es u = clip(mu1 + mu2 (T - t_mid), -U, U) (condiciones KKT); se resuelve por conjunto activo:
se fijan los saturados, se resuelve el sistema reducido y se repite hasta que no cambie el conjunto.
Tiempo minimo con la cota: T_min = 2 sqrt(d/U) (bang-bang, d = 1) para x(T)=d y v(T)=0 partiendo del reposo.
Segunda via: SLSQP de SciPy con N = 40 y cotas.
Tolerancias: sin cota J = 12 con error < 1e-3; SLSQP frente a conjunto activo (N = 40) < 1e-6 relativo; con U < 6 el coste crece.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.optimize import minimize


def matriz(N, T=1.0):
    h = T / N
    tm = (np.arange(N) + 0.5) * h
    A = np.vstack([h * (T - tm), h * np.ones(N)])
    return A, h


def conjunto_activo(N, U, T=1.0, d=1.0):
    A, h = matriz(N, T)
    b = np.array([d, 0.0])
    libre = np.ones(N, bool)
    u = np.zeros(N)
    for it in range(60):
        fijo = ~libre
        r = b - A[:, fijo] @ u[fijo]
        Al = A[:, libre]
        if Al.shape[1] == 0:
            return None, it
        lam = np.linalg.solve(Al @ Al.T, r)
        u_l = Al.T @ lam
        u[libre] = u_l
        viol = np.abs(u) > U + 1e-12
        if not viol[libre].any():
            return u, it + 1
        nuevo = libre & viol
        u[nuevo] = np.sign(u[nuevo]) * U
        libre = libre & ~viol
    return None, 60


def coste(u, T=1.0):
    return float(np.sum(u * u) * T / len(u))


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    N = 200
    print("Problema SINTETICO adimensional: minimo esfuerzo con |u| <= U (T = 1, d = 1) ; sin cota: J* = 12, max|u| = 6")
    print("    U     J        max|u|   saturados   iteraciones")
    J_sin = None
    for U in (100.0, 6.0, 5.0, 4.5, 4.2, 4.0, 3.0):
        u, it = conjunto_activo(N, U)
        if u is None:
            print(f"{U:6.2f}   infactible (T < T_min)")
            continue
        sat = int(np.sum(np.abs(u) >= U - 1e-9))
        print(f"{U:6.2f}  {coste(u):8.4f}  {np.max(np.abs(u)):7.4f}  {sat:9d}  {it:6d}")
        if U == 100.0:
            J_sin = coste(u)
    for U in (2.0, 1.9):
        u, it = conjunto_activo(N, U)
        print(f"{U:6.2f}   {'infactible' if u is None else f'J = {coste(u):.4f}'}")
    print(f"Tiempo minimo T_min = 2 sqrt(d/U): U = 4 -> {2*math.sqrt(1/4):.4f} ; U = 2,5 -> {2*math.sqrt(1/2.5):.4f} ; U = 2 -> {2*math.sqrt(1/2):.4f} (mayor que T = 1: infactible)")
    # exacto de T=1: U_min = 4 d/T^2 = 4
    print(f"Con T = 1 la cota minima factible es U = 4 d/T^2 = 4,0 (bang-bang, J = 16)")
    u4, _ = conjunto_activo(N, 4.0001)
    print(f"Con U = 4,0001: J = {coste(u4):.4f} ; max|u| = {np.max(np.abs(u4)):.4f}")
    # segunda via N = 40
    Nn = 40
    u_a, _ = conjunto_activo(Nn, 5.0)
    A, h = matriz(Nn)
    r = minimize(lambda z: float(np.sum(z * z) * h), np.zeros(Nn), jac=lambda z: 2 * z * h, bounds=[(-5.0, 5.0)] * Nn,
                 constraints=[{"type": "eq", "fun": lambda z: A @ z - np.array([1.0, 0.0]), "jac": lambda z: A}], method="SLSQP", options={"ftol": 1e-14, "maxiter": 300})
    print(f"N = 40, U = 5: J (conjunto activo) = {coste(u_a):.9f} ; J (SLSQP) = {r.fun:.9f} ; diferencia relativa = {abs(coste(u_a)-r.fun)/r.fun:.1e}")
    assert abs(J_sin - 12.0) < 1e-3
    assert abs(coste(u_a) - r.fun) / r.fun < 1e-6
    ua, _ = conjunto_activo(N, 5.0)
    ub, _ = conjunto_activo(N, 4.5)
    assert coste(ub) > coste(ua) > J_sin
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
