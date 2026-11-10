#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B74-C09: filtro de Kalman extendido (EKF) sobre una orbita kepleriana sintetica.

Todo SINTETICO: la misma orbita y las mismas dos estaciones fijas de la clase C07 (marco inercial simplificado), observaciones de
alcance (sigma 10 m) y velocidad de alcance (sigma 0.01 m/s) cada 30 s durante 20 min (ILUSTRATIVO). mu = 3.986004e14 m3/s2 (valor nominal
ilustrativo, no consultado). La matriz de transicion se obtiene por diferencias centrales del propagador (1 m, 1e-3 m/s); el jacobiano de
la medida es analitico. Ruido de proceso pequeno (Q = diag(0,0,0,1e-8,1e-8,1e-8) (m/s)^2 por paso), ILUSTRATIVO.
Estado inicial: verdad + error sorteado con P0 = diag((200 m)^2 x3, (0.2 m/s)^2 x3); se repite con P0 grande (2 km, 2 m/s). Pruebas: (1) el error final del EKF es menor que el inicial;
(2) la solucion del EKF en el ultimo instante coincide con el ajuste por lotes (Gauss-Newton) con diferencia < 10 m; (3) el NEES medio
de 40 realizaciones (semilla 29) esta entre 3 y 10 con P0 pequena (esperado cercano a 6) y es mayor con P0 grande.
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
        if abs(d) < 1e-9: break
    z = al * chi**2; C, S = stumpff(z)
    f = 1 - chi**2 / r0n * C; g = dt - chi**3 / math.sqrt(MU) * S
    r = f * r0 + g * v0; rn = np.linalg.norm(r)
    fd = math.sqrt(MU) / (rn * r0n) * (z * S - 1) * chi; gd = 1 - chi**2 / rn * C
    return np.concatenate([r, fd * r0 + gd * v0])


def stm(x, dt):
    Phi = np.zeros((6, 6))
    for k in range(6):
        d = np.zeros(6); d[k] = 1.0 if k < 3 else 1e-3
        Phi[:, k] = (prop(x + d, dt) - prop(x - d, dt)) / (2 * d[k])
    return Phi


def estado_inicial():
    a, e, inc = 7.2e6, 0.01, math.radians(55)
    p = a * (1 - e**2)
    rp = p / (1 + e) * np.array([1.0, 0, 0]); vp = math.sqrt(MU / p) * np.array([0, 1 + e, 0])
    c, s = math.cos(inc), math.sin(inc)
    Q = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    return np.concatenate([Q @ rp, Q @ vp])


EST = np.array([[6.371e6, 0, 0], [0, 4.5e6, 4.5e6]])
SIG = np.array([10.0, 0.01])
DT, NP = 30.0, 40


def h(x, s):
    d = x[:3] - s; rho = np.linalg.norm(d)
    return np.array([rho, np.dot(d, x[3:]) / rho])


def H_an(x, s):
    d = x[:3] - s; rho = np.linalg.norm(d); u = d / rho; v = x[3:]
    drr_dr = (v - np.dot(u, v) * u) / rho
    return np.vstack([np.concatenate([u, np.zeros(3)]), np.concatenate([drr_dr, u])])


def ekf(x0, P0, ys, Qd):
    x, P = x0.copy(), P0.copy()
    nees_hist = []
    for k in range(NP):
        Phi = stm(x, DT)
        x = prop(x, DT)
        P = Phi @ P @ Phi.T + Qd
        for j, s in enumerate(EST):
            y = ys[k][j]
            H = H_an(x, s)
            R = np.diag(SIG**2)
            S = H @ P @ H.T + R
            K = P @ H.T @ np.linalg.inv(S)
            x = x + K @ (y - h(x, s))
            P = (np.eye(6) - K @ H) @ (P) @ (np.eye(6) - K @ H).T + K @ R @ K.T
    return x, P


