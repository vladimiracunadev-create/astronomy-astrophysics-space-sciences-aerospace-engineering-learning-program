#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C14: cuentas básicas de un telescopio de iniciación.

Datos: configuraciones de EJEMPLO (apertura D, distancia focal F, oculares), no productos reales. Modelo (SIMULADO):
razón focal N = F/D; aumento M = F/f_ocular; pupila de salida = D/M; campo real = campo aparente/M (campo aparente SUPUESTO de
50 grados); poder separador teórico de Rayleigh theta = 1,22 lambda/D con lambda = 550 nm (ecuación estándar de difracción; se
desarrolla en B42 y no se verificó en una fuente de esta clase); tamaño lunar mínimo resuelto = distancia x theta, con la
distancia de la Luna del 5-nov-2025 a las 12:00 UT (357 024 km, NASA SVS 5415). Ganancia ideal en magnitud: 5 log10(D/7 mm) (C11).
Dominio: fuente puntual y óptica perfecta; la turbulencia y la calidad real empeoran el resultado. Tolerancia: 1e-9 en casos analíticos.
Prueba independiente: D = 100 mm, lambda = 550 nm -> 1,384 segundos de arco (cálculo a mano); un telescopio con M = 2 D(mm)
tiene pupila de salida de 0,5 mm; el aumento publicitario de 600x en 60 mm da pupila de salida de 0,1 mm.
"""
from __future__ import annotations

import math
import sys

LAMBDA_M = 550e-9
AFOV_DEG = 50.0
PUPILA_MM = 7.0
DIST_LUNA_KM = 357_024.0       # NASA SVS 5415, 2025-11-05 12:00 UT
ARCSEC = 180.0 / math.pi * 3600.0


def razon_focal(f_mm: float, d_mm: float) -> float:
    return f_mm / d_mm


def aumento(f_mm: float, f_ocular_mm: float) -> float:
    return f_mm / f_ocular_mm


def pupila_salida_mm(d_mm: float, m: float) -> float:
    return d_mm / m


def campo_real_deg(m: float) -> float:
    return AFOV_DEG / m


def rayleigh_arcsec(d_mm: float) -> float:
    return 1.22 * LAMBDA_M / (d_mm * 1e-3) * ARCSEC


def tamano_lunar_km(d_mm: float) -> float:
    return DIST_LUNA_KM * rayleigh_arcsec(d_mm) / ARCSEC


def ganancia_mag(d_mm: float) -> float:
    return 5.0 * math.log10(d_mm / PUPILA_MM)


EJEMPLOS = {
    "refractor 70 mm f/10": (70.0, 700.0),
    "reflector 114 mm f/7,9": (114.0, 900.0),
    "Dobson 200 mm f/6": (200.0, 1200.0),
}


def pruebas() -> None:
    assert abs(rayleigh_arcsec(100.0) - 1.384) < 0.001, rayleigh_arcsec(100.0)
    assert abs(pupila_salida_mm(100.0, 200.0) - 0.5) < 1e-12                    # M = 2 D(mm)
    assert abs(pupila_salida_mm(60.0, 600.0) - 0.1) < 1e-12                     # el «600x» de 60 mm
    assert abs(razon_focal(1200.0, 200.0) - 6.0) < 1e-12
    assert abs(aumento(1200.0, 10.0) - 120.0) < 1e-12
    assert abs(ganancia_mag(70.0) - 5.0) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Configuraciones de EJEMPLO (SIMULADO). campo aparente supuesto 50 grados")
    for nombre, (d, f) in EJEMPLOS.items():
        print(f"{nombre}: F/D = {razon_focal(f, d):.1f} | Rayleigh {rayleigh_arcsec(d):.2f} arcsec | rasgo lunar minimo "
              f"{tamano_lunar_km(d):.1f} km | ganancia ideal +{ganancia_mag(d):.2f} mag")
        for fo in (25.0, 10.0):
            m = aumento(f, fo)
            print(f"   ocular {fo:4.0f} mm: M = {m:5.1f}x | pupila de salida {pupila_salida_mm(d, m):4.2f} mm | campo real {campo_real_deg(m):4.2f} grados")
    print("Aumento 600x en 60 mm: pupila de salida", f"{pupila_salida_mm(60.0, 600.0):.2f} mm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
