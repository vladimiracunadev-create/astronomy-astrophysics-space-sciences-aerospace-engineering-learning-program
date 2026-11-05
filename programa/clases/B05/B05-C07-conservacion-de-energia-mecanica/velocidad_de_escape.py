#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B05-C07: conservación de la energía mecánica y velocidad de escape.

Datos PUBLICADOS: GM, radio medio y velocidad de escape de la Tierra (NASA NSSDC, Earth Fact
Sheet, act. 15-nov-2024); masa y radio de la Luna y su velocidad de escape (Moon Fact Sheet,
act. 11-ene-2024); G = 6,674 30e-11 (NIST CODATA 2022). Modelo: gravedad puntual, movimiento
radial, sin atmósfera ni rotación; integración con velocity-Verlet. Dominio de validez: un
solo cuerpo atractor. Tolerancias: 0,1 % (Tierra) y 1 % (Luna) frente a NASA; deriva de
energía < 1e-6.
"""
from __future__ import annotations
import math
import sys

G = 6.67430e-11
GM_T = 3.9860e14          # m³/s²
R_T = 6_371_000.0         # radio medio volumétrico, m
M_L, R_L = 0.07346e24, 1_737_400.0
V_ESC_T_NASA, V_ESC_L_NASA = 11_186.0, 2_380.0   # m/s publicados

def v_esc(gm: float, r: float) -> float:
    return math.sqrt(2 * gm / r)

def lanzar_radial(gm: float, r0: float, v0: float, t_fin: float, dt: float):
    """Verlet radial; devuelve (r, v, deriva relativa de energía específica)."""
    r, v = r0, v0
    e0 = 0.5 * v * v - gm / r
    a = -gm / r**2
    for _ in range(int(t_fin / dt)):
        v += 0.5 * a * dt
        r += v * dt
        a = -gm / r**2
        v += 0.5 * a * dt
    e = 0.5 * v * v - gm / r
    return r, v, abs(e - e0) / abs(e0)

def main() -> int:
    ve_t = v_esc(GM_T, R_T)
    ve_l = v_esc(G * M_L, R_L)
    assert abs(ve_t - V_ESC_T_NASA) / V_ESC_T_NASA < 1e-3, ve_t
    assert abs(ve_l - V_ESC_L_NASA) / V_ESC_L_NASA < 1e-2, ve_l
    r, v, deriva = lanzar_radial(GM_T, R_T, 5_000.0, 600.0, 0.01)
    assert deriva < 1e-6, deriva
    r_max = GM_T / (GM_T / R_T - 0.5 * 5_000.0**2)   # de E = v0²/2 - GM/R0 = -GM/r_max
    assert r < r_max
    print(f"python {sys.version.split()[0]} | pruebas OK")
    print(f"v_escape Tierra (R=6371 km) = {ve_t:.1f} m/s (NASA 11 186); Luna = {ve_l:.1f} m/s (NASA 2380)")
    print(f"Lanzamiento vertical a 5000 m/s: r(600 s) = {r:.0f} m, v = {v:.1f} m/s, deriva de energía = {deriva:.1e}")
    print(f"Altura máxima analítica: {(r_max - R_T)/1e3:.0f} km sobre la superficie media")
    print(f"Con g constante (9,80665): h_max = {5_000.0**2 / (2 * 9.80665) / 1e3:.0f} km")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
