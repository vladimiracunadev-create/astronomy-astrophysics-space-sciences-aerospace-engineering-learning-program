#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B95-C02: margen de dosis ionizante y supervivencia de un sistema en serie con componentes comerciales.

CONSULTADO (2026-11-10): NASA, State-of-the-Art of Small Spacecraft Technology, cap. 8 (aviónica), Tabla 8-4: valores de TID
  DECLARADOS POR LOS FABRICANTES (no verificados por la NASA): 20 krad (sistema), 30 krad (PCB), 40 krad (ensayado), 60 krad(Si), 100 krad.
ILUSTRATIVOS (sinteticos, no medidos ni extraidos de una fuente): dosis anual detras de blindaje, factor de margen de diseno (RDM),
  tasas de fallo lambda de cada componente, cobertura de latch-up.
Modelo: dosis de mision D = tasa [krad(Si)/anio] x T [anios]; margen M = TID_tolerada / D; aceptable si M >= RDM.
  Supervivencia en serie R = exp(-T sum(lambda_i)); con un par redundante en frio y conmutador ideal R_par = 1 - (1 - exp(-lambda T))^2 (modelo simplificado).
Unidades: krad(Si), anios, 1/anio. Tolerancia: Monte Carlo (semilla 20261110, N = 200000) frente a la formula analitica < 4 sigma.
"""
from __future__ import annotations
import math, platform, random

TASA_DOSIS = 6.0   # krad(Si)/anio detras de blindaje, ILUSTRATIVO
T = 2.0            # anios de mision, ILUSTRATIVO
RDM = 2.0          # margen de diseno de radiacion, ILUSTRATIVO
# (nombre, TID declarada [krad], lambda [1/anio] ILUSTRATIVA, protegido contra latch-up)
COMP = [
    ("OBC A (20 krad declarado)", 20.0, 0.05, True),
    ("OBC B (30 krad, PCB)", 30.0, 0.06, True),
    ("OBC C (40 krad ensayado)", 40.0, 0.07, True),
    ("SBC D (60 krad(Si))", 60.0, 0.08, False),
    ("SBC E (100 krad, sin recinto)", 100.0, 0.20, True),
]


def margen(tid, dosis):
    return tid / dosis


def r_serie(lams, t):
    return math.exp(-t * sum(lams))


def r_par(lam, t):
    r = math.exp(-lam * t)
    return 1.0 - (1.0 - r) ** 2


def mc_serie(lams, t, n, rng):
    ok = 0
    for _ in range(n):
        if all(rng.expovariate(l) > t for l in lams):
            ok += 1
    return ok / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    dosis = TASA_DOSIS * T
    print(f"Dosis de mision ILUSTRATIVA D = {TASA_DOSIS} krad(Si)/anio x {T} anios = {dosis:.2f} krad(Si); RDM = {RDM}")
    print(" componente                       TID[krad]  margen  RDM?   latch-up")
    aptos = []
    for nom, tid, lam, lu in COMP:
        m = margen(tid, dosis)
        ok = m >= RDM
        aptos.append(ok)
        print(f" {nom:31s} {tid:8.1f}  {m:6.2f}  {'si' if ok else 'NO':4s}   {'protegido' if lu else 'sin proteccion'}")
    lams = [c[2] for c in COMP]
    rs = r_serie(lams, T)
    print(f"Supervivencia en serie de los 5 (analitica) R = {rs:.5f}")
    rng = random.Random(20261110)
    n = 200000
    rm = mc_serie(lams, T, n, rng)
    sig = math.sqrt(rs * (1 - rs) / n)
    print(f"Monte Carlo (N = {n}, semilla 20261110) R = {rm:.5f} ; |dif| = {abs(rm - rs):.5f} ; sigma = {sig:.5f}")
    print("Efecto de la redundancia fria en el OBC A (lambda = 0.05/anio, T = 2 anios):")
    r1 = math.exp(-0.05 * T)
    rp = r_par(0.05, T)
    print(f"  simple R = {r1:.5f} ; par R = {rp:.5f}")
    rs_red = rs / r1 * rp
    print(f"  sistema con OBC A duplicado R = {rs_red:.5f}")
    # sensibilidad: duplicar la tasa de dosis (p. ej. orbita mas alta)
    dosis2 = 2.0 * dosis
    print(f"Con la dosis duplicada ({dosis2:.1f} krad) cumplen RDM: {[round(margen(c[1], dosis2), 2) >= RDM for c in COMP]}")
    assert abs(rm - rs) < 4 * sig
    assert rp > r1
    assert abs(margen(20.0, 4.0) - 5.0) < 1e-12
    assert all(a == (c[1] / dosis >= RDM) for a, c in zip(aptos, COMP))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
