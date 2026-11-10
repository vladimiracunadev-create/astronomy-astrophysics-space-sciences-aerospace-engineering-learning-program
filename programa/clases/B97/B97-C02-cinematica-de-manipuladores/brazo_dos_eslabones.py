#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C02: cinematica directa e inversa de un brazo plano de dos eslabones.

Dato consultado (2026-11-10): el brazo Canadarm2 mide 17 m (Agencia Espacial Canadiense). La division en dos eslabones de 8.5 m es ILUSTRATIVA
(el brazo real tiene mas articulaciones; su numero no se consulto). Objetivo (10 m, 6 m) y velocidad de punta 0.10 m/s: ILUSTRATIVOS.
Modelo: brazo plano 2R, angulos en rad, longitudes en m. FK: x = l1 cos q1 + l2 cos(q1+q2); y = l1 sin q1 + l2 sin(q1+q2).
IK analitica por ley de cosenos (codo arriba y abajo). Jacobiano J = [[dx/dq1, dx/dq2],[dy/dq1, dy/dq2]], det J = l1 l2 sin q2.
Segunda via: FK de la IK reproduce el objetivo (< 1e-9 m); jacobiano analitico frente a diferencias finitas centradas (< 1e-6).
Sistema de referencia: base del brazo en el origen, x hacia delante, y hacia arriba. Sin limites articulares ni dinamica.
"""
from __future__ import annotations
import math, platform

L1 = L2 = 8.5             # m (ILUSTRATIVO; suma = 17 m, longitud consultada)
OBJ = (10.0, 6.0)         # m (ILUSTRATIVO)
V = 0.10                  # m/s (ILUSTRATIVO)


def fk(q1, q2):
    return (L1 * math.cos(q1) + L2 * math.cos(q1 + q2), L1 * math.sin(q1) + L2 * math.sin(q1 + q2))


def ik(x, y, arriba=False):
    c2 = (x * x + y * y - L1 * L1 - L2 * L2) / (2 * L1 * L2)
    if abs(c2) > 1:
        raise ValueError("fuera del espacio de trabajo")
    q2 = math.acos(c2) * (1 if arriba else -1)
    q1 = math.atan2(y, x) - math.atan2(L2 * math.sin(q2), L1 + L2 * math.cos(q2))
    return q1, q2


def jac(q1, q2):
    s1, c1 = math.sin(q1), math.cos(q1)
    s12, c12 = math.sin(q1 + q2), math.cos(q1 + q2)
    return [[-L1 * s1 - L2 * s12, -L2 * s12], [L1 * c1 + L2 * c12, L2 * c12]]


def jac_num(q1, q2, h=1e-6):
    cols = []
    for dq in ((h, 0), (0, h)):
        a, b = fk(q1 + dq[0], q2 + dq[1]), fk(q1 - dq[0], q2 - dq[1])
        cols.append(((a[0] - b[0]) / (2 * h), (a[1] - b[1]) / (2 * h)))
    return [[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]]


def tasas(q1, q2, vx, vy):
    j = jac(q1, q2)
    det = j[0][0] * j[1][1] - j[0][1] * j[1][0]
    return ((j[1][1] * vx - j[0][1] * vy) / det, (-j[1][0] * vx + j[0][0] * vy) / det), det


def calc():
    q1a, q2a = ik(*OBJ, arriba=False)
    q1b, q2b = ik(*OBJ, arriba=True)
    e1 = math.hypot(fk(q1a, q2a)[0] - OBJ[0], fk(q1a, q2a)[1] - OBJ[1])
    e2 = math.hypot(fk(q1b, q2b)[0] - OBJ[0], fk(q1b, q2b)[1] - OBJ[1])
    ja, jn = jac(q1a, q2a), jac_num(q1a, q2a)
    dj = max(abs(ja[i][k] - jn[i][k]) for i in range(2) for k in range(2))
    (w1, w2), det = tasas(q1a, q2a, V, 0.0)
    detf = L1 * L2 * math.sin(q2a)
    cerca = {}
    for q2 in (1.0, 0.3, 0.05):
        (a, b), d = tasas(0.5, q2, V, 0.0)
        cerca[q2] = (math.hypot(a, b), d)
    return dict(q1a=math.degrees(q1a), q2a=math.degrees(q2a), q1b=math.degrees(q1b), q2b=math.degrees(q2b), err_fk=max(e1, e2),
                dj=dj, det=det, det_f=detf, w1=math.degrees(w1), w2=math.degrees(w2), alcance=L1 + L2, dist=math.hypot(*OBJ),
                w_q1=math.degrees(cerca[1.0][0]), w_q03=math.degrees(cerca[0.3][0]), w_q005=math.degrees(cerca[0.05][0]),
                d_q1=cerca[1.0][1], d_q005=cerca[0.05][1])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Brazo ILUSTRATIVO 2R: l1 = l2 = {L1} m (alcance {r['alcance']:.1f} m); objetivo = {OBJ} m a {r['dist']:.3f} m de la base")
    print(f"IK codo abajo : q1 = {r['q1a']:.3f} deg, q2 = {r['q2a']:.3f} deg")
    print(f"IK codo arriba: q1 = {r['q1b']:.3f} deg, q2 = {r['q2b']:.3f} deg")
    print(f"Error de la FK frente al objetivo = {r['err_fk']:.2e} m; jacobiano analitico frente a numerico = {r['dj']:.2e}")
    print(f"det J = {r['det']:.4f} m2 (l1 l2 sin q2 = {r['det_f']:.4f}); velocidades articulares para 0.10 m/s en x: {r['w1']:.4f} y {r['w2']:.4f} deg/s")
    print("Velocidad articular combinada para 0.10 m/s de punta, q1 = 0.5 rad:")
    print(f"  q2 = 1.00 rad -> {r['w_q1']:.3f} deg/s ; q2 = 0.30 rad -> {r['w_q03']:.3f} deg/s ; q2 = 0.05 rad -> {r['w_q005']:.3f} deg/s")
    assert r["err_fk"] < 1e-9 and r["dj"] < 1e-6 and abs(r["det"] - r["det_f"]) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
