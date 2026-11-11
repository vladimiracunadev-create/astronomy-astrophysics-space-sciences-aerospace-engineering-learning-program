#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C03: posiciones orbitales y espectro como recursos limitados (regimenes de acceso SINTETICOS).

CONTENIDO EDUCATIVO: no es asesoria legal ni regulatoria.
CONSULTADO (2026-11-11): UIT, «ITU Radio Regulatory Framework for Space Services» (PDF creado 2018-01-10; hasta CMR-15) y presentacion de la Oficina de
Radiocomunicaciones «Orbit-Spectrum International Regulatory Framework» (PDF, metadatos 2021-05-11): el Articulo 44 de la Constitucion de la UIT dice que
las frecuencias y las orbitas asociadas, incluida la geoestacionaria, son recursos naturales limitados que deben usarse de forma racional, eficiente y
economica para que los paises tengan acceso equitativo; hay dos enfoques: coordinacion («primero en llegar, primero en ser servido», con coordinacion
antes del uso) y planificacion a priori (planes de los Apendices 30, 30A y 30B); la diligencia debida administrativa (Res. 49) busca evitar la reserva
de capacidad sin uso real, y una red sin la informacion completa a tiempo se cancela.
NO CONSULTADO: valores de GM, del periodo sideral y del radio ecuatorial (valores astronomicos estandar usados aqui), el texto del Reglamento y del Apendice 30B.
SINTETICO: 40 paises, 60 posiciones, demandas, capacidades y reclamos; separacion de 2 grados y eficiencia espectral de 2 bit/s/Hz (ilustrativas).
Sistema de referencia: orbita circular ecuatorial geocentrica; r en km, longitud orbital en grados. Semilla fija 120.
Tolerancias: r_GEO por dos vias a 1e-6 relativo; Gini por dos formulas a 1e-12.
"""
from __future__ import annotations
import math, platform, random

MU = 398600.4418          # km3/s2 (valor estandar, no consultado)
T_SID = 86164.0905        # s, dia sideral (no consultado)
R_EQ = 6378.137           # km (no consultado)


def r_geo():
    return (MU * (T_SID / (2 * math.pi)) ** 2) ** (1 / 3)


def periodo(r):
    return 2 * math.pi * math.sqrt(r ** 3 / MU)


def gini_a(x):
    n, m = len(x), sum(x) / len(x)
    return sum(abs(a - b) for a in x for b in x) / (2 * n * n * m)


def gini_b(x):
    s = sorted(x)
    n = len(s)
    return (2 * sum((i + 1) * v for i, v in enumerate(s)) / (n * sum(s))) - (n + 1) / n


def escenario(seed=120, n=40, slots=60):
    rng = random.Random(seed)
    want = [min(20, max(1, int(rng.paretovariate(1.2)))) for _ in range(n)]
    cap = [rng.lognormvariate(0, 1) for _ in range(n)]
    orden = sorted(range(n), key=lambda i: -cap[i])      # llegan primero los de mayor capacidad
    return want, orden


def fcfs(want, orden, slots, factor_reclamo=2):
    """Orden de llegada: cada pais reclama factor*demanda hasta agotar las posiciones."""
    a, resto = [0] * len(want), slots
    for i in orden:
        g = min(factor_reclamo * want[i], resto)
        a[i], resto = g, resto - g
    return a


def fcfs_con_diligencia(want, orden, slots):
    """Tras la diligencia debida: cada pais conserva min(reclamo, uso real); lo liberado se reparte de nuevo en orden de llegada."""
    a = [min(x, w) for x, w in zip(fcfs(want, orden, slots), want)]
    libre = slots - sum(a)
    for i in orden:
        g = min(want[i] - a[i], libre)
        a[i], libre = a[i] + g, libre - g
    return a


def plan(want, orden, slots):
    """Planificacion a priori: una posicion garantizada por pais; el resto por orden de llegada sobre la demanda residual."""
    a = [1] * len(want)
    libre = slots - len(want)
    for i in orden:
        g = min(want[i] - 1, libre)
        a[i], libre = a[i] + g, libre - g
    return a


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("RECURSOS LIMITADOS: Art. 44 UIT y regimenes consultados en documentos UIT 2018/2021 (consulta 2026-11-11); paises, demandas y capacidades SINTETICOS.")
    r = r_geo()
    lo, hi = 7000.0, 100000.0   # segunda via: biseccion sobre el periodo
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if periodo(mid) < T_SID else (lo, mid)
    r2 = (lo + hi) / 2
    v = math.sqrt(MU / r)
    t = 2 * math.pi * r / v
    print(f"Radio de la orbita geoestacionaria: {r:.2f} km (altitud sobre el ecuador {r - R_EQ:.2f} km); periodo recalculado {periodo(r):.4f} s")
    print(f"Verificacion: biseccion sobre el periodo y periodo por v=sqrt(mu/r) = {t:.4f} s ; diferencia relativa de r = {abs(r - r2) / r:.1e}")
    sep = 2.0
    print(f"Separacion de {sep} grados entre satelites: {2 * r * math.sin(math.radians(sep / 2)):.1f} km ; posiciones en 360 grados = {int(360 / sep)}")
    print(f"Capacidad ilustrativa de una posicion con 500 MHz y 2 bit/s/Hz: {500e6 * 2 / 1e9:.1f} Gbit/s")
    want, orden = escenario()
    S, N = 60, len(want)
    print(f"Escenario: {N} paises, {S} posiciones, demanda total = {sum(want)}, demanda maxima = {max(want)}")
    print("Regimen                          asignadas  paises con >=1  demanda no atendida  Gini")
    res = {}
    for nombre, a in (("orden de llegada (reclamo x2)", fcfs(want, orden, S)),
                      ("orden de llegada + diligencia", fcfs_con_diligencia(want, orden, S)),
                      ("plan a priori (1 por pais)", plan(want, orden, S))):
        res[nombre] = a
        ga, gb = gini_a(a), gini_b(a)
        assert abs(ga - gb) < 1e-12 and sum(a) <= S
        no_atendida = sum(max(0, w - x) for w, x in zip(want, a))
        print(f"{nombre:32s} {sum(a):8d}  {sum(1 for x in a if x > 0):14d}  {no_atendida:19d}  {ga:.3f}")
    assert all(x >= 1 for x in res["plan a priori (1 por pais)"])
    assert abs(r - r2) / r < 1e-6 and abs(r - 42164.17) < 0.05 and abs(t - T_SID) < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
