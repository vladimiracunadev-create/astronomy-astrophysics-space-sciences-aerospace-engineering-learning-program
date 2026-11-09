#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C23: sondas heliosfericas, velocidad en perihelio, flujo y equilibrio termico cerca del Sol, y enlace y energia a gran distancia.

Datos: GM_sol, R_sol = 6,957e8 m y S_sol = 1361 W/m2 (UAI B3 de 2015, arXiv:1510.07674, consultada el 2026-11-09); au = 1,495978707e11 m (IERS, consultada el 2026-11-09); c, h y
sigma de Stefan-Boltzmann de NIST CODATA 2022 (consultada el 2026-11-09). CONSULTADO SOLO EN RESUMEN (2026-11-09): Parker Solar Probe (Raouafi et al., arXiv:2301.02727): lanzamiento el
12 de agosto de 2018 y 24 orbitas previstas; el resumen no da la distancia del perihelio. ILUSTRATIVOS (valores de uso general, no consultados aqui; no son datos de mision): perihelio 9,86 R_sol,
periodo 88 d, absortividad/emisividad 0,4 de una placa que irradia por su cara iluminada, distancia de 160 au para una sonda lejana, 8,4 GHz, vida media del Pu-238 de 87,7 anios y
degradacion termoelectrica del 0,8 % anual.
Modelo: (1) semieje desde el periodo, afelio = 2a - r_p, velocidad por vis-viva y comprobacion con un periodo RK4; (2) flujo S = S_sol (au/r)^2 y temperatura de placa T = (alpha S/(eps sigma))^(1/4);
(3) tiempo luz y perdida de espacio libre a 160 au frente a una distancia de 1932 km; (4) potencia de un RTG P0 2^(-t/87,7) (1 - 0,008)^t.
Supuestos: dos cuerpos, sin corona ni polvo, placa plana perpendicular a la luz. Validez: ilustrativa; no es el diseno termico de ninguna sonda.
Tolerancia: periodo numerico frente al dado, 1e-6; conservacion de energia especifica, 1e-8 relativo.
"""
from __future__ import annotations
import math, platform

GMS = 1.3271244e20
RS = 6.957e8
AU = 1.495978707e11
C = 299792458.0
S0 = 1361.0
SIGMA = 5.670374419e-8
RP = 9.86 * RS
PER = 88.0 * 86400


def integra(a, rp, pasos=40000):
    vp = math.sqrt(GMS * (2 / rp - 1 / a))
    dt = PER / pasos
    s = [rp, 0.0, 0.0, vp]
    e0 = 0.5 * vp ** 2 - GMS / rp

    def f(s):
        r3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return [s[2], s[3], -GMS * s[0] / r3, -GMS * s[1] / r3]

    t = 0.0
    emax = 0.0
    while True:
        k1 = f(s)
        k2 = f([s[i] + 0.5 * dt * k1[i] for i in range(4)])
        k3 = f([s[i] + 0.5 * dt * k2[i] for i in range(4)])
        k4 = f([s[i] + dt * k3[i] for i in range(4)])
        n = [s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)]
        e = 0.5 * (n[2] ** 2 + n[3] ** 2) - GMS / math.hypot(n[0], n[1])
        emax = max(emax, abs((e - e0) / e0))
        if t > 0.5 * PER and s[1] < 0 <= n[1]:
            return t + (-s[1] / (n[1] - s[1])) * dt, emax
        s = n
        t += dt


def calc():
    r = {}
    a = (GMS * PER ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    ra = 2 * a - RP
    r["a_au"], r["ra_au"], r["rp_au"] = a / AU, ra / AU, RP / AU
    r["e"] = (ra - RP) / (ra + RP)
    r["vp"] = math.sqrt(GMS * (2 / RP - 1 / a))
    r["va"] = math.sqrt(GMS * (2 / ra - 1 / a))
    r["per_num"], r["emax"] = integra(a, RP)
    r["flujo_rel"] = (AU / RP) ** 2
    r["S_p"] = S0 * r["flujo_rel"]
    r["T_negro"] = (r["S_p"] / SIGMA) ** 0.25
    r["T_gris"] = (0.4 * r["S_p"] / SIGMA) ** 0.25
    d = 160 * AU
    r["luz_h"] = d / C / 3600
    lam = C / 8.4e9
    r["fs_far"] = 20 * math.log10(4 * math.pi * d / lam)
    r["fs_leo"] = 20 * math.log10(4 * math.pi * 1932e3 / lam)
    r["dif_db"] = r["fs_far"] - r["fs_leo"]
    r["rtg"] = {t: 2 ** (-t / 87.7) * (1 - 0.008) ** t for t in (0, 10, 25, 47)}
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"perihelio = {r['rp_au']:.5f} au = 9.86 R_sol ; semieje = {r['a_au']:.5f} au ; afelio = {r['ra_au']:.5f} au ; e = {r['e']:.5f}")
    print(f"vis-viva: v perihelio = {r['vp']/1e3:.3f} km/s ; v afelio = {r['va']/1e3:.3f} km/s")
    print(f"periodo dado = {PER/86400:.1f} d ; periodo RK4 = {r['per_num']/86400:.6f} d ; error maximo de energia = {r['emax']:.2e}")
    print(f"flujo en perihelio = {r['S_p']:.1f} W/m2 = {r['flujo_rel']:.1f} x S_sol")
    print(f"temperatura de placa negra = {r['T_negro']:.1f} K ; placa con alpha/eps = 0.4 = {r['T_gris']:.1f} K")
    print(f"160 au: tiempo luz = {r['luz_h']:.3f} h ; perdida de espacio libre a 8.4 GHz = {r['fs_far']:.2f} dB ; a 1932 km = {r['fs_leo']:.2f} dB ; diferencia = {r['dif_db']:.2f} dB")
    for t, p in r["rtg"].items():
        print(f"RTG a los {t:2d} anios: {p*100:.2f} % de la potencia inicial")
    assert abs(r["per_num"] - PER) / PER < 1e-6
    assert r["emax"] < 1e-8
    assert abs(r["dif_db"] - 20 * math.log10(160 * AU / 1932e3)) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
