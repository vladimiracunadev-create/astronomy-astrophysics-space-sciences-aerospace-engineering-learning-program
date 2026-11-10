#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C01: odometria por correspondencias de puntos de referencia SINTETICOS, ajuste de cuerpo rigido y RANSAC.

Version simplificada en 2D de la estimacion de movimiento 3D-a-3D: entre dos instantes el robot observa los mismos puntos
de referencia en su marco; el movimiento relativo es la transformacion rigida que lleva el conjunto 1 al 2 (SVD, Kabsch).
RANSAC (muestra minima de 2 puntos) rechaza correspondencias erroneas. Se integran los movimientos y se mide la deriva.
Unidades: m y rad; marco del mundo 2D con x, y; marco del cuerpo con x hacia adelante. Semilla fija. Tolerancias: sin ruido
y sin atipicos el movimiento se recupera a < 1e-9 m. TODOS los datos son SINTETICOS (no vienen de un rover ni de imagenes).
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import (cabecera, comprobar, fin, rot, inversa, componer, integrar, lazo_cuadrado, kabsch2d)

cabecera("Datos SINTETICOS: 300 puntos de referencia, alcance 8 m, lazo cuadrado de 80 m de perimetro, semilla 11")
gt, rel_gt = lazo_cuadrado(40, 0.5)
rng_mundo = np.random.default_rng(11)
puntos = rng_mundo.uniform([-6, -6], [26, 26], size=(300, 2))
ALCANCE = 8.0


def observar(pose, ids):
    """Coordenadas de los puntos ids en el marco del cuerpo de la pose."""
    return (rot(pose[2]).T @ (puntos[ids] - pose[:2]).T).T


def visibles(pose):
    d = np.linalg.norm(puntos - pose[:2], axis=1)
    return np.where(d < ALCANCE)[0]


def pose_desde_Rt(R, t):
    """Movimiento del cuerpo (pose k+1 vista desde k) a partir de la transformacion p_{k+1} = R p_k + t."""
    return inversa(np.array([t[0], t[1], math.atan2(R[1, 0], R[0, 0])]))


def ransac_movimiento(P, Q, rng, iteraciones=60, umbral=0.10):
    mejor = None
    n = len(P)
    for _ in range(iteraciones):
        idx = rng.choice(n, 2, replace=False)
        s, R, t = kabsch2d(P[idx], Q[idx])
        err = np.linalg.norm((R @ P.T).T + t - Q, axis=1)
        inl = err < umbral
        if mejor is None or inl.sum() > mejor.sum():
            mejor = inl
    s, R, t = kabsch2d(P[mejor], Q[mejor])
    return R, t, mejor


def corrida(sigma, frac_atipicos, usar_ransac, semilla):
    rng = np.random.default_rng(semilla)
    rel_est = []
    n_inl = []
    for k in range(len(rel_gt)):
        ids = np.intersect1d(visibles(gt[k]), visibles(gt[k + 1]))
        P = observar(gt[k], ids) + rng.normal(0, sigma, (len(ids), 2))
        Q = observar(gt[k + 1], ids) + rng.normal(0, sigma, (len(ids), 2))
        m = int(round(frac_atipicos * len(ids)))
        if m:
            malos = rng.choice(len(ids), m, replace=False)
            Q[malos] = Q[rng.permutation(malos)] + rng.normal(0, 1.0, (m, 2)) + 2.0   # correspondencias erroneas
        if usar_ransac:
            R, t, inl = ransac_movimiento(P, Q, rng)
            n_inl.append(int(inl.sum()))
        else:
            _, R, t = kabsch2d(P, Q)
            n_inl.append(len(ids))
        rel_est.append(pose_desde_Rt(R, t))
    est = integrar(np.array(rel_est))
    return est, np.array(n_inl)


def deriva(est):
    return float(np.linalg.norm(est[-1, :2] - gt[-1, :2]))


largo = float(np.sum(np.linalg.norm(rel_gt[:, :2], axis=1)))
print(f"Recorrido verdadero: {len(rel_gt)} pasos, {largo:.1f} m; la pose final vuelve al origen")

# 1) Sin ruido ni atipicos: el ajuste debe recuperar el movimiento exacto
est0, _ = corrida(0.0, 0.0, False, 1)
e0 = float(np.max(np.linalg.norm(est0[:, :2] - gt[:, :2], axis=1)))
print(f"Sin ruido ni atipicos: error maximo de posicion = {e0:.2e} m")
comprobar(e0 < 1e-9, "sin ruido el ajuste debe recuperar la trayectoria exacta")

# 2) Ruido de medida y atipicos: deriva con y sin RANSAC
print("sigma[m]  atipicos  RANSAC  deriva_final[m]  deriva[% de recorrido]  inliers_medios")
resultados = {}
for sigma, frac, ran in [(0.02, 0.0, False), (0.02, 0.2, False), (0.02, 0.2, True), (0.05, 0.2, True), (0.10, 0.2, True)]:
    ds = []
    ni = []
    for sem in range(6):
        est, n_inl = corrida(sigma, frac, ran, 100 + sem)
        ds.append(deriva(est))
        ni.append(n_inl.mean())
    d = float(np.mean(ds))
    resultados[(sigma, frac, ran)] = d
    print(f"{sigma:7.2f}  {frac:8.0%}  {'si' if ran else 'no':>6}  {d:15.3f}  {100 * d / largo:21.2f}  {np.mean(ni):14.1f}")
comprobar(resultados[(0.02, 0.2, True)] < 0.5 * resultados[(0.02, 0.2, False)],
          "RANSAC debe reducir la deriva con 20 % de atipicos")
comprobar(resultados[(0.05, 0.2, True)] > resultados[(0.02, 0.2, True)], "mas ruido debe dar mas deriva")

# 3) La deriva se acumula: error de posicion a lo largo del recorrido (una corrida, sigma 0.05 m, RANSAC)
est, _ = corrida(0.05, 0.2, True, 500)
err = np.linalg.norm(est[:, :2] - gt[:, :2], axis=1)
print("Deriva acumulada en una corrida (sigma = 0.05 m, 20 % atipicos, RANSAC):")
for frac in (0.25, 0.5, 0.75, 1.0):
    k = int(frac * (len(gt) - 1))
    print(f"  tras {k:3d} pasos ({frac * largo:5.1f} m): error = {err[k]:.3f} m")
fin()
