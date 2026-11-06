#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C23: seguimiento de la deriva de un instrumento.

Datos: SINTETICOS (semilla fija). Un detector mide cada 3 meses durante 10
anios una fuente estable de referencia; la respuesta relativa (1 al inicio)
decae a -0.15 %/anio y tiene ruido de 0.30 % (1 sigma). Como orden de magnitud
real se cita que el manual del instrumento WFC3 de Hubble (STScI, Instrument
Handbook sec. 6.8, consultado 2026-11-05) da cambios de sensibilidad UVIS de
0.1-0.2 %/anio segun el filtro y 0.11 +/- 0.07 %/anio para F814W en UVIS2.
Modelo: r(t) = r0 (1 + m t) + ruido; ajuste lineal por minimos cuadrados con
u(m) = s / sqrt(Sxx) (como en C05); la correccion divide por (1 + m^ t).
Tiempo de deteccion: la deriva se detecta a 3 sigma cuando |m^| >= 3 u(m);
con muestreo cada dt y ruido sigma, u(m)^2 = 12 sigma^2 / (N^3 dt^2) aprox.
Supuestos: deriva lineal, ruido blanco gaussiano. Tolerancia: recta exacta
sin ruido a 1e-12; cobertura 1 sigma de la pendiente 0.683 +/- 5 errores
binomiales (R = 4000).
"""
from __future__ import annotations
import math
import platform
import random
import sys

M_V, SIG = -0.0015, 0.0030               # por anio ; relativo
DT = 0.25                                # anios


def ajuste(t, y):
    n = len(t)
    tm, ym = sum(t) / n, sum(y) / n
    sxx = sum((a - tm) ** 2 for a in t)
    m = sum((a - tm) * (b - ym) for a, b in zip(t, y)) / sxx
    c = ym - m * tm
    s = math.sqrt(sum((b - (c + m * a)) ** 2 for a, b in zip(t, y)) / (n - 2))
    return c, m, s, s / math.sqrt(sxx), sxx


def serie(T, rng, ruido=True):
    t = [i * DT for i in range(int(T / DT) + 1)]
    return t, [1.0 + M_V * a + (rng.gauss(0, SIG) if ruido else 0.0) for a in t]


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(23)
    # 1) sin ruido
    t, y = serie(10, rng, ruido=False)
    c, m, s, u, _ = ajuste(t, y)
    assert abs(m - M_V) < 1e-12 and abs(c - 1.0) < 1e-12 and s < 1e-12
    # 2) una serie de 10 anios
    t, y = serie(10, rng)
    c, m, s, u, sxx = ajuste(t, y)
    print(f"10 anios, N = {len(t)}: pendiente = {100*m:+.3f} +/- {100*u:.3f} %/anio (verdadera {100*M_V:+.2f}) ; s = {100*s:.3f} %")
    corr = [b / (c + m * a) for a, b in zip(t, y)]
    print(f"sin correccion, ultima medida = {y[-1]:.4f}; con correccion = {corr[-1]:.4f} (verdad 1.0000)")
    # 3) cobertura 1 sigma
    R = 4000
    dentro = 0
    for _ in range(R):
        tt, yy = serie(10, rng)
        _, mm, _, uu, _ = ajuste(tt, yy)
        dentro += abs(mm - M_V) <= uu
    f = dentro / R
    print(f"cobertura 1 sigma de la pendiente = {f:.3f} (esperada ~0.683)")
    assert abs(f - 0.683) < 5 * math.sqrt(0.683 * 0.317 / R) + 0.01
    # 4) tiempo de deteccion a 3 sigma de la deriva real
    print("T (anios)   N    u(m) (%/anio)   |m|/u(m)")
    detect = None
    for T in (1, 2, 3, 4, 5, 7, 10):
        tt, _ = serie(T, rng, ruido=False)
        n = len(tt)
        sxx_t = sum((a - sum(tt) / n) ** 2 for a in tt)
        um = SIG / math.sqrt(sxx_t)
        print(f"{T:6d}   {n:4d}   {100*um:12.4f}   {abs(M_V)/um:8.2f}")
        if detect is None and abs(M_V) / um >= 3:
            detect = T
    print(f"la deriva de 0.15 %/anio se detecta a 3 sigma con unos {detect} anios de datos")
    assert detect in (4, 5)
    # 5) formula aproximada de u(m)
    N, T = 41, 10.0
    um_aprox = math.sqrt(12 * SIG ** 2 / (N ** 3 * DT ** 2))
    tt, _ = serie(10, rng, ruido=False)
    um_ex = SIG / math.sqrt(sum((a - sum(tt) / len(tt)) ** 2 for a in tt))
    print(f"u(m): formula aprox = {100*um_aprox:.4f} ; exacta = {100*um_ex:.4f} %/anio")
    assert abs(um_aprox - um_ex) / um_ex < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
