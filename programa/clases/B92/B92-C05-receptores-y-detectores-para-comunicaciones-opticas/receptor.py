#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C05: receptor PPM de conteo de fotones (error de simbolo) y tiempo muerto del detector.

Datos consultados (2026-11-10): ranuras de 0.125 a 512 ns y modulacion de intensidad por todo o nada (OOK) en la capa
fisica, con PPM como modulacion de la capa de codificacion (CCSDS 141.0-B-1, sec. 3.7 y 3.9); ordenes PPM
{4, 8, 16, 32, 64, 128, 256} (CCSDS 142.0-B-1, sec. 3.8.5). Como contexto: el receptor de DSOC en Palomar usa un
receptor de conteo de fotones de nanohilos superconductores (NASA/JPL, pagina de DSOC), sin mas especificaciones.
ILUSTRATIVOS (sinteticos, no medidos): fotones de fondo por ranura nb = 0.1, eficiencia de deteccion 0.8, tiempo muerto 20 ns.
Modelo: canal de Poisson; en la ranura con pulso el conteo es Poisson(ns + nb) y en las otras M-1, Poisson(nb);
el receptor elige la ranura de mayor conteo y desempata al azar. Con nb = 0: SER = (M-1)/M exp(-ns).
Tiempo muerto no paralizable: tasa medida = R/(1 + R tau); paralizable: R exp(-R tau).
Segunda via: Monte Carlo (random.Random(92)); caso nb = 0 analitico; simulacion de eventos para el tiempo muerto.
Tolerancia: exacto frente a Monte Carlo 4 desviaciones estandar del propio Monte Carlo (20000 simbolos); nb = 0 frente a analitico 1e-12.
"""
from __future__ import annotations
import math, platform, random


def pmf(k, lam):
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1)) if lam > 0 else (1.0 if k == 0 else 0.0)


def ser_exacta(m, ns, nb, kmax=400):
    """Probabilidad de error de simbolo con decision por maximo conteo y desempate aleatorio."""
    pb = [pmf(k, nb) for k in range(kmax)]
    cb = [0.0] * kmax
    s = 0.0
    for k in range(kmax):
        cb[k] = s            # P(B < k)
        s += pb[k]
    pc = 0.0
    for k in range(kmax):
        ps = pmf(k, ns + nb)
        if ps < 1e-18 and k > ns + nb:
            break
        inner = 0.0
        for j in range(m):
            inner += math.comb(m - 1, j) / (j + 1) * pb[k] ** j * cb[k] ** (m - 1 - j)
        pc += ps * inner
    return 1.0 - pc


def poisson(rng, lam):
    if lam <= 0:
        return 0
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def ser_mc(m, ns, nb, n, rng):
    err = 0
    for _ in range(n):
        cuentas = [poisson(rng, nb) for _ in range(m)]
        cuentas[0] = poisson(rng, ns + nb)
        mx = max(cuentas)
        cand = [i for i, c in enumerate(cuentas) if c == mx]
        if rng.choice(cand) != 0:
            err += 1
    return err / n


def ns_para(m, nb, objetivo):
    lo, hi = 0.0, 60.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if ser_exacta(m, mid, nb) > objetivo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def muerto_mc(r, tau, rng, n=100000):
    t, ultimo, cont = 0.0, -1.0, 0
    for _ in range(n):
        t += rng.expovariate(r)
        if t - ultimo >= tau:
            cont += 1
            ultimo = t
    return cont / t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nb = 0.1
    rng = random.Random(92)
    print(f"Error de simbolo PPM, M = 16, nb = {nb} fotones por ranura (ILUSTRATIVO)")
    print("  ns detectados   SER exacta   SER Monte Carlo")
    dmax = 0.0
    for ns in (2.0, 4.0, 6.0, 8.0, 10.0):
        e = ser_exacta(16, ns, nb)
        mc = ser_mc(16, ns, nb, 20000, rng)
        dmax = max(dmax, abs(e - mc) / math.sqrt(e * (1 - e) / 20000))
        print(f"  {ns:12.1f}   {e:10.3e}   {mc:10.3e}")
    print(f"Diferencia maxima exacta frente a Monte Carlo = {dmax:.2f} desviaciones estandar del Monte Carlo")
    dm0 = 0.0
    for m in (4, 16, 64):
        for ns in (1.0, 3.0, 7.0):
            dm0 = max(dm0, abs(ser_exacta(m, ns, 0.0) - (m - 1) / m * math.exp(-ns)))
    print(f"Caso sin fondo (nb = 0): diferencia con (M-1)/M exp(-ns) = {dm0:.1e}")
    print("Fotones necesarios para SER = 1e-3 con nb = 0.1 (eficiencia 0.8, ILUSTRATIVA):")
    print("   M  bits/simbolo  ns detectados  ns incidentes  incidentes por bit")
    prev = None
    for m in (4, 16, 64, 256):
        ns = ns_para(m, nb, 1e-3)
        bits = int(math.log2(m))
        print(f"  {m:3d}  {bits:11d}  {ns:13.3f}  {ns / 0.8:13.3f}  {ns / 0.8 / bits:18.3f}")
        if prev is not None:
            assert ns / bits < prev
        prev = ns / bits
    tau = 20e-9
    print(f"Tiempo muerto tau = {tau * 1e9:.0f} ns (ILUSTRATIVO)")
    print("  R [Mcps]  no paralizable  paralizable  simulacion (no paralizable)")
    dd = 0.0
    for r in (1e7, 5e7, 2e8):
        npar = r / (1 + r * tau)
        par = r * math.exp(-r * tau)
        sim = muerto_mc(r, tau, rng)
        dd = max(dd, abs(sim - npar) / npar)
        print(f"  {r / 1e6:8.0f}  {npar / 1e6:14.3f}  {par / 1e6:11.3f}  {sim / 1e6:.3f}")
    print(f"Tasa maxima medible (no paralizable) = 1/tau = {1 / tau / 1e6:.0f} Mcps ; error relativo de la simulacion = {dd:.1e}")
    assert dmax < 4.0 and dm0 < 1e-12 and dd < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
