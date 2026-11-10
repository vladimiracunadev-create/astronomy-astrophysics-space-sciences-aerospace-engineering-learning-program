#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C01: rotor rigido y con distorsion centrifuga del 12C16O frente a lineas del catalogo JPL.

Datos (consultados el 2026-11-09):
  - CODATA 2022 (NIST): h, c, k, u. S1.
  - NIST Chemistry WebBook, CO X 1Sigma+: Be, alpha_e, De, re. S2.
  - Catalogo JPL (archivo c028001.cat), frecuencias J=1-0..6-5 en MHz con error 0.0005 MHz. S4.
Modelo: E(J) = B J(J+1) - D J^2 (J+1)^2 [cm^-1]; nu(J+1<-J) = 2B(J+1) - 4D(J+1)^3.
Masas atomicas: se usan NUMEROS DE MASA enteros (12 y 16) como aproximacion (no se consulto una tabla de masas):
  introduce ~1e-4 relativo en el momento de inercia; se declara en la tolerancia.
Supuestos: molecula lineal, estado vibracional fundamental, sin estructura hiperfina.
Validez: B0 = Be - alpha_e/2 es una relacion estandar (calculo propio, no leida en la fuente).
Tolerancias: B calculado con re y masas enteras vs Be del WebBook: 5e-3 relativo; frecuencias con B0,D vs JPL: 2e-6 relativo.
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34          # J s (exacto, CODATA 2022)
C = 299792458.0             # m/s (exacto)
KB = 1.380649e-23           # J/K (exacto)
U = 1.66053906892e-27       # kg (CODATA 2022)

# NIST WebBook, 12C16O X 1Sigma+ (cm^-1, Angstrom)
BE, ALPHA_E, DE, RE_A = 1.93128087, 0.01750441, 6.12147e-06, 1.128323
B0 = BE - ALPHA_E / 2.0
# JPL c028001.cat (MHz): J_superior 1..6
JPL = {1: 115271.2018, 2: 230538.0000, 3: 345795.9899, 4: 461040.7682, 5: 576267.9305, 6: 691473.0763}


def cm1_a_mhz(x_cm1: float) -> float:
    return x_cm1 * C * 100.0 / 1e6


def B_rigido(re_angstrom: float, m1: float, m2: float) -> float:
    mu = m1 * m2 / (m1 + m2) * U
    I = mu * (re_angstrom * 1e-10) ** 2
    return H / (8 * math.pi ** 2 * C * 100.0 * I)   # cm^-1


def nu_mhz(Jinf: int, B: float, D: float) -> float:
    """Frecuencia (MHz) de la transicion Jinf+1 <- Jinf."""
    return cm1_a_mhz(2 * B * (Jinf + 1) - 4 * D * (Jinf + 1) ** 3)


def main() -> int:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos: CODATA 2022 (h, c, k, u), NIST WebBook (CO) y 6 lineas del catalogo JPL, consultados el 2026-11-09")
    # 1. B desde la geometria
    Brig = B_rigido(RE_A, 12.0, 16.0)
    print(f"B rigido (re = {RE_A} A, masas 12 y 16 u) = {Brig:.5f} cm^-1 ; Be (WebBook) = {BE:.5f} ; dif. relativa = {abs(Brig-BE)/BE:.2e}")
    assert abs(Brig - BE) / BE < 5e-3, "B rigido fuera de tolerancia"
    print(f"B0 = Be - alpha_e/2 = {B0:.6f} cm^-1 = {cm1_a_mhz(B0):.2f} MHz ; 2*B0 = {cm1_a_mhz(2*B0):.2f} MHz")
    # 2. Frecuencias: rigido vs con distorsion vs JPL
    print(" J_sup   JPL [MHz]       rigido [MHz]   dif. rel.    con D [MHz]    dif. rel.")
    peor_D = 0.0
    for Jsup, f in JPL.items():
        fr = nu_mhz(Jsup - 1, B0, 0.0)
        fd = nu_mhz(Jsup - 1, B0, DE)
        peor_D = max(peor_D, abs(fd - f) / f)
        print(f"  {Jsup}->{Jsup-1}  {f:13.4f}  {fr:13.4f}  {abs(fr-f)/f:9.2e}  {fd:13.4f}  {abs(fd-f)/f:9.2e}")
    print(f"Peor diferencia relativa con distorsion = {peor_D:.2e}")
    assert peor_D < 2e-6, "frecuencias con distorsion fuera de tolerancia"
    # 3. Niveles y espaciado 2B (cm^-1)
    print("Niveles E(J) = B0 J(J+1) - D J^2(J+1)^2 [cm^-1]:", ", ".join(f"J={J}: {B0*J*(J+1)-DE*(J*(J+1))**2:.6f}" for J in range(0, 5)))
    # 4. Poblaciones de Boltzmann a 20 K y 300 K
    for T in (20.0, 300.0):
        w = [(2 * J + 1) * math.exp(-B0 * J * (J + 1) * H * C * 100.0 / (KB * T)) for J in range(0, 80)]
        Z = sum(w)
        Jpico = max(range(len(w)), key=lambda j: w[j])
        Japrox = math.sqrt(KB * T / (2 * B0 * H * C * 100.0)) - 0.5
        print(f"T = {T:5.1f} K: Z = {Z:8.3f} (kT/hcB0 + 1/3 = {KB*T/(H*C*100*B0)+1/3:8.3f}) ; J del pico = {Jpico} (formula {Japrox:.2f})")
        assert abs(Z - (KB * T / (H * C * 100 * B0) + 1 / 3)) / Z < 5e-3
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
