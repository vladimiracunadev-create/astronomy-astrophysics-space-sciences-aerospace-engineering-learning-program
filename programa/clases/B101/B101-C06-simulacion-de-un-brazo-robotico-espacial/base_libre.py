#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C06: brazo planar de 2 eslabones sobre una base LIBRE (sin fuerzas externas): momento lineal y angular nulos.

Datos SINTETICOS: base 500 kg e I0 = 300 kg m2 con el hombro a 0.6 m de su centro; eslabones de 40 kg x 1.5 m y 30 kg x 1.2 m (varillas uniformes).
Se prescriben q1(t), q2(t); el giro de la base sale de H = 0 (RK4, paso 5 ms). Unidades: m, kg, rad, s. Plano de movimiento, sin gravedad.
Comprobaciones: CMasa fijo, H recalculado con velocidades por diferencias de la trayectoria, fase geometrica independiente de la velocidad.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: base libre 500 kg, eslabones 40 kg x 1.5 m y 30 kg x 1.2 m, plano, sin fuerzas externas")
M0, I0, b = 500.0, 300.0, 0.6
m1, l1 = 40.0, 1.5
m2, l2 = 30.0, 1.2
I1, I2 = m1 * l1**2 / 12, m2 * l2**2 / 12
Mt = M0 + m1 + m2


def u(a):
    return np.array([np.cos(a), np.sin(a)])


def posiciones(th0, q1, q2):
    """Centros de masa respecto del centro de masa del sistema, que se mantiene en el origen."""
    f1, f2 = th0 + q1, th0 + q1 + q2
    rho0 = np.zeros(2)
    rho1 = b * u(th0) + 0.5 * l1 * u(f1)
    rho2 = b * u(th0) + l1 * u(f1) + 0.5 * l2 * u(f2)
    c0 = -(m1 * rho1 + m2 * rho2) / Mt
    return c0, c0 + rho1, c0 + rho2


def punta(th0, q1, q2):
    f1, f2 = th0 + q1, th0 + q1 + q2
    c0, _, _ = posiciones(th0, q1, q2)
    return c0 + b * u(th0) + l1 * u(f1) + l2 * u(f2)


def coef_H(th0, q1, q2, h=1e-7):
    """H = A0 th0' + A1 q1' + A2 q2' (A por derivadas numericas de las posiciones)."""
    x = np.array([th0, q1, q2])
    base = posiciones(*x)
    A = np.zeros(3)
    for k in range(3):
        dx = np.zeros(3)
        dx[k] = h
        P = posiciones(*(x + dx))
        M = posiciones(*(x - dx))
        dr = [(P[j] - M[j]) / (2 * h) for j in range(3)]
        H = sum(mm * (r[0] * v[1] - r[1] * v[0]) for mm, r, v in zip((M0, m1, m2), base, dr))
        w0 = 1.0 if k == 0 else 0.0
        w1 = 1.0 if k in (0, 1) else 0.0
        w2 = 1.0
        A[k] = H + I0 * w0 + I1 * w1 + I2 * w2
    return A


def th0_punto(th0, q, qd):
    A = coef_H(th0, *q)
    return -(A[1] * qd[0] + A[2] * qd[1]) / A[0]


def suave(s):
    return 10 * s**3 - 15 * s**4 + 6 * s**5, (30 * s**2 - 60 * s**3 + 30 * s**4)


def trayectoria(vertices, T_tramo, dt=5e-3):
    """Recorre vertices de (q1, q2) con perfiles suaves; devuelve t, q(t), qd(t)."""
    ts, qs, qds = [], [], []
    t0 = 0.0
    for a, c in zip(vertices[:-1], vertices[1:]):
        n = int(round(T_tramo / dt))
        for k in range(n):
            s = k * dt / T_tramo
            f, df = suave(s)
            qs.append(a + f * (c - a))
            qds.append(df / T_tramo * (c - a))
            ts.append(t0 + k * dt)
        t0 += T_tramo
    qs.append(vertices[-1])
    qds.append(np.zeros(2))
    ts.append(t0)
    return np.array(ts), np.array(qs), np.array(qds)


def simular(vertices, T_tramo, dt=5e-3):
    ts, qs, qds = trayectoria(vertices, T_tramo, dt)
    th = 0.0
    hist = [th]
    for k in range(len(ts) - 1):
        qa, qb = qs[k], qs[k + 1]
        qm, qdm = 0.5 * (qa + qb), 0.5 * (qds[k] + qds[k + 1])
        k1 = th0_punto(th, qa, qds[k])
        k2 = th0_punto(th + 0.5 * dt * k1, qm, qdm)
        k3 = th0_punto(th + 0.5 * dt * k2, qm, qdm)
        k4 = th0_punto(th + dt * k3, qb, qds[k + 1])
        th += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        hist.append(th)
    return ts, qs, qds, np.array(hist)


