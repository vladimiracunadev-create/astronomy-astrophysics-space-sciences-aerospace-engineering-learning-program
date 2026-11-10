#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C17: probabilidad de falla de arquitecturas 1oo1, 1oo2, 2oo2 y 2oo3, con y sin falla de causa comun.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): tasa de falla por canal 1.0e-3 /h, mision de 100 h, factor beta de causa comun 0.05, votador perfecto,
fallas independientes salvo la causa comun, 400000 misiones simuladas con semilla fija. Ninguna cifra es una tasa de falla real ni un nivel de integridad de seguridad (SIL).
Modelo: p = 1 - exp(-lambda T). 'Falla' = perdida de la funcion pedida. 1oo1: p. 1oo2 (basta un canal): ambos fallan. 2oo2 (se necesitan ambos): falla uno cualquiera.
2oo3: fallan al menos dos. Causa comun: una fraccion beta de p falla todos los canales a la vez; el resto (1 - beta) p es independiente.
Segunda via: Monte Carlo (tolerancia 3 sigma binomial) para cada arquitectura y caso.
Unidades: horas y probabilidades. Sin deteccion de fallas, sin reparacion y sin falla del votador.
"""
from __future__ import annotations
import math, platform, random

LAM, T, BETA, NSIM, SEMILLA = 1.0e-3, 100.0, 0.05, 400000, 20261110                  # SINTETICOS


def p_canal():
    return 1 - math.exp(-LAM * T)


def analitico(arq, beta):
    p = p_canal()
    q = (1 - beta) * p                                  # parte independiente
    c = beta * p                                        # causa comun
    if arq == "1oo1":
        return p
    if arq == "1oo2":
        ind = q * q
    elif arq == "2oo2":
        ind = 1 - (1 - q) ** 2
    elif arq == "2oo3":
        ind = 3 * q * q * (1 - q) + q ** 3
    return 1 - (1 - c) * (1 - ind)


def simular(arq, beta, rng):
    p = p_canal()
    n_canal = {"1oo1": 1, "1oo2": 2, "2oo2": 2, "2oo3": 3}[arq]
    fallas = 0
    for _ in range(NSIM):
        if rng.random() < beta * p:                      # causa comun
            fallas += 1
            continue
        nf = sum(rng.random() < (1 - beta) * p for _ in range(n_canal))
        if arq == "1oo1":
            f = nf >= 1
        elif arq == "1oo2":
            f = nf == 2
        elif arq == "2oo2":
            f = nf >= 1
        else:
            f = nf >= 2
        fallas += f
    return fallas / NSIM


def calc():
    rng = random.Random(SEMILLA)
    filas, ok = [], True
    for arq in ("1oo1", "1oo2", "2oo2", "2oo3"):
        for beta in (0.0, BETA):
            a = analitico(arq, beta)
            m = simular(arq, beta, rng)
            sig = math.sqrt(max(a * (1 - a), 1e-12) / NSIM)
            ok = ok and abs(m - a) <= 3 * sig + 1e-12
            filas.append((arq, beta, a, m, abs(m - a) / sig))
    d = {(f[0], f[1]): f[2] for f in filas}
    return dict(filas=filas, ok=ok, p=p_canal(), a1=d[("1oo1", 0.0)], a12=d[("1oo2", 0.0)], a22=d[("2oo2", 0.0)], a23=d[("2oo3", 0.0)],
                a12b=d[("1oo2", BETA)], a23b=d[("2oo3", BETA)], r12=d[("1oo1", 0.0)] / d[("1oo2", 0.0)], r12b=d[("1oo1", 0.0)] / d[("1oo2", BETA)],
                piso=BETA * p_canal(), zmax=max(f[4] for f in filas))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: lambda = {LAM} /h; T = {T:.0f} h -> p de un canal = {r['p']:.5f}; beta = {BETA}; {NSIM} misiones; semilla {SEMILLA}")
    print(" arquitectura   beta    analitica    Monte Carlo   |dif| en sigmas")
    for arq, b, a, m, z in r["filas"]:
        print(f"{arq:12s} {b:6.2f} {a:12.6f} {m:13.6f} {z:12.2f}")
    print(f"Mejora de 1oo2 frente a 1oo1: x{r['r12']:.1f} sin causa comun y x{r['r12b']:.1f} con beta = {BETA} (piso beta p = {r['piso']:.6f})")
    assert r["ok"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
