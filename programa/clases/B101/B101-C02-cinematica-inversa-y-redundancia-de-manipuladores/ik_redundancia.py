#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C02: cinematica inversa: analitica planar (2 soluciones) y numerica de 7 articulaciones con espacio nulo.

Unidades: m, rad. Datos SINTETICOS. Semilla 102. Tolerancias: 1e-8 m / rad en el error de pose.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: brazo planar 2R (0.6, 0.5 m) y brazo de 7 articulaciones de B101-C01")
l1, l2 = 0.6, 0.5
x, y = 0.55, 0.45
c2 = (x * x + y * y - l1 * l1 - l2 * l2) / (2 * l1 * l2)
comprobar(abs(c2) <= 1, "objetivo alcanzable")
print(f"Planar 2R, objetivo ({x}, {y}) m: cos q2 = {c2:.6f}")
for signo, nombre in ((1, "codo abajo"), (-1, "codo arriba")):
    q2 = signo * np.arccos(c2)
    q1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(q2), l1 + l2 * np.cos(q2))
    xf = l1 * np.cos(q1) + l2 * np.cos(q1 + q2)
    yf = l1 * np.sin(q1) + l2 * np.sin(q1 + q2)
    print(f"  {nombre}: q1 = {np.degrees(q1):8.3f}  q2 = {np.degrees(q2):8.3f} grados ; FK = ({xf:.6f}, {yf:.6f})")
    comprobar(abs(xf - x) < 1e-12 and abs(yf - y) < 1e-12, "la FK debe devolver el objetivo")
print(f"Fuera de alcance: |r| = 1.2 m > l1 + l2 = {l1 + l2} m -> sin solucion (|cos q2| = {abs((1.2**2 - l1**2 - l2**2) / (2 * l1 * l2)):.3f} > 1)")

rng = np.random.default_rng(102)
q_obj = np.radians([30, -40, 25, 60, -35, 50, 20])
T_obj = fk(q_obj)
print("Objetivo de 6 dimensiones generado con q = [30 -40 25 60 -35 50 20] grados")
sol = []
for k in range(40):
    q0 = rng.uniform(-1.5, 1.5, 7)
    q, it, e = ik_amortiguada(T_obj, q0)
    if e < 1e-8:
        sol.append(q)
print(f"Newton amortiguado desde 40 arranques: {len(sol)} convergen (error < 1e-8)")
comprobar(len(sol) >= 30, "la mayoria debe converger")
# soluciones distintas (modulo 2 pi)
dist = []
for q in sol:
    w = (q + np.pi) % (2 * np.pi) - np.pi
    if all(np.linalg.norm(((w - u + np.pi) % (2 * np.pi)) - np.pi) > 1e-3 for u in dist):
        dist.append(w)
print(f"Configuraciones articulares distintas que alcanzan la MISMA pose: {len(dist)}")
comprobar(len(dist) >= 5, "un brazo redundante tiene muchas soluciones")
print("  error de pose de cada una (max) = %.2e" % max(np.linalg.norm(error_pose(T_obj, fk(q))) for q in dist))

# espacio nulo: movimiento autonomo que no cambia la pose
q = sol[0]
J = jacobiano(q)
U, S, Vt = np.linalg.svd(J)
n = Vt[6]   # direccion del espacio nulo (7 - 6 = 1)
print(f"Rango de J = {np.linalg.matrix_rank(J)} ; |J n| = {np.linalg.norm(J @ n):.2e} (espacio nulo de dimension 1)")
comprobar(np.linalg.norm(J @ n) < 1e-10, "J n debe ser cero")
qn = q.copy()
for _ in range(2000):
    Jn = jacobiano(qn)
    nn = np.linalg.svd(Jn)[2][6]
    if nn @ n < 0:
        nn = -nn
    qn = qn + 1e-3 * nn
    e = error_pose(T_obj, fk(qn))
    qn = qn + Jn.T @ np.linalg.solve(Jn @ Jn.T + 1e-6 * np.eye(6), e)
e = np.linalg.norm(error_pose(T_obj, fk(qn)))
dq = np.linalg.norm(qn - q)
print(f"Tras 2 rad de recorrido en el espacio nulo: error de pose = {e:.2e} ; desplazamiento articular = {dq:.3f} rad")
comprobar(e < 1e-6 and dq > 0.3, "la pose se mantiene y las articulaciones se mueven")
# pseudoinversa: la solucion de menor norma de velocidad
v = np.array([0.01, 0.0, -0.02, 0.0, 0.01, 0.0])
qd = np.linalg.pinv(J) @ v
print(f"pinv: |J qd - v| = {np.linalg.norm(J @ qd - v):.2e} ; |qd| = {np.linalg.norm(qd):.4f} ; qd . n = {qd @ n:.2e}")
comprobar(abs(qd @ n) < 1e-10 and np.linalg.norm(J @ qd - v) < 1e-12, "pinv es ortogonal al espacio nulo")
fin()