def lazo(c, a):
    """Rectangulo de lado 2a (grados) en el espacio (q1, q2), recorrido en sentido horario o antihorario."""
    a = np.radians(a)
    c = np.array(c, float)
    return [c + np.array(v) * a for v in ((-1, -1), (1, -1), (1, 1), (-1, 1), (-1, -1))]


c = np.radians([40.0, 60.0])
print("Lazo rectangular cerrado en el espacio articular (q1, q2) centrado en (40, 60) grados; T = 3 s por lado")
resultados = {}
for lado in (10, 20, 30):
    V = lazo(np.degrees(c), lado)
    ts, qs, qds, th = simular(V, 3.0)
    resultados[lado] = th[-1]
    print(f"  lado {2 * lado:2d} grados: giro neto de la base = {np.degrees(th[-1]):8.4f} grados (las articulaciones vuelven a su sitio: dq = {np.abs(qs[-1] - qs[0]).max():.1e})")
comprobar(all(abs(v) > 1e-3 for v in resultados.values()), "un lazo cerrado debe dejar un giro neto en la base")
comprobar(resultados[20] / resultados[10] > 3.0 and resultados[30] / resultados[20] > 1.8, "el giro crece con el area del lazo")

V = lazo(np.degrees(c), 20)
_, _, _, th_inv = simular(V[::-1], 3.0)
print(f"Lazo invertido (lado 40): giro = {np.degrees(th_inv[-1]):8.4f} grados (opuesto al del lazo directo: {np.degrees(resultados[20]):8.4f})")
comprobar(abs(th_inv[-1] + resultados[20]) < 1e-3 * abs(resultados[20]) + 1e-9, "sentido opuesto, giro opuesto")
ts6, _, _, th6 = simular(V, 6.0)
print(f"Mismo lazo al doble de lentitud (6 s por lado): giro = {np.degrees(th6[-1]):8.4f} grados -> diferencia = {abs(th6[-1] - resultados[20]):.1e} rad")
comprobar(abs(th6[-1] - resultados[20]) < 1e-6, "la fase geometrica no depende de la velocidad")
ida = lazo(np.degrees(c), 20)[:3]
_, _, _, th_i = simular(ida + ida[::-1][1:], 3.0)
print(f"Ida y vuelta por el mismo camino: giro neto = {th_i[-1]:.1e} rad (debe ser 0)")
comprobar(abs(th_i[-1]) < 1e-6, "camino reversible sin giro neto")

# verificaciones independientes sobre la trayectoria del lazo directo
ts, qs, qds, th = simular(V, 3.0)
cm, Hs = [], []
for k in range(1, len(ts) - 1):
    r = np.array(posiciones(th[k], *qs[k]))
    cm.append(np.linalg.norm((np.array([M0, m1, m2])[:, None] * r).sum(0) / Mt))
    # velocidades por diferencias centrales de la TRAYECTORIA (independiente de coef_H)
    rp, rm = np.array(posiciones(th[k + 1], *qs[k + 1])), np.array(posiciones(th[k - 1], *qs[k - 1]))
    v = (rp - rm) / (ts[k + 1] - ts[k - 1])
    wth = (th[k + 1] - th[k - 1]) / (ts[k + 1] - ts[k - 1])
    w1 = wth + (qs[k + 1][0] - qs[k - 1][0]) / (ts[k + 1] - ts[k - 1])
    w2 = w1 + (qs[k + 1][1] - qs[k - 1][1]) / (ts[k + 1] - ts[k - 1])
    H = sum(m * (rr[0] * vv[1] - rr[1] * vv[0]) for m, rr, vv in zip((M0, m1, m2), r, v)) + I0 * wth + I1 * w1 + I2 * w2
    Hs.append(H)
print(f"Centro de masa del sistema: |r_cm| maximo = {max(cm):.1e} m (debe ser 0)")
print(f"Momento angular recalculado con velocidades por diferencias de la trayectoria: |H| maximo = {max(abs(h) for h in Hs):.2e} kg m2/s")
comprobar(max(cm) < 1e-12 and max(abs(h) for h in Hs) < 5e-3, "conservacion del momento")
th_max = np.abs(th).max()
print(f"Giro maximo de la base durante el lazo = {np.degrees(th_max):.3f} grados")
punta_libre = [punta(th[k], *qs[k]) for k in range(0, len(ts), 50)]
punta_fija = [punta(0.0, *qs[k]) for k in range(0, len(ts), 50)]
dif = max(np.linalg.norm(a - b_) for a, b_ in zip(punta_libre, punta_fija))
print(f"Diferencia maxima de posicion de la punta (base libre frente a base fija): {dif * 1000:.1f} mm")
comprobar(dif > 1e-3, "la base libre cambia la posicion de la punta")
fin()
