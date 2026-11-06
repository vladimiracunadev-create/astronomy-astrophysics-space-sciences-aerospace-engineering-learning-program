#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C17: filtro de Kalman lineal en una dimensión.

Datos: SINTÉTICOS, semilla fija. Objeto que se mueve en una dimensión con
velocidad casi constante; se mide su posición cada dt = 1 s con ruido gaussiano
de sigma = 5 m. Estado x = [posición, velocidad].
Modelo: x_k = F x_{k-1} + w, F = [[1, dt],[0, 1]]; z_k = H x_k + v, H = [1, 0];
Q = sa^2 [[dt^4/4, dt^3/2],[dt^3/2, dt^2]] (aceleración aleatoria blanca de
desviación sa = 0.1 m/s^2); R = sigma^2.
Predicción:  x- = F x,  P- = F P F^T + Q.
Actualización: S = H P- H^T + R, K = P- H^T / S, x = x- + K (z - H x-), P = (I - K H) P-.
Referencias independientes:
 (1) caso escalar F=1, Q=0: el filtro con P0 enorme da la media aritmética de las
     medidas y P_k = R/k;
 (2) la covarianza de predicción en régimen estacionario coincide con la solución
     de la ecuación de Riccati discreta (scipy.linalg.solve_discrete_are);
 (3) consistencia: el error normalizado NEES = e^T P^-1 e tiene media ~ 2 (dim. del estado).
Supuestos: modelo lineal, ruidos blancos gaussianos con covarianzas conocidas.
Tolerancias: 1e-4 en (1) (P0 = 1e12 no es infinito); 2 % en (2); 10 % en el RMSE y 10 % en el NEES.
"""
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import solve_discrete_are


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def kalman(z, F, H, Q, R, x0, P0):
    x, P = x0.copy(), P0.copy()
    xs, Ps, Pp = [], [], []
    for zk in z:
        x = F @ x
        P = F @ P @ F.T + Q
        Pp.append(P.copy())
        S = H @ P @ H.T + R
        K = P @ H.T @ np.linalg.inv(S)
        x = x + K @ (zk - H @ x)
        P = (np.eye(len(x)) - K @ H) @ P
        xs.append(x.copy())
        Ps.append(P.copy())
    return np.array(xs), np.array(Ps), np.array(Pp)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15017)

# (1) Caso escalar: media aritmética
R1 = 4.0
z = 10 + 2 * rng.standard_normal(50)
xs, Ps, _ = kalman(z[:, None], np.eye(1), np.eye(1), np.zeros((1, 1)), np.array([[R1]]), np.zeros(1), np.eye(1) * 1e12)
medias = np.cumsum(z) / np.arange(1, 51)
d1 = np.max(np.abs(xs[:, 0] - medias))
d2 = np.max(np.abs(Ps[:, 0, 0] * np.arange(1, 51) / R1 - 1))
print(f"(1) caso escalar: diferencia con la media aritmética {d1:.1e}; |P_k k/R - 1| máx. {d2:.1e}")
prueba(d1 < 1e-4 and d2 < 1e-4, "el filtro escalar es la media")

# (2) Régimen estacionario
dt, sig, sa = 1.0, 5.0, 0.1
F = np.array([[1, dt], [0, 1.0]])
H = np.array([[1.0, 0.0]])
Q = sa**2 * np.array([[dt**4 / 4, dt**3 / 2], [dt**3 / 2, dt**2]])
R = np.array([[sig**2]])
Pss = solve_discrete_are(F.T, H.T, Q, R)          # covarianza de predicción estacionaria
K_ss = Pss @ H.T @ np.linalg.inv(H @ Pss @ H.T + R)
Ppost = (np.eye(2) - K_ss @ H) @ Pss
print(f"(2) Riccati: P- = {np.round(Pss,3).tolist()}; K = {K_ss.ravel().round(4).tolist()}; sd posterior de la posición = {np.sqrt(Ppost[0,0]):.3f} m, de la velocidad = {np.sqrt(Ppost[1,1]):.4f} m/s")

# (3) Simulación
T, runs = 200, 300
x_true0 = np.array([0.0, 7.0])
err_f, err_m, nees = [], [], []
G = np.array([dt**2 / 2, dt])          # Q = sa^2 G G^T: una sola aceleración aleatoria
ultimo_Pp = None
for _ in range(runs):
    x = x_true0.copy()
    xt, zs = [], []
    for k in range(T):
        x = F @ x + G * sa * rng.standard_normal()
        xt.append(x.copy())
        zs.append(H @ x + sig * rng.standard_normal(1))
    xt, zs = np.array(xt), np.array(zs)
    xs, Ps, Pp = kalman(zs, F, H, Q, R, np.array([zs[0, 0], 0.0]), np.diag([sig**2, 10.0**2]))
    e = (xs - xt)[100:]                     # tras el transitorio
    err_f.append(e[:, 0])
    err_m.append((zs[100:, 0] - xt[100:, 0]))
    nees.append(np.einsum("ki,kij,kj->k", e, np.linalg.inv(Ps[100:]), e))
    ultimo_Pp = Pp[-1]
rmse_f = np.sqrt(np.mean(np.concatenate(err_f) ** 2))
rmse_m = np.sqrt(np.mean(np.concatenate(err_m) ** 2))
nm = np.mean(np.concatenate(nees))
print(f"(3) RMSE de la posición: medidas {rmse_m:.3f} m; filtro {rmse_f:.3f} m (teoría posterior {np.sqrt(Ppost[0,0]):.3f} m); NEES medio {nm:.3f} (ideal 2)")
print(f"    P- al final {np.round(ultimo_Pp,3).tolist()} (estacionaria {np.round(Pss,3).tolist()})")
prueba(np.max(np.abs(ultimo_Pp / Pss - 1)) < 0.02, "P converge a la solución de Riccati")
prueba(abs(rmse_f / np.sqrt(Ppost[0, 0]) - 1) < 0.1 and abs(rmse_m / sig - 1) < 0.05 and rmse_f < 0.6 * rmse_m, "RMSE del filtro")
prueba(abs(nm / 2 - 1) < 0.1, "consistencia (NEES)")

# (4) Modelo equivocado: Q demasiado pequeña
Qm = Q * 1e-4
nees2, err2 = [], []
for _ in range(100):
    x = x_true0.copy()
    xt, zs = [], []
    for k in range(T):
        x = F @ x + G * sa * rng.standard_normal()
        xt.append(x.copy())
        zs.append(H @ x + sig * rng.standard_normal(1))
    xt, zs = np.array(xt), np.array(zs)
    xs, Ps, _ = kalman(zs, F, H, Qm, R, np.array([zs[0, 0], 0.0]), np.diag([sig**2, 10.0**2]))
    e = (xs - xt)[100:]
    err2.append(e[:, 0])
    nees2.append(np.einsum("ki,kij,kj->k", e, np.linalg.inv(Ps[100:]), e))
print(f"(4) con Q multiplicada por 1e-4: RMSE {np.sqrt(np.mean(np.concatenate(err2)**2)):.3f} m; NEES medio {np.mean(np.concatenate(nees2)):.1f} (ideal 2): filtro demasiado confiado")
prueba(np.mean(np.concatenate(nees2)) > 3 * 2, "NEES delata el modelo erróneo")
print("Pruebas superadas.")
