#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C10: semieje mayor y excentricidad desde los apsides y desde un vector de estado.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3).
ORBITAS SINTETICAS: (1) 200 x 35786 km de altitud (transferencia); (2) 600 x 800 km (casi circular); (3) 500 x 39700 km (muy excentrica).
Vectores de estado SINTETICOS: se generan en un punto arbitrario de cada orbita (nu = 110 grados, plano xy, marco inercial geocentrico, SI).
Segunda via: (a, e) se obtienen (i) de los apsides, (ii) del vector de estado con a = 1/(2/r - v^2/mu) y e = |((v^2 - mu/r) r - (r.v) v)/mu|,
(iii) de energia y momento angular (a = -mu/2eps, e = sqrt(1 + 2 eps h^2/mu^2)); las tres vias deben coincidir.
Sensibilidad: se perturba v en 1 m/s (en la direccion de v, en el periapsis) y se compara da con la derivada analitica da/dv = 2 v a^2/mu.
Tolerancias: acuerdo entre vias 1e-9 relativa; derivada numerica frente a analitica 5e-3 relativa (la diferencia es el termino de segundo orden de un salto finito de 1 m/s).
"""
from __future__ import annotations
import math, platform

MU, RE = 3.986004e14, 6.3781e6


def estado(rp, ra, nu_deg):
    a = 0.5 * (rp + ra)
    e = (ra - rp) / (ra + rp)
    p = a * (1 - e * e)
    nu = math.radians(nu_deg)
    r = p / (1 + e * math.cos(nu))
    pos = (r * math.cos(nu), r * math.sin(nu))
    f = math.sqrt(MU / p)
    vel = (-f * math.sin(nu), f * (e + math.cos(nu)))
    return pos, vel


def desde_estado(pos, vel):
    r = math.hypot(*pos)
    v2 = vel[0] ** 2 + vel[1] ** 2
    a = 1.0 / (2.0 / r - v2 / MU)
    rv = pos[0] * vel[0] + pos[1] * vel[1]
    ex = ((v2 - MU / r) * pos[0] - rv * vel[0]) / MU
    ey = ((v2 - MU / r) * pos[1] - rv * vel[1]) / MU
    return a, math.hypot(ex, ey)


def desde_energia(pos, vel):
    r = math.hypot(*pos)
    eps = 0.5 * (vel[0] ** 2 + vel[1] ** 2) - MU / r
    h = pos[0] * vel[1] - pos[1] * vel[0]
    return -MU / (2 * eps), math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU ** 2))


def calcular():
    R = {}
    casos = {"1": (RE + 200e3, RE + 35786e3), "2": (RE + 600e3, RE + 800e3), "3": (RE + 500e3, RE + 39700e3)}
    peor = 0.0
    for k, (rp, ra) in casos.items():
        a0 = 0.5 * (rp + ra)
        e0 = (ra - rp) / (ra + rp)
        pos, vel = estado(rp, ra, 110.0)
        a1, e1 = desde_estado(pos, vel)
        a2, e2 = desde_energia(pos, vel)
        R[f"a{k}"], R[f"e{k}"] = a0, e0
        R[f"rp{k}"], R[f"ra{k}"] = rp, ra
        R[f"r110_{k}"] = math.hypot(*pos)
        R[f"v110_{k}"] = math.hypot(*vel)
        d = max(abs(a1 - a0) / a0, abs(a2 - a0) / a0, abs(e1 - e0), abs(e2 - e0))
        R[f"dif{k}"] = d
        peor = max(peor, d)
        R[f"T{k}_min"] = 2 * math.pi * math.sqrt(a0 ** 3 / MU) / 60.0
    R["peor"] = peor
    # sensibilidad en el periapsis de la orbita 1
    rp, ra = casos["1"]
    a0 = 0.5 * (rp + ra)
    vp = math.sqrt(MU * (2 / rp - 1 / a0))
    dv = 1.0
    a_mas = 1.0 / (2.0 / rp - (vp + dv) ** 2 / MU)
    R["da_num"] = a_mas - a0
    R["da_ana"] = 2 * vp * a0 ** 2 / MU * dv
    R["dif_sens"] = abs(R["da_num"] - R["da_ana"]) / R["da_ana"]
    h = rp * (vp + dv)
    eps = 0.5 * (vp + dv) ** 2 - MU / rp
    R["e_nuevo"] = math.sqrt(1 + 2 * eps * h * h / MU ** 2)
    R["de_num"] = R["e_nuevo"] - R["e1"]
    R["ra_nuevo"] = a_mas * (1 + R["e_nuevo"])
    R["dra"] = R["ra_nuevo"] - ra
    R["vp"] = vp
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    for k in ("1", "2", "3"):
        print(f"Orbita SINTETICA {k}: periapsis {R['rp' + k] / 1e3:.1f} km ; apoapsis {R['ra' + k] / 1e3:.1f} km del centro")
        print(f"  a = {R['a' + k] / 1e3:.3f} km ; e = {R['e' + k]:.6f} ; T = {R['T' + k + '_min']:.3f} min")
        print(f"  en nu = 110 grados: r = {R['r110_' + k] / 1e3:.3f} km ; v = {R['v110_' + k]:.3f} m/s ; acuerdo de las tres vias = {R['dif' + k]:.1e}")
    print(f"Peor acuerdo entre vias = {R['peor']:.1e}")
    print(f"Sensibilidad (orbita 1, periapsis, +1 m/s a v_p = {R['vp']:.3f} m/s):")
    print(f"  delta a numerico = {R['da_num']:.3f} m ; analitico 2 v a^2/mu = {R['da_ana']:.3f} m ; dif = {R['dif_sens']:.1e}")
    print(f"  delta e = {R['de_num']:.3e} ; nuevo apoapsis = {R['ra_nuevo'] / 1e3:.3f} km (delta r_a = {R['dra'] / 1e3:.3f} km)")
    assert R["peor"] < 1e-9
    assert R["dif_sens"] < 5e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
