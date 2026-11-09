#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C04: espejo concavo esferico y parabolico, foco paraxial y aberracion esferica longitudinal.

Datos: sin constantes fisicas. Radio de curvatura R = 2000 mm y aperturas de 100 a 400 mm son ILUSTRATIVOS.
Modelo: superficie conica z = c r^2 / (1 + sqrt(1 - (1+k) c^2 r^2)), c = 1/R; k = 0 esfera, k = -1 paraboloide. Rayos paralelos al eje que
inciden a la altura h se trazan EXACTAMENTE (interseccion con la conica y ley de reflexion) y se registra donde cortan el eje.
Segunda via analitica: esfera, x(h) = R (1 - 1/(2 cos t)) con sen t = h/R; paraboloide, todos los rayos cortan en R/2.
Supuestos: rayos meridionales, reflexion perfecta, sin difraccion. Validez: geometrica.
Tolerancia: trazado frente a formula cerrada 1e-9 mm; foco paraxial R/2 a 1e-6 mm; paraboloide, dispersion menor que 1e-9 mm.
"""
from __future__ import annotations
import math, platform, sys


def traza_eje(R, k, h):
    """Rayo paralelo al eje a la altura h (viaja hacia -z... usamos +z hacia el espejo). Devuelve z donde corta el eje tras reflejar.
    El vertice esta en z = 0 y el espejo es concavo hacia -z (el centro de curvatura esta en z = -R)."""
    c = -1.0 / R
    # resolver r = h: sag z0 = c h^2 / (1 + sqrt(1-(1+k) c^2 h^2))
    z0 = c * h * h / (1 + math.sqrt(1 - (1 + k) * c * c * h * h))
    # pendiente de la superficie dz/dr
    dz = c * h / math.sqrt(1 - (1 + k) * c * c * h * h)
    # normal (hacia el lado de incidencia, +z): n ~ (dz, -1) normalizada con signo
    nx, nz = dz, -1.0
    nn = math.hypot(nx, nz)
    nx, nz = nx / nn, nz / nn
    if nz < 0:
        nx, nz = -nx, -nz
    d = (0.0, -1.0)                 # el rayo viaja hacia -z
    kdn = d[0] * nx + d[1] * nz
    rx, rz = d[0] - 2 * kdn * nx, d[1] - 2 * kdn * nz
    t = -h / rx
    return z0 + t * rz


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = 2000.0
    print(f"R = {R:.0f} mm ; foco paraxial f = R/2 = {R/2:.1f} mm")
    print(f"{'h [mm]':>8} {'f/N':>6} {'esfera z_eje [mm]':>18} {'LSA esfera [mm]':>16} {'formula [mm]':>13} {'parab. [mm]':>12}")
    # con el vertice en 0 el foco esta en z = -R/2
    for h in (10, 50, 100, 150, 200):
        zs = traza_eje(R, 0.0, h)
        zp = traza_eje(R, -1.0, h)
        t = math.asin(h / R)
        z_formula = -R * (1 - 1 / (2 * math.cos(t)))
        # nota: con signo, el eje se corta a distancia R(1 - 1/(2 cos t)) del vertice
        lsa = (-zs) - R / 2
        lsa_f = R * (1 - 1 / (2 * math.cos(t))) - R / 2
        print(f"{h:8.0f} {R/2/(2*h):6.2f} {-zs:18.6f} {lsa:16.6f} {lsa_f:13.6f} {-zp:12.6f}")
        assert abs((-zs) - R * (1 - 1 / (2 * math.cos(t)))) < 1e-9
        assert abs((-zp) - R / 2) < 1e-9
    # limite paraxial
    z_par = -traza_eje(R, 0.0, 0.001)
    print(f"h = 0,001 mm : z = {z_par:.6f} mm")
    assert abs(z_par - R / 2) < 1e-6
    # aproximacion de tercer orden LSA ~ -h^2/(4R)
    h = 100.0
    t = math.asin(h / R)
    exacto = (R * (1 - 1 / (2 * math.cos(t)))) - R / 2
    aprox = -h * h / (4 * R)
    print(f"h = 100 mm : LSA exacta = {exacto:.6f} mm ; tercer orden -h^2/(4R) = {aprox:.6f} mm ; razon = {exacto/aprox:.4f}")
    assert abs(exacto / aprox - 1) < 0.01
    # tamano del disco de aberracion en el foco paraxial para una esfera f/5, D = 200 mm (h = 100)
    D = 200.0
    tsa = abs(exacto) * (D / 2) / (R / 2 - 0)  # angulo del rayo marginal ~ h/f
    print(f"disco de aberracion de la esfera f/5 (D = 200 mm) en el foco paraxial = {2*tsa*1e3/1:.1f} micras de diametro (aprox. de rayo marginal)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
