#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C20: cinematica de orientacion con cuaterniones.

Datos: SINTETICOS. Velocidad angular constante en ejes del cuerpo
w = 0.1 rad/s * (1,1,1)/sqrt(3); duracion 60 s (giro total 6 rad).
Modelo: q' = 1/2 q (x) (0, w) (cuaternion escalar-primero, rotacion activa
cuerpo -> inercial, w en el cuerpo). Para w constante el eje es fijo y la
solucion exacta es q(t) = (cos(|w| t/2), sin(|w| t/2) w/|w|).
Integradores: Euler explicito, Euler + renormalizacion, RK4 + renormalizacion.
Supuestos: w conocida sin ruido. Validez: ilustrativa.
Tolerancia: error de RK4 con paso 0.1 s < 1e-8 (angulo).
"""
from __future__ import annotations
import platform
import numpy as np


def qmul(p, q):
    p0, p1, p2, p3 = p
    q0, q1, q2, q3 = q
    return np.array([p0 * q0 - p1 * q1 - p2 * q2 - p3 * q3,
                     p0 * q1 + p1 * q0 + p2 * q3 - p3 * q2,
                     p0 * q2 - p1 * q3 + p2 * q0 + p3 * q1,
                     p0 * q3 + p1 * q2 - p2 * q1 + p3 * q0])


def qdot(q, w):
    return 0.5 * qmul(q, np.concatenate([[0.0], w]))


def exacta(w, t):
    n = np.linalg.norm(w)
    return np.concatenate([[np.cos(n * t / 2)], np.sin(n * t / 2) * w / n])


def angulo(q1, q2):
    """Angulo de la rotacion relativa (rad), estable para angulos pequenos."""
    q1 = q1 / np.linalg.norm(q1)
    q2 = q2 / np.linalg.norm(q2)
    c = np.array([q1[0], -q1[1], -q1[2], -q1[3]])
    r = qmul(c, q2)
    return 2 * np.arctan2(np.linalg.norm(r[1:]), abs(r[0]))


def integrar(w, T, h, metodo):
    q = np.array([1.0, 0, 0, 0])
    for _ in range(int(round(T / h))):
        if metodo == "euler":
            q = q + h * qdot(q, w)
        elif metodo == "euler_n":
            q = q + h * qdot(q, w)
            q /= np.linalg.norm(q)
        else:
            k1 = qdot(q, w)
            k2 = qdot(q + 0.5 * h * k1, w)
            k3 = qdot(q + 0.5 * h * k2, w)
            k4 = qdot(q + h * k3, w)
            q = q + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            q /= np.linalg.norm(q)
    return q


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    w = 0.1 * np.ones(3) / np.sqrt(3)
    T = 60.0
    qe = exacta(w, T)
    print("q exacta (t=60 s) =", qe.round(6), "| angulo total =", round(float(2 * np.arccos(qe[0])), 6), "rad")
    for h in (0.5, 0.1, 0.01):
        for met in ("euler", "euler_n", "rk4"):
            q = integrar(w, T, h, met)
            print(f"h = {h:5.2f} s  {met:8s}: |q| - 1 = {np.linalg.norm(q) - 1: .3e}  error angular = {angulo(q, qe):.3e} rad")
    q = integrar(w, T, 0.1, "rk4")
    assert angulo(q, qe) < 1e-6
    assert angulo(integrar(w, T, 0.1, "euler_n"), qe) > 1e-5
    # consistencia: w = 2 q* (x) q'
    qq = exacta(w, 10.0)
    h = 1e-6
    qd = (exacta(w, 10.0 + h) - exacta(w, 10.0 - h)) / (2 * h)
    qc = np.array([qq[0], -qq[1], -qq[2], -qq[3]])
    w_rec = 2 * qmul(qc, qd)[1:]
    print("w recuperada de q y q' =", w_rec.round(8), "| w =", w.round(8))
    assert np.allclose(w_rec, w, atol=1e-8)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
