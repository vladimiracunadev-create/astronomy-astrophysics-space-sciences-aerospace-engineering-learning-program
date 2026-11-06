#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C18: intercomparacion de instrumentos.

Datos: SINTETICOS. Tres radiometros miden la misma irradiancia (verdadera
1361.0 W/m2) con incertidumbres tipicas declaradas u1 = 0.60, u2 = 0.80,
u3 = 0.50 W/m2. Resultados de ejemplo: 1361.4, 1360.1, 1362.9 W/m2.
Modelo: la diferencia de dos medidas independientes tiene varianza
u1^2 + u2^2 (GUM 5.1.2 con c = +1, -1); diferencia normalizada
z = |x1 - x2| / sqrt(u1^2 + u2^2); compatibles si z <= 2 (cobertura ~95 %).
Media ponderada: xw = sum(x_i/u_i^2)/sum(1/u_i^2), u(xw) = 1/sqrt(sum 1/u_i^2).
Razon de Birge: RB = sqrt(chi2/(N-1)), chi2 = sum((x_i - xw)^2/u_i^2); RB >> 1
indica incertidumbres subestimadas o un sesgo.
Supuestos: independencia, normalidad. Tolerancia: bajo hipotesis nula la
fraccion de |z| > 1 y > 2 coincide con 31.73 % y 4.55 % dentro de 5 errores
binomiales (R = 100000).
"""
from __future__ import annotations
import math
import platform
import random
import sys

U = [0.60, 0.80, 0.50]
X = [1361.4, 1360.1, 1362.9]


def z(x1, u1, x2, u2):
    return abs(x1 - x2) / math.hypot(u1, u2)


def ponderada(x, u):
    w = [1 / (v * v) for v in u]
    xw = sum(a * b for a, b in zip(x, w)) / sum(w)
    return xw, 1 / math.sqrt(sum(w))


def birge(x, u):
    xw, _ = ponderada(x, u)
    chi2 = sum(((a - xw) / b) ** 2 for a, b in zip(x, u))
    return chi2, math.sqrt(chi2 / (len(x) - 1))


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    pares = [(0, 1), (0, 2), (1, 2)]
    for i, j in pares:
        print(f"z({i+1},{j+1}) = {z(X[i], U[i], X[j], U[j]):.3f}")
    xw, uw = ponderada(X, U)
    chi2, rb = birge(X, U)
    print(f"media ponderada = {xw:.3f} +/- {uw:.3f} W/m2 ; chi2 = {chi2:.3f} ; razon de Birge = {rb:.3f}")
    # Pruebas exactas
    assert abs(ponderada([10.0, 10.0], [1.0, 1.0])[1] - 1 / math.sqrt(2)) < 1e-15
    assert abs(ponderada([10.0, 20.0], [1.0, 1.0])[0] - 15.0) < 1e-15
    assert abs(z(0.0, 3.0, 5.0, 4.0) - 1.0) < 1e-15            # 5 / sqrt(9+16)
    # Hipotesis nula: dos instrumentos con las incertidumbres declaradas
    rng = random.Random(18)
    R = 100000
    z1 = z2 = 0
    for _ in range(R):
        a = 1361.0 + rng.gauss(0, U[0])
        b = 1361.0 + rng.gauss(0, U[1])
        zz = z(a, U[0], b, U[1])
        z1 += zz > 1
        z2 += zz > 2
    f1, f2 = z1 / R, z2 / R
    print(f"nula: P(z>1) = {f1:.4f} (teorica 0.3173) ; P(z>2) = {f2:.4f} (teorica 0.0455)")
    assert abs(f1 - 0.3173) < 5 * math.sqrt(0.3173 * 0.6827 / R)
    assert abs(f2 - 0.0455) < 5 * math.sqrt(0.0455 * 0.9545 / R)
    # Sesgo no declarado: el instrumento 2 tiene +2.0 W/m2 de sesgo oculto
    sesgado = [1361.4, 1360.1 + 2.0, 1362.9]
    print(f"con sesgo oculto de +2.0 en el instrumento 2: z(1,2) = {z(sesgado[0], U[0], sesgado[1], U[1]):.3f}")
    # Razon de Birge bajo la hipotesis nula: media de RB^2 ~ 1 (chi2 con N-1 gl)
    s = 0.0
    M = 20000
    for _ in range(M):
        xs = [1361.0 + rng.gauss(0, u) for u in U]
        s += birge(xs, U)[0]
    print(f"media de chi2 bajo la nula = {s/M:.3f} (teorica N-1 = 2)")
    assert abs(s / M - 2.0) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
