#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C16: radio de marea, masa de Hills y tasa de retorno de masa de un evento de disrupcion por marea.

Datos: G, c (NIST CODATA 2022), GM_sol y R_sol nominal 6.957e8 m (IAU 2015 B3), 1 au (IERS TN36), consultados 2026-11-09.
Numero de eventos observados: 56 (Gezari, arXiv:2104.14580, resumen). Estrella de tipo solar y agujero de 1e6 Msol:
valores ILUSTRATIVOS (sinteticos).
Modelo: r_t = R_* (M/m_*)^(1/3). Masa de Hills: r_t = r_s = 2GM/c^2 => M_H = (R_* c^2/(2G))^(3/2) m_*^(-1/2).
Dispersion de energia del residuo: DeltaE = G M R_*/r_t^2; retorno del residuo mas ligado: t_min = 2 pi G M/(2 DeltaE)^(3/2);
con dM/dE uniforme, dM/dt = (m_*/(2 DeltaE)) |dE/dt| con E(t) = -(1/2)(2 pi G M/t)^(2/3) => dM/dt proporcional a t^(-5/3).
Supuestos: estrella intacta hasta r_t, distribucion de energia plana, orbitas keplerianas. Validez: orientativa.
Tolerancia: 1e-9 entre la masa de Hills por biseccion y por formula; 1e-6 entre la pendiente numerica y -5/3.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
M_SOL = GM_SOL / G
AU = 1.49597870700e11


def r_marea(r_star, m_bh, m_star):
    return r_star * (m_bh / m_star) ** (1 / 3)


def masa_hills_bisec(r_star, m_star):
    lo, hi = 1e3 * M_SOL, 1e12 * M_SOL
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if r_marea(r_star, mid, m_star) > 2 * G * mid / C ** 2:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def retorno(t, m_bh, m_star, r_star):
    """Masa devuelta hasta t (con dM/dE uniforme)."""
    rt = r_marea(r_star, m_bh, m_star)
    de = G * m_bh * r_star / rt ** 2
    e_t = 0.5 * (2 * math.pi * G * m_bh / t) ** (2 / 3)
    return m_star / (2 * de) * (de - e_t) if e_t <= de else 0.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ms, rs_ = M_SOL, R_SOL
    mh_f = (rs_ * C ** 2 / (2 * G)) ** 1.5 * ms ** -0.5
    mh_b = masa_hills_bisec(rs_, ms)
    assert abs(mh_b / mh_f - 1) < 1e-9, "masa de Hills"
    print(f"masa de Hills (estrella de 1 Msol, 1 Rsol) = {mh_f / M_SOL:.4e} Msol (biseccion {mh_b / M_SOL:.4e})")
    print(f"{'M_BH [Msol]':>12} {'r_t [au]':>10} {'r_t/r_s':>9} {'t_min [d]':>10}")
    for mbh in (1e5, 1e6, 1e7, 1e8):
        m = mbh * M_SOL
        rt = r_marea(rs_, m, ms)
        de = G * m * rs_ / rt ** 2
        tmin = 2 * math.pi * G * m / (2 * de) ** 1.5 / 86400
        print(f"{mbh:12.0e} {rt / AU:10.4f} {rt / (2 * G * m / C ** 2):9.2f} {tmin:10.2f}")
    m = 1e6 * M_SOL
    rt = r_marea(rs_, m, ms)
    de = G * m * rs_ / rt ** 2
    tmin = 2 * math.pi * G * m / (2 * de) ** 1.5
    print(f"M = 1e6 Msol: DeltaE = {de:.4e} J/kg ; t_min = {tmin / 86400:.2f} d")
    # pendiente de la tasa de retorno
    for fac in (10.0, 100.0):
        t = fac * tmin
        h = 1e-4 * t
        r1 = (retorno(t + h, m, ms, rs_) - retorno(t - h, m, ms, rs_)) / (2 * h)
        r2 = (retorno(t * 1.01 + h, m, ms, rs_) - retorno(t * 1.01 - h, m, ms, rs_)) / (2 * h)
        pend = math.log(r2 / r1) / math.log(1.01)
        assert abs(pend + 5 / 3) < 1e-4, "pendiente -5/3"
        print(f"t = {fac:5.0f} t_min: tasa = {r1 / ms * 86400:.4e} Msol_estrella/dia ; pendiente = {pend:.6f} (-5/3 = {-5 / 3:.6f})")
    mret = retorno(1e9 * tmin, m, ms, rs_) / ms
    print(f"fraccion de la masa estelar devuelta cuando e_t -> 0: {mret:.4f} (esperada 0.5 de la estrella: la mitad ligada)")
    assert abs(mret - 0.5) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
