#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C07: resonancia de Laplace de Io, Europa y Ganimedes con periodos publicados.

Datos consultados el 2026-11-09 (NASA/NSSDC, ficha de satelites jovianos): semiejes (1e3 km) y periodos siderales (dias):
Io 421.8 / 1.769138; Europa 671.1 / 3.551181; Ganimedes 1070.4 / 7.154553; Calisto 1882.7 / 16.689017.
(GM)_J nominal de la IAU 2015 (Resolucion B3), texto del PDF extraido el 2026-11-09: 1.2668653e17 m^3 s^-2.
Sistema de referencia: orbitas keplerianas medias alrededor de Jupiter; las fichas no dan la incertidumbre de los periodos: se rotula.
Modelo: movimientos medios n = 360/P (grados/dia); relacion de Laplace n1 - 3 n2 + 2 n3 = 0; razones de periodos y racional mas cercano.
Via 2: semieje de la tercera ley de Kepler con (GM)_J frente al semieje de la ficha. Las resonancias son un resultado de la dinamica (no se simulan aqui).
Tolerancias: |n1 - 3 n2 + 2 n3| < 1e-3 grados/dia; semiejes de Kepler frente a la ficha < 0.5 %.
"""
from __future__ import annotations
import math, platform
from fractions import Fraction

GM_J = 1.2668653e17
SAT = [("Io", 421.8e6, 1.769138), ("Europa", 671.1e6, 3.551181), ("Ganimedes", 1070.4e6, 7.154553), ("Calisto", 1882.7e6, 16.689017)]


def calcular():
    n = [360.0 / p for _, _, p in SAT]
    laplace = n[0] - 3.0 * n[1] + 2.0 * n[2]
    razones = [SAT[i + 1][2] / SAT[i][2] for i in range(3)]
    cercanos = []
    for x in razones:
        fr = Fraction(x).limit_denominator(5)
        cercanos.append((fr, x / float(fr) - 1.0))
    kepler = []
    for nombre, a, p in SAT:
        ak = (GM_J * (p * 86400.0) ** 2 / (4.0 * math.pi ** 2)) ** (1.0 / 3.0)
        kepler.append((nombre, a, ak, ak / a - 1.0))
    return dict(n=n, laplace=laplace, razones=razones, cercanos=cercanos, kepler=kepler,
                amax_ratio=[(SAT[i + 1][1] / SAT[i][1]) for i in range(3)], r23=2.0 ** (2.0 / 3.0))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print("Datos: ficha NASA/NSSDC de satelites jovianos (consulta 2026-11-09); sin incertidumbre publicada en la ficha")
    print(f"{'satelite':>10} {'P [d]':>10} {'n [grados/d]':>14} {'a ficha [km]':>13} {'a Kepler [km]':>14} {'dif.':>9}")
    for (nm, a, p), nn, (_, _, ak, d) in zip(SAT, r["n"], r["kepler"]):
        print(f"{nm:>10} {p:10.6f} {nn:14.6f} {a / 1e3:13.1f} {ak / 1e3:14.1f} {d:9.2e}")
    print(f"Relacion de Laplace n1 - 3 n2 + 2 n3 = {r['laplace']:.3e} grados/dia")
    for (a, b), x, (fr, d) in zip([("Io", "Europa"), ("Europa", "Ganimedes"), ("Ganimedes", "Calisto")], r["razones"], r["cercanos"]):
        print(f"P({b})/P({a}) = {x:.6f} ; racional mas cercano (den. <= 5) = {fr} ; desviacion relativa = {d:+.2e}")
    print(f"Razon de semiejes de una resonancia 2:1 = 2^(2/3) = {r['r23']:.5f} ; a(Europa)/a(Io) de la ficha = {r['amax_ratio'][0]:.5f}")
    assert abs(r["laplace"]) < 1e-3
    assert all(abs(d) < 0.5e-2 for _, _, _, d in r["kepler"])
    assert r["cercanos"][0][0] == 2 and r["cercanos"][1][0] == 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
