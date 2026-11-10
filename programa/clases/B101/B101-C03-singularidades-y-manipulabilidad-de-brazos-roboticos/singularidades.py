#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C03: jacobiano, manipulabilidad (Yoshikawa), valores singulares y minimos cuadrados amortiguados cerca de una singularidad.

Unidades: m, rad. Datos SINTETICOS (brazo de B101-C01). Tolerancias: jacobiano frente a diferencias finitas < 1e-7.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: planar 2R (0.6, 0.5 m) y brazo de 7 articulaciones de B101-C01")
l1, l2 = 0.6, 0.5
print("Planar 2R: w = sqrt(det(J J^T)) contra l1 l2 |sin q2|")
for q2d in (90, 45, 10, 1, 0):
    q2 = np.radians(q2d)
    J = np.array([[-l2 * np.sin(q2), -l2 * np.sin(q2)], [l1 + l2 * np.cos(q2), l2 * np.cos(q2)]])
    w = np.sqrt(max(np.linalg.det(J @ J.T), 0.0))
    wa = l1 * l2 * abs(np.sin(q2))
    print(f"  q2 = {q2d:3d} grados: w = {w:.6f}  formula = {wa:.6f}")
    comprobar(abs(w - wa) < 1e-12, "manipulabilidad planar")

rng = np.random.default_rng(103)
q = rng.uniform(-1, 1, 7)
J = jacobiano(q)
h = 1e-6
Jn = np.zeros((6, 7))
for i in range(7):
    dq = np.zeros(7)
    dq[i] = h
    Tp, Tm = fk(q + dq), fk(q - dq)
    Jn[:3, i] = (Tp[:3, 3] - Tm[:3, 3]) / (2 * h)
    dR = Tp[:3, :3] @ Tm[:3, :3].T
    Jn[3:, i] = np.array([dR[2, 1] - dR[1, 2], dR[0, 2] - dR[2, 0], dR[1, 0] - dR[0, 1]]) / (4 * h)
print(f"Jacobiano analitico contra diferencias finitas (6x7): diferencia max = {np.abs(J - Jn).max():.2e}")
comprobar(np.abs(J - Jn).max() < 1e-7, "jacobiano")

print("Brazo de 7 articulaciones, codo q4 de 90 grados a 0 (resto: q = [0.3 -0.4 0.2 q4 -0.3 0.5 0.1] rad)")
print("  q4 [gr]   w            sigma_min     sigma_max    cond")
ws = []
for q4d in (90, 60, 30, 10, 3, 1, 0):
    q = np.array([0.3, -0.4, 0.2, np.radians(q4d), -0.3, 0.5, 0.1])
    J = jacobiano(q)
    s = np.linalg.svd(J, compute_uv=False)
    w = np.sqrt(max(np.linalg.det(J @ J.T), 0))
    ws.append(w)
    print(f"  {q4d:5d}   {w:10.3e}   {s[-1]:10.3e}   {s[0]:9.4f}   {s[0] / max(s[-1], 1e-300):9.2e}")
comprobar(all(ws[i] > ws[i + 1] for i in range(len(ws) - 1)), "w debe decrecer al estirar el codo")
comprobar(ws[-1] < 1e-6, "codo estirado es singular")

# velocidad pedida en la direccion que se pierde
q = np.array([0.3, -0.4, 0.2, np.radians(2.0), -0.3, 0.5, 0.1])
J = jacobiano(q)
U, S, Vt = np.linalg.svd(J)
v = U[:, 5] * 0.05   # 5 cm/s a lo largo del eje singular mas debil
qd_pinv = np.linalg.pinv(J) @ v
print(f"Codo a 2 grados, velocidad pedida 0.05 en el eje debil (sigma_min = {S[5]:.4f}):")
print(f"  pinv:      |qd| = {np.linalg.norm(qd_pinv):8.3f} rad/s ; error = {np.linalg.norm(J @ qd_pinv - v):.2e}")
for lam in (0.01, 0.05, 0.2):
    qd = J.T @ np.linalg.solve(J @ J.T + lam**2 * np.eye(6), v)
    print(f"  DLS {lam:4.2f}: |qd| = {np.linalg.norm(qd):8.3f} rad/s ; error = {np.linalg.norm(J @ qd - v):.2e}")
qd05 = J.T @ np.linalg.solve(J @ J.T + 0.05**2 * np.eye(6), v)
comprobar(np.linalg.norm(qd05) < np.linalg.norm(qd_pinv), "DLS reduce la velocidad articular")
comprobar(np.linalg.norm(J @ qd05 - v) > 1e-6, "DLS introduce un error de seguimiento")
qd0 = J.T @ np.linalg.solve(J @ J.T + 1e-12 * np.eye(6), v)
print(f"  DLS con lambda -> 0 contra pinv: diferencia relativa = {np.linalg.norm(qd0 - qd_pinv) / np.linalg.norm(qd_pinv):.2e}")
comprobar(np.linalg.norm(qd0 - qd_pinv) / np.linalg.norm(qd_pinv) < 1e-4, "limite lambda -> 0")
fin()
