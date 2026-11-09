#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C05: reflexion rasante de rayos X, geometria Wolter I y area efectiva.

Datos: h, c, e (eV), radio clasico del electron r_e = 2,8179403205e-15 m y numero de Avogadro de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09).
ILUSTRATIVOS (no son los parametros de ningun telescopio): recubrimiento tipo iridio con Z = 77, A = 192,2 g/mol y densidad 22,5 g/cm3 (valores de uso general, no consultados aqui),
distancia focal 10 m, longitud de cada segmento 0,8 m, 20 conchas con R_i = 0,15 * 1,06^i m. Modelo de electrones libres: se ignoran los bordes de absorcion.
Modelo: (1) decremento del indice delta = r_e lambda^2 n_e / (2 pi) y angulo critico theta_c = sqrt(2 delta), contrastado con acos(1 - delta); (2) angulo de incidencia
rasante alpha_i = R_i / (4 f); (3) reflectividad de Fresnel sin absorcion para alpha > theta_c y 1 si no; area efectiva = suma 2 pi R_i L alpha_i * refl^2 (dos reflexiones);
(4) trazado Monte Carlo de rayos paralelos (semilla 20261109) que reproduce la suma con otro metodo.
Supuestos: conchas conicas, sin rugosidad, sin obstruccion ni dispersion. Validez: ilustrativa.
Tolerancia: theta_c de dos vias, 1e-3 relativo (error de segundo orden de la aproximacion de angulo pequeno); Monte Carlo frente a la suma, 2 %.
"""
from __future__ import annotations
import math, platform, random

H = 6.62607015e-34
C = 299792458.0
EV = 1.602176634e-19
RE = 2.8179403205e-15
NA = 6.02214076e23
Z, A, RHO = 77, 192.2e-3, 22.5e3          # kg/mol, kg/m3
F, L = 10.0, 0.8
RADIOS = [0.15 * 1.06 ** i for i in range(20)]


def delta(e_kev):
    lam = H * C / (e_kev * 1e3 * EV)
    ne = Z * RHO * NA / A
    return RE * lam ** 2 * ne / (2 * math.pi), lam


def refl(alpha, d):
    s = math.sin(alpha)
    if s * s <= 2 * d:
        return 1.0
    q = math.sqrt(s * s - 2 * d)
    return ((s - q) / (s + q)) ** 2


def area_suma(e_kev):
    d, _ = delta(e_kev)
    tot = 0.0
    for r in RADIOS:
        al = r / (4 * F)
        tot += 2 * math.pi * r * L * al * refl(al, d) ** 2
    return tot


def area_mc(e_kev, n=400000, seed=20261109):
    d, _ = delta(e_kev)
    rng = random.Random(seed)
    rmax = RADIOS[-1] + RADIOS[-1] / (4 * F) * L
    acierto = 0.0
    for _ in range(n):
        r = rmax * math.sqrt(rng.random())
        for ri in RADIOS:
            al = ri / (4 * F)
            if ri <= r < ri + al * L:
                acierto += refl(al, d) ** 2
                break
    return acierto / n * math.pi * rmax ** 2


def calc():
    r = {"geo": sum(2 * math.pi * x * L * x / (4 * F) for x in RADIOS)}
    r["alfa"] = (RADIOS[0] / (4 * F), RADIOS[-1] / (4 * F))
    r["tc"] = {}
    r["area"] = {}
    for e in (1, 5, 10, 20):
        d, lam = delta(e)
        tc1 = math.sqrt(2 * d)
        tc2 = math.acos(1 - d)
        r["tc"][e] = (lam * 1e9, d, tc1, tc2)
        r["area"][e] = (area_suma(e), area_mc(e))
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"alpha de la concha interna = {math.degrees(r['alfa'][0]):.4f} grados ; externa = {math.degrees(r['alfa'][1]):.4f} grados")
    print(f"area geometrica de las 20 conchas = {r['geo']*1e4:.2f} cm2")
    print(f"{'E [keV]':>8} {'lambda [nm]':>12} {'delta':>12} {'theta_c [deg] sqrt':>20} {'theta_c [deg] acos':>20}")
    for e, (lam, d, a, b) in r["tc"].items():
        print(f"{e:8d} {lam:12.5f} {d:12.4e} {math.degrees(a):20.6f} {math.degrees(b):20.6f}")
        assert abs(a - b) / a < 1e-3
    print(f"{'E [keV]':>8} {'A_eff suma [cm2]':>18} {'A_eff MC [cm2]':>16}")
    for e, (s, m) in r["area"].items():
        print(f"{e:8d} {s*1e4:18.2f} {m*1e4:16.2f}")
        assert abs(m - s) / s < 0.02
    a = r["area"]
    assert a[1][0] > a[10][0] > a[20][0] > 0
    assert a[1][0] <= r["geo"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
