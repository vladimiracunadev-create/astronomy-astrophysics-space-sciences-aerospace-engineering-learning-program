#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C14: excitacion de Boltzmann, ionizacion de Saha del hidrogeno y cociente de abundancias con lineas debiles.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): h, k_B, c, m_e exactos o medidos; energia de Rydberg 13,605693122990 eV; m_e/m_p = 5,446170214889e-4. La presion electronica de
2 Pa, el truncamiento de la funcion de particion en n = 10 y las fuerzas de oscilador relativas son ILUSTRATIVOS (no se consultaron tablas atomicas). Semilla 20261109.
Modelo: Boltzmann n_2/n_1 = (g_2/g_1) exp(-DeltaE/kT) con g_n = 2 n^2; Saha N_p n_e / N_H = (2 pi m_e k T/h^2)^(3/2) (2 g_p/U_H) exp(-chi/kT) con g_p = 1;
fraccion de hidrogeno en n = 2 = neutro x excitado; cociente de abundancias de lineas debiles log N ~ log(W/(f lambda^2)).
Supuestos: equilibrio termodinamico local, solo hidrogeno, sin correccion por reduccion del potencial de ionizacion. Validez: orden de magnitud del maximo de Balmer en un gas de H puro.
Tolerancia: dos vias de la fraccion n = 2 (suma directa y formula cerrada) iguales a 1e-12; Monte Carlo del cociente de abundancias frente a la propagacion analitica a 10 %.
"""
from __future__ import annotations
import math, platform, random, sys

H = 6.62607015e-34
KB = 1.380649e-23
ME = 9.1093837139e-31
EV = 1.602176634e-19
RY_EV = 13.605693122990
MU = 1 / (1 + 5.446170214889e-4)
CHI = RY_EV * MU                       # energia de ionizacion del hidrogeno (masa reducida), eV
PE = 2.0                               # Pa, ilustrativo
NMAX = 10
SEMILLA = 20261109


def energia(n):
    return CHI * (1 - 1 / n ** 2)


def particion(T):
    return sum(2 * n * n * math.exp(-energia(n) * EV / (KB * T)) for n in range(1, NMAX + 1))


def saha_const(T):
    return (2 * math.pi * ME * KB * T / H ** 2) ** 1.5


def razon_ion(T, ne):
    """N_p / N_H."""
    return saha_const(T) * 2 * 1.0 / particion(T) * math.exp(-CHI * EV / (KB * T)) / ne


def fraccion_n2(T):
    ne = PE / (KB * T)
    q = razon_ion(T, ne)
    neutro = 1 / (1 + q)
    exc = 8 * math.exp(-energia(2) * EV / (KB * T)) / particion(T)
    return neutro * exc, neutro


def calcular():
    r = {}
    r["chi"] = CHI
    r["e21"] = energia(2)
    fila = []
    for T in (5000, 7000, 9000, 10000, 12000, 15000, 20000):
        f2, neutro = fraccion_n2(float(T))
        fila.append((T, neutro, f2, razon_ion(float(T), PE / (KB * T))))
    r["filas"] = fila
    mejor = max(range(4000, 30001, 50), key=lambda t: fraccion_n2(float(t))[0])
    r["T_pico"] = mejor
    r["f2_pico"] = fraccion_n2(float(mejor))[0]
    # ionizacion al 50 %
    lo, hi = 4000.0, 30000.0
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if razon_ion(m, PE / (KB * m)) < 1.0:
            lo = m
        else:
            hi = m
    r["T_mitad"] = 0.5 * (lo + hi)
    # dos vias: suma directa en niveles
    T = 10000.0
    suma = sum(2 * n * n * math.exp(-energia(n) * EV / (KB * T)) for n in range(1, NMAX + 1))
    r["pob2_suma"] = 8 * math.exp(-energia(2) * EV / (KB * T)) / suma
    r["pob2_formula"] = 8 * math.exp(-energia(2) * EV / (KB * T)) / particion(T)
    r["boltz_21"] = 4 * math.exp(-(energia(2)) * EV / (KB * T))
    # cociente de abundancias con 4 lineas debiles por elemento
    rnd = random.Random(SEMILLA)
    f = [0.9, 0.5, 0.2, 0.05]
    lam = [450e-9, 500e-9, 550e-9, 600e-9]
    dex_true = 0.30
    N1, N2 = 1.0, 10 ** dex_true

    def estim():
        l1 = []
        l2 = []
        for fi, li in zip(f, lam):
            w1 = N1 * fi * li ** 2 * (1 + rnd.gauss(0, 0.05))
            w2 = N2 * fi * li ** 2 * (1 + rnd.gauss(0, 0.05))
            l1.append(math.log10(w1 / (fi * li ** 2)))
            l2.append(math.log10(w2 / (fi * li ** 2)))
        return sum(l2) / 4 - sum(l1) / 4
    est = [estim() for _ in range(3000)]
    m = sum(est) / len(est)
    sd = math.sqrt(sum((a - m) ** 2 for a in est) / (len(est) - 1))
    r["dex_media"], r["dex_sd"] = m, sd
    r["dex_pred"] = 0.4342944819 * 0.05 * math.sqrt(2 / 4)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"chi (H, masa reducida) = {r['chi']:.5f} eV ; E(n=2) - E(n=1) = {r['e21']:.5f} eV ; P_e = {PE} Pa")
    print(f"{'T (K)':>7} {'N_H/N_tot':>10} {'N(n=2)/N_tot':>13} {'N_p/N_H':>12}")
    for T, a, b, c in r["filas"]:
        print(f"{T:7d} {a:10.5f} {b:13.4e} {c:12.4e}")
    print(f"maximo de la poblacion n = 2: T = {r['T_pico']} K, fraccion {r['f2_pico']:.4e} ; ionizacion del 50 % en T = {r['T_mitad']:.0f} K")
    print(f"T = 10000 K: poblacion de n = 2 relativa al neutro, suma directa {r['pob2_suma']:.6e} ; formula {r['pob2_formula']:.6e} ; n2/n1 de Boltzmann = {r['boltz_21']:.4e}")
    print(f"cociente de abundancias (dex): verdadero 0.300 ; media MC {r['dex_media']:.4f} ; dispersion MC {r['dex_sd']:.4f} ; propagacion analitica {r['dex_pred']:.4f}")
    assert abs(r["pob2_suma"] - r["pob2_formula"]) < 1e-12 * r["pob2_suma"] + 1e-300
    assert 7000 < r["T_pico"] < 14000
    assert abs(r["dex_sd"] / r["dex_pred"] - 1) < 0.10
    assert abs(r["dex_media"] - 0.30) < 3 * r["dex_sd"] / math.sqrt(3000)
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
