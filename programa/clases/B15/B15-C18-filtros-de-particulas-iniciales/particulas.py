#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C18: filtro de partículas (bootstrap) en una dimensión.

Datos: SINTÉTICOS, semilla fija. Estado x = [posición, velocidad]; modelo
x_k = F x_{k-1} + G a, a ~ N(0, sa^2), F = [[1, dt],[0, 1]], G = [dt^2/2, dt].
Filtro: N partículas; en cada paso se propagan con el modelo, se pesan con la
verosimilitud de la medida y se remuestrean (sistemático) cuando
ESS = 1/sum(w^2) < N/2.
Referencias independientes:
 (1) remuestreo sistemático: el número de copias de la partícula i difiere de
     N w_i en menos de 1;  (2) ESS = N con pesos uniformes y 1 con pesos
     degenerados;  (3) caso lineal gaussiano (medida de la posición): el filtro
     de Kalman es exacto, así que el de partículas debe acercarse a su RMSE al
     crecer N;  (4) caso no lineal (distancia oblicua a un sensor desplazado):
     el filtro de partículas supera a la inversión directa de cada medida.
Supuestos: modelo y ruidos conocidos. Tolerancias: 10 % en el RMSE (3); 1 en (1).
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def remuestreo_sistematico(w, rng):
    N = len(w)
    pos = (rng.random() + np.arange(N)) / N
    cs = np.cumsum(w)
    cs[-1] = 1.0
    return np.searchsorted(cs, pos)


def ess(w):
    return 1.0 / np.sum(w**2)


def pf(z, medida, sigma, N, F, G, sa, x0, P0, rng):
    part = rng.multivariate_normal(x0, P0, N)
    w = np.full(N, 1.0 / N)
    est, ess_min, nres = [], N, 0
    for zk in z:
        part = part @ F.T + np.outer(rng.standard_normal(N) * sa, G)
        w = w * np.exp(-0.5 * ((zk - medida(part)) / sigma) ** 2)
        w /= w.sum()
        e = ess(w)
        ess_min = min(ess_min, e)
        if e < N / 2:
            idx = remuestreo_sistematico(w, rng)
            part, w = part[idx], np.full(N, 1.0 / N)
            nres += 1
        est.append(w @ part)
    return np.array(est), ess_min, nres


def kalman(z, F, H, Q, R, x0, P0):
    x, P, out = x0.copy(), P0.copy(), []
    for zk in z:
        x = F @ x
        P = F @ P @ F.T + Q
        S = H @ P @ H.T + R
        K = P @ H.T @ np.linalg.inv(S)
        x = x + (K @ (zk - H @ x))
        P = (np.eye(2) - K @ H) @ P
        out.append(x.copy())
    return np.array(out)


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15018)

# (1) y (2)
w = rng.random(10); w /= w.sum()
cuenta = np.bincount(remuestreo_sistematico(w, rng), minlength=10)
print(f"(1) remuestreo sistemático (N=10): máx |copias - N w| = {np.max(np.abs(cuenta - 10*w)):.3f}")
prueba(np.max(np.abs(cuenta - 10 * w)) < 1, "remuestreo")
d = np.zeros(100); d[0] = 1
print(f"(2) ESS: uniforme (N=100) {ess(np.full(100, .01)):.1f}; degenerado {ess(d):.1f}")
prueba(abs(ess(np.full(100, .01)) - 100) < 1e-9 and abs(ess(d) - 1) < 1e-12, "ESS")

# Modelo común
dt, sa = 1.0, 0.1
F = np.array([[1, dt], [0, 1.0]])
G = np.array([dt**2 / 2, dt])
Q = sa**2 * np.outer(G, G)

# (3) Lineal gaussiano: PF frente a Kalman
sig, T, runs = 5.0, 60, 20
H = np.array([[1.0, 0.0]])
R = np.array([[sig**2]])
x0, P0 = np.array([0.0, 7.0]), np.diag([sig**2, 1.0])
res = {}
for Np in (50, 200, 1000, 5000):
    errs_pf, errs_kf = [], []
    for r in range(runs):
        x = rng.multivariate_normal(x0, P0)
        xt, zs = [], []
        for k in range(T):
            x = F @ x + G * sa * rng.standard_normal()
            xt.append(x.copy()); zs.append(x[0] + sig * rng.standard_normal())
        xt, zs = np.array(xt), np.array(zs)
        e_pf, _, _ = pf(zs, lambda p: p[:, 0], sig, Np, F, G, sa, x0, P0, rng)
        e_kf = kalman(zs[:, None], F, H, Q, R, x0, P0)
        errs_pf.append((e_pf - xt)[20:, 0]); errs_kf.append((e_kf - xt)[20:, 0])
    res[Np] = (np.sqrt(np.mean(np.concatenate(errs_pf) ** 2)), np.sqrt(np.mean(np.concatenate(errs_kf) ** 2)))
print("(3) lineal gaussiano, RMSE de la posición (m) tras 20 pasos:")
for Np, (a, b) in res.items():
    print(f"    N = {Np:5d} partículas: filtro de partículas {a:.3f}; Kalman (exacto) {b:.3f}; cociente {a/b:.3f}")
prueba(res[5000][0] / res[5000][1] < 1.10 and res[50][0] >= res[5000][0], "con muchas partículas se acerca a Kalman")

# (4) No lineal: distancia oblicua
h, sg, T = 20.0, 2.0, 60
Rz = lambda p: np.sqrt(p[:, 0] ** 2 + h**2)
x0n, P0n = np.array([-150.0, 5.0]), np.diag([10.0**2, 1.0])
sa_n = 0.05
Gs = G * sa_n
errs_pf, errs_raw, esmin, nres = [], [], 1e9, []
for r in range(20):
    x = rng.multivariate_normal(x0n, P0n)
    xt, zs = [], []
    for k in range(T):
        x = F @ x + Gs * rng.standard_normal()
        xt.append(x.copy()); zs.append(np.hypot(x[0], h) + sg * rng.standard_normal())
    xt, zs = np.array(xt), np.array(zs)
    e_pf, em, nr = pf(zs, Rz, sg, 2000, F, G, sa_n, x0n, P0n, rng)
    raw = np.sign(xt[:, 0]) * np.sqrt(np.maximum(zs**2 - h**2, 0))          # inversión directa (conoce el signo)
    errs_pf.append(e_pf[:, 0] - xt[:, 0]); errs_raw.append(raw - xt[:, 0])
    esmin = min(esmin, em); nres.append(nr)
ep, er = np.concatenate(errs_pf), np.concatenate(errs_raw)
print(f"(4) distancia oblicua (sensor a {h:.0f} m de la pista, ruido {sg} m), 2000 partículas, 20 trayectorias:")
print(f"    RMSE posición: filtro de partículas {np.sqrt(np.mean(ep**2)):.2f} m; inversión directa {np.sqrt(np.mean(er**2)):.2f} m")
print(f"    ESS mínimo observado {esmin:.0f} de 2000; remuestreos por trayectoria {np.mean(nres):.1f} de {T}")
prueba(np.sqrt(np.mean(ep**2)) < 0.6 * np.sqrt(np.mean(er**2)), "el filtro de partículas supera a la inversión")
print("Pruebas superadas.")
