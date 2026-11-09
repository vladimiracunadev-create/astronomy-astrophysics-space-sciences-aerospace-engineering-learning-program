#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C03: del par (T_ef, L) al radio en el diagrama de Hertzsprung-Russell.

Datos: h, k_B, c, sigma (NIST CODATA 2022, consultados 2026-11-09); R_sol, L_sol y T_ef,sol
nominales (IAU 2015 B3, arXiv:1510.07674). Las cuatro estrellas de ejemplo son SINTETICAS
(valores ilustrativos), no objetos catalogados.
Modelo: cuerpo negro; L = 4 pi R^2 sigma T^4; sigma = 2 pi^5 k^4 /(15 h^3 c^2);
R/R_sol = (L/L_sol)^(1/2) (T_sol/T)^2; diferencia de magnitudes dM = -2.5 log10(L/L_sol).
Supuestos: la estrella irradia como cuerpo negro de temperatura efectiva T_ef.
Validez: definicion de T_ef; no describe el espectro real. Tolerancia: 1e-3 con los valores
nominales IAU (redondeos de la estimacion solar, no exactamente coherentes entre si) y
1e-9 en las identidades.
"""
from __future__ import annotations
import math
import platform
import sys

H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0
SIGMA = 2 * math.pi ** 5 * K ** 4 / (15 * H ** 3 * C ** 2)
R_SOL, L_SOL, T_SOL = 6.957e8, 3.828e26, 5772.0


def luminosidad(R, T):
    return 4 * math.pi * R * R * SIGMA * T ** 4


def radio_solar(l_rel, T):
    return math.sqrt(l_rel) * (T_SOL / T) ** 2


def dmag(l_rel):
    return -2.5 * math.log10(l_rel)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert abs(SIGMA / 5.670374419e-8 - 1) < 1e-9, "sigma derivada no coincide con NIST"
    l_chk = luminosidad(R_SOL, T_SOL)
    assert abs(l_chk / L_SOL - 1) < 1e-3, "L(R_sol,T_sol) no coincide con L_sol nominal"
    assert abs(dmag(100.0) + 5.0) < 1e-12, "Pogson: factor 100 = 5 magnitudes"
    assert abs(radio_solar(1.0, T_SOL) - 1.0) < 1e-12
    print(f"sigma = {SIGMA:.9e} W m-2 K-4 ; L(R_sol,T_sol) = {l_chk:.4e} W ({l_chk / L_SOL:.5f} L_sol nominal)")
    est = [("enana roja", 0.01, 3200.0), ("secuencia principal", 1.0, 5772.0),
           ("gigante roja", 100.0, 4500.0), ("enana blanca", 0.003, 12000.0)]
    for n, l, t in est:
        r = radio_solar(l, t)
        l_back = luminosidad(r * R_SOL, t) / L_SOL
        assert abs(l_back / l - 1) < 2e-3
        print(f"{n:20s} L={l:8.3f} L_sol T={t:7.0f} K -> R = {r:9.4f} R_sol ; dM = {dmag(l):+.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
