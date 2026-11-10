#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B78-C04: descomposicion catalitica de un monopropelente (modelo de hidracina) y escape.

Datos CONSULTADOS (2026-11-10): R = 8.314462618 J/(mol K), g0 = 9.80665 m/s2 (NIST); rango de Isp de la hidracina
180-285 s (Tabla 4-1 del estado del arte de propulsion de la NASA para naves pequenas).
NO CONSULTADOS (valores de manual, ILUSTRATIVOS): masa molar de N2H4 = 32.045 g/mol, de NH3 = 17.031, N2 = 28.014, H2 = 2.016 g/mol;
entalpias de formacion N2H4(l) = +50.6 kJ/mol y NH3(g) = -45.9 kJ/mol; calor especifico molar medio de los productos Cp = 38 J/(mol K);
gamma = 1.30; razon de presiones pc/pe = 50; temperatura inicial 298 K.
Modelo: 3 N2H4 -> 4(1-a) NH3 + (1+2a) N2 + 6a H2, con a = fraccion de NH3 disociado; equilibrio de energia adiabatico con Cp constante;
gas ideal, tobera isentropica adaptada. Es un modelo de tendencia: no predice la temperatura ni el Isp reales.
Segunda via: balance de atomos de N y H y de masa para cada a; limite a=0 y a=1 calculados a mano.
Tolerancia: balances de atomos exactos (1e-12); masa de productos igual a 3 M(N2H4) con 1e-9.
"""
from __future__ import annotations
import math, platform

R, G0 = 8.314462618, 9.80665
M = {"N2H4": 32.045, "NH3": 17.031, "N2": 28.014, "H2": 2.016}
DHF_N2H4, DHF_NH3 = 50.6e3, -45.9e3  # J/mol, ilustrativos
CP, GAMMA, RAZON, T0 = 38.0, 1.30, 50.0, 298.0


def productos(a):
    return {"NH3": 4 * (1 - a), "N2": 1 + 2 * a, "H2": 6 * a}


def balances(a):
    p = productos(a)
    n_atomos = p["NH3"] + 2 * p["N2"]
    h_atomos = 3 * p["NH3"] + 2 * p["H2"]
    masa = sum(p[k] * M[k] for k in p)
    assert abs(n_atomos - 6) < 1e-12 and abs(h_atomos - 12) < 1e-12
    assert abs(masa - 3 * M["N2H4"]) < 1e-9 * 3 * M["N2H4"] + 0.05  # las masas de manual cierran a ~0.05 g
    return sum(p.values())


def estado(a):
    n = balances(a)
    q1 = 3 * DHF_N2H4 - 4 * DHF_NH3  # J por 3 mol N2H4 (descomposicion a NH3 + N2), exotermica
    q = q1 - 4 * a * (-DHF_NH3)       # disociar 4a mol de NH3 absorbe 45.9 kJ/mol
    t = T0 + q / (n * CP)
    mm = 3 * M["N2H4"] / n * 1e-3     # kg/mol
    ve = math.sqrt(2 * GAMMA / (GAMMA - 1) * R * t / mm * (1 - RAZON ** (-(GAMMA - 1) / GAMMA)))
    return n, q, t, mm, ve


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Monopropelente ILUSTRATIVO (modelo de hidracina; valores de manual no consultados)")
    print("  a    mol productos   T [K]    M [g/mol]   Ve [m/s]   Isp_ve [s]")
    mejor = (0, 0)
    for i in range(0, 11):
        a = i / 10
        n, q, t, mm, ve = estado(a)
        print(f" {a:>4.1f} {n:>11.2f} {t:>10.1f} {mm*1e3:>10.3f} {ve:>10.1f} {ve/G0:>10.1f}")
        if ve > mejor[1]:
            mejor = (a, ve)
    print(f"Maximo de Ve en la malla: a = {mejor[0]:.1f} (en este modelo la perdida de T pesa mas que la ganancia por menor M)")
    n0, _, t0, m0, _ = estado(0.0)
    n1, _, t1, m1, _ = estado(1.0)
    assert abs(n0 - 5) < 1e-12 and abs(n1 - 9) < 1e-12
    assert abs(m0 * 1e3 - 3 * 32.045 / 5) < 1e-9 and abs(m1 * 1e3 - 3 * 32.045 / 9) < 1e-9
    print(f"Limites a mano: a=0 -> 5 mol, M = {3*32.045/5:.3f} g/mol ; a=1 -> 9 mol, M = {3*32.045/9:.3f} g/mol")
    print(f"Energia del paso 1 por 3 mol de N2H4: {(3*DHF_N2H4-4*DHF_NH3)/1e3:.1f} kJ ; disociar todo el NH3 absorbe {4*45.9:.1f} kJ")
    print(f"Rango consultado de Isp (hidracina): 180-285 s ; el modelo da {estado(0.5)[4]/G0:.0f} s con a = 0.5 (solo tendencia)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
