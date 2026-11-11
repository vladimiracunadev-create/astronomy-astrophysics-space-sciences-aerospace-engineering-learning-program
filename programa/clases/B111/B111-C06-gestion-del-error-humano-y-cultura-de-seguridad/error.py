#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C06: barreras en serie ("queso suizo"), causa comun y reporte de eventos (SINTETICO).

Marco (Reason 2000, BMJ 320:768-770; solo metadatos consultados; el texto completo no): enfoque de sistema, fallas activas
y condiciones latentes, defensas en capas.
Modelo SINTETICO: cinco barreras con probabilidad de falla individual q = (0.10, 0.05, 0.20, 0.10, 0.15).
Independientes: P = producto de q_i. Con condicion latente comun: con probabilidad c = 0.10 esta presente y multiplica
cada q_i por k = 3 (tope 1); P = (1-c) * prod(q_i) + c * prod(min(1, k q_i)). Segunda via: Monte Carlo (semilla 116,
1000000 eventos) con tolerancia relativa 15 %.
Reporte: de N = 1000 casi-eventos SINTETICOS de cuatro tipos (resbalon, descuido, equivocacion, violacion) con mezcla
(0.30, 0.35, 0.25, 0.10), la tasa de reporte por tipo es (0.40, 0.30, 0.60, 0.20); se calculan los esperados reportados y
la fraccion global; la cultura de seguridad se modela como un aumento multiplicativo r de las tasas (tope 1).
Supuestos: barreras independientes dado el estado latente; tasas ilustrativas, sin evaluar a personas ni organizaciones.
"""
from __future__ import annotations
import math, platform, random

Q = (0.10, 0.05, 0.20, 0.10, 0.15)
C_LAT, K = 0.10, 3.0
TIPOS = ("resbalon", "descuido", "equivocacion", "violacion")
MEZCLA = (0.30, 0.35, 0.25, 0.10)
TASA = (0.40, 0.30, 0.60, 0.20)


def producto(qs):
    return math.prod(qs)


def p_comun():
    return (1 - C_LAT) * producto(Q) + C_LAT * producto([min(1.0, K * q) for q in Q])


def montecarlo(rng, m=1000000):
    n = 0
    for _ in range(m):
        f = K if rng.random() < C_LAT else 1.0
        if all(rng.random() < min(1.0, f * q) for q in Q):
            n += 1
    return n / m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    pi = producto(Q)
    pc = p_comun()
    rng = random.Random(116)
    mc = montecarlo(rng)
    print(f"Barreras SINTETICAS q = {Q}")
    print(f"P(todas fallan), independientes = {pi:.3e}")
    print(f"P(todas fallan), con condicion latente comun (c = {C_LAT}, k = {K:g}) = {pc:.3e}")
    print(f"Monte Carlo (1000000 eventos) = {mc:.3e} ; diferencia relativa = {abs(mc - pc) / pc:.3f}")
    print(f"Cociente causa comun / independiente = {pc / pi:.3f}")
    print("Aporte de cada capa: P sin la barrera i (independientes) y multiplicador de riesgo")
    for i, q in enumerate(Q, 1):
        sin = math.prod(x for j, x in enumerate(Q) if j != i - 1)
        print(f"  barrera {i}: sin ella P = {sin:.3e} ; aumento = {sin / pi:.2f}")
    print("Reporte de 1000 casi-eventos SINTETICOS:")
    print("  tipo           ocurren  tasa  reportados")
    tot = 0.0
    for t, m, r in zip(TIPOS, MEZCLA, TASA):
        rep = 1000 * m * r
        tot += rep
        print(f"  {t:13s} {1000 * m:8.0f}  {r:4.2f}  {rep:10.1f}")
    print(f"Reportados = {tot:.1f} de 1000 (fraccion {tot / 1000:.3f})")
    for r in (1.0, 1.5):
        t2 = sum(1000 * m * min(1.0, r * x) for m, x in zip(MEZCLA, TASA))
        print(f"  con cultura que multiplica la tasa por {r:.1f}: reportados = {t2:.1f}")
    assert abs(sum(MEZCLA) - 1.0) < 1e-12
    assert abs(mc - pc) / pc < 0.15
    assert pc > pi
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
