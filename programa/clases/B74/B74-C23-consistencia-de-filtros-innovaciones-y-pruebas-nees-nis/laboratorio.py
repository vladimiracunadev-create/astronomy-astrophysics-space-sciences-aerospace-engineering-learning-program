#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C23: pruebas de consistencia de un filtro de Kalman con NEES y NIS (promedios de Monte Carlo y limites chi-cuadrado).

Todo SINTETICO: movimiento en una dimension con aceleracion aleatoria (q verdadero = 0.05 (m/s2)^2), medida de posicion cada 1 s con sigma 5 m, 60 s,
N = 100 realizaciones independientes (semilla 73). Tres filtros: acertado (q = 0.05), optimista (q = 0.005) y conservador (q = 0.5). Para cada paso k se calculan
NEES_k = promedio sobre las N realizaciones de e^T P^-1 e (n = 2 grados de libertad) y NIS_k = promedio de nu^2/S (1 grado de libertad). Limites de aceptacion de dos colas al 95 %:
[chi2_{0.025, N d}/N, chi2_{0.975, N d}/N] con el cuantil de chi-cuadrado por la aproximacion de Wilson-Hilferty (z de la normal por biseccion con erf; aproximacion estandar NO consultada).
Se reporta la fraccion de pasos (k >= 10) dentro de los limites y el promedio temporal.
Tolerancias: el filtro acertado debe tener fraccion dentro de limites >= 0.85 en NEES y NIS; el optimista debe tener NEES medio > limite superior; el conservador < limite inferior.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np


def zq(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 0.5 * (1 + math.erf(mid / math.sqrt(2))) < p: lo = mid
        else: hi = mid
    return (lo + hi) / 2


def chi2q(p, nu):
    z = zq(p)
    return nu * (1 - 2 / (9 * nu) + z * math.sqrt(2 / (9 * nu))) ** 3


def sim(rng, N, n, dt, qv, sig):
    F = np.array([[1, dt], [0, 1.0]]); G = np.array([dt**2 / 2, dt])
    X = np.zeros((N, 2)); X[:, 1] = 10.0
    tru = np.zeros((n, N, 2)); med = np.zeros((n, N))
    for k in range(n):
        a = rng.normal(0, math.sqrt(qv), N)
        X = X @ F.T + a[:, None] * G
        tru[k] = X
        med[k] = X[:, 0] + rng.normal(0, sig, N)
    return tru, med


def filtra(tru, med, q, sig, dt):
    n, N = med.shape
    F = np.array([[1, dt], [0, 1.0]]); G = np.array([[dt**2 / 2], [dt]])
    Q = q * (G @ G.T); H = np.array([[1.0, 0.0]]); R = sig**2
    nees = np.zeros(n); nis = np.zeros(n)
    for r in range(N):
        x = np.array([0.0, 8.0]); P = np.diag([100.0**2, 20.0**2])
        for k in range(n):
            x = F @ x; P = F @ P @ F.T + Q
            S = (H @ P @ H.T)[0, 0] + R
            nu = med[k, r] - x[0]
            K = (P @ H.T)[:, 0] / S
            x = x + K * nu
            P = (np.eye(2) - np.outer(K, H[0])) @ P
            e = x - tru[k, r]
            nees[k] += e @ np.linalg.solve(P, e) / N
            nis[k] += nu**2 / S / N
    return nees, nis


def main():
    rng = np.random.default_rng(73)
    N, n, dt, sig, qv = 100, 60, 1.0, 5.0, 0.05
    tru, med = sim(rng, N, n, dt, qv, sig)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (datos SINTETICOS, semilla 73)",
           f"N = {N} realizaciones, {n} pasos ; q verdadero = {qv} (m/s2)^2"]
    lim = {}
    for d, nom in ((2, "NEES"), (1, "NIS")):
        lim[nom] = (chi2q(0.025, N * d) / N, chi2q(0.975, N * d) / N)
        out.append(f"Limites {nom} (95 %, {d} gl, promedio de {N}): [{lim[nom][0]:.3f}, {lim[nom][1]:.3f}] ; esperado {d}")
    res = {"lo_nees": lim["NEES"][0], "hi_nees": lim["NEES"][1], "lo_nis": lim["NIS"][0], "hi_nis": lim["NIS"][1]}
    out.append("filtro          q       NEES medio  dentro   NIS medio  dentro")
    ok = True
    for nom, q in (("acertado", 0.05), ("optimista", 0.005), ("conservador", 0.5)):
        ne, ni = filtra(tru, med, q, sig, dt)
        s = slice(10, n)
        fe = float(np.mean((ne[s] >= lim["NEES"][0]) & (ne[s] <= lim["NEES"][1])))
        fi = float(np.mean((ni[s] >= lim["NIS"][0]) & (ni[s] <= lim["NIS"][1])))
        out.append(f"{nom:12s} {q:7.3f}  {ne[s].mean():10.3f}  {fe:6.2f}  {ni[s].mean():10.3f}  {fi:6.2f}")
        res[f"ne_{nom}"] = float(ne[s].mean()); res[f"fe_{nom}"] = fe; res[f"ni_{nom}"] = float(ni[s].mean()); res[f"fi_{nom}"] = fi
        if nom == "acertado": ok &= fe >= 0.85 and fi >= 0.85
        if nom == "optimista": ok &= ne[s].mean() > lim["NEES"][1]
        if nom == "conservador": ok &= ne[s].mean() < lim["NEES"][0]
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
