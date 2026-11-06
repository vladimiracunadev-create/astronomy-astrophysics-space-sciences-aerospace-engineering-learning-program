#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C10: angulo de rotacion terrestre (ERA) y culminacion.

Datos: definicion convencional del Earth Rotation Angle (IERS Conventions
2010, TN36, ec. 5.14/5.15, consultada 2026-11-05):
  ERA(Tu) = 2 pi (0.7790572732640 + 1.00273781191135448 Tu),
  Tu = JD(UT1) - 2451545.0 (dias).
Longitud de ejemplo: -70.4 grados (este positivo), valor sintetico de un
observatorio en el desierto de Atacama; ascension recta de ejemplo 12 h
medida respecto al origen del CIO (no se convierte desde un catalogo).
Modelo: angulo local = ERA + longitud este; angulo horario H = local - RA;
culminacion cuando H = 0 (mod 360 grados). Se usa UTC como aproximacion de
UT1 (|UT1-UTC| < 0.9 s, S1), error en ERA < 0.9 s * 15.04 "/s = 13.5".
Supuestos: sin movimiento polar ni nutacion; rotacion uniforme local.
Validez: instantes cercanos a la epoca; tolerancia 1e-9 rev en identidades.
"""
from __future__ import annotations
import math
import platform
import sys

THETA0 = 0.7790572732640        # rev
RATE = 1.00273781191135448      # rev por dia UT1
DIA = 86400.0


def era_rev(jd_ut1: float) -> float:
    tu = jd_ut1 - 2451545.0
    return (THETA0 + RATE * tu) % 1.0


def era_rev_estable(jd_ut1: float) -> float:
    """Forma equivalente (ec. 5.15): menos error de redondeo."""
    tu = jd_ut1 - 2451545.0
    frac = jd_ut1 % 1.0                      # fraccion del dia juliano (0.5 a las 0 h UT1)
    return (frac + THETA0 + (RATE - 1.0) * tu) % 1.0


def jd(y, mo, d, h=0, mi=0, s=0.0):
    a = (14 - mo) // 12
    yy, mm = y + 4800 - a, mo + 12 * a - 3
    jdn = d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
    return jdn - 0.5 + (h * 3600 + mi * 60 + s) / DIA


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dia_sideral = DIA / RATE
    print(f"dia sidereo = {dia_sideral:.4f} s = {dia_sideral/3600:.6f} h ; acortamiento {DIA - dia_sideral:.4f} s/dia")
    assert abs(dia_sideral - 86164.0989) < 1e-3
    # ERA en J2000.0 (2000-01-01 12:00 UT1)
    assert abs(era_rev(2451545.0) - THETA0) < 1e-15
    print(f"ERA(J2000) = {era_rev(2451545.0)*360:.6f} grados")
    # Despues de un dia sidereo exacto, el angulo vuelve al mismo valor
    j0 = jd(2026, 11, 5, 0, 0, 0)
    j1 = j0 + 1.0 / RATE
    assert abs(((era_rev(j1) - era_rev(j0) + 0.5) % 1.0) - 0.5) < 1e-9
    # Formas equivalentes 5.14 y 5.15
    for k in range(0, 20000, 997):
        assert abs(((era_rev(j0 + k / 7.0) - era_rev_estable(j0 + k / 7.0) + 0.5) % 1.0) - 0.5) < 1e-9
    # Avance por dia solar medio: 0.98564736 grados mas de lo que gira el reloj
    extra = (RATE - 1.0) * 360.0
    print(f"giro extra por dia solar = {extra:.6f} grados = {extra/15*3600:.3f} s de tiempo (el dia sidereo es mas corto)")
    # Culminacion de una fuente con RA = 180 grados en longitud -70.4
    lon, ra = -70.4, 180.0
    objetivo = (ra - lon) % 360.0 / 360.0           # ERA necesario (rev)
    # Buscar el instante UTC del 2026-11-05 en que ERA = objetivo (biseccion en el dia)
    lo, hi = j0, j0 + 1.0
    f = lambda j: ((era_rev(j) - objetivo + 0.5) % 1.0) - 0.5
    # el ERA crece ~1 rev/dia: hay un cruce; localizar por barrido y refinar
    prev = f(lo)
    t_sol = None
    for k in range(1, 2881):
        j = lo + k * (hi - lo) / 2880
        cur = f(j)
        if prev < 0 <= cur:
            a, b = j - (hi - lo) / 2880, j
            for _ in range(60):
                mdp = 0.5 * (a + b)
                if f(mdp) < 0:
                    a = mdp
                else:
                    b = mdp
            t_sol = 0.5 * (a + b)
            break
        prev = cur
    assert t_sol is not None
    hh = (t_sol - j0) * 24
    print(f"culminacion (RA=12h, lon=-70.4) el 2026-11-05 a las {int(hh):02d}:{int((hh%1)*60):02d}:{((hh*60)%1)*60:04.1f} UTC (aprox UT1)")
    # Comprobacion: ERA + lon = RA en ese instante
    assert abs((((era_rev(t_sol) * 360.0 + lon - ra) + 180.0) % 360.0) - 180.0) < 1e-6
    # Sensibilidad: 0.9 s de UT1-UTC = 13.5 segundos de arco
    print(f"0.9 s de UT1-UTC = {0.9*RATE*360/DIA*3600:.2f} segundos de arco")
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
