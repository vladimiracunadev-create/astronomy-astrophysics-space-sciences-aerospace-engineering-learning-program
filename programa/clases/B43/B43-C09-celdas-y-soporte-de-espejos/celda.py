#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C09: celda y soporte: equilibrio de una balanza triangular (whiffletree) y reparto del soporte lateral.

Datos: ILUSTRATIVOS (espejo de 4,0 kg; g = 9,80665 m/s^2 de NIST CODATA 2022, consultada el 2026-11-09; radio del triangulo 60 mm; desplazamiento del pivote 3 mm; zenit de 60 grados).
Modelo: balanza rigida de tres puntos de apoyo Q_i y pivote P: sum F_i = F y sum F_i (Q_i - P) = 0 (3 ecuaciones, 3 incognitas, regla de Cramer). Para un triangulo equilatero de circunradio rho y pivote desplazado e hacia un vertice, F_1 = F/3 + 2 F e/(3 rho).
Soporte lateral: N almohadillas en el semicirculo inferior con fuerzas F_j proporcionales a cos(phi_j) y suma F_j cos(phi_j) = W_lateral, frente a la distribucion continua (2 W/pi) cos(phi).
Supuestos: cuerpo rigido sin friccion, almohadillas que solo empujan, peso aplicado en el centro. Validez: estatica.
Tolerancia: equilibrio de fuerzas y momentos, 1e-12 relativo; formula del desplazamiento del pivote, 1e-12.
"""
from __future__ import annotations
import math, platform

G = 9.80665; M = 4.0

def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

def balanza(Q, P, F):
    A = [[1.0, 1.0, 1.0], [Q[i][0] - P[0] for i in range(3)], [Q[i][1] - P[1] for i in range(3)]]
    b = [F, 0.0, 0.0]
    d = det3(A)
    out = []
    for j in range(3):
        Aj = [row[:] for row in A]
        for i in range(3):
            Aj[i][j] = b[i]
        out.append(det3(Aj) / d)
    return out

def calc():
    r = {}
    F = M * G
    rho = 0.060
    Q = [(rho * math.cos(math.radians(90 + 120 * i)), rho * math.sin(math.radians(90 + 120 * i))) for i in range(3)]
    f0 = balanza(Q, (0.0, 0.0), F)
    r["F_total_N"] = F; r["F_centrado"] = f0
    e = 0.003
    f1 = balanza(Q, (0.0, e), F)  # hacia el vertice 0 (90 grados)
    r["F_desplazado"] = f1
    r["F1_formula"] = F / 3 + 2 * F * e / (3 * rho)
    r["F2_formula"] = F / 3 - F * e / (3 * rho)
    r["residuo_fuerza"] = abs(sum(f1) - F) / F
    mx = sum(f1[i] * (Q[i][0]) for i in range(3)); my = sum(f1[i] * (Q[i][1] - e) for i in range(3))
    r["residuo_momento"] = (abs(mx) + abs(my)) / (F * rho)
    r["desbalance_pct"] = (f1[0] - F / 3) / (F / 3) * 100
    # lateral
    Wl = F * math.sin(math.radians(60))
    r["W_lateral_N"] = Wl
    filas = []
    for N in (3, 5, 7, 9, 13):
        phis = [-math.pi / 2 + math.pi * (j + 0.5) / N for j in range(N)]
        s = sum(math.cos(p) ** 2 for p in phis)
        Fj = [Wl * math.cos(p) / s for p in phis]
        cont = [2 * Wl / N * math.cos(p) for p in phis]
        filas.append((N, max(Fj), max(cont), sum(f * math.cos(p) for f, p in zip(Fj, phis)), sum(f * math.sin(p) for f, p in zip(Fj, phis))))
    r["lateral"] = filas
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("F_total_N =", f"{r['F_total_N']:.6g}")
    print("centrado:", " ".join(f"{x:.6f}" for x in r["F_centrado"]))
    print("desplazado:", " ".join(f"{x:.6f}" for x in r["F_desplazado"]))
    for k in ("F1_formula", "F2_formula", "residuo_fuerza", "residuo_momento", "desbalance_pct", "W_lateral_N"):
        print(f"{k} = {r[k]:.6g}")
    print("N | F max exacta (N) | F max continua (N) | suma F cos (N) | suma F sin (N)")
    for N, a, b, c, d in r["lateral"]:
        print(f"{N} | {a:.4f} | {b:.4f} | {c:.4f} | {d:.2e}")
    assert all(abs(x - r["F_total_N"] / 3) < 1e-12 for x in r["F_centrado"])
    assert abs(r["F_desplazado"][0] - r["F1_formula"]) < 1e-12 and abs(r["F_desplazado"][1] - r["F2_formula"]) < 1e-12
    assert r["residuo_fuerza"] < 1e-12 and r["residuo_momento"] < 1e-12
    for N, a, b, c, d in r["lateral"]:
        assert abs(c - r["W_lateral_N"]) < 1e-9 and abs(d) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
