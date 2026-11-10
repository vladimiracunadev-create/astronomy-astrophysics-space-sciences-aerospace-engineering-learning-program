#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C03: puntos de equilibrio de Lagrange L1-L5 en tres sistemas.

Datos consultados (2026-11-10): GM del Sol 132 712 x 10^6 km3/s2 (NASA/NSSDC, Sun Fact Sheet, 2024-05-09);
GM de Jupiter 126.687 x 10^6 km3/s2 (NASA/NSSDC, Jupiter Fact Sheet, 2024-10-02); GM de la Luna 4902.800 km3/s2 y
semieje de la Luna 384 400 km (JPL SSD); distancia Sol-Tierra 149.6 x 10^6 km y distancia Sol-Jupiter 778.5 x 10^6 km
(NASA/NSSDC, Planetary Fact Sheet, 2025-03-18); distancia de Webb a la Tierra "unos 1.5 millones de km" (NASA, pagina de la orbita de Webb).
GM de la Tierra ~ 398 600 km3/s2: deducido de la masa de la tabla de planetas del JPL (aproximado).
Marco sinodico baricentrico adimensional; primarios en (-mu, 0) y (1-mu, 0). Los puntos son equilibrios del potencial efectivo Omega.
Segunda via: biseccion frente a Newton (colineales) y aproximacion de Hill (L1, L2 ~ +-(mu/3)^(1/3)). Tolerancias: gradiente < 1e-12; biseccion-Newton < 1e-12.
"""
from __future__ import annotations
import json, math, platform, sys

GM = {"Sol": 132712e6, "Jupiter": 126.687e6, "Tierra": 398600.0, "Luna": 4902.800}
SISTEMAS = {  # nombre: (GM1, GM2, distancia entre primarios en km)
    "Tierra-Luna": (GM["Tierra"], GM["Luna"], 384400.0),
    "Sol-Tierra": (GM["Sol"], GM["Tierra"], 149.6e6),
    "Sol-Jupiter": (GM["Sol"], GM["Jupiter"], 778.5e6),
}


def gx(x, mu):
    return x - (1 - mu) * (x + mu) / abs(x + mu) ** 3 - mu * (x - 1 + mu) / abs(x - 1 + mu) ** 3


def dgx(x, mu):
    return 1 + 2 * (1 - mu) / abs(x + mu) ** 3 + 2 * mu / abs(x - 1 + mu) ** 3


def biseccion(f, a, b):
    fa = f(a)
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0:
            b = m
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def newton(x, mu):
    for _ in range(100):
        d = gx(x, mu) / dgx(x, mu)
        x -= d
        if abs(d) < 1e-15:
            break
    return x


def grad(x, y, mu):
    r1 = math.hypot(x + mu, y)
    r2 = math.hypot(x - 1 + mu, y)
    return (x - (1 - mu) * (x + mu) / r1**3 - mu * (x - 1 + mu) / r2**3, y - (1 - mu) * y / r1**3 - mu * y / r2**3)


def colineales(mu):
    eps = 1e-9
    L1 = biseccion(lambda x: gx(x, mu), -mu + eps, 1 - mu - eps)
    L2 = biseccion(lambda x: gx(x, mu), 1 - mu + eps, 3.0)
    L3 = biseccion(lambda x: gx(x, mu), -3.0, -mu - eps)
    return L1, L2, L3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    res = {}
    gmax = 0.0
    dmax = 0.0
    for nom, (g1, g2, d_km) in SISTEMAS.items():
        mu = g2 / (g1 + g2)
        L1, L2, L3 = colineales(mu)
        N = [newton(x0, mu) for x0 in (L1 + 1e-3, L2 + 1e-3, L3 + 1e-3)]
        dn = max(abs(a - b) for a, b in zip((L1, L2, L3), N))
        dmax = max(dmax, dn)
        L4 = (0.5 - mu, math.sqrt(3) / 2)
        L5 = (0.5 - mu, -math.sqrt(3) / 2)
        for p in ((L1, 0), (L2, 0), (L3, 0), L4, L5):
            gmax = max(gmax, math.hypot(*grad(p[0], p[1], mu)))
        hill = (mu / 3) ** (1 / 3)
        d1 = (1 - mu - L1) * d_km
        d2 = (L2 - (1 - mu)) * d_km
        res[nom] = dict(mu=mu, L1=L1, L2=L2, L3=L3, d1=d1, d2=d2, hill=hill, rel_hill=abs((1 - mu - L1) - hill) / hill)
        print(f"{nom}: mu = {mu:.6e}")
        print(f"   L1 = {L1:.8f} ({d1:,.0f} km del cuerpo menor) ; L2 = {L2:.8f} ({d2:,.0f} km) ; L3 = {L3:.8f}")
        print(f"   L4,L5 = ({0.5 - mu:.8f}, +-{math.sqrt(3) / 2:.8f}) ; Hill (mu/3)^(1/3) = {hill:.6f} ; |dist(L1) - Hill|/Hill = {res[nom]['rel_hill']:.3f}")
    print(f"Gradiente maximo en los 15 puntos = {gmax:.2e} ; diferencia biseccion-Newton maxima = {dmax:.2e}")
    se = res["Sol-Tierra"]
    print(f"Sol-Tierra: L2 a {se['d2']:,.0f} km de la Tierra ; la pagina de NASA sobre Webb dice 'unos 1.5 millones de km'")
    assert gmax < 1e-9 and dmax < 1e-12
    assert 1.4e6 < se["d2"] < 1.6e6
    assert res["Tierra-Luna"]["L1"] < 1 and 0.8 < res["Tierra-Luna"]["L1"] < 0.9
    print("Pruebas superadas.")
    out = {"python": platform.python_version(), "gmax": gmax, "dmax": dmax}
    for k, v in res.items():
        t = {"Tierra-Luna": "tl", "Sol-Tierra": "st", "Sol-Jupiter": "sj"}[k]
        for kk, vv in v.items():
            out[f"{t}_{kk}"] = vv
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
