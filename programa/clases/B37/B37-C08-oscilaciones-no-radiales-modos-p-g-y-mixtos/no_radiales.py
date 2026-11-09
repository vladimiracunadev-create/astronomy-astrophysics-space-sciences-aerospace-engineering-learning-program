#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B37-C08: armonicos esfericos, frecuencias de Lamb y de Brunt-Vaisala y diagrama de propagacion de modos p y g.

Datos: constantes G, k_B y m_u de NIST CODATA 2022, consultadas el 2026-11-09. Los parametros de la capa isoterma (T = 6000 K, mu = 1,3, gamma = 5/3, g = 274 m/s2) y de la envoltura
para el diagrama (c y N de juguete) son ILUSTRATIVOS (sinteticos); no representan un modelo solar.
Modelo: (1) normalizacion de los armonicos esfericos Y_l^m por cuadratura (Gauss-Legendre por Simpson en mu = cos theta) y recuento de lineas nodales (l - |m| paralelos, |m| meridianos).
(2) Capa isoterma de gas ideal: N = (g/c) sqrt(gamma - 1) y frecuencia de corte acustica nu_ac = c/(4 pi H), con H = k T/(mu m_u g); se contrasta N^2 = g (1/gamma dlnP/dr - dlnrho/dr)
calculado por diferencias finitas con la forma analitica. (3) Relacion de dispersion local k_r^2 = (omega^2 - L_l^2)(omega^2 - N^2)/(c^2 omega^2): clasificacion en p (omega > L, N), g (omega < L, N) y evanescente.
Supuestos: aproximacion local (WKB), sin rotacion ni campo magnetico. Validez: orientativa.
Tolerancia: normalizacion de Y_l^m dentro de 1e-6; N numerico dentro de 1e-6 relativo del analitico; conteo de nodos exacto.
"""
from __future__ import annotations
import math, platform, sys

G_ = 6.67430e-11
KB = 1.380649e-23
MU = 1.66053906892e-27


def legendre(l, m, x):
    """P_l^m(x) por recurrencia (m >= 0), sin fase de Condon-Shortley."""
    pmm = 1.0
    if m > 0:
        s = math.sqrt((1 - x) * (1 + x))
        f = 1.0
        for _ in range(m):
            pmm *= f * s
            f += 2
    if l == m:
        return pmm
    pm1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pm1
    for ll in range(m + 2, l + 1):
        pl = (x * (2 * ll - 1) * pm1 - (ll + m - 1) * pmm) / (ll - m)
        pmm, pm1 = pm1, pl
    return pm1


def norma(l, m):
    return math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - m) / math.factorial(l + m))


def integral_Y2(l, m, n=20000):
    # Int |Y|^2 dOmega = 2 pi Int_-1^1 N^2 P^2 dmu
    h = 2.0 / n
    s = 0.0
    for i in range(n + 1):
        x = -1 + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * (norma(l, m) * legendre(l, m, x)) ** 2
    return 2 * math.pi * s * h / 3


def nodos_latitud(l, m, n=4000):
    cuenta = 0
    prev = None
    for i in range(1, n):
        x = -1 + 2 * i / n
        v = legendre(l, m, x)
        if prev is not None and v * prev < 0:
            cuenta += 1
        if v != 0:
            prev = v
    return cuenta


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'l':>3} {'m':>3} {'Int |Y|^2':>12} {'paralelos nodales':>18} {'meridianos':>11}")
    for l, m in ((1, 0), (1, 1), (2, 1), (3, 2), (5, 3), (10, 4)):
        I = integral_Y2(l, m)
        np_ = nodos_latitud(l, m)
        print(f"{l:3d} {m:3d} {I:12.8f} {np_:18d} {m:11d}")
        assert abs(I - 1) < 1e-6
        assert np_ == l - m
    # 2. capa isoterma
    T, mu, gam, g = 6000.0, 1.3, 5 / 3, 274.0
    c = math.sqrt(gam * KB * T / (mu * MU))
    H = KB * T / (mu * MU * g)
    N_ana = g / c * math.sqrt(gam - 1)
    # perfil: P = P0 exp(-z/H), rho = rho0 exp(-z/H); N^2 por diferencias finitas
    dz = 1000.0
    def lnP(z): return -z / H
    def lnrho(z): return -z / H
    z0 = 0.0
    dlnP = (lnP(z0 + dz) - lnP(z0 - dz)) / (2 * dz)
    dlnr = (lnrho(z0 + dz) - lnrho(z0 - dz)) / (2 * dz)
    N2 = g * (dlnP / gam - dlnr)
    N_num = math.sqrt(N2)
    nu_ac = c / (4 * math.pi * H)
    print(f"isoterma: c = {c / 1e3:.3f} km/s ; H = {H / 1e3:.3f} km ; N analitico = {N_ana:.6e} rad/s ; N numerico = {N_num:.6e} rad/s")
    print(f"frecuencia de corte acustica nu_ac = c/(4 pi H) = {nu_ac * 1e3:.3f} mHz ; N/(2 pi) = {N_ana / (2 * math.pi) * 1e3:.3f} mHz")
    assert abs(N_num / N_ana - 1) < 1e-6
    # 3. diagrama de propagacion en una capa de juguete (r = 0,95 R_sol, c = 100 km/s?) ilustrativa
    r, c_loc, N_loc = 6.6e8, 2.0e5, 1.0e-3
    print(f"{'l':>3} {'nu [mHz]':>9} {'L_l/(2pi) [mHz]':>16} {'N/(2pi) [mHz]':>14} {'k_r^2':>12} {'tipo':>12}")
    nu_N = N_loc / (2 * math.pi) * 1e3
    tipos = {}
    for l, nu in ((2, 3.0), (2, 0.05), (100, 3.0), (100, 0.05), (2, 0.14)):
        w = 2 * math.pi * nu * 1e-3
        L = math.sqrt(l * (l + 1)) * c_loc / r
        kr2 = (w * w - L * L) * (w * w - N_loc**2) / (c_loc**2 * w * w)
        if kr2 > 0:
            tipo = "p" if w > max(L, N_loc) else "g"
        else:
            tipo = "evanescente"
        tipos[(l, nu)] = tipo
        print(f"{l:3d} {nu:9.3f} {L / (2 * math.pi) * 1e3:16.4f} {nu_N:14.4f} {kr2:12.3e} {tipo:>12}")
    assert tipos[(2, 3.0)] == "p" and tipos[(2, 0.05)] == "g" and tipos[(2, 0.14)] == "evanescente"
    # el modo p de l alto tiene frecuencia de Lamb mayor
    Lh = math.sqrt(100 * 101) * c_loc / r
    Ll = math.sqrt(2 * 3) * c_loc / r
    print(f"L_100/L_2 = {Lh / Ll:.3f} (esperado sqrt(101*100/6) = {math.sqrt(101 * 100 / 6):.3f})")
    assert abs(Lh / Ll - math.sqrt(101 * 100 / 6)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
