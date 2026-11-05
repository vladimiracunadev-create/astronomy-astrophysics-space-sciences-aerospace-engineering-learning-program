#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C16: tamaños y tiempos solares para observar con seguridad (SIN mirar el Sol).

Datos PUBLICADOS: NASA Sun Fact Sheet (act. 9-may-2024, consultada 2026-11-05): radio medio 695 700 km, distancia
media 149,6 millones de km, diámetro angular 1919 arcsec a 1 UA (rango 1887-1952), rotación sidérea 609,12 h a 16 grados de
latitud; NASA Earth Fact Sheet: período sidéreo de la Tierra 365,256 d. Estimación de SILSO (Royal Observatory of Belgium, SIDC,
https://www.sidc.be/SILSO/home, consultada 2026-11-05): número de manchas diario estimado (EISN) del 1 al 5 de noviembre de
2026: 33, 49, 45, 78, 100. Salidas CALCULADAS. Modelo: proyección de un disco (orificio) y rotación rígida a 16 grados.
Dominio: ejemplos de proyección sin óptica; nada de este programa sustituye un filtro certificado.
Tolerancias: 0,5 % en el diámetro de la imagen proyectada.
Prueba independiente: el diámetro angular se calcula de dos maneras (1919 arcsec publicado vs 2 R/D con radio y distancia
publicados) y deben coincidir dentro de 0,5 %; además, el período sinódico de rotación se deriva del sidéreo.
"""
from __future__ import annotations

import math
import sys

R_SOL_KM = 695_700.0
UA_KM = 149.6e6
DIAM_ANG_ARCSEC = 1919.0
ROT_SIDEREA_H = 609.12            # a 16 grados de latitud
ANIO_SIDEREO_D = 365.256
EISN = [33, 49, 45, 78, 100]       # SILSO, estimado, 1-5 nov 2026
ARCSEC = 180.0 / math.pi * 3600.0


def diametro_angular_arcsec() -> float:
    return 2.0 * R_SOL_KM / UA_KM * ARCSEC


def imagen_orificio_mm(distancia_m: float) -> float:
    """Diámetro de la imagen del Sol proyectada a una distancia (m) detrás de un orificio pequeño."""
    return distancia_m * 1000.0 * DIAM_ANG_ARCSEC / ARCSEC


def sinodico_rotacion_dias() -> float:
    sid = ROT_SIDEREA_H / 24.0
    return 1.0 / (1.0 / sid - 1.0 / ANIO_SIDEREO_D)


def transmitancia(od: float) -> float:
    """Transmitancia de un filtro de densidad óptica OD (relación física general; NO es un valor de la norma)."""
    return 10.0 ** (-od)


def pruebas() -> None:
    assert abs(diametro_angular_arcsec() - DIAM_ANG_ARCSEC) / DIAM_ANG_ARCSEC < 0.005, diametro_angular_arcsec()
    assert abs(imagen_orificio_mm(1.0) - 9.30) < 0.05, imagen_orificio_mm(1.0)
    assert abs(transmitancia(5.0) - 1e-5) < 1e-18
    s = sinodico_rotacion_dias()
    assert 26.0 < s < 29.0, s


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"Diametro angular: publicado {DIAM_ANG_ARCSEC:.0f} arcsec ({DIAM_ANG_ARCSEC / 3600:.4f} grados); calculado 2R/D: {diametro_angular_arcsec():.0f} arcsec")
    for d in (0.5, 1.0, 2.0, 3.0):
        print(f"Proyeccion con orificio a {d:.1f} m: imagen de {imagen_orificio_mm(d):.2f} mm")
    print(f"Rotacion solar a 16 grados: sidérea {ROT_SIDEREA_H / 24:.2f} d; sinódica (vista desde la Tierra) {sinodico_rotacion_dias():.2f} d")
    print(f"Un punto cruza la cara visible en ~{sinodico_rotacion_dias() / 2:.1f} d (media vuelta)")
    print(f"EISN (SILSO, estimado) 1-5 nov 2026: {EISN}; media {sum(EISN) / len(EISN):.1f}; maximo {max(EISN)}")
    print(f"Aritmetica de densidad optica (relacion general): OD 3 -> {transmitancia(3):.0e}; OD 5 -> {transmitancia(5):.0e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
