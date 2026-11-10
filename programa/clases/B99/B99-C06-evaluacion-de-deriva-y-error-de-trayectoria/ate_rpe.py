#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C06: error absoluto (ATE) y relativo (RPE) de trayectoria sobre trayectorias SINTETICAS.

ATE: se asocian las poses por indice, se alinea la estimacion con la verdad por cuerpo rigido (SVD) y se toma el RMSE de la
traslacion restante (definicion de la herramienta de evaluacion del conjunto TUM RGB-D: asociacion, alineacion por SVD y RMSE
de la traslacion). RPE: error del movimiento relativo entre poses separadas delta pasos; no requiere alineacion y sirve para
estimar la deriva. Comprobaciones analiticas: ATE de una trayectoria identica = 0; invariancia del ATE alineado y del RPE a
una transformacion rigida; error de escala sobre una recta, ATE = |s-1| d sqrt((N^2-1)/12) y RPE = |s-1| d.
Unidades: m y rad; marco del mundo 2D. Semillas fijas. Todas las trayectorias son SINTETICAS.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import (cabecera, comprobar, fin, lazo_cuadrado, odometria_ruidosa, integrar, componer, entre, info_diag,
                       optimizar_grafo, ate_rmse, rpe_trans, rot, wrap)

cabecera("Datos SINTETICOS: lazo cuadrado de 80 m (161 poses) y rectas de paso 0.5 m, semillas fijas")
gt, rel = lazo_cuadrado(40, 0.5)
n = len(gt)
largo = float(np.sum(np.linalg.norm(rel[:, :2], axis=1)))

# 1) Casos analiticos
ate_id, _ = ate_rmse(gt[:, :2], gt[:, :2])
print(f"Trayectoria identica: ATE = {ate_id:.1e} m")
comprobar(ate_id < 1e-12, "el ATE de la trayectoria identica debe ser cero")

th, t = 0.7, np.array([12.0, -5.0])
mov = np.array([componer(np.array([*t, th]), p) for p in gt])
sin_alinear = float(np.sqrt(np.mean(np.sum((mov[:, :2] - gt[:, :2]) ** 2, axis=1))))
ate_mov, _ = ate_rmse(mov[:, :2], gt[:, :2])
rt, rr = rpe_trans(mov, gt, 1)
print(f"Verdad movida rigidamente (giro 0.7 rad, traslado 13 m): error sin alinear = {sin_alinear:.2f} m ; ATE alineado = {ate_mov:.1e} m ; RPE = {rt:.1e} m, {rr:.1e} rad")
comprobar(ate_mov < 1e-9 and rt < 1e-9 and rr < 1e-9, "ATE alineado y RPE deben ser invariantes a una transformacion rigida")

N, d, s = 100, 0.5, 1.02
recta = np.column_stack([np.arange(N) * d, np.zeros(N), np.zeros(N)])
est = recta.copy()
est[:, 0] *= s
ate_s, _ = ate_rmse(est[:, :2], recta[:, :2])
ate_teo = abs(s - 1) * d * np.sqrt((N**2 - 1) / 12)
rt_s, _ = rpe_trans(est, recta, 1)
print(f"Recta de {N} puntos con error de escala 2 %: ATE = {ate_s:.6f} m (teoria {ate_teo:.6f}) ; RPE(1 paso) = {rt_s:.6f} m (teoria {abs(s - 1) * d:.6f})")
comprobar(abs(ate_s - ate_teo) < 1e-9 and abs(rt_s - abs(s - 1) * d) < 1e-9, "ATE y RPE deben coincidir con la teoria")

# 2) Dos estimadores sobre el lazo: odometria sola y grafo con cierre de bucle
sig_t, sig_r = 0.02, 0.005
rng = np.random.default_rng(61)
z = odometria_ruidosa(rel, rng, sig_t, sig_r, sesgo_rot=0.001)
x_odo = integrar(z)
Om = info_diag(sig_t, sig_r)
aristas = [(i, i + 1, z[i], Om) for i in range(n - 1)]
aristas.append((n - 1, 0, entre(gt[-1], gt[0]) + np.array([0.01, -0.01, 0.002]), info_diag(0.02, 0.005)))
x_graf, _ = optimizar_grafo(x_odo, aristas, iteraciones=30)
print(f"\nLazo de {largo:.0f} m con sesgo de giro de 0.001 rad por paso; la pose final verdadera vuelve al origen")
print("estimador            ATE[m]  RPE(1 paso)[m]  RPE(40 pasos)[m]  RPE(40) rot[rad]  error final[m]  deriva[% de recorrido]")
res = {}
for nombre, x in (("odometria sola", x_odo), ("grafo con bucle", x_graf)):
    a, _ = ate_rmse(x[:, :2], gt[:, :2])
    r1 = rpe_trans(x, gt, 1)
    r40 = rpe_trans(x, gt, 40)
    ef = float(np.linalg.norm(x[-1, :2] - gt[-1, :2]))
    res[nombre] = (a, r1[0], r40[0], ef)
    print(f"{nombre:18s} {a:7.3f}  {r1[0]:14.4f}  {r40[0]:16.3f}  {r40[1]:16.4f}  {ef:14.3f}  {100 * ef / largo:22.2f}")
comprobar(res["grafo con bucle"][0] < res["odometria sola"][0], "el grafo debe reducir el ATE")
comprobar(res["grafo con bucle"][3] < res["odometria sola"][3], "el grafo debe reducir el error final")
print(f"El RPE de 1 paso apenas cambia ({res['odometria sola'][1]:.4f} frente a {res['grafo con bucle'][1]:.4f} m): el cierre corrige el error global, no el local")

# 3) La deriva crece mas que linealmente con la distancia (rectas con ruido de giro): ATE medio de 30 semillas
print("\npasos  distancia[m]  ATE medio[m]")
dist, ates = [], []
for Np in (80, 160, 320, 640):
    relr = np.tile([0.5, 0.0, 0.0], (Np, 1))
    gtr = integrar(relr)
    v = []
    for sem in range(30):
        e = integrar(odometria_ruidosa(relr, np.random.default_rng(900 + sem), 0.02, 0.005))
        v.append(ate_rmse(e[:, :2], gtr[:, :2])[0])
    dist.append(0.5 * Np)
    ates.append(float(np.mean(v)))
    print(f"{Np:5d}  {0.5 * Np:12.0f}  {ates[-1]:12.3f}")
pend = float(np.polyfit(np.log(dist), np.log(ates), 1)[0])
print(f"Pendiente log-log del ATE frente a la distancia = {pend:.2f} (1 = lineal)")
comprobar(pend > 1.0, "el ATE debe crecer mas que linealmente con la distancia")

# 4) El RPE de rotacion identifica directamente un sesgo de giro (recta con giro constante)
relb = np.tile([0.5, 0.0, 0.002], (160, 1))
est_b = integrar(relb)
rec = integrar(np.tile([0.5, 0.0, 0.0], (160, 1)))
ate_b, _ = ate_rmse(est_b[:, :2], rec[:, :2])
rb = rpe_trans(est_b, rec, 1)
print(f"Sesgo de giro de 0.002 rad por paso en una recta de 80 m: ATE = {ate_b:.3f} m ; RPE rotacion (1 paso) = {rb[1]:.4f} rad (= sesgo)")
comprobar(abs(rb[1] - 0.002) < 1e-9, "el RPE de rotacion debe igualar el sesgo por paso")
fin()
