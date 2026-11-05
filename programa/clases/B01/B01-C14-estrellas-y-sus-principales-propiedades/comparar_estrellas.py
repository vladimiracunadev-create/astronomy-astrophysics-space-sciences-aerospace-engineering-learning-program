#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C14: relacionar temperatura, radio y luminosidad de estrellas.

Datos PUBLICADOS: NASA Exoplanet Archive, tabla pscomppars (consulta TAP del 2026-11-05;
archivo mutable) con T_eff [K], radio [R_sol], log10(L/L_sol) y distancia [pc] de cinco
estrellas anfitrionas; Sol: T_eff 5772 K, R = 6,957e8 m y L = 3,828e26 W (valores
nominales IAU 2015 B3); constantes SI exactas h, c, k (BIPM, 9.ª ed.).
Modelo: ley de Stefan–Boltzmann L = 4π R² σ T⁴ con σ = 2π⁵k⁴/(15 c² h³) (derivada);
cuerpo negro. Supuestos: la estrella emite como cuerpo negro de temperatura efectiva
constante; R y T de la tabla son compatibles entre sí. Dominio de validez: estrellas con
T_eff y R publicados; no sirve para estrellas con radio inflado ni binarias. Tolerancias:
Sol, 0,2 % entre L calculada y L nominal; σ derivado frente a CODATA 2014 (5,670367e-8),
1e-5 relativa; estrellas, 0,10 dex en log10(L).
"""

from __future__ import annotations

import math
import platform
import sys

H, C, K = 6.626_070_15e-34, 299_792_458, 1.380_649e-23
SIGMA = 2 * math.pi**5 * K**4 / (15 * C**2 * H**3)
R_SOL, T_SOL, L_SOL = 6.957e8, 5772.0, 3.828e26
AU = 149_597_870_700
PC_LY = 3.2615637771

# nombre: (T_eff K, R en R_sol, log10(L/L_sol) publicado, distancia pc)
ESTRELLAS = {
    "TRAPPIST-1": (2566.0, 0.1192, -3.25727, 12.42988881),
    "Proxima Cen": (2900.0, 0.141, -2.82102, 1.30119),
    "tau Cet": (5310.0, 0.83, -0.30539, 3.60304),
    "Kepler-452": (5757.0, 1.11, 0.08448, 551.727),
    "HD 209458": (6091.0, 1.19, 0.23086, 48.3016),
}


def luminosidad(radio_m: float, t: float) -> float:
    return 4 * math.pi * radio_m**2 * SIGMA * t**4


def log_l_relativa(r_rel: float, t: float) -> float:
    return math.log10(r_rel**2 * (t / T_SOL) ** 4)


def pruebas() -> None:
    assert abs(SIGMA - 5.670367e-8) / 5.670367e-8 < 1e-5                       # CODATA 2014 (leída en IAU 2015 B3)
    assert abs(luminosidad(R_SOL, T_SOL) - L_SOL) / L_SOL < 2e-3               # Sol
    flujo = L_SOL / (4 * math.pi * AU**2)
    assert abs(flujo - 1361) < 2                                                # constante solar nominal
    for nombre, (t, r, logl, _) in ESTRELLAS.items():
        assert abs(log_l_relativa(r, t) - logl) < 0.10, nombre


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    print(f"σ derivada = {SIGMA:.6e} W m^-2 K^-4")
    print(f"Sol: L(R,T) = {luminosidad(R_SOL, T_SOL):.4e} W (nominal {L_SOL:.3e}); flujo a 1 au = {L_SOL / (4 * math.pi * AU**2):.1f} W/m²")
    b = H * C / (K * 4.965114231744276)
    print("Estrella       T[K]   R[Rsol]  logL_calc  logL_pub   dist[ly]   λ_max[nm]")
    for n, (t, r, logl, d) in ESTRELLAS.items():
        print(f"{n:12s} {t:7.0f} {r:8.3f} {log_l_relativa(r, t):9.3f} {logl:9.3f} {d * PC_LY:10.2f} {b / t * 1e9:10.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
