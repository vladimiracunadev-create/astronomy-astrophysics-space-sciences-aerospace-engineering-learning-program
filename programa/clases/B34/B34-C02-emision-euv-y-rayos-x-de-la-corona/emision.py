#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C02: longitud de onda del maximo de Wien, energia termica y medida de emision de un bucle.

Datos: h, c, k_B, e y la constante de Wien b = 2.897 771 955e-3 m K (NIST CODATA 2022), consultados 2026-11-09. Las temperaturas (1e6 a 3e7 K), la densidad (1e15 m^-3), las dimensiones del bucle (radio 1e6 m,
longitud 1e8 m), la perdida radiativa (3e-23 erg cm^3/s) y la dependencia n^2 T^(1/2) del bremsstrahlung son ILUSTRATIVAS (sinteticas); no se modela ningun instrumento.
Modelo: energia termica kT en eV y keV; maximo de Wien b/T de un cuerpo negro a esa temperatura (como referencia de escala: el plasma coronal es opticamente delgado y no es un cuerpo negro);
medida de emision EM = n^2 V y potencia radiada P = EM Lambda; cociente de la emision de bremsstrahlung integrada n^2 T^(1/2) entre dos temperaturas.
Supuestos: plasma isotermo y opticamente delgado. Validez: ordenes de magnitud.
Tolerancia: b/T frente a hc/(4.965114232 k T) a 1e-9.
"""
from __future__ import annotations
import math, platform, sys
H, C, KB, E = 6.62607015e-34, 299792458.0, 1.380649e-23, 1.602176634e-19
WIEN = 2.897771955e-3

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'T [K]':>9} {'kT [eV]':>10} {'maximo de Wien b/T [nm]':>25} {'banda':>14}")
    for t in (1e6, 3e6, 1e7, 3e7):
        lam = WIEN / t * 1e9
        ev = KB * t / E
        banda = "EUV/X blando" if lam > 1 else "rayos X"
        print(f"{t:9.1e} {ev:10.1f} {lam:25.4f} {banda:>14}")
        assert abs(WIEN / t / (H * C / (4.965114232 * KB * t)) - 1) < 1e-9
    r, l, n = 1e6, 1e8, 1e15
    v = math.pi * r * r * l
    em = n * n * v
    lam_rad = 3e-23 * 1e-7 * 1e-6
    print(f"volumen = {v:.3e} m3 ; EM = n^2 V = {em:.3e} m-3 = {em * 1e-6:.3e} cm-3 ; potencia radiada P = EM Lambda = {em * lam_rad:.3e} W")
    print(f"bremsstrahlung integrado (n^2 T^(1/2)): cociente 1e7 K / 1e6 K = {math.sqrt(10):.4f} para igual EM")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
