#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C04: turbulencia (Fried, centelleo), desvanecimiento y nubes con diversidad de estaciones.

Datos consultados (2026-11-10), solo como contexto: el experimento LCRD reporta un parametro de Fried de hasta 2 cm
(a 500 nm, en el cenit, al mediodia) y una longitud de coherencia media de 4 cm en un enlace nocturno; una
disponibilidad por clima de 80 %; y el telescopio del OGS-1 de 1 m (Israel et al., SPIE 2024, NTRS 20230018608).
Tambien: c = 299792458 m/s (NIST, CODATA 2022) y la banda C de la rejilla del CCSDS 141.0-B-1.
ILUSTRATIVOS (sinteticos, no medidos): perfil Hufnagel-Valley 5/7 (A = 1.7e-14 m^-2/3, viento 21 m/s), apertura 1 m,
profundidad optica cenital 0.05, probabilidad de nube 0.2 por estacion, correlacion 0.1.
Modelo: r0 = (0.423 k^2 sec(z) INT Cn2 dh)^(-3/5); sigma_R^2 = 2.25 k^(7/6) sec(z)^(11/6) INT Cn2 h^(5/6) dh (onda plana, enlace
descendente, turbulencia debil); desvanecimiento log-normal de media 1: ln I ~ N(-s^2/2, s^2), s^2 = ln(1 + sigma_I^2).
Segunda via: integrales analiticas (gamma) de cada termino exponencial, y Monte Carlo (random.Random(92)).
Tolerancia: integrales numericas frente a analiticas 1e-6 relativa; Monte Carlo 3e-3 absoluta.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

A_HV, VIENTO = 1.7e-14, 21.0
H0 = 1.0e-5


def cn2(h):
    return (0.00594 * (VIENTO / 27.0) ** 2 * (H0 * h) ** 10 * math.exp(-h / 1000.0)
            + 2.7e-16 * math.exp(-h / 1500.0) + A_HV * math.exp(-h / 100.0))


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def i_cn2_analitica():
    t1 = 0.00594 * (VIENTO / 27.0) ** 2 * H0 ** 10 * math.factorial(10) * 1000.0 ** 11
    return t1 + 2.7e-16 * 1500.0 + A_HV * 100.0


def i_rytov_analitica():
    g = math.gamma(11.0 / 6.0)
    t1 = 0.00594 * (VIENTO / 27.0) ** 2 * H0 ** 10 * 1000.0 ** (10.0 + 11.0 / 6.0) * math.gamma(10.0 + 11.0 / 6.0)
    return t1 + 2.7e-16 * 1500.0 ** (11.0 / 6.0) * g + A_HV * 100.0 ** (11.0 / 6.0) * g


def fried(lam, ic, zen_deg=0.0):
    k = 2.0 * math.pi / lam
    sec = 1.0 / math.cos(math.radians(zen_deg))
    return (0.423 * k * k * sec * ic) ** (-0.6)


def rytov(lam, ir, zen_deg=0.0):
    k = 2.0 * math.pi / lam
    sec = 1.0 / math.cos(math.radians(zen_deg))
    return 2.25 * k ** (7.0 / 6.0) * sec ** (11.0 / 6.0) * ir


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    top = 60000.0
    ic_num = simpson(cn2, 0.0, top, 120000)
    ir_num = simpson(lambda h: cn2(h) * h ** (5.0 / 6.0), 0.0, top, 120000)
    ic_an, ir_an = i_cn2_analitica(), i_rytov_analitica()
    d1, d2 = abs(ic_num - ic_an) / ic_an, abs(ir_num - ir_an) / ir_an
    print(f"Integral de Cn2 dh: numerica {ic_num:.5e} ; analitica {ic_an:.5e} m^(1/3) ; dif. {d1:.1e}")
    print(f"Integral de Cn2 h^(5/6) dh: numerica {ir_num:.5e} ; analitica {ir_an:.5e} ; dif. {d2:.1e}")
    r500 = fried(500e-9, ic_an)
    print(f"Parametro de Fried a 500 nm, cenit (HV 5/7 ILUSTRATIVO): r0 = {r500 * 100:.2f} cm")
    print(" lambda [nm]  zenit [deg]  r0 [cm]  D/r0 (D = 1 m)  sigma_R^2 (plana)")
    for lam, z in ((500e-9, 0.0), (1550e-9, 0.0), (1550e-9, 30.0), (1550e-9, 60.0)):
        r0 = fried(lam, ic_an, z)
        sr = rytov(lam, ir_an, z)
        print(f"  {lam * 1e9:8.0f} {z:10.0f} {r0 * 100:10.2f} {1.0 / r0:13.2f} {sr:15.4f}")
    esc = fried(1550e-9, ic_an) / r500
    print(f"Escalado r0 ~ lambda^(6/5): cociente 1550/500 nm = {esc:.4f} ; (1550/500)^1.2 = {(1550 / 500) ** 1.2:.4f}")
    # desvanecimiento
    print("Desvanecimiento log-normal (media 1): margen para probabilidad de desvanecimiento p")
    nd = NormalDist()
    rng = random.Random(92)
    dmc = 0.0
    for si in (0.1, 0.5):
        s2 = math.log(1.0 + si)
        s = math.sqrt(s2)
        for p in (1e-2, 1e-3):
            q = nd.inv_cdf(p)
            thr = math.exp(-0.5 * s2 + s * q)
            mdb = -10.0 * math.log10(thr)
            print(f"  sigma_I^2 = {si:3.1f}  p = {p:.0e}  umbral = {thr:.4f}  margen = {mdb:5.2f} dB")
            if p == 1e-2:
                n = 200000
                c = sum(1 for _ in range(n) if math.exp(rng.gauss(-0.5 * s2, s)) < thr) / n
                dmc = max(dmc, abs(c - p))
    print(f"  Monte Carlo (p = 1e-2, 200000 muestras): diferencia absoluta maxima {dmc:.1e}")
    tau = 0.05
    print(f"Extincion clara (tau cenital {tau}, ILUSTRATIVO): T(0) = {math.exp(-tau):.4f} ; T(60 deg) = {math.exp(-tau / math.cos(math.radians(60.0))):.4f}")
    # nubes
    p = 0.2
    print("Disponibilidad por nubes con N estaciones (p nube = 0.2, ILUSTRATIVO; LCRD reporto 80 % de disponibilidad por clima):")
    c_corr = 0.1
    rng2 = random.Random(92)
    dmc2 = 0.0
    for nst in (1, 2, 3, 4):
        ind = 1.0 - p ** nst
        corr = 1.0 - (c_corr * p + (1.0 - c_corr) * p ** nst)
        n = 200000
        todas = 0
        for _ in range(n):
            if rng2.random() < c_corr:
                todas += rng2.random() < p
            else:
                todas += all(rng2.random() < p for _ in range(nst))
        mc = 1.0 - todas / n
        dmc2 = max(dmc2, abs(mc - corr))
        print(f"  N = {nst}  independientes {ind:.4f}  con correlacion {c_corr}: {corr:.4f}  (Monte Carlo {mc:.4f})")
    print(f"Diferencia maxima Monte Carlo frente a analitico (nubes) = {dmc2:.1e}")
    assert d1 < 1e-6 and d2 < 1e-6
    assert abs(esc - (1550 / 500) ** 1.2) < 1e-9
    assert dmc < 3e-3 and dmc2 < 3e-3
    assert 0.04 < r500 < 0.06
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
