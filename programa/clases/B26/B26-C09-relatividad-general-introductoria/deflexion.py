#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C09: deflexion de la luz por el Sol con trazado de rayos en campo debil.

Datos: c exacta y G (NIST CODATA 2022, consultados 2026-11-09); GM_sol y R_sol nominales (IAU 2015 B3,
arXiv:1510.07674, texto del PDF extraido el 2026-11-09). El rayo pasa rasante al limbo (b = R_sol); la
distancia de partida (2000 b) es una eleccion numerica.
Modelo: en la aproximacion de campo debil la luz se propaga como en un medio de indice efectivo
n(r) = 1 + 2GM/(c^2 r) (metrica isotropa con g00 y g_ij perturbados). Ecuacion de rayos:
d(n dr/ds)/ds = grad n, con p = n dr/ds. Deflexion analitica: alfa = 4GM/(c^2 b). Con solo la
parte temporal (n = 1 + GM/(c^2 r), el "valor newtoniano") la deflexion es la mitad.
Supuestos: masa puntual, rayo en un plano, campo debil (GM/(c^2 b) << 1), sin refraccion de la corona.
Validez: b >> r_s. Tolerancia: 0.2 % entre el trazado de rayos y 4GM/(c^2 b) (parte del error es el
tramo no recorrido, de orden b/X).
"""
from __future__ import annotations
import math
import platform
import sys

C, G = 299792458.0, 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8


def rayo(k, b, X=2000.0, ds_rel=0.05):
    """Traza un rayo con n = 1 + k/r desde (-X b, b) hacia +x. Devuelve el angulo final (rad)."""
    x, y = -X * b, b
    px, py = 1.0 + k / math.hypot(x, y), 0.0

    def f(x, y, px, py):
        r = math.hypot(x, y)
        n = 1 + k / r
        pm = math.hypot(px, py)
        gn = -k / r ** 3
        return px / pm, py / pm, gn * x, gn * y

    while x < X * b:
        h = ds_rel * b if abs(x) < 20 * b else 20 * ds_rel * b * min(abs(x) / (20 * b), 20)
        k1 = f(x, y, px, py)
        k2 = f(x + h / 2 * k1[0], y + h / 2 * k1[1], px + h / 2 * k1[2], py + h / 2 * k1[3])
        k3 = f(x + h / 2 * k2[0], y + h / 2 * k2[1], px + h / 2 * k2[2], py + h / 2 * k2[3])
        k4 = f(x + h * k3[0], y + h * k3[1], px + h * k3[2], py + h * k3[3])
        x += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        y += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        px += h * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2]) / 6
        py += h * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3]) / 6
    return math.atan2(py, px)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    b = R_SOL
    alfa = 4 * GM_SOL / (C ** 2 * b)
    ang = rayo(2 * GM_SOL / C ** 2, b)
    ang_n = rayo(GM_SOL / C ** 2, b)
    arcsec = 180 / math.pi * 3600
    print(f"4GM/(c^2 b) = {alfa:.6e} rad = {alfa * arcsec:.4f} arcsec (b = R_sol)")
    print(f"trazado de rayos (n = 1 + 2GM/(c^2 r)) : alfa = {abs(ang):.6e} rad = {abs(ang) * arcsec:.4f} arcsec")
    print(f"trazado de rayos (n = 1 +  GM/(c^2 r)) : alfa = {abs(ang_n):.6e} rad = {abs(ang_n) * arcsec:.4f} arcsec (valor newtoniano)")
    assert abs(abs(ang) / alfa - 1) < 2e-3, "deflexion fuera del 0.2 %"
    assert abs(abs(ang_n) / (alfa / 2) - 1) < 2e-3, "la mitad no coincide"
    assert ang < 0, "la luz debe curvarse hacia el Sol"
    for fb in (2.0, 5.0):
        print(f"b = {fb:.0f} R_sol: alfa = {4 * GM_SOL / (C ** 2 * fb * R_SOL) * arcsec:.4f} arcsec (escala 1/b)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
