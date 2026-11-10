#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Biblioteca comun de los laboratorios del bloque B87 (sensores y control de actitud).

Unidades: SI (m, s, kg, rad, T, N m); los angulos se imprimen en grados cuando se indica.
Convenciones (todas EXPLICITAS):
  * Cuaternion q = [qx, qy, qz, qw] (parte escalar al final), norma 1. q lleva vectores del sistema inercial I
    al sistema del cuerpo B:  v_B = A(q) v_I  con A(q) = (qw^2 - |qv|^2) I + 2 qv qv^T - 2 qw [qv x].
  * Producto q (x) p tal que A(q (x) p) = A(q) A(p) (convencion de Markley, parte escalar al final).
  * Cinematica: dq/dt = 0.5 [w; 0] (x) q, con w la velocidad angular del cuerpo respecto de I, expresada en B.
  * Dinamica con ruedas: I dw/dt = -w x (I w + h) - u + tau_ext ; dh/dt = u (u: par sobre las ruedas).
  * Sistema de referencia inercial I: ejes de EJEMPLO (no J2000 real); orbita circular de dos cuerpos.
Constantes ADOPTADAS como valores de ejemplo (no consultadas en una fuente concreta; ver CLASE):
  radio terrestre 6378137 m, mu terrestre 3.986004418e14 m3/s2.
