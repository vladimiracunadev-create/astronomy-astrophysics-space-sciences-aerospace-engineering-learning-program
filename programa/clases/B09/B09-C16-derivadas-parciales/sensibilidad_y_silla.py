#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C16: derivadas parciales, propagación de incertidumbre y silla.

Datos (PUBLICADOS): R_sol = 6.957e8 m, T_eff = 5772 K (IAU 2015 B3,
arXiv:1510.07674; nominales); sigma = 5.670374419e-8 W m-2 K-4 (CODATA 2022);
(GM)_Tierra = 3.986004e5 km3/s2 (IAU), GM_Luna = 4.90e3 km3/s2 y d = 384 400 km
(NASA/NSSDC). Incertidumbres relativas 1 % en R y 0.5 % en T: SINTÉTICAS.
Muestras de Monte Carlo: SIMULADAS (random.Random(7), N = 200 000).
Modelo: L(R, T) = 4 pi R^2 sigma T^4. dL/L = 2 dR/R + 4 dT/T (diferencial);
para errores independientes (propagación lineal) sigma_L/L = sqrt((2 sR)^2 + (4 sT)^2).
Hessiano de Phi(x, y) = -GE/r1 - GL/r2 en x* para clasificar el punto crítico.
Supuestos: errores gaussianos independientes pequeños. Validez: cociente de
incertidumbre << 1. Tolerancias: derivadas parciales a 1e-6 relativa; MC a 3 sigma
estadísticas; Laplace: Phi_xx + 2 Phi_yy = 0 a 1e-9 relativa.
"""
from __future__ import annotations
import math, platform, random, sys

SIGMA = 5.670374419e-8
R0, T0 = 6.957e8, 5772.0
SR, ST = 0.01, 0.005
GE, GL, D = 3.986004e5, 4.90e3, 384_400.0


def L(R, T):
    return 4 * math.pi * R * R * SIGMA * T**4


def phi(x, y):
    return -GE / math.hypot(x, y) - GL / math.hypot(x - D, y)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    L0 = L(R0, T0)
    # parciales: analíticas vs cociente central
    hR, hT = 1e-5 * R0, 1e-5 * T0
    dLdR = (L(R0 + hR, T0) - L(R0 - hR, T0)) / (2 * hR)
    dLdT = (L(R0, T0 + hT) - L(R0, T0 - hT)) / (2 * hT)
    print(f"L0 = {L0:.5e} W")
    print(f"dL/dR : analítica 2L/R = {2*L0/R0:.6e} W/m ; numérica {dLdR:.6e}")
    print(f"dL/dT : analítica 4L/T = {4*L0/T0:.6e} W/K ; numérica {dLdT:.6e}")
    prueba(abs(dLdR / (2 * L0 / R0) - 1) < 1e-6 and abs(dLdT / (4 * L0 / T0) - 1) < 1e-6, "parciales")
    # derivadas mixtas iguales
    h1, h2 = 1e-3 * R0, 1e-3 * T0
    mixta1 = (L(R0 + h1, T0 + h2) - L(R0 + h1, T0 - h2) - L(R0 - h1, T0 + h2) + L(R0 - h1, T0 - h2)) / (4 * h1 * h2)
    esp = 8 * L0 / (R0 * T0)
    print(f"d2L/dRdT : numérica {mixta1:.6e} ; analítica 8L/(RT) = {esp:.6e}")
    prueba(abs(mixta1 / esp - 1) < 1e-5, "derivada mixta")
    # propagación lineal y Monte Carlo
    s_lin = math.sqrt((2 * SR) ** 2 + (4 * ST) ** 2)
    rng = random.Random(7)
    N = 200_000
    vals = [L(R0 * (1 + rng.gauss(0, SR)), T0 * (1 + rng.gauss(0, ST))) / L0 for _ in range(N)]
    m = sum(vals) / N
    sd = math.sqrt(sum((v - m) ** 2 for v in vals) / (N - 1))
    print(f"\nIncertidumbre relativa de L (R: {SR:.1%}, T: {ST:.1%}, sintéticas)")
    print(f"  propagación lineal: {s_lin:.4%};  Monte Carlo (simulado): {sd:.4%};  media MC = {m:.5f}")
    prueba(abs(sd / s_lin - 1) < 0.02, "MC ~ propagación lineal")
    # contribuciones
    print(f"  contribución de R: {(2*SR)**2/s_lin**2:.1%} de la varianza; de T: {(4*ST)**2/s_lin**2:.1%}")
    # Hessiano en el punto de atracción igual
    xs = D / (1 + math.sqrt(GL / GE))
    pxx = -2 * GE / xs**3 - 2 * GL / (D - xs) ** 3
    pyy = GE / xs**3 + GL / (D - xs) ** 3
    h = 10.0
    pxx_n = (phi(xs + h, 0) - 2 * phi(xs, 0) + phi(xs - h, 0)) / h**2
    pyy_n = (phi(xs, h) - 2 * phi(xs, 0) + phi(xs, -h)) / h**2
    pxy_n = (phi(xs + h, h) - phi(xs + h, -h) - phi(xs - h, h) + phi(xs - h, -h)) / (4 * h * h)
    print(f"\nHessiano de Phi en x* = {xs:.1f} km (unidad s^-2):")
    print(f"  Phi_xx = {pxx:.4e} (numérica {pxx_n:.4e});  Phi_yy = {pyy:.4e} (numérica {pyy_n:.4e});  Phi_xy ≈ {pxy_n:.1e}")
    disc = pxx * pyy - 0.0
    prueba(abs(pxx_n / pxx - 1) < 1e-4 and abs(pyy_n / pyy - 1) < 1e-4, "Hessiano")
    prueba(abs(pxy_n) < 1e-14, "Phi_xy = 0 sobre el eje")
    prueba(disc < 0, "discriminante negativo -> silla")
    prueba(abs(pxx + 2 * pyy) < 1e-9 * abs(pxx), "Laplace: Phi_xx + Phi_yy + Phi_zz = 0")
    print(f"  discriminante Phi_xx*Phi_yy - Phi_xy^2 = {disc:.3e} < 0 -> punto de silla")
    print(f"  Phi_xx + 2 Phi_yy = {pxx + 2*pyy:.3e} (Laplace en 3D)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
