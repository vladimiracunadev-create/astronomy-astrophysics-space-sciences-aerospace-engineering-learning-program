#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C22: efecto de los parametros de orientacion terrestre (EOP).

Datos: definicion del ERA (IERS Conventions 2010, TN36, ec. 5.14), |UT1-UTC| < 0.9 s,
periodo del bamboleo de Chandler ~ 435 d y amplitudes de los bamboleos
chandleriano y anual "del orden de 0.5 y 0.1 segundos de arco" (TN36 cap. 5 y
glosario, consultado 2026-11-05). Valores de las series xp, yp: SINTETICOS
(amplitud chandleriana 0.20", anual 0.08", fases arbitrarias).
Modelo: [GCRS] = Q(t) R(t) W(t) [ITRS] (TN36 ec. 5.1): W = movimiento polar
(giros pequenos xp, yp), R = rotacion por el ERA alrededor del polo, Q =
movimiento del polo en el sistema celeste (precesion-nutacion), que NO se
calcula aqui (se toma Q = I).
Aproximacion de giros pequenos: W = R1(-yp) R2(-xp).
Supuestos: Tierra rigida; sin mareas. Tolerancia: ortogonalidad y det = 1 a
1e-14; desplazamiento por polo = a * theta a 1e-6 relativa.
"""
from __future__ import annotations
import math
import platform
import sys

ARC = math.pi / (180 * 3600)            # rad por segundo de arco
A_EQ = 6378137.0                         # m (GRS80)
OMEGA = 7.292115e-5


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]


def R1(t):
    c, s = math.cos(t), math.sin(t)
    return [[1, 0, 0], [0, c, s], [0, -s, c]]


def R2(t):
    c, s = math.cos(t), math.sin(t)
    return [[c, 0, -s], [0, 1, 0], [s, 0, c]]


def R3(t):
    c, s = math.cos(t), math.sin(t)
    return [[c, s, 0], [-s, c, 0], [0, 0, 1]]


def traspuesta(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def era_rad(tu):
    return 2 * math.pi * ((0.7790572732640 + 1.00273781191135448 * tu) % 1.0)


def W(xp, yp):
    return matmul(R1(-yp), R2(-xp))


def itrs_a_gcrs(v, tu, xp=0.0, yp=0.0):
    # [GCRS] = Q R W [ITRS], con Q = I y R = R3(-ERA) (TIRS -> CIRS)
    return mv(R3(-era_rad(tu)), mv(W(xp, yp), v))


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # 1) ortogonalidad y determinante
    M = matmul(R3(-era_rad(9804.5)), W(0.3 * ARC, -0.2 * ARC))
    I = matmul(M, traspuesta(M))
    assert all(abs(I[i][j] - (1.0 if i == j else 0.0)) < 1e-14 for i in range(3) for j in range(3))
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    assert abs(det - 1.0) < 1e-14
    # 2) polo en el sistema terrestre: el desplazamiento por polo = a * theta
    for xp_as in (0.1, 0.5):
        v = [0.0, 0.0, 6356752.314]                  # punto del polo (ITRS)
        w = mv(W(xp_as * ARC, 0.0), v)
        d = math.dist(v, w)
        esp = 6356752.314 * xp_as * ARC
        print(f"xp = {xp_as} arcsec: el polo terrestre se desplaza {d:.3f} m (esperado {esp:.3f} m)")
        assert abs(d - esp) / esp < 1e-6
    # 3) UT1-UTC = 0.9 s
    print(f"0.9 s de UT1-UTC en el ecuador: {0.9 * OMEGA * A_EQ:.1f} m")
    assert abs(0.9 * OMEGA * A_EQ - 418.6) < 0.5
    # 4) 1 mas de error del polo celeste en la superficie
    print(f"1 mas = {1e-3 * ARC * A_EQ * 100:.2f} cm en la superficie")
    # 5) movimiento polar sintetico: Chandler 435 d + anual 365.25 d
    Ac, Aa = 0.20, 0.08
    pc, pa = 435.0, 365.25
    bat = 1.0 / (1.0 / pa - 1.0 / pc)
    print(f"periodo de batido Chandler/anual = {bat:.0f} d = {bat/365.25:.2f} anios")
    assert abs(bat - 2278.4) < 0.5
    xs = [Ac * math.cos(2 * math.pi * t / pc) + Aa * math.cos(2 * math.pi * t / pa) for t in range(0, 4000)]
    print(f"amplitud maxima sintetica de xp = {max(xs):.3f} arcsec (suma {Ac + Aa:.2f})")
    assert max(xs) <= Ac + Aa + 1e-12 and max(xs) > 0.27
    # 6) efecto en una estacion en (lat 45, lon 0) con ERA = 0: GCRS con y sin movimiento polar
    st = [4517590.879, 0.0, 4487348.409]
    a = itrs_a_gcrs(st, 0.0)
    b = itrs_a_gcrs(st, 0.0, 0.28 * ARC, 0.0)
    print(f"movimiento polar de 0.28 arcsec mueve la estacion {math.dist(a, b):.2f} m")
    assert abs(math.dist(a, b) - 0.28 * ARC * math.hypot(*st)) / (0.28 * ARC * math.hypot(*st)) < 0.2
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
