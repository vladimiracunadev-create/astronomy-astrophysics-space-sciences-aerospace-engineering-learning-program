#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C03: telescopio ultravioleta, serie de Lyman desde la constante de Rydberg y cuentas fotonicas con estadistica de Poisson.

Datos: constante de Rydberg, h, c, m_e, m_p, e, k_B de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09); R_sol = 6,957e8 m de la UAI B3 de 2015 (consultada el 2026-11-09)
y au = 1,495978707e11 m (IERS, consultada el 2026-11-09). ILUSTRATIVOS: estrella de 10000 K con radio 1 R_sol a 1000 pc, banda 150-170 nm, apertura 0,25 m de radio,
rendimiento total 0,15, fondo 0,5 cuentas/s. No es una estrella real ni el rendimiento de ningun instrumento.
Modelo: (1) serie de Lyman 1/lambda = R_H (1 - 1/n^2) con R_H = R_inf/(1 + m_e/m_p); (2) tasa de fotones = integral de pi B_lambda (R/d)^2 A eta lambda/(hc) dlambda (Simpson);
(3) Monte Carlo de Poisson (semilla 20261109) frente a sqrt(N); (4) tiempo para S/N = 10: t = SN^2 (S+B)/S^2.
Supuestos: cuerpo negro, sin extincion interestelar, rendimiento plano. Validez: ilustrativa.
Tolerancia: tasa por Simpson de 2000 puntos frente a 4000, 1e-9 relativo; media de Poisson a 1 %, desviacion a 5 %.
"""
from __future__ import annotations
import math, platform, random

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
RINF = 10973731.568157
ME = 9.1093837139e-31
MP = 1.67262192595e-27
EV = 1.602176634e-19
RSUN = 6.957e8
AU = 1.495978707e11
PC = 648000 / math.pi * AU


def planck_lambda(lam, t):
    return 2 * H * C ** 2 / lam ** 5 / math.expm1(H * C / (lam * KB * t))


def tasa_fotones(n, t=10000.0, rad=RSUN, d=1000 * PC, l1=150e-9, l2=170e-9, area=math.pi * 0.25 ** 2, eta=0.15):
    h = (l2 - l1) / n
    s = 0.0
    for k in range(n + 1):
        lam = l1 + k * h
        g = math.pi * planck_lambda(lam, t) * (rad / d) ** 2 * area * eta * lam / (H * C)
        s += g * (1 if k in (0, n) else (4 if k % 2 else 2))
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
    rh = RINF / (1 + ME / MP)
    r["RH"] = rh
    r["lyman"] = {n: 1e9 / (rh * (1 - 1 / n ** 2)) for n in (2, 3, 4)}
    r["limite"] = 1e9 / rh
    r["E_lya_eV"] = H * C / (r["lyman"][2] * 1e-9) / EV
    r["rate"] = tasa_fotones(2000)
    r["rate2"] = tasa_fotones(4000)
    s, b = r["rate"], 0.5
    r["S"], r["B"] = s, b
    r["t10"] = 100 * (s + b) / s ** 2
    rng = random.Random(20261109)
    mu = s * 100.0
    r["mu100"] = mu
    xs = [poisson(rng, mu) for _ in range(2000)]
    mean = sum(xs) / len(xs)
    var = sum((x - mean) ** 2 for x in xs) / (len(xs) - 1)
    r["mc_mean"], r["mc_std"] = mean, math.sqrt(var)
    t = r["t10"]
    sn = []
    for _ in range(2000):
        tot = poisson(rng, (s + b) * t)
        sn.append(tot - b * t)
    m2 = sum(sn) / len(sn)
    sd2 = math.sqrt(sum((x - m2) ** 2 for x in sn) / (len(sn) - 1))
    r["sn_mc"] = m2 / sd2
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"R_H = {r['RH']:.3f} 1/m")
    for n, v in r["lyman"].items():
        print(f"Lyman n={n}->1: {v:.4f} nm")
    print(f"limite de la serie: {r['limite']:.4f} nm ; energia de Lyman-alfa = {r['E_lya_eV']:.4f} eV")
    print(f"tasa de fotones detectados (2000 pasos) = {r['rate']:.6f} /s ; (4000 pasos) = {r['rate2']:.6f} /s")
    print(f"esperado en 100 s: {r['mu100']:.2f} ; Monte Carlo: media = {r['mc_mean']:.2f}, desviacion = {r['mc_std']:.3f} (sqrt = {math.sqrt(r['mu100']):.3f})")
    print(f"tiempo para S/N = 10 con fondo 0.5 /s: t = {r['t10']:.2f} s ; S/N simulada = {r['sn_mc']:.2f}")
    assert abs(r["lyman"][2] - 121.567) < 0.01
    assert abs(r["rate"] - r["rate2"]) / r["rate"] < 1e-9
    assert abs(r["mc_mean"] - r["mu100"]) / r["mu100"] < 0.01
    assert abs(r["mc_std"] / math.sqrt(r["mu100"]) - 1) < 0.05
    assert abs(r["sn_mc"] - 10) < 0.6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
