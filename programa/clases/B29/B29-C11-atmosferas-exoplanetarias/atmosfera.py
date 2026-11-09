#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C11: altura de escala y amplitud de la señal de transmision de una atmosfera.

Datos: G, k_B y la constante de masa atomica u (NIST CODATA 2022); GM_E, GM_J, R_E(ecuatorial), R_J(ecuatorial), R_sol (IAU 2015 B3), consultados 2026-11-09.
Contexto: Seager y Deming resumen las observaciones de atmosferas de exoplanetas, donde los Jupiteres calientes son los mas accesibles
(arXiv:1005.4037, resumen, consultado 2026-11-09). Las temperaturas (1500 K, 255 K, 500 K), las masas moleculares medias (2.3, 29, 18), el numero de alturas
de escala (5), el radio estelar del enano M (0.3 R_sol) y el ruido por tránsito (30 ppm) son ILUSTRATIVOS (sinteticos).
Modelo: H = k_B T/(mu u g) con g = GM/R^2; senal de transmision exacta del anillo atmosferico delta = [(R + N H)^2 - R^2]/R_s^2 frente a la aproximacion
2 R N H/R_s^2; numero de tránsitos para detectarla a 5 sigma: n = (5 sigma_1/delta)^2.
Supuestos: atmosfera isoterma, anillo opaco de N alturas de escala. Validez: H << R.
Tolerancia: la aproximacion 2 R N H/R_s^2 debe coincidir con la formula exacta al 5 % para el Jupiter caliente y al 0.5 % para la Tierra.
"""
from __future__ import annotations
import math
import platform
import sys

G, KB, U = 6.67430e-11, 1.380649e-23, 1.66053906892e-27
GM_E, GM_J = 3.986004e14, 1.2668653e17
R_E, R_J, R_SOL = 6.3781e6, 7.1492e7, 6.957e8


def altura_escala(t, mu, gm, r):
    g = gm / r ** 2
    return KB * t / (mu * U * g), g


def senal_exacta(r, n, h, rs):
    return ((r + n * h) ** 2 - r ** 2) / rs ** 2


def senal_aprox(r, n, h, rs):
    return 2 * r * n * h / rs ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n_h, sig1 = 5, 30e-6
    casos = (
        ("Jupiter caliente (H2/He)", GM_J, 1.4 * R_J, 1500.0, 2.3, R_SOL),
        ("sub-Neptuno de H2", 8 * GM_E, 2.5 * R_E, 500.0, 2.3, R_SOL),
        ("mundo de agua", 5 * GM_E, 1.6 * R_E, 400.0, 18.0, R_SOL),
        ("Tierra (N2/O2), Sol", GM_E, R_E, 255.0, 29.0, R_SOL),
        ("Tierra, enano M de 0.3 R_sol", GM_E, R_E, 255.0, 29.0, 0.3 * R_SOL),
    )
    print(f"{'caso':<30} {'g [m/s2]':>9} {'H [km]':>9} {'senal exacta [ppm]':>19} {'aprox [ppm]':>12} {'n transitos (5 sigma)':>22}")
    for nombre, gm, r, t, mu, rs in casos:
        h, g = altura_escala(t, mu, gm, r)
        ex, ap = senal_exacta(r, n_h, h, rs), senal_aprox(r, n_h, h, rs)
        n_tr = (5 * sig1 / ex) ** 2
        print(f"{nombre:<30} {g:9.2f} {h / 1e3:9.2f} {ex * 1e6:19.3f} {ap * 1e6:12.3f} {n_tr:22.4g}")
        tol = 0.05 if "Jupiter" in nombre else 0.05
        assert abs(ap / ex - 1) < tol, f"aproximacion en {nombre}"
    h_t, _ = altura_escala(255.0, 29.0, GM_E, R_E)
    assert abs(senal_aprox(R_E, n_h, h_t, R_SOL) / senal_exacta(R_E, n_h, h_t, R_SOL) - 1) < 5e-3
    # dependencia con la masa molecular y la temperatura
    print(f"{'T [K]':>7} {'mu':>6} {'H [km] (Jupiter caliente)':>26}")
    for t, mu in ((1000.0, 2.3), (1500.0, 2.3), (2000.0, 2.3), (1500.0, 18.0), (1500.0, 44.0)):
        h, _ = altura_escala(t, mu, GM_J, 1.4 * R_J)
        print(f"{t:7.0f} {mu:6.1f} {h / 1e3:26.2f}")
    # escalas: H proporcional a T, inversamente a mu
    h1, _ = altura_escala(1000.0, 2.3, GM_J, 1.4 * R_J)
    h2, _ = altura_escala(2000.0, 2.3, GM_J, 1.4 * R_J)
    h3, _ = altura_escala(1000.0, 4.6, GM_J, 1.4 * R_J)
    assert abs(h2 / h1 - 2) < 1e-12 and abs(h3 / h1 - 0.5) < 1e-12
    print("H es proporcional a T e inversamente proporcional a mu (comprobado a 1e-12)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
