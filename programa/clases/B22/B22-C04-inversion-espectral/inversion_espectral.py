#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B22-C04: inversion espectral (cuerpo negro y mezcla de temperaturas).

Datos: SINTETICOS (no son observaciones). Radiancia espectral de Planck
B(lam, T) = 2 h c^2 / lam^5 / (exp(h c / (lam k T)) - 1)   [W m^-2 sr^-1 m^-1]
con h = 6.62607015e-34 J s, c = 299792458 m/s, k = 1.380649e-23 J/K (exactas, SI).
Parte 1: un cuerpo negro de T = 25 K en 40 longitudes de onda log-espaciadas entre
30 y 1000 micras, con ruido gaussiano relativo del 2 % (semilla 4); se estima T.
Parte 2: mezcla w(T) en 15 temperaturas (10-80 K) con dos componentes (20 K y 45 K);
espectro = suma_j w_j B(lam, T_j) con ruido relativo del 1 % (semilla 5). Se invierte
w con (a) minimos cuadrados ingenuos, (b) Tikhonov, (c) minimos cuadrados no negativos.
Supuestos: emision optimamente delgada ignorada (cuerpo negro puro, sin emisividad);
ruido gaussiano multiplicativo conocido; modelo correcto.
Validez: lam 30-1000 micras, T 10-80 K (cociente h c/(lam k T) entre 0.18 y 48).
Tolerancias: ley de Wien (maximo de B) 1e-4 relativa; T recuperada sin ruido 1e-6;
Tikhonov y NNLS reducen el error respecto de la inversion ingenua.
"""
from __future__ import annotations
import platform
import numpy as np
import scipy
from scipy.optimize import least_squares, nnls, brentq

H, C, K = 6.62607015e-34, 299792458.0, 1.380649e-23


def planck(lam, T):
    x = H * C / (lam * K * T)
    return 2 * H * C ** 2 / lam ** 5 / np.expm1(x)


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__, "| scipy", scipy.__version__)

    # 0) Prueba: constante de Wien b = lam_max T calculada desde h, c, k
    #    x = 5 (1 - e^-x), x = h c / (lam_max k T)  ->  b = h c / (k x)
    x_w = brentq(lambda x: x - 5 * (1 - np.exp(-x)), 1.0, 10.0, xtol=1e-14)
    b_wien = H * C / (K * x_w)
    lam_fino = np.linspace(1e-6, 2e-4, 400001)
    lam_pico = lam_fino[np.argmax(planck(lam_fino, 30.0))]
    print(f"x de Wien = {x_w:.9f}; b = {b_wien*1e3:.9f} mm K; pico numerico a 30 K = {lam_pico*1e6:.2f} um "
          f"(Wien: {b_wien/30*1e6:.2f} um)")
    assert abs(lam_pico * 30.0 / b_wien - 1) < 1e-4

    # Parte 1: un parametro
    lam = np.logspace(np.log10(30e-6), np.log10(1000e-6), 40)
    T0 = 25.0
    s0 = planck(lam, T0)
    rng = np.random.default_rng(4)
    y = s0 * (1 + 0.02 * rng.normal(size=lam.size))
    f = lambda q: (planck(lam, q[0]) - y) / (0.02 * y)
    r_sin = least_squares(lambda q: (planck(lam, q[0]) - s0) / s0, [40.0], xtol=1e-14, ftol=1e-14)
    r = least_squares(f, [40.0])
    J = r.jac
    sT = float(np.sqrt(np.linalg.inv(J.T @ J))[0, 0])
    print(f"parte 1 sin ruido: T = {r_sin.x[0]:.8f} K (verdad {T0}); con ruido 2 %: T = {r.x[0]:.3f} +- {sT:.3f} K; "
          f"chi2/gl = {2*r.cost/(lam.size-1):.2f}")
    assert abs(r_sin.x[0] - T0) < 1e-6
    assert abs(r.x[0] - T0) < 4 * sT

    # Parte 2: mezcla de temperaturas (problema lineal mal condicionado)
    Tg = np.linspace(10.0, 80.0, 15)
    B = np.column_stack([planck(lam, T) for T in Tg])
    escala = B.max(axis=0)
    An = B / escala                       # columnas normalizadas a 1 (cada columna: unidades de su maximo)
    w_ver = np.exp(-0.5 * ((Tg - 20) / 4) ** 2) + 0.7 * np.exp(-0.5 * ((Tg - 45) / 6) ** 2)
    d0 = An @ w_ver
    rng = np.random.default_rng(5)
    sig = 0.01 * d0
    d = d0 + sig * rng.normal(size=lam.size)
    Aw, bw = An / sig[:, None], d / sig   # pesos 1/sigma
    sv = np.linalg.svd(Aw, compute_uv=False)
    print(f"parte 2: cond(A) = {sv[0]/sv[-1]:.2e}")
    # prueba: un solo T reproduce Planck exactamente
    j = 5
    assert np.allclose(B[:, j], planck(lam, Tg[j]), rtol=1e-14)
    rel = lambda w: np.linalg.norm(w - w_ver) / np.linalg.norm(w_ver)

    w_ing = np.linalg.lstsq(Aw, bw, rcond=None)[0]
    def tik(l):
        M = np.vstack([Aw, l * np.eye(15)]); r_ = np.concatenate([bw, np.zeros(15)])
        return np.linalg.lstsq(M, r_, rcond=None)[0]
    lams = np.logspace(-2, 4, 61)
    errs = np.array([rel(tik(l)) for l in lams])
    res = np.array([np.linalg.norm(Aw @ tik(l) - bw) for l in lams])
    k_dis = int(np.argmin(np.abs(res - np.sqrt(lam.size))))     # discrepancia: chi^2 = n
    w_tik = tik(lams[k_dis])
    w_nn, _ = nnls(Aw, bw)
    # NNLS + Tikhonov: Tikhonov con restriccion de no negatividad
    M = np.vstack([Aw, lams[k_dis] * np.eye(15)]); r_ = np.concatenate([bw, np.zeros(15)])
    w_tn, _ = nnls(M, r_)
    print(f"lam de discrepancia = {lams[k_dis]:.2e}")
    print(f"error relativo: ingenuo {rel(w_ing):.3e} | Tikhonov {rel(w_tik):.3e} | NNLS {rel(w_nn):.3e} | Tikhonov+NNLS {rel(w_tn):.3e}")
    print(f"minimo de w: ingenuo {w_ing.min():.2f} | Tikhonov {w_tik.min():.2f} | NNLS {w_nn.min():.2f} | T+NNLS {w_tn.min():.2f}")
    print("  T (K)   verdad   ingenuo   Tikhonov  T+NNLS")
    for i in range(15):
        print(f"  {Tg[i]:5.1f}   {w_ver[i]:6.3f}  {w_ing[i]:8.2f}  {w_tik[i]:8.3f}  {w_tn[i]:7.3f}")
    chi_ver = np.linalg.norm(Aw @ w_ver - bw) ** 2
    chi_tn = np.linalg.norm(Aw @ w_tn - bw) ** 2
    print(f"chi2 con la verdad = {chi_ver:.1f}; chi2 de Tikhonov+NNLS = {chi_tn:.1f}; datos = {lam.size}")
    assert rel(w_tik) < 0.5 * rel(w_ing)
    assert w_nn.min() >= 0 and w_tn.min() >= 0
    assert rel(w_tn) < rel(w_ing)
    # Error de modelo: ajustar UN solo cuerpo negro a la mezcla de dos temperaturas
    def un_cuerpo(q):
        Tq = q[1]
        return (q[0] * planck(lam, Tq) / planck(lam, Tq).max() - d) / sig
    r1 = least_squares(un_cuerpo, [1.0, 30.0], bounds=([0, 5], [10, 100]))
    chi1 = 2 * r1.cost / (lam.size - 2)
    print(f"un solo T ajustado a la mezcla: T = {r1.x[1]:.2f} K, chi2/gl = {chi1:.1f} (modelo incorrecto)")
    assert chi1 > 5.0                     # el desajuste delata el error de modelo
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
