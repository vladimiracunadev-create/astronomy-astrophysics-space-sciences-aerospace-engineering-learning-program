#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C19: periodograma de Lomb-Scargle, funcion ventana y alias en series con muestreo irregular.

Datos: ninguna constante fisica. Contexto: VanderPlas presenta una introduccion conceptual al periodograma de Lomb-Scargle como algoritmo para detectar senales
periodicas en datos con muestreo desigual (arXiv:1703.09824, resumen, consultado 2026-11-09). La frecuencia de la senal (0.37 ciclos/d), la amplitud, el ruido, el
calendario nocturno (40 dias, 70 % de noches) y los numeros de ensayos son ILUSTRATIVOS (sinteticos).
Modelo: potencia clasica P(w) = 1/2 {[Sum y cos w(t - tau)]^2/Sum cos^2 w(t - tau) + [Sum y sen w(t - tau)]^2/Sum sen^2 w(t - tau)}, tan 2 w tau = Sum sen 2wt/Sum cos 2wt;
es igual a (chi^2_0 - chi^2_min)/2 de un ajuste por minimos cuadrados de a cos wt + b sen wt (comprobacion independiente por ecuaciones normales).
Funcion ventana W(f) = |Sum exp(-2 pi i f t)|/N; con ruido gaussiano de varianza conocida sigma^2, z = P/sigma^2 sigue una exponencial de media 1 (Scargle 1982).
Supuestos: ruido blanco gaussiano, series sin media. Validez: ilustrativa.
Tolerancia: potencia por la formula y por minimos cuadrados con 1e-9 relativo; media de z bajo el ruido dentro de 3 errores de 1; fraccion de z > 3 dentro de 4 desviaciones de exp(-3).
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

F0, AMP, SIG = 0.37, 1.0, 1.0


def ls_potencia(ts, ys, f):
    w = 2 * math.pi * f
    s2 = sum(math.sin(2 * w * t) for t in ts)
    c2 = sum(math.cos(2 * w * t) for t in ts)
    tau = math.atan2(s2, c2) / (2 * w)
    cs = [math.cos(w * (t - tau)) for t in ts]
    sn = [math.sin(w * (t - tau)) for t in ts]
    a = sum(y * c for y, c in zip(ys, cs)) ** 2 / sum(c * c for c in cs)
    b = sum(y * s for y, s in zip(ys, sn)) ** 2 / sum(s * s for s in sn)
    return 0.5 * (a + b)


def ls_minimos_cuadrados(ts, ys, f):
    w = 2 * math.pi * f
    c = [math.cos(w * t) for t in ts]
    s = [math.sin(w * t) for t in ts]
    scc, sss, scs = sum(x * x for x in c), sum(x * x for x in s), sum(a * b for a, b in zip(c, s))
    syc, sys_ = sum(y * x for y, x in zip(ys, c)), sum(y * x for y, x in zip(ys, s))
    det = scc * sss - scs * scs
    a = (syc * sss - sys_ * scs) / det
    b = (sys_ * scc - syc * scs) / det
    chi0 = sum(y * y for y in ys)
    chi = sum((y - a * ci - b * si) ** 2 for y, ci, si in zip(ys, c, s))
    return 0.5 * (chi0 - chi)


def ventana(ts, f):
    re = sum(math.cos(2 * math.pi * f * t) for t in ts)
    im = sum(math.sin(2 * math.pi * f * t) for t in ts)
    return math.hypot(re, im) / len(ts)


def calendario(rng, dias=40, frac=0.7, por_noche=3):
    ts = []
    for d in range(dias):
        if rng.random() < frac:
            for _ in range(por_noche):
                ts.append(d + rng.uniform(0.0, 0.3))
    return sorted(ts)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ts = calendario(rng)
    n = len(ts)
    ys = [AMP * math.cos(2 * math.pi * F0 * t + 0.6) + rng.gauss(0, SIG) for t in ts]
    m = statistics.mean(ys)
    ys = [y - m for y in ys]
    print(f"{n} medidas en 40 dias (noches con datos con probabilidad 0.7, 3 medidas por noche)")
    for f in (0.05, 0.37, 0.63, 1.37, 2.9):
        a, b = ls_potencia(ts, ys, f), ls_minimos_cuadrados(ts, ys, f)
        assert abs(a / b - 1) < 1e-9, f"LS frente a minimos cuadrados en f={f}"
    print("Lomb-Scargle clasico = minimos cuadrados de una sinusoide (diferencia relativa < 1e-9) en cinco frecuencias")
    fs = [0.02 + 0.002 * i for i in range(1500)]
    pot = [ls_potencia(ts, ys, f) for f in fs]
    orden = sorted(range(len(fs)), key=lambda i: -pot[i])
    picos = []
    for i in orden:
        if all(abs(fs[i] - fp) > 0.05 for fp, _ in picos):
            picos.append((fs[i], pot[i]))
        if len(picos) == 4:
            break
    print(f"{'pico':>5} {'f [1/d]':>9} {'P(f)':>9} {'P/sigma^2':>10}")
    for k, (f, p) in enumerate(picos, 1):
        print(f"{k:5d} {f:9.3f} {p:9.3f} {p / SIG ** 2:10.3f}")
    f_best = picos[0][0]
    print(f"frecuencia verdadera = {F0} ; pico principal en {f_best:.3f} ; alias esperados en {F0 + 1:.2f} y {1 - F0:.2f}")
    print(f"{'f [1/d]':>8} {'ventana W(f)':>13}")
    for f in (0.0, 0.5, 1.0, 1.5, 2.0):
        print(f"{f:8.1f} {ventana(ts, f):13.3f}")
    # distribucion bajo el ruido
    z = []
    for _ in range(4000):
        yr = [rng.gauss(0, SIG) for _ in ts]
        z.append(ls_potencia(ts, yr, F0) / SIG ** 2)
    mz = statistics.mean(z)
    se = statistics.pstdev(z) / math.sqrt(len(z))
    frac = sum(1 for x in z if x > 3) / len(z)
    esp = math.exp(-3)
    sd = math.sqrt(esp * (1 - esp) / len(z))
    print(f"ruido puro, f = {F0}: media de z = {mz:.4f} +/- {se:.4f} (esperada 1) ; fraccion con z > 3 = {frac:.4f} (esperada exp(-3) = {esp:.4f} +/- {sd:.4f})")
    assert abs(mz - 1) < 3 * se + 0.01 and abs(frac - esp) < 4 * sd, "distribucion del ruido"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
