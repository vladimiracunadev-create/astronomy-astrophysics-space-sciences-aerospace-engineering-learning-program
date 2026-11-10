#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C21: control predictivo (MPC) de un eje con restricciones: par |u| <= 0.01 N m (duro, caja) y velocidad |w| <= 0.08 rad/s
(penalizacion cuadratica exacta aproximada). Modelo de doble integrador discretizado a 1 s (Iz = 0.30 kg m^2 SINTETICO), horizonte N = 40,
coste cuadratico; QP condensado resuelto con gradiente proyectado acelerado (FISTA, 1500 iteraciones por solucion). Se compara con un PD saturado de
igual wn = 0.2 rad/s, zeta = 0.9. Maniobra de 60 deg desde el reposo; 150 s. Sin ruido ni retardo (SINTETICO)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *

IZ, UMAX, WMAX, DT, N = 0.30, 0.01, 0.08, 1.0, 40
AMAX = UMAX / IZ
QT, QW, R, PEN = 1.0, 20.0, 50.0, 3000.0


def matrices():
    Gt = np.zeros((N, N)); Gw = np.zeros((N, N))
    for k in range(N):
        for j in range(k + 1):
            Gw[k, j] = DT
            Gt[k, j] = DT * DT * (k - j + 0.5)
    return Gt, Gw


GT, GW = matrices()
LIP = 2 * (QT * np.linalg.norm(GT, 2) ** 2 + QW * np.linalg.norm(GW, 2) ** 2 + R) + 2 * PEN * np.linalg.norm(GW, 2) ** 2


def coste_grad(a, th0, w0, ref):
    th = th0 + np.arange(1, N + 1) * DT * w0 + GT @ a
    w = w0 + GW @ a
    ex = np.maximum(0, np.abs(w) - WMAX) * np.sign(w)
    J = QT * np.sum((th - ref) ** 2) + QW * np.sum(w ** 2) + R * np.sum(a ** 2) + PEN * np.sum(ex ** 2)
    g = 2 * QT * GT.T @ (th - ref) + 2 * QW * GW.T @ w + 2 * R * a + 2 * PEN * GW.T @ ex
    return J, g


def resolver(th0, w0, ref, a0=None, it=600):
    a = np.zeros(N) if a0 is None else a0.copy()
    y = a.copy(); t = 1.0
    for _ in range(it):
        J, g = coste_grad(y, th0, w0, ref)
        an = np.clip(y - g / LIP, -AMAX, AMAX)
        tn = (1 + math.sqrt(1 + 4 * t * t)) / 2
        y = an + (t - 1) / tn * (an - a)
        a, t = an, tn
    J, g = coste_grad(a, th0, w0, ref)
    gm = np.linalg.norm(a - np.clip(a - g / LIP, -AMAX, AMAX)) * LIP
    return a, J, gm


def lazo(modo, T=150, ref=60 * D2R):
    th, w = 0.0, 0.0
    kp, kd = IZ * 0.2 ** 2, 2 * 0.9 * 0.2 * IZ
    a_prev = None; tmax = 0.0; wpk = 0.0; t_in = None
    for k in range(int(T / DT)):
        if modo == "mpc":
            a, _, _ = resolver(th, w, ref, a_prev, 1500)
            a_prev = np.concatenate([a[1:], a[-1:]])
            u = IZ * a[0]
        else:
            u = float(np.clip(-kp * (th - ref) - kd * w, -UMAX, UMAX))
        tmax = max(tmax, abs(u))
        acc = u / IZ
        th += w * DT + 0.5 * acc * DT * DT
        w += acc * DT
        wpk = max(wpk, abs(w))
        if t_in is None and abs(th - ref) < 0.5 * D2R:
            t_in = (k + 1) * DT
    return dict(t_in=t_in, tmax=tmax, wpk=wpk, th_fin=th * R2D)


def calcular():
    ref = 60 * D2R
    a1, J1, gm1 = resolver(0.0, 0.0, ref, None, 1500)
    a2, J2, _ = resolver(0.0, 0.0, ref, None, 15000)
    return dict(mpc=lazo("mpc"), pd=lazo("pd"), gm=gm1, dif=float(np.max(np.abs(a1 - a2))) / AMAX, J=J1, J2=J2, Lip=LIP, amax=AMAX,
                pen_viol=float(np.max(np.abs(GW @ a1)) ))


def main():
    banner("B87-C21 MPC | SINTETICO: doble integrador (Iz = 0.30), N = 40 a 1 s, |u| <= 0.01 N m, |w| <= 0.08 rad/s, giro de 60 deg")
    d = calcular(); m, p = d['mpc'], d['pd']
    print(f"QP condensado de {N} variables: constante de Lipschitz = {d['Lip']:.1f} ; aceleracion maxima = {d['amax']:.4f} rad/s^2")
    print(f"convergencia: |a(1500 it) - a(15000 it)| maximo = {d['dif']*100:.3f} % del limite ; residuo del gradiente proyectado = {d['gm']:.2e}")
    print(f"MPC: entra a 0.5 deg en {m['t_in']:.0f} s ; par maximo = {m['tmax']*1e3:.3f} mN m ; velocidad pico = {m['wpk']:.4f} rad/s ({m['wpk']*R2D:.2f} deg/s)")
    print(f"PD saturado: entra a 0.5 deg en {p['t_in']:.0f} s ; par maximo = {p['tmax']*1e3:.3f} mN m ; velocidad pico = {p['wpk']:.4f} rad/s ({p['wpk']*R2D:.2f} deg/s)")
    print(f"limite de velocidad = {WMAX} rad/s ({WMAX*R2D:.2f} deg/s)")
    assert m['tmax'] <= UMAX + 1e-12 and m['wpk'] < WMAX * 1.05 and p['wpk'] > WMAX * 1.05
    assert d['dif'] < 0.01 and m['t_in'] is not None
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
