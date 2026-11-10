#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C03: transcripcion directa (colocacion trapezoidal) de un problema de control de minimo esfuerzo.

Problema SINTETICO adimensional (doble integrador, sin dimension fisica): x' = v, v' = u, t en [0, 1], x(0)=v(0)=0, x(1)=1, v(1)=0;
minimizar J = integral de u^2 dt. Solucion analitica: u*(t) = 6 - 12 t, x*(t) = 3 t^2 - 2 t^3, J* = 12.
Discretizacion: N tramos, nodos t_k = k/N; variables (x_k, v_k, u_k); defectos trapezoidales
x_{k+1} - x_k - h (v_k + v_{k+1})/2 = 0 y v_{k+1} - v_k - h (u_k + u_{k+1})/2 = 0; J_N = sum h (u_k^2 + u_{k+1}^2)/2.
Como el problema discreto es un QP con restricciones lineales, se resuelve con el sistema KKT (NumPy). Segunda via: SLSQP de SciPy (N = 8).
Tolerancias: |J_N - J_SLSQP| < 1e-6 (N = 8); orden de convergencia observado entre 1,8 y 2,2; error de J en N = 64 menor que 2e-2 (esperado ~ 0,75/N^2 * 12 / 64).
"""
from __future__ import annotations
import platform
import numpy as np
import scipy
from scipy.optimize import minimize


def armar(N):
    h = 1.0 / N
    n = 3 * (N + 1)  # [x(0..N), v(0..N), u(0..N)]
    ix = lambda k: k
    iv = lambda k: N + 1 + k
    iu = lambda k: 2 * (N + 1) + k
    filas, b = [], []
    for k in range(N):
        a = np.zeros(n)
        a[ix(k + 1)], a[ix(k)], a[iv(k)], a[iv(k + 1)] = 1, -1, -h / 2, -h / 2
        filas.append(a); b.append(0.0)
        a = np.zeros(n)
        a[iv(k + 1)], a[iv(k)], a[iu(k)], a[iu(k + 1)] = 1, -1, -h / 2, -h / 2
        filas.append(a); b.append(0.0)
    for idx, val in ((ix(0), 0.0), (iv(0), 0.0), (ix(N), 1.0), (iv(N), 0.0)):
        a = np.zeros(n); a[idx] = 1
        filas.append(a); b.append(val)
    A = np.array(filas)
    w = np.zeros(n)
    for k in range(N + 1):
        w[iu(k)] = h if 0 < k < N else h / 2
    return A, np.array(b), w, iu, ix, iv


def resolver_kkt(N):
    A, b, w, iu, ix, iv = armar(N)
    n = A.shape[1]
    H = np.diag(2 * w)  # J = sum w u^2 -> gradiente 2 w u
    K = np.block([[H, A.T], [A, np.zeros((A.shape[0], A.shape[0]))]])
    # la matriz H es singular en x y v, pero el sistema KKT es regular porque A fija x y v
    rhs = np.concatenate([np.zeros(n), b])
    sol = np.linalg.solve(K, rhs)
    z = sol[:n]
    J = float(np.sum(w[2 * (N + 1):] * z[2 * (N + 1):] ** 2))
    return z, J, iu


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    print("Problema SINTETICO adimensional: minimizar integral de u^2, J* = 12 (analitico)")
    print("   N     J_N        error J     orden   max|u - u*|")
    prev = None
    ordenes = []
    for N in (4, 8, 16, 32, 64, 128):
        z, J, iu = resolver_kkt(N)
        t = np.linspace(0, 1, N + 1)
        eu = np.max(np.abs(z[2 * (N + 1):] - (6 - 12 * t)))
        err = abs(J - 12.0)
        ord_ = "" if prev is None else f"{np.log2(prev / err):.2f}"
        if prev is not None:
            ordenes.append(np.log2(prev / err))
        print(f"{N:4d}  {J:10.6f}  {err:10.3e}  {ord_:>6}  {eu:10.3e}")
        prev = err
    # segunda via: SLSQP con N = 8
    N = 8
    A, b, w, iu, ix, iv = armar(N)
    n = A.shape[1]
    r = minimize(lambda z: float(np.sum(w[2 * (N + 1):] * z[2 * (N + 1):] ** 2)), np.zeros(n), jac=lambda z: np.concatenate([np.zeros(2 * (N + 1)), 2 * w[2 * (N + 1):] * z[2 * (N + 1):]]),
                 constraints=[{"type": "eq", "fun": lambda z: A @ z - b, "jac": lambda z: A}], method="SLSQP", options={"ftol": 1e-14, "maxiter": 200})
    zk, Jk, _ = resolver_kkt(N)
    print(f"N = 8: J (KKT) = {Jk:.9f} ; J (SLSQP) = {r.fun:.9f} ; diferencia = {abs(Jk - r.fun):.2e}")
    print(f"Tamano del problema N = 64: {3 * 65} variables y {2 * 64 + 4} restricciones")
    assert abs(Jk - r.fun) < 1e-6
    assert all(1.8 < o < 2.2 for o in ordenes[-3:])
    assert abs(resolver_kkt(64)[1] - 12) < 2e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
