#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C08: cobertura de usuarios de un control segun su altura y probabilidad de diversidad en un grupo.

Datos consultados (2026-11-10; OMS, ficha «Disability», 7 de marzo de 2023): 1.3 mil millones de personas (16 %, 1 de cada 6) tienen una discapacidad significativa.
Burke, Howard y Kessler (2022): pista de traslado de 1.00 m y ventanas/puestos de trabajo como funciones del habitat.
SINTETICOS / ILUSTRATIVOS (no son datos de ninguna poblacion; la seleccion medica de tripulaciones y las normas de accesibilidad NO se consultaron): alcance comodo inferior y superior de usuarios
de pie (700 +- 50 y 1750 +- 90 mm) y sentados (450 +- 40 y 1300 +- 70 mm), mezcla 85 % de pie y 15 % sentados, independencia entre alcance inferior y superior.
Modelo: cobertura(h) = sum_g w_g P(low_g <= h) P(high_g >= h). Probabilidad de que un grupo de N personas incluya al menos una con discapacidad significativa:
1 - (1 - 0.16)^N (independencia; vale para poblacion general, NO para una tripulacion seleccionada).
Segunda via: simulacion de 100000 usuarios (semilla 109008); la cobertura simulada coincide con la analitica con tolerancia 0.01 en tres alturas.
Unidades: altura [mm].
"""
from __future__ import annotations
import platform, random
from statistics import NormalDist

P_DISC = 0.16  # OMS 2023
GRUPOS = {  # nombre: (peso, low_media, low_sd, high_media, high_sd) SINTETICOS
    "de pie": (0.85, 700.0, 50.0, 1750.0, 90.0),
    "sentado": (0.15, 450.0, 40.0, 1300.0, 70.0),
}


def cobertura(h):
    c = 0.0
    for w, lm, ls, hm, hs in GRUPOS.values():
        c += w * NormalDist(lm, ls).cdf(h) * (1 - NormalDist(hm, hs).cdf(h))
    return c


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Usuarios SINTETICOS (85 % de pie, 15 % sentados) ; 16 % de la OMS (2023) para la poblacion general")
    print("Probabilidad de al menos una persona con discapacidad significativa en un grupo (poblacion general):")
    for n in (2, 4, 10):
        print(f"   N = {n:2d}: {1 - (1 - P_DISC) ** n:.4f}")
    alturas = list(range(300, 2001, 10))
    cov = {h: cobertura(h) for h in alturas}
    mejor = max(cov, key=cov.get)
    print(f"Mejor altura de control = {mejor} mm con cobertura {cov[mejor]:.4f}")
    for u in (0.99, 0.95, 0.90):
        ok = [h for h in alturas if cov[h] >= u]
        print(f"   cobertura >= {u:.2f}: de {min(ok)} a {max(ok)} mm (ancho {max(ok) - min(ok)} mm)")
    print(" h [mm]  cobertura")
    for h in (500, 900, 1100, 1300, 1500, 1700):
        print(f"{h:7d} {cobertura(h):10.4f}")
    rng = random.Random(109008)
    N = 100000
    usuarios = []
    for _ in range(N):
        r = rng.random()
        w0 = GRUPOS["de pie"][0]
        g = GRUPOS["de pie"] if r < w0 else GRUPOS["sentado"]
        usuarios.append((rng.gauss(g[1], g[2]), rng.gauss(g[3], g[4])))
    for h in (900, 1300, 1500):
        sim = sum(1 for lo, hi in usuarios if lo <= h <= hi) / N
        print(f"Simulacion en h = {h}: {sim:.4f} frente a {cobertura(h):.4f}")
        assert abs(sim - cobertura(h)) < 0.01
    assert 0.5 < cov[mejor] <= 1.0
    # una altura solo para el grupo de pie cubre menos
    solo_pie = cobertura(1600)
    print(f"Control a 1600 mm (comodo para de pie): cobertura = {solo_pie:.4f}")
    assert solo_pie < cov[mejor]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
