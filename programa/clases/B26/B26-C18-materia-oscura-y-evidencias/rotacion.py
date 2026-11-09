#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C18: curva de rotacion SINTETICA con halo de materia oscura y comparacion con solo bariones.

Datos: ninguno observado. Galaxia sintetica: componente barionica de Plummer (M_b = 5e10 Msol, a = 3 kpc), halo
pseudo-isotermo (v_inf = 180 km/s, r_c = 5 kpc) y ruido gaussiano de 5 km/s en 20 radios (1 a 30 kpc):
valores ILUSTRATIVOS. G (NIST CODATA 2022); GM_sol (IAU 2015 B3, arXiv:1510.07674); 1 kpc = 1e3 * 648000/pi
au con 1 au del IERS TN36 (consultados 2026-11-09). La separacion de 8 sigma entre el centro de masa por
lentes y el gas del Cumulo Bala (Clowe et al., astro-ph/0608407) se cita solo como contexto (resumen).
Modelo: v^2(r) = G M_b r^2/(r^2 + a^2)^(3/2) + v_inf^2 [1 - (r_c/r) atan(r/r_c)]. Ajuste lineal por minimos
cuadrados ponderados de v^2 = A f_b(r) + B f_h(r) con f_b, f_h conocidas (r_c, a fijos). Comparacion con el
ajuste de solo bariones.
Supuestos: simetria esferica, orbitas circulares. Validez: ilustrativa.
Tolerancia: A y B dentro de 3 sigma; el modelo sin halo debe tener chi^2/dof > 10 veces el del modelo completo.
"""
from __future__ import annotations
import math
import platform
import random
import sys

G = 6.67430e-11
GM_SOL = 1.3271244e20
M_SOL = GM_SOL / G
KPC = 1e3 * (648000 / math.pi) * 1.49597870700e11
MB, A_PL, VINF, RC, SIG = 5e10 * M_SOL, 3.0, 180e3, 5.0, 5e3


def fb(r):
    rm = r * KPC
    return G * rm * rm / (rm * rm + (A_PL * KPC) ** 2) ** 1.5       # v^2 por unidad de masa barionica


def fh(r):
    return 1 - RC / r * math.atan(r / RC)


def resuelve(rs, v2, sig2, bases):
    n = len(bases)
    m = [[sum(bases[i](r) * bases[j](r) / s for r, s in zip(rs, sig2)) for j in range(n)] for i in range(n)]
    y = [sum(bases[i](r) * v / s for r, v, s in zip(rs, v2, sig2)) for i in range(n)]
    if n == 1:
        inv = [[1 / m[0][0]]]
    else:
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        inv = [[m[1][1] / det, -m[0][1] / det], [-m[1][0] / det, m[0][0] / det]]
    par = [sum(inv[i][j] * y[j] for j in range(n)) for i in range(n)]
    err = [math.sqrt(inv[i][i]) for i in range(n)]
    chi2 = sum((v - sum(par[i] * bases[i](r) for i in range(n))) ** 2 / s for r, v, s in zip(rs, v2, sig2))
    return par, err, chi2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(18)
    rs = [1 + 29 * i / 19 for i in range(20)]
    v_real = [math.sqrt(MB * fb(r) + VINF ** 2 * fh(r)) for r in rs]
    v_obs = [v + rng.gauss(0, SIG) for v in v_real]
    v2 = [v * v for v in v_obs]
    sig2 = [(2 * v * SIG) ** 2 for v in v_obs]
    par, err, chi2 = resuelve(rs, v2, sig2, [fb, fh])
    mb_fit, vinf2 = par[0], par[1]
    assert abs(par[0] - MB) < 3 * err[0] and abs(par[1] - VINF ** 2) < 3 * err[1], "parametros fuera de 3 sigma"
    dof = len(rs) - 2
    print(f"con halo: M_b = {mb_fit / M_SOL:.3e} Msol (verdadero 5e10) ; v_inf = {math.sqrt(vinf2) / 1e3:.1f} km/s (verdadero 180) ; chi2/dof = {chi2 / dof:.2f}")
    par1, err1, chi2_1 = resuelve(rs, v2, sig2, [fb])
    print(f"solo bariones: M_b = {par1[0] / M_SOL:.3e} Msol ; chi2/dof = {chi2_1 / (len(rs) - 1):.1f}")
    assert chi2_1 / (len(rs) - 1) > 10 * (chi2 / dof), "el modelo sin halo debe ajustar mucho peor"
    v_kep = [math.sqrt(mb_fit * fb(r)) / 1e3 for r in rs]
    for i in (0, 5, 10, 19):
        print(f"r = {rs[i]:5.1f} kpc: v_obs = {v_obs[i] / 1e3:6.1f} km/s ; componente barionica = {v_kep[i]:6.1f} km/s")
    r30 = 30 * KPC
    m_din = (v_obs[-1]) ** 2 * r30 / G / M_SOL
    m_bar30 = MB * (30 ** 3 / (30 ** 2 + A_PL ** 2) ** 1.5)       # masa de Plummer dentro de 30 kpc
    print(f"masa dinamica dentro de 30 kpc ~ v^2 r/G = {m_din:.3e} Msol ; barionica (Plummer) = {m_bar30 / M_SOL:.3e} Msol ; "
          f"fraccion barionica = {m_bar30 / M_SOL / m_din:.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
