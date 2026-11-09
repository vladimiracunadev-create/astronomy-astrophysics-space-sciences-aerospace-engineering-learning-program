#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C25: rodamientos y apoyos de precision: contacto de Hertz, rigidez y reparto de carga entre bolas.

Datos: ILUSTRATIVOS (bola de acero de 6 mm de diametro sobre plano, E = 200 GPa y nu = 0,3 para ambos cuerpos; cargas de 10 a 1000 N; rodamiento radial de Z bolas sin holgura). Valores de orden de magnitud, NO consultados
en una norma de rodamientos ni en una hoja de fabricante.
Modelo (Hertz, esfera sobre plano): a = (3 F R/(4 E*))^(1/3), delta = a^2/R, p_0 = 3 F/(2 pi a^2), 1/E* = 2 (1 - nu^2)/E, rigidez k = dF/d delta = 3 F/(2 delta) (crece como F^(1/3)).
Reparto de carga (Stribeck, contacto puntual, sin holgura): Q(psi) = Q_max cos^(3/2)(psi) en |psi| < 90 grados con F = sum Q(psi) cos(psi); Q_max Z/F tiende a 2 pi/integral(cos^(5/2)) = 4,37 cuando Z crece.
Verificacion independiente: la presion de Hertz p = p_0 sqrt(1 - r^2/a^2) se integra numericamente (Simpson) para recuperar F = (2/3) p_0 pi a^2 y el acercamiento delta = (2/E*) integral de p dr (desplazamiento central de Boussinesq).
Supuestos: materiales elasticos lineales e isotropos, contacto sin friccion, geometria esferica exacta, sin precarga ni holgura ni pista curva. Validez: a << R.
Tolerancia: integrales numericas frente a las formulas cerradas, 1e-5 relativo (la raiz del integrando limita la regla de Simpson); Stribeck con Z = 400, 0,5 % de 4,37.
"""
from __future__ import annotations
import math, platform

E = 200e9; NU = 0.3; R = 3e-3
EST = E / (2 * (1 - NU ** 2))

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def hertz(F):
    a = (3 * F * R / (4 * EST)) ** (1 / 3)
    d = a * a / R
    p0 = 3 * F / (2 * math.pi * a * a)
    return a, d, p0

def stribeck(Z):
    s = 0.0
    for j in range(Z):
        psi = 2 * math.pi * j / Z
        psi = (psi + math.pi) % (2 * math.pi) - math.pi
        if abs(psi) < math.pi / 2:
            s += math.cos(psi) ** 2.5
    return Z / s

def calc():
    r = {}
    filas = []
    for F in (10.0, 100.0, 1000.0):
        a, d, p0 = hertz(F)
        k = 3 * F / (2 * d)
        filas.append((F, a * 1e6, d * 1e6, p0 / 1e9, k / 1e6))
    r["filas"] = filas
    a, d, p0 = hertz(100.0)
    pr = lambda x: p0 * math.sqrt(max(0.0, 1 - (x / a) ** 2))
    F_num = simpson(lambda x: 2 * math.pi * x * pr(x), 0.0, a, 4000)
    d_num = 2 / EST * simpson(pr, 0.0, a, 4000)
    r["F_num_N"] = F_num; r["F_formula_N"] = 2 / 3 * p0 * math.pi * a * a
    r["delta_num_um"] = d_num * 1e6; r["delta_formula_um"] = d * 1e6
    r["razon_rigidez_1000_10"] = (3 * 1000.0 / 2 / hertz(1000.0)[1]) / (3 * 10.0 / 2 / hertz(10.0)[1])
    r["stribeck"] = [(Z, stribeck(Z)) for Z in (6, 8, 12, 20, 400)]
    integral = simpson(lambda p: math.cos(p) ** 2.5, -math.pi / 2, math.pi / 2, 4000)
    r["stribeck_limite"] = 2 * math.pi / integral
    r["Qmax_12_N"] = 1000.0 * stribeck(12) / 12
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("F (N) | a (um) | delta (um) | p0 (GPa) | k (N/um)")
    for F, a, d, p, k in r["filas"]:
        print(f"{F:.0f} | {a:.2f} | {d:.3f} | {p:.3f} | {k:.2f}")
    for k in ("F_num_N", "F_formula_N", "delta_num_um", "delta_formula_um", "razon_rigidez_1000_10", "stribeck_limite", "Qmax_12_N"):
        print(f"{k} = {r[k]:.6g}")
    print("Z | Q_max Z/F")
    for Z, v in r["stribeck"]:
        print(f"{Z} | {v:.4f}")
    assert abs(r["F_num_N"] - 100.0) / 100.0 < 1e-5 and abs(r["F_formula_N"] - 100.0) < 1e-5
    assert abs(r["delta_num_um"] - r["delta_formula_um"]) / r["delta_formula_um"] < 1e-5
    assert abs(r["razon_rigidez_1000_10"] - 100 ** (1 / 3)) < 1e-5
    assert abs(r["stribeck"][-1][1] - 4.37) / 4.37 < 0.005
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
