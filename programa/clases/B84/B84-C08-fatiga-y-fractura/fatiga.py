#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C08: ley de Paris, tamano critico de grieta, Basquin y regla de Miner.

DATOS ILUSTRATIVOS (aleacion de aluminio tipica, NO consultados, no de diseno):
  Paris: da/dN = C (dK)^m con C = 1e-11 (m/ciclo con dK en MPa sqrt(m)), m = 3,0; dK = Y dS sqrt(pi a), Y = 1,12 (grieta de borde)
  Tenacidad K_Ic = 30 MPa sqrt(m); rango de tension dS = 100 MPa con R = 0 (S_max = 100 MPa); grieta inicial a0 = 0,5 mm.
  Basquin: S_a = Sf' (2N)^b con Sf' = 900 MPa y b = -0,10; correccion de Goodman con S_u = 480 MPa.
Segunda via: la integral de Paris se resuelve por RK4 en log(a) y se compara con la formula cerrada
  N = 2/((m-2) C (Y dS sqrt(pi))^m) (a0^(1-m/2) - ac^(1-m/2)).
Unidades: MPa, m, ciclos. Tolerancia: RK4 frente a formula cerrada < 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

C, M, KIC, Y = 1e-11, 3.0, 30.0, 1.12


def a_critico(smax):
    return (KIC / (Y * smax)) ** 2 / math.pi


def n_cerrado(ds, a0, ac):
    return 2.0 / ((M - 2.0) * C * (Y * ds * math.sqrt(math.pi)) ** M) * (a0 ** (1 - M / 2) - ac ** (1 - M / 2))


def n_numerico(ds, a0, ac, pasos=20000):
    # dN/d(ln a) = a / (C (Y ds sqrt(pi a))^m); integrar en x = ln a con regla de Simpson
    f = lambda x: math.exp(x) / (C * (Y * ds * math.sqrt(math.pi * math.exp(x))) ** M)
    x0, x1 = math.log(a0), math.log(ac)
    h = (x1 - x0) / pasos
    s = f(x0) + f(x1)
    for i in range(1, pasos):
        s += (4 if i % 2 else 2) * f(x0 + i * h)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Aleacion ILUSTRATIVA: C = 1e-11, m = 3, Y = 1,12, K_Ic = 30 MPa sqrt(m)")
    ds, a0 = 100.0, 0.5e-3
    ac = a_critico(ds)
    print(f"a_critico con S_max = {ds:.0f} MPa: {ac * 1e3:.3f} mm")
    nc = n_cerrado(ds, a0, ac)
    nn = n_numerico(ds, a0, ac)
    print(f"Ciclos de a0 = 0,5 mm a a_c: formula cerrada = {nc:.1f} ; Simpson en ln a = {nn:.1f} ; dif. relativa = {abs(nc - nn) / nc:.1e}")
    print("Sensibilidad de la vida al rango de tension (a0 = 0,5 mm):")
    prev = None
    for d in (50.0, 75.0, 100.0, 150.0):
        a_c = a_critico(d)
        n = n_cerrado(d, a0, a_c)
        extra = "" if prev is None else f"  (cociente con la fila anterior = {n / prev:.3f})"
        print(f"  dS = {d:5.0f} MPa  a_c = {a_c * 1e3:7.3f} mm  N = {n:12.1f}{extra}")
        prev = n
    print("Sensibilidad al tamano inicial de grieta (dS = 100 MPa):")
    for a in (0.2e-3, 0.5e-3, 1.0e-3, 2.0e-3):
        print(f"  a0 = {a * 1e3:4.1f} mm  N = {n_cerrado(ds, a, ac):12.1f}")
    # Basquin con correccion de Goodman
    sf, b, su = 900.0, -0.10, 480.0
    print("Basquin (sin y con media), S_a equivalente por Goodman S_ar = S_a/(1 - S_m/S_u):")
    for sa, sm in ((150.0, 0.0), (150.0, 100.0), (100.0, 100.0)):
        sar = sa / (1 - sm / su)
        N = 0.5 * (sar / sf) ** (1 / b)
        print(f"  S_a = {sa:5.0f}, S_m = {sm:5.0f} -> S_ar = {sar:7.2f} MPa -> N = {N:12.3e}")
    # Miner: tres bloques
    bloques = ((200.0, 0.0, 3.0e5), (150.0, 0.0, 5.0e6), (100.0, 0.0, 1.0e8))
    D = 0.0
    for sa, sm, n in bloques:
        N = 0.5 * (sa / sf) ** (1 / b)
        D += n / N
        print(f"  bloque S_a = {sa:5.0f}: n = {n:9.1f}, N_f = {N:12.3e}, n/N = {n / N:.4f}")
    print(f"Dano de Miner D = {D:.4f} ({'vida agotada' if D >= 1 else 'queda vida'})")
    assert abs(nc - nn) / nc < 1e-6
    assert ac > a0
    assert abs(n_cerrado(50.0, a0, a_critico(50.0)) / n_cerrado(100.0, a0, a_critico(100.0)) - 8.0) < 1.0  # N ~ dS^-3 (con a_c)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
