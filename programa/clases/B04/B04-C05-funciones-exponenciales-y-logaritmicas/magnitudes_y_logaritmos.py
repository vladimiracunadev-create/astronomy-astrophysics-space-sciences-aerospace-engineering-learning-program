#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C05: logaritmos y la escala de magnitudes bolométricas.

Datos (PUBLICADOS; definiciones): IAU 2015 Resolución B2 (arXiv:1510.06262):
L0 = 3.0128e28 W (M_bol = 0), f0 = 2.518021002e-8 W/m2 (m_bol = 0) y solar
m_bol = -26.832; IAU 2015 B3 (arXiv:1510.07674): L_sol nominal = 3.828e26 W,
S_sol nominal = 1361 W/m2; IAU 2012/2015: 1 au = 149 597 870 700 m y
1 pc = 648000/pi au. Estrellas hipotéticas: SINTÉTICAS.
Modelo: M = -2.5 log10(L/L0), m = -2.5 log10(f/f0), m - M = 5 log10(d/10 pc).
Supuestos: emisión isótropa, sin extinción interestelar. Validez: magnitud
bolométrica (no una banda concreta). Tolerancia: 1e-8 relativa en f0 (la fuente
da 10 cifras); 2e-3 mag en las magnitudes solares.
"""
from __future__ import annotations
import math, platform, sys

L0 = 3.0128e28
F0_PUBLICADO = 2.518021002e-8
L_SOL = 3.828e26
S_SOL = 1361.0
AU = 149_597_870_700.0
PC = 648_000.0 / math.pi * AU


def M_de_L(L):
    return -2.5 * math.log10(L / L0)


def m_de_f(f, f0=F0_PUBLICADO):
    return -2.5 * math.log10(f / f0)


def modulo(d_pc):
    return 5.0 * math.log10(d_pc / 10.0)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    # --- pruebas ---
    f0_calc = L0 / (4 * math.pi * (10 * PC) ** 2)       # definición: L0 visto a 10 pc
    assert abs(f0_calc / F0_PUBLICADO - 1) < 1e-8, f0_calc
    assert abs(M_de_L(L_SOL) - 4.74) < 5e-3
    assert abs(m_de_f(S_SOL) - (-26.832)) < 2e-3
    d_au_pc = AU / PC                                    # 1 au en pc
    assert abs(M_de_L(L_SOL) + modulo(d_au_pc) - m_de_f(S_SOL)) < 2e-3   # coherencia M, m, d
    for f in (1e-12, 1.0, 1361.0):                       # ida y vuelta log/exp
        assert abs(F0_PUBLICADO * 10 ** (-0.4 * m_de_f(f)) / f - 1) < 1e-12
    assert abs(100 ** 0.2 - 2.5118864315) < 1e-9        # razón de Pogson
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (f0 desde L0 a 10 pc, magnitudes solares, coherencia M-m-d, ida y vuelta)")
    print(f"\nf0 calculado desde L0 y 10 pc = {f0_calc:.9e} W/m2  (publicado {F0_PUBLICADO:.9e})")
    print(f"M_bol del Sol = {M_de_L(L_SOL):.4f} mag;  m_bol del Sol = {m_de_f(S_SOL):.4f} mag")
    print(f"Razón de Pogson 100^(1/5) = {100 ** 0.2:.6f}")
    print("\nEstrellas hipotéticas (sintéticas), L en unidades solares nominales:")
    print(f"{'L/Lsol':>8}{'M_bol':>9}{'d (pc)':>9}{'m_bol':>9}{'flujo (W/m2)':>15}")
    for Ls, d in ((1.0, 10.0), (100.0, 10.0), (100.0, 100.0), (0.01, 1.3)):
        M = M_de_L(Ls * L_SOL)
        m = M + modulo(d)
        f = F0_PUBLICADO * 10 ** (-0.4 * m)
        print(f"{Ls:8.2f}{M:9.3f}{d:9.1f}{m:9.3f}{f:15.4e}")
    print("\nDiferencia de 5 mag = factor de flujo", f"{100 ** (5 / 5):.0f}", "; 1 mag =", f"{10 ** 0.4:.4f}")
    print("\nExtinción exponencial I = I0 exp(-tau): tau = 0,25 (sintético)")
    tau = 0.25
    print(f"  I/I0 = {math.exp(-tau):.4f};  pérdida = {-2.5 * math.log10(math.exp(-tau)):.4f} mag "
          f"(= 1,0857 tau = {2.5 / math.log(10) * tau:.4f})")
    print("  Tiempo de duplicación con crecimiento 3 % por periodo:",
          f"{math.log(2) / math.log(1.03):.2f} periodos")


if __name__ == "__main__":
    main()
