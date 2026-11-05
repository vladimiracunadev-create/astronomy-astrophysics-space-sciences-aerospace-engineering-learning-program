#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B08-C08: fase iluminada de la Luna a partir de la geometría Sol-Tierra-Luna.

Datos CALCULADOS por la NASA (SVS 5415, «Moon Phase and Libration, 2025», efeméride JPL DE421; archivo
mooninfo_2025.txt, consultado el 2026-11-05) copiados fila a fila: fecha UT, fase iluminada [%], distancia [km],
diámetro angular [arcsec], AR [h] y Dec [grados] (J2000). Radio de la Luna 1737,4 km y distancia media del Sol 149,6e6 km
(NASA Moon y Sun Fact Sheets). Modelo propio (SIMULADO): ángulo de fase i con tan(i) = R sen(psi)/(d - R cos(psi)),
fracción iluminada k = (1 + cos i)/2, con psi = elongación Luna-Sol, Sol de astrolib_b08.
Dominio: 2025 (precesión de J2000 a la fecha). Tolerancia: 0,3 puntos porcentuales de fase; 1 arcsec de diámetro.
Prueba independiente: los porcentajes de fase y diámetros publicados por la NASA, y el período sinódico
publicado (29,53 d) contra el promedio de 11 lunaciones leídas de la tabla.
"""
from __future__ import annotations

import math
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from astrolib_b08 import D2R, jd_utc, precesion_j2000, pruebas_biblioteca, separacion, sun_radec  # noqa: E402

R_LUNA_KM = 1737.4          # NASA Moon Fact Sheet (radio medio)
UA_KM = 149.6e6             # NASA Sun Fact Sheet (distancia media)

# (fecha UT, fase %, distancia km, diámetro arcsec, AR h, Dec grados) -- mooninfo_2025.txt
FILAS = [
    ("2025-03-29 11:00", 0.01, 358689, 1998.2, 0.503, 4.4159),
    ("2025-04-05 00:00", 49.12, 380413, 1884.1, 7.0489, 27.7182),
    ("2025-04-13 00:00", 99.96, 405996, 1765.3, 13.3484, -10.9831),
    ("2025-04-21 00:00", 50.82, 386467, 1854.6, 20.2121, -24.393),
    ("2025-09-21 19:00", 0.01, 397001, 1805.3, 11.8687, -0.1711),
    ("2025-11-05 12:00", 99.86, 357024, 2007.5, 2.5582, 19.484),
    ("2025-11-12 00:00", 52.54, 382513, 1873.7, 9.3307, 18.1791),
    ("2025-11-20 06:00", 0.18, 406685, 1762.4, 15.5989, -24.2297),
]
# Mínimos de fase (luna nueva, hora UT del mínimo horario) de la misma tabla, 2025
LUNAS_NUEVAS = ["2025-01-29 14", "2025-02-28 02", "2025-03-29 12", "2025-04-27 20", "2025-05-27 03", "2025-06-25 11",
                "2025-07-24 21", "2025-08-23 08", "2025-09-21 21", "2025-10-21 14", "2025-11-20 09", "2025-12-20 04"]
SINODICO_NASA_D = 29.53
# Extremos de libración 2025 leídos de la tabla (columnas Elon, Elat; grados)
LIB_LON = (-7.656, 8.024)
LIB_LAT = (-6.812, 6.853)


def fase_porcentaje(fecha: str, dist_km: float, ar_h: float, dec: float) -> tuple[float, float]:
    t = datetime.strptime(fecha, "%Y-%m-%d %H:%M")
    jd = jd_utc(t.year, t.month, t.day, t.hour, t.minute)
    ra_l, dec_l = precesion_j2000(ar_h * 15.0, dec, jd)
    ra_s, dec_s, r_ua = sun_radec(jd)
    psi = separacion(ra_l, dec_l, ra_s, dec_s) * D2R
    r_sol = r_ua * UA_KM
    i = math.atan2(r_sol * math.sin(psi), dist_km - r_sol * math.cos(psi))
    return 50.0 * (1.0 + math.cos(i)), psi / D2R


def diametro_arcsec(dist_km: float) -> float:
    return 2.0 * math.atan(R_LUNA_KM / dist_km) / D2R * 3600.0


def sinodico_promedio() -> float:
    ts = [datetime.strptime(s, "%Y-%m-%d %H") for s in LUNAS_NUEVAS]
    return (ts[-1] - ts[0]).total_seconds() / 86400.0 / (len(ts) - 1)


def pruebas() -> None:
    pruebas_biblioteca()
    for fecha, fase, dist, diam, ar, dec in FILAS:
        k, _ = fase_porcentaje(fecha, dist, ar, dec)
        assert abs(k - fase) < 0.3, (fecha, k, fase)
        assert abs(diametro_arcsec(dist) - diam) < 1.0, (fecha, diametro_arcsec(dist), diam)
    assert abs(sinodico_promedio() - SINODICO_NASA_D) < 0.1, sinodico_promedio()


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print("Fecha UT | fase NASA % | fase modelo % | elongacion Luna-Sol | diametro NASA / modelo (arcsec)")
    for fecha, fase, dist, diam, ar, dec in FILAS:
        k, psi = fase_porcentaje(fecha, dist, ar, dec)
        print(f"{fecha} | {fase:6.2f} | {k:6.2f} | {psi:6.1f} | {diam:7.1f} / {diametro_arcsec(dist):7.1f}")
    print(f"Periodo sinodico promedio (11 lunaciones de 2025): {sinodico_promedio():.2f} d | NASA: {SINODICO_NASA_D} d")
    print(f"Libracion 2025 (tabla NASA): longitud {LIB_LON[0]:+.1f}..{LIB_LON[1]:+.1f}, latitud {LIB_LAT[0]:+.1f}..{LIB_LAT[1]:+.1f} grados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
