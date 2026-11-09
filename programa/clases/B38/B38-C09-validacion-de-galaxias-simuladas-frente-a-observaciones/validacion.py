#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C09: validar una funcion de masa estelar simulada frente a una referencia: residuos en dex, chi cuadrado, ajuste y prueba de Kolmogorov-Smirnov.

Datos: ninguna constante fisica ni catalogo. Las dos funciones de Schechter (referencia: log M* = 10,66, alfa = -1,25; simulacion: log M* = 10,95, alfa = -1,45), la normalizacion, el rango 1e8-10^11,5 Msol,
el tamano de las muestras y la semilla 20261109 son ILUSTRATIVOS (sinteticos); la "referencia" NO es una medida real ni la "simulacion" una simulacion real. Del proyecto EAGLE (Schaye et al.)
solo se leyo el resumen (2026-11-09): afirma un acuerdo de la funcion de masa estelar dentro de ~0,2 dex entre 1e8 y 1e11 Msol tras calibrar la retroalimentacion; aqui se usa 0,2 dex solo como UMBRAL DE EJEMPLO.
Modelo: Phi(M) dlogM = ln10 Phi* (M/M*)^(alfa+1) exp(-M/M*) dlogM; muestras por rechazo; residuo en dex = log10(N_sim/N_ref) por intervalo; chi2 de Poisson; ajuste de log M* por
barrido; KS de dos muestras con la serie asintotica de Kolmogorov. Separacion de la muestra en calibracion y prueba para evitar ajustar y validar con los mismos datos.
Supuestos: muestras independientes, sin errores de masa ni incompletitud. Validez: ilustrativa.
Tolerancia: la simulacion sin ajustar debe rechazarse (p < 0,01) y superar 0,2 dex en algun intervalo; ajustar solo M* deja un chi2 reducido de prueba mayor que 10, ajustar M* y alfa lo baja de 3 y la simulacion calibrada no se rechaza (p > 0,01); la autocomparacion no se rechaza (p > 0,01).
"""
from __future__ import annotations
import math, platform, random, sys

LOGMIN, LOGMAX = 8.0, 11.5
NB = 7
BORDES = [8.0 + 0.5 * k for k in range(NB + 1)]

def schechter_dlogm(logm, logms, alfa):
    x = 10 ** (logm - logms)
    return math.log(10) * x ** (alfa + 1) * math.exp(-x)

def muestra(rng, n, logms, alfa):
    # rechazo con envolvente constante (maximo en el borde bajo para alfa < -1 es el del extremo inferior)
    fmax = max(schechter_dlogm(LOGMIN + 0.001 * k, logms, alfa) for k in range(4000))
    out = []
    while len(out) < n:
        lm = rng.uniform(LOGMIN, LOGMAX)
        if rng.random() * fmax <= schechter_dlogm(lm, logms, alfa):
            out.append(lm)
    return out

def esperado(logms, alfa, ntot):
    # integral por Simpson en cada intervalo, normalizada al total
    def integ(a, b, n=400):
        h = (b - a) / n
        s = schechter_dlogm(a, logms, alfa) + schechter_dlogm(b, logms, alfa)
        for i in range(1, n):
            s += (4 if i % 2 else 2) * schechter_dlogm(a + i * h, logms, alfa)
        return s * h / 3
    por_bin = [integ(BORDES[k], BORDES[k + 1]) for k in range(NB)]
    tot = sum(por_bin)
    return [ntot * v / tot for v in por_bin]

def cuentas(m):
    c = [0] * NB
    for x in m:
        k = min(int((x - LOGMIN) / 0.5), NB - 1)
        c[k] += 1
    return c

def ks2(a, b):
    a, b = sorted(a), sorted(b)
    na, nb = len(a), len(b)
    i = j = 0
    d = 0.0
    while i < na and j < nb:
        if a[i] <= b[j]:
            i += 1
        else:
            j += 1
        d = max(d, abs(i / na - j / nb))
    ne = na * nb / (na + nb)
    lam = (math.sqrt(ne) + 0.12 + 0.11 / math.sqrt(ne)) * d
    p = 0.0
    for k in range(1, 101):
        p += 2 * (-1) ** (k - 1) * math.exp(-2 * k * k * lam * lam)
    return d, min(max(p, 0.0), 1.0)

def chi2(obs, esp):
    return sum((o - e) ** 2 / e for o, e in zip(obs, esp) if e > 0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    ref = muestra(rng, 20000, 10.66, -1.25)
    sim = muestra(rng, 20000, 10.95, -1.45)
    ref2 = muestra(rng, 20000, 10.66, -1.25)
    cr, cs = cuentas(ref), cuentas(sim)
    print(f"{'log M*':>11} {'N ref':>7} {'N sim':>7} {'residuo [dex]':>14}")
    peor = 0.0
    for k in range(NB):
        r = math.log10(cs[k] / cr[k])
        peor = max(peor, abs(r))
        print(f"{BORDES[k]:4.1f}-{BORDES[k + 1]:4.1f} {cr[k]:7d} {cs[k]:7d} {r:14.3f}")
    d, p = ks2(ref, sim)
    print(f"sim sin ajustar: residuo maximo {peor:.3f} dex, KS D = {d:.4f}, p = {p:.2e}")
    assert p < 0.01 and peor > 0.2
    d0, p0 = ks2(ref, ref2)
    print(f"autocomparacion de dos muestras de la referencia: KS D = {d0:.4f}, p = {p0:.3f}")
    assert p0 > 0.01
    # calibracion y prueba: la referencia se parte en dos mitades
    cal_ref, pru_ref = ref[:10000], ref[10000:]
    cc, cp = cuentas(cal_ref), cuentas(pru_ref)
    # (a) ajustar solo M* con la pendiente de la simulacion fija
    mejor_a = min(((chi2(cc, esperado(10.40 + 0.02 * k, -1.45, len(cal_ref))), 10.40 + 0.02 * k) for k in range(0, 51)))
    # (b) ajustar M* y alfa
    mejor_b = None
    for k in range(0, 36):
        for q in range(0, 21):
            lm, al = 10.40 + 0.02 * k, -1.55 + 0.02 * q
            c = chi2(cc, esperado(lm, al, len(cal_ref)))
            if mejor_b is None or c < mejor_b[0]:
                mejor_b = (c, lm, al)
    print(f"ajuste solo de M* (alfa = -1,45): log M* = {mejor_a[1]:.2f}, chi2 de calibracion {mejor_a[0]:.1f}")
    print(f"ajuste de M* y alfa: log M* = {mejor_b[1]:.2f}, alfa = {mejor_b[2]:.2f}, chi2 de calibracion {mejor_b[0]:.1f}")
    ra = chi2(cp, esperado(mejor_a[1], -1.45, len(pru_ref))) / (NB - 1)
    rb = chi2(cp, esperado(mejor_b[1], mejor_b[2], len(pru_ref))) / (NB - 2)
    r0 = chi2(cp, esperado(10.95, -1.45, len(pru_ref))) / NB
    print(f"chi2 reducido en la muestra de prueba: sin ajustar {r0:.1f}; solo M* {ra:.1f}; M* y alfa {rb:.2f}")
    assert r0 > ra > 10 > 3 > rb
    sim_cal = muestra(rng, 20000, mejor_b[1], mejor_b[2])
    dk, pk = ks2(sim_cal, pru_ref)
    print(f"simulacion calibrada frente a la mitad de prueba: KS D = {dk:.4f}, p = {pk:.3f}")
    assert pk > 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
