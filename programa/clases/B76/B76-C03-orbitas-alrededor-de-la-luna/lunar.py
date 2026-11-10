#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C03: orbitas circulares alrededor de la Luna y efecto de la Tierra (CR3BP plano).

Datos CONSULTADOS (2026-11-10): GM_L = 4902.800118 km3/s2 (JPL, DE440), R_L = 1737.4 km (JPL, IAU 2015), a_L = 384400 km.
ILUSTRATIVOS: altitudes de 100 km y 2000 km; radios de prueba 0.1, 0.3, 0.5 y 0.9 de la esfera de Hill.
Modelo: (1) kepleriano lunar; (2) CR3BP plano en ejes sinodicos; orbita circular de radio r alrededor de la Luna con velocidad
inercial sqrt(mu/r); velocidad sinodica = +-v - r (prograda +, retrograda -). RK4 de paso 5e-4 (adimensional) durante 30 d.
Criterio de "ligada": la distancia a la Luna no supera 1.0 radio de Hill durante 30 d. No incluye el Sol ni el campo no esferico lunar.
Tolerancias: conservacion de la constante de Jacobi < 1e-6 en cada integracion.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

RH = (MU / 3) ** (1 / 3)  # radio de Hill adimensional


def kepler(alt):
    r = R_L + alt
    v = math.sqrt(GM_L / r)
    return r, v, 2 * math.pi * r / v / 60.0, math.sqrt(2) * v


def prueba(frac, sentido, dias_=30.0):
    r = frac * RH
    v = math.sqrt(MU / r)
    s = (1 - MU + r, 0.0, 0.0, 0.0, sentido * v - r, 0.0)
    c0 = jacobi(s)
    rmax = r
    t = 0.0
    h = 5e-4
    tf = dias_ * DIA / T_U
    while t < tf:
        s = rk4(rhs, s, h)
        t += h
        d = math.hypot(s[0] - (1 - MU), s[1])
        rmax = max(rmax, d)
        if d > 3 * RH:
            break
    return rmax / RH, abs(jacobi(s) - c0), t * T_U / DIA


def calcular():
    out = dict(kep={a: kepler(a) for a in (100.0, 2000.0)}, casos={})
    for frac in (0.1, 0.3, 0.5, 0.9):
        for nom, sg in (("prograda", 1), ("retrograda", -1)):
            out['casos'][(frac, nom)] = prueba(frac, sg)
    out['rh_km'] = RH * A_L
    return out


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Kepleriano lunar (GM_L consultado):")
    for a, (rr, v, p, ve) in r['kep'].items():
        print(f"  h = {a:6.0f} km : r = {rr:7.1f} km ; v = {v:.4f} km/s ; P = {p:7.2f} min ; v_esc = {ve:.4f} km/s")
    print(f"Radio de Hill = {r['rh_km']:.0f} km. CR3BP plano, 30 d (ILUSTRATIVO en radios de prueba):")
    print(" r/R_Hill  sentido     max r/R_Hill  |dC|       t_integrado [d]")
    for (f, nom), (mx, dc, t) in r['casos'].items():
        estado = "sale de la esfera de Hill" if mx > 1.0 else "ligada"
        print(f"  {f:4.2f}    {nom:10s}   {mx:8.3f}   {dc:9.2e}   {t:6.2f}  {estado}")
    for k, (mx, dc, t) in r['casos'].items():
        assert dc < 1e-6, (k, dc)
    assert r['casos'][(0.1, 'prograda')][0] < 1.0 and r['casos'][(0.1, 'retrograda')][0] < 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
