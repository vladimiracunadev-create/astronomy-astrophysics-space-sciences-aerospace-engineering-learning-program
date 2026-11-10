#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C10: fase y transferencia de Hohmann para un encuentro coplanar entre orbitas circulares.

Datos CONSULTADOS (2026-11-10): GM_T = 398600.435507 km3/s2 (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): perseguidor circular a 300 km y objetivo circular a 400 km; fase inicial del objetivo 20 grados por delante.
Modelo: dos cuerpos con Tierra puntual; maniobras impulsivas. Fase requerida phi = pi - n_obj * t_transferencia (objetivo por delante).
Verificacion: integracion RK4 de dos cuerpos (paso 1 s) del perseguidor tras el primer impulso; distancia final al objetivo.
Tolerancias: distancia de llegada < 1 km con la fase exacta; el tiempo de espera es el modulo del angulo faltante dividido por (n_c - n_o).
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

MU_SI = GM_T * 1e9
RC = (R_T_EQ + 300.0) * 1e3
RT = (R_T_EQ + 400.0) * 1e3


def calcular(fase_ini_deg=20.0):
    nc = math.sqrt(MU_SI / RC ** 3)
    nt = math.sqrt(MU_SI / RT ** 3)
    at = 0.5 * (RC + RT)
    vc = math.sqrt(MU_SI / RC)
    v1 = math.sqrt(MU_SI * (2 / RC - 1 / at))
    v2 = math.sqrt(MU_SI * (2 / RT - 1 / at))
    vt = math.sqrt(MU_SI / RT)
    tt = math.pi * math.sqrt(at ** 3 / MU_SI)
    phi = math.pi - nt * tt
    espera = ((phi - math.radians(fase_ini_deg)) % (2 * math.pi)) / (nc - nt)
    # verificacion numerica: objetivo en angulo phi; perseguidor en (RC,0) con v1 tangencial
    s = (RC, 0.0, 0.0, 0.0, v1, 0.0)
    s = propagar_dt(kepler_rhs, s, tt, 1.0)
    ang_t = phi + nt * tt
    obj = (RT * math.cos(ang_t), RT * math.sin(ang_t), 0.0)
    dist = math.dist(s[:3], obj)
    dv_vel = math.hypot(s[3] - (-vt * math.sin(ang_t)), s[4] - vt * math.cos(ang_t))
    return dict(nc=nc, nt=nt, dv1=v1 - vc, dv2=vt - v2, tt=tt, phi=math.degrees(phi), espera=espera, dist=dist,
                vel_rel=dv_vel, sinodico=2 * math.pi / (nc - nt), dv_total=(v1 - vc) + (vt - v2),
                r_llegada=math.hypot(*s[:2]) - RT)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"n perseguidor = {r['nc']:.6e} rad/s ; n objetivo = {r['nt']:.6e} rad/s ; periodo sinodico = {r['sinodico'] / 3600:.3f} h")
    print(f"Hohmann 300 -> 400 km: dv1 = {r['dv1']:.2f} m/s ; dv2 = {r['dv2']:.2f} m/s ; total = {r['dv_total']:.2f} m/s ; t = {r['tt'] / 60:.2f} min")
    print(f"Fase requerida (objetivo por delante) = {r['phi']:.3f} grados ; espera desde 20 grados = {r['espera'] / 3600:.3f} h = {r['espera'] / 60:.1f} min")
    print(f"Llegada integrada: error de radio = {r['r_llegada']:.3f} m ; distancia al objetivo = {r['dist']:.3f} m ; velocidad relativa residual = {r['vel_rel']:.4f} m/s (antes del dv2 = {r['dv2']:.2f} m/s)")
    assert r['dist'] < 1000.0
    assert abs(r['vel_rel'] - r['dv2']) < 0.05
    assert 0 < r['phi'] < 180
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
