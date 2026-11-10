#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C12: repuestos de unidades reemplazables (ORU) con fallas de Poisson y confianza de cubrir una mision.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): 5 tipos de unidad con cantidades, tasas de falla (por 10 000 h) y masas; mision de 8760 h; confianza objetivo 95 %;
fallas independientes con tasa constante (proceso de Poisson); semilla fija y 100000 misiones simuladas. Ninguna tasa corresponde a un componente real.
Modelo: mu_i = n_i lambda_i T; P(fallas_i <= s_i) = sum_{k<=s_i} exp(-mu_i) mu_i^k / k!; confianza del conjunto = producto sobre tipos.
Metodos: (A) cada tipo con confianza >= 95 % (NO garantiza el 95 % del conjunto); (C) cada tipo con 0.95^(1/5) (garantiza el conjunto); (B) reparto voraz que sube la confianza del conjunto al 95 % con la mayor ganancia de log-confianza por kg.
Segunda via: Monte Carlo de las fallas por tiempos entre fallas exponenciales (tolerancia 0.5 % absoluta en la confianza del conjunto).
Unidades: horas, kg. Sin fallas de modo comun, sin reparacion de la unidad dañada y sin reabastecimiento durante la mision.
"""
from __future__ import annotations
import math, platform, random

T_MISION, CONF, NSIM, SEMILLA = 8760.0, 0.95, 100000, 20261110                     # SINTETICOS
TIPOS = [("motor de rueda", 6, 1.2, 4.0), ("controlador", 2, 0.8, 1.5), ("sensor de vision", 3, 2.0, 0.6),
         ("junta articular", 4, 0.9, 3.2), ("bateria", 2, 0.5, 9.0)]              # nombre, n, lambda [1/10000 h], masa [kg]


def cdf(mu, s):
    return sum(math.exp(-mu) * mu ** k / math.factorial(k) for k in range(s + 1))


def mus():
    return [n * lam / 10000.0 * T_MISION for _, n, lam, _ in TIPOS]


def metodo_a():
    return [next(s for s in range(200) if cdf(mu, s) >= CONF) for mu in mus()]


def conj(s):
    p = 1.0
    for mu, si in zip(mus(), s):
        p *= cdf(mu, si)
    return p


def metodo_b():
    s = [0] * len(TIPOS)
    while conj(s) < CONF:
        mejor = max(range(len(TIPOS)), key=lambda i: (math.log(cdf(mus()[i], s[i] + 1)) - math.log(cdf(mus()[i], s[i]))) / TIPOS[i][3])
        s[mejor] += 1
    return s


def metodo_c():
    q = CONF ** (1.0 / len(TIPOS))
    return [next(s for s in range(200) if cdf(mu, s) >= q) for mu in mus()]


def masa(s):
    return sum(si * t[3] for si, t in zip(s, TIPOS))


def simular(s):
    rng = random.Random(SEMILLA)
    lam = [n * l / 10000.0 for _, n, l, _ in TIPOS]
    ok = 0
    for _ in range(NSIM):
        bien = True
        for l, si in zip(lam, s):
            t, k = 0.0, 0
            while True:
                t += rng.expovariate(l)
                if t > T_MISION:
                    break
                k += 1
            if k > si:
                bien = False
        ok += bien
    return ok / NSIM


def calc():
    a, b, c = metodo_a(), metodo_b(), metodo_c()
    pa, pb, pc = conj(a), conj(b), conj(c)
    sim = simular(b)
    return dict(mu=mus(), a=a, b=b, c=c, pa=pa, pb=pb, pc=pc, ma=masa(a), mb=masa(b), mc=masa(c), sim=sim, dif=abs(sim - pb), ahorro=masa(c) - masa(b),
                mu_tot=sum(mus()), n_a=sum(a), n_b=sum(b), n_c=sum(c), ahorro_pct=100 * (masa(c) - masa(b)) / masa(c))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: mision de {T_MISION:.0f} h; confianza objetivo {100*CONF:.0f} %; semilla {SEMILLA}")
    print(" tipo               mu     s (A)   s (C)   s (B)  masa [kg]")
    for (n, _, _, m), mu, sa, sc, sb in zip(TIPOS, r["mu"], r["a"], r["c"], r["b"]):
        print(f"{n:18s} {mu:6.3f} {sa:6d} {sc:7d} {sb:7d} {m:9.1f}")
    print(f"(A) 95 % por tipo: {r['n_a']} repuestos, {r['ma']:.1f} kg, confianza del conjunto = {100*r['pa']:.2f} % (NO alcanza el objetivo)")
    print(f"(C) 0.95^(1/5) por tipo: {r['n_c']} repuestos, {r['mc']:.1f} kg, confianza del conjunto = {100*r['pc']:.2f} %")
    print(f"(B) voraz   : {r['n_b']} repuestos, {r['mb']:.1f} kg, confianza del conjunto = {100*r['pb']:.2f} %; ahorro frente a (C) = {r['ahorro']:.1f} kg ({r['ahorro_pct']:.1f} %)")
    print(f"Monte Carlo de (B): {100*r['sim']:.2f} %; diferencia con el calculo exacto = {100*r['dif']:.3f} puntos")
    assert r["dif"] < 0.005 and r["pb"] >= CONF and r["pc"] >= CONF and r["pa"] < CONF and r["mb"] <= r["mc"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
