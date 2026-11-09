#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C06: colapso esferico, umbral delta_c y funcion de masa de Press-Schechter.

Datos: G = 6.67430e-11 m^3 kg^-1 s^-2 (NIST CODATA 2022, tabla allascii consultada 2026-11-09); 1 au = 149 597 870 700 m (IERS TN36, consultada 2026-11-09)
para definir el Mpc; Omega_m = 0.315, h = 0.674 y sigma8 = 0.811 (resumen de Planck 2018, arXiv:1807.06209, consultado 2026-11-09).
La relacion sigma(M) = sigma8 (M/M8)^-0.27 es una ley de potencias ILUSTRATIVA (no el sigma(M) de un espectro real).
Modelo: (a) delta_c por el colapso de una capa en Einstein-de Sitter: formula cerrada (3/20)(12 pi)^(2/3) y cuadratura numerica independiente del tiempo de colapso;
(b) fraccion de masa en halos de Press-Schechter F(>M) = erfc(nu/sqrt 2), nu = delta_c/sigma(M); (c) caminatas aleatorias del conjunto de excursion con semilla 20261109.
Supuestos: colapso esferico, EdS, sin cizalla ni rotacion; la mitad de la masa que PS asigna con el factor 2 es la correccion historica; no se usa Sheth-Tormen.
Tolerancia: delta_c numerico dentro del 0,1 % del cerrado; fraccion de caminatas dentro de 3 sigma binomial de erfc con la barrera corregida por discretizacion (0,5826 sqrt(dS), correccion conocida NO consultada).
"""
from __future__ import annotations
import math, platform, random

G = 6.67430e-11
AU = 149597870700.0
MPC = AU * 648000 / math.pi * 1e6
OM, H, S8 = 0.315, 0.674, 0.811


def delta_c_cerrado():
    return 3.0 / 20.0 * (12 * math.pi) ** (2.0 / 3.0)


def delta_c_numerico(di):
    # unidades: H_i = 1, radio de fondo R_b = 1 en t_i, G M = 1/2 (masa del radio lagrangiano r = 1), R_i = 1 - di/3, v_i = (1 - di/3)^2 (modo creciente)
    gm = 0.5
    ri = 1 - di / 3
    vi = (1 - di / 3) ** 2
    e = 0.5 * vi * vi - gm / ri
    rmax = gm / (-e)
    c = 2 * rmax / math.sqrt(2 * gm / rmax)

    def t_sub(phi):
        # t(phi) = c Int_0^phi sin^2 u du por Simpson (n par)
        n = 20000
        h = phi / n
        s = math.sin(0) ** 2 + math.sin(phi) ** 2
        for i in range(1, n):
            s += (4 if i % 2 else 2) * math.sin(i * h) ** 2
        return c * s * h / 3

    phi_i = math.asin(math.sqrt(ri / rmax))
    t_ida = t_sub(math.pi / 2) - t_sub(phi_i)
    t_col = t_ida + t_sub(math.pi / 2)  # simetrica en el colapso
    ti_bg = 2.0 / 3.0
    ac = (1 + t_col / ti_bg) ** (2.0 / 3.0)
    return di * ac


def rho_crit_h1():
    h0 = 100e3 / MPC  # s^-1
    return 3 * h0 * h0 / (8 * math.pi * G)  # kg/m^3


def msun_h():
    # masa de referencia: kg -> unidades de 1e13 Msun/h con GM_sun = 1.3271244e20 m^3/s^2 (UAI 2015 B3, valor nominal)
    return 1.3271244e20 / G


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dc = delta_c_cerrado()
    print(f"delta_c cerrado = {dc:.5f}")
    print(f"{'delta_i':>9} {'delta_c numerico':>17} {'dif. relativa':>14}")
    prev = None
    for di in (1e-3, 1e-4, 1e-5):
        v = delta_c_numerico(di)
        print(f"{di:9.0e} {v:17.5f} {abs(v - dc) / dc:14.2e}")
        prev = v
    dcn = prev
    # funcion de masa
    rho = rho_crit_h1()
    msun = msun_h()
    rho_m = OM * rho / msun * MPC ** 3  # Msun h^2 / Mpc^3 -> con h=1: Msun (Mpc/h)^-3
    m8 = 4 * math.pi / 3 * rho_m * 8.0 ** 3
    print(f"rho_crit/h^2 = {rho / msun * MPC ** 3:.4e} Msun/Mpc^3 ; rho_m (h=1) = {rho_m:.4e} ; M8 = {m8:.3e} Msun/h")
    sig = lambda m: S8 * (m / m8) ** -0.27
    print(f"{'M [Msun/h]':>11} {'sigma(M)':>9} {'nu':>7} {'F(>M)':>8} {'n(>M) [(Mpc/h)^-3]':>20}")
    tab = {}
    for lm in (11, 12, 13, 14, 15):
        m = 10.0 ** lm
        nu = dc / sig(m)
        F = math.erfc(nu / math.sqrt(2))
        # n(>M) = Int_M^inf (rho/M') dF/dlnM' dlnM' ; por cuadratura en ln M
        n = 4000
        top = math.log(1e17)
        a = math.log(m)
        h = (top - a) / n
        def dn(l):
            mm = math.exp(l)
            nu2 = dc / sig(mm)
            dFdl = math.sqrt(2 / math.pi) * math.exp(-nu2 ** 2 / 2) * nu2 * 0.27
            return rho_m / mm * dFdl
        s = dn(a) + dn(top) + sum((4 if i % 2 else 2) * dn(a + i * h) for i in range(1, n))
        nn = s * h / 3
        tab[lm] = (nu, F, nn)
        print(f"{m:11.1e} {sig(m):9.3f} {nu:7.3f} {F:8.4f} {nn:20.3e}")
    # consistencia: la integral de M dn/dlnM reproduce F(>M)
    m = 1e13
    n = 4000
    a, top = math.log(m), math.log(1e17)
    h = (top - a) / n
    def mdn(l):
        mm = math.exp(l)
        nu2 = dc / sig(mm)
        return math.sqrt(2 / math.pi) * math.exp(-nu2 ** 2 / 2) * nu2 * 0.27
    s = mdn(a) + mdn(top) + sum((4 if i % 2 else 2) * mdn(a + i * h) for i in range(1, n))
    Fint = s * h / 3
    print(f"fraccion de masa por cuadratura = {Fint:.5f} ; erfc = {tab[13][1]:.5f}")
    # caminatas del conjunto de excursion
    rng = random.Random(20261109)
    nw = 4000
    print(f"{'S':>5} {'pasos':>6} {'cruces':>7} {'frac. sim.':>11} {'erfc(dc/sqrt(2S))':>18} {'barrera corr.':>14} {'sigma bin.':>10}")
    res = []
    for pasos in (250, 1000):
        smax = 4.0
        ds = smax / pasos
        sd = math.sqrt(ds)
        cruzo = [None] * nw
        for w in range(nw):
            d = 0.0
            for i in range(1, pasos + 1):
                d += rng.gauss(0, sd)
                if d >= dc:
                    cruzo[w] = i * ds
                    break
        for S in (1.0, 2.0, 4.0):
            c = sum(1 for x in cruzo if x is not None and x <= S + 1e-12)
            fr = c / nw
            pt = math.erfc(dc / math.sqrt(2 * S))
            sg = math.sqrt(pt * (1 - pt) / nw)
            ptc = math.erfc((dc + 0.5826 * sd) / math.sqrt(2 * S))
            res.append((pasos, S, fr, pt, sg, ptc))
            print(f"{S:5.1f} {pasos:6d} {c:7d} {fr:11.4f} {pt:18.4f} {ptc:18.4f} {sg:10.4f}")
    assert abs(dcn - dc) / dc < 1e-3
    assert abs(Fint - tab[13][1]) < 1e-4
    # la discretizacion pierde cruces; con la barrera desplazada 0.5826 sqrt(dS) (correccion conocida, no consultada) coincide
    for pasos, S, fr, pt, sg, ptc in res:
        assert fr <= pt + 3 * sg
        assert abs(fr - ptc) < 3 * sg
    assert tab[11][2] > tab[13][2] > tab[15][2]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
