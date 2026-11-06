#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C04: unidades y constantes con astropy.

Datos: factor 1 lbf = 4.448222 N (NIST SP 811, Apéndice B.8, 7 cifras; no es
exacto en esa tabla) y 1 au, 1 pc, G y GM de la Tierra tal como los publica la
documentación de astropy.constants (G: CODATA 2022 según esa página). El
impulso de 100 lbf*s es un número SINTÉTICO de ejemplo.
Modelo: análisis dimensional y conversión; la comprobación es que el programa
detecta sumas de magnitudes incompatibles y que las conversiones coinciden con
cálculos manuales y con identidades exactas (1 pc = 648000/pi au).
Supuestos: se usa el conjunto de constantes por defecto de la versión de astropy
impresa abajo; otra versión puede traer otros valores.
Validez: demostración de conversión y de dimensiones.
Tolerancia: 1e-12 relativa en identidades exactas; 1e-6 relativa entre la
conversión manual con 4.448222 y la de astropy.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import astropy
import astropy.units as u
import astropy.constants as const
from astropy.units import UnitConversionError


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def cerca(a, b, tol):
    return abs(a - b) <= tol * abs(b)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  astropy {astropy.__version__}")

    # 1) Identidad exacta: 1 pc = 648000/pi au
    pc_en_au = (1 * u.pc).to(u.au).value
    print(f"1 pc = {pc_en_au:.9f} au (648000/pi = {648000/math.pi:.9f})")
    prueba(cerca(pc_en_au, 648000 / math.pi, 1e-12), "pc en au")

    # 2) Caso Mars Climate Orbiter (idea): impulso en lbf*s leído como N*s
    impulso_lbf_s = 100.0
    manual = impulso_lbf_s * 4.448222
    con_astropy = (impulso_lbf_s * u.imperial.lbf * u.s).to(u.N * u.s).value
    print(f"100 lbf*s = {con_astropy:.6f} N*s (manual con 4.448222: {manual:.6f}); "
          f"leerlo como N*s subestima el impulso en un factor {con_astropy/impulso_lbf_s:.4f}")
    prueba(cerca(manual, con_astropy, 1e-6), "lbf -> N")

    # 3) El programa detecta una suma incompatible
    try:
        _ = (5 * u.km) + (3 * u.s)
        prueba(False, "debía fallar km + s")
    except UnitConversionError as e:
        print(f"km + s -> UnitConversionError: {e}")
    try:
        (1000 * u.nm).to(u.Hz)
        prueba(False, "debía fallar nm -> Hz")
    except UnitConversionError:
        print("nm -> Hz sin equivalencia: UnitConversionError")
    f = (1000 * u.nm).to(u.THz, equivalencies=u.spectral())
    print(f"1000 nm con u.spectral() = {f:.3f}  (c/lambda = {299792458/1e-6/1e12:.3f} THz)")
    prueba(cerca(f.value, 299792458 / 1e-6 / 1e12, 1e-9), "espectral")

    # 4) Período orbital con unidades: T = 2 pi sqrt(a^3/GM)
    a = (6378.137 + 400.0) * u.km
    T = (2 * math.pi * np.sqrt(a**3 / const.GM_earth)).to(u.min)
    T_manual = 2 * math.pi * math.sqrt((a.to(u.m).value) ** 3 / 3.986004e14) / 60
    print(f"T(LEO 400 km) = {T:.4f} (manual {T_manual:.4f} min)")
    prueba(cerca(T.value, T_manual, 1e-9), "período con unidades")

    # 5) Constantes: G y c
    print(f"G = {const.G.value:.5e} {const.G.unit}, c = {const.c.value:.0f} {const.c.unit}, "
          f"GM_earth = {const.GM_earth.value:.6e} {const.GM_earth.unit}")
    prueba(cerca(const.c.value, 299792458.0, 1e-15), "c exacta")
    print(f"au = {const.au.value:.8e} m  (1 au = 149597870700 m: dif. relativa "
          f"{abs(const.au.value-149597870700)/149597870700:.1e})")

    # 6) Magnitud sin dimensión: ángulo pequeño
    theta = (1 * u.arcmin).to(u.rad)
    print(f"1 arcmin = {theta:.6e}; tamaño de 1' a 43 Mpc = {(43*u.Mpc*theta.value).to(u.kpc):.3f}")
    prueba(cerca(theta.value, math.pi / 10800, 1e-12), "arcmin")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
