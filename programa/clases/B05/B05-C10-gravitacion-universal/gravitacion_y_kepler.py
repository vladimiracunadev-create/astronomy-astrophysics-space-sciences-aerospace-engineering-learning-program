#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C10: ley de gravitación, g(r), y la prueba de la Luna.

Datos PUBLICADOS: G = 6,674 30e-11 m³ kg⁻¹ s⁻² (NIST CODATA 2022); masa de la Tierra
5,9722e24 kg, GM, radio ecuatorial y gravedad media 9,820 m/s² (NASA NSSDC, Earth Fact
Sheet, act. 15-nov-2024); semieje mayor lunar 384 400 km, período sidéreo 27,3217 d
y velocidad orbital 1,022 km/s (NASA NSSDC, Moon Fact Sheet, act. 11-ene-2024).
Modelo: gravedad newtoniana con masas puntuales; órbita lunar circular de radio igual al
semieje mayor. Supuestos: despreciar el Sol y la excentricidad (0,0549). Dominio de
validez: velocidades << c. Tolerancias: 1 % en el período lunar; 0,5 % en G*M frente a GM.
"""
from __future__ import annotations
import math
import sys

G = 6.67430e-11
M_T = 5.9722e24
GM_T = 3.9860e14
R_EQ = 6_378_137.0
G_MEDIA = 9.820
A_LUNA = 3.844e8
T_LUNA_NASA_D = 27.3217
V_LUNA_NASA = 1022.0

def g_en(r: float) -> float:
    return GM_T / r**2

def periodo_circular(r: float, gm: float = GM_T) -> float:
    return 2 * math.pi * math.sqrt(r**3 / gm)

def main() -> int:
    assert abs(G * M_T - GM_T) / GM_T < 5e-3          # coherencia G*M con GM de NASA
    t_luna = periodo_circular(A_LUNA) / 86400.0
    assert abs(t_luna - T_LUNA_NASA_D) / T_LUNA_NASA_D < 1e-2, t_luna
    v_luna = 2 * math.pi * A_LUNA / (T_LUNA_NASA_D * 86400.0)
    assert abs(v_luna - V_LUNA_NASA) / V_LUNA_NASA < 5e-2, v_luna
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"G*M_T = {G*M_T:.5e} m³/s² (NASA GM {GM_T:.4e}); diferencia relativa {abs(G*M_T-GM_T)/GM_T:.1e}")
    print(f"g en el radio ecuatorial = {g_en(R_EQ):.4f} m/s²; media NASA {G_MEDIA} m/s²; g_n = 9.80665")
    for h in (0.0, 400e3, 35_786e3):
        r = R_EQ + h
        print(f"  g(h = {h/1e3:7.0f} km) = {g_en(r):.4f} m/s² ({g_en(r)/9.80665:.3f} g_n)")
    a_luna = GM_T / A_LUNA**2
    print(f"Aceleración de la Luna hacia la Tierra: {a_luna:.4e} m/s²; cociente g(R)/a = {g_en(R_EQ)/a_luna:.1f}; (A_LUNA/R_EQ)² = {(A_LUNA/R_EQ)**2:.1f}")
    print(f"Período lunar por Kepler: {t_luna:.3f} d (NASA sidéreo {T_LUNA_NASA_D} d); v = {v_luna:.1f} m/s (NASA 1022)")
    # tercera ley: T²/a³ constante para tres radios
    for r in (R_EQ + 400e3, 4.2164e7, A_LUNA):
        print(f"  r = {r:12.4e} m: T²/r³ = {periodo_circular(r)**2/r**3:.6e} s²/m³ (4 pi^2/GM = {4*math.pi**2/GM_T:.6e})")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
