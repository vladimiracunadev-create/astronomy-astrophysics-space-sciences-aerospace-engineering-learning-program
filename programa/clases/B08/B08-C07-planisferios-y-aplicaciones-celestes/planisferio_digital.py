#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C07: un planisferio hecho con tiempo sidéreo.

Un planisferio alinea fecha y hora para mostrar qué parte del cielo está sobre el horizonte. Aquí se reproduce
esa lógica: la ascensión recta que culmina es el tiempo sidéreo local, y un astro del ecuador celeste está sobre el
horizonte entre TSL-6 h y TSL+6 h. Datos SIMULADOS (calculados) para lat -30,0 y lon -70,7 (redondeadas).
Modelo: GMST IAU 1982 (astrolib_b08), sin refracción. Dominio: 1950-2050. Tolerancia: 0,01 h.
Prueba independiente: (1) GMST contra astropy (en astrolib_b08); (2) un astro con ascensión recta igual al TSL tiene ángulo
horario cero y altura 90-|lat-dec| (fórmula esférica de C04); (3) a TSL+6 h, un punto del ecuador celeste está en el horizonte (este u oeste).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import altaz, jd_utc, lst_deg, pruebas_biblioteca  # noqa: E402

LAT, LON = -30.0, -70.7


def ra_en_meridiano_h(y: int, m: int, d: int, hora_ut: float, lon: float = LON) -> float:
    return lst_deg(jd_utc(y, m, d, hora_ut), lon) / 15.0


def banda_ecuador(tsl_h: float) -> tuple[float, float]:
    """AR (h) de los puntos del ecuador celeste que están en el horizonte este y en el horizonte oeste.

    En el este (H = -6 h) la AR es TSL + 6 h; en el oeste (H = +6 h) es TSL - 6 h.
    """
    return (tsl_h + 6.0) % 24.0, (tsl_h - 6.0) % 24.0


def limite_circumpolar_dec(lat: float) -> float:
    return -(90.0 - abs(lat)) if lat < 0 else 90.0 - lat


def pruebas() -> None:
    pruebas_biblioteca()
    tsl = ra_en_meridiano_h(2025, 11, 5, 0.0)
    alt, _ = altaz(tsl * 15, -20.0, LAT, tsl * 15)            # ángulo horario cero
    assert abs(alt - (90.0 - abs(LAT + 20.0))) < 1e-9, alt
    este, oeste = banda_ecuador(tsl)
    for ar, az_esperado in ((este, 90.0), (oeste, 270.0)):    # el ecuador celeste toca el horizonte en el este y el oeste exactos
        alt_h, az_h = altaz(ar * 15, 0.0, LAT, tsl * 15)
        assert abs(alt_h) < 1e-9 and abs(az_h - az_esperado) < 1e-6, (ar, alt_h, az_h)
    assert abs(limite_circumpolar_dec(-30.0) + 60.0) < 1e-12


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Lat -30,0 lon -70,7 (SIMULADO). Fecha UT | TSL = AR en el meridiano | AR en el horizonte este / en el horizonte oeste (ecuador celeste)")
    for (y, m, d, h) in [(2025, 11, 5, 0.0), (2025, 11, 5, 4.0), (2025, 11, 5, 8.0), (2025, 11, 20, 0.0), (2025, 12, 5, 0.0)]:
        tsl = ra_en_meridiano_h(y, m, d, h)
        e, o = banda_ecuador(tsl)
        print(f"{y}-{m:02d}-{d:02d} {h:04.1f} UT | {tsl:6.3f} h | {e:5.2f} h / {o:5.2f} h")
    print(f"Circumpolares en lat -30: dec <= {limite_circumpolar_dec(-30.0):.0f}; no salen: dec > {-limite_circumpolar_dec(-30.0):.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
