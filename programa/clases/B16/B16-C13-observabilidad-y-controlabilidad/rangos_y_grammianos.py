#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C13: controlabilidad, observabilidad y grammiano.

Datos: SINTÉTICOS. Cuerpo rígido linealizado en torno a la orientación nula y
sin momento almacenado: tres ejes desacoplados, J = diag(50, 40, 30) kg m^2,
estado x = [th_x, w_x, th_y, w_y, th_z, w_z]. Entradas: pares de ruedas.
Modelo: x' = A x + B u, y = C x.
Referencias independientes:
  - rango de la matriz de controlabilidad [B, AB, ..., A^(n-1) B] y de
    observabilidad (Kalman); también la prueba PBH;
  - grammiano de controlabilidad del doble integrador en [0, T]:
    W = [[T^3/(3 J^2), T^2/(2 J^2)], [T^2/(2 J^2), T/J^2]];
  - energía mínima de un giro de reposo a reposo de ángulo D en el tiempo T:
    E = 12 J^2 D^2 / T^3 = x_f^T W^-1 x_f;
  - un modo no controlable con salida acotada: x1' = -x1 + u, x2' = 2 x2,
    y = x1, cuya función de transferencia 1/(s+1) oculta e^(2t).
Supuestos: LTI, linealización en el origen (el resultado NO vale para el
sistema no lineal completo). Tolerancia: rangos exactos; 1e-8 relativa en W y E.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy.integrate import quad_vec
from scipy.linalg import expm


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def ctrb(A, B):
    n = A.shape[0]
    M = [B]
    for _ in range(n - 1):
        M.append(A @ M[-1])
    return np.hstack(M)


def obsv(A, C):
    return ctrb(A.T, C.T).T


def eje(J):
    return np.array([[0.0, 1.0], [0.0, 0.0]]), np.array([[0.0], [1.0 / J]])


def pbh_no_controlable(A, B):
    """Autovalores en los que rango [lambda I - A, B] < n (prueba PBH)."""
    n = A.shape[0]
    malos = []
    for lam in np.unique(np.round(np.linalg.eigvals(A), 9)):
        if np.linalg.matrix_rank(np.hstack([lam * np.eye(n) - A, B]), tol=1e-9) < n:
            malos.append(float(lam))
    return malos


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    Js = (50.0, 40.0, 30.0)
    A = np.zeros((6, 6)); B3 = np.zeros((6, 3))
    for i, J in enumerate(Js):
        a, b = eje(J)
        A[2*i:2*i+2, 2*i:2*i+2] = a
        B3[2*i:2*i+2, i] = b.ravel()
    r3 = np.linalg.matrix_rank(ctrb(A, B3))
    r2 = np.linalg.matrix_rank(ctrb(A, B3[:, :2]))
    r1 = np.linalg.matrix_rank(ctrb(A, B3[:, :1]))
    print(f"rango de controlabilidad con 3, 2 y 1 ruedas: {r3}, {r2}, {r1} (n = 6)")
    prueba((r3, r2, r1) == (6, 4, 2), "rangos de controlabilidad")
    print("PBH con 2 ruedas: autovalores no controlables", pbh_no_controlable(A, B3[:, :2]))
    prueba(len(pbh_no_controlable(A, B3[:, :2])) == 1, "PBH detecta el modo z")

    a, b = eje(50.0)
    c_ang, c_vel = np.array([[1.0, 0.0]]), np.array([[0.0, 1.0]])
    print(f"observabilidad midiendo ángulo: rango {np.linalg.matrix_rank(obsv(a, c_ang))}; "
          f"midiendo solo velocidad: rango {np.linalg.matrix_rank(obsv(a, c_vel))} (n = 2)")
    prueba(np.linalg.matrix_rank(obsv(a, c_ang)) == 2 and np.linalg.matrix_rank(obsv(a, c_vel)) == 1,
           "rangos de observabilidad")

    # grammiano y energía mínima
    J, T, D = 50.0, 20.0, 0.1
    W_ex = np.array([[T**3 / (3 * J**2), T**2 / (2 * J**2)], [T**2 / (2 * J**2), T / J**2]])
    W_num, _ = quad_vec(lambda t: (expm(a * t) @ b) @ (expm(a * t) @ b).T, 0.0, T, epsabs=1e-13, epsrel=1e-13)
    err = np.max(np.abs(W_num - W_ex) / np.abs(W_ex))
    print(f"grammiano numérico vs cerrado: error relativo máx = {err:.2e}")
    prueba(err < 1e-8, "grammiano")
    xf = np.array([[D], [0.0]])
    E = (xf.T @ np.linalg.inv(W_num) @ xf).item()
    E_ex = 12 * J**2 * D**2 / T**3
    print(f"energía mínima de un giro de {D} rad en {T} s: {E:.8f} N^2 m^2 s (cerrada {E_ex:.8f})")
    prueba(abs(E - E_ex) < 1e-8 * E_ex, "energía mínima")
    for T2 in (10.0, 20.0, 40.0):
        print(f"   T = {T2:4.0f} s -> energía {12*J**2*D**2/T2**3:.6f}")

    # modo oculto: la salida está acotada, el estado no
    A2 = np.array([[-1.0, 0.0], [0.0, 2.0]]); B2 = np.array([[1.0], [0.0]]); C2 = np.array([[1.0, 0.0]])
    print("modo oculto: rango de controlabilidad", np.linalg.matrix_rank(ctrb(A2, B2)),
          " | polos de la transferencia 1/(s+1) = -1, polos de A =", np.linalg.eigvals(A2))
    x = np.array([[0.0], [1e-6]])
    for _ in range(100):
        x = expm(A2 * 0.1) @ x                      # sin entrada
    print(f"tras 10 s con x2(0) = 1e-6: x2 = {x[1,0]:.3e}, la salida y = x1 sigue acotada")
    prueba(abs(x[1, 0] - 1e-6 * np.exp(20)) < 1e-12 * np.exp(20), "crecimiento e^(2t)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
