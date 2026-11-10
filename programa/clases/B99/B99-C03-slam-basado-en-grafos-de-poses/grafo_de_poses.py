#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C03: SLAM de grafo de poses 2D con Gauss-Newton sobre datos SINTETICOS.

Nodos = poses (x, y, theta) de un lazo cuadrado de 80 m (161 poses, la ultima coincide con la primera); aristas de
odometria (i, i+1) y una arista de cierre de bucle (160, 0). Error de arista e = (R_i^T (t_j - t_i) - z_xy, wrap(th_j - th_i - z_th));
coste F = sum e^T Omega e (Grisetti et al., tutorial de SLAM de grafos). Comprobaciones: Jacobiano analitico = numerico; con
aristas sin ruido el optimo recupera la verdad; con ruido consistente con Omega el chi2 final promedia los grados de libertad.
Unidades: m y rad. Ruido de odometria: sigma_t = 0.02 m, sigma_r = 0.005 rad por paso. Semillas fijas. Datos SINTETICOS.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import (cabecera, comprobar, fin, lazo_cuadrado, odometria_ruidosa, integrar, entre, info_diag, error_arista,
                       jacobianos_arista, jacobiano_numerico, chi2_total, optimizar_grafo, ate_rmse, wrap)

cabecera("Datos SINTETICOS: lazo cuadrado de 80 m, 161 poses, odometria sigma_t = 0.02 m, sigma_r = 0.005 rad")
SIG_T, SIG_R = 0.02, 0.005
SIG_LT, SIG_LR = 0.02, 0.005
gt, rel = lazo_cuadrado(40, 0.5)
n = len(gt)
Om = info_diag(SIG_T, SIG_R)
OmL = info_diag(SIG_LT, SIG_LR)


def construir(rng, con_ruido=True, con_bucle=True):
    z = odometria_ruidosa(rel, rng, SIG_T, SIG_R) if con_ruido else rel.copy()
    aristas = [(i, i + 1, z[i], Om) for i in range(n - 1)]
    x0 = integrar(z)
    if con_bucle:
        zl = entre(gt[-1], gt[0])
        if con_ruido:
            zl = zl + np.array([rng.normal(0, SIG_LT), rng.normal(0, SIG_LT), rng.normal(0, SIG_LR)])
        aristas.append((n - 1, 0, zl, OmL))
    return x0, aristas


# 1) Jacobiano analitico frente a diferencias finitas
rng = np.random.default_rng(1)
peor = 0.0
for _ in range(50):
    xi = np.array([*rng.uniform(-5, 5, 2), rng.uniform(-3, 3)])
    xj = np.array([*rng.uniform(-5, 5, 2), rng.uniform(-3, 3)])
    z = rng.normal(0, 1, 3)
    Ja, Jb = jacobianos_arista(xi, xj)
    Na, Nb = jacobiano_numerico(xi, xj, z)
    peor = max(peor, float(np.max(np.abs(Ja - Na))), float(np.max(np.abs(Jb - Nb))))
print(f"Jacobiano analitico frente a diferencias finitas (50 aristas al azar): diferencia maxima = {peor:.2e}")
comprobar(peor < 1e-6, "el Jacobiano analitico debe coincidir con el numerico")

# 2) Aristas sin ruido: partiendo de una estimacion perturbada, el optimo es la verdad
rng = np.random.default_rng(2)
x0, ar = construir(rng, con_ruido=False)
x_ini = gt + rng.normal(0, [0.3, 0.3, 0.05], gt.shape)
x_ini[0] = gt[0]
x_opt, h = optimizar_grafo(x_ini, ar, iteraciones=40)
err = float(np.max(np.linalg.norm(x_opt[:, :2] - gt[:, :2], axis=1)))
print(f"Sin ruido, partiendo de una estimacion perturbada: chi2 {h[0]:.3e} -> {h[-1]:.3e} en {len(h) - 1} iteraciones; error maximo = {err:.2e} m")
comprobar(h[-1] < 1e-8 and err < 1e-5, "sin ruido el optimo debe ser la verdad")

# 3) Un caso con ruido: deriva de la odometria sola y grafo optimizado
rng = np.random.default_rng(3)
x0, ar = construir(rng)
x_opt, h = optimizar_grafo(x0, ar, iteraciones=30)
ate0, _ = ate_rmse(x0[:, :2], gt[:, :2])
ate1, _ = ate_rmse(x_opt[:, :2], gt[:, :2])
print(f"Odometria sola: error de la pose final = {np.linalg.norm(x0[-1, :2] - gt[-1, :2]):.3f} m ; ATE = {ate0:.3f} m")
print("Iteracion -> chi2: " + " ; ".join(f"{k}: {v:.1f}" for k, v in enumerate(h[:6])))
print(f"Grafo optimizado: error de la pose final = {np.linalg.norm(x_opt[-1, :2] - gt[-1, :2]):.3f} m ; ATE = {ate1:.3f} m")
comprobar(all(h[k + 1] <= h[k] + 1e-6 for k in range(len(h) - 1)), "el chi2 no debe crecer entre iteraciones")
comprobar(ate1 < ate0, "el cierre de bucle debe reducir el ATE")

# 4) Sin cierre de bucle la optimizacion no cambia nada
x0s, ars = construir(np.random.default_rng(3), con_bucle=False)
x_s, hs = optimizar_grafo(x0s, ars, iteraciones=10)
cambio = float(np.max(np.abs(x_s - x0s)))
print(f"Sin arista de cierre: chi2 inicial = {hs[0]:.2e} ; cambio maximo de las poses = {cambio:.2e} (la cadena ya es consistente consigo misma)")
comprobar(cambio < 1e-6, "sin cierre de bucle la cadena de odometria ya es optima")

# 5) chi2 esperado = grados de libertad (3 aristas de 3 componentes menos 3*160 incognitas libres = 3)
chis, ates0, ates1 = [], [], []
for s in range(50):
    x0, ar = construir(np.random.default_rng(1000 + s))
    xo, h = optimizar_grafo(x0, ar, iteraciones=30)
    chis.append(h[-1])
    ates0.append(ate_rmse(x0[:, :2], gt[:, :2])[0])
    ates1.append(ate_rmse(xo[:, :2], gt[:, :2])[0])
dof = 3 * len(ar) - 3 * (n - 1)
print(f"50 semillas: chi2 final medio = {np.mean(chis):.2f} (grados de libertad = {dof}) ; ATE medio odometria = {np.mean(ates0):.3f} m -> optimizado = {np.mean(ates1):.3f} m")
comprobar(abs(np.mean(chis) - dof) < 1.3, "con ruido consistente, el chi2 medio debe ser cercano a los grados de libertad")
comprobar(np.mean(ates1) < np.mean(ates0), "el ATE medio debe bajar con el grafo optimizado")
fin()
