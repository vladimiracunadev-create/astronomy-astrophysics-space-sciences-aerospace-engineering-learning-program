#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B129-C01: cobertura y redundancia de una red SINTETICA de observadores.

Todo SINTETICO e ILUSTRATIVO: numero de observadores N, longitudes equiespaciadas, ventana de oscuridad fija
(hora solar media local entre 21:00 y 05:00 = 8 h, sin estaciones ni latitud), probabilidad de cielo despejado p = 0.40
independiente por observador y noche. No procede de ninguna red real.
Modelo: en el instante UTC t el observador i esta en oscuridad si (t + lon_i/15) mod 24 esta en [21, 29).
Sea m(t) el numero de observadores en oscuridad. Con despeje independiente:
  P(>=1 observando) = 1 - (1-p)^m ;  P(>=2) = 1 - (1-p)^m - m p (1-p)^(m-1)  (>=2 permite triangular).
Segunda via: Monte Carlo (semilla 129) con 40000 noches; tolerancia: |analitico - MC| <= 4 sigma binomial.
Sistema de referencia: tiempo UTC en horas; longitud este positiva en grados.
"""
from __future__ import annotations
import math, platform, random

P_DESPEJE = 0.40
INI, DUR = 21.0, 8.0
PASO_MIN = 1  # minutos


def en_oscuridad(t_h, lon):
    loc = (t_h + lon / 15.0) % 24.0
    return (loc - INI) % 24.0 < DUR


def m_de_t(lons, t_h):
    return sum(1 for lo in lons if en_oscuridad(t_h, lo))


def analitico(lons, p):
    p1 = p2 = cub = 0.0
    n = 24 * 60 // PASO_MIN
    for k in range(n):
        t = k * PASO_MIN / 60.0
        m = m_de_t(lons, t)
        if m > 0:
            cub += 1
        p1 += 1 - (1 - p) ** m
        p2 += 1 - (1 - p) ** m - (m * p * (1 - p) ** (m - 1) if m > 0 else 0.0)
    return cub / n, p1 / n, p2 / n


def montecarlo(lons, p, noches, rng):
    c1 = c2 = 0
    for _ in range(noches):
        t = rng.random() * 24.0
        despejados = sum(1 for lo in lons if en_oscuridad(t, lo) and rng.random() < p)
        c1 += despejados >= 1
        c2 += despejados >= 2
    return c1 / noches, c2 / noches


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla 129")
    print(f"Red SINTETICA: p(despeje) = {P_DESPEJE}, oscuridad local {INI:.0f}:00-{(INI + DUR) % 24:.0f}:00 (8 h), longitudes equiespaciadas")
    print("  N  cobertura(m>=1)  P(>=1) anal  P(>=1) MC   P(>=2) anal  P(>=2) MC   dif/sigma")
    rng = random.Random(129)
    noches = 40000
    previo = (-1.0, -1.0)
    peor = 0.0
    for n in (2, 3, 6, 12, 24):
        lons = [360.0 * i / n for i in range(n)]
        cob, a1, a2 = analitico(lons, P_DESPEJE)
        m1, m2 = montecarlo(lons, P_DESPEJE, noches, rng)
        s1 = math.sqrt(a1 * (1 - a1) / noches)
        s2 = math.sqrt(max(a2 * (1 - a2), 1e-12) / noches)
        z = max(abs(a1 - m1) / s1, abs(a2 - m2) / s2)
        peor = max(peor, z)
        print(f"{n:3d}  {cob:14.4f}  {a1:11.4f} {m1:10.4f}  {a2:11.4f} {m2:10.4f}  {z:8.2f}")
        assert z <= 4.0, "el Monte Carlo no coincide con la via analitica"
        assert a1 >= previo[0] and a2 >= previo[1], "la cobertura debe crecer con N"
        previo = (a1, a2)
    # caso cerrado: N = 12 equiespaciados => m = 4 en todo instante
    lons12 = [30.0 * i for i in range(12)]
    ms = {m_de_t(lons12, k / 60.0) for k in range(24 * 60)}
    esperado = 1 - (1 - P_DESPEJE) ** 4
    _, a1, _ = analitico(lons12, P_DESPEJE)
    print(f"Caso cerrado N=12: m(t) = {sorted(ms)}; 1-(1-p)^4 = {esperado:.4f}; analitico = {a1:.4f}")
    assert ms == {4} and abs(a1 - esperado) < 1e-12
    # cuantos observadores para P(>=1) >= 0.95 y P(>=2) >= 0.80
    for n in range(3, 200):
        lons = [360.0 * i / n for i in range(n)]
        _, a1, a2 = analitico(lons, P_DESPEJE)
        if a1 >= 0.95 and a2 >= 0.80:
            print(f"Minimo N con P(>=1) >= 0.95 y P(>=2) >= 0.80: N = {n} (P1 = {a1:.4f}, P2 = {a2:.4f})")
            break
    print(f"Maxima desviacion MC-analitico = {peor:.2f} sigma. Pruebas superadas.")


if __name__ == "__main__":
    main()
