#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B66-C03: umbral de movimiento de granos por el viento (tipo Bagnold) en cuatro entornos.

Datos consultados (2026-11-09; NASA/NSSDC): Tierra g = 9.820 m/s2, P = 1014 mb, T = 288 K; Marte g = 3.73 m/s2, densidad de superficie ~0.016 +/- 0.006 kg/m3;
Venus g = 8.87 m/s2, P = 92 bar, T = 737 K. Titan: g = GM/R^2 con GM = 8978.13710 km3/s2 y R = 2574.76 km (JPL SSD). Constante R = 8.314462618 J/(mol K) (NIST, CODATA 2022).
NO CONSULTADOS / ILUSTRATIVOS: masas molares del aire (28.97 g/mol), CO2 (44.01 g/mol) y N2 (28.01 g/mol); presion y temperatura de superficie de Titan (1.47e5 Pa, 94 K);
densidades de grano (2650, 3000, 3000 y 1000 kg/m3); diametro de grano 200 micras; coeficiente A = 0.1; factor de velocidad de lanzamiento k = 2.
Modelo: rho_aire = P M /(R T) (gas ideal; Marte se toma de la ficha); u*t = A sqrt((rho_p - rho) g D / rho); longitud de saltacion ILUSTRATIVA L = (k u*t)^2 / g.
Segunda via: parametro de Shields theta_t = rho u*t^2 /((rho_p - rho) g D) debe valer A^2 en todos los cuerpos.
Supuestos: grano esferico y liso, sin efectos de cohesion ni de numero de Reynolds de grano (que cambian A en la realidad), viento estacionario. Tolerancia: theta_t = A^2 con 1e-12.
"""
from __future__ import annotations
import math, platform

R_GAS = 8.314462618
D, A, K = 200e-6, 0.1, 2.0
G_TITAN = 8978.13710e9 / (2574.76e3) ** 2


def rho_gas(p, m, t):
    return p * m / (R_GAS * t)


ENTORNOS = {  # nombre: (g, rho_aire, rho_grano)
    "Tierra": (9.820, rho_gas(1014e2, 0.02897, 288.0), 2650.0),
    "Marte": (3.73, 0.016, 3000.0),
    "Venus": (8.87, rho_gas(92e5, 0.04401, 737.0), 3000.0),
    "Titan": (G_TITAN, rho_gas(1.47e5, 0.02801, 94.0), 1000.0),
}


def u_umbral(g, rho, rho_p, d=D):
    return A * math.sqrt((rho_p - rho) * g * d / rho)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Grano ILUSTRATIVO D = {D * 1e6:.0f} micras ; A = {A} ; k = {K}")
    print(" entorno  g [m/s2]  rho_aire [kg/m3]  rho_grano  u*t [m/s]  theta_t   L_salt [m]")
    res = {}
    for nom, (g, rho, rp) in ENTORNOS.items():
        u = u_umbral(g, rho, rp)
        th = rho * u * u / ((rp - rho) * g * D)
        res[nom] = (u, th)
        print(f"{nom:7s} {g:9.4f} {rho:15.4f} {rp:10.0f} {u:10.4f} {th:9.5f} {(K * u) ** 2 / g:11.4f}")
    for nom in ("Marte", "Venus", "Titan"):
        print(f"u*t({nom})/u*t(Tierra) = {res[nom][0] / res['Tierra'][0]:.3f}")
    for nom, (u, th) in res.items():
        assert abs(th - A * A) < 1e-12, nom
    assert res["Marte"][0] > 5 * res["Tierra"][0]
    assert res["Venus"][0] < res["Tierra"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
