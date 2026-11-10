#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C17: transformaciones inercial - LVLH - sinodico con verificacion de ida y vuelta e invariantes.

Datos CONSULTADOS (2026-11-10): GM_T, GM_L (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC), a_L = 384400 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): referencia circular a 400 km; estado relativo (120, -800, 40, 0.05, -0.3, 0.01) m y m/s; estado cislunar (0.9, 0.1, 0.05,
-0.2, 0.3, 0.1) adimensional; tiempo adimensional 0.7. No son observaciones.
Modelo: (1) LVLH de una referencia circular (x radial, y a lo largo de la trayectoria, z normal) con el cambio de marco que resta omega x r;
(2) sinodico <-> inercial del CR3BP con angulo theta = t (adimensional). Se trabaja sin SPICE ni efemerides (su uso no se consulto).
Invariantes: Jacobi sinodico C = 2 Omega - v^2 y la forma inercial C = -2 (E_in - h_z) con E_in = v_in^2/2 - (1-mu)/r1 - mu/r2.
Tolerancias: ida y vuelta < 1e-9 (relativa); igualdad de las dos formas del Jacobi < 1e-12.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

R0 = (R_T_EQ + 400.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)


def syn_a_in(s, t, mu=MU):
    x, y, z, vx, vy, vz = s
    c, sn = math.cos(t), math.sin(t)
    X, Y = c * x - sn * y, sn * x + c * y
    VX = c * (vx - y) - sn * (vy + x)
    VY = sn * (vx - y) + c * (vy + x)
    return (X, Y, z, VX, VY, vz)


def in_a_syn(S, t, mu=MU):
    X, Y, z, VX, VY, vz = S
    c, sn = math.cos(t), math.sin(t)
    x, y = c * X + sn * Y, -sn * X + c * Y
    vxr = c * VX + sn * VY
    vyr = -sn * VX + c * VY
    return (x, y, z, vxr + y, vyr - x, vz)


def jacobi_inercial(S, t, mu=MU):
    X, Y, Z, VX, VY, VZ = S
    c, sn = math.cos(t), math.sin(t)
    # posiciones de la Tierra y la Luna en el marco inercial
    xe, ye = -mu * c, -mu * sn
    xm, ym = (1 - mu) * c, (1 - mu) * sn
    r1 = math.sqrt((X - xe) ** 2 + (Y - ye) ** 2 + Z * Z)
    r2 = math.sqrt((X - xm) ** 2 + (Y - ym) ** 2 + Z * Z)
    e = 0.5 * (VX ** 2 + VY ** 2 + VZ ** 2) - (1 - mu) / r1 - mu / r2
    hz = X * VY - Y * VX
    return -2 * (e - hz)


def calcular():
    rel = (120.0, -800.0, 40.0, 0.05, -0.3, 0.01)
    ref, cue = lvlh_a_inercial(rel, R0, N)
    ida_vuelta = max(abs(a - b) for a, b in zip(inercial_a_lvlh(ref, cue, N), rel))
    # punto fijo en LVLH: su velocidad inercial relativa a la referencia es n x r
    fijo = (120.0, -800.0, 40.0, 0.0, 0.0, 0.0)
    ref2, cue2 = lvlh_a_inercial(fijo, R0, N)
    vrel = [cue2[3] - ref2[3], cue2[4] - ref2[4], cue2[5] - ref2[5]]
    esperado = [-N * fijo[1], N * fijo[0], 0.0]
    err_omega = max(abs(a - b) for a, b in zip(vrel, esperado))
    # sinodico
    s = (0.9, 0.1, 0.05, -0.2, 0.3, 0.1)
    t = 0.7
    S = syn_a_in(s, t)
    rt = max(abs(a - b) for a, b in zip(in_a_syn(S, t), s))
    c_syn = jacobi(s)
    c_in = jacobi_inercial(S, t)
    # la Luna fija en el sinodico
    luna_in = syn_a_in((1 - MU, 0, 0, 0, 0, 0), 0.0)
    v_luna = math.hypot(luna_in[3], luna_in[4]) * A_L * N_L
    return dict(ida_vuelta=ida_vuelta, err_omega=err_omega, rt=rt, c_syn=c_syn, c_in=c_in, dc=abs(c_syn - c_in),
                v_luna=v_luna, vrel=vrel, esperado=esperado, S=S)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"LVLH <-> inercial: error de ida y vuelta = {r['ida_vuelta']:.2e}")
    print(f"Punto fijo en LVLH: velocidad inercial relativa = ({r['vrel'][0]:.6f}, {r['vrel'][1]:.6f}, {r['vrel'][2]:.6f}) m/s ; n x r = ({r['esperado'][0]:.6f}, {r['esperado'][1]:.6f}, {r['esperado'][2]:.6f}) m/s")
    print(f"Sinodico <-> inercial: error de ida y vuelta = {r['rt']:.2e}")
    print(f"Estado inercial = ({', '.join(f'{v:.6f}' for v in r['S'])})")
    print(f"Jacobi sinodico = {r['c_syn']:.10f} ; Jacobi inercial = {r['c_in']:.10f} ; diferencia = {r['dc']:.2e}")
    print(f"Velocidad inercial de la Luna (quieta en el marco sinodico) = {r['v_luna']:.4f} km/s")
    assert r['ida_vuelta'] < 1e-9 and r['rt'] < 1e-9
    assert r['err_omega'] < 1e-9
    assert r['dc'] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
