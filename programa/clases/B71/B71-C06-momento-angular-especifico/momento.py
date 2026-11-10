#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C06: momento angular especifico h = r x v, h = sqrt(mu p) y velocidad areolar.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3).
Sistema: marco inercial geocentrico, SI, vectores 3D. ORBITA SINTETICA: periapsis 200 km, apoapsis 35786 km de altitud,
inclinada 28.5 grados (valor ilustrativo), con el periapsis en el eje +x.
Segunda via: h = r x v en cada punto de una integracion RK4 (4000 pasos, 3D) frente a h = sqrt(mu a (1 - e^2)) y a r_p v_p.
Tolerancias: |h| constante dentro de 1e-9 relativa; direccion de h constante dentro de 1e-9; r_p v_p = r_a v_a dentro de 1e-12.
"""
from __future__ import annotations
import math, platform

MU = 3.986004e14
RE = 6.3781e6


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norma(a):
    return math.sqrt(sum(x * x for x in a))


def rk4(s, dt):
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2 + s[2] ** 2) ** 1.5
        return (s[3], s[4], s[5], -MU * s[0] / d3, -MU * s[1] / d3, -MU * s[2] / d3)
    k1 = f(s)
    k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(6)))
    k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(6)))
    k4 = f(tuple(s[i] + dt * k3[i] for i in range(6)))
    return tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(6))


def calcular():
    R = {}
    rp, ra = RE + 200e3, RE + 35786e3
    a = 0.5 * (rp + ra)
    e = (ra - rp) / (ra + rp)
    p = a * (1 - e * e)
    R.update(rp=rp, ra=ra, a=a, e=e, p=p)
    vp = math.sqrt(MU * (2 / rp - 1 / a))
    va = math.sqrt(MU * (2 / ra - 1 / a))
    R.update(vp=vp, va=va)
    R["h_rpvp"] = rp * vp
    R["h_ra"] = ra * va
    R["h_formula"] = math.sqrt(MU * p)
    R["dif_pa"] = abs(rp * vp - ra * va) / (rp * vp)
    R["dif_formula"] = abs(rp * vp - R["h_formula"]) / R["h_formula"]
    R["areolar"] = 0.5 * R["h_formula"]
    t = 2 * math.pi * math.sqrt(a ** 3 / MU)
    R["T"] = t
    R["area_elipse"] = math.pi * a * a * math.sqrt(1 - e * e)
    R["area_por_T"] = R["areolar"] * t
    R["dif_area"] = abs(R["area_elipse"] - R["area_por_T"]) / R["area_elipse"]
    inc = math.radians(28.5)
    s = (rp, 0.0, 0.0, 0.0, vp * math.cos(inc), vp * math.sin(inc))
    h0 = cruz(s[:3], s[3:])
    h0n = norma(h0)
    u0 = tuple(x / h0n for x in h0)
    n = 4000
    dmod = ddir = 0.0
    for _ in range(n):
        s = rk4(s, t / n)
        h = cruz(s[:3], s[3:])
        hn = norma(h)
        dmod = max(dmod, abs(hn - h0n) / h0n)
        ddir = max(ddir, norma(tuple(h[i] / hn - u0[i] for i in range(3))))
    R["h_num"] = h0n
    R["deriva_mod"] = dmod
    R["deriva_dir"] = ddir
    R["inc_deg"] = math.degrees(math.acos(u0[2]))
    # velocidad transversal y radial en un punto: nu = 90 grados
    r90 = p
    R["r90"] = r90
    R["vt90"] = R["h_formula"] / r90
    R["vr90"] = MU / R["h_formula"] * e
    R["v90"] = math.hypot(R["vt90"], R["vr90"])
    R["v90_visviva"] = math.sqrt(MU * (2 / r90 - 1 / a))
    R["dif_v90"] = abs(R["v90"] - R["v90_visviva"]) / R["v90"]
    # circular de referencia
    R["h_circ_ra"] = math.sqrt(MU * ra)
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("Orbita SINTETICA: periapsis 200 km, apoapsis 35786 km de altitud, i = 28.5 grados (ilustrativo)")
    print(f"  a = {R['a'] / 1e3:.3f} km ; e = {R['e']:.6f} ; p = {R['p'] / 1e3:.3f} km")
    print(f"  r_p v_p = {R['h_rpvp']:.6e} m2/s ; r_a v_a = {R['h_ra']:.6e} m2/s ; sqrt(mu p) = {R['h_formula']:.6e} m2/s")
    print(f"  diferencias relativas: periapsis-apoapsis {R['dif_pa']:.1e} ; periapsis-formula {R['dif_formula']:.1e}")
    print(f"  velocidad areolar h/2 = {R['areolar']:.6e} m2/s ; area de la elipse = {R['area_elipse']:.6e} m2 ; h/2 * T = {R['area_por_T']:.6e} m2 ; dif = {R['dif_area']:.1e}")
    print(f"RK4 3D (4000 pasos): deriva maxima de |h| = {R['deriva_mod']:.2e} ; de la direccion de h = {R['deriva_dir']:.2e} ; inclinacion de h = {R['inc_deg']:.4f} grados")
    print(f"En nu = 90 grados (r = p = {R['r90'] / 1e3:.3f} km): v_transversal = h/r = {R['vt90']:.3f} m/s ; v_radial = mu e/h = {R['vr90']:.3f} m/s ; |v| = {R['v90']:.3f} m/s ; vis-viva = {R['v90_visviva']:.3f} m/s")
    print(f"h de una circular de radio r_a = {R['h_circ_ra']:.6e} m2/s (mayor que la de la transferencia)")
    assert R["dif_pa"] < 1e-12 and R["dif_formula"] < 1e-12
    assert R["deriva_mod"] < 1e-9 and R["deriva_dir"] < 1e-9
    assert R["dif_area"] < 1e-12 and R["dif_v90"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
