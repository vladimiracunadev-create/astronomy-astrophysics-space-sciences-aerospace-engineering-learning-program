#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C01: espacio muestral de tres computadores redundantes.

Datos: SINTETICOS; probabilidad de que cada computador funcione durante la
mision p = 0.9 (valor ILUSTRATIVO, no de una mision real).
Modelo: tres computadores independientes; cada uno 'F' (funciona) o 'X' (falla);
espacio muestral de 2**3 = 8 resultados. Evento A = 'al menos 2 funcionan'.
Supuestos: independencia (fallos de causa comun excluidos), p identica.
Validez: solo el modelo didactico; no es un analisis de fiabilidad real.
Tolerancia: la frecuencia simulada difiere de la exacta menos de 5e-4
(N = 1 000 000, semilla fija); las pruebas exactas usan aritmetica de
fracciones. Las pruebas detienen la ejecucion si fallan.
"""
import itertools
import platform
from fractions import Fraction

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")

p = Fraction(9, 10)
resultados = list(itertools.product("FX", repeat=3))
prob = {w: p ** w.count("F") * (1 - p) ** w.count("X") for w in resultados}
print(f"tamano del espacio muestral: {len(resultados)}")
assert len(resultados) == 8
assert sum(prob.values()) == 1  # axioma: P(Omega) = 1

A = {w for w in resultados if w.count("F") >= 2}
PA = sum(prob[w] for w in A)
print(f"P(A) = {PA} = {float(PA):.6f}")
assert PA == 3 * p**2 * (1 - p) + p**3  # solucion analitica independiente
assert PA == Fraction(972, 1000)

# probabilidad condicional y Bayes: P(computador 1 funciona | A)
B = {w for w in resultados if w[0] == "F"}
P_B_y_A = sum(prob[w] for w in A & B)
P_B_dado_A = P_B_y_A / PA
print(f"P(C1 funciona | A) = {P_B_dado_A} = {float(P_B_dado_A):.6f}")
# Bayes: P(B|A) = P(A|B) P(B) / P(A);  P(A|B) = P(al menos 1 de los otros 2)
P_A_dado_B = 1 - (1 - p) ** 2
assert P_B_dado_A == P_A_dado_B * p / PA

# union: P(A U B) = P(A) + P(B) - P(A n B)
P_union = sum(prob[w] for w in A | B)
assert P_union == PA + p - P_B_y_A
print(f"P(A U B) = {float(P_union):.6f}")

# simulacion
rng = np.random.default_rng(12345)
N = 1_000_000
ok = rng.random((N, 3)) < float(p)
frec = float(np.mean(ok.sum(axis=1) >= 2))
print(f"frecuencia simulada de A (N={N}): {frec:.6f}  diferencia = {abs(frec - float(PA)):.2e}")
assert abs(frec - float(PA)) < 5e-4

# fallo de causa comun: con prob q=0.01 los tres fallan a la vez
q = Fraction(1, 100)
PA_cc = (1 - q) * PA
print(f"con fallo de causa comun q=0.01: P(A) = {float(PA_cc):.6f}")
print("Pruebas superadas.")
