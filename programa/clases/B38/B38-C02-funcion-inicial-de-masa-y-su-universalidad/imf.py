#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C02: funcion inicial de masa (Salpeter, Kroupa por tramos, Chabrier) y dispersion de la pendiente.

Datos: ninguna constante fisica. Las formas funcionales (Salpeter indice 2,35; Kroupa con indices 0,3 / 1,3 / 2,3 y cortes en 0,08 y 0,5 Msol; Chabrier lognormal
bajo 1 Msol con mu = 0,08 y sigma = 0,69 en log10 y cola 2,3) son convenciones ESTANDAR NO VERIFICADAS EN EL TEXTO: solo se leyeron los resumenes de Kroupa (2001) y de
Chabrier (2003), consultados el 2026-11-09. Los rangos de masa (0,08-100 Msol), el tamano de las muestras y la semilla 20261109 son ILUSTRATIVOS (sinteticos).
Modelo: xi(m) = dN/dm continua en los cortes; momentos por integracion analitica (potencias) frente a integracion numerica de Simpson (dos vias independientes);
muestreo por transformada inversa; pendiente de la cola m > 1 Msol por maxima verosimilitud alpha = 1 + n / sum(ln(m_i/m_min)), con error (alpha - 1)/sqrt(n).
Supuestos: IMF unica e igual para todas las muestras. Validez: ilustrativa.
Tolerancia: momentos analitico y numerico a 1e-6 relativo; la pendiente estimada debe estar a menos de 3 sigma del valor de entrada en todas las muestras.
"""
from __future__ import annotations
import math, platform, random, sys

CORTES = [0.08, 0.5]
INDICES = [0.3, 1.3, 2.3]
MLO, MHI = 0.08, 100.0

def kroupa_coef():
    # continuidad en los cortes con k3 = 1
    k3 = 1.0
    k2 = k3 * CORTES[1] ** (-INDICES[2] + INDICES[1])
    k1 = k2 * CORTES[0] ** (-INDICES[1] + INDICES[0])
    return [k1, k2, k3]

def xi_kroupa(m):
    k = kroupa_coef()
    if m < CORTES[0]:
        return k[0] * m ** -INDICES[0]
    if m < CORTES[1]:
        return k[1] * m ** -INDICES[1]
    return k[2] * m ** -INDICES[2]

def xi_salpeter(m):
    return m ** -2.35

def xi_chabrier(m):
    if m < 1.0:
        return 0.158 / (m * math.log(10)) * math.exp(-((math.log10(m) - math.log10(0.08)) ** 2) / (2 * 0.69 ** 2))
    c1 = 0.158 / math.log(10) * math.exp(-((math.log10(1.0) - math.log10(0.08)) ** 2) / (2 * 0.69 ** 2))
    return c1 * m ** -2.3

def momento_analitico_kroupa(p, a, b):
    """integral de m^p xi(m) dm entre a y b (potencias por tramos)."""
    k = kroupa_coef()
    tramos = [(MLO, CORTES[0], k[0], INDICES[0]), (CORTES[0], CORTES[1], k[1], INDICES[1]), (CORTES[1], MHI, k[2], INDICES[2])]
    tot = 0.0
    for lo, hi, kk, al in tramos:
        l, h = max(lo, a), min(hi, b)
        if h <= l:
            continue
        e = p - al + 1
        tot += kk * (h ** e - l ** e) / e
    return tot

def simpson_log(f, a, b, n=20000):
    """integral por Simpson en variable u = ln m."""
    la, lb = math.log(a), math.log(b)
    h = (lb - la) / n
    g = lambda u: f(math.exp(u)) * math.exp(u)
    s = g(la) + g(lb)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(la + i * h)
    return s * h / 3

def muestra_cola(rng, n, alpha, m0=1.0, m1=MHI):
    a = 1 - alpha
    return [(m0 ** a + rng.random() * (m1 ** a - m0 ** a)) ** (1 / a) for _ in range(n)]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'IMF':>10} {'N total':>9} {'<m>':>8} {'f(N,m>8)':>10} {'f(M,m>8)':>10}")
    for nombre, f in (("Salpeter", xi_salpeter), ("Kroupa", xi_kroupa), ("Chabrier", xi_chabrier)):
        n0 = simpson_log(f, MLO, MHI)
        m0 = simpson_log(lambda m: m * f(m), MLO, MHI)
        nm8 = simpson_log(f, 8, MHI)
        mm8 = simpson_log(lambda m: m * f(m), 8, MHI)
        print(f"{nombre:>10} {n0:9.4f} {m0 / n0:8.4f} {nm8 / n0:10.5f} {mm8 / m0:10.5f}")
    # dos vias para Kroupa
    for p, a, b in ((0, MLO, MHI), (1, MLO, MHI), (0, 8, MHI), (1, 8, MHI), (1, 0.08, 0.5)):
        ana = momento_analitico_kroupa(p, a, b)
        num = simpson_log(lambda m: m ** p * xi_kroupa(m), a, b, 200000)
        assert abs(ana - num) / ana < 1e-6, (p, a, b, ana, num)
    n_tot = momento_analitico_kroupa(0, MLO, MHI)
    m_tot = momento_analitico_kroupa(1, MLO, MHI)
    n_sn = momento_analitico_kroupa(0, 8, MHI)
    m_sn = momento_analitico_kroupa(1, 8, MHI)
    print(f"Kroupa: estrellas > 8 Msol por Msol formada = {n_sn / m_tot:.6f}  (una por {m_tot / n_sn:.1f} Msol)")
    print(f"Kroupa: masa en m > 8 Msol / masa total = {m_sn / m_tot:.5f}")
    # dispersion de la pendiente de la cola
    rng = random.Random(20261109)
    print(f"{'n(m>1)':>8} {'alpha_est':>10} {'error':>8} {'desv/sigma':>11}")
    alpha_in = 2.3
    for n in (30, 100, 1000, 10000):
        xs = muestra_cola(rng, n, alpha_in)
        est = 1 + n / sum(math.log(x) for x in xs)
        err = (est - 1) / math.sqrt(n)
        z = (est - alpha_in) / err
        print(f"{n:8d} {est:10.4f} {err:8.4f} {z:11.2f}")
        assert abs(z) < 3
    # muchos clusteres pequenos: la dispersion observada iguala a la de Poisson
    ests = []
    for _ in range(400):
        xs = muestra_cola(rng, 50, alpha_in)
        ests.append(1 + 50 / sum(math.log(x) for x in xs))
    mu = sum(ests) / len(ests)
    sd = math.sqrt(sum((e - mu) ** 2 for e in ests) / (len(ests) - 1))
    esperado = (alpha_in - 1) / math.sqrt(50)
    print(f"400 cumulos de 50 estrellas: pendiente media {mu:.3f}, dispersion {sd:.3f}, esperada por Poisson {esperado:.3f}")
    assert 0.8 < sd / esperado < 1.25
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
