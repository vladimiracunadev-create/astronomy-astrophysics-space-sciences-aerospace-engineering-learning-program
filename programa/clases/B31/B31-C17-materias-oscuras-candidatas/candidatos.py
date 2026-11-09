#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C17: curvas de rotacion con y sin halo, longitud de onda de de Broglie de un candidato ultraligero y retroceso nuclear.

Datos: G, h, c, e (NIST CODATA 2022), GM_sol (UAI 2015 B3) y 1 pc = 648000/pi au (UAI y IERS), consultados 2026-11-09. La masa del disco (5e10 M_sol), la longitud de escala (3 kpc), el halo
isotermo (v_inf = 200 km/s, radio de nucleo 5 kpc), la masa de la particula ultraligera (1e-22 eV), la masa del candidato (100 GeV), el blanco (A = 131), la velocidad caracteristica (220 km/s)
y el numero de sucesos (200 000, semilla fija) son ILUSTRATIVOS (sinteticos); no se ajusta ninguna galaxia ni experimento.
Modelo: (1) v^2 = G M(<r)/r con M_disco(<r) = M_d [1 - (1 + r/R_d) e^(-r/R_d)] (aproximacion esferica) y halo isotermo con M_halo(<r) = v_inf^2 a (r/a - arctan(r/a))/G; pendiente logaritmica
de la curva del disco en el regimen kepleriano (-1/2); (2) lambda = h/(m v) = h c/(m c^2 beta); (3) retroceso elastico: E_R = (mu^2 v^2/m_N)(1 - cos theta*), mu masa reducida; media sobre angulos
isotropos mu^2 <v^2>/m_N con <v^2> = 3 v_0^2/2 de una distribucion maxwelliana; Monte Carlo frente al valor analitico.
Supuestos: distribuciones esfericas, retroceso elastico no relativista. Validez: orden de magnitud.
Tolerancia: pendiente kepleriana dentro de 0.05 de -0.5; retroceso medio de Monte Carlo dentro de 1 % del analitico.
"""
from __future__ import annotations
import math
import platform
import random
import sys

G, H, C, E = 6.67430e-11, 6.62607015e-34, 299792458.0, 1.602176634e-19
GM_SOL = 1.3271244e20
AU = 1.49597870700e11
PC = 648000 / math.pi * AU
KPC = 1e3 * PC
M_SOL = GM_SOL / G


def v_disco(r_kpc, md=5e10, rd=3.0):
    r = r_kpc * KPC
    x = r_kpc / rd
    m = md * M_SOL * (1 - (1 + x) * math.exp(-x))
    return math.sqrt(G * m / r)


def v_halo2(r_kpc, vinf=2e5, a_kpc=5.0):
    x = r_kpc / a_kpc
    return vinf ** 2 * (1 - math.atan(x) / x)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"M_sol = GM/G = {M_SOL:.4e} kg ; 1 kpc = {KPC:.6e} m")
    print(f"{'r [kpc]':>8} {'v disco [km/s]':>15} {'v disco + halo [km/s]':>22}")
    filas = {}
    for r in (2, 5, 10, 20, 40, 80):
        vd = v_disco(r)
        vt = math.sqrt(vd ** 2 + v_halo2(r))
        filas[r] = (vd, vt)
        print(f"{r:8d} {vd / 1e3:15.2f} {vt / 1e3:22.2f}")
    pend = math.log(filas[80][0] / filas[40][0]) / math.log(2)
    pend_t = math.log(filas[80][1] / filas[40][1]) / math.log(2)
    print(f"pendiente logaritmica entre 40 y 80 kpc: solo disco = {pend:.3f} (kepleriano -0.5) ; con halo = {pend_t:.3f}")
    assert abs(pend + 0.5) < 0.05
    # de Broglie
    m_ev, v = 1e-22, 200e3
    lam = H * C / (m_ev * (v / C) * C ** 0) / C            # h/(m v) con m c^2 en eV: h c/(m c^2) = 1.2398e-6 eV m / 1e-22 eV
    lam = (H * C / E) / m_ev / (v / C)
    print(f"longitud de onda de de Broglie de una particula de 1e-22 eV a 200 km/s: {lam:.4e} m = {lam / KPC:.3f} kpc")
    # retroceso
    mx, a_n = 100.0, 131
    mn = a_n * 0.93149410372
    mu = mx * mn / (mx + mn)
    v0 = 220e3
    v2 = 1.5 * v0 ** 2
    er_ana = mu ** 2 * v2 / C ** 2 / mn * 1e6                    # keV: (GeV) (v/c)^2 -> GeV ; x1e6 keV/GeV
    rng = random.Random(20261109)
    n = 200000
    s = 0.0
    sig = v0 / math.sqrt(2)
    for _ in range(n):
        vx, vy, vz = rng.gauss(0, sig), rng.gauss(0, sig), rng.gauss(0, sig)
        v2i = vx * vx + vy * vy + vz * vz
        ct = 2 * rng.random() - 1
        s += mu ** 2 * v2i / C ** 2 / mn * (1 - ct) * 1e6
    er_mc = s / n
    print(f"WIMP de 100 GeV sobre un blanco A = 131 (m_N = {mn:.2f} GeV, mu = {mu:.2f} GeV): <E_R> analitico = {er_ana:.3f} keV ; Monte Carlo = {er_mc:.3f} keV ; cociente = {er_mc / er_ana:.4f}")
    assert abs(er_mc / er_ana - 1) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
