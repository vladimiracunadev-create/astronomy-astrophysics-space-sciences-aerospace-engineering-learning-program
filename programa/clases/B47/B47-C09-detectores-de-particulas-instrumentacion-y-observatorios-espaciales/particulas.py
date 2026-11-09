#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C09: detector de particulas de silicio, perdida de energia de Bethe-Bloch, alcance y telescopio DeltaE-E.

Datos: N_A, radio clasico del electron, m_e c^2 = 0,51099895069 MeV, energia en reposo del proton (938,27208943 MeV) y de la particula alfa (3727,3794118 MeV) de NIST CODATA 2022
(allascii.txt, consultada el 2026-11-09). ILUSTRATIVOS (valores de uso general para silicio, no consultados en esta clase): Z/A = 14/28,0855, densidad 2,329 g/cm3, I = 173 eV.
Espesores del telescopio: DeltaE de 300 micrometros, tipicos de un ejemplo, no de un instrumento.
Modelo: (1) S(E) = K z^2 (Z/A) / beta^2 [ 0,5 ln(2 m_e c^2 beta^2 gamma^2 T_max / I^2) - beta^2 ] sin correccion de densidad ni de capas, con K = 4 pi N_A r_e^2 m_e c^2;
(2) alcance CSDA R(E) = integral de dE/S desde una velocidad minima fija (Simpson); (3) identidad de escala R_alfa(E) = (M_alfa/M_p)/z^2 R_p(E M_p/M_alfa) contrastada
con las dos integrales independientes; (4) DeltaE en una placa fina por integracion paso a paso frente a S * rho * t.
Supuestos: particula pesada, perdida continua, sin fluctuaciones ni radiacion de frenado, sin correcciones de baja energia. Validez: unos 1 a 1000 MeV por nucleon; ilustrativa.
Tolerancia: identidad de escala, 1e-3 relativo (la correccion m_e/M de T_max la rompe levemente); DeltaE de dos vias, 2 % (la placa no es infinitamente fina).
"""
from __future__ import annotations
import math, platform

NA = 6.02214076e23
RE_CM = 2.8179403205e-13
MEC2 = 0.51099895069
MP, MA = 938.27208943, 3727.3794118
K = 4 * math.pi * NA * RE_CM ** 2 * MEC2          # MeV cm2 / mol
ZA, RHO, I_MEV = 14 / 28.0855, 2.329, 173e-6


def stopping(e, m, z):
    g = 1 + e / m
    b2 = 1 - 1 / g ** 2
    tmax = 2 * MEC2 * b2 * g ** 2 / (1 + 2 * g * MEC2 / m + (MEC2 / m) ** 2)
    return K * z * z * ZA / b2 * (0.5 * math.log(2 * MEC2 * b2 * g ** 2 * tmax / I_MEV ** 2) - b2)


def alcance(e, m, z, e_min, n=4000):
    h = (e - e_min) / n
    s = 0.0
    for i in range(n + 1):
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w / stopping(e_min + i * h, m, z)
    return s * h / 3


def delta_e(e0, m, z, t_cm, pasos=20000):
    dx = t_cm / pasos
    e = e0
    for _ in range(pasos):
        k1 = stopping(e, m, z)
        k2 = stopping(e - 0.5 * dx * RHO * k1, m, z)
        e -= dx * RHO * k2
    return e0 - e


def calc():
    r = {"K": K}
    r["S"] = {e: stopping(e, MP, 1) for e in (1, 10, 100, 1000)}
    emin_p = 1.0
    emin_a = emin_p * MA / MP
    r["R"] = {}
    for e in (10, 30, 100):
        rp = alcance(e, MP, 1, emin_p)
        ra = alcance(e * MA / MP, MA, 2, emin_a)
        pred = (MA / MP) / 4 * rp
        r["R"][e] = (rp / RHO * 10, ra / RHO * 10, pred / RHO * 10)   # mm
    t = 300e-4
    ep, ea = 30.0, 30.0 * MA / MP
    dp = delta_e(ep, MP, 1, t)
    da = delta_e(ea, MA, 2, t)
    r["dE"] = (dp, da, da / dp)
    r["fino"] = (stopping(ep, MP, 1) * RHO * t, stopping(ea, MA, 2) * RHO * t)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"K = 4 pi N_A r_e^2 m_e c^2 = {r['K']:.6f} MeV cm2/mol")
    for e, s in r["S"].items():
        print(f"protón {e:5d} MeV: S = {s:.3f} MeV cm2/g ; dE/dx = {s*RHO:.2f} MeV/cm")
    print(f"{'E_p [MeV]':>10} {'R_p [mm]':>10} {'R_alfa [mm]':>12} {'prediccion [mm]':>16}")
    for e, (a, b, c) in r["R"].items():
        print(f"{e:10d} {a:10.4f} {b:12.4f} {c:16.4f}")
        assert abs(b - c) / b < 1e-3
    dp, da, q = r["dE"]
    print(f"DeltaE en 300 um: proton 30 MeV = {dp:.4f} MeV ; alfa 119.2 MeV (misma velocidad) = {da:.4f} MeV ; cociente = {q:.4f}")
    print(f"placa fina S rho t: proton = {r['fino'][0]:.4f} MeV ; alfa = {r['fino'][1]:.4f} MeV")
    assert abs(dp - r["fino"][0]) / dp < 2e-2
    assert abs(q - 4) < 0.05
    assert abs(r["K"] - 0.307075) < 1e-5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
