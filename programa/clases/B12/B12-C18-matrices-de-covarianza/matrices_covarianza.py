#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C18: matrices de covarianza.

Datos: SINTETICOS e ILUSTRATIVOS. (a) Covarianza de posicion plana (m^2) con
sigma_x = 3 m, sigma_y = 4 m y correlacion 0.8. (b) Estado (posicion,
velocidad) con sigma_x = 3 m y sigma_v = 0.02 m/s, propagado dt = 100 s con
x' = x + v dt. (c) Una "matriz de correlacion" inconsistente.
Modelo: P simetrica semidefinida positiva; descomposicion espectral
P = V L V^T; transformacion lineal P' = J P J^T; distancia de Mahalanobis
d^2 = e^T P^-1 e ~ chi^2 con k grados de libertad (k = 2: P(d^2<=s)=1-exp(-s/2)).
Supuestos: errores gaussianos de media cero para el muestreo.
Validez: linealizacion de la transformacion.
Tolerancia: reconstruccion espectral 1e-12; covarianza muestral dentro de
0.05 (N = 1 000 000); cobertura del elipse de 95 % dentro de 0.003. Las
pruebas detienen la ejecucion si fallan.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")
s1, s2, rho = 3.0, 4.0, 0.8
P = np.array([[s1**2, rho * s1 * s2], [rho * s1 * s2, s2**2]])
print("P =", P.tolist())
assert np.allclose(P, P.T)
w, V = np.linalg.eigh(P)
print(f"autovalores = {np.round(w, 4)} (m^2); semiejes 1-sigma = {np.round(np.sqrt(w), 4)} m")
assert np.all(w > 0) and np.allclose(V @ np.diag(w) @ V.T, P, atol=1e-12)
tr, det = P.trace(), np.linalg.det(P)
assert abs(w.sum() - tr) < 1e-12 and abs(w.prod() - det) < 1e-9
ang = math.degrees(0.5 * math.atan2(2 * P[0, 1], P[0, 0] - P[1, 1]))
print(f"traza = {tr:.1f}; det = {det:.2f}; angulo del eje mayor = {ang:.2f} grados respecto del eje x")
k95 = math.sqrt(-2 * math.log(0.05))
print(f"elipse al 95 % (2 gl): factor {k95:.4f}; semiejes = {np.round(k95*np.sqrt(w[::-1]), 3)} m")

# muestreo con Cholesky y covarianza muestral
L = np.linalg.cholesky(P)
assert np.allclose(L @ L.T, P, atol=1e-12)
rng = np.random.default_rng(1818)
N = 1_000_000
e = rng.standard_normal((N, 2)) @ L.T
Ps = np.cov(e.T)
print("covarianza muestral =", np.round(Ps, 3).tolist())
assert np.max(np.abs(Ps - P)) < 0.05
d2 = np.einsum("ij,jk,ik->i", e, np.linalg.inv(P), e)
cov95 = float(np.mean(d2 <= -2 * math.log(0.05)))
print(f"fraccion con d^2 <= {-2*math.log(0.05):.4f}: {cov95:.4f} (chi^2 de 2 gl: 0.95)")
assert abs(cov95 - 0.95) < 0.003

# propagacion lineal de un estado (x, v)
sx, sv, dt = 3.0, 0.02, 100.0
P0 = np.diag([sx**2, sv**2])
J = np.array([[1.0, dt], [0.0, 1.0]])
P1 = J @ P0 @ J.T
r = P1[0, 1] / math.sqrt(P1[0, 0] * P1[1, 1])
print(f"P tras dt={dt:.0f} s: var(x) = {P1[0,0]:.2f} m^2, cov = {P1[0,1]:.4f} m^2/s, var(v) = {P1[1,1]:.4f}; correlacion = {r:.4f}")
assert abs(P1[0, 0] - (sx**2 + dt**2 * sv**2)) < 1e-12 and abs(r - 0.5547) < 1e-3
assert abs(np.linalg.det(P1) - np.linalg.det(P0)) < 1e-12  # J con det 1 conserva el determinante

# matriz de correlacion inconsistente
C = np.array([[1, 0.9, 0.9], [0.9, 1, -0.9], [0.9, -0.9, 1]])
wc = np.linalg.eigvalsh(C)
print(f"correlaciones (0.9, 0.9, -0.9): autovalores = {np.round(wc, 4)} -> no semidefinida positiva")
assert wc.min() < 0
try:
    np.linalg.cholesky(C)
    raise SystemExit("Cholesky debio fallar")
except np.linalg.LinAlgError:
    print("Cholesky falla: la matriz no es una covarianza valida")
print("Pruebas superadas.")
