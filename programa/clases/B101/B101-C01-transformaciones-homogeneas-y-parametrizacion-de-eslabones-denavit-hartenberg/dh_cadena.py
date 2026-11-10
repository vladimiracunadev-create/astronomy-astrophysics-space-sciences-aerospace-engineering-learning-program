#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C01: transformaciones homogeneas y cinematica directa D-H de un brazo SINTETICO de 7 articulaciones.

Unidades: m y rad. Marco {0} en la base, {E} en el extremo. Tolerancia: 1e-12 en matrices.
Comprobaciones independientes: (1) D-H cerrada = Rz Tz Tx Rx; (2) brazo planar de 2 eslabones contra su formula; (3) inversa T^-1.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: brazo de 7 articulaciones, longitudes 0.4/0.6/0.6/0.3 m (didactico)")
print("Tabla D-H estandar: i, alpha [grados], a [m], d [m]")
for i in range(7):
    print(f"  {i + 1}  {np.degrees(ALPHA_NOM[i]):6.1f}  {A_NOM[i]:5.2f}  {D_NOM[i]:5.2f}")

# 1) forma cerrada frente a movimientos elementales
rng = np.random.default_rng(101)
dmax = 0.0
for _ in range(1000):
    a, al, d, th = rng.uniform(-1, 1), rng.uniform(-3, 3), rng.uniform(-1, 1), rng.uniform(-3, 3)
    dmax = max(dmax, np.abs(dh(a, al, d, th) - dh_elemental(a, al, d, th)).max())
print(f"D-H cerrada contra Rz Tz Tx Rx (1000 casos): diferencia maxima = {dmax:.2e}")
comprobar(dmax < 1e-12, "la forma cerrada debe coincidir con el producto elemental")

# 2) brazo planar de 2 eslabones: posicion con la formula directa
l1, l2 = 0.6, 0.5
q1, q2 = 0.7, -0.4
T = dh(l1, 0, 0, q1) @ dh(l2, 0, 0, q2)
x, y = l1 * np.cos(q1) + l2 * np.cos(q1 + q2), l1 * np.sin(q1) + l2 * np.sin(q1 + q2)
print(f"Planar 2R: x,y D-H = ({T[0, 3]:.6f}, {T[1, 3]:.6f}) ; formula = ({x:.6f}, {y:.6f})")
comprobar(abs(T[0, 3] - x) < 1e-12 and abs(T[1, 3] - y) < 1e-12, "planar 2R")

# 3) brazo de 7 articulaciones
T0 = fk(np.zeros(7))
print(f"Extremo con q = 0: p = ({T0[0, 3]:.4f}, {T0[1, 3]:.4f}, {T0[2, 3]:.4f}) m (alcance maximo 1.9 m)")
comprobar(np.allclose(T0[:3, 3], [0, 0, 1.9], atol=1e-12), "q = 0 debe dar (0, 0, 1.9)")
q = np.radians([30, -40, 25, 60, -35, 50, 20])
Ts = cadena(q)
Te = Ts[-1]
R = Te[:3, :3]
print("Con q = [30 -40 25 60 -35 50 20] grados:")
print("  p [m] = (%.4f, %.4f, %.4f)" % tuple(Te[:3, 3]))
print("  R ortonormal: |R R^T - I| = %.2e ; det R = %.12f" % (np.abs(R @ R.T - np.eye(3)).max(), np.linalg.det(R)))
comprobar(np.abs(R @ R.T - np.eye(3)).max() < 1e-12 and abs(np.linalg.det(R) - 1) < 1e-12, "R debe ser de rotacion")
Tinv = np.linalg.inv(Te)
Ti2 = homogenea(R.T, -R.T @ Te[:3, 3])
print(f"Inversa: inv(T) contra [R^T, -R^T p]: diferencia = {np.abs(Tinv - Ti2).max():.2e}")
comprobar(np.abs(Tinv - Ti2).max() < 1e-12, "inversa homogenea")
# cambio de marco: punto de la herramienta (0.05, 0, 0.1) m en {E} -> {0}
pt_E = np.array([0.05, 0.0, 0.1, 1.0])
pt_0 = Te @ pt_E
print("Punto de {E} (0.05, 0, 0.10) en {0}: (%.4f, %.4f, %.4f) m" % tuple(pt_0[:3]))
comprobar(abs(np.linalg.norm(pt_0[:3] - Te[:3, 3]) - np.linalg.norm(pt_E[:3])) < 1e-12, "distancia al origen de {E} invariante")
# cada eslabon conserva su longitud
dist = [np.linalg.norm(Ts[i + 1][:3, 3] - Ts[i][:3, 3]) for i in range(7)]
print("Distancia entre origenes sucesivos [m]:", " ".join(f"{v:.3f}" for v in dist))
comprobar(np.allclose(dist, D_NOM, atol=1e-12), "las distancias deben ser |d_i| (a = 0)")
# alcance
r = np.linalg.norm(Te[:3, 3])
print(f"|p| = {r:.4f} m <= 1.9 m")
comprobar(r <= 1.9 + 1e-12, "no se puede superar el alcance")
fin()
