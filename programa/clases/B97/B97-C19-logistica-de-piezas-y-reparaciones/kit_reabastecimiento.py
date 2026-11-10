#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C19: kit de repuestos y frecuencia de reabastecimiento de una base robotica.

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): mision de 720 dias; 3 tipos de unidad con cantidad, tasa de falla (por 10 000 h) y masa;
costo fijo por vuelo de reabastecimiento de 10 kg equivalentes; confianza de mision 95 %; fallas de Poisson independientes; 100000 misiones simuladas, semilla fija.
Modelo: por intervalo de tau dias, mu_i = n_i lambda_i 24 tau / 10000; stock inicial s_i tal que P(X_i <= s_i) >= q con q = 0.95^(1/(k * 3)) (k intervalos);
masa total = stock inicial + k F + consumo esperado (constante). Tras cada reabastecimiento el stock vuelve a s_i.
Segunda via: simulacion de la mision completa (tolerancia 3 sigma binomial) frente a la confianza analitica producto de las probabilidades por intervalo y tipo.
Unidades: dias, horas y kg. Sin retrasos de entrega ni fallas del propio vuelo; reabastecimiento instantaneo al final de cada intervalo.
"""
from __future__ import annotations
import math, platform, random

DIAS, F_VUELO, CONF, NSIM, SEMILLA = 720, 10.0, 0.95, 100000, 20261110              # SINTETICOS
TIPOS = [("motor", 6, 1.2, 4.0), ("controlador", 2, 0.8, 1.5), ("junta", 4, 0.9, 3.2)]   # nombre, n, lambda [1/10000 h], masa [kg]
INTERVALOS = (30, 60, 90, 120, 180, 240, 360, 720)


def cdf(mu, s):
    return sum(math.exp(-mu) * mu ** k / math.factorial(k) for k in range(s + 1))


def plan(tau):
    k = DIAS // tau
    q = CONF ** (1.0 / (k * len(TIPOS)))
    st, mus = [], []
    for _, n, lam, _ in TIPOS:
        mu = n * lam * 24 * tau / 10000.0
        mus.append(mu)
        st.append(next(s for s in range(500) if cdf(mu, s) >= q))
    masa_stock = sum(s * t[3] for s, t in zip(st, TIPOS))
    consumo = sum(mu * t[3] for mu, t in zip(mus, TIPOS)) * k
    conf = 1.0
    for mu, s in zip(mus, st):
        conf *= cdf(mu, s) ** k
    return dict(tau=tau, k=k, st=st, mus=mus, stock=masa_stock, vuelos=(k - 1) * F_VUELO, consumo=consumo, total=masa_stock + (k - 1) * F_VUELO + consumo, conf=conf)


def simular(p, rng):
    ok = 0
    for _ in range(NSIM):
        bien = True
        for _k in range(p["k"]):
            for mu, s in zip(p["mus"], p["st"]):
                # Poisson por inversion
                u, x, term = rng.random(), 0, math.exp(-mu)
                acum = term
                while u > acum:
                    x += 1
                    term *= mu / x
                    acum += term
                if x > s:
                    bien = False
        ok += bien
    return ok / NSIM


def calc():
    planes = [plan(t) for t in INTERVALOS]
    mejor = min(planes, key=lambda p: p["total"])
    sim = simular(mejor, random.Random(SEMILLA))
    sig = math.sqrt(mejor["conf"] * (1 - mejor["conf"]) / NSIM)
    sin_vuelos = planes[-1]
    return dict(planes=planes, mejor=mejor, sim=sim, z=abs(sim - mejor["conf"]) / sig, tau_opt=mejor["tau"], total_opt=mejor["total"], stock_opt=mejor["stock"],
                total_720=sin_vuelos["total"], stock_720=sin_vuelos["stock"], total_30=planes[0]["total"], ahorro=sin_vuelos["total"] - mejor["total"],
                conf_opt=mejor["conf"], k_opt=mejor["k"], consumo=mejor["consumo"])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: mision de {DIAS} dias; costo por vuelo {F_VUELO:.0f} kg; confianza de mision {100*CONF:.0f} %; semilla {SEMILLA}")
    print(" tau [d]  intervalos  stock [kg]  vuelos [kg]  consumo [kg]  total [kg]  confianza analitica")
    for p in r["planes"]:
        print(f"{p['tau']:7d} {p['k']:10d} {p['stock']:11.1f} {p['vuelos']:12.1f} {p['consumo']:13.1f} {p['total']:11.1f} {100*p['conf']:15.2f} %")
    print(f"Intervalo de masa total minima: {r['tau_opt']} d ({r['k_opt']} intervalos); total = {r['total_opt']:.1f} kg frente a {r['total_720']:.1f} kg sin reabastecimiento (ahorro {r['ahorro']:.1f} kg)")
    print(f"Simulacion de la mision con ese plan: confianza = {100*r['sim']:.2f} % (analitica {100*r['conf_opt']:.2f} %; {r['z']:.2f} sigma)")
    assert r["z"] < 3 and all(p["conf"] >= CONF - 1e-9 for p in r["planes"]) and 0 < r["tau_opt"] < DIAS
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
