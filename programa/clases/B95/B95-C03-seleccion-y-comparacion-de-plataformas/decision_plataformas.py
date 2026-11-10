#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B95-C03: comparacion multicriterio y trazable de plataformas candidatas.

CONSULTADO (2026-11-10): CubeSat Design Specification Rev. 14.1, Tabla 1 (masa maxima tipica: 3U = 6.00 kg, 6U = 12.00 kg) y Tabla 2.
  El capitulo de plataformas completas del informe de la NASA no se pudo consultar.
ILUSTRATIVOS (sinteticos; NO son productos reales ni datos de fabricantes): cuatro plataformas A-D con sus atributos, los requisitos
  de la mision y los pesos de los criterios.
Modelo: (1) restricciones duras (masa de carga util >= requisito; potencia >= requisito); (2) puntaje ponderado tras normalizar
  cada criterio a [0, 1] (min-max; los criterios de coste se invierten); (3) sensibilidad: 20000 vectores de pesos Dirichlet(1,..,1) con
  semilla 20261110 y fraccion de veces que cada plataforma gana. Segunda via: normalizacion vectorial (norma euclidea) y comparacion del orden.
Unidades: kg, W, USD (ilustrativos), meses, adimensional.
"""
from __future__ import annotations
import math, platform, random

REQ_CARGA_KG = 1.2   # requisito de carga util, ILUSTRATIVO
REQ_POTENCIA_W = 8.0  # potencia orbital media disponible minima, ILUSTRATIVO
CRIT = ["carga util [kg]", "potencia [W]", "apuntamiento [arcsec, menos es mejor]", "coste [kUSD, menos es mejor]", "plazo [meses, menos es mejor]"]
MAS_ES_MEJOR = [True, True, False, False, False]
PESOS = [0.30, 0.20, 0.20, 0.20, 0.10]  # ILUSTRATIVOS
PLAT = {
    "A 3U": [1.0, 6.0, 60.0, 450.0, 8.0],
    "B 6U": [2.5, 14.0, 30.0, 900.0, 12.0],
    "C 6U": [2.0, 10.0, 15.0, 1300.0, 14.0],
    "D 12U": [5.0, 25.0, 20.0, 1800.0, 18.0],
}


def duras(v):
    return v[0] >= REQ_CARGA_KG and v[1] >= REQ_POTENCIA_W


def normaliza_minmax(nombres):
    cols = list(zip(*[PLAT[n] for n in nombres]))
    out = {n: [] for n in nombres}
    for j, col in enumerate(cols):
        lo, hi = min(col), max(col)
        for n in nombres:
            x = (PLAT[n][j] - lo) / (hi - lo) if hi > lo else 1.0
            out[n].append(x if MAS_ES_MEJOR[j] else 1.0 - x)
    return out


def normaliza_vectorial(nombres):
    cols = list(zip(*[PLAT[n] for n in nombres]))
    out = {n: [] for n in nombres}
    for j, col in enumerate(cols):
        nrm = math.sqrt(sum(c * c for c in col))
        for n in nombres:
            x = PLAT[n][j] / nrm
            out[n].append(x if MAS_ES_MEJOR[j] else -x)  # signo para criterios de coste
    return out


def puntajes(norm, pesos):
    return {n: sum(w * x for w, x in zip(pesos, v)) for n, v in norm.items()}


def ranking(p):
    return sorted(p, key=lambda n: -p[n])


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Requisitos ILUSTRATIVOS: carga util >= {REQ_CARGA_KG} kg ; potencia >= {REQ_POTENCIA_W} W")
    print("Plataformas candidatas SINTETICAS (no son productos reales):")
    aptos = []
    for n, v in PLAT.items():
        ok = duras(v)
        if ok:
            aptos.append(n)
        print(f"  {n:6s} carga {v[0]:4.1f} kg  P {v[1]:5.1f} W  apunt. {v[2]:5.1f}  coste {v[3]:7.1f} kUSD  plazo {v[4]:4.1f} m  -> {'pasa restricciones' if ok else 'DESCARTADA'}")
    print(f"Pesos ILUSTRATIVOS {PESOS} (suma = {sum(PESOS):.2f})")
    nm = normaliza_minmax(aptos)
    pm = puntajes(nm, PESOS)
    print("Puntaje ponderado (min-max):")
    for n in ranking(pm):
        print(f"  {n:6s} {pm[n]:.4f}")
    nv = normaliza_vectorial(aptos)
    pv = puntajes(nv, PESOS)
    print(f"Orden con normalizacion vectorial (segunda via): {ranking(pv)} ; orden min-max: {ranking(pm)}")
    # sensibilidad a los pesos
    rng = random.Random(20261110)
    ganas = {n: 0 for n in aptos}
    N = 20000
    for _ in range(N):
        g = [rng.gammavariate(1.0, 1.0) for _ in CRIT]
        s = sum(g)
        w = [x / s for x in g]
        p = puntajes(nm, w)
        ganas[ranking(p)[0]] += 1
    print(f"Sensibilidad: pesos Dirichlet(1,...,1), N = {N}, semilla 20261110; fraccion de victorias:")
    for n in aptos:
        print(f"  {n:6s} {ganas[n] / N:.4f}")
    # prueba de inversion de orden: quitar una plataforma y recalcular
    sin = [n for n in aptos if n != "D 12U"]
    nm2 = normaliza_minmax(sin)
    pm2 = puntajes(nm2, PESOS)
    print(f"Sin D 12U (min-max renormaliza): orden = {ranking(pm2)}  (antes: {ranking(pm)})")
    assert abs(sum(PESOS) - 1.0) < 1e-12 and abs(sum(ganas.values()) - N) == 0
    assert all(0.0 <= x <= 1.0 for v in nm.values() for x in v)
    assert "A 3U" not in aptos
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
