#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C08: masa termica, radios de Bondi y de Hill y tiempo de crecimiento de un nucleo por captura de guijarros.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol y (GM)_Tierra nominales de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): a = 5 ua; disco de B52-C02 (T = 280 K (r/ua)^-0.5, mu = 2.3); densidad superficial de guijarros 1 kg/m^2;
nucleo objetivo de 10 masas terrestres (orden de magnitud citado en el resumen de Lambrechts y Johansen 2012, consultado solo como resumen).
La tasa de acrecion de guijarros en regimen de Hill, dM/dt = 2 R_H^2 Omega Sigma_peb, es un modelo de ensenanza: su forma NO se consulto.
Sistema de referencia: orbita circular a 5 ua; SI.
Masa termica M_th = h^3 M* = cs^3/(G Omega). R_B = G M/cs^2 ; R_H = a (M/(3M*))^(1/3). R_B = R_H en M_th/sqrt(3) (cierre) frente a biseccion.
Tiempo: M^(1/3) lineal en t (analitico) frente a RK4. Tolerancias: M_th/sqrt(3) 1e-9; tiempo 1e-6.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
GM_T = 3.986004e14
MSOL, MT = GM / G, GM_T / G
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
MU, T1 = 2.3, 280.0
A = 5.0 * UA
T = T1 * 5.0 ** -0.5
CS = math.sqrt(K_B * T / (MU * M_P))
OM = math.sqrt(GM / A ** 3)
H_R = CS / OM / A
SIG_PEB = 1.0
M_NUCLEO = 10.0 * MT


def r_bondi(m): return G * m / CS ** 2
def r_hill(m): return A * (m / (3.0 * MSOL)) ** (1.0 / 3.0)


def masa_igual():
    f = lambda m: r_bondi(m) - r_hill(m)
    a, b = 1e22, 1e30
    for _ in range(300):
        c = math.sqrt(a * b)
        if f(c) < 0: a = c
        else: b = c
    return math.sqrt(a * b)


def tasa(m): return 2.0 * r_hill(m) ** 2 * OM * SIG_PEB


def tiempo_rk4(m0, m1):
    m, t = m0, 0.0
    while m < m1:
        h = 1e-3 * m / tasa(m)
        k1 = tasa(m); k2 = tasa(m + 0.5 * h * k1); k3 = tasa(m + 0.5 * h * k2); k4 = tasa(m + h * k3)
        mn = m + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if mn >= m1:
            t += h * (m1 - m) / (mn - m)
            break
        m, t = mn, t + h
    return t


def calcular():
    mth = H_R ** 3 * MSOL
    mth2 = CS ** 3 / (G * OM)
    meq_cerrado = mth / math.sqrt(3.0)
    meq_num = masa_igual()
    filas = []
    for mt in (1.0, 10.0, 100.0, 1000.0):
        m = mt * MT
        filas.append((mt, r_bondi(m), r_hill(m), min(r_bondi(m), r_hill(m)), "Bondi" if r_bondi(m) < r_hill(m) else "Hill"))
    m0 = 0.01 * MT
    B = 2.0 * A ** 2 * (3.0 * MSOL) ** (-2.0 / 3.0) * OM * SIG_PEB
    t_an = 3.0 * (M_NUCLEO ** (1 / 3) - m0 ** (1 / 3)) / B
    t_num = tiempo_rk4(m0, M_NUCLEO)
    return dict(mth=mth, mth2=mth2, meq_c=meq_cerrado, meq_n=meq_num, filas=filas, t_an=t_an, t_num=t_num, h=H_R, cs=CS, om=OM, B=B)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Disco sintetico a 5 ua: T = {T:.1f} K ; c_s = {r['cs']:.1f} m/s ; h = {r['h']:.4f} ; Omega = {r['om']:.4e} s^-1")
    print(f"Masa termica M_th = h^3 M* = {r['mth'] / MT:.2f} M_Tierra (otra via cs^3/(G Omega): {r['mth2'] / MT:.2f})")
    print(f"R_B = R_H en M = {r['meq_n'] / MT:.3f} M_Tierra (biseccion) ; M_th/sqrt(3) = {r['meq_c'] / MT:.3f} M_Tierra")
    print(f"{'m [M_T]':>8} {'R_B [km]':>12} {'R_H [km]':>12} {'radio de captura [km]':>22} {'limita':>7}")
    for mt, rb, rh, rc, lim in r["filas"]:
        print(f"{mt:8.0f} {rb / 1e3:12.4e} {rh / 1e3:12.4e} {rc / 1e3:22.4e} {lim:>7}")
    print(f"Guijarros (Sigma = {SIG_PEB} kg/m^2, regimen de Hill): 0.01 -> 10 M_T en analitico = {r['t_an'] / ANIO:.4e} anios ; RK4 = {r['t_num'] / ANIO:.4e} anios ; dif. rel. = {abs(r['t_num'] / r['t_an'] - 1):.1e}")
    assert abs(r["mth"] / r["mth2"] - 1) < 1e-9
    assert abs(r["meq_n"] / r["meq_c"] - 1) < 1e-9
    assert abs(r["t_num"] / r["t_an"] - 1) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
