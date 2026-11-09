#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C14: radiacion y degradacion, dosis ionizante con blindaje de aluminio y tasa de eventos de partícula simple.

Datos: N_A, radio clasico del electron, m_e c^2 = 0,51099895069 MeV, energia en reposo del proton (938,27208943 MeV) y 1 MeV = 1,602176634e-13 J de NIST CODATA 2022
(allascii.txt, consultada el 2026-11-09). ILUSTRATIVOS (no son un entorno de radiacion ni un componente real): protones monoenergeticos de 30 MeV con fluencia 1e10 cm-2, blindaje de
aluminio (Z/A = 13/26,98, 2,70 g/cm3, I = 166 eV; valores de uso general, no consultados aqui), silicio (Z/A = 14/28,0855, I = 173 eV), seccion eficaz de SEU 1e-14 cm2/bit,
1e6 bits, flujo 1 cm-2 s-1 y una mision de 5 anios.
Modelo: (1) perdida de energia de Bethe sin correcciones (como en C09); energia de salida del blindaje por integracion de dE/dx y alcance por la integral de dE/S; (2) dosis D = fluencia * S * 1,602e-10 Gy
con S en MeV cm2/g; (3) numero de eventos ~ Poisson(sigma N phi T) simulado con semilla 20261109 en 20000 misiones frente a la media y a P(0) = exp(-media).
Supuestos: haz unidireccional, perdida continua, sin dispersion nuclear ni secundarios, sin dependencia con la tasa de dosis. Validez: ilustrativa.
Tolerancia: espesor de parada de dos vias (alcance integral y barrido del espesor), 2 %; media Poisson, 2 %; P(0), 0,01 absoluto.
"""
from __future__ import annotations
import math, platform, random

NA = 6.02214076e23
RE_CM = 2.8179403205e-13
MEC2 = 0.51099895069
MP = 938.27208943
K = 4 * math.pi * NA * RE_CM ** 2 * MEC2
MEV_J = 1.602176634e-13
AL = (13 / 26.98, 2.70, 166e-6)
SI = (14 / 28.0855, 2.329, 173e-6)


def stopping(e, mat):
    za, rho, i_ev = mat
    g = 1 + e / MP
    b2 = 1 - 1 / g ** 2
    tmax = 2 * MEC2 * b2 * g ** 2 / (1 + 2 * g * MEC2 / MP + (MEC2 / MP) ** 2)
    return K * za / b2 * (0.5 * math.log(2 * MEC2 * b2 * g ** 2 * tmax / i_ev ** 2) - b2)


def e_salida(e0, t_cm, mat=AL, pasos=4000):
    dx = t_cm / pasos
    e = e0
    for _ in range(pasos):
        if e <= 0.5:
            return 0.0
        k1 = stopping(e, mat)
        e2 = e - 0.5 * dx * mat[1] * k1
        if e2 <= 0.5:
            return 0.0
        e -= dx * mat[1] * stopping(e2, mat)
    return max(e, 0.0)


def alcance_g(e0, mat, emin=0.5, n=4000):
    h = (e0 - emin) / n
    s = 0.0
    for i in range(n + 1):
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w / stopping(emin + i * h, mat)
    return s * h / 3


def poisson(rng, mu):
    tot = 0
    while mu > 0:
        m = min(mu, 10.0)
        mu -= m
        l, k, p = math.exp(-m), 0, 1.0
        while True:
            p *= rng.random()
            if p <= l:
                break
            k += 1
        tot += k
    return tot


def calc():
    r = {}
    e0, flu = 30.0, 1e10
    r["alcance_mm"] = alcance_g(e0, AL) / AL[1] * 10
    r["dosis"] = {}
    for t_mm in (0.0, 1.0, 2.0, 4.0, 6.0):
        e = e_salida(e0, t_mm / 10)
        s = stopping(e, SI) if e > 0 else 0.0
        r["dosis"][t_mm] = (e, s, flu * s * MEV_J * 1e3)
    # espesor de parada por barrido (biseccion sobre el espesor)
    a, b = 0.0, 2 * r["alcance_mm"] / 10
    for _ in range(60):
        m = 0.5 * (a + b)
        if e_salida(e0, m, pasos=6000) > 0:
            a = m
        else:
            b = m
    r["parada_mm"] = 10 * 0.5 * (a + b)
    mu = 1e-14 * 1e6 * 1 * 5 * 365.25 * 86400
    r["mu"] = mu
    rng = random.Random(20261109)
    n = 20000
    xs = [poisson(rng, mu) for _ in range(n)]
    r["mc_mean"] = sum(xs) / n
    r["mc_var"] = sum((x - r["mc_mean"]) ** 2 for x in xs) / (n - 1)
    r["p0_mc"] = xs.count(0) / n
    r["p0"] = math.exp(-mu)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"alcance CSDA de 30 MeV en aluminio (integral) = {r['alcance_mm']:.4f} mm ; espesor de parada por barrido = {r['parada_mm']:.4f} mm")
    print(f"{'Al [mm]':>8} {'E_salida [MeV]':>15} {'S_Si [MeV cm2/g]':>18} {'dosis [Gy]':>12}")
    for t, (e, s, d) in r["dosis"].items():
        print(f"{t:8.1f} {e:15.3f} {s:18.3f} {d:12.2f}")
    print(f"eventos esperados en la mision = {r['mu']:.3f} ; Monte Carlo: media = {r['mc_mean']:.3f}, varianza = {r['mc_var']:.3f}")
    print(f"P(0 eventos): exp(-mu) = {r['p0']:.4f} ; Monte Carlo = {r['p0_mc']:.4f}")
    assert abs(r["parada_mm"] - r["alcance_mm"]) / r["alcance_mm"] < 0.02
    assert abs(r["mc_mean"] - r["mu"]) / r["mu"] < 0.02
    assert abs(r["p0_mc"] - r["p0"]) < 0.01
    d = [v[2] for v in r["dosis"].values()]
    assert d[0] < d[1] < d[2] < d[3]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
