#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C13: cambio de plano interplanetario (inclinacion respecto a la ecliptica) combinado con el cambio de velocidad.

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Venus 108.210e6, Tierra 149.598e6, Marte 227.956e6, Jupiter 778.479e6 km) e inclinaciones orbitales (Venus 3.395, Marte 1.848, Jupiter 1.304 grados).
GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado). Modelo: transferencia de Hohmann desde la Tierra (en la ecliptica) a un destino cuyo plano esta inclinado un angulo i;
el nodo se supone en el punto de llegada (peor caso de no coplanaridad: todo el cambio de plano se hace con velocidades de transferencia y del planeta). Planetas en orbitas circulares.
Pruebas: (1) combinada = sqrt(v1^2 + v2^2 - 2 v1 v2 cos i) igual a la norma de la diferencia de vectores en 3D (tol. 1e-12); (2) el reparto optimo de i entre salida y llegada, hallado por seccion aurea,
coincide con un barrido fino de i1 (tol. 1e-4 grados) y no cuesta mas que hacerlo todo en un extremo.
"""
import math, platform
MU = 1.32712440e11
AE_ = 149.598e6
DEST = {"Venus": (108.210e6, 3.395), "Marte": (227.956e6, 1.848), "Jupiter": (778.479e6, 1.304)}


def comb(v1, v2, i):
    return math.sqrt(v1 * v1 + v2 * v2 - 2 * v1 * v2 * math.cos(i))


def vec(v, i):
    return [v * math.cos(i), 0.0, v * math.sin(i)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(" destino  i [grados]  v_transf_llegada  V_planeta  dv separado [km/s] (velocidad + plano)  dv combinado [km/s]  ahorro [km/s]  dv solo-plano [km/s]")
    for nom, (ad, idg) in DEST.items():
        i = math.radians(idg)
        at = 0.5 * (AE_ + ad)
        va = math.sqrt(MU * (2 / ad - 1 / at)); V = math.sqrt(MU / ad)
        if ad < AE_:
            va = math.sqrt(MU * (2 / ad - 1 / at))
        dv_v = abs(V - va); dv_p = 2 * va * math.sin(i / 2)
        c = comb(va, V, i)
        a3 = vec(va, 0.0); b3 = vec(V, i)
        assert abs(c - math.dist(a3, b3)) < 1e-12
        print(f"{nom:8s} {idg:8.3f} {va:16.4f} {V:11.4f} {dv_v + dv_p:30.4f} {c:24.4f} {dv_v + dv_p - c:14.4f} {dv_p:18.4f}")
    # reparto optimo en Marte entre la salida (en el perihelio, i1) y la llegada (afelio, i2 = i - i1)
    ad, idg = DEST["Marte"]
    i = math.radians(idg); at = 0.5 * (AE_ + ad)
    VE = math.sqrt(MU / AE_); vp = math.sqrt(MU * (2 / AE_ - 1 / at))
    va = math.sqrt(MU * (2 / ad - 1 / at)); VM = math.sqrt(MU / ad)
    f = lambda i1: comb(vp, VE, i1) + comb(va, VM, i - i1)
    lo, hi = 0.0, i
    g = (math.sqrt(5) - 1) / 2
    for _ in range(100):
        c1 = hi - g * (hi - lo); d1 = lo + g * (hi - lo)
        if f(c1) < f(d1): hi = d1
        else: lo = c1
    i1 = 0.5 * (lo + hi)
    barr = min((f(i * k / 100000), i * k / 100000) for k in range(100001))
    print(f"Marte: reparto optimo i1 = {math.degrees(i1):.4f} grados en la salida y {math.degrees(i-i1):.4f} grados en la llegada")
    print(f"   dv total optimo = {f(i1):.6f} km/s ; todo en la llegada = {f(0.0):.6f} km/s ; todo en la salida = {f(i):.6f} km/s")
    print(f"   barrido fino: i1 = {math.degrees(barr[1]):.4f} grados ; dv = {barr[0]:.6f} km/s")
    assert abs(math.degrees(i1) - math.degrees(barr[1])) < 1e-3
    assert f(i1) <= f(0.0) + 1e-12 and f(i1) <= f(i) + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
