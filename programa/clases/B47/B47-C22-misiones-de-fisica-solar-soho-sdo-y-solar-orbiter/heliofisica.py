#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C22: misiones de fisica solar, punto de Lagrange L1, orbita geosincrona, orbita heliocentrica de perihelio cercano y flujo solar.

Datos: GM_sol = 1,3271244e20 m3/s2, S_sol = 1361 W/m2 (UAI B3 de 2015, arXiv:1510.07674, consultada el 2026-11-09); GM_Tierra = 3,986004e14 m3/s2 y R_ecuatorial terrestre 6,3781e6 m (UAI B3);
au = 1,495978707e11 m (IERS, consultada el 2026-11-09); c y sigma de Stefan-Boltzmann de NIST CODATA 2022 (consultada el 2026-11-09).
CONSULTADO SOLO EN RESUMEN (2026-11-09): Solar Orbiter (Muller et al., arXiv:2009.00861): lanzado el 10 de febrero de 2020 con seis instrumentos de teledeteccion y cuatro in situ; el resumen no da
distancias orbitales. ILUSTRATIVOS (no son el diseno de ninguna mision): perihelio 0,28 au, afelio 0,91 au, dia sideral de 86164,09 s (valor de uso general, no consultado aqui), placa negra plana.
Modelo: (1) L1 como raiz del balance de fuerzas en el sistema Sol-Tierra con velocidad angular omega^2 = G(M+m)/R^3, contrastada con la aproximacion de Hill r = R (m/(3M))^(1/3);
(2) radio geosincrono a = (GM T^2/(4 pi^2))^(1/3); (3) periodo kepleriano de la orbita heliocentrica frente a una integracion RK4, y velocidad en perihelio por vis-viva;
(4) flujo S(r) = S_sol/r^2 y temperatura de equilibrio de una placa negra T = (S/sigma)^(1/4) (ilustrativa: ignora albedo, emisividad y geometria); tiempo luz = r/c.
Supuestos: orbitas keplerianas de dos cuerpos, Tierra en orbita circular, masa de la Tierra frente a la del Sol segun GM. Validez: ilustrativa.
Tolerancia: L1 exacto frente a Hill, 1 %; periodo numerico frente a kepleriano, 1e-6.
"""
from __future__ import annotations
import math, platform

GMS = 1.3271244e20
GME = 3.986004e14
RE = 6.3781e6
AU = 1.495978707e11
C = 299792458.0
S0 = 1361.0
SIGMA = 5.670374419e-8


def l1():
    m_ratio = GME / GMS
    w2 = GMS * (1 + m_ratio) / AU ** 3
    xcm = AU * m_ratio / (1 + m_ratio)

    def f(r):
        x = AU - r
        return GMS / x ** 2 - GME / r ** 2 - w2 * (x - xcm)

    lo, hi = 1e8, 5e9
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(m) > 0:
            hi = m
        else:
            lo = m
    return 0.5 * (lo + hi)


def periodo_num(a, e, pasos=40000):
    rp = a * (1 - e)
    vp = math.sqrt(GMS * (1 + e) / rp)
    t_k = 2 * math.pi * math.sqrt(a ** 3 / GMS)
    dt = t_k / pasos
    s = [rp, 0.0, 0.0, vp]

    def f(s):
        r3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return [s[2], s[3], -GMS * s[0] / r3, -GMS * s[1] / r3]

    t = 0.0
    while True:
        k1 = f(s)
        k2 = f([s[i] + 0.5 * dt * k1[i] for i in range(4)])
        k3 = f([s[i] + 0.5 * dt * k2[i] for i in range(4)])
        k4 = f([s[i] + dt * k3[i] for i in range(4)])
        n = [s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)]
        if t > 0.5 * t_k and s[1] < 0 <= n[1]:
            return t + (-s[1] / (n[1] - s[1])) * dt
        s = n
        t += dt


def calc():
    r = {}
    r["l1"] = l1()
    r["hill"] = AU * (GME / (3 * GMS)) ** (1 / 3)
    t_sid = 86164.09
    a_geo = (GME * t_sid ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    r["geo"], r["geo_alt"] = a_geo, a_geo - RE
    rp, ra = 0.28 * AU, 0.91 * AU
    a = 0.5 * (rp + ra)
    e = (ra - rp) / (ra + rp)
    r["a_au"], r["e"] = a / AU, e
    r["per_kep"] = 2 * math.pi * math.sqrt(a ** 3 / GMS)
    r["per_num"] = periodo_num(a, e)
    r["vp"] = math.sqrt(GMS * (2 / rp - 1 / a))
    r["va"] = math.sqrt(GMS * (2 / ra - 1 / a))
    r["flujo"] = {d: S0 / d ** 2 for d in (1.0, 0.91, 0.28)}
    r["temp"] = {d: (S0 / d ** 2 / SIGMA) ** 0.25 for d in (1.0, 0.91, 0.28)}
    r["luz"] = {d: d * AU / C for d in (1.0, 0.72)}
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"L1: distancia a la Tierra = {r['l1']/1e9:.5f} millones de km ; aproximacion de Hill = {r['hill']/1e9:.5f} ; diferencia = {100*(r['hill']-r['l1'])/r['l1']:.3f} %")
    print(f"orbita geosincrona: a = {r['geo']/1e3:.2f} km ; altitud = {r['geo_alt']/1e3:.2f} km")
    print(f"orbita heliocentrica ilustrativa: a = {r['a_au']:.4f} au ; e = {r['e']:.4f} ; periodo kepleriano = {r['per_kep']/86400:.4f} d ; RK4 = {r['per_num']/86400:.4f} d")
    print(f"vis-viva: v perihelio = {r['vp']/1e3:.3f} km/s ; v afelio = {r['va']/1e3:.3f} km/s ; cociente = {r['vp']/r['va']:.4f} (afelio/perihelio = {0.91/0.28:.4f})")
    for d in r["flujo"]:
        print(f"d = {d:.2f} au: S = {r['flujo'][d]:.1f} W/m2 ; T de placa negra = {r['temp'][d]:.1f} K")
    print(f"tiempo luz: 1 au = {r['luz'][1.0]:.2f} s ; 0.72 au = {r['luz'][0.72]:.2f} s")
    assert abs(r["hill"] - r["l1"]) / r["l1"] < 0.01
    assert abs(r["per_num"] - r["per_kep"]) / r["per_kep"] < 1e-6
    assert abs(r["vp"] / r["va"] - 0.91 / 0.28) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
