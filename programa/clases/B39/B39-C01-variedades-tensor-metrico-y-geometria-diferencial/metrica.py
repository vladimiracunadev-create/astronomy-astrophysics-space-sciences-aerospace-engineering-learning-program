#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B39-C01: la metrica de la 2-esfera, longitudes, areas y cambio de coordenadas.

Datos: ninguna constante fisica ni dato observado. La variedad (2-esfera de radio 2), la colatitud del circulo (theta0 = 1 rad) y los vectores de prueba son
ILUSTRATIVOS; los resultados de comparacion son formulas cerradas de geometria.
Modelo: ds^2 = a^2 (dtheta^2 + sin^2 theta dphi^2); longitud = integral de sqrt(g_ab x'^a x'^b) dt; area = integral de sqrt(det g) dtheta dphi; la metrica se transforma como g' = J^-T g J^-1 con J = d(x')/d(x), calculado por diferencias finitas.
Supuestos: variedad bidimensional suave, sin el polo. Validez: ilustrativa (geometria, no fisica).
Tolerancia: longitudes y areas frente a la formula cerrada a 1e-9; metrica transformada frente a la formula estereografica a 1e-7.
"""
from __future__ import annotations
import math, platform

A = 2.0  # radio de la esfera (ilustrativo)

def g_sph(th, ph):
    return [[A * A, 0.0], [0.0, A * A * math.sin(th) ** 2]]

def longitud(curva, dcurva, n=4000):
    """Integral de Simpson de sqrt(g_ab x'^a x'^b) para t en [0,1]."""
    f = lambda t: math.sqrt(sum(g_sph(*curva(t))[i][j] * dcurva(t)[i] * dcurva(t)[j] for i in range(2) for j in range(2)))
    h = 1.0 / n
    s = f(0) + f(1) + sum((4 if k % 2 else 2) * f(k * h) for k in range(1, n))
    return s * h / 3

def area_casquete(th0, n=4000):
    f = lambda th: math.sqrt(math.fabs(A ** 4 * math.sin(th) ** 2))
    h = th0 / n
    s = f(0) + f(th0) + sum((4 if k % 2 else 2) * f(k * h) for k in range(1, n))
    return 2 * math.pi * s * h / 3

def estereo(th, ph):
    r = math.tan(th / 2)
    return (r * math.cos(ph), r * math.sin(ph))

def jacobiano(th, ph, h=1e-6):
    cols = []
    for d in ((h, 0), (0, h)):
        p = estereo(th + d[0], ph + d[1]); m = estereo(th - d[0], ph - d[1])
        cols.append([(p[0] - m[0]) / (2 * h), (p[1] - m[1]) / (2 * h)])
    return [[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]]

def inv2(m):
    d = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return [[m[1][1] / d, -m[0][1] / d], [-m[1][0] / d, m[0][0] / d]]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    th0 = 1.0
    # Longitud del paralelo theta0: 2 pi a sin(theta0)
    L = longitud(lambda t: (th0, 2 * math.pi * t), lambda t: (0.0, 2 * math.pi))
    L_cerr = 2 * math.pi * A * math.sin(th0)
    print(f"longitud del paralelo   numerica {L:.9f}  cerrada {L_cerr:.9f}")
    # Longitud del meridiano de 0 a theta0: a theta0
    Lm = longitud(lambda t: (th0 * t, 0.3), lambda t: (th0, 0.0))
    print(f"longitud del meridiano  numerica {Lm:.9f}  cerrada {A * th0:.9f}")
    # Area del casquete: 2 pi a^2 (1 - cos theta0)
    Ar = area_casquete(th0)
    Ar_cerr = 2 * math.pi * A * A * (1 - math.cos(th0))
    print(f"area del casquete       numerica {Ar:.9f}  cerrada {Ar_cerr:.9f}")
    # Angulo entre dos vectores en un punto (th=1, ph=0): u = d_theta, v = d_theta + d_phi
    g = g_sph(1.0, 0.0)
    u, v = (1.0, 0.0), (1.0, 1.0)
    dot = lambda a, b: sum(g[i][j] * a[i] * b[j] for i in range(2) for j in range(2))
    ang = math.acos(dot(u, v) / math.sqrt(dot(u, u) * dot(v, v)))
    ang_cerr = math.atan2(math.sin(1.0), 1.0)  # tan = a sin(theta)/a * 1 = sin(1)
    print(f"angulo entre u y v      {math.degrees(ang):.6f} grados  cerrado {math.degrees(ang_cerr):.6f} grados")
    # Cambio de coordenadas a (x, y) estereograficas: g_xy = 4 a^2/(1+r^2)^2 delta
    th, ph = 1.0, 0.7
    J = jacobiano(th, ph); Ji = inv2(J); G = g_sph(th, ph)
    gp = [[sum(Ji[k][i] * G[k][l] * Ji[l][j] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
    r = math.tan(th / 2)
    fac = 4 * A * A / (1 + r * r) ** 2
    print(f"g' numerica  [{gp[0][0]:.7f} {gp[0][1]:.2e}; {gp[1][0]:.2e} {gp[1][1]:.7f}]  formula {fac:.7f} delta")
    # invariancia de la longitud del paralelo en las dos cartas
    r0 = math.tan(th0 / 2)
    L2 = 2 * math.pi * r0 * math.sqrt(4 * A * A / (1 + r0 * r0) ** 2)
    print(f"longitud en carta estereografica {L2:.9f}")
    assert abs(L - L_cerr) < 1e-9 and abs(Lm - A * th0) < 1e-9
    assert abs(Ar - Ar_cerr) < 1e-9
    assert abs(ang - ang_cerr) < 1e-12
    assert abs(gp[0][0] - fac) < 1e-7 and abs(gp[1][1] - fac) < 1e-7 and abs(gp[0][1]) < 1e-7
    assert abs(L2 - L_cerr) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
