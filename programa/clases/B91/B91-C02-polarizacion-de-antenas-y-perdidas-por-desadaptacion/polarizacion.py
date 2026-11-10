#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C02: perdida por desadaptacion de polarizacion con vectores de Jones.

Datos consultados (2026-11-10): NASA/JPL DSN 810-005 modulo 101 rev. D (2011), Tabla 1: elipticidad (razon axial) de la antena de 70 m,
  X-band <= 1.0 dB y S-band <= 2.2 dB (maximo); polarizacion RCP o LCP, una a la vez. Definicion del modulo: elipticidad (dB) = 20 log(V2/V1).
SINTETICO (no medido): razon axial de la antena del satelite, 3.0 dB (ilustrativa), angulos de inclinacion.
Modelo: PLF = |e_t . conj(e_r)|^2 con vectores de Jones normalizados; la razon axial AR [dB] = 20 log(a/b) con a semieje mayor y b menor.
Convencion: onda en direccion de propagacion; sentido derecho (RCP) = giro horario visto desde la fuente (convencion IEEE, ilustrativa).
Segunda via: forma cerrada PLF = cos^2(psi) (lineal-lineal), 1/2 (circular-lineal), y
  PLF_max = (1 + Rt Rr)^2 / ((1 + Rt^2)(1 + Rr^2)) para mismo sentido y ejes alineados, con R = b/a.
Tolerancias: Jones frente a forma cerrada < 1e-12.
"""
from __future__ import annotations
import cmath, math, platform


def jones(ar_db, tilt_deg, sentido):
    """Vector de Jones de una elipse: eje mayor a inclinado tilt respecto a x; sentido +1 antihorario, -1 horario."""
    r = 10 ** (-abs(ar_db) / 20.0)  # b/a
    n = math.sqrt(1 + r * r)
    ex, ey = 1 / n, 1j * sentido * r / n
    t = math.radians(tilt_deg)
    c, s = math.cos(t), math.sin(t)
    return (c * ex - s * ey, s * ex + c * ey)


def plf(et, er):
    # acoplamiento entre la onda incidente (et) y la antena receptora que "ve" la polarizacion er: |<et, er*>|^2 con er definida en el mismo sentido de propagacion
    prod = et[0] * er[0].conjugate() + et[1] * er[1].conjugate()
    return abs(prod) ** 2


def db(x):
    return 10 * math.log10(x) if x > 0 else float("-inf")


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("1) Lineal - lineal: PLF = cos^2(psi)")
    mx = 0.0
    for psi in (0, 15, 30, 45, 60, 90):
        a = plf(jones(300, 0, 1), jones(300, psi, 1))  # AR 300 dB ~ lineal
        cf = math.cos(math.radians(psi)) ** 2
        mx = max(mx, abs(a - cf))
        print(f"   psi = {psi:3d} deg   PLF = {a:.6f}  ({db(max(a,1e-12)):7.2f} dB)   cos^2 = {cf:.6f}")
    assert mx < 1e-12
    pc = plf(jones(0, 0, -1), jones(300, 0, 1))
    print(f"2) Circular - lineal: PLF = {pc:.6f} ({db(pc):.3f} dB) ; esperado 0.5")
    assert abs(pc - 0.5) < 1e-12
    print("3) Elipse - elipse, mismo sentido, ejes alineados (PLF_max) y perpendiculares (PLF_min)")
    print("   AR_t [dB]  AR_r [dB]   PLF_max   PLF_min   perdida_max [dB]  perdida_min [dB]  cerrada_max")
    mxe = 0.0
    for art, arr in ((0, 0), (1.0, 1.0), (1.0, 3.0), (3.0, 3.0), (2.2, 3.0)):
        pmax = plf(jones(art, 0, -1), jones(arr, 0, -1))
        pmin = plf(jones(art, 0, -1), jones(arr, 90, -1))
        rt, rr = 10 ** (-art / 20), 10 ** (-arr / 20)
        cerr = (1 + rt * rr) ** 2 / ((1 + rt ** 2) * (1 + rr ** 2))
        mxe = max(mxe, abs(pmax - cerr))
        print(f"   {art:7.1f}   {arr:8.1f}   {pmax:8.5f}  {pmin:8.5f}  {db(pmax):12.3f}    {db(pmin):14.3f}     {cerr:8.5f}")
    assert mxe < 1e-12
    print("4) Sentido opuesto (RCP frente a LCP): AR 1.0 dB y 3.0 dB")
    for ar in (1.0, 3.0):
        p = plf(jones(ar, 0, -1), jones(ar, 0, +1))
        print(f"   AR = {ar:.1f} dB en ambos: PLF = {p:.5f} ({db(p):.2f} dB)  -> aislamiento de polarizacion cruzada")
    print("5) Enlace sintetico: estacion X-band (AR 1.0 dB, publicado como maximo) frente a satelite (AR 3.0 dB, SINTETICO)")
    p_best = plf(jones(1.0, 0, -1), jones(3.0, 0, -1))
    p_worst = plf(jones(1.0, 0, -1), jones(3.0, 90, -1))
    print(f"   mejor orientacion: {db(p_best):.3f} dB ; peor orientacion: {db(p_worst):.3f} dB ; intervalo = {db(p_best)-db(p_worst):.3f} dB")
    # simetria de la fase global
    et = jones(1.0, 20, -1)
    er = tuple(cmath.exp(1j * 0.7) * x for x in jones(3.0, 35, -1))
    assert abs(plf(et, er) - plf(et, jones(3.0, 35, -1))) < 1e-12
    print("Invariancia a la fase global verificada. Pruebas superadas.")


if __name__ == "__main__":
    main()
