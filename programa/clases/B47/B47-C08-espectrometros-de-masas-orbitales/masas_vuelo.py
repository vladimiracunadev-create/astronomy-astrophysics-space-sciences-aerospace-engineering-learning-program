#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C08: espectrometro de masas de tiempo de vuelo, resolucion de masa y separacion de iones D+ y H2+.

Datos: u = 1,66053906892e-27 kg, e = 1,602176634e-19 C, masa del proton 1,0072764665789 u, masa del deuteron 2,013553212544 u, masa de la particula alfa 4,001506179129 u
y masa del electron en u de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). La energia de enlace del H2+ (2,65 eV) se desprecia (cambia la masa en 3e-9 u).
ILUSTRATIVOS (no son los parametros de ningun instrumento): longitud de vuelo L = 1,50 m, tension de aceleracion U = 1000 V, dispersion de energia inicial sigma = 0,2 eV y anchura
del pulso de arranque sigma = 0,5 ns.
Modelo: (1) t = L sqrt(m/(2 q U)); (2) resolucion R = m/dm = t/(2 dt); (3) Monte Carlo (semilla 20261109) con energia inicial gaussiana y pulso de arranque gaussiano, contrastado con
la propagacion sigma_t^2 = (t sigma_e/(2U))^2 + sigma_p^2; (4) resolucion exigida para separar D+ y H2+.
Supuestos: campo uniforme de aceleracion, zona libre de campo, sin reflectron, sin carga espacial. Validez: ilustrativa.
Tolerancia: tiempos de vuelo por dos vias (formula y energia cinetica), 1e-12; dispersion Monte Carlo frente a propagacion, 3 %.
"""
from __future__ import annotations
import math, platform, random

U_KG = 1.66053906892e-27
E = 1.602176634e-19
MP, MD, MA, ME_U = 1.0072764665789, 2.013553212544, 4.001506179129, 5.485799090441e-4
L, UACC = 1.50, 1000.0
SIG_E, SIG_P = 0.2, 0.5e-9


def tof(masa_u, q=1):
    return L * math.sqrt(masa_u * U_KG / (2 * q * E * UACC))


def tof_energia(masa_u, q=1):
    v = math.sqrt(2 * q * E * UACC / (masa_u * U_KG))   # v desde la energia cinetica
    return L / v


def simula(masa_u, n, rng, q=1):
    ts = []
    for _ in range(n):
        eps = rng.gauss(0, SIG_E)
        u = UACC + eps
        t = L * math.sqrt(masa_u * U_KG / (2 * q * E * u)) + rng.gauss(0, SIG_P)
        ts.append(t)
    m = sum(ts) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in ts) / (n - 1))
    return m, sd


def calc():
    r = {}
    iones = {"H2+": 2 * MP + ME_U, "D+": MD, "He2+ (m/q)": MA / 2}
    r["m"] = iones
    r["t"] = {k: tof(v) for k, v in iones.items()}
    r["t2"] = {k: tof_energia(v) for k, v in iones.items()}
    r["R_exigida"] = iones["D+"] / (iones["H2+"] - iones["D+"])
    rng = random.Random(20261109)
    r["mc"] = {}
    for k in ("H2+", "D+"):
        m, sd = simula(iones[k], 40000, rng)
        t0 = r["t"][k]
        prop = math.sqrt((t0 * SIG_E / (2 * UACC)) ** 2 + SIG_P ** 2)
        r["mc"][k] = (m, sd, prop)
    t_d, sd_d = r["mc"]["D+"][0], r["mc"]["D+"][1]
    r["R_logr"] = t_d / (2 * 2.3548 * sd_d)
    r["sep"] = (r["mc"]["H2+"][0] - r["mc"]["D+"][0]) / math.hypot(r["mc"]["D+"][1], r["mc"]["H2+"][1])
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'ion':>12} {'m/q [u]':>12} {'t formula [us]':>16} {'t energia [us]':>16}")
    for k in r["m"]:
        print(f"{k:>12} {r['m'][k]:12.6f} {r['t'][k]*1e6:16.6f} {r['t2'][k]*1e6:16.6f}")
        assert abs(r["t"][k] - r["t2"][k]) / r["t"][k] < 1e-12
    print(f"resolucion exigida para separar D+ y H2+: m/dm = {r['R_exigida']:.1f}")
    for k, (m, sd, prop) in r["mc"].items():
        print(f"{k:>5}: media = {m*1e6:.5f} us ; desviacion MC = {sd*1e9:.3f} ns ; propagacion = {prop*1e9:.3f} ns")
        assert abs(sd - prop) / prop < 0.03
    print(f"resolucion lograda m/dm (FWHM) = {r['R_logr']:.1f} ; separacion de picos = {r['sep']:.2f} sigma")
    assert r["R_logr"] > r["R_exigida"] * 0.9
    assert 1200 < r["R_exigida"] < 1400
    assert r["t"]["H2+"] > r["t"]["D+"] > r["t"]["He2+ (m/q)"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
