#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C03: mecanizacion strapdown con cuaterniones (actitud, velocidad, posicion) en un sistema inercial.

Datos: SINTETICOS e ILUSTRATIVOS; ninguna medicion real. Sin semilla aleatoria (trayectoria determinista).
Sistema de referencia: inercial local (sin rotacion terrestre, gravedad uniforme g = 9.80665 m/s2 hacia -z, valor estandar del NIST consultado);
cuerpo con ejes x,y,z; cuaternion q = (w, x, y, z) que rota del cuerpo al sistema de navegacion. Unidades SI, angulos en rad.
Trayectoria: el cuerpo gira a w = (0, 0, 0.5) rad/s (constante, alrededor de z) durante 20 s y mide una fuerza especifica en el cuerpo
f_b = (1.0, 0, g) m/s2 (empuje de 1 m/s2 a lo largo de su eje x y sosten contra la gravedad).
Mecanizacion: q_{k+1} = q_k (x) exp(0.5 w dt) (cuaternion exacto de rotacion para w constante) y la comparacion con Euler de primer orden
q_{k+1} = q_k + 0.5 q_k (x) (0, w) dt, normalizado. v' = R(q) f_b + g_vec ; p' = v.
Segunda via: solucion analitica del cuerpo que gira a velocidad constante con empuje fijo en el cuerpo. Tolerancia: 1e-9 (exponencial), 1e-3 (Euler, dt = 0.01 s).
"""
from __future__ import annotations
import math, platform

G = 9.80665


def qmul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return (w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2)


def qnorm(q):
    n = math.sqrt(sum(c * c for c in q))
    return tuple(c / n for c in q)


def qexp(w, dt):
    ang = math.sqrt(sum(c * c for c in w)) * dt
    if ang < 1e-15:
        return (1.0, 0.5 * w[0] * dt, 0.5 * w[1] * dt, 0.5 * w[2] * dt)
    u = [c * dt / ang for c in w]
    s = math.sin(0.5 * ang)
    return (math.cos(0.5 * ang), u[0] * s, u[1] * s, u[2] * s)


def rot(q, v):
    w, x, y, z = q
    r = [[1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
         [2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
         [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)]]
    return tuple(sum(r[i][j] * v[j] for j in range(3)) for i in range(3))


W = (0.0, 0.0, 0.5)
F_B = (1.0, 0.0, G)
T = 20.0


def integrar(dt, metodo):
    q = (1.0, 0.0, 0.0, 0.0)
    v = [0.0, 0.0, 0.0]
    p = [0.0, 0.0, 0.0]
    n = int(round(T / dt))
    for _ in range(n):
        a_n = rot(qmul(q, qexp(W, 0.5 * dt)) if metodo == "exp" else q, F_B)
        a = (a_n[0], a_n[1], a_n[2] - G)
        # 'exp' usa la actitud del punto medio del paso (segundo orden); 'euler' la del inicio (primer orden)
        for i in range(3):
            p[i] += v[i] * dt + 0.5 * a[i] * dt * dt
            v[i] += a[i] * dt
        if metodo == "exp":
            q = qmul(q, qexp(W, dt))
        else:
            dq = qmul(q, (0.0, W[0], W[1], W[2]))
            q = qnorm(tuple(q[i] + 0.5 * dq[i] * dt for i in range(4)))
    return q, tuple(v), tuple(p)


def analitico():
    w = W[2]
    psi = w * T
    # a_n = (cos(w t), sin(w t)) ; v = (sin/w, (1-cos)/w) ; p = ((1-cos)/w^2 , (t - sin/w)/w)
    v = (math.sin(psi) / w, (1.0 - math.cos(psi)) / w, 0.0)
    p = ((1.0 - math.cos(psi)) / (w * w), (T - math.sin(psi) / w) / w, 0.0)
    q = (math.cos(0.5 * psi), 0.0, 0.0, math.sin(0.5 * psi))
    return q, v, p


def err(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    qa, va, pa = analitico()
    print(f"Analitico (SINTETICO): psi = {W[2] * T:.3f} rad, v = ({va[0]:.5f}, {va[1]:.5f}, {va[2]:.1f}) m/s, p = ({pa[0]:.4f}, {pa[1]:.4f}, {pa[2]:.1f}) m")
    print(" metodo   dt [s]   error posicion [m]   error velocidad [m/s]   error actitud |q-q_a|   norma de q")
    res = {}
    for metodo in ("exp", "euler"):
        for dt in (0.1, 0.01):
            q, v, p = integrar(dt, metodo)
            ea = err(q, qa)
            if q[0] * qa[0] < 0:
                ea = err(tuple(-c for c in q), qa)
            res[(metodo, dt)] = (err(p, pa), err(v, va), ea)
            nq = math.sqrt(sum(c * c for c in q))
            print(f"{metodo:7s} {dt:8.3f} {err(p, pa):20.3e} {err(v, va):23.3e} {ea:21.3e} {nq:12.9f}")
    # La gravedad: una IMU en caida libre (f = 0) no mide nada, aunque acelere
    q = (1.0, 0.0, 0.0, 0.0)
    a_n = rot(q, (0.0, 0.0, 0.0))
    print(f"Caida libre: f_b = 0 -> a_z = f_z - g = {a_n[2] - G:.5f} m/s2 (la IMU mide fuerza especifica, no aceleracion)")
    # Rotacion de 360 grados: el cuaternion regresa a -q (doble cobertura)
    qq = (1.0, 0.0, 0.0, 0.0)
    for _ in range(int(round(2.0 * math.pi / 0.5 / 0.01))):
        qq = qmul(qq, qexp(W, 0.01))
    print(f"Tras una vuelta completa (psi = 2 pi): q = ({qq[0]:.6f}, {qq[1]:.6f}, {qq[2]:.6f}, {qq[3]:.6f}) -> -q es la misma rotacion")
    assert res[("exp", 0.01)][2] < 1e-9
    assert res[("exp", 0.01)][0] < 5e-3 and res[("exp", 0.1)][0] > res[("exp", 0.01)][0]
    assert res[("euler", 0.01)][2] < 1e-3
    assert res[("euler", 0.1)][2] > 5 * res[("euler", 0.01)][2]
    assert qq[0] < -0.999
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
