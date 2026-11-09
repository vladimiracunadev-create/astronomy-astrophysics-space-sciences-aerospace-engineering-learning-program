#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C08: indice de decaimiento del campo confinante, altura critica y energia de una prominencia que erupciona.

Datos: g_sol = GM_sol/R_sol^2 (UAI 2015 B3), consultados 2026-11-09. El perfil del campo externo B(h) = B_0 (1 + h/h_0)^-3 (dipolo de juguete), h_0 = 50 Mm, el indice critico n_c = 1.5
(valor de referencia ILUSTRATIVO, no consultado), la masa (1e12 kg), la altura inicial (30 Mm) y la velocidad (100 km/s) son ILUSTRATIVOS (sinteticos).
Modelo: indice de decaimiento n(h) = -d ln B/d ln h = 3 h/(h_0 + h) (analitico y por diferencias finitas centradas); altura critica h_c tal que n(h_c) = n_c (biseccion; analitica h_c = n_c h_0/(3 - n_c));
energia gravitatoria m g h (g constante sobre la escala) y cinetica m v^2/2 de la prominencia; velocidad de escape en la superficie para comparar.
Supuestos: g constante en la escala de la prominencia; el criterio de inestabilidad es una regla de umbral. Validez: ilustrativa.
Tolerancia: biseccion frente a la altura critica analitica a 1e-9; diferencia finita frente al analitico a 1e-6.
"""
from __future__ import annotations
import math, platform, sys
GM, R = 1.3271244e20, 6.957e8
H0, NC = 50e6, 1.5

def b(h):
    return (1 + h / H0) ** -3

def n_fd(h, d=1e3):
    return -(math.log(b(h + d)) - math.log(b(h - d))) / (math.log(h + d) - math.log(h - d))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'h [Mm]':>7} {'n analitico':>12} {'n diferencias finitas':>22}")
    for h in (10e6, 30e6, 50e6, 100e6, 200e6):
        an = 3 * h / (H0 + h)
        fd = n_fd(h)
        print(f"{h / 1e6:7.0f} {an:12.6f} {fd:22.6f}")
        assert abs(fd / an - 1) < 1e-6
    lo, hi = 1e6, 1e9
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if 3 * m / (H0 + m) < NC:
            lo = m
        else:
            hi = m
    hc = 0.5 * (lo + hi)
    ana = NC * H0 / (3 - NC)
    print(f"altura critica (n = {NC}): biseccion = {hc / 1e6:.6f} Mm ; analitica n_c h_0/(3 - n_c) = {ana / 1e6:.6f} Mm")
    assert abs(hc / ana - 1) < 1e-9
    g = GM / R ** 2
    m, h, v = 1e12, 30e6, 100e3
    print(f"g = {g:.2f} m/s2 ; masa 1e12 kg a {h / 1e6:.0f} Mm: energia potencial m g h = {m * g * h:.3e} J ; cinetica a {v / 1e3:.0f} km/s: {0.5 * m * v * v:.3e} J ; cociente cinetica/potencial = {0.5 * v * v / (g * h):.3f}")
    print(f"velocidad de escape en la superficie = {math.sqrt(2 * GM / R) / 1e3:.1f} km/s")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
