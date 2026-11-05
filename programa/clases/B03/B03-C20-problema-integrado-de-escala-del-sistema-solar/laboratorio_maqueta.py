#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C20: tabla de una maqueta a escala del Sistema Solar con verificaciones cruzadas.

Datos PUBLICADOS (NASA Planetary Fact Sheets: semiejes en 1e6 km, radios medios volumétricos en km y
períodos en d; Sun Fact Sheet: radio 695 700 km); 1 au = 149 597 870 700 m y c = 299 792 458 m/s (SI).
Modelo: escala de longitudes única, distancia modelo = distancia real / FACTOR, con el factor fijado
por el requisito 1 au = 10 m. Supuestos: órbitas circulares de radio igual al semieje; cuerpos esféricos.
Validez: maqueta didáctica, no efemérides. Tolerancias: razones conservadas a 1e-12; Kepler a 1,5 %.
"""
from __future__ import annotations

import platform

AU_M = 149_597_870_700
C = 299_792_458
MODELO_1AU_M = 10.0                      # requisito: 1 au = 10 m en la maqueta
FACTOR = AU_M / MODELO_1AU_M             # longitud real / longitud modelo
SITIO_M = 350.0                          # requisito: la maqueta cabe en 350 m
CUERPOS = {  # a [1e6 km], radio [km], T [d]
    "Mercurio": (57.909, 2439.7, 87.969), "Venus": (108.210, 6051.8, 224.701), "Tierra": (149.598, 6371.0, 365.256),
    "Marte": (227.956, 3389.5, 686.980), "Júpiter": (778.479, 69911.0, 4332.589),
    "Saturno": (1432.041, 58232.0, 10755.699), "Urano": (2867.043, 25362.0, 30685.400),
    "Neptuno": (4514.953, 24622.0, 60189.018),
}
R_SOL_KM = 695_700.0


def a_modelo_m(longitud_km: float) -> float:
    return longitud_km * 1000.0 / FACTOR


def pruebas() -> None:
    assert abs(a_modelo_m(AU_M / 1000) - MODELO_1AU_M) < 1e-9                   # 1 au -> 10 m
    nep = a_modelo_m(CUERPOS["Neptuno"][0] * 1e6)
    assert nep < SITIO_M, nep                                                     # cumple el requisito del sitio
    for n, (a, r, t) in CUERPOS.items():                                          # las razones se conservan
        real = (a * 1e6) / R_SOL_KM
        mod = a_modelo_m(a * 1e6) / a_modelo_m(R_SOL_KM)
        assert abs(real - mod) / real < 1e-12, n
        au, anios = a * 1e6 * 1000 / AU_M, t / 365.256
        assert abs(anios ** 2 / au ** 3 - 1) < 0.015, n                           # Kepler como control de datos
    assert abs(CUERPOS["Neptuno"][0] * 1e9 / AU_M - 30.18) < 0.01                 # 30,18 au publicado en la ficha de razones


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    print(f"Factor de escala: 1 : {FACTOR:.4e} (1 au = {MODELO_1AU_M:.0f} m)")
    print(f"Sol: diámetro modelo = {a_modelo_m(2 * R_SOL_KM) * 100:.2f} cm")
    print(f"{'Cuerpo':9s} {'d modelo [m]':>13s} {'diámetro [mm]':>14s} {'luz real [min]':>15s}")
    for n, (a, r, t) in CUERPOS.items():
        luz_min = a * 1e9 / C / 60
        print(f"{n:9s} {a_modelo_m(a * 1e6):13.2f} {a_modelo_m(2 * r) * 1000:14.3f} {luz_min:15.2f}")
    print(f"Neptuno a {a_modelo_m(CUERPOS['Neptuno'][0] * 1e6):.1f} m del Sol; el sitio mide {SITIO_M:.0f} m")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
