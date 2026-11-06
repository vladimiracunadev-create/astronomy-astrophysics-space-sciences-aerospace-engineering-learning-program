#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B22-C02: regularizacion de Tikhonov y curva L.

Datos: SINTETICOS (no son observaciones). Mismo problema que B22-C01: perfil de
brillo x(s) en n = 40 puntos, nucleo gaussiano w = 0.05, ruido gaussiano
sigma = 1e-3 (semilla fija 22).
Modelo: x_lam = argmin ||A x - b||^2 + lam^2 ||x||^2 (forma estandar, L = I, x0 = 0).
Tres calculos equivalentes: ecuaciones normales, minimos cuadrados aumentados
y filtro SVD con f_i = s_i^2 / (s_i^2 + lam^2).
Supuestos: ruido blanco de sigma conocida (solo para el principio de discrepancia);
la verdad solo se conoce porque el dato es sintetico.
Validez: n = 40; el lam optimo depende de ruido, nucleo y solucion.
Tolerancias: equivalencia de los tres metodos 1e-8 (relativa); caso escalar
analitico x = s b / (s^2 + lam^2) a 1e-14.
"""
from __future__ import annotations
import platform
import numpy as np


def construir(n=40, w=0.05):
    s = np.linspace(0.0, 1.0, n)
    h = 1.0 / (n - 1)
    A = h * np.exp(-((s[:, None] - s[None, :]) ** 2) / (2 * w ** 2)) / (w * np.sqrt(2 * np.pi))
    x = np.exp(-((s - 0.3) ** 2) / (2 * 0.04 ** 2)) + 0.6 * np.exp(-((s - 0.7) ** 2) / (2 * 0.06 ** 2))
    return s, A, x


def tikhonov_normales(A, b, lam):
    return np.linalg.solve(A.T @ A + lam ** 2 * np.eye(A.shape[1]), A.T @ b)


def tikhonov_aumentado(A, b, lam):
    n = A.shape[1]
    M = np.vstack([A, lam * np.eye(n)])
    r = np.concatenate([b, np.zeros(n)])
    return np.linalg.lstsq(M, r, rcond=None)[0]


def tikhonov_svd(U, sv, Vt, b, lam):
    f = sv ** 2 / (sv ** 2 + lam ** 2)
    return Vt.T @ (f * (U.T @ b) / sv)


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    s, A, x_ver = construir()
    n, sigma = len(s), 1e-3
    rng = np.random.default_rng(22)
    b = A @ x_ver + rng.normal(0.0, sigma, size=n)
    U, sv, Vt = np.linalg.svd(A)
    rel = lambda a: np.linalg.norm(a - x_ver) / np.linalg.norm(x_ver)

    # 1) Caso escalar analitico
    a_, b_, l_ = 0.5, 2.0, 0.3
    x_esc = tikhonov_normales(np.array([[a_]]), np.array([b_]), l_)[0]
    assert abs(x_esc - a_ * b_ / (a_ ** 2 + l_ ** 2)) < 1e-14
    print("escalar: x_lam =", x_esc, "= s b/(s^2+lam^2) =", a_ * b_ / (a_ ** 2 + l_ ** 2))

    # 2) Equivalencia de los tres metodos
    lam0 = 1e-3
    x1, x2, x3 = tikhonov_normales(A, b, lam0), tikhonov_aumentado(A, b, lam0), tikhonov_svd(U, sv, Vt, b, lam0)
    d12 = np.linalg.norm(x1 - x2) / np.linalg.norm(x2)
    d23 = np.linalg.norm(x3 - x2) / np.linalg.norm(x2)
    print(f"lam = {lam0:g}: dif. normales-aumentado = {d12:.2e}; SVD-aumentado = {d23:.2e}")
    assert d12 < 1e-8 and d23 < 1e-8

    # 3) lam -> 0 recupera la solucion ingenua; lam grande -> x -> 0
    x_ing = np.linalg.solve(A, b)
    assert np.linalg.norm(tikhonov_svd(U, sv, Vt, b, 1e-14) - x_ing) / np.linalg.norm(x_ing) < 1e-6
    assert np.linalg.norm(tikhonov_svd(U, sv, Vt, b, 1e3)) < 1e-5

    # 4) Curva L y eleccion de lam
    lams = np.logspace(-6, 0, 61)
    res = np.array([np.linalg.norm(A @ tikhonov_svd(U, sv, Vt, b, l) - b) for l in lams])
    sol = np.array([np.linalg.norm(tikhonov_svd(U, sv, Vt, b, l)) for l in lams])
    err = np.array([rel(tikhonov_svd(U, sv, Vt, b, l)) for l in lams])
    xi, eta = np.log10(res), np.log10(sol)
    d1x, d1y = np.gradient(xi), np.gradient(eta)
    d2x, d2y = np.gradient(d1x), np.gradient(d1y)
    curv = (d1x * d2y - d2x * d1y) / (d1x ** 2 + d1y ** 2) ** 1.5
    # el vertice es el maximo de curvatura con signo (curva convexa); se evita el borde
    k = 3 + int(np.argmax(np.abs(curv[3:-3])))
    lam_L = lams[k]
    k_opt = int(np.argmin(err))
    # principio de discrepancia: ||A x - b|| = sigma sqrt(n)
    k_dis = int(np.argmin(np.abs(res - sigma * np.sqrt(n))))
    print("  lam         ||Ax-b||     ||x||     error rel. (vs verdad)")
    for kk in range(0, len(lams), 6):
        print(f"  {lams[kk]:.1e}   {res[kk]:.3e}   {sol[kk]:.3e}   {err[kk]:.3e}")
    print(f"lam de la curva L (vertice)  = {lam_L:.2e} -> error {err[k]:.3e}")
    print(f"lam optimo (conoce la verdad)= {lams[k_opt]:.2e} -> error {err[k_opt]:.3e}")
    print(f"lam por discrepancia         = {lams[k_dis]:.2e} -> error {err[k_dis]:.3e}")
    print(f"solucion ingenua (lam = 0)   -> error {rel(x_ing):.3e}")
    assert err[k] < 1e-2 * rel(x_ing)                # mucho mejor que la ingenua
    assert err[k] < 10 * err[k_opt]                  # el vertice queda cerca (aqui ~5 veces el optimo)
    assert err[k_dis] < 5 * err[k_opt]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
