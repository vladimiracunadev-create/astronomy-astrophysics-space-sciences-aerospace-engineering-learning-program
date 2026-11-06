#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C18: integrales dobles y triples; masa y momento de inercia.

Datos (PUBLICADOS, NASA/NSSDC, Earth Fact Sheet, actualizada 2024-11-15):
masa 5.9722e24 kg, radio medio volumétrico 6371.000 km, densidad media
5513 kg/m3, momento de inercia polar I/(M R^2) = 0.3308. IAU 2015 B3
(arXiv:1510.07674): S_sol nominal = 1361 W/m2 y R_eE nominal = 6.3781e6 m.
Núcleo de radio 3500 km: SINTÉTICO (hipótesis de partida).
Modelo A (triple integral esférica): M = int rho r^2 sin(theta) dr dtheta dphi;
I_z = int rho (r sin theta)^2 dV; para rho(r) con simetría esférica:
M = 4 pi int rho r^2 dr ; I = (8 pi / 3) int rho r^4 dr.
Con dos capas (núcleo rho_c, manto rho_m) se resuelven rho_c y rho_m para
reproducir M y I/(M R^2) (ajuste ESTIMADO, no un modelo sísmico).
Modelo B (integral doble): potencia solar interceptada por una esfera,
P = S int_0^{pi/2} int_0^{2 pi} cos(theta) R^2 sin(theta) dphi dtheta = S pi R^2.
Supuestos: simetría esférica; S uniforme. Validez: ilustrativa.
Tolerancias: integrales numéricas (Simpson 2D n = 400) a 1e-8 relativa.
"""
from __future__ import annotations
import math, platform, sys

M_T, R_T, RHO_NASA, K_NASA = 5.9722e24, 6.371e6, 5513.0, 0.3308
S_SOL, R_EQ = 1361.0, 6.3781e6
R_NUCLEO = 3.5e6


def simpson(f, a, b, n=400):
    h = (b - a) / n
    s = f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    return s * h / 3


def simpson2(f, a, b, c, d, n=400):
    return simpson(lambda x: simpson(lambda y: f(x, y), c, d, n), a, b, n)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # 1) esfera uniforme: integral triple en coordenadas esféricas
    rho = 1.0
    R = 1.0
    V_num = simpson(lambda r: simpson(lambda th: 2 * math.pi * r * r * math.sin(th), 0, math.pi, 200), 0, R, 200)
    prueba(abs(V_num - 4 * math.pi / 3) < 1e-8, "volumen de la esfera unitaria")
    I_num = simpson(lambda r: simpson(lambda th: 2 * math.pi * (r * math.sin(th)) ** 2 * r * r * math.sin(th), 0, math.pi, 200), 0, R, 200)
    prueba(abs(I_num - 8 * math.pi / 15) < 1e-8, "I de la esfera uniforme = 2/5 M R^2")
    print(f"Esfera uniforme: V = {V_num:.8f} (4pi/3 = {4*math.pi/3:.8f});  I/(M R^2) = {I_num/V_num:.6f} (esperado 0.4)")
    # 2) densidad media de la Tierra
    V_T = 4 * math.pi * R_T**3 / 3
    print(f"\nDensidad media = M/V = {M_T/V_T:.1f} kg/m3 (NASA: {RHO_NASA:.0f}); dif. = {M_T/V_T/RHO_NASA-1:+.2e}")
    prueba(abs(M_T / V_T / RHO_NASA - 1) < 1e-3, "densidad media contra NASA")
    # 3) dos capas: resolver rho_c y rho_m para M e I
    rc, R = R_NUCLEO, R_T
    a11, a12 = 4 * math.pi / 3 * rc**3, 4 * math.pi / 3 * (R**3 - rc**3)
    a21, a22 = 8 * math.pi / 15 * rc**5, 8 * math.pi / 15 * (R**5 - rc**5)
    b1, b2 = M_T, K_NASA * M_T * R**2
    det = a11 * a22 - a12 * a21
    rho_c = (b1 * a22 - a12 * b2) / det
    rho_m = (a11 * b2 - a21 * b1) / det
    print(f"\nModelo de dos capas (núcleo {rc/1e3:.0f} km, SINTÉTICO) ajustado a M e I/(M R^2) = {K_NASA}:")
    print(f"  rho_núcleo = {rho_c:.0f} kg/m3;  rho_manto = {rho_m:.0f} kg/m3  (ESTIMADAS por ajuste)")
    prueba(rho_c > rho_m > 0, "núcleo más denso que el manto")
    # verificación por integración numérica de la densidad por capas
    rho_f = lambda r: rho_c if r < rc else rho_m
    Mi = 4 * math.pi * (simpson(lambda r: rho_c * r * r, 0, rc, 2000) + simpson(lambda r: rho_m * r * r, rc, R, 2000))
    Ii = 8 * math.pi / 3 * (simpson(lambda r: rho_c * r**4, 0, rc, 2000) + simpson(lambda r: rho_m * r**4, rc, R, 2000))
    print(f"  M integrada = {Mi:.5e} kg (NASA {M_T:.4e});  I/(M R^2) integrada = {Ii/(Mi*R**2):.5f} (NASA {K_NASA})")
    prueba(abs(Mi / M_T - 1) < 1e-9 and abs(Ii / (Mi * R**2) - K_NASA) < 1e-9, "ajuste reproduce M e I")
    masa_nucleo = 4 * math.pi / 3 * rc**3 * rho_c
    print(f"  fracción de masa en el núcleo = {masa_nucleo/M_T:.1%}; fracción del volumen = {(rc/R)**3:.1%}")
    # 4) integral doble: potencia interceptada
    P_num = simpson2(lambda th, ph: S_SOL * math.cos(th) * R_EQ**2 * math.sin(th), 0, math.pi / 2, 0, 2 * math.pi, 200)
    P_ana = S_SOL * math.pi * R_EQ**2
    prueba(abs(P_num / P_ana - 1) < 1e-8, "potencia interceptada")
    print(f"\nPotencia solar interceptada (S nominal, R ecuatorial nominal): numérica {P_num:.5e} W; S*pi*R^2 = {P_ana:.5e} W")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
