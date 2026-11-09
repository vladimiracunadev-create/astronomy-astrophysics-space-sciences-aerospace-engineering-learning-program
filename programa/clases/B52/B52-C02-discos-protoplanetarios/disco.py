#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C02: perfiles de un disco protoplanetario de ley de potencias y estabilidad de Toomre.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol nominal de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): Sigma(r) = S1 (r/ua)^-p con S1 = 1.0e4 kg/m^2 y p = 1.5; T(r) = 280 K (r/ua)^-0.5; mu = 2.3;
disco entre 0.1 y 100 ua. Los perfiles de ley de potencias NO se consultaron en una fuente; son una parametrizacion de ensenanza.
Sistema de referencia: plano medio del disco, simetria axial, estrella central de 1 M_sol; unidades SI.
Modelo: cs = sqrt(k T / (mu m_p)); Omega = sqrt(GM/r^3); H = cs/Omega; Q = cs Omega / (pi G Sigma).
Masa del disco: M = 2 pi * integral(Sigma r dr); analitica frente a Simpson en ln r (tolerancia 1e-6 relativo).
Pendiente de h/r = H/r en escala log-log: 0.25 (tolerancia 1e-9).
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
UA = 1.495978707e11
MU = 2.3
S1, P = 1.0e4, 1.5
T1 = 280.0
R_IN, R_OUT = 0.1, 100.0


def sigma(x):          # x en ua -> kg/m^2
    return S1 * x ** (-P)


def temp(x):
    return T1 * x ** (-0.5)


def cs(x):
    return math.sqrt(K_B * temp(x) / (MU * M_P))


def omega(x):
    return math.sqrt(GM / (x * UA) ** 3)


def h_sobre_r(x):
    return cs(x) / omega(x) / (x * UA)


def toomre(x):
    return cs(x) * omega(x) / (math.pi * G * sigma(x))


def masa_analitica():
    return 2 * math.pi * S1 * UA ** 2 * (R_OUT ** (2 - P) - R_IN ** (2 - P)) / (2 - P)


def masa_simpson(n=20000):
    # integral de Sigma r dr = integral de Sigma r^2 d(ln r)
    a, b = math.log(R_IN), math.log(R_OUT)
    h = (b - a) / n
    f = lambda u: sigma(math.exp(u)) * (math.exp(u) * UA) ** 2
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return 2 * math.pi * s * h / 3.0


def calcular():
    ma, ms = masa_analitica(), masa_simpson()
    xs = [R_IN * (R_OUT / R_IN) ** (i / 999.0) for i in range(1000)]
    qs = [toomre(x) for x in xs]
    qmin = min(qs)
    xq = xs[qs.index(qmin)]
    lx = [math.log(x) for x in (1.0, 100.0)]
    pend = (math.log(h_sobre_r(100.0)) - math.log(h_sobre_r(1.0))) / (lx[1] - lx[0])
    return dict(ma=ma, ms=ms, msol=GM / G, qmin=qmin, xq=xq, pend=pend, qs={x: toomre(x) for x in (0.1, 1.0, 5.0, 30.0, 100.0)},
                hr={x: h_sobre_r(x) for x in (0.1, 1.0, 5.0, 30.0, 100.0)}, cs1=cs(1.0), om1=omega(1.0))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Disco ilustrativo: Sigma = {S1:.1e} kg/m^2 (r/ua)^-{P}; T = {T1:.0f} K (r/ua)^-0.5; mu = {MU}; de {R_IN} a {R_OUT} ua")
    print(f"{'r [ua]':>8} {'Sigma [kg/m^2]':>15} {'T [K]':>8} {'h/r':>8} {'Q':>10}")
    for x in (0.1, 1.0, 5.0, 30.0, 100.0):
        print(f"{x:8.1f} {sigma(x):15.4e} {temp(x):8.1f} {r['hr'][x]:8.4f} {r['qs'][x]:10.2f}")
    print(f"Masa del disco: analitica = {r['ma'] / r['msol']:.5f} M_sol ; Simpson = {r['ms'] / r['msol']:.5f} M_sol ; dif. relativa = {abs(r['ms'] / r['ma'] - 1):.1e}")
    print(f"Pendiente log-log de h/r entre 1 y 100 ua = {r['pend']:.9f} (esperada 0.25)")
    print(f"Q minimo en la malla = {r['qmin']:.2f} en r = {r['xq']:.1f} ua ; el disco es estable (Q > 1): {r['qmin'] > 1.0}")
    assert abs(r["ms"] / r["ma"] - 1) < 1e-6
    assert abs(r["pend"] - 0.25) < 1e-9
    assert r["qmin"] > 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
