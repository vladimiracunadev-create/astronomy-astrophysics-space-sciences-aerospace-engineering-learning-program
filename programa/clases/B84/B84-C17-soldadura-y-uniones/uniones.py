#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C17: union atornillada con precarga (factor de carga y margenes) y garganta de una soldadura de filete.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B), Tabla 2.2-3: factor de seguridad ultimo 1,4 (metalico, carga estatica); 1,5 para uniones adhesivas/insertos.
DATOS ILUSTRATIVOS (no consultados): tornillo M6 con area de esfuerzo As = 20,1 mm2 y resistencia ultima 800 MPa (F_u = 16 080 N); longitud agarrada Lg = 12 mm
de aluminio (E = 69 GPa), tornillo de acero E = 200 GPa; par de apriete T = 8,0 N m con factor de tuerca K = 0,20 (dispersion +/- 25 %); coeficiente de friccion
entre placas mu = 0,20; cargas externas: traccion F = 3000 N por tornillo y cortante V = 1500 N por tornillo (limite). Modelo de rigidez: tornillo kb = E_b A_s/L_g;
miembros: area equivalente del cilindro de presion Am = pi/4[(1,5 d + 0,5 Lg)^2 - (1,1 d)^2] y km = E_m Am/L_g (APROXIMACION de ingenieria elegida aqui).
Precarga: F_p = T/(K d). Factor de carga: C = kb/(kb + km). Fuerza en el tornillo: F_b = F_p + C F. Fuerza que separa: F_sep = F_p,min/(1 - C).
Margenes (FS = 1,4 sobre las cargas limite): MS_u = F_u/(FS F_b,max) - 1; MS_sep = F_p,min/(FS (1 - C) F) - 1; MS_slip = mu (F_p,min - (1 - C) F)/(FS V) - 1.
Soldadura de filete: garganta a = 0,707 w; tension en la garganta tau = F/(a L); w = 4 mm, L = 40 mm, resistencia ilustrativa 130 MPa.
Segunda via: identidad F_b - F_c = F con la misma precarga (equilibrio de la union). Tolerancia 1e-9.
"""
from __future__ import annotations
import math, platform

D = 6e-3
AS = 20.1e-6
FU = 800e6 * AS
LG = 12e-3
EB, EM = 200e9, 69e9
T, KN = 8.0, 0.20
MU = 0.20
F_EXT, V_EXT = 3000.0, 1500.0
FS = 1.4


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    kb = EB * AS / LG
    am = math.pi / 4 * ((1.5 * D + 0.5 * LG) ** 2 - (1.1 * D) ** 2)
    km = EM * am / LG
    C = kb / (kb + km)
    print("Union ILUSTRATIVA M6 en aluminio, FS = 1,4 (GEVS, metalico estatico)")
    print(f"kb = {kb / 1e6:.2f} MN/m ; km = {km / 1e6:.2f} MN/m ; factor de carga C = kb/(kb+km) = {C:.4f}")
    fp = T / (KN * D)
    fp_min, fp_max = 0.75 * fp, 1.25 * fp
    print(f"Precarga nominal F_p = T/(K d) = {fp:.1f} N ; con dispersion +/-25 %: [{fp_min:.1f}, {fp_max:.1f}] N ; {fp_max / (AS * 1e6):.1f} MPa de tension maxima por precarga")
    fb_max = fp_max + C * F_EXT
    fc = fp_min - (1 - C) * F_EXT
    print(f"Fuerza maxima en el tornillo F_b = F_p,max + C F = {fb_max:.1f} N ; fuerza de apriete residual F_c = {fc:.1f} N")
    assert abs((fb_max - (fp_max - (1 - C) * F_EXT)) - F_EXT) < 1e-9  # F_b - F_c = F para la misma precarga
    ms_u = FU / (FS * fb_max) - 1
    ms_sep = fp_min / (FS * (1 - C) * F_EXT) - 1
    ms_slip = MU * (fp_min - (1 - C) * F_EXT) / (FS * V_EXT) - 1
    print(f"MS rotura  = {FU:.0f}/({FS} x {fb_max:.1f}) - 1 = {ms_u:.3f}")
    print(f"MS separacion = {fp_min:.1f}/({FS} x (1-C) x {F_EXT:.0f}) - 1 = {ms_sep:.3f}")
    print(f"MS deslizamiento = mu (F_p,min - (1-C) F)/({FS} V) - 1 = {ms_slip:.3f}")
    print(f"Carga de separacion F_sep = F_p,min/(1-C) = {fp_min / (1 - C):.0f} N (carga limite aplicada {F_EXT:.0f} N)")
    print("Efecto de la precarga (traccion aplicada 3000 N):")
    for frac in (0.5, 0.75, 1.0, 1.25):
        f = fp * frac
        print(f"  F_p = {f:7.1f} N -> MS_sep = {f / (FS * (1 - C) * F_EXT) - 1:7.3f}  MS_rotura = {FU / (FS * (f + C * F_EXT)) - 1:7.3f}")
    # Soldadura
    w, L, tau_adm = 4e-3, 40e-3, 130e6
    a = 0.707 * w
    for F in (5000.0, 10000.0, 20000.0):
        tau = F / (a * L)
        print(f"Soldadura de filete w = 4 mm, L = 40 mm: F = {F:7.0f} N -> tau = {tau / 1e6:6.1f} MPa, MS = {tau_adm / (FS * tau) - 1:6.3f}")
    assert 0 < C < 0.5
    assert ms_sep > 0 and ms_u > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
