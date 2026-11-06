#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C08: conversion UTC -> TAI -> TT -> TDB.

Datos: tabla de segundos intercalares (TAI-UTC) del archivo Leap_Second.dat
del IERS (28 entradas, de 1972-01-01 a 2017-01-01; consultado 2026-11-05);
TT = TAI + 32.184 s (IERS TN36; NAIF); TDB - TT periodica segun el modelo
de NAIF/SPICE con K = 1.657e-3 s, EB = 1.671e-2, M0 = 6.239996 rad,
M1 = 1.99096871e-7 rad/s (precision ~3e-5 s, segun NAIF).
Modelo: TAI = UTC + (TAI-UTC)(fecha); TT = TAI + 32.184; TDB = TT + K sin E,
E = M + EB sin M, M = M0 + M1 t, con t = segundos de TT desde J2000.
Supuestos: UTC posterior a 1972-01-01 (con segundos enteros);
instantes durante un segundo intercalar no se tratan aqui (ver C09).
Validez: de 1972 a la expiracion de la tabla (2027-06-28 segun su cabecera).
Tolerancia: identidades exactas en las partes enteras; |TDB-TT| <= 1.7 ms.
"""
from __future__ import annotations
import math
import platform
import sys

# (MJD de inicio, TAI-UTC en s). Fuente: IERS Leap_Second.dat.
LEAP = [(41317, 10), (41499, 11), (41683, 12), (42048, 13), (42413, 14), (42778, 15),
        (43144, 16), (43509, 17), (43874, 18), (44239, 19), (44786, 20), (45151, 21),
        (45516, 22), (46247, 23), (47161, 24), (47892, 25), (48257, 26), (48804, 27),
        (49169, 28), (49534, 29), (50083, 30), (50630, 31), (51179, 32), (53736, 33),
        (54832, 34), (56109, 35), (57204, 36), (57754, 37)]
TT_MENOS_TAI = 32.184
K, EB, M0, M1 = 1.657e-3, 1.671e-2, 6.239996, 1.99096871e-7
MJD_J2000 = 51544.5      # JD 2451545.0 - 2400000.5


def mjd(y: int, mo: int, d: int) -> int:
    """MJD de las 0 h de una fecha gregoriana (algoritmo de Fliegel-Van Flandern)."""
    a = (14 - mo) // 12
    yy, mm = y + 4800 - a, mo + 12 * a - 3
    jdn = d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
    return jdn - 2400001      # JDN (mediodia) -> MJD de las 0 h


def tai_menos_utc(m: int) -> int:
    assert m >= LEAP[0][0], "UTC anterior a 1972: no definido aqui"
    val = LEAP[0][1]
    for mj, v in LEAP:
        if m >= mj:
            val = v
    return val


def tdb_menos_tt(t_seg_j2000: float) -> float:
    M = M0 + M1 * t_seg_j2000
    E = M + EB * math.sin(M)
    return K * math.sin(E)


def convertir(y, mo, d, h, mi, s):
    """Devuelve (TAI-UTC, TT-UTC, MJD_TT, TDB-TT) para un UTC (s entero o decimal)."""
    m = mjd(y, mo, d)
    dtai = tai_menos_utc(m)
    seg_utc = h * 3600 + mi * 60 + s
    mjd_tt = m + (seg_utc + dtai + TT_MENOS_TAI) / 86400.0
    t = (mjd_tt - MJD_J2000) * 86400.0
    return dtai, dtai + TT_MENOS_TAI, mjd_tt, tdb_menos_tt(t)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Pruebas de calendario y de tabla
    assert mjd(1972, 1, 1) == 41317 and mjd(2000, 1, 1) == 51544 and mjd(2017, 1, 1) == 57754
    assert all(mjd(*f) == m for f, m in [((1999, 1, 1), 51179), ((2006, 1, 1), 53736), ((2012, 7, 1), 56109)])
    assert tai_menos_utc(57753) == 36 and tai_menos_utc(57754) == 37
    # J2000: 2000-01-01 12:00:00 UTC
    dtai, dtt, mjd_tt, dtdb = convertir(2000, 1, 1, 12, 0, 0)
    print(f"2000-01-01 12:00:00 UTC: TAI-UTC={dtai} s, TT-UTC={dtt:.3f} s, "
          f"TT desde J2000 = {(mjd_tt - MJD_J2000) * 86400:.3f} s, TDB-TT = {dtdb * 1e3:+.4f} ms")
    assert dtai == 32 and abs(dtt - 64.184) < 1e-12
    # 2020-12-01 00:00:00 UTC (TDB-UTC debe rondar 69.184 s: dato de NAIF)
    dtai, dtt, mjd_tt, dtdb = convertir(2020, 12, 1, 0, 0, 0)
    print(f"2020-12-01 00:00:00 UTC: TT-UTC={dtt:.3f} s, TDB-UTC={dtt + dtdb:.6f} s")
    assert dtai == 37 and abs((dtt + dtdb) - 69.184) < 2e-3
    # Amplitud maxima del termino periodico
    t_max = max(abs(tdb_menos_tt(k * 86400.0)) for k in range(0, 366 * 5))
    print(f"max |TDB-TT| en 5 anios = {t_max * 1e3:.4f} ms")
    assert t_max < 1.7e-3 and t_max > 1.5e-3
    # TT y TAI avanzan igual: dos instantes separados 1 dia UTC sin intercalar
    a = convertir(2020, 12, 1, 0, 0, 0)[2]
    b = convertir(2020, 12, 2, 0, 0, 0)[2]
    assert abs((b - a) * 86400 - 86400) < 1e-6
    # Un dia con segundo intercalar: 2016-12-31 -> 2017-01-01 dura 86401 s de TAI
    c = convertir(2016, 12, 31, 0, 0, 0)[2]
    d = convertir(2017, 1, 1, 0, 0, 0)[2]
    print(f"2016-12-31 -> 2017-01-01: {(d - c) * 86400:.3f} s de TT")
    assert abs((d - c) * 86400 - 86401) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
