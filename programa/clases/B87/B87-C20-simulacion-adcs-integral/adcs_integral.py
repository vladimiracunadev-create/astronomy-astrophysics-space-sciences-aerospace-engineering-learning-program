#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C20: simulacion ADCS integral SINTETICA: dinamica con ruedas + giroscopio (10 Hz) + vectores de Sol y campo (1 Hz) + MEKF de
6 estados + control PD en cuaterniones con ruedas (par de rueda limitado) + par perturbador constante. Satelite I = diag(0.35, 0.40, 0.30)
kg m^2; objetivo: actitud fija de ejemplo; error inicial de 20 deg; 600 s; dt = 0.1 s; semilla 20260524. Vectores de referencia fijos en I
(ejemplo). Segunda via: el momento angular total inercial cambia solo por la integral del par perturbador."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

N_ARW = 0.2 * D2R / 60.0
K_RRW = 2.0 * D2R / 3600.0 / 60.0
SS, SM = 0.5 * D2R, 1.0 * D2R
R1 = unit([0.6, 0.5, 0.62]); R2 = unit([-0.2, 0.9, -0.3])
TAU_D = np.array([2e-6, -1e-6, 3e-6])
UMAX = 0.01


class MEKF:
    def __init__(self, q0):
        self.q = q0.copy(); self.b = np.zeros(3)
        self.P = np.diag([(5 * D2R) ** 2] * 3 + [(0.1 * D2R) ** 2] * 3)

    def propagar(self, wm, dt):
        wh = wm - self.b
        self.q = qmul(rotvec_to_q(wh * dt), self.q)
        F = np.zeros((6, 6)); F[:3, :3] = -skew(wh); F[:3, 3:] = -np.eye(3)
        Phi = np.eye(6) + F * dt + 0.5 * (F * dt) @ (F * dt)
        Q = np.zeros((6, 6)); Q[:3, :3] = np.eye(3) * N_ARW ** 2 * dt; Q[3:, 3:] = np.eye(3) * K_RRW ** 2 * dt
        self.P = Phi @ self.P @ Phi.T + Q
        return wh

    def actualizar(self, bm, r, s):
        zh = A_of_q(self.q) @ r
        H = np.hstack([skew(zh), np.zeros((3, 3))])
        S = H @ self.P @ H.T + s ** 2 * np.eye(3)
        Kg = self.P @ H.T @ np.linalg.inv(S)
        dx = Kg @ (bm - zh)
        IKH = np.eye(6) - Kg @ H
        self.P = IKH @ self.P @ IKH.T + Kg @ (s ** 2 * np.eye(3)) @ Kg.T
        self.q = qnormalize(qmul(np.concatenate([dx[:3] / 2, [1.0]]), self.q))
        self.b = self.b + dx[3:]


def calcular(T=600.0, dt=0.1, seed=20260524):
    rng = np.random.default_rng(seed)
    I = inertia_example()
    Id = np.diag(I)
    wn, zeta = 0.15, 0.9
    kp = 2 * Id.mean() * wn ** 2; kd = 2 * zeta * wn * Id
    qc = q_from_axis_angle([1, 1, 0.5], 20 * D2R)         # actitud objetivo de ejemplo
    q = np.array([0, 0, 0, 1.0]); w = np.zeros(3); h = np.zeros(3)
    b_true = np.array([0.05, -0.03, 0.02]) * D2R
    qh0 = qmul(rotvec_to_q(unit([1, -1, 1]) * 3 * D2R), q)
    f = MEKF(qh0)
    Hi0 = A_of_q(q).T @ (I @ w + h)
    errp, erre, umax, hmax, imp = [], [], 0.0, 0.0, np.zeros(3)
    for k in range(int(T / dt)):
        t = k * dt
        b_true = b_true + K_RRW * math.sqrt(dt) * rng.standard_normal(3)
        wm = w + b_true + N_ARW / math.sqrt(dt) * rng.standard_normal(3)
        wh = f.propagar(wm, dt)
        if k % 10 == 9:
            At = A_of_q(q)
            f.actualizar(noisy_unit(At @ R1, SS, rng), R1, SS)
            f.actualizar(noisy_unit(At @ R2, SM, rng), R2, SM)
        qe = qmul(f.q, qconj(qc))
        s = 1.0 if qe[3] >= 0 else -1.0
        tau_cmd = -kp * s * qe[:3] - kd * wh
        u = np.clip(-tau_cmd, -UMAX, UMAX)               # par sobre las ruedas (el cuerpo recibe -u)
        umax = max(umax, float(np.max(np.abs(u))))
        A_old = A_of_q(q)
        q, w, h = step(q, w, h, u, TAU_D, I, dt)
        imp = imp + 0.5 * (A_old.T + A_of_q(q).T) @ TAU_D * dt     # regla del trapecio
        hmax = max(hmax, float(np.linalg.norm(h)))
        errp.append(ang_between(q, qc) * R2D); erre.append(ang_between(f.q, q) * R2D)
    Hi = A_of_q(q).T @ (I @ w + h)
    dH = np.linalg.norm((Hi - Hi0) - imp)
    ult = int(200 / dt)
    return dict(p_ini=errp[0], p_rms=math.sqrt(np.mean(np.square(errp[-ult:]))), p_fin=errp[-1], e_rms=math.sqrt(np.mean(np.square(erre[-ult:]))),
                umax=umax, hmax=hmax, dH=float(dH), Hint=float(np.linalg.norm(imp)), t90=float(np.argmax(np.array(errp) < 2.0) * dt),
                bfin=float(np.linalg.norm(f.b - b_true) * R2D * 3600))


def main():
    banner("B87-C20 simulacion ADCS integral | SINTETICO (semilla 20260524): 600 s, giroscopio 10 Hz, Sol/campo 1 Hz, MEKF, PD con ruedas")
    d = calcular()
    print(f"error de apuntamiento (verdadero vs objetivo): inicial = {d['p_ini']:.2f} deg ; < 2 deg desde t = {d['t90']:.0f} s ; rms ultimos 200 s = {d['p_rms']*3600:.1f} arcsec ; final = {d['p_fin']*3600:.1f} arcsec")
    print(f"error de estimacion del MEKF (ultimos 200 s) rms = {d['e_rms']*3600:.1f} arcsec ; error del sesgo estimado = {d['bfin']:.1f} deg/h")
    print(f"par de rueda maximo = {d['umax']*1e3:.2f} mN m (limite {UMAX*1e3:.0f}) ; momento de rueda maximo = {d['hmax']:.4f} N m s")
    print(f"segunda via: |Delta H_total - integral del par perturbador| = {d['dH']:.2e} N m s (integral = {d['Hint']:.2e})")
    assert d['p_rms'] * 3600 < 600 and d['e_rms'] < 0.2 and d['dH'] < 1e-7 and d['umax'] <= UMAX + 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
