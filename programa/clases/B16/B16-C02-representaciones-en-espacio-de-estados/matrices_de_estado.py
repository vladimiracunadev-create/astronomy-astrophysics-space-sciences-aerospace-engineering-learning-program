#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C02: matrices A, B, C, D, exponencial matricial y discretización.

Datos: SINTÉTICOS. Telescopio de un eje, J = 50 kg m^2, medida de ángulo
(sensor de estrellas ideal). Sin ruido.
Modelo: x' = A x + B u, y = C x + D u con x = [theta, omega], u = par (N m).
Solución: x(t) = expm(A t) x0 + int expm(A (t-s)) B u(s) ds.
Referencia independiente: fórmulas cerradas del doble integrador
(expm(A t) = [[1, t], [0, 1]]) y discretización exacta con par constante.
Supuestos: LTI, par constante entre muestras (retenedor de orden cero).
Tolerancia: 1e-12 relativa en matrices; 1e-10 en la trayectoria.
"""
from __future__ import annotations
import platform, sys
import numpy as np
from scipy.linalg import expm
import scipy


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def zoh(A, B, T):
    """Discretización exacta con retenedor de orden cero (bloque aumentado)."""
    n, m = A.shape[0], B.shape[1]
    M = np.zeros((n + m, n + m))
    M[:n, :n], M[:n, n:] = A, B
    E = expm(M * T)
    return E[:n, :n], E[:n, n:]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    J, T = 50.0, 0.5
    A = np.array([[0.0, 1.0], [0.0, 0.0]])
    B = np.array([[0.0], [1.0 / J]])
    C = np.array([[1.0, 0.0]])
    print("A =", A.tolist(), " B =", B.ravel().tolist(), " C =", C.ravel().tolist(), " D = 0")

    t = 3.0
    E = expm(A * t)
    prueba(np.allclose(E, [[1, t], [0, 1]], rtol=1e-12, atol=1e-14), "expm del doble integrador")
    print("expm(A t) con t = 3:", E.tolist())

    Ad, Bd = zoh(A, B, T)
    Ad_ex = np.array([[1, T], [0, 1]])
    Bd_ex = np.array([[T**2 / (2 * J)], [T / J]])
    prueba(np.allclose(Ad, Ad_ex, rtol=1e-12, atol=1e-14), "Ad")
    prueba(np.allclose(Bd, Bd_ex, rtol=1e-12, atol=1e-14), "Bd")
    print("Ad =", Ad.tolist(), "\nBd =", Bd.ravel().tolist())

    # 120 pasos de 0.5 s con par constante 0.2 N m == fórmula cerrada a 60 s
    x = np.array([[0.01], [0.002]])
    for _ in range(120):
        x = Ad @ x + Bd * 0.2
    th_ex = 0.01 + 0.002 * 60 + 0.5 * (0.2 / J) * 60**2
    prueba(abs(x[0, 0] - th_ex) < 1e-10, "trayectoria discreta")
    print(f"theta(60 s) discreto = {x[0,0]:.9f} rad; cerrado = {th_ex:.9f} rad")

    # cambio de base: los autovalores y la respuesta no cambian
    P = np.array([[1.0, 2.0], [0.0, 1.0]])
    Ap = np.linalg.inv(P) @ A @ P
    print("autovalores de A:", np.linalg.eigvals(A), " de P^-1 A P:", np.linalg.eigvals(Ap))
    prueba(np.allclose(np.sort(np.linalg.eigvals(Ap)), np.sort(np.linalg.eigvals(A))), "invariancia de autovalores")

    # masa-resorte-amortiguador: mismas matrices con otro significado físico
    m, c, k = 2.0, 0.4, 8.0
    A2 = np.array([[0, 1], [-k / m, -c / m]])
    lam = np.linalg.eigvals(A2)
    print(f"masa-resorte-amortiguador: autovalores {lam[0]:.4f}, {lam[1]:.4f}; wn = {np.sqrt(k/m):.4f} rad/s")
    prueba(abs(abs(lam[0]) - np.sqrt(k / m)) < 1e-12, "|lambda| = wn")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
