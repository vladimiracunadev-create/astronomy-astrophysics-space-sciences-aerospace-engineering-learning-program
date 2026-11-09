#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C06: corrimiento al rojo en un cohete acelerado frente a gh/c^2.

Datos: c exacta (NIST CODATA 2022, consultado 2026-11-09); GM y radio ecuatorial terrestres nominales
(IAU 2015 B3, arXiv:1510.07674, texto del PDF extraido el 2026-11-09): (GM)_E = 3.986004e14 m3/s2,
R_E = 6.3781e6 m. Resultado de la prueba con satelites Galileo: desviacion fraccional
(+0.19 +/- 2.48)e-5 del corrimiento (Delva et al., arXiv:1812.03711, resumen, consultado 2026-11-09).
La altura de la torre (100 m) y la aceleracion del cohete son valores ILUSTRATIVOS (sinteticos).
Modelo: emisor en el piso del cohete (aceleracion a), receptor a altura h; la luz tarda ~h/c, el
receptor gana velocidad beta = a h / c^2 y ve la frecuencia reducida por el Doppler relativista
exacto sqrt((1-beta)/(1+beta)) = exp(-atanh beta) (forma estable: con beta ~ 1e-16 la resta 1 - sqrt(...)
en coma flotante pierde las cifras). Principio de equivalencia: el mismo corrimiento a primer orden que el
gravitacional g h / c^2 con g = (GM)_E / R_E^2.
Supuestos: campo uniforme, h << R_E, orden mas bajo en h. Validez: h pequena.
Tolerancia: la desviacion relativa entre Doppler exacto y beta debe ser <= beta (segundo orden).
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
GM_E, R_E = 3.986004e14, 6.3781e6


def doppler(beta):
    """Cociente de frecuencias sqrt((1-beta)/(1+beta)) = exp(-atanh(beta))."""
    return math.exp(-math.atanh(beta))


def un_menos_doppler(beta):
    """1 - Doppler sin cancelacion catastrofica para beta ~ 1e-16."""
    return -math.expm1(-math.atanh(beta))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    g = GM_E / R_E ** 2
    print(f"g = (GM)_E / R_E^2 = {g:.4f} m/s2")
    for h in (1.0, 100.0, 1.0e4):
        beta = g * h / C ** 2
        exacto = un_menos_doppler(beta)
        print(f"h = {h:8.1f} m: g h / c^2 = {beta:.4e} ; 1 - Doppler exacto = {exacto:.4e} ; "
              f"diferencia relativa = {abs(exacto / beta - 1):.2e}")
        assert abs(exacto / beta - 1) <= beta + 1e-15, "no es de segundo orden"
    # caso con beta grande para ver que el primer orden es solo eso
    for beta in (1e-3, 1e-2, 0.1):
        ex = un_menos_doppler(beta)
        assert abs(ex / beta - 1) < beta
    # frecuencia relativa de un maser de 1.42040575 GHz (valor ilustrativo)
    f0 = 1.42040575e9
    h = 100.0
    df = f0 * g * h / C ** 2
    print(f"frecuencia de 1.42040575 GHz (ilustrativa) a {h:.0f} m de altura: cambio = {df:.3e} Hz")
    # cuota del experimento con Galileo
    sigma = 2.48e-5
    print(f"prueba Galileo: desviacion (+0.19 +/- 2.48)e-5 -> incertidumbre relativa 1 sigma = {sigma:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
