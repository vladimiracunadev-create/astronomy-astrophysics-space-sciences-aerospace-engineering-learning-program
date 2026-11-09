#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C14: radio de Einstein, imagenes y magnificacion de una lente puntual y de una esfera isoterma.

Datos: G y c (NIST, CODATA 2022, 2026-11-09); GM_sol (IAU 2015 B3). Distancias angulares D_l = 1000,
D_s = 2000 y D_ls = 1200 Mpc, masa 1e11 Msol y dispersion 250 km/s: SINTETICAS/ILUSTRATIVAS
(no proceden de una cosmologia calculada ni de una lente observada).
Modelo: lente delgada, aproximacion de angulos pequenos. Masa puntual: beta = theta - theta_E^2/theta,
theta_E = sqrt(4 G M D_ls / (c^2 D_l D_s)); imagenes theta_pm = (beta pm sqrt(beta^2 + 4 theta_E^2))/2;
magnificacion total mu = (u^2 + 2)/(u sqrt(u^2 + 4)), u = beta/theta_E. SIS: theta_E = 4 pi (sigma/c)^2 D_ls/D_s.
Supuestos: lente axisimetrica, sin cizalla externa, sin retrasos temporales.
Validez: ordenes de magnitud; las galaxias reales no son puntuales ni perfectamente isotermas.
Masa proyectada de la SIS dentro de R: pi sigma^2 R/G. Tolerancias: 1e-9 (raices y identidad de masa), 1e-6 (magnificacion por derivada numerica).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
C = 299_792_458.0
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
MPC = 3.0856776e22
ARCSEC = math.pi / (180 * 3600)
DL, DS, DLS = 1000 * MPC, 2000 * MPC, 1200 * MPC


def theta_e_puntual(m_kg):
    return math.sqrt(4 * G * m_kg * DLS / (C ** 2 * DL * DS))


def theta_e_sis(sigma):
    return 4 * math.pi * (sigma / C) ** 2 * DLS / DS


def imagenes(beta, te):
    s = math.sqrt(beta * beta + 4 * te * te)
    return 0.5 * (beta + s), 0.5 * (beta - s)


def raiz_lente(beta, te, lado):
    """Resuelve beta = theta - te^2/theta por biseccion en el lado + o -."""
    f = lambda t: t - te * te / t - beta
    lo, hi = (te * 1e-6, 100 * te) if lado > 0 else (-100 * te, -te * 1e-6)
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if (f(lo) > 0) == (f(mid) > 0):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def mag_numerica(theta, te, h=1e-7):
    """mu = (theta/beta)(dtheta/dbeta) = (theta/beta) / (dbeta/dtheta) con derivada central."""
    beta = lambda t: t - te * te / t
    db = (beta(theta * (1 + h)) - beta(theta * (1 - h))) / (2 * theta * h)
    return (theta / beta(theta)) / db


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = 1e11 * M_SOL
    te = theta_e_puntual(m)
    for u in (0.1, 0.5, 1.0, 2.0):
        beta = u * te
        tp, tm = imagenes(beta, te)
        # Prueba 1: la ecuacion de la lente se cumple y la biseccion coincide con la forma cerrada
        assert abs(raiz_lente(beta, te, +1) / tp - 1) < 1e-9
        assert abs(raiz_lente(beta, te, -1) / tm - 1) < 1e-9
        # Prueba 2: magnificacion por derivada numerica frente a la forma cerrada
        mup, mum = mag_numerica(tp, te), mag_numerica(tm, te)
        total = abs(mup) + abs(mum)
        assert abs(total / ((u * u + 2) / (u * math.sqrt(u * u + 4))) - 1) < 1e-6
    # Prueba 3: la masa proyectada dentro del radio de Einstein de la SIS coincide con pi sigma^2 R/G
    # (cilindro; la masa esferica 3D es 2 sigma^2 R/G, un factor pi/2 menor)
    sigma = 250e3
    tes = theta_e_sis(sigma)
    m_e = C ** 2 / (4 * G) * tes ** 2 * DL * DS / DLS
    assert abs(m_e / (math.pi * sigma ** 2 * tes * DL / G) - 1) < 1e-9
    print(f"masa puntual 1e11 Msol: theta_E = {te / ARCSEC:.3f} arcsec ; R_E = {te * DL / MPC * 1e3:.2f} kpc")
    for u in (0.1, 0.5, 1.0, 2.0):
        mu_tot = (u * u + 2) / (u * math.sqrt(u * u + 4))
        tp, tm = imagenes(u * te, te)
        print(f"  u = {u:3.1f}: imagenes a {tp / te:+.3f} y {tm / te:+.3f} theta_E ; mu_total = {mu_tot:.2f}")
    print(f"SIS sigma = 250 km/s: theta_E = {tes / ARCSEC:.3f} arcsec ; R_E = {tes * DL / MPC * 1e3:.2f} kpc ; M(<R_E) = {m_e / M_SOL:.3e} Msol")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
