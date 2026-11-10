#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C02: registro rigido entre dos sensores (Kabsch/SVD) con datos SINTETICOS.

Todo es sintetico (semilla 103): la pose verdadera sensor -> base del robot, los puntos de correspondencia y el ruido.
Convencion: p_base = R p_sensor + t. Unidades: m y grados. Sistema: ejes derecha-mano; el sensor en m, la base del robot en m.
Pose verdadera ILUSTRATIVA: rotacion Rz(25 grados) Ry(-10 grados) Rx(5 grados), traslacion (0.35, -0.10, 0.80) m.
Puntos: N en un volumen de 1 m x 1 m x 1 m a 1-3 m del sensor; ruido gaussiano isotropo sigma en el sensor.
Metodo: Kabsch (centrado, SVD de la covarianza cruzada, correccion de reflexion). Verificacion: error contra la verdad;
sin ruido el error debe ser < 1e-9; con ruido se compara con la ley de escala sigma/sqrt(N); con puntos colineales la
rotacion alrededor de la recta no es observable. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np


def rot(ax, ay, az):
    cx, sx, cy, sy, cz, sz = np.cos(ax), np.sin(ax), np.cos(ay), np.sin(ay), np.cos(az), np.sin(az)
    rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return rz @ ry @ rx


R_V = rot(np.radians(5), np.radians(-10), np.radians(25))
T_V = np.array([0.35, -0.10, 0.80])


def kabsch(a, b):
    """Devuelve R, t tales que b ~ R a + t."""
    ca, cb = a.mean(axis=0), b.mean(axis=0)
    h = (a - ca).T @ (b - cb)
    u, _, vt = np.linalg.svd(h)
    d = np.sign(np.linalg.det(vt.T @ u.T))
    r = vt.T @ np.diag([1, 1, d]) @ u.T
    return r, cb - r @ ca


def angulo(r):
    w = np.array([r[2, 1] - r[1, 2], r[0, 2] - r[2, 0], r[1, 0] - r[0, 1]]) / 2
    return np.degrees(np.arctan2(np.linalg.norm(w), (np.trace(r) - 1) / 2))


def puntos(rng, n):
    return rng.uniform([-0.5, -0.5, 1.0], [0.5, 0.5, 3.0], size=(n, 3))


def ensayo(rng, n, sigma):
    a = puntos(rng, n)
    b = a @ R_V.T + T_V
    a_ruidoso = a + rng.normal(0, sigma, a.shape)
    r, t = kabsch(a_ruidoso, b)
    return angulo(r @ R_V.T), np.linalg.norm(t - T_V) * 1000


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    rng = np.random.default_rng(103)
    print("DATOS SINTETICOS (semilla 103): pose verdadera ILUSTRATIVA Rz(25)Ry(-10)Rx(5) grados, t = (0.35, -0.10, 0.80) m")
    # 1. Sin ruido
    a = puntos(rng, 12)
    r0, t0 = kabsch(a, a @ R_V.T + T_V)
    e0 = max(angulo(r0 @ R_V.T), np.linalg.norm(t0 - T_V))
    print(f"Sin ruido (N = 12): error de rotacion = {angulo(r0 @ R_V.T):.2e} grados, de traslacion = {np.linalg.norm(t0 - T_V):.2e} m")
    # 2. Caso base
    sig = 0.002
    a = puntos(rng, 12)
    b = a @ R_V.T + T_V
    an = a + rng.normal(0, sig, a.shape)
    r1, t1 = kabsch(an, b)
    res = np.sqrt(np.mean(np.sum((an @ r1.T + t1 - b) ** 2, axis=1)))
    er, et = angulo(r1 @ R_V.T), np.linalg.norm(t1 - T_V)
    print(f"Caso base (N = 12, sigma = 2 mm): rotacion {er:.4f} grados, traslacion {et*1000:.2f} mm, residuo RMS {res*1000:.2f} mm")
    # 3. Brazo de palanca
    print("Error de posicion de un punto a distancia d del origen del sensor (caso base):")
    for d in (1.0, 5.0, 10.0):
        p = np.array([0.0, 0.0, d])
        err = np.linalg.norm((r1 @ p + t1) - (R_V @ p + T_V))
        print(f"  d = {d:4.1f} m: {err*1000:7.2f} mm")
    # 4. Monte Carlo
    print("Monte Carlo (500 repeticiones): rotacion media [grados] / traslacion media [mm]")
    print("  N \\ sigma     1 mm            2 mm            5 mm")
    tabla = {}
    for n in (4, 8, 16, 32):
        fila = []
        for sg in (0.001, 0.002, 0.005):
            r = np.array([ensayo(np.random.default_rng(5000 + s), n, sg) for s in range(500)])
            tabla[(n, sg)] = r.mean(axis=0)
            fila.append(f"{r[:,0].mean():7.4f}/{r[:,1].mean():6.2f}")
        print(f"  {n:3d}        " + "      ".join(fila))
    c416 = tabla[(4, 0.002)][0] / tabla[(16, 0.002)][0]
    cociente = tabla[(16, 0.002)][0] / tabla[(32, 0.002)][0]
    print(f"Cociente de rotacion N = 4 frente a N = 16 (sigma = 2 mm) = {c416:.3f} ; sqrt(16/4) = 2.000 (muestras pequenas: peor que la ley)")
    print(f"Cociente de rotacion N = 16 frente a N = 32 (sigma = 2 mm) = {cociente:.3f} ; esperado sqrt(32/16) = 1.414")
    # 5. Degeneracion colineal
    print("Puntos casi colineales (a lo largo de z, 8 puntos, sigma = 2 mm), 200 repeticiones:")
    er_col = []
    for s in range(200):
        g = np.random.default_rng(9000 + s)
        a = np.c_[np.zeros(8), np.zeros(8), g.uniform(1.0, 3.0, 8)]
        b = a @ R_V.T + T_V
        r, _ = kabsch(a + g.normal(0, 0.002, a.shape), b)
        er_col.append(angulo(r @ R_V.T))
    print(f"  error de rotacion medio = {np.mean(er_col):.2f} grados (no observable alrededor de la recta)")
    assert e0 < 1e-9
    assert 1.25 < cociente < 1.6
    assert np.mean(er_col) > 10 * er
    assert abs(np.linalg.det(r1) - 1) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
