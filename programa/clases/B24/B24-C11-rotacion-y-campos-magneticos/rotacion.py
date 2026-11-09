#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C11: rotacion estelar, rotacion critica y conservacion de J y del flujo.

Datos: GM_sol y R_sol nominales (IAU 2015 B3, arXiv:1510.07674); periodo sideral del Sol de
609.12 h a 16 grados de latitud (NASA Sun Fact Sheet, actualizada 2024-05-09). Los radios y
campos de la contraccion hipotetica (100 R_sol -> R_sol; 1 G -> estrella de neutrones de
10 km) son valores ILUSTRATIVOS (estimados), no una estrella concreta.
Modelo: v = 2 pi R cos(phi) / P; v_crit = sqrt(G M / R); momento angular J = I omega con
I = (2/5) M R^2 (esfera uniforme, comprobado por integral de volumen); con J y estructura fijas
omega R^2 = const; flujo magnetico congelado: B R^2 = const.
Supuestos: rotacion rigida, sin perdida de masa ni de momento angular. Validez: orden de magnitud.
Tolerancia: 1e-4 entre la integral de volumen y (2/5) M R^2.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
GM_SOL, R_SOL = 1.3271244e20, 6.957e8
M_SOL = GM_SOL / G
P_16 = 609.12 * 3600.0


def v_superficie(R, P, lat_deg=0.0):
    return 2 * math.pi * R * math.cos(math.radians(lat_deg)) / P


def v_critica(M, R):
    return math.sqrt(G * M / R)


def momento_inercia_integral(M, R, n_r=400, n_t=400):
    """I = Int rho (r sin t)^2 dV con rho uniforme."""
    rho = M / (4 / 3 * math.pi * R ** 3)
    dr, dt = R / n_r, math.pi / n_t
    s = 0.0
    for i in range(n_r):
        r = (i + 0.5) * dr
        for j in range(n_t):
            t = (j + 0.5) * dt
            s += rho * (r * math.sin(t)) ** 2 * (2 * math.pi * r * r * math.sin(t)) * dr * dt
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    i_num = momento_inercia_integral(M_SOL, R_SOL)
    i_cer = 0.4 * M_SOL * R_SOL ** 2
    assert abs(i_num / i_cer - 1) < 1e-4, "I por integral != 2/5 M R^2"
    v16 = v_superficie(R_SOL, P_16, 16.0)
    vc = v_critica(M_SOL, R_SOL)
    print(f"I (integral) / (2/5 M R^2) = {i_num / i_cer:.6f}")
    print(f"v a 16 grados de latitud = {v16 / 1e3:.3f} km/s ; v_crit = {vc / 1e3:.1f} km/s ; cociente = {v16 / vc:.4f}")
    omega = 2 * math.pi / P_16
    print(f"J (uniforme, omega a 16 grados) = {i_cer * omega:.3e} kg m2/s (cota: la estructura real difiere)")
    # contraccion hipotetica con J conservado y misma estructura: P ~ R^2
    r0, r1 = 100 * R_SOL, R_SOL
    p_nuevo = P_16 * (r1 / r0) ** 2
    assert abs(p_nuevo / P_16 - 1e-4) < 1e-12
    print(f"contraccion 100 R_sol -> R_sol con J fijo: P_final/P_inicial = {p_nuevo / P_16:.1e}")
    # flujo congelado
    b0, r_ns = 1e-4, 1e4  # 1 G, 10 km
    b1 = b0 * (R_SOL / r_ns) ** 2
    assert abs(b1 * r_ns ** 2 / (b0 * R_SOL ** 2) - 1) < 1e-12
    print(f"flujo congelado: B de 1 G (1e-4 T) a 10 km -> {b1:.2e} T ({b1 * 1e4:.2e} G)")
    # rotacion critica de una enana blanca ilustrativa
    m_wd, r_wd = 0.6 * M_SOL, 0.0127 * R_SOL
    print(f"v_crit enana blanca (0.6 Msol, 0.0127 Rsol) = {v_critica(m_wd, r_wd) / 1e3:.0f} km/s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
