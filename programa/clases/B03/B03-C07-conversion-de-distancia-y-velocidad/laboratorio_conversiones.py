#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C07: conversión de distancia y velocidad con factores exactos.

Datos: factores EXACTOS del SI (1 au = 149 597 870 700 m; c = 299 792 458 m/s; 1 h = 3600 s;
1 km = 1000 m; BIPM SI 9.ª ed.) y valores PUBLICADOS de la NASA: velocidad orbital media de la
Luna 1,022 km/s y de la Tierra 29,78 km/s, velocidad de escape terrestre 11,186 km/s, semieje de
Neptuno 4514,953e6 km. Modelo: multiplicar por factores iguales a 1 (cociente de equivalencias).
Supuestos: ninguno físico; es aritmética de unidades. Tolerancia: 1e-12 relativa en las pruebas.
"""
from __future__ import annotations

import platform

M_POR_AU = 149_597_870_700          # m, exacto
C_MS = 299_792_458                  # m/s, exacto
S_POR_H = 3600
M_POR_KM = 1000


def km_a_au(km: float) -> float:
    return km * M_POR_KM / M_POR_AU


def kms_a_kmh(v: float) -> float:
    return v * S_POR_H


def tiempo_de_luz_s(m: float) -> float:
    return m / C_MS


def pruebas() -> None:
    assert abs(km_a_au(M_POR_AU / 1000) - 1) < 1e-12                   # ida y vuelta
    assert abs(kms_a_kmh(1) - 3600) < 1e-12 and abs(kms_a_kmh(1.0) / 3600 - 1) < 1e-12
    assert abs(tiempo_de_luz_s(M_POR_AU) - 499.00478384) < 1e-6        # tiempo de luz de 1 au
    assert abs(36 / 3.6 - 10) < 1e-12                                  # 36 km/h = 10 m/s
    assert abs(1000 * 1000 / M_POR_KM - 1000) < 1e-9


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"1 au / c = {tiempo_de_luz_s(M_POR_AU):.3f} s")
    print(f"Neptuno (semieje): {km_a_au(4514.953e6):.4f} au; luz: {tiempo_de_luz_s(4514.953e9):.0f} s = "
          f"{tiempo_de_luz_s(4514.953e9) / 3600:.2f} h")
    for nombre, v in (("Luna (órbita)", 1.022), ("Tierra (órbita)", 29.78), ("Escape terrestre", 11.186)):
        print(f"{nombre:17s}: {v} km/s = {kms_a_kmh(v):,.0f} km/h = {v * 1000:,.0f} m/s")
    print(f"Tierra: {29.78 * 86400 / (M_POR_AU / 1000):.5f} au/día")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
