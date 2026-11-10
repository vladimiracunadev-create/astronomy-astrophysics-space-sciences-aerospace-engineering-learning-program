#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C06: flujo supersonico - relacion area-Mach, angulo de Mach y expansion de Prandtl-Meyer.

Consultado (2026-11-10): NASA Glenn, relaciones isentropicas y descripcion de la tobera (subsonico antes de la garganta, supersonico despues).
ESTANDAR (no consultado): A/A* = (1/M) [ (2/(g+1)) (1 + (g-1) M^2/2) ]^((g+1)/(2(g-1))); angulo de Mach mu = asin(1/M);
funcion de Prandtl-Meyer nu(M) = sqrt((g+1)/(g-1)) atan(sqrt((g-1)(M^2-1)/(g+1))) - atan(sqrt(M^2-1)).
ILUSTRATIVOS: gamma = 1.4 (aire), razones de area 2, 5, 10; expansion desde M1 = 2 con deflexion de 10 grados.
Via 2 (area-Mach): integracion numerica de dA/A = (M^2 - 1) dV/V desde M = 1 con dV/V = dM / (M (1 + (g-1) M^2/2)).
Via 2 (Prandtl-Meyer): integracion numerica de dnu = sqrt(M^2 - 1) dV/V desde M = 1.
Tolerancias: vias numericas frente a cerradas < 1e-7 relativa.
"""
import math, platform

G = 1.4


def area_ratio(M):
    return (1 / M) * ((2 / (G + 1)) * (1 + 0.5 * (G - 1) * M * M)) ** ((G + 1) / (2 * (G - 1)))


def mach_supersonico(ar):
    lo, hi = 1.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if area_ratio(mid) < ar:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def nu(M):
    k = math.sqrt((G + 1) / (G - 1))
    return k * math.atan(math.sqrt((M * M - 1) / k ** 2)) - math.atan(math.sqrt(M * M - 1))


def integral_area(M, n=200000):
    """ln(A/A*) = integral desde 1 hasta M de (m^2-1)/(m (1 + (g-1) m^2/2)) dm (regla del punto medio)."""
    h = (M - 1.0) / n
    s = 0.0
    for i in range(n):
        m = 1.0 + (i + 0.5) * h
        s += (m * m - 1) / (m * (1 + 0.5 * (G - 1) * m * m)) * h
    return math.exp(s)


def integral_nu(M, n=200000):
    """Cambio de variable m = 1 + s^2 para tratar la raiz en m = 1 (punto medio en s)."""
    smax = math.sqrt(M - 1.0)
    h = smax / n
    s = 0.0
    for i in range(n):
        t = (i + 0.5) * h
        m = 1.0 + t * t
        s += math.sqrt(m * m - 1) / (m * (1 + 0.5 * (G - 1) * m * m)) * 2 * t * h
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Aire ILUSTRATIVO: gamma = {G}")
    print(" A/A*     M (supersonico)   mu [grados]   A/A* por integral   diferencia")
    peor = 0.0
    for ar in (2.0, 5.0, 10.0):
        M = mach_supersonico(ar)
        num = integral_area(M)
        d = abs(num - ar) / ar
        peor = max(peor, d)
        print(f" {ar:5.1f}      {M:.5f}         {math.degrees(math.asin(1 / M)):7.3f}        {num:.6f}          {d:.1e}")
    print(f"Prandtl-Meyer: nu(2) = {math.degrees(nu(2.0)):.4f} grados ; nu(inf) = {math.degrees(0.5 * math.pi * (math.sqrt((G + 1) / (G - 1)) - 1)):.3f} grados")
    n_int = math.degrees(integral_nu(2.0))
    dn = abs(n_int - math.degrees(nu(2.0))) / math.degrees(nu(2.0))
    print(f" nu(2) por integral = {n_int:.4f} grados ; diferencia relativa = {dn:.1e}")
    # expansion de 10 grados desde M1 = 2
    nu2 = nu(2.0) + math.radians(10.0)
    lo, hi = 2.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if nu(mid) < nu2:
            lo = mid
        else:
            hi = mid
    M2 = 0.5 * (lo + hi)
    f1 = 1 + 0.2 * 4.0
    f2 = 1 + 0.2 * M2 * M2
    print(f"Expansion de 10 grados desde M1 = 2: M2 = {M2:.4f} ; p2/p1 = {(f1 / f2) ** 3.5:.4f} ; T2/T1 = {f1 / f2:.4f}")
    # velocidad maxima limite (vacio): V_max/a0
    print(f"Velocidad limite (vacio) V_max / a_0 = {math.sqrt(2 / (G - 1)):.4f}")
    assert peor < 1e-7 and dn < 1e-7
    assert abs(area_ratio(1.0) - 1.0) < 1e-12
    print("Pruebas superadas.")


main()
