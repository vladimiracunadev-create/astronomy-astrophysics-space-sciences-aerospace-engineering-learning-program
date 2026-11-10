#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C15: elipse relativa, deriva por diferencia de semieje y correccion en una formacion.

Datos CONSULTADOS (2026-11-10): GM_T = 398600.435507 km3/s2 (JPL, DE440), radio ecuatorial 6378.137 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos): orbita del jefe a 700 km de altitud; elipse relativa 2:1 de semieje menor rho = 250 m; diferencia de semieje mayor
delta_a = 1.0 m (error de insercion); correccion cada 10 orbitas con un impulso a lo largo de la trayectoria.
Modelo: HCW. Elipse libre: x = rho cos(nt), y = -2 rho sin(nt), con estado inicial (rho, 0, 0, 0, -2 n rho, 0). Un error de velocidad a lo largo de la
trayectoria dv_y = -n delta_a/2 (delta_a = diferencia de semieje mayor) desplaza el centro radial x_c = 4 x0 + 2 ydot0/n y produce una deriva
de -3 pi x_c por orbita en y (se verifica con HCW). La correccion es un impulso -dv_y.
Tolerancias: elipse libre cerrada < 1e-6 m tras una orbita; deriva HCW frente a formula < 1e-6 m.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

R0 = (R_T_EQ + 700.0) * 1e3
N = math.sqrt(GM_T * 1e9 / R0 ** 3)
P = 2 * math.pi / N
RHO = 250.0
DA = 1.0


def elipse(rho):
    return (rho, 0.0, 0.0, 0.0, -2 * N * rho, 0.0)


def calcular():
    s0 = elipse(RHO)
    s1 = hcw(N, P, s0)
    cierre = math.dist(s1[:3], s0[:3])
    # elipse con error de velocidad: delta_a -> dv_y = -n da / 2 ... (da = semieje del seguidor - jefe)
    dvy = -N * DA / 2           # una velocidad mas rapida a lo largo = semieje mayor; signo segun convencion
    s_e = (s0[0], s0[1], s0[2], s0[3], s0[4] + dvy, s0[5])
    # el desplazamiento del centro y la deriva por orbita
    s_orb = hcw(N, P, s_e)
    deriva = s_orb[1] - s_e[1]
    # centro de x: x_c = 4 x0 + 2 ydot0/n (constante del movimiento)
    xc = 4 * s_e[0] + 2 * s_e[4] / N
    deriva_teoria = -3 * math.pi * xc          # y_dot_drift = -3/2 n x_c por orbita -> -3 pi x_c
    # correccion: impulso dv_y de signo opuesto cada 10 orbitas
    dv_corr = -dvy
    s_c = (*s_e[:4], s_e[4] + dv_corr, s_e[5])
    deriva_corr = hcw(N, 10 * P, s_c)[1] - s_c[1]
    deriva_10 = hcw(N, 10 * P, s_e)[1] - s_e[1]
    dv_anio = abs(dv_corr) * (365.25 * 86400 / (10 * P))
    return dict(n=N, P=P / 60, cierre=cierre, xc=xc, deriva=deriva, deriva_teoria=deriva_teoria, dvy=dvy,
                deriva_10=deriva_10, deriva_corr=deriva_corr, dv_anio=dv_anio, rho=RHO,
                amp_y=max(abs(hcw(N, k * P / 360, s0)[1]) for k in range(361)))


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Jefe a 700 km: n = {r['n']:.6e} rad/s ; P = {r['P']:.3f} min")
    print(f"Elipse 2:1 con rho = {r['rho']:.0f} m: amplitud en y = {r['amp_y']:.2f} m ; cierre tras 1 orbita = {r['cierre']:.2e} m")
    print(f"Error de semieje {DA} m -> dv_y = {r['dvy'] * 1000:.4f} mm/s ; centro radial x_c = {r['xc']:.4f} m")
    print(f"Deriva en y por orbita (HCW) = {r['deriva']:.4f} m ; formula -3 pi x_c = {r['deriva_teoria']:.4f} m")
    print(f"Deriva en 10 orbitas = {r['deriva_10']:.3f} m ; con la correccion de dv = {-r['dvy'] * 1000:.4f} mm/s = {r['deriva_corr']:.2e} m")
    print(f"Presupuesto si se repite cada 10 orbitas durante un anio (ILUSTRATIVO) = {r['dv_anio']:.3f} m/s")
    assert r['cierre'] < 1e-6
    assert abs(r['deriva'] - r['deriva_teoria']) < 1e-6
    assert abs(r['deriva_corr']) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
