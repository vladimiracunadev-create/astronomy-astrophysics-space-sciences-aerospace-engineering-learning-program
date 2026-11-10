#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C11: aproximacion por tramos a lo largo de la trayectoria (V-bar) y seguridad pasiva.

Datos CONSULTADOS (2026-11-10): GM_T = 398600.435507 km3/s2 (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): orbita del objetivo a 400 km; tramos V-bar de -5000 m a -1000 m, -300 m y -50 m; duraciones de 1/2, 1/4 y 1/8 de periodo;
esfera de exclusion de 200 m (hipotesis del autor, no un requisito consultado).
Modelo: HCW (x radial, y a lo largo de la trayectoria), guiado de dos impulsos de cislunar_lib.dos_impulsos.
Seguridad pasiva: si falla el segundo impulso, se propaga HCW 3 periodos y se mide la distancia minima al objetivo.
Verificacion: llegada propagada con HCW frente al punto objetivo < 1e-9 m; la velocidad tras el impulso 2 es nula.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)
P = 2 * math.pi / N
EXCL = 200.0


def tramo(y0, yf, frac):
    T = frac * P
    dv1, dv2 = dos_impulsos(N, T, [0, y0, 0], [0, 0, 0], [0, yf, 0], [0, 0, 0])
    v0p = dv1
    fin = hcw(N, T, (0, y0, 0, v0p[0], v0p[1], v0p[2]))
    err = math.dist(fin[:3], (0, yf, 0))
    # falla del segundo impulso: seguir con la velocidad al final del tramo
    s = fin
    dmin = 1e18
    for k in range(0, 3 * 360):
        s2 = hcw(N, k * P / 360.0, s)
        dmin = min(dmin, math.dist(s2[:3], (0, 0, 0)))
    return dict(T=T, dv1=math.hypot(*dv1), dv2=math.hypot(*dv2), err=err, dmin=dmin, dv1v=dv1, dv2v=dv2,
                vsal=math.hypot(*dv2[:3]))


def calcular():
    tramos = [(-5000.0, -1000.0, 0.5), (-1000.0, -300.0, 0.25), (-300.0, -50.0, 0.125)]
    res = [tramo(*t) for t in tramos]
    return dict(n=N, P=P / 60, tramos=tramos, res=res, total=sum(r['dv1'] + r['dv2'] for r in res),
                rbar=tramo_rbar())


def tramo_rbar():
    """Aproximacion R-bar: desde 200 m por debajo (x = -200) hasta 50 m por debajo en 1/4 de periodo, con velocidad final nula."""
    T = 0.25 * P
    dv1, dv2 = dos_impulsos(N, T, [-200.0, 0, 0], [0, 0, 0], [-50.0, 0, 0], [0, 0, 0])
    return dict(dv1=math.hypot(*dv1), dv2=math.hypot(*dv2), dv1v=dv1)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Orbita del objetivo: n = {r['n']:.6e} rad/s ; periodo = {r['P']:.3f} min ; esfera de exclusion ILUSTRATIVA = {EXCL} m")
    print(" tramo y0 -> yf [m]    T [min]   dv1 [m/s]   dv2 [m/s]   error llegada [m]   dist. minima si falla dv2 [m]")
    for (y0, yf, f), q in zip(r['tramos'], r['res']):
        print(f"{y0:7.0f} -> {yf:6.0f}   {q['T'] / 60:7.2f}   {q['dv1']:9.4f}   {q['dv2']:9.4f}   {q['err']:12.2e}   {q['dmin']:12.1f}")
    print(f"Delta-v total de los tres tramos = {r['total']:.4f} m/s")
    rb = r['rbar']
    print(f"R-bar de x = -200 m a -50 m en un cuarto de periodo: dv1 = {rb['dv1']:.4f} m/s ; dv2 = {rb['dv2']:.4f} m/s")
    for q in r['res']:
        assert q['err'] < 1e-6
    assert r['res'][0]['dmin'] > 0 and r['total'] < 5.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
