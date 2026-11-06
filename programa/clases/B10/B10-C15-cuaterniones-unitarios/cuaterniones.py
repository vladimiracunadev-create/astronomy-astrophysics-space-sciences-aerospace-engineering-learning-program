#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C15: cuaterniones unitarios (escalar primero, Hamilton).

Datos: SINTETICOS (ejes y angulos inventados).
Modelo: q = (q0, q1, q2, q3) = (cos(t/2), sin(t/2) u); producto de Hamilton;
rotacion activa v' = q v q* (v como cuaternion puro); matriz R(q).
Convencion: escalar primero (como SPICE), rotacion ACTIVA de vectores. La
rotacion de coordenadas de SPICE corresponde al conjugado: se verifica con
R(q*) = R(q)^T.
Supuestos: aritmetica doble; |q| = 1. Validez: renormalizar tras muchos pasos.
Tolerancia: 1e-12 en identidades.
"""
from __future__ import annotations
import platform
import numpy as np


def qmul(p, q):
    p0, p1, p2, p3 = p
    q0, q1, q2, q3 = q
    return np.array([
        p0 * q0 - p1 * q1 - p2 * q2 - p3 * q3,
        p0 * q1 + p1 * q0 + p2 * q3 - p3 * q2,
        p0 * q2 - p1 * q3 + p2 * q0 + p3 * q1,
        p0 * q3 + p1 * q2 - p2 * q1 + p3 * q0])


def conj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def desde_eje_angulo(u, t):
    u = np.asarray(u, float) / np.linalg.norm(u)
    return np.concatenate([[np.cos(t / 2)], np.sin(t / 2) * u])


def a_matriz(q):
    q0, q1, q2, q3 = q
    return np.array([
        [1 - 2 * (q2 ** 2 + q3 ** 2), 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)],
        [2 * (q1 * q2 + q0 * q3), 1 - 2 * (q1 ** 2 + q3 ** 2), 2 * (q2 * q3 - q0 * q1)],
        [2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 1 - 2 * (q1 ** 2 + q2 ** 2)]])


def desde_matriz(R):
    tr = np.trace(R)
    cand = [(1 + tr), (1 + 2 * R[0, 0] - tr), (1 + 2 * R[1, 1] - tr), (1 + 2 * R[2, 2] - tr)]
    k = int(np.argmax(cand))
    if k == 0:
        q0 = 0.5 * np.sqrt(cand[0])
        q = np.array([q0, (R[2, 1] - R[1, 2]) / (4 * q0), (R[0, 2] - R[2, 0]) / (4 * q0), (R[1, 0] - R[0, 1]) / (4 * q0)])
    elif k == 1:
        q1 = 0.5 * np.sqrt(cand[1])
        q = np.array([(R[2, 1] - R[1, 2]) / (4 * q1), q1, (R[0, 1] + R[1, 0]) / (4 * q1), (R[0, 2] + R[2, 0]) / (4 * q1)])
    elif k == 2:
        q2 = 0.5 * np.sqrt(cand[2])
        q = np.array([(R[0, 2] - R[2, 0]) / (4 * q2), (R[0, 1] + R[1, 0]) / (4 * q2), q2, (R[1, 2] + R[2, 1]) / (4 * q2)])
    else:
        q3 = 0.5 * np.sqrt(cand[3])
        q = np.array([(R[1, 0] - R[0, 1]) / (4 * q3), (R[0, 2] + R[2, 0]) / (4 * q3), (R[1, 2] + R[2, 1]) / (4 * q3), q3])
    return q / np.linalg.norm(q)


def rotar(q, v):
    return qmul(qmul(q, np.concatenate([[0.0], v])), conj(q))[1:]


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def Rx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def slerp(p, q, t):
    d = p @ q
    if d < 0:
        q, d = -q, -d
    om = np.arccos(np.clip(d, -1, 1))
    if om < 1e-12:
        return p
    return (np.sin((1 - t) * om) * p + np.sin(t * om) * q) / np.sin(om)


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    qz = desde_eje_angulo([0, 0, 1], np.radians(90))
    qx = desde_eje_angulo([1, 0, 0], np.radians(90))
    print("q(z,90) =", qz.round(6), "| q(x,90) =", qx.round(6))
    v = np.array([1.0, 2.0, 3.0])
    print("rotar (z,90) (1,2,3) =", rotar(qz, v).round(9), "| matriz:", (Rz(np.pi / 2) @ v).round(9))
    assert np.allclose(rotar(qz, v), Rz(np.pi / 2) @ v, atol=1e-12)
    assert np.allclose(a_matriz(qz), Rz(np.pi / 2), atol=1e-12)
    # composicion: q_total = qz (x) qx representa R_z R_x (se aplica primero qx)
    qt = qmul(qz, qx)
    print("qz (x) qx =", qt.round(6), "| escalar = cos(60) =", round(float(np.cos(np.radians(60))), 6))
    assert np.allclose(a_matriz(qt), Rz(np.pi / 2) @ Rx(np.pi / 2), atol=1e-12)
    assert not np.allclose(qmul(qz, qx), qmul(qx, qz))
    # q y -q
    assert np.allclose(a_matriz(-qt), a_matriz(qt), atol=1e-12)
    # conjugado = inversa = transpuesta
    assert np.allclose(a_matriz(conj(qt)), a_matriz(qt).T, atol=1e-12)
    assert np.allclose(qmul(qt, conj(qt)), [1, 0, 0, 0], atol=1e-12)
    # ida y vuelta matriz <-> cuaternion en muchos casos
    rng = np.random.default_rng(15)
    peor = 0.0
    for _ in range(2000):
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        R = a_matriz(q)
        q2 = desde_matriz(R)
        assert np.allclose(R, a_matriz(q2), atol=1e-12)
        assert min(np.abs(q - q2).max(), np.abs(q + q2).max()) < 1e-10
        peor = max(peor, np.abs(R.T @ R - np.eye(3)).max())
    print(f"2000 ida y vuelta matriz<->cuaternion: error maximo de ortogonalidad {peor:.2e}")
    # slerp: la mitad del camino da la mitad del angulo
    p0 = np.array([1.0, 0, 0, 0])
    q1 = desde_eje_angulo([0, 1, 0], np.radians(100))
    qm = slerp(p0, q1, 0.5)
    ang = 2 * np.degrees(np.arccos(qm[0]))
    print(f"slerp a mitad de camino: angulo = {ang:.9f} grados (esperado 50)")
    assert abs(ang - 50.0) < 1e-9
    # deriva de norma y renormalizacion
    q = desde_eje_angulo([1, 1, 1], 1e-3)
    acc = np.array([1.0, 0, 0, 0])
    for _ in range(1_000_000):
        acc = qmul(q, acc)
    print(f"tras 1e6 productos: |q| - 1 = {np.linalg.norm(acc) - 1:.2e}; tras renormalizar: {np.linalg.norm(acc / np.linalg.norm(acc)) - 1:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