def lotes(x_ini, ys):
    x = x_ini.copy()
    for _ in range(6):
        N = np.zeros((6, 6)); b = np.zeros(6)
        xk = x.copy(); Phi = np.eye(6)
        for k in range(NP):
            Phi_k = stm(xk, DT)
            xk = prop(xk, DT); Phi = Phi_k @ Phi
            for j, s in enumerate(EST):
                H = H_an(xk, s) @ Phi
                W = np.diag(1 / SIG**2)
                N += H.T @ W @ H
                b += H.T @ W @ (ys[k][j] - h(xk, s))
        dx = np.linalg.solve(N, b)
        x = x + dx
        if np.linalg.norm(dx[:3]) < 1e-3:
            break
    return x


def main():
    rng = np.random.default_rng(29)
    xt0 = estado_inicial()
    truth = [xt0]
    for k in range(NP):
        truth.append(prop(truth[-1], DT))
    P0 = np.diag([200.0**2] * 3 + [0.2**2] * 3)
    P0g = np.diag([2000.0**2] * 3 + [2.0**2] * 3)
    Qd = np.diag([0, 0, 0, 1e-8, 1e-8, 1e-8])
    def sim_obs():
        return [[h(truth[k + 1], s) + rng.normal(0, SIG) for s in EST] for k in range(NP)]
    out = [f"Python {platform.python_version()}, NumPy {np.__version__} (orbita y observaciones SINTETICAS, semilla 29)"]
    ys = sim_obs()
    x0 = xt0 + rng.multivariate_normal(np.zeros(6), P0)
    xf, Pf = ekf(x0, P0, ys, Qd)
    e_ini = np.linalg.norm(x0[:3] - xt0[:3])
    e_fin = np.linalg.norm(xf[:3] - truth[-1][:3])
    sf = np.sqrt(np.diag(Pf))
    out.append(f"Caso conductor (P0: 200 m, 0.2 m/s): error inicial = {e_ini:.1f} m ; error final del EKF = {e_fin:.2f} m ; velocidad final = {np.linalg.norm(xf[3:]-truth[-1][3:]):.5f} m/s")
    out.append(f"sigma formal final (x,y,z) [m] = {sf[0]:.2f} {sf[1]:.2f} {sf[2]:.2f}")
    xl = lotes(x0, ys)
    xl_fin = xl
    for k in range(NP):
        xl_fin = prop(xl_fin, DT)
    dif = np.linalg.norm(xl_fin[:3] - xf[:3])
    out.append(f"Diferencia EKF frente al ajuste por lotes en el instante final = {dif:.3f} m")
    def mc(P0x, n=40):
        v = []
        for _ in range(n):
            ysi = sim_obs()
            x0i = xt0 + rng.multivariate_normal(np.zeros(6), P0x)
            xi, Pi = ekf(x0i, P0x, ysi, Qd)
            ei = xi - truth[-1]
            v.append(float(ei @ np.linalg.solve(Pi, ei)))
        return float(np.mean(v))
    nm = mc(P0)
    nmg = mc(P0g)
    out.append(f"NEES medio de 40 realizaciones con P0 pequena = {nm:.2f} (esperado cercano a 6)")
    out.append(f"NEES medio de 40 realizaciones con P0 grande (2 km, 2 m/s) = {nmg:.2f} (la linealizacion falla)")
    ok = e_fin < e_ini and dif < 10.0 and 3.0 < nm < 10.0 and nmg > nm
    out.append("Pruebas superadas." if ok else "PRUEBAS FALLIDAS")
    if not ok:
        print(chr(10).join(out)); raise SystemExit(1)
    res = dict(e_ini=float(e_ini), e_fin=float(e_fin), ev=float(np.linalg.norm(xf[3:] - truth[-1][3:])), sx=float(sf[0]), sy=float(sf[1]), sz=float(sf[2]),
               dif=float(dif), nees=nm, neesg=nmg)
    return out, res


if __name__ == "__main__":
    o, r = main()
    print(json.dumps(r) if "--json" in sys.argv else "\n".join(o))
