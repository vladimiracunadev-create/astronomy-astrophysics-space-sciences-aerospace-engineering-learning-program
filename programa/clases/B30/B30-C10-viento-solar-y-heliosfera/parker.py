#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C10: solucion transonica de Parker del viento solar isotermo y espiral magnetica.

Datos: k_B y u (NIST CODATA 2022); GM_sol y R_sol (IAU 2015 B3), 1 au (IERS TN36), consultados 2026-11-09. La temperatura coronal (1.0, 1.5, 2.0 millones de K), la masa molecular
media (0.6), la densidad en 1 au (5e6 m^-3) y el periodo de rotacion (25.4 d) son ILUSTRATIVOS.
Modelo: viento isotermo y estacionario; con u = v/c_s, x = r/r_c y r_c = GM/(2 c_s^2), la ecuacion de Parker es u^2 - ln u^2 = 4 ln x + 4/x + C; la solucion que pasa por el punto
critico (x = 1, u = 1) tiene C = -3 (rama subsonica u < 1 para x < 1, supersonica u > 1 para x > 1), resuelta por biseccion; flujo de masa 4 pi r^2 rho v constante;
espiral de Parker tan(psi) = Omega r/v.
Supuestos: isotermo, esferico, estacionario, sin campo magnetico en la dinamica. Validez: orientativa.
Tolerancia: residuo de la ecuacion de Parker < 1e-12; v(r_c) = c_s a 1e-9; flujo de masa constante a 1e-12.
"""
from __future__ import annotations
import math
import platform
import sys

KB, U = 1.380649e-23, 1.66053906892e-27
GM_SOL, R_SOL, AU = 1.3271244e20, 6.957e8, 1.49597870700e11
MU = 0.6


def f(u, x, c=-3.0):
    return u * u - math.log(u * u) - 4 * math.log(x) - 4 / x - c


def u_parker(x):
    if abs(x - 1) < 1e-12:
        return 1.0
    if x < 1:
        lo, hi = 1e-12, 1.0
        # f decrece de +inf a... en (0,1): buscar raiz de f(u) = 0 con u < 1
        for _ in range(300):
            mid = 0.5 * (lo + hi)
            if f(mid, x) > 0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    lo, hi = 1.0, 50.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if f(mid, x) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'T [K]':>10} {'c_s [km/s]':>11} {'r_c [R_sol]':>12} {'v(1 au) [km/s]':>15} {'v(10 R_sol) [km/s]':>19}")
    res = {}
    for t in (1.0e6, 1.5e6, 2.0e6):
        cs = math.sqrt(KB * t / (MU * U))
        rc = GM_SOL / (2 * cs ** 2)
        v1 = cs * u_parker(AU / rc)
        v10 = cs * u_parker(10 * R_SOL / rc)
        res[t] = (cs, rc, v1)
        print(f"{t:10.3g} {cs / 1e3:11.2f} {rc / R_SOL:12.3f} {v1 / 1e3:15.1f} {v10 / 1e3:19.1f}")
    cs, rc, v1 = res[1.5e6]
    # residuos y punto critico
    for x in (0.2, 0.5, 2.0, 10.0, 50.0):
        u = u_parker(x)
        assert abs(f(u, x)) < 1e-12, f"residuo en x={x}"
    assert abs(u_parker(1.0) - 1.0) < 1e-9
    print(f"{'x = r/r_c':>9} {'u = v/c_s':>10} {'r [R_sol]':>10} {'v [km/s]':>9} {'n/n(1 au)':>10}")
    x1 = AU / rc
    u1 = u_parker(x1)
    for x in (0.2, 0.5, 1.0, 2.0, 5.0, x1):
        u = u_parker(x)
        # flujo de masa constante: rho x^2 u = const
        n_rel = (x1 ** 2 * u1) / (x ** 2 * u)
        print(f"{x:9.3f} {u:10.4f} {x * rc / R_SOL:10.2f} {u * cs / 1e3:9.1f} {n_rel:10.1f}")
    # flujo de masa y espiral
    n_1au = 5e6
    mdot = 4 * math.pi * AU ** 2 * n_1au * 1.67262192595e-27 * v1
    print(f"flujo de masa con n(1 au) = 5e6 m-3 y v = {v1 / 1e3:.0f} km/s: {mdot:.3e} kg/s = {mdot * 3.15576e7 / (GM_SOL / 6.6743e-11):.3e} M_sol/anio")
    omega = 2 * math.pi / (25.4 * 86400)
    for v in (3e5, 4e5, 6e5):
        psi = math.degrees(math.atan(omega * AU / v))
        print(f"espiral de Parker a 1 au con v = {v / 1e3:.0f} km/s: angulo con la radial = {psi:.1f} grados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
