#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C08: apoyo axial del espejo primario: disco apoyado en un anillo, metodo de Ritz y flexion residual tras enfocar.

Datos: ILUSTRATIVOS (disco de borosilicato de a = 100 mm, t = 33,3 mm, E = 63 GPa, rho = 2230 kg/m^3, nu = 0,20; g = 9,80665 m/s^2 de NIST CODATA 2022, consultada el 2026-11-09). Propiedades de orden de magnitud, no consultadas.
Modelo: placa delgada axisimetrica bajo peso propio uniforme, borde libre, apoyada en un anillo de radio b. Energia de Kirchhoff minimizada con base polinomica w = sum c_k rho^(2k) (k = 0..9) y la restriccion w(b) = 0 por multiplicador de Lagrange (sistema KKT resuelto por Gauss).
Adimensional: w en unidades de q a^4/D_f. La flexion util es la que queda tras quitar piston y desenfoque (ajuste por minimos cuadrados con 1 y rho^2, ponderado por area).
Verificacion independiente: para b = a (apoyo en el borde) la flecha centro-borde debe ser (5+nu)/(1+nu)/64 (solucion cerrada de C03).
Supuestos: Kirchhoff (t << a), apoyo ideal sin friccion, sin cortante transversal. Validez: cualitativa para t/a = 1/3.
Tolerancia: Ritz frente a solucion cerrada, 1e-5 relativo.
"""
from __future__ import annotations
import math, platform

G = 9.80665
E = 63e9; RHO = 2230.0; NU = 0.20; A = 0.100; T = 0.200 / 6
K = 10

def rigidez(nu):
    M = [[0.0] * K for _ in range(K)]
    for k in range(1, K):
        for l in range(1, K):
            s = k + l
            if s < 2:
                continue
            ek = 2 * k * (2 * k - 1); el = 2 * l * (2 * l - 1)
            coef = ek * el + 2 * k * 2 * l + nu * (ek * 2 * l + el * 2 * k)
            M[k][l] = coef / (2 * s - 2)
    return M

def gauss(Am, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(Am)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x

def resolver(beta, nu=NU):
    Km = rigidez(nu)
    n = K + 1
    Am = [[0.0] * n for _ in range(n)]
    for i in range(K):
        for j in range(K):
            Am[i][j] = Km[i][j]
        Am[i][K] = beta ** (2 * i); Am[K][i] = beta ** (2 * i)
    b = [1.0 / (2 * k + 2) for k in range(K)] + [0.0]
    x = gauss(Am, b)
    return x[:K]

def w(c, rho):
    return sum(ck * rho ** (2 * k) for k, ck in enumerate(c))

def residual_rms(c, n=400):
    # ajuste ponderado por area a a + b rho^2 y RMS del resto
    s = [(i + 0.5) / n for i in range(n)]
    W = [x for x in s]  # peso rho
    ws = [w(c, x) for x in s]
    S = lambda f: sum(W[i] * f(i) for i in range(n))
    s0 = S(lambda i: 1); s2 = S(lambda i: s[i] ** 2); s4 = S(lambda i: s[i] ** 4)
    t0 = S(lambda i: ws[i]); t2 = S(lambda i: ws[i] * s[i] ** 2)
    det = s0 * s4 - s2 * s2
    a0 = (t0 * s4 - t2 * s2) / det; a2 = (s0 * t2 - s2 * t0) / det
    res = [ws[i] - a0 - a2 * s[i] ** 2 for i in range(n)]
    m = S(lambda i: res[i]) / s0
    var = S(lambda i: (res[i] - m) ** 2) / s0
    pv = max(res) - min(res)
    return math.sqrt(var), pv

def calc():
    r = {}
    c = resolver(1.0)
    r["centro_borde_ritz"] = w(c, 0.0) - w(c, 1.0)
    r["centro_borde_cerrado"] = (5 + NU) / (1 + NU) / 64
    Df = E * T ** 3 / (12 * (1 - NU ** 2)); q = RHO * G * T
    esc = q * A ** 4 / Df * 1e9
    r["escala_nm"] = esc
    tabla = []
    best = None
    for i in range(0, 91):
        beta = 0.30 + 0.01 * i if False else 0.30 + 0.0075 * i
        if beta > 0.99:
            break
        cb = resolver(beta)
        rms, pv = residual_rms(cb)
        tabla.append((beta, rms * esc, pv * esc))
        if best is None or rms < best[1]:
            best = (beta, rms, pv)
    r["tabla"] = [x for x in tabla if abs(round((x[0] - 0.30) / 0.075) - (x[0] - 0.30) / 0.075) < 1e-9 and round((x[0] - 0.30) / 0.075) % 1 == 0 and round((x[0] - 0.30) / 0.0075) % 10 == 0]
    r["beta_opt"] = best[0]; r["rms_opt_nm"] = best[1] * esc; r["pv_opt_nm"] = best[2] * esc
    cb1 = resolver(0.99)
    r["rms_borde_nm"] = residual_rms(resolver(0.9999))[0] * esc
    r["lambda_14_nm"] = 550.0 / 14
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k in ("centro_borde_ritz", "centro_borde_cerrado", "escala_nm", "beta_opt", "rms_opt_nm", "pv_opt_nm", "rms_borde_nm"):
        print(f"{k} = {r[k]:.6g}")
    print("b/a | RMS residual (nm) | PV (nm)")
    for b, rm, pv in r["tabla"]:
        print(f"{b:.3f} | {rm:.4f} | {pv:.4f}")
    assert abs(r["centro_borde_ritz"] - r["centro_borde_cerrado"]) / r["centro_borde_cerrado"] < 1e-5
    assert 0.5 < r["beta_opt"] < 0.9
    assert r["rms_opt_nm"] < r["rms_borde_nm"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
