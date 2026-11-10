#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B100-C03: nivel de reposicion con revision periodica, demora y reserva de seguridad.

Politica de nivel maximo (R, S): cada R dias se revisa y se pide hasta S; el pedido llega L dias despues.
Intervalo de proteccion = R + L. S = mu*(R+L) + z*sigma*sqrt(R+L); reserva de seguridad = z*sigma*sqrt(R+L).
CONSULTADO (2026-11-10): periodo sinodico de Marte 779.94 d (NASA/NSSDC, ficha de Marte): ventana de salida cada ~780 d.
SINTETICOS (semilla 20261110): demanda diaria normal, media mu = 10 u/d, desviacion sigma = 3 u/d (truncada en 0, efecto despreciable);
casos: A = revision 30 d, demora 10 d; B = revision 780 d (ventana sinodica redondeada), demora 180 d (ilustrativa).
Nivel de servicio objetivo 95 % por ciclo (z = NormalDist().inv_cdf(0.95)). Se simulan 3000 ciclos por caso.
Segunda via: nivel de servicio analitico Phi(z) frente al simulado. Tolerancia: |simulado - 0.95| < 0.02.
"""
from __future__ import annotations
import math
import platform
import random
from statistics import NormalDist

SEMILLA = 20261110
MU, SIGMA = 10.0, 3.0
CICLOS = 3000


def politica(r, l, z):
    t = r + l
    ss = z * SIGMA * math.sqrt(t)
    return MU * t + ss, ss


def simular(r, l, s, rng):
    t = r + l
    sin_falta = 0
    for _ in range(CICLOS):
        d = 0.0
        for _ in range(t):
            d += max(0.0, rng.gauss(MU, SIGMA))
        if d <= s:
            sin_falta += 1
    return sin_falta / CICLOS


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar); semilla {SEMILLA}")
    z = NormalDist().inv_cdf(0.95)
    print(f"Demanda SINTETICA mu = {MU} u/d, sigma = {SIGMA} u/d ; z(95 %) = {z:.4f}")
    rng = random.Random(SEMILLA)
    resultados = {}
    print(" caso   R [d]  L [d]   S [u]   reserva [u]   servicio simulado   servicio analitico")
    for nom, r, l in (("A", 30, 10), ("B", 780, 180)):
        s, ss = politica(r, l, z)
        sim = simular(r, l, s, rng)
        ana = NormalDist().cdf(z)
        resultados[nom] = (s, ss, sim)
        print(f"  {nom}    {r:5d}  {l:4d}  {s:8.1f}  {ss:10.1f}   {sim * 100:15.2f} %   {ana * 100:14.2f} %")
    print(f"Cociente de nivel maximo B/A = {resultados['B'][0] / resultados['A'][0]:.2f}")
    print(f"Cociente de reserva de seguridad B/A = {resultados['B'][1] / resultados['A'][1]:.2f} ; "
          f"sqrt de los intervalos = {math.sqrt(960 / 40):.2f}")
    s_sin, _ = politica(780, 180, 0.0)
    sim0 = simular(780, 180, s_sin, random.Random(SEMILLA + 1))
    print(f"Sin reserva de seguridad (z = 0) el servicio simulado cae a {sim0 * 100:.1f} %")
    for nom in ("A", "B"):
        assert abs(resultados[nom][2] - 0.95) < 0.02
    assert abs(resultados["B"][1] / resultados["A"][1] - math.sqrt(960 / 40)) < 1e-9
    assert sim0 < 0.6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
