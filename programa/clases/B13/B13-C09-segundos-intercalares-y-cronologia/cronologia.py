#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C09: fechas julianas y segundos intercalares.

Datos: tabla TAI-UTC del IERS (Leap_Second.dat, 28 entradas de 1972-01-01 a
2017-01-01; consultada 2026-11-05; vence segun su cabecera el 2027-06-28).
Modelo: calendario gregoriano <-> dia juliano modificado (MJD = JD - 2400000.5)
con enteros (Fliegel-Van Flandern). Cuenta continua de TAI desde 1972-01-01
00:00:00 UTC: tai = dias*86400 + segundos_del_dia + (TAI-UTC)(fecha) - 10.
Un instante 23:59:60 solo es valido si el dia siguiente tiene TAI-UTC una
unidad mayor.
Supuestos: UTC desde 1972; segundos enteros; sin dato de UT1.
Validez: hasta la expiracion de la tabla. Tolerancia: identidades exactas
(enteros).
"""
from __future__ import annotations
import datetime
import platform
import sys

LEAP = [(41317, 10), (41499, 11), (41683, 12), (42048, 13), (42413, 14), (42778, 15),
        (43144, 16), (43509, 17), (43874, 18), (44239, 19), (44786, 20), (45151, 21),
        (45516, 22), (46247, 23), (47161, 24), (47892, 25), (48257, 26), (48804, 27),
        (49169, 28), (49534, 29), (50083, 30), (50630, 31), (51179, 32), (53736, 33),
        (54832, 34), (56109, 35), (57204, 36), (57754, 37)]


def mjd(y, mo, d):
    a = (14 - mo) // 12
    yy, mm = y + 4800 - a, mo + 12 * a - 3
    jdn = d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
    return jdn - 2400001


def fecha(m):
    """Inversa de mjd(): devuelve (anio, mes, dia) de un MJD entero."""
    j = m + 2400001 + 32044
    g = j // 146097
    dg = j % 146097
    c = (dg // 36524 + 1) * 3 // 4
    dc = dg - c * 36524
    b = dc // 1461
    db = dc % 1461
    a = (db // 365 + 1) * 3 // 4
    da = db - a * 365
    y = g * 400 + c * 100 + b * 4 + a
    mth = (da * 5 + 308) // 153 - 2
    d = da - (mth + 4) * 153 // 5 + 122
    return y + (mth + 2) // 12 - 4800, (mth + 2) % 12 + 1, d + 1


def tai_menos_utc(m):
    v = None
    for mj, val in LEAP:
        if m >= mj:
            v = val
    if v is None:
        raise ValueError("UTC anterior a 1972")
    return v


def cuenta_tai(y, mo, d, h, mi, s):
    m = mjd(y, mo, d)
    if s == 60:
        if not (h == 23 and mi == 59 and tai_menos_utc(m + 1) == tai_menos_utc(m) + 1):
            raise ValueError("segundo intercalar no valido en esa fecha")
    return (m - 41317) * 86400 + h * 3600 + mi * 60 + s + tai_menos_utc(m) - 10


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Calendario
    assert mjd(1972, 1, 1) == 41317 and mjd(2000, 1, 1) == 51544
    assert mjd(2000, 1, 1) + 0.5 == 51544.5          # J2000 = JD 2451545.0
    for m in range(41317, 62000, 7):
        assert mjd(*fecha(m)) == m
    assert fecha(57754) == (2017, 1, 1)
    assert mjd(1900, 3, 1) - mjd(1900, 2, 28) == 1     # 1900 no es bisiesto
    assert mjd(2000, 3, 1) - mjd(2000, 2, 28) == 2     # 2000 si lo es
    for f, nombre in (((2000, 1, 1), "sabado"), ((2026, 11, 5), "jueves")):
        dia = datetime.date(*f).weekday()
        assert dia == (mjd(*f) + 2) % 7                # MJD 0 fue miercoles (=2 con lunes=0); contraste con datetime
        print(f"{f}: MJD {mjd(*f)} dia de la semana (0=lun) = {dia} ({nombre})")
    # Segundos intercalares
    a = cuenta_tai(2016, 12, 31, 23, 59, 59)
    b = cuenta_tai(2016, 12, 31, 23, 59, 60)
    c = cuenta_tai(2017, 1, 1, 0, 0, 0)
    print(f"23:59:59 -> 23:59:60 = {b - a} s ; 23:59:60 -> 00:00:00 = {c - b} s ; total {c - a} s")
    assert (b - a, c - b, c - a) == (1, 1, 2)
    dur = cuenta_tai(2017, 1, 1, 0, 0, 0) - cuenta_tai(2016, 12, 31, 0, 0, 0)
    print(f"duracion del dia 2016-12-31 = {dur} s")
    assert dur == 86401
    for malo in ((2016, 6, 30, 23, 59, 60), (2016, 12, 31, 12, 0, 60)):
        try:
            cuenta_tai(*malo)
        except ValueError:
            pass
        else:
            raise AssertionError("debio rechazar " + str(malo))
    # Total acumulado 1972-2017
    n = (cuenta_tai(2017, 1, 1, 0, 0, 0) - cuenta_tai(1972, 1, 1, 0, 0, 0)) - (mjd(2017, 1, 1) - mjd(1972, 1, 1)) * 86400
    print(f"segundos intercalares 1972-01-01 .. 2017-01-01 = {n}")
    assert n == 27
    # Resta ingenua frente a la correcta
    ingenua = (mjd(2017, 1, 1) - mjd(2016, 12, 31)) * 86400
    print(f"resta ingenua = {ingenua} s ; correcta = {dur} s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
