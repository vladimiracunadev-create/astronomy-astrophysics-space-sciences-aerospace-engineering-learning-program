#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B87-C02: conversiones entre matriz de actitud, Euler 3-2-1, cuaternion y eje-angulo; bloqueo de cardan.
Convencion: v_B = A v_I, cuaternion con parte escalar al final. Casos SINTETICOS (semilla 20260511)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from adcs_comun import *


def calcular():
    rng = np.random.default_rng(20260511)
    err_q = err_e = err_ax = 0.0
    for _ in range(2000):
        q = random_q(rng)
        A = A_of_q(q)
        err_q = max(err_q, np.abs(A_of_q(q_of_A(A)) - A).max())
        y, p, r = euler321_of_A(A)
        err_e = max(err_e, np.abs(A_euler321(y, p, r) - A).max())
        n, ang = q_to_axis_angle(q)
        err_ax = max(err_ax, np.abs(A_of_q(q_from_axis_angle(n, ang)) - A).max())
    # composicion: A(q (x) p) = A(q) A(p)
    q = random_q(rng); p = random_q(rng)
    comp = np.abs(A_of_q(qmul(q, p)) - A_of_q(q) @ A_of_q(p)).max()
    # doble cobertura
    dc = np.abs(A_of_q(q) - A_of_q(-q)).max()
    # ejemplo conductor: yaw 30, pitch 20, roll 10 grados
    A0 = A_euler321(30 * D2R, 20 * D2R, 10 * D2R)
    q0 = q_of_A(A0)
    n0, a0 = q_to_axis_angle(q0)
    # bloqueo de cardan: pitch -> 90 deg, sensibilidad de (yaw, roll) a una rotacion de 1e-6 rad
    sens = []
    for pit in (0.0, 80.0, 89.0, 89.99):
        A1 = A_euler321(30 * D2R, pit * D2R, 10 * D2R)
        dA = A1 @ Rx(1e-6).T  # rotacion de 1e-6 rad alrededor de un eje inercial
        y1, p1, r1 = euler321_of_A(dA)
        sens.append((pit, max(abs(y1 - 30 * D2R), abs(r1 - 10 * D2R)) / 1e-6))
    # velocidad angular: dq/dt = 0.5 [w;0] (x) q vs diferencias finitas de A
    w = np.array([0.1, -0.2, 0.3]); e = 1e-7
    qd = 0.5 * qmul(np.concatenate([w, [0]]), q)
    v = np.array([1.0, 2.0, 3.0])
    cin = np.abs(((A_of_q(qnormalize(q + e * qd)) - A_of_q(q)) / e) @ v + np.cross(w, A_of_q(q) @ v)).max()
    return dict(err_q=err_q, err_e=err_e, err_ax=err_ax, comp=comp, dc=dc, q0=q0, ang0=a0 * R2D, n0=n0,
                A0=A0, sens=sens, cin=cin, qn0=np.linalg.norm(q0))


def main():
    banner("B87-C02 representaciones de orientacion | 2000 casos SINTETICOS (semilla 20260511)")
    d = calcular()
    print("Ejemplo conductor: yaw 30 deg, pitch 20 deg, roll 10 deg (secuencia 3-2-1, I -> B)")
    print("A =")
    for fila in d['A0']:
        print("   [" + "  ".join(f"{x: .6f}" for x in fila) + "]")
    print(f"q = [{d['q0'][0]:.6f} {d['q0'][1]:.6f} {d['q0'][2]:.6f} {d['q0'][3]:.6f}] ; |q| = {d['qn0']:.6f}")
    print(f"eje = [{d['n0'][0]:.5f} {d['n0'][1]:.5f} {d['n0'][2]:.5f}] ; angulo = {d['ang0']:.4f} deg")
    print(f"error maximo de ida y vuelta A->q->A = {d['err_q']:.2e} ; A->Euler->A = {d['err_e']:.2e} ; q->eje-angulo->A = {d['err_ax']:.2e}")
    print(f"composicion A(q(x)p) - A(q)A(p): {d['comp']:.2e} ; doble cobertura A(q) - A(-q): {d['dc']:.2e}")
    print(f"cinematica dq/dt = 0.5[w;0](x)q frente a diferencias finitas: {d['cin']:.2e}")
    print("Sensibilidad de (yaw, roll) a una rotacion de 1e-6 rad (veces):")
    for pit, s in d['sens']:
        print(f"  pitch = {pit:6.2f} deg -> {s:12.2f}")
    assert d['err_q'] < 1e-14 and d['err_e'] < 1e-12 and d['err_ax'] < 1e-14
    assert d['comp'] < 1e-14 and d['dc'] < 1e-15 and d['cin'] < 1e-5
    assert d['sens'][-1][1] > 1000 * d['sens'][0][1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
