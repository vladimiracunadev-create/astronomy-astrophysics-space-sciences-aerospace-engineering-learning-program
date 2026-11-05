#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C11: altura del Sol al mediodía, duración del día y sombra de un gnomon.

Datos: oblicuidad de la Tierra 23,44° y rotación sidérea 23,9345 h (NASA Earth Fact Sheet,
PUBLICADOS); latitud de ejemplo −33,45° (lugar HIPOTÉTICO de la clase, no un sitio medido).
Modelo: declinación del Sol en los solsticios = ±oblicuidad y 0 en los equinoccios; altura
meridiana h = 90° − |φ − δ|; semiángulo horario cos H0 = −tan φ · tan δ (geometría esférica
sin refracción ni tamaño del disco solar); sombra L = altura_gnomon / tan(h).
Supuestos: Sol puntual, atmósfera ignorada, solo fechas de solsticio y equinoccio (no
interpola entre fechas). Dominio de validez: |φ| < 66,56° (sin sol de medianoche).
Tolerancias: casos analíticos a 1e-9 (equinoccio ecuador = 90°; día de 12 h con δ = 0).
"""

from __future__ import annotations

import math
import platform
import sys

OBLICUIDAD = 23.44      # grados (NASA)
ROT_SIDEREA_H = 23.9345  # horas (NASA)
LAT = -33.45            # grados, ejemplo hipotético


def altura_meridiana(lat: float, dec: float) -> float:
    return 90.0 - abs(lat - dec)


def duracion_dia_h(lat: float, dec: float) -> float:
    x = -math.tan(math.radians(lat)) * math.tan(math.radians(dec))
    assert -1.0 < x < 1.0, "sin salida/puesta (fuera del dominio)"
    return 2 * math.degrees(math.acos(x)) / 15.0


def sombra(gnomon_m: float, alt_deg: float) -> float:
    return gnomon_m / math.tan(math.radians(alt_deg))


def pruebas() -> None:
    assert abs(altura_meridiana(0.0, 0.0) - 90.0) < 1e-9        # ecuador en equinoccio
    assert abs(duracion_dia_h(45.0, 0.0) - 12.0) < 1e-9          # equinoccio: 12 h en cualquier latitud
    assert abs(duracion_dia_h(0.0, OBLICUIDAD) - 12.0) < 1e-9    # ecuador: 12 h todo el año
    assert abs(sombra(1.0, 45.0) - 1.0) < 1e-12                  # gnomon a 45°: sombra = altura
    assert abs(360.0 / ROT_SIDEREA_H - 15.0411) < 1e-3           # grados por hora sidérea


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    fechas = {"solsticio de diciembre": -OBLICUIDAD, "equinoccio": 0.0, "solsticio de junio": +OBLICUIDAD}
    for nombre, dec in fechas.items():
        h = altura_meridiana(LAT, dec)
        print(f"{nombre}: δ = {dec:+.2f}° | altura al mediodía = {h:.2f}° | "
              f"día = {duracion_dia_h(LAT, dec):.2f} h | sombra de 1 m = {sombra(1.0, h):.3f} m")
    print(f"Altura del polo celeste = |φ| = {abs(LAT):.2f}°")
    print(f"Giro aparente de las estrellas = {360.0 / ROT_SIDEREA_H:.4f}°/h ; del Sol medio = {360.0 / 24.0:.1f}°/h")
    print(f"Adelanto diario de las estrellas = {(24.0 - ROT_SIDEREA_H) * 60:.2f} min")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
