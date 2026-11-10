#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C10: filtro de Kalman extendido multiplicativo (MEKF) de 6 estados (error de actitud + sesgo del giroscopio) con giroscopio
(10 Hz) y vectores de Sol y campo (1 Hz). Datos SINTETICOS (semilla 20260520): giro lento de ejemplo (~0.5 deg/s),
sesgo verdadero (0.05, -0.03, 0.02) deg/s, ARW 0.2 deg/sqrt(h), RRW 2 deg/h/sqrt(h), Sol 0.5 deg, campo 1.0 deg;
vectores de referencia fijos en I (ejemplo). Error inicial de actitud 5 deg. Se compara con integrar solo el giroscopio."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

N_ARW = 0.2 * D2R / 60.0
K_RRW = 2.0 * D2R / 3600.0 / 60.0
SS, SM = 0.5 * D2R, 1.0 * D2R
R1 = unit([0.6, 0.5, 0.62]); R2 = unit([-0.2, 0.9, -0.3])


def omega_true(t):
    return 0.5 * D2R * np.array([math.sin(0.05 * t), math.cos(0.04 * t), 0.6 + 0.3 * math.sin(0.02 * t)])


def correr(T=900.0, dt=0.1, seed=20260520, usar_filtro=True):
    rng = np.random.default_rng(seed)
    q = random_q(rng)
    b_true = np.array([0.05, -0.03, 0.02]) * D2R
    # estimacion inicial: error de 5 deg
    ax = unit(rng.standard_normal(3))
    qh = qmul(rotvec_to_q(ax * 5 * D2R), q)
    bh = np.zeros(3)
    P = np.diag([(5 * D2R) ** 2] * 3 + [(0.1 * D2R) ** 2] * 3)
    qg = qh.copy()                       # solo giroscopio
    errs, errg, nees = [], [], []
    ts = []
    for k in range(int(T / dt)):
        t = k * dt
        w = omega_true(t)
        # medida del giroscopio
        b_true = b_true + K_RRW * math.sqrt(dt) * rng.standard_normal(3)
        wm = w + b_true + N_ARW / math.sqrt(dt) * rng.standard_normal(3)
        # verdad
        q = qmul(rotvec_to_q(w * dt), q)
        # solo giroscopio
        qg = qmul(rotvec_to_q(wm * dt), qg)
        # propagacion del filtro
        wh = wm - bh
        qh = qmul(rotvec_to_q(wh * dt), qh)
        F = np.zeros((6, 6)); F[:3, :3] = -skew(wh); F[:3, 3:] = -np.eye(3)
        Phi = np.eye(6) + F * dt + 0.5 * (F * dt) @ (F * dt)
        Q = np.zeros((6, 6)); Q[:3, :3] = np.eye(3) * N_ARW ** 2 * dt; Q[3:, 3:] = np.eye(3) * K_RRW ** 2 * dt
        P = Phi @ P @ Phi.T + Q
        if usar_filtro and (k % 10 == 9):
            At = A_of_q(q); Ah = A_of_q(qh)
            for r, s in ((R1, SS), (R2, SM)):
                bm = noisy_unit(At @ r, s, rng)
                zh = Ah @ r
                H = np.hstack([skew(zh), np.zeros((3, 3))])
                S = H @ P @ H.T + s ** 2 * np.eye(3)
                Kg = P @ H.T @ np.linalg.inv(S)
                dx = Kg @ (bm - zh)
                P = (np.eye(6) - Kg @ H) @ P @ (np.eye(6) - Kg @ H).T + Kg @ (s ** 2 * np.eye(3)) @ Kg.T
                qh = qnormalize(qmul(np.concatenate([dx[:3] / 2, [1.0]]), qh))
                bh = bh + dx[3:]
        e = ang_between(qh, q)
        errs.append(e); errg.append(ang_between(qg, q)); ts.append(t)
        if k % 10 == 9 and t > T / 2:
            # error de actitud en ejes del cuerpo (vector pequeno)
            d = qmul(q, qconj(qh)); th = 2 * d[:3] * np.sign(d[3] if d[3] != 0 else 1)
            nees.append(float(th @ np.linalg.solve(P[:3, :3], th)))
    return np.array(ts), np.array(errs), np.array(errg), np.array(nees), float(np.linalg.norm(bh - b_true)), float(np.linalg.norm(b_true))


def calcular():
    ts, e, g, nees, db, bn = correr()
    mitad = ts > ts[-1] / 2
    # solo vectores (SVD cada 1 s) como referencia
    rng = np.random.default_rng(20260520)
    ev = []
    for _ in range(600):
        qt = random_q(rng); At = A_of_q(qt)
        a = noisy_unit(At @ R1, SS, rng); b = noisy_unit(At @ R2, SM, rng)
        w = np.array([1 / SS ** 2, 1 / SM ** 2])
        ev.append(ang_between(q_of_A(wahba_svd([a, b], [R1, R2], w)), qt))
    return dict(rms_f=math.sqrt(np.mean(e[mitad] ** 2)) * R2D, e0=e[0] * R2D, e60=e[600] * R2D, rms_g=float(np.sqrt(np.mean(g ** 2))) * R2D,
                gfin=g[-1] * R2D, ef=e[-1] * R2D, rms_v=math.sqrt(np.mean(np.square(ev))) * R2D, db=db * R2D * 3600, bn=bn * R2D * 3600,
                nees=float(np.mean(nees)), t60=ts[600])


def main():
    banner("B87-C10 MEKF | SINTETICO (semilla 20260520): giroscopio 10 Hz, Sol 0.5 deg y campo 1.0 deg a 1 Hz, 900 s, error inicial 5 deg")
    d = calcular()
    print(f"error de actitud: inicial = {d['e0']:.3f} deg ; a 60 s = {d['e60']:.3f} deg ; final = {d['ef']:.4f} deg")
    print(f"rms del filtro en la segunda mitad (450-900 s) = {d['rms_f']:.4f} deg")
    print(f"solo giroscopio (sesgo sin corregir): final = {d['gfin']:.2f} deg ; rms = {d['rms_g']:.2f} deg")
    print(f"solo vectores (SVD por epoca, sin filtrar): rms = {d['rms_v']:.4f} deg")
    print(f"sesgo: |verdadero| = {d['bn']:.1f} deg/h ; error de estimacion final = {d['db']:.1f} deg/h")
    print(f"NEES medio (consistencia, ideal ~3) = {d['nees']:.2f}")
    assert d['gfin'] > 10 * d['rms_f'] and d['rms_f'] < d['rms_v'] and d['db'] < 0.3 * d['bn']
    assert 0.3 < d['nees'] < 12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
