#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C02: niveles de energia por diferencias finitas, oscilador armonico, hidrogeno y efecto tunel.

Datos: h, e, m_e, epsilon_0, c y la energia de Rydberg R_inf h c = 13.605693122990 eV (NIST CODATA 2022), consultados 2026-11-09. El ancho del pozo (1 nm), la frecuencia del oscilador
(1e15 rad/s), y la barrera (V_0 = 2 eV, ancho 0.5 nm, E = 1 eV) son ILUSTRATIVOS (sinteticos).
Modelo: pozo infinito de ancho L: H discretizado en N puntos interiores (matriz tridiagonal); n-esimo autovalor por biseccion con la sucesion de Sturm y comparacion con
E_n = n^2 pi^2 hbar^2/(2 m L^2); oscilador armonico en unidades m = hbar = omega = 1 (autovalores n + 1/2) y conversion a eV; energia del estado fundamental del hidrogeno
-m e^4/(8 epsilon_0^2 h^2) frente a la energia de Rydberg de NIST; transmision a traves de una barrera rectangular por la formula analitica y por integracion numerica RK4 de la ecuacion
de Schrodinger (aritmetica compleja).
Supuestos: masa constante, potenciales estacionarios, 1D. Validez: estados ligados bajos.
Tolerancia: autovalores del pozo a 1e-4 relativo; oscilador a 1e-4; Rydberg a 1e-9; transmision numerica frente a la analitica a 1e-6.
"""
from __future__ import annotations
import cmath
import math
import platform
import sys

H, E, ME, EPS0, C = 6.62607015e-34, 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12, 299792458.0
HBAR = H / (2 * math.pi)
RYD_EV = 13.605693122990


def autovalor(diag, off, k):
    """k-esimo autovalor (k = 0 el menor) de una matriz tridiagonal simetrica por biseccion de Sturm."""
    n = len(diag)
    lo = min(diag[i] - 2 * abs(off) for i in range(n))
    hi = max(diag[i] + 2 * abs(off) for i in range(n))

    def menores(x):
        cnt, q = 0, diag[0] - x
        if q < 0:
            cnt += 1
        for i in range(1, n):
            q = diag[i] - x - off * off / (q if q != 0 else 1e-300)
            if q < 0:
                cnt += 1
        return cnt
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if menores(mid) > k:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def transmision_numerica(e_ev, v0_ev, a, kp=None):
    k = math.sqrt(2 * ME * e_ev * E) / HBAR
    q = cmath.sqrt(2 * ME * (e_ev - v0_ev) * E + 0j) / HBAR     # imaginario dentro de la barrera
    # integra psi'' = -(k(x))^2 psi desde la derecha: psi = exp(i k x) a x = a con psi' = i k psi
    n = 20000
    h = a / n
    psi, dpsi = cmath.exp(1j * k * a), 1j * k * cmath.exp(1j * k * a)
    k2 = q * q
    for _ in range(n):
        f = lambda p, d: (d, -k2 * p)
        a1 = f(psi, dpsi)
        a2 = f(psi - 0.5 * h * a1[0], dpsi - 0.5 * h * a1[1])
        a3 = f(psi - 0.5 * h * a2[0], dpsi - 0.5 * h * a2[1])
        a4 = f(psi - h * a3[0], dpsi - h * a3[1])
        psi -= h * (a1[0] + 2 * a2[0] + 2 * a3[0] + a4[0]) / 6
        dpsi -= h * (a1[1] + 2 * a2[1] + 2 * a3[1] + a4[1]) / 6
    # a x = 0: psi = A e^{ikx} + B e^{-ikx}
    amp_a = 0.5 * (psi + dpsi / (1j * k))
    t_ana_den = abs(amp_a) ** 2
    return 1.0 / t_ana_den


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # pozo infinito
    big_l, n = 1e-9, 1500
    hh = big_l / (n + 1)
    t = HBAR ** 2 / (2 * ME * hh * hh)
    diag, off = [2 * t] * n, -t
    print(f"{'n':>2} {'E_n numerico [eV]':>18} {'E_n analitico [eV]':>19} {'dif. relativa':>14}")
    for k in range(5):
        num = autovalor(diag, off, k) / E
        ana = (k + 1) ** 2 * math.pi ** 2 * HBAR ** 2 / (2 * ME * big_l ** 2) / E
        print(f"{k + 1:2d} {num:18.6f} {ana:19.6f} {abs(num / ana - 1):14.2e}")
        assert abs(num / ana - 1) < 1e-4, f"pozo n={k + 1}"
    # oscilador armonico en unidades naturales
    nx, xm = 1500, 9.0
    dx = 2 * xm / (nx + 1)
    diag = [1 / dx ** 2 + 0.5 * (-xm + (i + 1) * dx) ** 2 for i in range(nx)]
    off = -0.5 / dx ** 2
    omega = 1e15
    print(f"{'n':>2} {'E_n numerico':>13} {'n + 1/2':>8} {'hbar omega [eV] (omega = 1e15 rad/s)':>38}")
    for k in range(5):
        num = autovalor(diag, off, k)
        print(f"{k:2d} {num:13.6f} {k + 0.5:8.1f} {(k + 0.5) * HBAR * omega / E:38.6f}")
        assert abs(num / (k + 0.5) - 1) < 1e-4, f"oscilador n={k}"
    # hidrogeno
    e1 = ME * E ** 4 / (8 * EPS0 ** 2 * H ** 2) / E
    print(f"estado fundamental del hidrogeno (masa del electron, nucleo fijo): {e1:.9f} eV ; energia de Rydberg de NIST = {RYD_EV:.9f} eV ; cociente = {e1 / RYD_EV:.10f}")
    assert abs(e1 / RYD_EV - 1) < 1e-9
    # tunel
    e_ev, v0, a = 1.0, 2.0, 0.5e-9
    k = math.sqrt(2 * ME * e_ev * E) / HBAR
    kap = math.sqrt(2 * ME * (v0 - e_ev) * E) / HBAR
    t_ana = 1.0 / (1 + (v0 ** 2 * math.sinh(kap * a) ** 2) / (4 * e_ev * (v0 - e_ev)))
    t_num = transmision_numerica(e_ev, v0, a)
    print(f"barrera de {v0} eV y {a * 1e9} nm con E = {e_ev} eV: kappa a = {kap * a:.4f} ; T analitica = {t_ana:.6e} ; T numerica (RK4) = {t_num:.6e} ; cociente = {t_num / t_ana:.8f}")
    assert abs(t_num / t_ana - 1) < 1e-6, "transmision"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
