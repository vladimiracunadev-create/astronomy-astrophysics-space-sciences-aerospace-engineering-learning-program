#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C06: derivación implícita en la ecuación de Kepler.

Datos (PUBLICADOS): baricentro Tierra-Luna, elementos keplerianos 1800-2050 AD
de NASA/JPL "Approximate Positions of the Planets" (Tabla 1): a = 1.00000261 au,
e = 0.01671123. (GM)_sol nominal = 1.3271244e20 m3/s2 (IAU 2015 B3) y
1 au = 1.495978707e11 m (IERS TN36). Excentricidad 0.9: SINTÉTICA.
Modelo: M = E - e sin E (Kepler), derivada implícita dE/dM = 1/(1 - e cos E).
Se resuelve con la iteración de Newton descrita por JPL (E0 = M + e sin M;
dE = (M - (E - e sin E)) / (1 - e cos E), tol = 1e-6 grados; aquí se usa una parada más estricta, 1e-10 grados).
Supuestos: órbita kepleriana de dos cuerpos, M en radianes.
Validez: 0 <= e < 1. Tolerancias: residuo < 1e-10 rad; derivada analítica vs
cociente central < 1e-6 relativa.
"""
from __future__ import annotations
import math, platform, sys

GM_SOL = 1.3271244e20
AU = 1.495978707e11
A_EMB, E_EMB = 1.00000261, 0.01671123
TOL = math.radians(1e-6)


def kepler(M, e):
    E = M + e * math.sin(M)
    for n in range(1, 60):
        dM = M - (E - e * math.sin(E))
        dE = dM / (1 - e * math.cos(E))
        E += dE
        if abs(dE) <= TOL * 1e-4:
            return E, n
    raise SystemExit("PRUEBA FALLIDA: Kepler no converge")


def dE_dM(E, e):
    return 1.0 / (1.0 - e * math.cos(E))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    for e in (E_EMB, 0.9):
        print(f"\ne = {e}")
        print("  M [deg]   E [deg]   iter   residuo      dE/dM analít.   numérica")
        for Mdeg in (1, 30, 90, 180):
            M = math.radians(Mdeg)
            E, n = kepler(M, e)
            res = abs(M - (E - e * math.sin(E)))
            prueba(res < 1e-10, "residuo de Kepler")
            d_an = dE_dM(E, e)
            h = 1e-6
            d_nu = (kepler(M + h, e)[0] - kepler(M - h, e)[0]) / (2 * h)
            prueba(abs(d_an - d_nu) / d_an < 1e-6, "dE/dM analítica vs numérica")
            print(f"  {Mdeg:6d}  {math.degrees(E):8.4f}  {n:4d}  {res:9.2e}  {d_an:12.6f}  {d_nu:12.6f}")
    # pendiente de la elipse: dy/dx = -(b/a) cot E  ==  -b^2 x / (a^2 y)
    a, e = 1.0, 0.6
    b = a * math.sqrt(1 - e * e)
    E = math.radians(50)
    x, y = a * math.cos(E), b * math.sin(E)
    m1 = -(b / a) / math.tan(E)
    m2 = -(b**2 * x) / (a**2 * y)
    prueba(abs(m1 - m2) < 1e-12, "pendiente de la elipse")
    print(f"\nPendiente de la elipse e=0.6, E=50 deg: {m2:.6f} (paramétrica {m1:.6f})")
    # velocidad radial de la Tierra (modelo) en M = 90 deg
    a_m = A_EMB * AU
    n_med = math.sqrt(GM_SOL / a_m**3)
    E, _ = kepler(math.pi / 2, E_EMB)
    dEdt = n_med * dE_dM(E, E_EMB)
    r = a_m * (1 - E_EMB * math.cos(E))
    drdt = a_m * E_EMB * math.sin(E) * dEdt
    print(f"\nMovimiento medio n = {n_med:.6e} rad/s -> periodo {2*math.pi/n_med/86400:.3f} d")
    print(f"M = 90 deg: r = {r/AU:.6f} au; dr/dt = {drdt:.3f} m/s; dE/dt = {dEdt:.6e} rad/s")
    # razón de velocidades angulares perihelio/afelio = (1+e)^2/(1-e)^2 para la anomalía verdadera
    razon = ((1 + E_EMB) / (1 - E_EMB)) ** 2
    print(f"Razón de la velocidad angular real perihelio/afelio = {razon:.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
