#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C11: curva de rotacion en MOND frente a un halo de materia oscura (NFW) y relacion de Tully-Fisher barionica.

Datos: G (NIST CODATA 2022, tabla allascii consultada 2026-11-09), GM_sol nominal (UAI 2015 B3, consultada 2026-11-09) y 1 au exacto (IERS TN36) para el kpc.
Consultado el 2026-11-09 solo el RESUMEN de Famaey y McGaugh (arXiv:1112.3960: MOND, ley de Milgrom con una constante de aceleracion, extensiones relativistas) y el RESUMEN de
Clowe et al. 2006 (arXiv:astro-ph/0608407: desplazamiento de 8 sigma). La constante a_0 = 1,2e-10 m/s^2 es el valor convencional NO consultado aqui; la funcion de interpolacion
«simple» y las galaxias (masas 5e10, 1e10 y 2e9 Msun, escala del disco 3, 2 y 1 kpc) son ILUSTRATIVAS. No se ajusta ninguna galaxia real.
Modelo: g = g_N/2 [1 + sqrt(1 + 4 a_0/g_N)] (equivale a mu(x) = x/(1+x)); v^2 = g r. Masa encerrada del disco exponencial en aproximacion ESFERICA: M(<r) = M [1 - (1 + r/R_d) exp(-r/R_d)].
Halo NFW: v^2 = 4 pi G rho_s r_s^3 [ln(1+x) - x/(1+x)]/r, x = r/r_s, ajustado por rejilla de minimos cuadrados a la curva MOND.
Segunda via: la ecuacion mu(g/a_0) g = g_N se comprueba por sustitucion; v^4 = G M a_0 a gran radio y en el limite profundo.
Supuestos: simetria esferica, sin gas ni bulbo, sin la fuerza externa. Validez: pedagogica; la conclusion NO es que MOND o la materia oscura sea correcta.
Tolerancia: sustitucion a 1e-12; v_plana frente a (G M a_0)^(1/4) dentro del 1 % a 500 kpc.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
GMSUN = 1.3271244e20
MSUN = GMSUN / G
AU = 149597870700.0
KPC = AU * 648000 / math.pi * 1e3
A0 = 1.2e-10


def g_mond(gn):
    return 0.5 * gn * (1 + math.sqrt(1 + 4 * A0 / gn))


def mu(x):
    return x / (1 + x)


def menc(r, m, rd):
    return m * (1 - (1 + r / rd) * math.exp(-r / rd))


def v_newton(r_kpc, m, rd):
    r = r_kpc * KPC
    return math.sqrt(G * menc(r_kpc, m, rd) * MSUN / r)


def v_mond(r_kpc, m, rd):
    r = r_kpc * KPC
    gn = G * menc(r_kpc, m, rd) * MSUN / r ** 2
    return math.sqrt(g_mond(gn) * r)


def v_nfw(r_kpc, rho_s, rs_kpc):
    r = r_kpc * KPC
    rs = rs_kpc * KPC
    x = r / rs
    return math.sqrt(4 * math.pi * G * rho_s * rs ** 3 * (math.log(1 + x) - x / (1 + x)) / r)


def ajusta_nfw(rr, vm):
    best = None
    for irs in range(0, 60):
        rs = 1.0 * (1.0 + irs * 0.5)  # 1 .. 30 kpc
        for irho in range(0, 400):
            rho = 1e-23 * 10 ** (irho * 0.01)  # kg/m3
            chi = sum((v_nfw(r, rho, rs) - v) ** 2 for r, v in zip(rr, vm))
            if best is None or chi < best[0]:
                best = (chi, rho, rs)
    return best


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) sustitucion
    errs = []
    for gn in (1e-13, 1e-11, 1e-10, 1e-9, 1e-7):
        g = g_mond(gn)
        errs.append(abs(mu(g / A0) * g - gn) / gn)
    print(f"comprobacion mu(g/a0) g = g_N: error relativo maximo = {max(errs):.1e}")
    # 2) galaxia principal
    m, rd = 5e10, 3.0
    rr = [2.0 + 2.0 * i for i in range(15)]  # 2..30 kpc
    vm = [v_mond(r, m, rd) for r in rr]
    vn = [v_newton(r, m, rd) for r in rr]
    print(f"{'r [kpc]':>8} {'v Newton':>9} {'v MOND':>8} {'g_N/a0':>8}")
    for r, a, b in zip(rr, vn, vm):
        if r in (2.0, 6.0, 10.0, 20.0, 30.0):
            gn = G * menc(r, m, rd) * MSUN / (r * KPC) ** 2
            print(f"{r:8.1f} {a / 1e3:9.1f} {b / 1e3:8.1f} {gn / A0:8.3f}")
    # 3) velocidad plana y Tully-Fisher
    print(f"{'M_b [Msun]':>11} {'v(500 kpc) [km/s]':>18} {'(G M a0)^1/4':>13} {'dif.':>8}")
    tf = []
    for mm, dd in ((5e10, 3.0), (1e10, 2.0), (2e9, 1.0)):
        v = v_mond(500.0, mm, dd)
        vt = (G * mm * MSUN * A0) ** 0.25
        tf.append(abs(v - vt) / vt)
        print(f"{mm:11.1e} {v / 1e3:18.2f} {vt / 1e3:13.2f} {abs(v - vt) / vt:8.4f}")
    # 4) NFW ajustado a la curva MOND
    chi, rho, rs = ajusta_nfw(rr, vm)
    rms = math.sqrt(chi / len(rr))
    m200 = 4 * math.pi * rho * (rs * KPC) ** 3 * (math.log(1 + 10) - 10 / 11) / MSUN  # masa dentro de 10 r_s, solo como escala
    print(f"NFW ajustado: rho_s = {rho:.2e} kg/m^3 ; r_s = {rs:.1f} kpc ; rms = {rms / 1e3:.2f} km/s ; M(<10 r_s) = {m200:.2e} Msun (escala, no M200)")
    print(f"{'r [kpc]':>8} {'v MOND':>8} {'v NFW':>8}")
    for r, b in zip(rr, vm):
        if r in (2.0, 10.0, 20.0, 30.0):
            print(f"{r:8.1f} {b / 1e3:8.1f} {v_nfw(r, rho, rs) / 1e3:8.1f}")
    # 5) relacion g_obs - g_bar: universal en MOND
    print(f"{'g_N/a0':>8} {'g_obs/a0 (MOND)':>16}")
    for x in (0.01, 0.1, 1.0, 10.0):
        print(f"{x:8.2f} {g_mond(x * A0) / A0:16.4f}")
    # 6) cumulos en colision (juguete que enlaza con C09)
    off_gas_gal = 153.4
    fgas = 0.85
    pred = (1 - fgas) * off_gas_gal
    print(f"si la lente siguiera los barones con fraccion de gas {fgas}: desplazamiento masa-gas previsto = {pred:.1f} kpc frente a {off_gas_gal} kpc del juguete de C09")
    assert max(errs) < 1e-12
    assert max(tf) < 0.01
    assert rms < 0.1 * max(vm)
    assert v_mond(30.0, m, rd) > v_newton(30.0, m, rd) * 1.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
