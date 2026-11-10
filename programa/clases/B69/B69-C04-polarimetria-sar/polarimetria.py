#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C04: polarimetria SAR, matriz de dispersion, descomposicion de Pauli y entropia (blancos canonicos SINTETICOS).

Datos: ningun dato observado. Matrices de dispersion S = [[Shh, Shv], [Svh, Svv]] (adimensionales, amplitud compleja relativa) de blancos canonicos idealizados: plano/esfera
(S = diag(1, 1)), diedro de 0 grados (S = diag(1, -1)) y dipolo horizontal (S = diag(1, 0)). Reciprocidad: Shv = Svh. Semilla 20261109 para mezclas aleatorias.
Sistema de referencia: base lineal horizontal-vertical (H, V) del sensor; convencion de retrodispersion BSA (Back Scatter Alignment). Rotacion del blanco alrededor de la
linea de vision: S(theta) = R(theta) S R(-theta) con R = [[cos, -sin], [sin, cos]] (theta en rad).
Modelo: vector de Pauli k = (1/sqrt2) [Shh + Svv, Shh - Svv, 2 Shv]; potencias |k1|^2 (superficie/ impar), |k2|^2 (diedro/ par, 0 grados) y |k3|^2 (cruzada / diedro a 45 grados o volumen).
Span = |Shh|^2 + 2 |Shv|^2 + |Svv|^2 = |k|^2. Matriz de coherencia T = <k k^H> (3 x 3); entropia H = -sum p_i log3 p_i con p_i = lambda_i / sum lambda (autovalores de T).
Supuestos: blancos puntuales, medio recíproco, sin ruido. Validez: ilustrar las definiciones; las imagenes reales requieren calibracion radiometrica y de fase.
Tolerancias: invarianzas del span y de la potencia k1 bajo rotacion 1e-12; entropia de un blanco unico 1e-9; entropia de mezcla de tres con pesos iguales dentro de 0.02 de 1.
"""
from __future__ import annotations
import platform
import numpy as np

rng = np.random.default_rng(20261109)

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

def pauli(S):
    return np.array([S[0, 0] + S[1, 1], S[0, 0] - S[1, 1], 2 * S[0, 1]]) / np.sqrt(2)

def span(S):
    return abs(S[0, 0]) ** 2 + 2 * abs(S[0, 1]) ** 2 + abs(S[1, 1]) ** 2

def rot(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])

def girar(S, th):
    return rot(th) @ S @ rot(-th)

def entropia(T):
    lam = np.clip(np.linalg.eigvalsh(T), 0, None)
    p = lam / lam.sum()
    p = p[p > 1e-15]
    return float(-(p * np.log(p) / np.log(3)).sum())

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
blancos = {
    "plano/esfera": np.array([[1, 0], [0, 1]], dtype=complex),
    "diedro 0 deg": np.array([[1, 0], [0, -1]], dtype=complex),
    "dipolo horiz": np.array([[1, 0], [0, 0]], dtype=complex),
}
print(f"{'blanco':14s} {'span':>6s} {'|k1|^2':>8s} {'|k2|^2':>8s} {'|k3|^2':>8s}")
for n, S in blancos.items():
    k = pauli(S)
    print(f"{n:14s} {span(S):6.3f} {abs(k[0])**2:8.3f} {abs(k[1])**2:8.3f} {abs(k[2])**2:8.3f}")
    check(abs(span(S) - np.sum(np.abs(k) ** 2)) < 1e-12, f"span = |k|^2 en {n}")

# Rotacion alrededor de la linea de vision
D = blancos["diedro 0 deg"]
print("Diedro girado alrededor de la linea de vision (potencias de Pauli):")
for deg in (0, 22.5, 45, 90):
    k = pauli(girar(D, np.deg2rad(deg)))
    print(f"  {deg:5.1f} deg: |k1|^2 = {abs(k[0])**2:.4f} ; |k2|^2 = {abs(k[1])**2:.4f} ; |k3|^2 = {abs(k[2])**2:.4f} ; span = {span(girar(D, np.deg2rad(deg))):.4f}")
    check(abs(span(girar(D, np.deg2rad(deg))) - span(D)) < 1e-12, "span invariante")
    check(abs(abs(k[0]) ** 2 - abs(pauli(D)[0]) ** 2) < 1e-12, "k1 invariante")
k45 = pauli(girar(D, np.deg2rad(45)))
check(abs(k45[1]) < 1e-12 and abs(abs(k45[2]) ** 2 - 2) < 1e-12, "diedro a 45 deg es pura polarizacion cruzada")
print("Un diedro a 45 deg pasa toda su potencia a k3 (cruzada): se confunde con volumen si no se conoce la orientacion.")

# Entropia
for n, S in blancos.items():
    k = pauli(S)[:, None]
    H = entropia(k @ k.conj().T)
    check(H < 1e-9, "entropia de un blanco unico")
print("Entropia de un blanco unico (los tres): 0.000")
M = 20000
Tm = np.zeros((3, 3), dtype=complex)
ks = [pauli(blancos["plano/esfera"]), pauli(blancos["diedro 0 deg"]), pauli(girar(blancos["diedro 0 deg"], np.deg2rad(45)))]
for _ in range(M):
    j = rng.integers(3)
    Tm += np.outer(ks[j], ks[j].conj())
Tm /= M
H3 = entropia(Tm)
print(f"Mezcla aleatoria de tres blancos ortogonales (pesos ~1/3, {M} muestras): entropia = {H3:.4f}")
check(abs(H3 - 1) < 0.02, "entropia de mezcla de tres")
mez2 = 0.5 * np.outer(ks[0], ks[0].conj()) + 0.5 * np.outer(ks[1], ks[1].conj())
print(f"Mezcla exacta 50/50 de dos blancos: entropia = {entropia(mez2):.4f} (log3 2 = {np.log(2)/np.log(3):.4f})")
check(abs(entropia(mez2) - np.log(2) / np.log(3)) < 1e-12, "entropia de dos")
print("Pruebas superadas.")
