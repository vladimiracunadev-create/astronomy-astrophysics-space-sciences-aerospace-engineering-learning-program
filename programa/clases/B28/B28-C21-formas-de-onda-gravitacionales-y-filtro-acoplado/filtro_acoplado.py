#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C21: forma de onda newtoniana de un chirrido, filtro acoplado y desajuste de un banco de plantillas.

Datos: G, c (NIST CODATA 2022) y GM_sol (IAU 2015 B3), consultados 2026-11-09. Contexto: GW150914 se detecto con un filtro acoplado de
relacion senal-ruido 24 (arXiv:1602.03837, resumen, consultado 2026-11-09). La masa de chirrido de 10 Msol, la frecuencia inicial
(30 Hz), la final (400 Hz), la tasa de muestreo (2048 Hz) y la senal-ruido objetivo (10) son ILUSTRATIVAS (sinteticas); el ruido es blanco gaussiano.
Modelo (orden newtoniano, circular, de frente): con tau = t_c - t, frecuencia f(tau) = (1/pi) (5/(256 tau))^(3/8) (G Mc/c^3)^(-5/8), fase
phi(tau) = -2 (5 G Mc/c^3)^(-5/8) tau^(5/8) y amplitud proporcional a (pi G Mc f/c^3)^(2/3); h = A cos(phi). Filtro acoplado con tiempo de
coalescencia conocido: rho(Mc') = Sum d h'/sqrt(Sum h'^2); desajuste: M(Mc') = Sum h h'/sqrt(Sum h^2 Sum h'^2).
Supuestos: ruido blanco, orden newtoniano, sin espines ni excentricidad, tiempo conocido. Validez: ilustrativa.
Tolerancia: 1e-3 relativa entre la frecuencia instantanea (derivada numerica de la fase) y la formula; media del filtro dentro de 3 errores de rho.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

G, C = 6.67430e-11, 299792458.0
GM_SOL = 1.3271244e20
FS = 2048.0
F_LOW, F_HIGH = 30.0, 400.0


def tc_masa(mc):
    return G * mc / C ** 3


def frecuencia(tau, mc):
    return (1 / math.pi) * (5 / (256 * tau)) ** 0.375 * tc_masa(mc) ** -0.625


def fase(tau, mc):
    return -2 * (5 * tc_masa(mc)) ** -0.625 * tau ** 0.625


def tau_de_f(f, mc):
    return 5 / 256 * (math.pi * f) ** (-8 / 3) * tc_masa(mc) ** (-5 / 3)


def plantilla(mc, taus):
    out = []
    for tau in taus:
        f = frecuencia(tau, mc)
        if f < F_LOW or f > F_HIGH:
            out.append(0.0)
        else:
            out.append((math.pi * tc_masa(mc) * f) ** (2 / 3) * math.cos(fase(tau, mc)))
    return out


def prod(a, b):
    return sum(x * y for x, y in zip(a, b))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mc0 = 10 * GM_SOL / G
    t_start = tau_de_f(F_LOW, mc0)
    n = int(t_start * FS)
    taus = [t_start - i / FS for i in range(n)]
    taus = [t for t in taus if t > 0.5 / FS]
    h0 = plantilla(mc0, taus)
    print(f"Mc = 10 Msol: tau(30 Hz) = {t_start:.4f} s ; muestras = {len(taus)} ; f(tau final) = {frecuencia(taus[-1], mc0):.1f} Hz")
    # comprobacion: frecuencia instantanea a partir de la derivada numerica de la fase
    for tau in (1.0, 0.3, 0.05):
        dt = 1e-6 * tau
        fn = -(fase(tau + dt, mc0) - fase(tau - dt, mc0)) / (2 * dt) / (2 * math.pi)
        fa = frecuencia(tau, mc0)
        assert abs(fn / fa - 1) < 1e-3, "frecuencia instantanea"
        print(f"tau = {tau:5.2f} s: f formula = {fa:8.3f} Hz ; derivada numerica de la fase = {fn:8.3f} Hz")
    norma = math.sqrt(prod(h0, h0))
    rho_obj = 10.0
    amp = rho_obj / norma
    print(f"norma de la plantilla = {norma:.4f} ; amplitud para rho = {rho_obj}: {amp:.4f}")
    rng = random.Random(20261109)
    sal = []
    for _ in range(200):
        d = [amp * x + rng.gauss(0, 1) for x in h0]
        sal.append(prod(d, h0) / norma)
    media, desv = statistics.mean(sal), statistics.pstdev(sal)
    print(f"filtro acoplado con la plantilla exacta, 200 realizaciones: media = {media:.3f} (esperada {rho_obj}) ; desviacion = {desv:.3f} (esperada 1)")
    assert abs(media - rho_obj) < 3 / math.sqrt(200) + 0.05 and abs(desv - 1) < 0.15
    # solo ruido: media 0, desviacion 1
    sr = []
    for _ in range(200):
        d = [rng.gauss(0, 1) for _ in h0]
        sr.append(prod(d, h0) / norma)
    print(f"solo ruido: media = {statistics.mean(sr):.3f} ; desviacion = {statistics.pstdev(sr):.3f}")
    # desajuste con el banco
    print(f"{'Mc/Mc0':>8} {'desajuste M':>12} {'SNR recuperada':>15}")
    resultados = {}
    for r in (0.97, 0.99, 0.995, 1.0, 1.005, 1.01, 1.03):
        hp = plantilla(r * mc0, taus)
        nh = math.sqrt(prod(hp, hp))
        m = prod(h0, hp) / (norma * nh) if nh > 0 else 0.0
        resultados[r] = m
        print(f"{r:8.3f} {m:12.4f} {rho_obj * m:15.3f}")
    assert abs(resultados[1.0] - 1.0) < 1e-12
    assert resultados[0.99] < 1 and resultados[1.01] < 1
    # espaciado del banco para M >= 0.97
    lo, hi = 1.0, 1.1
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        hp = plantilla(mid * mc0, taus)
        m = prod(h0, hp) / (norma * math.sqrt(prod(hp, hp)))
        if m > 0.97:
            lo = mid
        else:
            hi = mid
    print(f"desajuste 0.97 (perdida de SNR del 3 %) para Mc'/Mc = {lo:.4f} (espaciado relativo ~ {abs(lo - 1) * 100:.2f} %) con el tiempo de coalescencia fijo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
