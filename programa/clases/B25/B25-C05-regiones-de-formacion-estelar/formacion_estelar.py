#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C05: esfera de Stromgren, tiempo de agotamiento y eficiencia por caida libre.

Datos: coeficiente de recombinacion beta2 = 2e-16 T^(-3/4) m3/s (Wikipedia, "Stromgren sphere",
fuente secundaria consultada 2026-11-09, ILUSTRATIVO); indice de Schmidt N = 1,4 +- 0,15
(Kennicutt 1998, arXiv:astro-ph/9712213, resumen consultado 2026-11-09); SFR de la Galaxia
1,65 +- 0,19 Msol/yr (Licquia y Newman, citado en Bland-Hawthorn y Gerhard 2016, arXiv:1602.07702,
texto del PDF consultado 2026-11-09); masa de gas >= 8,9e9 Msol (suma de limites inferiores de la
Tabla I de Ferriere 2001, C03). G, m_p de NIST (CODATA 2022). Q = 1e49 fotones/s, n = 100 cm^-3 y
la eficiencia por caida libre 0,01 son valores SINTETICOS/ILUSTRATIVOS.
Modelo: esfera de hidrogeno uniforme y totalmente ionizada dentro de R_S, neutra fuera;
equilibrio ionizacion-recombinacion Q = (4 pi/3) R_S^3 n^2 beta2.
Supuestos: sin polvo, sin helio, T uniforme = 1e4 K, un solo emisor.
Validez: orden de magnitud. Tolerancias: 1e-9 (cierre del balance) y 1e-6 (biseccion).
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
MP = 1.67262192595e-27
PC_CM = 3.0856776e18
YR = 365.25 * 86400.0


def beta2(T):
    """cm^3/s desde 2e-16 T^-0.75 m^3/s."""
    return 2e-16 * T ** -0.75 * 1e6


def r_stromgren_cm(Q, n, T=1e4):
    return (3 * Q / (4 * math.pi * n * n * beta2(T))) ** (1 / 3)


def r_stromgren_biseccion(Q, n, T=1e4):
    """Resuelve int_0^R 4 pi r^2 n^2 beta2 dr = Q por biseccion (integral analitica r^3/3)."""
    lo, hi = 0.0, 1e24
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 4 * math.pi * n * n * beta2(T) * mid ** 3 / 3 < Q:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def t_depletion_rel(sig_ratio, N=1.4):
    """t_dep(S2)/t_dep(S1) = (S2/S1)^(1-N)."""
    return sig_ratio ** (1 - N)


def t_ff_yr(n_h2_cm3, mu_h2=2.8):
    rho = n_h2_cm3 * 1e6 * mu_h2 * MP
    return math.sqrt(3 * math.pi / (32 * G * rho)) / YR


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    Q, n = 1e49, 100.0
    rs = r_stromgren_cm(Q, n)
    # Prueba 1: cierre del balance
    assert abs(4 * math.pi / 3 * rs ** 3 * n * n * beta2(1e4) / Q - 1) < 1e-9
    # Prueba 2: biseccion independiente
    assert abs(r_stromgren_biseccion(Q, n) / rs - 1) < 1e-6
    # Prueba 3: escalas R ~ Q^(1/3) n^(-2/3)
    assert abs(r_stromgren_cm(8 * Q, n) / rs - 2) < 1e-9
    assert abs(r_stromgren_cm(Q, 8 * n) / rs - 0.25) < 1e-9
    # Prueba 4: referencia independiente (B24-C01): t_ff(n(H2)=1e4) = 0,308 Myr
    assert abs(t_ff_yr(1e4) / 1e6 - 0.308) < 0.001
    print(f"beta2(1e4 K) = {beta2(1e4):.2e} cm^3/s")
    print(f"R_S (Q = 1e49 /s, n = 100 cm^-3) = {rs / PC_CM:.2f} pc")
    print(f"R_S con Q x8: {r_stromgren_cm(8 * Q, n) / PC_CM:.2f} pc ; con n x8: {r_stromgren_cm(Q, 8 * n) / PC_CM:.2f} pc")
    print(f"t_dep(MW) = {8.9e9 / 1.65 / 1e9:.1f} Gyr (gas >= 8.9e9 Msol, SFR 1.65 Msol/yr)")
    print(f"t_dep(10 Sigma)/t_dep(Sigma) = {t_depletion_rel(10):.3f} (N = 1.4) ; N = 1: {t_depletion_rel(10, 1.0):.3f}")
    n_nube = 43.0
    tff = t_ff_yr(n_nube)
    m = 1.743e4
    print(f"nube de C04: n(H2) = {n_nube:.0f} cm^-3 -> t_ff = {tff / 1e6:.2f} Myr")
    print(f"SFR con eps_ff = 0.01: {0.01 * m / tff:.2e} Msol/yr")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
