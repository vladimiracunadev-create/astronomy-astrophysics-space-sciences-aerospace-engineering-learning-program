#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C12: presion de radiacion y aceleracion de una vela solar.

Datos CONSULTADOS (2026-11-10): c = 299792458 m/s y h = 6.62607015e-34 J s (exactas, NIST CODATA);
luminosidad solar 382.8e24 W y distancia media Tierra-Sol 149.6e6 km (NASA/NSSDC, Sun Fact Sheet);
area de la vela de LightSail 2: 32 m2 (resumenes de resultados de busqueda; mision de The Planetary Society, no de la NASA).
NO CONSULTADO (valor de manual): GM del Sol = 1.32712440e20 m3/s2 (solo para el numero de ligereza).
ILUSTRATIVOS (sinteticos): masa total de la nave 5 kg, reflectividad especular rho = 0.9 (el resto se absorbe; coeficiente de presion 1 + rho = 1.9), vela orientada de frente al Sol,
masa de una vela de 1000 m2 con 20 g/m2 (areal) para el numero de ligereza.
Modelo: irradiancia I = L/(4 pi d^2); presion para reflexion ideal P = 2 I/c; con reflectividad rho: P = (1 + rho) I/c; fuerza F = P A cos^2(alpha);
nave estatica frente al Sol, sin sombra ni arrastre. Segunda via: conteo de fotones de 550 nm (p = h/lambda, N = I/(h c/lambda)).
Tolerancia: presion por flujo de momento frente a conteo de fotones < 1e-12 relativa.
"""
from __future__ import annotations
import math, platform

C = 299792458.0
H = 6.62607015e-34
L_SUN = 382.8e24
AU = 149.6e9
GM_SOL = 1.32712440e20


def irradiancia(d):
    return L_SUN / (4 * math.pi * d ** 2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    i1 = irradiancia(AU)
    print(f"Irradiancia a 1 UA (calculada de L y d consultados) = {i1:.1f} W/m2")
    rho = 0.9
    area, masa = 32.0, 5.0
    p_abs, p_ref, p_mix = i1 / C, 2 * i1 / C, (1 + rho) * i1 / C
    print(f"Presion: absorbente {p_abs*1e6:.3f} uPa ; reflector ideal {p_ref*1e6:.3f} uPa ; rho = {rho} (ILUSTRATIVA) {p_mix*1e6:.3f} uPa")
    lam = 550e-9
    n_fot = i1 / (H * C / lam)
    p_fot = n_fot * (H / lam)
    assert abs(p_fot - p_abs) / p_abs < 1e-12
    print(f"Conteo de fotones (550 nm): {n_fot:.3e} fotones/(m2 s) -> presion absorbente {p_fot*1e6:.3f} uPa (coincide)")
    print(f"Vela de {area:.0f} m2 (area de LightSail 2, consultada) y {masa:.0f} kg (ILUSTRATIVOS):")
    print("  alpha [grados]   F [uN]    a [mm/s2]   dv por dia [m/s]")
    for alfa in (0.0, 30.0, 45.0, 60.0):
        f = p_mix * area * math.cos(math.radians(alfa)) ** 2
        a = f / masa
        print(f"  {alfa:>12.0f} {f*1e6:>9.2f} {a*1e3:>11.4f} {a*86400:>12.3f}")
    f0 = p_mix * area
    assert abs(f0 / 2 / (area * i1 / C) - (1 + rho) / 2) < 1e-12
    print("Distancia al Sol (alpha = 0):")
    for nombre, d in (("Venus 0.72 UA", 0.72 * AU), ("Tierra 1.00 UA", AU), ("Marte 1.52 UA", 1.52 * AU), ("Jupiter 5.20 UA", 5.20 * AU)):
        f = (1 + rho) * irradiancia(d) / C * area
        print(f"  {nombre:<16} F = {f*1e6:>7.2f} uN")
    # ley del inverso del cuadrado
    r = ((1 + rho) * irradiancia(2 * AU) / C) / p_mix
    assert abs(r - 0.25) < 1e-12
    print("F(2 UA)/F(1 UA) = 0.25 (inverso del cuadrado)")
    beta = (1 + rho) * i1 / C * 1000.0 * AU ** 2 / (GM_SOL * (20e-3 * 1000.0))
    print(f"Numero de ligereza de una vela de 1000 m2 y 20 g/m2 (areal): beta = F_rad/F_grav = {beta:.3f} (independiente de la distancia; GM no consultado)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
