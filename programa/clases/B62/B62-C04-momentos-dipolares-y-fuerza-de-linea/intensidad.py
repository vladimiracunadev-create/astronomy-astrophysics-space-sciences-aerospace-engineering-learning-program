#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C04: momento dipolar, fuerza de linea, coeficiente A e intensidad de catalogo del 12C16O.

Datos (consultados el 2026-11-09):
  - CODATA 2022 (NIST): h, c, k, eps0 (derivada de e, h, alpha no se usa: eps0 = 1/(mu0 c^2) con mu0 = 4 pi 1e-7 como aproximacion
    declarada, error relativo ~1e-10 que no afecta a las tolerancias), 1 D = 1e-21/c C m. S1.
  - Catalogo JPL c028001.cat: LGINT (log10 nm^2 MHz a 300 K) de las lineas J=1-0, 2-1, 3-2. S4.
  - Documento del catalogo JPL (Pickett et al., ed. 2 mayo 2003): Ec. (2) I = 4.16231e-5 nu S mu^2 [exp(-E''/kT)-exp(-E'/kT)]/Q,
    con nu en MHz, mu en Debye, I en nm^2 MHz; conversion a cm^-1/(molecula cm^-2): dividir por 2.99792458e18. S3.
  - LAMDA co.dat: coeficientes A de Einstein 7.203e-08, 6.910e-07, 2.497e-06 s^-1 (J=1-0, 2-1, 3-2). S5.
Modelo: A(J->J-1) = 16 pi^3 nu^3 mu^2 /(3 eps0 h c^3) * J/(2J+1) ; fuerza de linea S = J (lineas rotacionales de molecula lineal).
Supuesto: Q (funcion de particion rotacional a 300 K) se calcula con B0, D (C01); no se consulto el valor tabulado del catalogo.
Resultado: el momento dipolar IMPLICITO en cada dato; no se consulto un valor de laboratorio del momento dipolar.
Tolerancias: coeficiente de la Ec. (2) recalculado vs 4.16231e-5: 1e-4 relativo (el documento es de 2003 y usa constantes anteriores a CODATA 2022); mu implicito por A en tres lineas coincide a 1e-3 relativo;
  mu implicito por JPL vs por LAMDA: 3 % (Q aproximado y A con 4 cifras).
"""
from __future__ import annotations
import math, platform, sys

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
MU0 = 4e-7 * math.pi
EPS0 = 1.0 / (MU0 * C * C)
DEBYE = 1e-21 / C                     # C m
B0, DE = 1.922529, 6.12147e-06        # cm^-1 (B0 = Be - alpha_e/2, WebBook; calculo propio)
JPL = {1: (115271.2018, -5.0105, 0.0), 2: (230538.0000, -4.1197, 3.8450), 3: (345795.9899, -3.6118, 11.5350)}  # MHz, LGINT, ELO cm^-1
LAMDA_A = {1: 7.203e-08, 2: 6.910e-07, 3: 2.497e-06}
CM1_A_J = H * C * 100.0               # J por cm^-1


def A_einstein(nu_hz: float, mu_debye: float, Ju: int) -> float:
    mu = mu_debye * DEBYE
    return 16 * math.pi ** 3 * nu_hz ** 3 * mu ** 2 / (3 * EPS0 * H * C ** 3) * Ju / (2 * Ju + 1)


def Q_rot(T: float) -> float:
    kT = KB * T
    return sum((2 * J + 1) * math.exp(-(B0 * J * (J + 1) - DE * (J * (J + 1)) ** 2) * CM1_A_J / kT) for J in range(0, 200))


def intensidad_jpl(nu_mhz, S, mu_d, Elo_cm1, Eup_cm1, T):
    """Ec. (2) del catalogo JPL con el coeficiente recalculado de las constantes (nm^2 MHz)."""
    coef = coeficiente()
    kT = KB * T
    fac = math.exp(-Elo_cm1 * CM1_A_J / kT) - math.exp(-Eup_cm1 * CM1_A_J / kT)
    return coef * nu_mhz * S * mu_d ** 2 * fac / Q_rot(T)


def coeficiente() -> float:
    """8 pi^3/(3 h c) /(4 pi eps0) en nm^2 MHz por (MHz Debye^2)."""
    si = 8 * math.pi ** 3 / (3 * H * C) / (4 * math.pi * EPS0) * DEBYE ** 2   # m^2 por (Hz * D^2) ... integral sobre la linea en m^2 Hz
    # I[m^2 Hz] = si * nu[Hz]; con nu en MHz: x1e6; paso a nm^2 MHz: x1e18 (m^2->nm^2) y /1e6 (Hz->MHz)
    return si * 1e6 * 1e18 / 1e6


def main() -> int:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos: CODATA 2022, LGINT de JPL (c028001.cat), A de LAMDA (co.dat) y Ec. (2) del documento JPL, consultados el 2026-11-09")
    c2 = coeficiente()
    print(f"Coeficiente de la Ec. (2) recalculado = {c2:.5e} (documento JPL: 4.16231e-05) ; dif. rel. = {abs(c2-4.16231e-5)/4.16231e-5:.1e}")
    assert abs(c2 - 4.16231e-5) / 4.16231e-5 < 1e-4, "coeficiente de la Ec. (2) fuera de tolerancia"
    # mu implicito por A de LAMDA
    print("Momento dipolar implicito por los A de LAMDA (A es proporcional a mu^2):")
    mus = []
    for J, A in LAMDA_A.items():
        nu = JPL[J][0] * 1e6
        a1 = A_einstein(nu, 1.0, J)
        mu = math.sqrt(A / a1)
        mus.append(mu)
        print(f"  J = {J}->{J-1}: nu = {nu/1e9:9.4f} GHz ; A(mu=1 D) = {a1:.4e} s^-1 ; mu implicito = {mu:.5f} D")
    assert max(mus) / min(mus) - 1 < 1e-3
    mu_lamda = sum(mus) / 3
    # mu implicito por intensidad JPL
    T = 300.0
    print(f"Q rotacional a 300 K (calculada) = {Q_rot(T):.3f}")
    mus_j = []
    for J, (nu, lg, elo) in JPL.items():
        eup = elo + 2 * B0 * J    # energia superior aproximada (cm^-1), rotor rigido
        I_nm2MHz = 10 ** lg
        I_cm = I_nm2MHz / 2.99792458e18
        i1 = intensidad_jpl(nu, J, 1.0, elo, eup, T)
        mu = math.sqrt(I_nm2MHz / i1)
        mus_j.append(mu)
        print(f"  J = {J}->{J-1}: LGINT = {lg:7.4f} -> {I_nm2MHz:.4e} nm^2 MHz = {I_cm:.4e} cm^-1/(molecula cm^-2) ; mu implicito = {mu:.5f} D")
    mu_jpl = sum(mus_j) / 3
    print(f"mu medio implicito: LAMDA = {mu_lamda:.5f} D ; JPL = {mu_jpl:.5f} D ; dif. rel. = {abs(mu_jpl-mu_lamda)/mu_lamda:.2e}")
    assert abs(mu_jpl - mu_lamda) / mu_lamda < 0.03
    # Escalado de la intensidad a otra temperatura: Ec. (3) frente a Ec. (4) (n = 1, molecula lineal)
    for J, (nu, lg, elo) in JPL.items():
        eup = elo + 2 * B0 * J
        I300 = 10 ** lg
        I20_exacta = I300 * Q_rot(300.0) / Q_rot(20.0) * (math.exp(-elo * CM1_A_J / (KB * 20)) - math.exp(-eup * CM1_A_J / (KB * 20))) / (math.exp(-elo * CM1_A_J / (KB * 300)) - math.exp(-eup * CM1_A_J / (KB * 300)))
        print(f"  J = {J}->{J-1}: I(20 K) por Ec. (3) = {I20_exacta:.4e} nm^2 MHz ; cociente I(20 K)/I(300 K) = {I20_exacta/I300:.3f}")
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
