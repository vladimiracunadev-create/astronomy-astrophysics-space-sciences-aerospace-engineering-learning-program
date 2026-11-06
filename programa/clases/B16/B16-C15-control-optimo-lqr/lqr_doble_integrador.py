#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C15: regulador cuadrático lineal (LQR) del eje rígido.

Datos: SINTÉTICOS. J = 50 kg m^2, x = [theta, omega], u = par (N m),
costo C = integral (q theta^2 + r u^2) dt con q = 1 y r variable; q y r se
dan en unidades de costo normalizadas (el costo C es adimensional por construcción).
Modelo: A = [[0,1],[0,0]], B = [0, 1/J]^T, Q = diag(q, 0), R = r.
Referencias independientes:
  - solución analítica del doble integrador (derivada en la clase):
      K1 = sqrt(q/r),  K2 = sqrt(2 J) (q/r)^(1/4),
      P12 = J sqrt(q r),  y el amortiguamiento del lazo es siempre
      zeta = 1/sqrt(2) = 0.7071, con wn = sqrt(K1/J);
  - método del hamiltoniano (subespacio estable) con numpy;
  - scipy.linalg.solve_continuous_are (SciPy 1.17.1 aquí; la documentación
    consultada es de la versión 1.18.0, misma ecuación);
  - el par máximo de la trayectoria ocurre en t = 0 (comprobado en 2001 instantes);
  - costo óptimo x0^T P x0 frente a la integral del costo a lo largo de la
    trayectoria simulada.
Supuestos: LTI, estado completo medido, sin saturación.
Tolerancia: 1e-9 entre métodos; 1e-6 relativa en el costo integrado.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.linalg import solve_continuous_are, expm
from scipy.integrate import solve_ivp

J = 50.0
A = np.array([[0.0, 1.0], [0.0, 0.0]])
B = np.array([[0.0], [1.0 / J]])


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def lqr_hamiltoniano(A, B, Q, R):
    n = A.shape[0]
    H = np.block([[A, -B @ np.linalg.inv(R) @ B.T], [-Q, -A.T]])
    w, v = np.linalg.eig(H)
    V = v[:, w.real < 0]
    X, Y = V[:n, :], V[n:, :]
    return np.real(Y @ np.linalg.inv(X))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    q = 1.0
    print("   r       K1        K2     wn(rad/s)  zeta   |u(0)| (N m) con theta0 = 0.1 rad   costo optimo x0'Px0")
    x0 = np.array([0.1, 0.0])
    for r in (1.0, 100.0, 10000.0):
        Q, R = np.diag([q, 0.0]), np.array([[r]])
        P_s = solve_continuous_are(A, B, Q, R)
        P_h = lqr_hamiltoniano(A, B, Q, R)
        K = (np.linalg.inv(R) @ B.T @ P_s)[0]
        K_ex = np.array([math.sqrt(q / r), math.sqrt(2 * J) * (q / r) ** 0.25])
        prueba(np.allclose(P_s, P_h, atol=1e-9 * max(1, np.abs(P_s).max())), "ARE vs hamiltoniano")
        prueba(np.allclose(K, K_ex, rtol=1e-9), "K frente a la fórmula cerrada")
        wn, z = math.sqrt(K[0] / J), K[1] / (2 * math.sqrt(K[0] * J))
        prueba(abs(z - 1 / math.sqrt(2)) < 1e-9, "zeta = 1/sqrt 2")
        Jopt = x0 @ P_s @ x0
        # costo a lo largo de la trayectoria
        def f(t, s):
            x, c = s[:2], s[2]
            u = -K @ x
            return [x[1], u / J, q * x[0]**2 + r * u**2]
        sol = solve_ivp(f, [0, 2000], [x0[0], x0[1], 0.0], rtol=1e-11, atol=1e-14)
        Jnum = sol.y[2, -1]
        prueba(abs(Jnum - Jopt) < 1e-6 * Jopt, "costo óptimo vs integrado")
        Acl = A - B @ K[None, :]
        picou = max(abs(-K @ (expm(Acl * tt) @ x0)) for tt in np.linspace(0, 400, 2001))
        prueba(abs(picou - abs(K @ x0)) < 1e-12, "el par máximo ocurre en t = 0")
        print(f"{r:8.0f}  {K[0]:7.4f}  {K[1]:8.4f}   {wn:6.4f}   {z:5.4f}   {abs(K@x0):9.5f}            {Jopt:.6f} (integrado {Jnum:.6f})")
    # el LQR siempre estabiliza: autovalores del lazo
    ev = np.linalg.eigvals(A - B @ K[None, :])
    prueba(np.all(ev.real < 0), "lazo estable")
    print("autovalores (r = 10000):", np.round(ev, 5))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
