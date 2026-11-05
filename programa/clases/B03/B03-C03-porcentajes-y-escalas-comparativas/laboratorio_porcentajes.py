#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C03: porcentajes con la órbita de la Tierra y con la constante G.

Datos PUBLICADOS: NASA Earth Fact Sheet (perihelio 147,095, afelio 152,100 y semieje
149,598 millones de km; act. 15-nov-2024); G de CODATA 2014 (6,67408e-11, citada en la
resolución IAU 2015 B3) y de CODATA 2022 (6,67430e-11, NIST). Modelo: cambio porcentual
= (final - inicial)/inicial x 100. Supuestos: valores tal como se publican. Validez:
comparación de dos valores. Tolerancia: casos exactos, 1e-9 en las pruebas.
"""
from __future__ import annotations

import platform

PERI, AFE, SEMI = 147.095, 152.100, 149.598
G14, G22 = 6.67408, 6.67430
M_LUNA, M_TIERRA = 0.07346, 5.9722   # 1e24 kg


def cambio_pct(inicial: float, final: float) -> float:
    return (final - inicial) / inicial * 100


def pruebas() -> None:
    assert cambio_pct(100, 150) == 50.0
    assert abs(cambio_pct(150, 100) - (-100 / 3)) < 1e-9
    assert abs(100 * 1.5 * 0.5 - 75) < 1e-12        # +50 % y luego -50 % no devuelve el inicio
    assert abs(cambio_pct(200, 200)) == 0


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"(afelio - perihelio)/semieje = {(AFE - PERI) / SEMI * 100:.2f} %")
    print(f"Afelio respecto del perihelio: {cambio_pct(PERI, AFE):+.2f} %")
    print(f"Perihelio respecto del afelio: {cambio_pct(AFE, PERI):+.2f} %")
    print(f"Cambio de G entre CODATA 2014 y 2022: {cambio_pct(G14, G22):+.4f} %")
    print(f"Masa de la Luna como % de la Tierra: {M_LUNA / M_TIERRA * 100:.2f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
