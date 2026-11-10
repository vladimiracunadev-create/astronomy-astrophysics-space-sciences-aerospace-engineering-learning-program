#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C03: teoria clasica de laminados (CLT) para tres apilados de un CFRP.

DATOS ILUSTRATIVOS (lamina unidireccional de fibra de carbono/epoxi, valores tipicos no consultados):
  E1 = 140 GPa, E2 = 10 GPa, G12 = 5 GPa, nu12 = 0,30, espesor de lamina t = 0,125 mm, rho = 1550 kg/m3.
Modelo: rigidez reducida Q de la lamina en ejes del material; transformacion al angulo theta (Q-barra);
A = sum Qbar_k t_k (matriz de rigidez de membrana, N/m); modulo efectivo en x: Ex = (A11 - A12^2/A22)/h.
Segunda via: para un apilado cuasi-isotropo [0/45/-45/90]s se comprueba A11 = A22 y A66 = (A11 - A12)/2 (isotropia en el plano)
y la regla de mezclas para E1 (E1 = Vf Ef + (1-Vf) Em) con Vf ilustrativo = 0,60, Ef = 230 GPa, Em = 3,5 GPa.
Unidades SI. Tolerancia: invarianza isotropa < 1e-9 relativa.
"""
from __future__ import annotations
import math, platform

E1, E2, G12, NU12 = 140e9, 10e9, 5e9, 0.30
T = 0.125e-3


def Q():
    nu21 = NU12 * E2 / E1
    d = 1 - NU12 * nu21
    return [[E1 / d, NU12 * E2 / d, 0.0], [NU12 * E2 / d, E2 / d, 0.0], [0.0, 0.0, G12]]


def qbar(th_deg):
    q = Q()
    c, s = math.cos(math.radians(th_deg)), math.sin(math.radians(th_deg))
    q11, q12, q22, q66 = q[0][0], q[0][1], q[1][1], q[2][2]
    c2, s2 = c * c, s * s
    Q11 = q11 * c2 * c2 + 2 * (q12 + 2 * q66) * s2 * c2 + q22 * s2 * s2
    Q22 = q11 * s2 * s2 + 2 * (q12 + 2 * q66) * s2 * c2 + q22 * c2 * c2
    Q12 = (q11 + q22 - 4 * q66) * s2 * c2 + q12 * (c2 * c2 + s2 * s2)
    Q66 = (q11 + q22 - 2 * q12 - 2 * q66) * s2 * c2 + q66 * (c2 * c2 + s2 * s2)
    Q16 = (q11 - q12 - 2 * q66) * s * c ** 3 + (q12 - q22 + 2 * q66) * s ** 3 * c
    Q26 = (q11 - q12 - 2 * q66) * s ** 3 * c + (q12 - q22 + 2 * q66) * s * c ** 3
    return [[Q11, Q12, Q16], [Q12, Q22, Q26], [Q16, Q26, Q66]]


def matriz_A(angulos):
    A = [[0.0] * 3 for _ in range(3)]
    for th in angulos:
        qb = qbar(th)
        for i in range(3):
            for j in range(3):
                A[i][j] += qb[i][j] * T
    return A


def modulo_x(A, h):
    """Modulo efectivo en x con cargas solo en x (se invierte A completa)."""
    a = [list(f) for f in A]
    det = (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
           + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
    c11 = (a[1][1] * a[2][2] - a[1][2] * a[2][1]) / det
    return 1.0 / (c11 * h)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Lamina UD ILUSTRATIVA: E1 = 140 GPa, E2 = 10 GPa, G12 = 5 GPa, nu12 = 0,30, t = 0,125 mm")
    apilados = {
        "UD [0]8": [0] * 8,
        "Cruzado [0/90]2s": [0, 90, 0, 90, 90, 0, 90, 0],
        "Cuasi-iso [0/45/-45/90]s": [0, 45, -45, 90, 90, -45, 45, 0],
    }
    print(f"{'apilado':26s} {'A11 [MN/m]':>11s} {'A22 [MN/m]':>11s} {'A12 [MN/m]':>11s} {'A66 [MN/m]':>11s} {'Ex [GPa]':>9s}")
    res = {}
    for nom, ang in apilados.items():
        A = matriz_A(ang)
        h = len(ang) * T
        ex = modulo_x(A, h) / 1e9
        res[nom] = (A, ex)
        print(f"{nom:26s} {A[0][0] / 1e6:11.4f} {A[1][1] / 1e6:11.4f} {A[0][1] / 1e6:11.4f} {A[2][2] / 1e6:11.4f} {ex:9.2f}")
    A = res["Cuasi-iso [0/45/-45/90]s"][0]
    iso1 = abs(A[0][0] - A[1][1]) / A[0][0]
    iso2 = abs(A[2][2] - (A[0][0] - A[0][1]) / 2) / A[2][2]
    print(f"Cuasi-isotropia: |A11-A22|/A11 = {iso1:.1e} ; |A66-(A11-A12)/2|/A66 = {iso2:.1e}")
    h = 8 * T
    Ex_iso = res["Cuasi-iso [0/45/-45/90]s"][1]
    nu_eff = A[0][1] / A[1][1]
    print(f"Cuasi-iso: E efectivo = {Ex_iso:.2f} GPa, nu efectivo = {nu_eff:.3f}, G = E/(2(1+nu)) = {Ex_iso / (2 * (1 + nu_eff)):.2f} GPa, A66 h^-1 = {A[2][2] / h / 1e9:.2f} GPa")
    Vf, Ef, Em = 0.60, 230e9, 3.5e9
    print(f"Regla de mezclas E1 = Vf Ef + (1-Vf) Em = {(Vf * Ef + (1 - Vf) * Em) / 1e9:.1f} GPa (Vf, Ef, Em ILUSTRATIVOS; la lamina usa 140 GPa)")
    rho = 1550.0
    print(f"Rigidez especifica UD = {res['UD [0]8'][1] * 1e9 / rho / 1e6:.1f} MN m/kg ; cuasi-iso = {Ex_iso * 1e9 / rho / 1e6:.1f} MN m/kg")
    assert iso1 < 1e-9 and iso2 < 1e-9
    assert abs(res["UD [0]8"][1] - 140.0) < 1e-6  # un UD cargado en la fibra tiene E1 exacto
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
