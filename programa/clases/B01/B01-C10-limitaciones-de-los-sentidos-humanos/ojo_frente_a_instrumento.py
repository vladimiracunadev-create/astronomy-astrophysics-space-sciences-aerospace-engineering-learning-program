#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C10: ¿qué distingue un ojo frente a un instrumento sencillo?

Datos: distancia media Tierra–Luna 384 400 km y radio lunar 1 737,4 km (NASA Moon Fact
Sheet, PUBLICADOS); pupila de 7 mm y telescopio de 100 mm: valores HIPOTÉTICOS (supuestos
de la clase, no medidos); λ = 550 nm (referencia en el visible, 380–700 nm según NASA).
Modelo: límite de difracción de Rayleigh θ = 1,22 λ/D; capacidad de captar luz ∝ D²;
magnitud: 5 magnitudes = factor 100 (definición de la escala).
Supuestos: apertura circular; sin turbulencia ni defectos ópticos; el ojo real queda por
encima del límite de difracción por otras causas, que no se modelan. Dominio de validez:
estimación de cota inferior de resolución. Tolerancias: coeficiente 1,22 frente al cero de
Airy (3,8317/π) al 0,3 %; razón de áreas exacta.
"""

from __future__ import annotations

import math
import platform
import sys

LAMBDA = 550e-9          # m (referencia en el visible)
D_OJO = 0.007            # m, hipotético (pupila dilatada)
D_TEL = 0.100            # m, hipotético
R_LUNA_KM = 1737.4       # km (NASA)
DIST_LUNA_KM = 384_400   # km (NASA, semieje mayor)
ARCSEC = math.pi / (180 * 3600)


def rayleigh(lam: float, d: float) -> float:
    return 1.22 * lam / d


def pruebas() -> None:
    assert abs(1.22 - 3.8317059702 / math.pi) / 1.22 < 3e-3        # cero de Airy: 3,8317/π = 1,2197
    assert abs(rayleigh(550e-9, 0.1) - 6.71e-6) < 1e-8              # caso analítico a mano
    assert abs((D_TEL / D_OJO) ** 2 - 204.08) < 0.01                # razón de áreas
    assert abs(2.5 * math.log10(100) - 5.0) < 1e-12                 # 5 mag = factor 100


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    for nombre, d in (("ojo (7 mm, hipot.)", D_OJO), ("telescopio (100 mm, hipot.)", D_TEL)):
        th = rayleigh(LAMBDA, d)
        print(f"{nombre}: θ = {th:.3e} rad = {th / ARCSEC:.2f}″ ; detalle lunar ≈ {th * DIST_LUNA_KM:.1f} km")
    razon = (D_TEL / D_OJO) ** 2
    print(f"Luz captada: razón de áreas = {razon:.1f}×  → {2.5 * math.log10(razon):.2f} magnitudes más débil")
    diam = 2 * R_LUNA_KM / DIST_LUNA_KM
    print(f"Diámetro angular medio de la Luna: {diam / ARCSEC:.0f}″ ({math.degrees(diam):.3f}°)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
