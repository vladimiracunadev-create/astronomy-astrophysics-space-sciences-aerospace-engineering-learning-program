#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C04: densidad critica de Hill para el colapso de un cumulo de particulas y dust/gas necesario.

Datos consultados el 2026-11-09: G de NIST (CODATA 2022); (GM)_sol nominal de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): disco de B52-C02 (Sigma = 1e4 kg/m^2 (r/ua)^-1.5, T = 280 K (r/ua)^-0.5, mu = 2.3); cuerpos compactos de 1000 kg/m^3.
Sistema de referencia: problema restringido circular de tres cuerpos, estrella M en el origen, cumulo m a distancia D en orbita circular; SI.
Modelo: la densidad media dentro de la esfera de Hill R_H = D (m/(3M))^(1/3) es rho_H = 9 M/(4 pi D^3) = 9 Omega^2/(4 pi G), independiente de m.
Via 2: el punto L1 colineal del problema restringido se halla por biseccion y la densidad media dentro de |L1| se compara con rho_H.
Tolerancias: L1 numerico frente a R_H analitico 1e-3 relativo para m/M <= 1e-9; rho en L1 frente a rho_H 3e-3.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
UA = 1.495978707e11
MSOL = GM / G
MU, S1, P, T1 = 2.3, 1.0e4, 1.5, 280.0
RHO_CUERPO = 1000.0


def sigma(x): return S1 * x ** (-P)
def cs(x): return math.sqrt(K_B * T1 * x ** -0.5 / (MU * M_P))
def omega(x): return math.sqrt(GM / (x * UA) ** 3)
def rho_gas(x): return sigma(x) / (math.sqrt(2 * math.pi) * cs(x) / omega(x))
def rho_hill(x): return 9.0 * omega(x) ** 2 / (4.0 * math.pi * G)


def radio_hill(m, D):
    return D * (m / (3.0 * MSOL)) ** (1.0 / 3.0)


def l1_numerico(m, D):
    """Posicion del punto L1 (entre la estrella y el cumulo) en el problema restringido circular; devuelve D - x."""
    M = MSOL
    w2 = G * (M + m) / D ** 3
    xcm = m * D / (M + m)
    f = lambda x: G * M / x ** 2 - G * m / (D - x) ** 2 - w2 * (x - xcm)
    a, b = 0.5 * D, D * (1.0 - 1e-12)
    fa = f(a)
    for _ in range(200):
        c = 0.5 * (a + b)
        fc = f(c)
        if (fc > 0) == (fa > 0):
            a, fa = c, fc
        else:
            b = c
    return D - 0.5 * (a + b)


def calcular():
    D = 5.0 * UA
    filas = []
    for m in (1e15, 1e18, 4.19e18, 1e21):
        rh = radio_hill(m, D)
        rl1 = l1_numerico(m, D)
        rho_l1 = m / (4.0 / 3.0 * math.pi * rl1 ** 3)
        filas.append((m, rh, rl1, rho_l1))
    cuerpo = []
    for x in (1.0, 5.0, 30.0):
        zmid = rho_hill(x) / rho_gas(x)
        cuerpo.append((x, rho_gas(x), rho_hill(x), zmid))
    m100 = 4.0 / 3.0 * math.pi * (50e3) ** 3 * RHO_CUERPO
    return dict(D=D, filas=filas, cuerpo=cuerpo, m100=m100, rh100=radio_hill(m100, D), rho_h5=rho_hill(5.0),
                comp=RHO_CUERPO / rho_hill(5.0))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cumulo a D = 5 ua de una estrella de {MSOL:.4e} kg ; rho_H analitica = 9 Omega^2/(4 pi G) = {r['rho_h5']:.4e} kg/m^3")
    print(f"{'m [kg]':>10} {'R_H analitico [m]':>18} {'|L1| numerico [m]':>18} {'dif. rel.':>10} {'rho en L1 / rho_H':>18}")
    for m, rh, rl1, rho in r["filas"]:
        print(f"{m:10.3e} {rh:18.6e} {rl1:18.6e} {abs(rl1 / rh - 1):10.2e} {rho / r['rho_h5']:18.6f}")
    print(f"{'r [ua]':>8} {'rho_gas [kg/m^3]':>17} {'rho_H [kg/m^3]':>15} {'Z_mid necesario':>16}")
    for x, rg, rhh, z in r["cuerpo"]:
        print(f"{x:8.1f} {rg:17.4e} {rhh:15.4e} {z:16.1f}")
    print(f"Cuerpo compacto de 100 km de diametro (1000 kg/m^3): m = {r['m100']:.3e} kg ; R_H a 5 ua = {r['rh100'] / 1e3:.0f} km ; rho_cuerpo/rho_H = {r['comp']:.3e}")
    for m, rh, rl1, rho in r["filas"][:3]:
        assert abs(rl1 / rh - 1) < 1e-3, (m, rh, rl1)
        assert abs(rho / r["rho_h5"] - 1) < 3e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
