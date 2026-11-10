#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C09: solucion de Hill-Clohessy-Wiltshire frente a la integracion no lineal de dos cuerpos.

Datos CONSULTADOS (2026-11-10): GM de la Tierra = 398600.435507 km3/s2 (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): orbita circular de la referencia a 400 km de altitud; estados relativos iniciales de 100 m y 1000 m.
Modelo: x radial (saliente), y a lo largo de la trayectoria, z normal; la referencia es circular con n = sqrt(GM/r^3).
Verdad numerica: dos cuerpos inerciales (RK4, paso 1 s) de la referencia y del cuerpo, con el estado relativo convertido al marco LVLH.
Tolerancias: HCW con ydot0 = -2 n x0 sin deriva (< 1e-6 m tras 5 orbitas); error HCW frente a no lineal del orden (offset^2/r).
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

MU_SI = GM_T * 1e9
R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(MU_SI / R0 ** 3)
PERIODO = 2 * math.pi / N


def inercial_desde_lvlh(rel):
    """Estado inercial de la referencia en (R0,0,0) con v=(0,N*R0,0) (LVLH = ejes inerciales en t = 0)."""
    x, y, z, u, v, w = rel
    # cuerpo: posicion = ref + rel; velocidad = ref + rel_vel + omega x rel (omega = N z^)
    ref = (R0, 0.0, 0.0, 0.0, N * R0, 0.0)
    cue = (R0 + x, y, z, u - N * y, N * R0 + v + N * x, w)
    return ref, cue


def lvlh_desde_inercial(ref, cue, t):
    """Estado relativo en LVLH de la referencia (circular, avanza con angulo N*t)."""
    th = math.atan2(ref[1], ref[0])
    c, s = math.cos(th), math.sin(th)
    rr = math.hypot(ref[0], ref[1])
    dx, dy, dz = cue[0] - ref[0], cue[1] - ref[1], cue[2] - ref[2]
    x = c * dx + s * dy
    y = -s * dx + c * dy
    dvx, dvy, dvz = cue[3] - ref[3], cue[4] - ref[4], cue[5] - ref[5]
    u = c * dvx + s * dvy + N * y          # velocidad relativa en LVLH: restar omega x rel
    v = -s * dvx + c * dvy - N * x
    return (x, y, dz, u, v, dvz)


def error_no_lineal(rel0, n_orb):
    ref, cue = inercial_desde_lvlh(rel0)
    t = n_orb * PERIODO
    ref = propagar_dt(kepler_rhs, ref, t, 1.0)
    cue = propagar_dt(kepler_rhs, cue, t, 1.0)
    veradero = lvlh_desde_inercial(ref, cue, t)
    lineal = hcw(N, t, rel0)
    return math.dist(veradero[:3], lineal[:3]), veradero, lineal


def calcular():
    out = dict(n=N, periodo=PERIODO / 60.0, casos=[])
    for desc, rel0 in (("elipse 100 m", (100.0, 0.0, 0.0, 0.0, -2 * N * 100.0, 0.0)),
                       ("elipse 1000 m", (1000.0, 0.0, 0.0, 0.0, -2 * N * 1000.0, 0.0)),
                       ("v-bar 1000 m", (0.0, -1000.0, 0.0, 0.0, 0.0, 0.0)),
                       ("deriva (x0=100 m, v=0)", (100.0, 0.0, 0.0, 0.0, 0.0, 0.0))):
        fila = [desc]
        for n_orb in (1, 5):
            e, vv, ll = error_no_lineal(rel0, n_orb)
            fila.append((n_orb, e, ll))
        out['casos'].append(fila)
    # sin deriva con ydot0 = -2 n x0: posicion y tras 5 orbitas
    out['deriva_cond'] = hcw(N, 5 * PERIODO, (100.0, 0.0, 0.0, 0.0, -2 * N * 100.0, 0.0))[1]
    out['deriva_libre'] = hcw(N, PERIODO, (100.0, 0.0, 0.0, 0.0, 0.0, 0.0))[1]
    out['deriva_teoria'] = -12 * math.pi * 100.0   # deriva por orbita = -12 pi x0 (HCW con velocidad relativa nula)
    return out


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Referencia circular r = {R0 / 1e3:.3f} km ; n = {r['n']:.6e} rad/s ; periodo = {r['periodo']:.3f} min")
    print(" caso                     orbitas  |error HCW - no lineal| [m]   y_HCW [m]")
    for fila in r['casos']:
        for (n_orb, e, ll) in fila[1:]:
            print(f"{fila[0]:24s} {n_orb:5d}   {e:14.4f}                  {ll[1]:12.3f}")
    print(f"Deriva en y tras 1 orbita con x0 = 100 m y velocidad nula = {r['deriva_libre']:.3f} m (formula -12 pi x0 = {r['deriva_teoria']:.3f} m)")
    print(f"y tras 5 orbitas con ydot0 = -2 n x0 = {r['deriva_cond']:.3e} m (acotado)")
    assert abs(r['deriva_libre'] - r['deriva_teoria']) < 1e-6
    assert abs(r['deriva_cond']) < 1e-6
    # el error crece con el desplazamiento
    e100 = r['casos'][0][2][1]
    e1000 = r['casos'][1][2][1]
    assert e1000 > e100
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
