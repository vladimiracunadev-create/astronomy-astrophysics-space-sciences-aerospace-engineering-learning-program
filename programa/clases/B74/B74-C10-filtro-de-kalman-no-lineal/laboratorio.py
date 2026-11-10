#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C10: EKF frente a filtro de puntos sigma (UKF) en una actualizacion no lineal.

Todo SINTETICO: un objeto con previa gaussiana en el plano (x, y) = (7000, 0) km con sigma 300 km por eje, observado por un
sensor en el origen que mide alcance (sigma 5 km) y azimut (sigma 0.15 rad, ILUSTRATIVO y grande a proposito para exagerar la no linealidad).
Se compara la actualizacion del EKF (jacobiano), la del UKF (puntos sigma, parametros alpha = 0.5, beta = 2, kappa = 0) y una referencia
de Bayes por muestreo de importancia con 100 000 muestras. 400 realizaciones (semilla 31). Metricas: error cuadratico medio de la
media a posteriori respecto de la verdad y NEES medio. Tolerancia: el ECM de la referencia debe ser menor o igual que el de EKF y UKF dentro de 5 %
(nadie supera a Bayes); la media del NEES de la referencia debe estar entre 1.6 y 2.4 (esperado 2).
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

RNG = np.random.default_rng(31)
M0 = np.array([7000.0, 0.0])  # km
P0 = np.eye(2) * 300.0**2
R = np.diag([5.0**2, 0.15**2])


def h(x):
    return np.array([np.hypot(x[0], x[1]), np.arctan2(x[1], x[0])])


def H_an(x):
    r = np.hypot(x[0], x[1])
    return np.array([[x[0] / r, x[1] / r], [-x[1] / r**2, x[0] / r**2]])


def ekf_upd(m, P, y):
    H = H_an(m)
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    inn = y - h(m); inn[1] = (inn[1] + np.pi) % (2 * np.pi) - np.pi
    return m + K @ inn, P - K @ S @ K.T


def ukf_upd(m, P, y, alpha=0.5, beta=2.0, kappa=0.0):
    n = 2; lam = alpha**2 * (n + kappa) - n
    L = np.linalg.cholesky((n + lam) * P)
    X = np.vstack([m, m + L.T, m - L.T])
    wm = np.full(2 * n + 1, 1 / (2 * (n + lam))); wc = wm.copy()
    wm[0] = lam / (n + lam); wc[0] = lam / (n + lam) + 1 - alpha**2 + beta
    Y = np.array([h(x) for x in X])
    # promedio angular correcto
    ym = np.array([wm @ Y[:, 0], math.atan2(wm @ np.sin(Y[:, 1]), wm @ np.cos(Y[:, 1]))])
    dY = Y - ym; dY[:, 1] = (dY[:, 1] + np.pi) % (2 * np.pi) - np.pi
    S = R + (wc[:, None] * dY).T @ dY
    C = (wc[:, None] * (X - m)).T @ dY
    K = C @ np.linalg.inv(S)
    inn = y - ym; inn[1] = (inn[1] + np.pi) % (2 * np.pi) - np.pi
    return m + K @ inn, P - K @ S @ K.T


def bayes_ref(y, N=400000):
    X = RNG.multivariate_normal(M0, P0, N)
    r = np.hypot(X[:, 0], X[:, 1]); th = np.arctan2(X[:, 1], X[:, 0])
    dth = (y[1] - th + np.pi) % (2 * np.pi) - np.pi
    w = np.exp(-0.5 * ((y[0] - r) ** 2 / R[0, 0] + dth**2 / R[1, 1]))
    w /= w.sum()
    m = w @ X
    d = X - m
    return m, (w[:, None] * d).T @ d


def main():
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (objeto y sensor SINTETICOS, semilla 31)"]
    res = {}
    n = 400
    acc = {k: [] for k in ("ekf", "ukf", "ref")}
    nees = {k: [] for k in ("ekf", "ukf", "ref")}
    for _ in range(n):
        x = RNG.multivariate_normal(M0, P0)
        y = h(x) + RNG.multivariate_normal(np.zeros(2), R)
        for k, (m, P) in (("ekf", ekf_upd(M0, P0, y)), ("ukf", ukf_upd(M0, P0, y)), ("ref", bayes_ref(y, 100000))):
            e = m - x
            acc[k].append(e @ e)
            nees[k].append(e @ np.linalg.solve(P, e))
    out.append("filtro    ECM [km^2]   rms [km]   NEES medio (esperado 2)")
    for k, nom in (("ekf", "EKF"), ("ukf", "UKF"), ("ref", "Bayes")):
        ecm = float(np.mean(acc[k])); ne = float(np.mean(nees[k]))
        out.append(f"{nom:6s}  {ecm:10.1f}  {math.sqrt(ecm):9.2f}  {ne:8.3f}")
        res[f"ecm_{k}"] = ecm; res[f"rms_{k}"] = math.sqrt(ecm); res[f"nees_{k}"] = ne
    ok = res["ecm_ref"] <= 1.05 * min(res["ecm_ekf"], res["ecm_ukf"]) and 1.6 < res["nees_ref"] < 2.4
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
