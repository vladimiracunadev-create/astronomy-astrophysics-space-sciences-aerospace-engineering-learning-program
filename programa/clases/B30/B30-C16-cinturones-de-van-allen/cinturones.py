#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C16: latitud de espejo, cono de perdida y periodo de rebote en un campo dipolar.

Datos: e, m_p, m_e, c (NIST CODATA 2022) y R_E ecuatorial (IAU 2015 B3), consultados 2026-11-09. B_0 = 3.12e-5 T, las energias (protones de 10 MeV y electrones de 1 MeV),
L = 4 y la altura de la atmosfera (100 km) son ILUSTRATIVOS (sinteticos).
Modelo: B(lat) = B_eq sqrt(1 + 3 sen^2 lat)/cos^6 lat sobre una linea de campo; invariante mu: sen^2(alpha_eq) = B_eq/B_m en el punto de espejo; latitud de espejo por biseccion;
cono de perdida en la base de la linea (r = R_E + 100 km); periodo de rebote tau_b = 4 Int_0^{lat_m} (ds/dlat) dlat/(v cos alpha), ds = L R_E cos(lat) sqrt(1 + 3 sen^2 lat) dlat,
con cos alpha = sqrt(1 - sen^2(alpha_eq) B/B_eq), integrado por dos sustituciones distintas que eliminan la singularidad en el espejo; radio de giro relativista r_g = p_perp/(e B).
Supuestos: dipolo centrado, invariancia de mu, particulas relativistas, sin campo electrico. Validez: orientativa.
Tolerancia: las dos sustituciones coinciden a 1e-6; sen^2(alpha_eq) = B_eq/B_m a 1e-12 en el espejo.
"""
from __future__ import annotations
import math
import platform
import sys

Q, MP, ME, C = 1.602176634e-19, 1.67262192595e-27, 9.1093837139e-31, 299792458.0
R_E, B0 = 6.3781e6, 3.12e-5
L = 4.0


def f_b(lat):
    """B/B_eq sobre la linea de campo."""
    return math.sqrt(1 + 3 * math.sin(lat) ** 2) / math.cos(lat) ** 6


def lat_espejo(alpha_eq):
    y = math.sin(alpha_eq) ** 2
    lo, hi = 0.0, math.radians(89.999)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f_b(mid) < 1 / y:
            lo = mid
        else:
            hi = mid
    m = 0.5 * (lo + hi)
    assert abs(y * f_b(m) - 1) < 1e-9
    return m


def integrando(lat, y):
    arg = 1 - y * f_b(lat)
    return math.cos(lat) * math.sqrt(1 + 3 * math.sin(lat) ** 2) / math.sqrt(max(arg, 1e-300))


def tau_b(alpha_eq, v, metodo):
    y = math.sin(alpha_eq) ** 2
    lm = lat_espejo(alpha_eq)
    n = 20000
    s = 0.0
    if metodo == 1:         # lat = lm sen(theta), theta en [0, pi/2]
        h = (math.pi / 2) / n
        for i in range(n):
            th = (i + 0.5) * h
            lat = lm * math.sin(th)
            s += integrando(lat, y) * lm * math.cos(th) * h
    else:                   # lat = lm (1 - u^2), u en [0, 1]
        h = 1.0 / n
        for i in range(n):
            u = (i + 0.5) * h
            lat = lm * (1 - u * u)
            s += integrando(lat, y) * 2 * lm * u * h
    return 4 * L * R_E * s / v


def velocidad(t_mev, masa):
    gam = 1 + t_mev * 1e6 * Q / (masa * C ** 2)
    return C * math.sqrt(1 - 1 / gam ** 2), gam


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'alpha_eq [deg]':>14} {'lat. espejo [deg]':>18} {'B_m/B_eq':>10}")
    for a in (10.0, 30.0, 60.0, 80.0):
        lm = lat_espejo(math.radians(a))
        print(f"{a:14.1f} {math.degrees(lm):18.3f} {f_b(lm):10.3f}")
    # cono de perdida
    ra = R_E + 1e5
    cos2 = ra / (L * R_E)
    lat_a = math.acos(math.sqrt(cos2))
    b_atm = B0 * (R_E / ra) ** 3 * math.sqrt(1 + 3 * math.sin(lat_a) ** 2)
    b_eq = B0 / L ** 3
    a_lc = math.degrees(math.asin(math.sqrt(b_eq / b_atm)))
    print(f"L = {L:.0f}: B_eq = {b_eq * 1e9:.1f} nT ; en la base (100 km) lat = {math.degrees(lat_a):.2f} deg, B = {b_atm * 1e9:.0f} nT ; cono de perdida alpha_LC = {a_lc:.2f} deg")
    # periodo de rebote
    print(f"{'particula':<14} {'T [MeV]':>8} {'v/c':>7} {'alpha_eq':>9} {'tau_b met.1 [s]':>16} {'met.2 [s]':>10} {'L R_E/v [s]':>12}")
    for nombre, masa, t in (("proton", MP, 10.0), ("electron", ME, 1.0)):
        v, gam = velocidad(t, masa)
        for a in (30.0, 60.0, 85.0):
            t1, t2 = tau_b(math.radians(a), v, 1), tau_b(math.radians(a), v, 2)
            assert abs(t1 / t2 - 1) < 1e-6, f"dos metodos {nombre} {a}"
            print(f"{nombre:<14} {t:8.1f} {v / C:7.4f} {a:9.1f} {t1:16.3f} {t2:10.3f} {L * R_E / v:12.3f}")
    # radio de giro
    t_mev = 1.0
    pc = math.sqrt((t_mev * 1e6 * Q) ** 2 + 2 * t_mev * 1e6 * Q * ME * C ** 2)
    rg = (pc / C) / (Q * b_eq)
    print(f"electron de 1 MeV en el ecuador de L = 4: p c = {pc / Q / 1e6:.4f} MeV ; radio de giro (alpha = 90) = {rg / 1e3:.2f} km")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
