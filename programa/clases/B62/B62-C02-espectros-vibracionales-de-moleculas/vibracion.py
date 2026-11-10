#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B62-C02: niveles vibracionales anarmonicos y banda ro-vibracional 1-0 del 12C16O.

Datos (consultados el 2026-11-09): NIST Chemistry WebBook, CO X 1Sigma+: we = 2169.81358, wexe = 13.28831, Be = 1.93128087,
alpha_e = 0.01750441 (cm^-1). S2. CODATA 2022 (c, u). S1.
Modelo: G(v) = we (v+1/2) - wexe (v+1/2)^2 ; B_v = Be - alpha_e (v+1/2) ;
  R(J) = nu0 + (B1+B0)(J+1) + (B1-B0)(J+1)^2 ; P(J) = nu0 - (B1+B0) J + (B1-B0) J^2   (J = nivel inferior), sin distorsion centrifuga.
Masas: numeros de masa enteros 12, 13 y 16 (aproximacion; no se consulto una tabla de masas).
Los resultados son CALCULOS del modelo con constantes consultadas; no son espectros observados.
Pruebas: (i) combinacion de diferencias R(J-1) - P(J+1) = 4 B0 (J+1/2) exacta en el modelo (tolerancia 1e-9 cm^-1);
  (ii) R(J) - P(J) = 4 B1 (J+1/2) exacta en el modelo (tolerancia 1e-9 cm^-1); (iii) k de fuerza armonica en N/m con tolerancia 1 % respecto a 1902 N/m (valor propio, solo orden de magnitud).
"""
from __future__ import annotations
import math, platform, sys

C = 299792458.0
U = 1.66053906892e-27
WE, WEXE, BE, AE = 2169.81358, 13.28831, 1.93128087, 0.01750441


def G(v: int) -> float:
    return WE * (v + 0.5) - WEXE * (v + 0.5) ** 2


def Bv(v: int) -> float:
    return BE - AE * (v + 0.5)


def R(J, nu0, B1, B0):
    return nu0 + (B1 + B0) * (J + 1) + (B1 - B0) * (J + 1) ** 2


def P(J, nu0, B1, B0):
    return nu0 - (B1 + B0) * J + (B1 - B0) * J ** 2


def main() -> int:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Constantes del WebBook (NIST) y CODATA 2022 consultadas el 2026-11-09; el resultado es un calculo, no un espectro observado")
    print("Niveles G(v) [cm^-1] y separaciones G(v+1)-G(v):")
    for v in range(0, 5):
        print(f"  v = {v}: G = {G(v):10.3f} ; salto a v+1 = {G(v+1)-G(v):9.3f} (we - 2 wexe (v+1) = {WE-2*WEXE*(v+1):9.3f})")
        assert abs((G(v + 1) - G(v)) - (WE - 2 * WEXE * (v + 1))) < 1e-9
    nu0 = G(1) - G(0)
    print(f"Origen de la banda fundamental 1-0 = {nu0:.4f} cm^-1 = {1e4/nu0:.4f} um")
    print(f"Primer sobretono 2-0 = {G(2)-G(0):.4f} cm^-1 (el doble de 1-0 serian {2*nu0:.4f}; la anarmonicidad lo baja {2*nu0-(G(2)-G(0)):.3f} cm^-1)")
    B0, B1 = Bv(0), Bv(1)
    print(f"B0 = {B0:.6f} cm^-1 ; B1 = {B1:.6f} cm^-1")
    print("  J   P(J) [cm^-1]   R(J) [cm^-1]")
    for J in range(0, 6):
        pj = P(J, nu0, B1, B0) if J > 0 else float('nan')
        print(f" {J:2d}  {pj:12.4f}  {R(J, nu0, B1, B0):12.4f}")
    # pruebas de combinacion de diferencias
    peor = 0.0
    for J in range(1, 12):
        d2 = R(J - 1, nu0, B1, B0) - P(J + 1, nu0, B1, B0)
        peor = max(peor, abs(d2 - 4 * B0 * (J + 0.5)))
    print(f"Combinacion de diferencias: max |R(J-1)-P(J+1) - 4 B0 (J+1/2)| = {peor:.2e} cm^-1")
    assert peor < 1e-9
    # R(J)-P(J) = 4 B1 (J+1/2) tambien exacta en el modelo
    peor1 = max(abs((R(J, nu0, B1, B0) - P(J, nu0, B1, B0)) - 4 * B1 * (J + 0.5)) for J in range(1, 12))
    print(f"Combinacion R(J)-P(J) = 4 B1 (J+1/2): max error = {peor1:.2e} cm^-1")
    assert peor1 < 1e-9
    # constante de fuerza armonica
    mu = 12.0 * 16.0 / 28.0 * U
    k = mu * (2 * math.pi * C * WE * 100.0) ** 2
    print(f"Constante de fuerza armonica k = mu (2 pi c we)^2 = {k:.1f} N/m (masas enteras)")
    assert abs(k - 1902.0) / 1902.0 < 0.01
    # isotopologo 13C16O (masas enteras, Born-Oppenheimer)
    mu13 = 13.0 * 16.0 / 29.0
    rho = math.sqrt((12.0 * 16.0 / 28.0) / mu13)
    print(f"13C16O (masas enteras): rho = {rho:.5f} ; we = {WE*rho:.3f} cm^-1 ; B_e = {BE*rho*rho:.5f} cm^-1 ; origen 1-0 aprox {(WE*rho)-2*(WEXE*rho*rho):.3f} cm^-1")
    # estimacion de energia de disociacion (Morse): De ~ we^2/(4 wexe)
    print(f"Estimacion de Morse De = we^2/(4 wexe) = {WE**2/(4*WEXE):.0f} cm^-1 (sin comparar con ningun valor consultado)")
    print("Pruebas superadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
