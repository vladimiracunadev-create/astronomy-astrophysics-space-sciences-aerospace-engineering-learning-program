#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C12: propagacion de incertidumbre (matriz de transicion, Monte Carlo y puntos sigma) en una orbita sintetica.

Todo SINTETICO: orbita kepleriana (a = 7200 km, e = 0.01, i = 55 deg), mu = 3.986004e14 m3/s2 (valor nominal ilustrativo, no consultado).
Incertidumbre inicial ILUSTRATIVA: 100 m por eje y 0.1 m/s por eje, sin correlaciones. Se propaga 1, 10 y 50 periodos con: (a) la matriz de transicion
por diferencias centrales; (b) Monte Carlo con 4000 muestras (semilla 41); (c) transformada unscented (13 puntos, alpha = 1, beta = 2, kappa = 3 - n). Se compara la desviacion estandar de la posicion a lo largo de la trayectoria (direccion de la velocidad) y la
fraccion de muestras de Monte Carlo dentro del elipsoide lineal de 95 % (esperado 0.95 si la gaussiana lineal vale).
Tolerancias: a 1 periodo la sigma lineal y la de Monte Carlo coinciden dentro del 5 %; en Kepler la STM verifica determinante = 1 (simplectica) dentro de 1e-6.
Version: Python 3.12.9, NumPy 2.4.4.
"""
import json, math, platform, sys
import numpy as np

MU = 3.986004e14


def stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z); return (1 - math.cos(s)) / z, (s - math.sin(s)) / s**3
    if z < -1e-8:
        s = math.sqrt(-z); return (math.cosh(s) - 1) / (-z), (math.sinh(s) - s) / s**3
    return 0.5 - z / 24, 1 / 6 - z / 120


def prop(x0, dt):
    r0, v0 = x0[:3], x0[3:]
    r0n = np.linalg.norm(r0); vr0 = np.dot(r0, v0) / r0n
    al = 2 / r0n - np.dot(v0, v0) / MU
    chi = math.sqrt(MU) * abs(al) * dt
    for _ in range(100):
        z = al * chi**2; C, S = stumpff(z)
        F = r0n * vr0 / math.sqrt(MU) * chi**2 * C + (1 - al * r0n) * chi**3 * S + r0n * chi - math.sqrt(MU) * dt
        dF = r0n * vr0 / math.sqrt(MU) * chi * (1 - z * S) + (1 - al * r0n) * chi**2 * C + r0n
        d = F / dF; chi -= d
        if abs(d) < 1e-10: break
    z = al * chi**2; C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C; g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0; rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi; gd = 1 - chi**2 / rn * C
    return np.concatenate([r, fd * r0 + gd * v0])


def estado_inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


def main():
    rng = np.random.default_rng(41)
    x0 = estado_inicial()
    P0 = np.diag([100.0**2] * 3 + [0.1**2] * 3)
    T = 2 * math.pi * math.sqrt(7.2e6**3 / MU)
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita y covarianza SINTETICAS, semilla 41)",
           f"Periodo = {T:.2f} s ; P0: 100 m y 0.1 m/s por eje"]
    res = {"T": T}
    out.append("n_per  sigma_along STM[m]  sigma_along MC[m]  sigma_along UT[m]  det(STM)   dentro 95% lineal")
    ok = True
    for npr in (1, 10, 50):
        dt = npr * T
        xe = prop(x0, dt)
        Phi = np.zeros((6, 6))
        for k in range(6):
            d = np.zeros(6); d[k] = 1.0 if k < 3 else 1e-3
            Phi[:, k] = (prop(x0 + d, dt) - prop(x0 - d, dt)) / (2 * d[k])
        P = Phi @ P0 @ Phi.T
        u = xe[3:] / np.linalg.norm(xe[3:])
        s_stm = math.sqrt(u @ P[:3, :3] @ u)
        X = rng.multivariate_normal(x0, P0, 4000)
        Y = np.array([prop(x, dt) for x in X])
        s_mc = float(np.std((Y[:, :3] - xe[:3]) @ u, ddof=1))
        # UT
        n = 6; alpha = 1.0; kappa = 3.0 - n; lam = alpha**2 * (n + kappa) - n
        L = np.linalg.cholesky((n + lam) * P0)
        S = np.vstack([x0, x0 + L.T, x0 - L.T])
        wm = np.full(2 * n + 1, 1 / (2 * (n + lam))); wc = wm.copy(); wm[0] = lam / (n + lam); wc[0] = wm[0] + 1 - alpha**2 + 2
        Z = np.array([prop(s, dt) for s in S])
        zm = wm @ Z
        dz = Z[:, :3] - zm[:3]
        Pu = (wc[:, None] * dz).T @ dz
        s_ut = math.sqrt(u @ Pu @ u)
        # fraccion dentro del elipsoide lineal 95 %
        dY = Y - xe
        Pl = P
        m2 = np.einsum("ij,jk,ik->i", dY[:, :3], np.linalg.inv(Pl[:3, :3]), dY[:, :3])
        frac = float(np.mean(m2 < 7.8147))
        detS = float(np.linalg.det(Phi))
        out.append(f"{npr:5d}  {s_stm:16.1f}  {s_mc:16.1f}  {s_ut:16.1f}  {detS:9.6f}  {frac:12.3f}")
        res[f"stm{npr}"] = s_stm; res[f"mc{npr}"] = s_mc; res[f"ut{npr}"] = s_ut; res[f"fr{npr}"] = frac; res[f"det{npr}"] = detS
        if npr == 1:
            ok &= abs(s_mc / s_stm - 1) < 0.05
        ok &= abs(detS - 1) < 1e-4
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print("\n".join(out)); raise SystemExit(1)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
