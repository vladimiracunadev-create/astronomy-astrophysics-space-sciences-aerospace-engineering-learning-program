#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C12: guiado relativo de dos impulsos con la matriz de transicion de HCW.

Datos CONSULTADOS (2026-11-10): GM_T = 398600.435507 km3/s2 (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): objetivo circular a 400 km; estado inicial relativo (x, y, z) = (0, -1000, 100) m con velocidad relativa nula;
punto final (0, -100, 0) m con velocidad relativa nula; duraciones T/P = 0.25 ... 2.0.
Modelo: v0+ = Phi_rv^-1 (r_f - Phi_rr r0); dv1 = v0+ - v0; dv2 = v_f - (Phi_vr r0 + Phi_vv v0+).
Verificacion independiente: el impulso 1 se aplica en la integracion no lineal de dos cuerpos (RK4, paso 1 s) y se compara la posicion final
con la de HCW. Cuando det(Phi_rv) es casi nulo (T multiplo de medio periodo: sin(nT) = 0 anula el control del movimiento normal al plano) el problema esta mal condicionado y se informa.
Tolerancias: error de llegada de HCW < 1e-6 m; diferencia con el modelo no lineal del orden de (separacion)^2/r.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)
P = 2 * math.pi / N
RI, VI = [0.0, -1000.0, 100.0], [0.0, 0.0, 0.0]
RF, VF = [0.0, -100.0, 0.0], [0.0, 0.0, 0.0]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def caso(frac):
    T = frac * P
    rr, rv, vr, vv = hcw_blocks(N, T)
    d = det3(rv)
    if abs(d) < 1e-3 * (1 / N) ** 3:
        return dict(frac=frac, singular=True, det=d)
    dv1, dv2 = dos_impulsos(N, T, RI, VI, RF, VF)
    s0 = (RI[0], RI[1], RI[2], dv1[0], dv1[1], dv1[2])
    fin = hcw(N, T, s0)
    err_hcw = math.dist(fin[:3], RF)
    ref, cue = lvlh_a_inercial(s0, R0, N)
    ref = propagar_dt(kepler_rhs, ref, T, 1.0)
    cue = propagar_dt(kepler_rhs, cue, T, 1.0)
    nl = inercial_a_lvlh(ref, cue, N)
    return dict(frac=frac, singular=False, dv1=math.hypot(*dv1), dv2=math.hypot(*dv2), err=err_hcw,
                nl=math.dist(nl[:3], RF), det=d)


def calcular():
    return [caso(f) for f in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0)]


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"n = {N:.6e} rad/s ; P = {P / 60:.3f} min ; inicial {RI} m -> final {RF} m, velocidades nulas")
    print(" T/P    dv1 [m/s]   dv2 [m/s]   total [m/s]   error HCW [m]   desvio no lineal [m]   det(Phi_rv)")
    for q in r:
        if q['singular']:
            print(f"{q['frac']:4.2f}   mal condicionado (det = {q['det']:.3e})")
        else:
            print(f"{q['frac']:4.2f}   {q['dv1']:9.4f}   {q['dv2']:9.4f}   {q['dv1'] + q['dv2']:10.4f}   {q['err']:12.2e}   {q['nl']:14.3f}   {q['det']:.3e}")
    ok = [q for q in r if not q['singular']]
    for q in ok:
        assert q['err'] < 1e-6
    assert ok and min(q['dv1'] + q['dv2'] for q in ok) > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
