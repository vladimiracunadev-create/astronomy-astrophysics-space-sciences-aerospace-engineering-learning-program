#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C06: rayos gamma, seccion eficaz de Klein-Nishina, umbral de pares y cinematica de un telescopio Compton.

Datos: m_e c^2 = 0,51099895069 MeV, seccion eficaz de Thomson 6,6524587051e-29 m2 y radio clasico del electron de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09).
ILUSTRATIVOS: energia del fotón incidente 1 MeV, resolucion en energia de 5 % en cada deposito (no es la de ningun instrumento), muestra de 100000 dispersiones.
Modelo: (1) seccion eficaz total de Klein-Nishina en forma cerrada frente a la integral numerica de dsigma/dOmega; limite k -> 0 igual a Thomson; (2) umbral de produccion
de pares 2 m_e c^2; (3) dispersion Compton muestreada por rechazo (semilla 20261109): energia media del fotón dispersado frente a la integral exacta; (4) angulo reconstruido
cos(phi) = 1 - m_e c^2 (1/E2 - 1/(E1+E2)) y su dispersion por ruido frente a la propagacion de errores.
Supuestos: electron libre en reposo, un solo scattering seguido de absorcion total, sin Doppler ni polarizacion. Validez: ilustrativa.
Tolerancia: forma cerrada frente a integral numerica, 1e-6 relativo; limite de Thomson, 1e-3; media muestreada a 0,5 %; dispersion angular a 5 %.
"""
from __future__ import annotations
import math, platform, random

MEC2 = 0.51099895069
RE = 2.8179403205e-15
SIGT = 6.6524587051e-29


def dsdo(k, mu):
    p = 1 / (1 + k * (1 - mu))
    return 0.5 * RE ** 2 * p ** 2 * (p + 1 / p - (1 - mu ** 2))


def sigma_cerrada(k):
    if k < 1e-4:
        return SIGT * (1 - 2 * k + 5.2 * k * k)
    a = (1 + k) / k ** 2 * (2 * (1 + k) / (1 + 2 * k) - math.log(1 + 2 * k) / k)
    b = math.log(1 + 2 * k) / (2 * k) - (1 + 3 * k) / (1 + 2 * k) ** 2
    return 2 * math.pi * RE ** 2 * (a + b)


def sigma_num(k, n=200000):
    h = 2.0 / n
    s = 0.0
    for i in range(n + 1):
        mu = -1 + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * dsdo(k, mu)
    return 2 * math.pi * s * h / 3


def e_media_exacta(k, n=100000):
    h = 2.0 / n
    num = den = 0.0
    for i in range(n + 1):
        mu = -1 + i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        p = 1 / (1 + k * (1 - mu))
        d = dsdo(k, mu)
        num += w * d * p
        den += w * d
    return num / den


def muestrear_mu(rng, k):
    while True:
        mu = rng.uniform(-1, 1)
        if rng.random() * dsdo(k, 1.0) * 1.0001 <= dsdo(k, mu):
            # cota: dsdo es maxima en mu = 1
            return mu


def phi_rec(e1, e2):
    c = 1 - MEC2 * (1 / e2 - 1 / (e1 + e2))
    return math.acos(max(-1.0, min(1.0, c)))


def calc():
    r = {}
    r["umbral"] = 2 * MEC2
    r["sig"] = {}
    for e in (0.001, 0.1, 1.0, 10.0):
        k = e / MEC2
        r["sig"][e] = (sigma_cerrada(k), sigma_num(k))
    r["lim"] = sigma_cerrada(1e-6) / SIGT
    k0 = 1.0 / MEC2
    r["emed_exacta"] = e_media_exacta(k0)
    rng = random.Random(20261109)
    n = 100000
    sume = 0.0
    phis = []
    phis_ruido = []
    sg = 0.05
    for _ in range(n):
        mu = muestrear_mu(rng, k0)
        ep = 1.0 / (1 + k0 * (1 - mu))
        sume += ep
        e1, e2 = 1.0 - ep, ep
        phis.append(phi_rec(e1, e2) - math.acos(mu))
    r["emed_mc"] = sume / n
    r["err_phi_max"] = max(abs(x) for x in phis)
    # dispersion por ruido para un angulo fijo de 60 grados
    mu = math.cos(math.radians(60))
    ep = 1.0 / (1 + k0 * (1 - mu))
    e1, e2 = 1.0 - ep, ep
    ph0 = math.degrees(phi_rec(e1, e2))
    r["ph0"] = ph0
    sam = []
    for _ in range(20000):
        a = e1 * (1 + sg * rng.gauss(0, 1))
        b = e2 * (1 + sg * rng.gauss(0, 1))
        sam.append(math.degrees(phi_rec(a, b)))
    m = sum(sam) / len(sam)
    r["sd_mc"] = math.sqrt(sum((x - m) ** 2 for x in sam) / (len(sam) - 1))
    de = 1e-6
    d1 = (math.degrees(phi_rec(e1 + de, e2)) - math.degrees(phi_rec(e1 - de, e2))) / (2 * de)
    d2 = (math.degrees(phi_rec(e1, e2 + de)) - math.degrees(phi_rec(e1, e2 - de))) / (2 * de)
    r["sd_prop"] = math.hypot(d1 * sg * e1, d2 * sg * e2)
    r["e1"], r["e2"] = e1, e2
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"umbral de pares 2 m_e c^2 = {r['umbral']:.6f} MeV")
    print(f"{'E [MeV]':>8} {'sigma cerrada [m2]':>20} {'sigma numerica [m2]':>20} {'sigma/sigma_T':>14}")
    for e, (a, b) in r["sig"].items():
        print(f"{e:8.3f} {a:20.6e} {b:20.6e} {a/SIGT:14.5f}")
        assert abs(a - b) / a < 1e-6
    print(f"limite k -> 0: sigma_KN/sigma_T = {r['lim']:.6f}")
    print(f"energia media dispersada / E0 (1 MeV): exacta = {r['emed_exacta']:.5f} ; Monte Carlo = {r['emed_mc']:.5f}")
    print(f"error maximo |phi_reconstruido - phi_verdadero| sin ruido = {r['err_phi_max']:.2e} rad")
    print(f"phi = {r['ph0']:.3f} grados con E1 = {r['e1']:.4f} MeV y E2 = {r['e2']:.4f} MeV")
    print(f"dispersion de phi con 5 % de ruido: Monte Carlo = {r['sd_mc']:.3f} grados ; propagacion = {r['sd_prop']:.3f} grados")
    assert abs(r["lim"] - 1) < 1e-3
    assert abs(r["emed_mc"] - r["emed_exacta"]) / r["emed_exacta"] < 0.005
    assert r["err_phi_max"] < 1e-6
    assert abs(r["sd_mc"] - r["sd_prop"]) / r["sd_prop"] < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
