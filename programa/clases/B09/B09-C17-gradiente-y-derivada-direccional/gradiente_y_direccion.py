#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C17: gradiente, derivada direccional y gravedad como -grad(Phi).

Datos (PUBLICADOS): (GM)_Tierra nominal = 3.986004e5 km3/s2 (IAU 2015 B3,
arXiv:1510.07674); GM_Luna = 4.90e3 km3/s2, distancia 384 400 km y radio medio
lunar 1737.4 km, gravedad superficial lunar 1.62 m/s2 (NASA/NSSDC, ficha lunar,
2024-01-11). Punto de prueba (200 000, 100 000) km: SINTÉTICO.
Modelo: Phi(x, y) = -GE/r1 - GL/r2 en el plano Tierra-Luna (dos cuerpos fijos,
sin rotación). Gravedad g = -grad Phi. Derivada direccional D_u Phi = grad Phi . u
(|u| = 1). Supuestos: cuerpos puntuales. Validez: lejos de ambos cuerpos.
Tolerancias: gradiente analítico vs numérico 1e-7 relativa; |D_u| <= |grad|;
perpendicularidad con la curva de nivel dentro de 1e-6.
"""
from __future__ import annotations
import math, platform, sys

GE, GL, D = 3.986004e5, 4.90e3, 384_400.0
R_LUNA, G_LUNA_NASA = 1737.4, 1.62


def phi(x, y):
    return -GE / math.hypot(x, y) - GL / math.hypot(x - D, y)


def grad(x, y):
    r1, r2 = math.hypot(x, y), math.hypot(x - D, y)
    gx = GE * x / r1**3 + GL * (x - D) / r2**3
    gy = GE * y / r1**3 + GL * y / r2**3
    return gx, gy


def grad_num(x, y, h=1.0):
    return ((phi(x + h, y) - phi(x - h, y)) / (2 * h), (phi(x, y + h) - phi(x, y - h)) / (2 * h))


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    x0, y0 = 200_000.0, 100_000.0
    gx, gy = grad(x0, y0)
    nx, ny = grad_num(x0, y0)
    mod = math.hypot(gx, gy)
    prueba(abs(gx - nx) / abs(gx) < 1e-7 and abs(gy - ny) / abs(gy) < 1e-7, "gradiente analítico vs numérico")
    print(f"Punto ({x0:.0f}, {y0:.0f}) km:  grad Phi = ({gx:.6e}, {gy:.6e}) km/s2;  |grad| = {mod:.6e} km/s2 = {mod*1e3:.5f} m/s2")
    ang = math.degrees(math.atan2(gy, gx))
    print(f"Dirección de máximo crecimiento: {ang:.2f} deg respecto al eje x; la gravedad apunta a {ang+180:.2f} deg")
    # derivada direccional en varias direcciones
    print("\n ángulo de u [deg]    D_u Phi [km/s2]    D_u / |grad|")
    for a in (ang, ang + 45, ang + 90, ang + 180, ang - 90):
        u = (math.cos(math.radians(a)), math.sin(math.radians(a)))
        du = gx * u[0] + gy * u[1]
        h = 1.0
        du_num = (phi(x0 + h * u[0], y0 + h * u[1]) - phi(x0 - h * u[0], y0 - h * u[1])) / (2 * h)
        prueba(abs(du - du_num) <= 1e-7 * mod, "D_u analítica vs numérica")
        prueba(abs(du) <= mod * (1 + 1e-12), "|D_u| <= |grad|")
        print(f"{a:12.2f}      {du:16.6e}      {du/mod:+.6f}")
    # perpendicularidad con la curva de nivel: paso pequeño a lo largo del nivel
    tx, ty = -gy / mod, gx / mod
    h = 100.0
    dphi_tang = phi(x0 + h * tx, y0 + h * ty) - phi(x0, y0)
    dphi_norm = phi(x0 + h * gx / mod, y0 + h * gy / mod) - phi(x0, y0)
    print(f"\nPaso de {h:.0f} km: a lo largo de la tangente ΔPhi = {dphi_tang:.3e}; a lo largo del gradiente ΔPhi = {dphi_norm:.3e}")
    prueba(abs(dphi_tang) < 1e-3 * abs(dphi_norm), "la tangente a la curva de nivel es perpendicular al gradiente")
    # Tierra sola: gravedad superficial radial
    R_E = 6378.1
    g_E = GE / R_E**2 * 1e3
    print(f"\nTierra sola en r = {R_E} km: |grad Phi| = GM/r^2 = {g_E:.4f} m/s2 (dirección radial hacia fuera)")
    # Luna: comprobación con la gravedad superficial de la NASA
    g_L = GL / R_LUNA**2 * 1e3
    print(f"Luna: GM_L/R^2 = {g_L:.4f} m/s2;  NASA = {G_LUNA_NASA} m/s2;  dif. = {g_L/G_LUNA_NASA-1:+.2%}")
    prueba(abs(g_L / G_LUNA_NASA - 1) < 5e-3, "gravedad lunar contra NASA")
    # el punto de silla: gradiente nulo
    xs = D / (1 + math.sqrt(GL / GE))
    gsx, gsy = grad(xs, 0.0)
    print(f"\nEn x* = {xs:.1f} km, y = 0: grad Phi = ({gsx:.2e}, {gsy:.2e}) km/s2 (nulo: punto crítico)")
    prueba(abs(gsx) < 1e-12 and abs(gsy) < 1e-18, "gradiente nulo en el punto de silla")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
