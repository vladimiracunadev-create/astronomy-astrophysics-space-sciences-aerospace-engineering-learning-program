#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C05: medidas de espin 1/2 en ejes distintos, suma de dos espines y desdoblamiento Zeeman.

Datos: magneton de Bohr (9.2740100657e-24 J/T, 5.7883817982e-5 eV/T, 1.39962449171e10 Hz/T), factor g del electron (-2.00231930436) y e, h (NIST CODATA 2022), consultados 2026-11-09. El campo
(1 T), los angulos de los analizadores (60 deg) y el numero de ensayos (100 000, semilla fija) son ILUSTRATIVOS (sinteticos).
Modelo: analizador de Stern-Gerlach a un angulo theta del estado preparado: P(+) = cos^2(theta/2) (comprobado con Monte Carlo y con la secuencia de dos analizadores); espin total de dos
espines 1/2 como matriz 4x4 (producto de Kronecker): S^2 aplicado al triplete y al singlete da s(s + 1) = 2 y 0 (hbar = 1); degeneracion 2l + 1 y autovalores l(l + 1) de L^2; desdoblamiento
Zeeman Delta E = g mu_B B para un electron.
Supuestos: analizadores ideales, campo uniforme. Validez: exacta para el modelo.
Tolerancia: frecuencias empiricas dentro de 4 errores estandar; S^2 a 1e-12; Zeeman en Hz frente al valor de NIST a 1e-4 (g = 2.0023).
"""
from __future__ import annotations
import math
import platform
import random
import sys

MU_B, MU_B_EV, MU_B_HZ = 9.2740100657e-24, 5.7883817982e-5, 1.39962449171e10
G_E = 2.00231930436
H, E = 6.62607015e-34, 1.602176634e-19


def kron(a, b):
    return [[a[i // 2][j // 2] * b[i % 2][j % 2] for j in range(4)] for i in range(4)]


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(4)) for i in range(4)]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    n = 100000
    print(f"{'theta [deg]':>11} {'P(+) = cos^2(theta/2)':>22} {'frecuencia':>11} {'desviacion [errores]':>21}")
    for th in (0, 30, 60, 90, 150):
        p = math.cos(math.radians(th) / 2) ** 2
        k = sum(1 for _ in range(n) if rng.random() < p)
        err = math.sqrt(max(p * (1 - p), 1e-12) / n)
        print(f"{th:11d} {p:22.5f} {k / n:11.5f} {abs(k / n - p) / err:21.2f}")
        assert abs(k / n - p) < 4 * err + 1e-12
    # secuencia z (+) -> x (+) -> z: P(z+ al final) = 1/4 + 1/4 ?  P(x+|z+) = 1/2 ; P(z+|x+) = 1/2 -> 1/4 de los atomos
    k = 0
    for _ in range(n):
        if rng.random() < 0.5 and rng.random() < 0.5:
            k += 1
    print(f"secuencia z+ -> x+ -> z+: frecuencia = {k / n:.5f} ; teoria 0.25000 (sin el analizador x seria 1)")
    assert abs(k / n - 0.25) < 4 * math.sqrt(0.25 * 0.75 / n)
    # dos espines
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]
    ident = [[1, 0], [0, 1]]
    total = []
    for p in (sx, sy, sz):
        a, b = kron(p, ident), kron(ident, p)
        total.append([[0.5 * (a[i][j] + b[i][j]) for j in range(4)] for i in range(4)])    # S_k = (sigma_k x 1 + 1 x sigma_k)/2
    def s2(v):
        out = [0j] * 4
        for m in total:
            w = mv(m, mv(m, v))
            out = [out[i] + w[i] for i in range(4)]
        return out
    r2 = 1 / math.sqrt(2)
    estados = {
        "triplete m = +1 (arriba, arriba)": [1, 0, 0, 0],
        "triplete m = 0": [0, r2, r2, 0],
        "triplete m = -1": [0, 0, 0, 1],
        "singlete": [0, r2, -r2, 0],
    }
    for nombre, v in estados.items():
        w = s2([complex(x) for x in v])
        val = sum(w[i].real * v[i] for i in range(4))
        s = 1 if abs(val - 2) < 1e-9 else 0 if abs(val) < 1e-9 else None
        print(f"{nombre:<34} <S^2> = {val:.6f} -> s = {s}")
        assert s is not None and all(abs(w[i] - val * v[i]) < 1e-12 for i in range(4))
    # momento angular orbital
    print(f"{'l':>2} {'l(l + 1)':>9} {'degeneracion 2l + 1':>20} {'valores de m':>26}")
    for l in range(4):
        print(f"{l:2d} {l * (l + 1):9d} {2 * l + 1:20d} {str(list(range(-l, l + 1))):>26}")
    # Zeeman
    b = 1.0
    de = G_E * MU_B * b
    print(f"desdoblamiento Zeeman del electron en {b} T: {de:.4e} J = {G_E * MU_B_EV * b * 1e3:.5f} meV ; frecuencia = {G_E * MU_B_HZ * b / 1e9:.4f} GHz")
    assert abs(de / H / (G_E * MU_B_HZ * b) - 1) < 1e-4
    assert abs(MU_B_EV * E / MU_B - 1) < 1e-4
    print(f"cociente 2 mu_B B / h con g = 2: {2 * MU_B * b / H / 1e9:.4f} GHz (g = 2.0023: {de / H / 1e9:.4f} GHz)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
