#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C01: dónde sale el Sol y hacia dónde apunta una sombra.

Datos: SIMULADOS (calculados) para un lugar de latitud -30,0 y longitud -70,7 (valores
redondeados, no medidos). Modelo: Sol de baja precisión (astrolib_b08), sin refracción
salvo el criterio de orto/ocaso del USNO (centro del Sol a -0,8333 grados de altura).
Dominio: 1950-2050, latitudes entre los círculos polares. Tolerancia: 0,5 grados en acimut.
Prueba independiente: fórmula analítica cos(A) = sin(dec)/cos(lat) para el acimut del orto.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, altaz, jd_utc, lst_deg, pruebas_biblioteca, sun_radec  # noqa: E402

LAT, LON = -30.0, -70.7


def azimut_orto_analitico(dec: float, lat: float) -> float:
    """Acimut del orto (desde el norte hacia el este), sin refracción, para el centro del Sol."""
    return math.acos(math.sin(dec * D2R) / math.cos(lat * D2R)) / D2R


def azimut_orto_numerico(y: int, m: int, d: int) -> tuple[float, float]:
    """Busca, en UT, el instante en que la altura del Sol cruza -0,8333 al subir y da su acimut."""
    prev = None
    for minuto in range(0, 24 * 60):
        jd = jd_utc(y, m, d) + minuto / 1440.0
        ra, dec, _ = sun_radec(jd)
        alt, az = altaz(ra, dec, LAT, lst_deg(jd, LON))
        if prev is not None and prev[0] < -0.8333 <= alt:
            return az, minuto / 60.0
        prev = (alt, az)
    raise RuntimeError("sin orto en ese día")


def sombra_mediodia(altura_vara_m: float, dec: float, lat: float) -> tuple[float, float]:
    """Altura del Sol al mediodía solar y largo de la sombra de una vara vertical."""
    alt = 90.0 - abs(lat - dec)
    return alt, altura_vara_m / math.tan(alt * D2R)


def pruebas() -> None:
    pruebas_biblioteca()
    for (y, m, d) in [(2025, 3, 20), (2025, 6, 21), (2025, 12, 21)]:
        az_num, _ = azimut_orto_numerico(y, m, d)
        _, dec, _ = sun_radec(jd_utc(y, m, d, 12))
        az_ana = azimut_orto_analitico(dec, LAT)
        assert abs(az_num - az_ana) < 0.5, (y, m, d, az_num, az_ana)   # el criterio de refracción desplaza < 0,5 grados
    alt, sombra = sombra_mediodia(1.0, 0.0, 0.0)
    assert abs(alt - 90.0) < 1e-12 and abs(sombra) < 1e-12              # Sol cenital: sombra nula


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Lugar: lat -30,0 lon -70,7 (datos SIMULADOS, baja precision)")
    for etiqueta, (y, m, d) in [("equinoccio de marzo", (2025, 3, 20)), ("solsticio de junio", (2025, 6, 21)),
                                ("solsticio de diciembre", (2025, 12, 21)), ("5 de noviembre", (2025, 11, 5))]:
        az, hut = azimut_orto_numerico(y, m, d)
        _, dec, _ = sun_radec(jd_utc(y, m, d, 12))
        alt, sombra = sombra_mediodia(1.0, dec, LAT)
        print(f"{etiqueta}: dec Sol {dec:+.2f} | acimut del orto {az:6.1f} (analitico {azimut_orto_analitico(dec, LAT):6.1f})"
              f" | altura al mediodia {alt:5.1f} | sombra de vara de 1 m: {sombra:.2f} m (hacia el sur)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
