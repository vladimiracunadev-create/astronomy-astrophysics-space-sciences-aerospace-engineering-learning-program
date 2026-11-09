#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C07: horizonte, orbita estable mas interna (ISCO) y eficiencia radiativa en la metrica de Kerr.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09; 1 au (IERS TN36, Tabla 1.1).
Masa de M87*: 6.5 (+/-0.7) x 10^9 Msol (Event Horizon Telescope, arXiv:1906.11238, resumen, consultado 2026-11-09).
Los espines de la tabla son ILUSTRATIVOS (sinteticos).
Modelo: unidades geometricas G = c = M = 1. Horizontes r_pm = 1 +- sqrt(1 - a^2). Energia especifica de una orbita
circular ecuatorial prograda (+) o retrograda (-): E = (1 - 2/r +- a/r^1.5)/sqrt(1 - 3/r +- 2a/r^1.5); el ISCO es el
minimo de E(r). Formula de Bardeen: r_isco = 3 + Z2 -+ sqrt((3 - Z1)(3 + Z1 + 2 Z2)), Z1 = 1 + (1 - a^2)^(1/3)
((1 + a)^(1/3) + (1 - a)^(1/3)), Z2 = sqrt(3 a^2 + Z1^2). Eficiencia eta = 1 - E(r_isco).
Supuestos: agujero negro de Kerr aislado, orbitas circulares ecuatoriales. Validez: 0 <= a < 1.
Tolerancia: 1e-6 entre el minimo numerico y la formula de Bardeen.
"""
from __future__ import annotations
import math
import platform
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
AU = 1.49597870700e11


def energia(r, a, s):
    return (1 - 2 / r + s * a / r ** 1.5) / math.sqrt(1 - 3 / r + s * 2 * a / r ** 1.5)


def isco_numerico(a, s):
    r_h = 1 + math.sqrt(1 - a * a)
    lo, hi = r_h * 1.0000001, 12.0
    # buscar el minimo de E(r) con razon aurea en la rama estable r > r_ph
    n = 400
    pts = [lo + (hi - lo) * i / n for i in range(n + 1)]
    vals = []
    for r in pts:
        d = 1 - 3 / r + s * 2 * a / r ** 1.5
        vals.append(energia(r, a, s) if d > 0 else float('inf'))
    i0 = min(range(len(vals)), key=lambda i: vals[i])
    a_, b_ = pts[max(i0 - 1, 0)], pts[min(i0 + 1, n)]
    g = (math.sqrt(5) - 1) / 2
    c_, d_ = b_ - g * (b_ - a_), a_ + g * (b_ - a_)
    for _ in range(200):
        if energia(c_, a, s) < energia(d_, a, s):
            b_ = d_
        else:
            a_ = c_
        c_, d_ = b_ - g * (b_ - a_), a_ + g * (b_ - a_)
    return 0.5 * (a_ + b_)


def isco_bardeen(a, s):
    z1 = 1 + (1 - a * a) ** (1 / 3) * ((1 + a) ** (1 / 3) + (1 - a) ** (1 / 3))
    z2 = math.sqrt(3 * a * a + z1 * z1)
    return 3 + z2 - s * math.sqrt((3 - z1) * (3 + z1 + 2 * z2))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'a':>5} {'r_+ [M]':>8} {'ISCO pro [M]':>13} {'eta pro [%]':>12} {'ISCO retro [M]':>15} {'eta retro [%]':>14}")
    for a in (0.0, 0.5, 0.9, 0.998):
        for s in (1, -1):
            n, b = isco_numerico(a, s), isco_bardeen(a, s)
            assert abs(n / b - 1) < 1e-6, f"ISCO numerico != Bardeen (a={a}, s={s})"
        rp, rr = isco_bardeen(a, 1), isco_bardeen(a, -1)
        print(f"{a:5.3f} {1 + math.sqrt(1 - a * a):8.4f} {rp:13.4f} {100 * (1 - energia(rp, a, 1)):12.2f} "
              f"{rr:15.4f} {100 * (1 - energia(rr, a, -1)):14.2f}")
    assert abs(isco_bardeen(0.0, 1) - 6.0) < 1e-9 and abs(isco_bardeen(1.0, 1) - 1.0) < 1e-6
    assert abs(isco_bardeen(1.0, -1) - 9.0) < 1e-6
    tg = GM_SOL / C ** 3
    print(f"GM_sol/c^3 = {tg * 1e6:.4f} us ; GM_sol/c^2 = {GM_SOL / C ** 2:.2f} m")
    M = 6.5e9
    rg = M * GM_SOL / C ** 2
    print(f"M87* (6.5e9 Msol): r_g = {rg:.3e} m = {rg / AU:.1f} au ; r_s = {2 * rg / AU:.1f} au ; GM/c^3 = {M * tg / 3600:.2f} h")
    T = 2 * math.pi * 6 ** 1.5 * M * tg / 86400
    print(f"periodo de la orbita en el ISCO de Schwarzschild: {T:.1f} d")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
