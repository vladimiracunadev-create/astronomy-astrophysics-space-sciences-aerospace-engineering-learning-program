#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C13: temperatura, energía térmica y equilibrio radiativo.

Datos PUBLICADOS: k_B = 1,380 649e-23 J/K y N_A = 6,022 140 76e23 /mol (exactos, SI/CODATA 2022);
R = 8,314 462 618... J/(mol K); sigma = 5,670 374 419...e-8 W/(m² K⁴) (CODATA 2022); Sol:
luminosidad 382,8e24 W, radio medio 695 700 km, temperatura efectiva 5772 K (NASA NSSDC, Sun
Fact Sheet, act. 9-may-2024); Tierra: semieje mayor 149,598e6 km, temperatura media 288 K
(NASA NSSDC, Earth Fact Sheet). SUPUESTO sin fuente consultada: masa molar 0,028 kg/mol (N2).
Modelo: cuerpos negros esféricos en equilibrio radiativo, absorción total (albedo 0) y
emisión uniforme. Dominio de validez: ilustrativo; no incluye albedo, atmósfera ni invernadero.
Tolerancias: 0,1 % en T_efectiva del Sol frente a NASA; 1e-9 en R = N_A k.
"""
from __future__ import annotations
import math
import sys

KB = 1.380649e-23
NA = 6.02214076e23
R_GAS = 8.314462618
SIGMA = 5.670374419e-8
L_SOL = 382.8e24
R_SOL = 695_700e3
T_EFF_SOL_NASA = 5772.0
A_TIERRA = 149.598e9
T_TIERRA_NASA = 288.0
M_N2 = 0.028

def main() -> int:
    assert abs(NA * KB - R_GAS) / R_GAS < 1e-9
    t_sol = (L_SOL / (4 * math.pi * R_SOL**2 * SIGMA)) ** 0.25
    assert abs(t_sol - T_EFF_SOL_NASA) / T_EFF_SOL_NASA < 1e-3, t_sol
    s = L_SOL / (4 * math.pi * A_TIERRA**2)
    t_eq = (s / (4 * SIGMA)) ** 0.25
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"N_A * k_B = {NA*KB:.9f} J/(mol K) (R = {R_GAS})")
    print(f"T efectiva del Sol calculada = {t_sol:.1f} K (NASA {T_EFF_SOL_NASA:.0f} K)")
    print(f"Flujo solar a 1 au (de L y distancia) = {s:.1f} W/m²")
    print(f"Temperatura de equilibrio de una esfera negra a 1 au = {t_eq:.1f} K = {t_eq-273.15:.1f} °C (media terrestre NASA: {T_TIERRA_NASA:.0f} K)")
    for T in (233.15, 288.0, 373.15):
        e = 1.5 * KB * T
        v = math.sqrt(3 * R_GAS * T / M_N2)
        print(f"  T = {T:6.2f} K: energía cinética de traslación media = {e:.3e} J ({e/1.602176634e-19*1000:.2f} meV); v_rms(N2, supuesto) = {v:.1f} m/s")
    # energía para calentar 100 kg de un material con c sintética 900 J/(kg K) de 250 K a 350 K
    q = 100.0 * 900.0 * (350.0 - 250.0)
    print(f"Energía para calentar 100 kg (c = 900 J/(kg K), sintética) de 250 K a 350 K: {q:.3e} J")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