Todo dato es SINTETICO (semilla fija); no hay datos medidos de ninguna mision.
"""
from __future__ import annotations
import math
import numpy as np

RE = 6378137.0
MU_E = 3.986004418e14
D2R = math.pi / 180.0
R2D = 180.0 / math.pi


def info():
    return f"Python {__import__('platform').python_version()} | numpy {np.__version__}"


def skew(v):
    return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]], float)


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def qmul(q, p):
    qv, q4, pv, p4 = q[:3], q[3], p[:3], p[3]
    return np.concatenate([p4 * qv + q4 * pv - np.cross(qv, pv), [q4 * p4 - qv @ pv]])


def qconj(q):
    return np.array([-q[0], -q[1], -q[2], q[3]])


def qnormalize(q):
    q = np.asarray(q, float)
    return q / np.linalg.norm(q)


def A_of_q(q):
    qv, q4 = q[:3], q[3]
    return (q4 * q4 - qv @ qv) * np.eye(3) + 2 * np.outer(qv, qv) - 2 * q4 * skew(qv)


def q_of_A(A):
    """Metodo de Shepperd: cuaternion (parte escalar al final) con A(q) = A."""
    tr = np.trace(A)
    cand = [tr, A[0, 0], A[1, 1], A[2, 2]]
    k = int(np.argmax(cand))
    if k == 0:
        q4 = 0.5 * math.sqrt(1 + tr)
        q = np.array([A[1, 2] - A[2, 1], A[2, 0] - A[0, 2], A[0, 1] - A[1, 0]]) / (4 * q4)
        q = np.concatenate([q, [q4]])
    else:
        i = k - 1
        j, l = (i + 1) % 3, (i + 2) % 3
        s = math.sqrt(1 + A[i, i] - A[j, j] - A[l, l])
        q = np.zeros(4)
        q[i] = 0.5 * s
        q[j] = (A[i, j] + A[j, i]) / (2 * s)
        q[l] = (A[i, l] + A[l, i]) / (2 * s)
        q[3] = (A[j, l] - A[l, j]) / (2 * s)
    q = qnormalize(q)
    return q if q[3] >= 0 else -q


def q_from_axis_angle(axis, ang):
    a = unit(axis)
    return np.concatenate([a * math.sin(ang / 2), [math.cos(ang / 2)]])


def q_to_axis_angle(q):
    q = q if q[3] >= 0 else -q
    ang = 2 * math.atan2(np.linalg.norm(q[:3]), q[3])
    n = np.linalg.norm(q[:3])
    return (q[:3] / n if n > 1e-15 else np.array([1.0, 0, 0])), ang


def rotvec_to_q(phi):
    phi = np.asarray(phi, float)
    n = np.linalg.norm(phi)
    if n < 1e-12:
        return qnormalize(np.concatenate([phi / 2, [1.0]]))
    return q_from_axis_angle(phi / n, n)


def ang_between(qa, qb):
    """Angulo de rotacion (rad) entre dos actitudes."""
    d = qmul(qa, qconj(qb))
    return 2 * math.atan2(np.linalg.norm(d[:3]), abs(d[3]))


def Rx(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, s], [0, -s, c]])


def Ry(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, -s], [0, 1, 0], [s, 0, c]])


def Rz(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, s, 0], [-s, c, 0], [0, 0, 1]])


def A_euler321(yaw, pitch, roll):
    """A = Rx(roll) Ry(pitch) Rz(yaw): secuencia 3-2-1 (pasiva), I -> B."""
    return Rx(roll) @ Ry(pitch) @ Rz(yaw)


def euler321_of_A(A):
    pitch = -math.asin(max(-1.0, min(1.0, A[0, 2])))
    yaw = math.atan2(A[0, 1], A[0, 0])
    roll = math.atan2(A[1, 2], A[2, 2])
    return yaw, pitch, roll


def deriv(q, w, h, u, tau, I):
    qd = 0.5 * qmul(np.concatenate([w, [0.0]]), q)
    wd = np.linalg.solve(I, -np.cross(w, I @ w + h) - u + tau)
    return qd, wd, u


def step(q, w, h, u, tau, I, dt):
    """RK4 de (q, w, h) con u y tau constantes en el paso. Renormaliza q."""
    def f(q_, w_, h_):
        return deriv(q_, w_, h_, u, tau, I)
    k1 = f(q, w, h)
    k2 = f(q + 0.5 * dt * k1[0], w + 0.5 * dt * k1[1], h + 0.5 * dt * k1[2])
    k3 = f(q + 0.5 * dt * k2[0], w + 0.5 * dt * k2[1], h + 0.5 * dt * k2[2])
    k4 = f(q + dt * k3[0], w + dt * k3[1], h + dt * k3[2])
    q = q + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    w = w + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    h = h + dt / 6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
    return qnormalize(q), w, h


# --- orbita y campo magnetico de EJEMPLO ------------------------------------------------------------
B0_T = 3.12e-5          # T, intensidad ecuatorial del dipolo SINTETICO (valor de ejemplo)
DIPOLE_TILT = 11.0 * D2R  # inclinacion del eje del dipolo respecto del eje z inercial (ejemplo)


def orbit_state(t, alt_m=500e3, inc_deg=51.6):
    a = RE + alt_m
    n = math.sqrt(MU_E / a ** 3)
    inc = inc_deg * D2R
    u = n * t
    r = a * np.array([math.cos(u), math.sin(u) * math.cos(inc), math.sin(u) * math.sin(inc)])
    return r, n


def dipole_B_inertial(r):
    m = np.array([math.sin(DIPOLE_TILT), 0.0, -math.cos(DIPOLE_TILT)])  # eje del dipolo (ejemplo)
    rn = np.linalg.norm(r)
    rh = r / rn
    return B0_T * (RE / rn) ** 3 * (3 * (m @ rh) * rh - m)


def sun_dir_inertial(t=0.0):
    """Direccion al Sol SINTETICA: fija en I (ejemplo), con elevacion de 23.4 deg sobre el plano xy."""
    e = 23.4 * D2R
    return np.array([math.cos(e), 0.0, math.sin(e)])


# --- Wahba ------------------------------------------------------------------------------------------
def wahba_svd(b, r, w=None):
    b = np.asarray(b, float); r = np.asarray(r, float)
    w = np.ones(len(b)) if w is None else np.asarray(w, float)
    Bm = sum(wi * np.outer(bi, ri) for wi, bi, ri in zip(w, b, r))
    U, S, Vt = np.linalg.svd(Bm)
    M = np.diag([1, 1, np.linalg.det(U) * np.linalg.det(Vt)])
    return U @ M @ Vt


def wahba_loss(A, b, r, w=None):
    w = np.ones(len(b)) if w is None else np.asarray(w, float)
    return 0.5 * sum(wi * np.sum((bi - A @ ri) ** 2) for wi, bi, ri in zip(w, b, r))


def triad(b1, b2, r1, r2):
    def frame(v1, v2):
        t1 = unit(v1)
        t2 = unit(np.cross(v1, v2))
        return np.column_stack([t1, t2, np.cross(t1, t2)])
    return frame(b1, b2) @ frame(r1, r2).T


def q_method(b, r, w=None):
    """Metodo q de Davenport: cuaternion (parte escalar al final) del autovalor maximo."""
    w = np.ones(len(b)) if w is None else np.asarray(w, float)
    Bm = sum(wi * np.outer(bi, ri) for wi, bi, ri in zip(w, b, r))
    S = Bm + Bm.T
    sigma = np.trace(Bm)
    z = np.array([Bm[1, 2] - Bm[2, 1], Bm[2, 0] - Bm[0, 2], Bm[0, 1] - Bm[1, 0]])
    K = np.zeros((4, 4))
    K[:3, :3] = S - sigma * np.eye(3)
    K[:3, 3] = z
    K[3, :3] = z
    K[3, 3] = sigma
    vals, vecs = np.linalg.eigh(K)
    q = vecs[:, -1]
    return q if q[3] >= 0 else -q


def noisy_unit(v, sigma, rng):
    """Perturba una direccion con error angular gaussiano de sigma (rad) por eje transversal."""
    v = unit(v)
    a = np.cross(v, [1.0, 0, 0]) if abs(v[0]) < 0.9 else np.cross(v, [0, 1.0, 0])
    a = unit(a)
    b = np.cross(v, a)
    return unit(v + sigma * (rng.standard_normal() * a + rng.standard_normal() * b))


def random_q(rng):
    return qnormalize(rng.standard_normal(4))


def inertia_example():
    """Microsatelite SINTETICO de ejemplo, kg m^2."""
    return np.diag([0.35, 0.40, 0.30])


def banner(titulo):
    print(info())
    print(titulo)
