#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C09: pupila de entrada y de salida, relieve ocular, obstruccion central y viñeteo por dos aperturas.

Datos: sin constantes fisicas. Objetivo f = 1000 mm con D = 100 mm, ocular f = 25 mm, obstruccion de 30 mm y aperturas de 50 mm separadas 300 mm son ILUSTRATIVOS.
Modelo: la pupila de salida es la imagen de la apertura limitante a traves de lo que sigue (ecuacion de lente delgada); la obstruccion central de razon e = d/D
retiene un area e^2; el viñeteo de dos aperturas circulares desplazadas se calcula con el area exacta de interseccion de dos circulos y se compara con una
simulacion Monte Carlo con semilla fija 20261109 (200 000 rayos).
Supuestos: lentes delgadas, aperturas circulares, haz uniforme. Validez: geometrica, sin difraccion.
Tolerancia: pupila de salida frente a D/M 1e-9 mm; area analitica frente a Monte Carlo 0,5 % de la apertura.
"""
from __future__ import annotations
import math, platform, random, sys


def interseccion(r1, r2, d):
    if d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a = r1 * r1 * math.acos((d * d + r1 * r1 - r2 * r2) / (2 * d * r1))
    b = r2 * r2 * math.acos((d * d + r2 * r2 - r1 * r1) / (2 * d * r2))
    c = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    return a + b - c


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    fo, D, fe = 1000.0, 100.0, 25.0
    s = fo + fe
    sp = s * fe / (s - fe)
    dsal = D * sp / s
    M = fo / fe
    print(f"pupila de salida: posicion s' = {sp:.4f} mm tras el ocular (relieve ocular) ; diametro = {dsal:.4f} mm ; D/M = {D/M:.4f} mm")
    assert abs(dsal - D / M) < 1e-9
    # obstruccion central
    d_obs = 30.0
    e = d_obs / D
    area_libre = 1 - e * e
    print(f"obstruccion central {d_obs:.0f} mm de {D:.0f} mm: razon e = {e:.3f} ; area util = {area_libre*100:.1f} % ; diametro equivalente = {D*math.sqrt(area_libre):.2f} mm")
    print(f"perdida de luz = {e*e*100:.1f} % ; magnitud perdida = {-2.5*math.log10(area_libre):.4f}")
    assert abs(area_libre - 0.91) < 1e-12
    # viñeteo: dos aperturas circulares de radio 25 separadas L = 300 mm, objeto fuera de eje
    r1 = r2 = 25.0
    L = 300.0
    rng = random.Random(20261109)
    print(f"viñeteo de dos aperturas de radio {r1:.0f} mm separadas {L:.0f} mm")
    print(f"{'angulo [deg]':>13} {'desplaz. [mm]':>14} {'area analitica [mm2]':>21} {'fraccion':>9} {'Monte Carlo':>12}")
    for ang in (0.0, 1.0, 2.0, 3.0, 4.0):
        off = L * math.tan(math.radians(ang))
        a = interseccion(r1, r2, off)
        frac = a / (math.pi * r1 * r1)
        n = 200_000
        dentro = 0
        for _ in range(n):
            x, y = rng.uniform(-r1, r1), rng.uniform(-r1, r1)
            if x * x + y * y <= r1 * r1 and (x - off) ** 2 + y * y <= r2 * r2:
                dentro += 1
        mc = dentro * (2 * r1) ** 2 / n / (math.pi * r1 * r1)
        print(f"{ang:13.1f} {off:14.3f} {a:21.3f} {frac:9.4f} {mc:12.4f}")
        assert abs(mc - frac) < 0.005
    # angulo al que se pierde la mitad de la luz (biseccion)
    lo, hi = 0.0, 45.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if interseccion(r1, r2, L * math.tan(math.radians(mid))) / (math.pi * r1 * r1) > 0.5:
            lo = mid
        else:
            hi = mid
    print(f"angulo con viñeteo del 50 % = {lo:.4f} deg ; campo sin viñeteo (desplazamiento 0) solo en el eje")
    assert 3.5 < lo < 4.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
