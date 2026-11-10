#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C18: control dimensional: ajuste de circulo y plano por minimos cuadrados e incertidumbre por Monte Carlo.

DATOS SINTETICOS (generados aqui con semilla fija, NO medidos): 36 puntos de un agujero de radio verdadero R = 25,000 mm con centro (10,000; 5,000) mm,
error de forma (lobulo de 3 ondas, amplitud 4 um) y ruido de medida gaussiano con sigma = 3 um; y 49 puntos de una superficie con alabeo
z = 0,008 (x/50)^2 mm mas ruido gaussiano de 2 um.
Metodo: ajuste algebraico de circulo (Kasa) por minimos cuadrados; planitud = maximo - minimo de los residuos respecto del plano de minimos cuadrados (una
estimacion, no la zona minima de la norma). Incertidumbre: se repite el muestreo 400 veces con ruido nuevo (Monte Carlo) y se toma la desviacion tipica
del diametro ajustado; segunda via: formula teorica sigma_R ~ sigma/sqrt(n) para el radio con ruido radial independiente.
Unidades: mm. Tolerancia: sigma_R de Monte Carlo frente a la teorica dentro de 20 %.
"""
from __future__ import annotations
import math, platform, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import solve

XC, YC, R0 = 10.0, 5.0, 25.0
N = 36
SIG = 3e-3


def puntos_circulo(rng, ruido=SIG):
    pts = []
    for i in range(N):
        th = 2 * math.pi * i / N
        r = R0 + 4e-3 * math.cos(3 * th) + rng.gauss(0, ruido)
        pts.append((XC + r * math.cos(th), YC + r * math.sin(th)))
    return pts


def ajuste_circulo(pts):
    # x^2 + y^2 = 2 a x + 2 b y + c  -> a, b centro; R = sqrt(c + a^2 + b^2)
    A = [[0.0] * 3 for _ in range(3)]
    rhs = [0.0] * 3
    for x, y in pts:
        f = (2 * x, 2 * y, 1.0)
        z = x * x + y * y
        for i in range(3):
            rhs[i] += f[i] * z
            for j in range(3):
                A[i][j] += f[i] * f[j]
    a, b, c = solve(A, rhs)
    return a, b, math.sqrt(c + a * a + b * b)


def ajuste_plano(pts):
    A = [[0.0] * 3 for _ in range(3)]
    rhs = [0.0] * 3
    for x, y, z in pts:
        f = (x, y, 1.0)
        for i in range(3):
            rhs[i] += f[i] * z
            for j in range(3):
                A[i][j] += f[i] * f[j]
    return solve(A, rhs)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(84018)
    pts = puntos_circulo(rng)
    a, b, r = ajuste_circulo(pts)
    print("36 puntos SINTETICOS de un agujero (R = 25,000 mm, centro 10,000; 5,000; lobulo 4 um; ruido 3 um)")
    print(f"Ajuste: centro = ({a:.5f}; {b:.5f}) mm, diametro = {2 * r:.5f} mm (verdadero 50,00000)")
    res = [math.hypot(x - a, y - b) - r for x, y in pts]
    print(f"Residuos radiales: min = {min(res) * 1e3:.2f} um, max = {max(res) * 1e3:.2f} um -> redondez (max-min) = {(max(res) - min(res)) * 1e3:.2f} um")
    # Monte Carlo
    rs = []
    for k in range(400):
        rk = random.Random(100000 + k)
        _, _, rr = ajuste_circulo(puntos_circulo(rk))
        rs.append(2 * rr)
    m = sum(rs) / len(rs)
    sd = math.sqrt(sum((x - m) ** 2 for x in rs) / (len(rs) - 1))
    teo = 2 * SIG / math.sqrt(N)
    print(f"Monte Carlo (400 repeticiones): diametro medio = {m:.5f} mm, desviacion tipica = {sd * 1e3:.3f} um ; teorica 2 sigma/sqrt(n) = {teo * 1e3:.3f} um")
    print(f"Incertidumbre expandida (k = 2) del diametro = {2 * sd * 1e3:.2f} um")
    assert abs(sd - teo) / teo < 0.2
    # Plano
    rng2 = random.Random(84019)
    pp = []
    for i in range(7):
        for j in range(7):
            x, y = -25 + 50 * i / 6, -25 + 50 * j / 6
            pp.append((x, y, 0.008 * (x / 50) ** 2 + rng2.gauss(0, 2e-3)))
    pa, pb, pc = ajuste_plano(pp)
    rz = [z - (pa * x + pb * y + pc) for x, y, z in pp]
    print(f"Plano de minimos cuadrados: z = {pa:.2e} x + {pb:.2e} y + {pc:.5f}; planitud (max - min de residuos) = {(max(rz) - min(rz)) * 1e3:.2f} um")
    # Efecto del numero de puntos
    print("Desviacion tipica del diametro frente al numero de puntos (teorica 2 sigma/sqrt(n)):")
    for n in (9, 18, 36, 72):
        rs2 = []
        for k in range(200):
            rk = random.Random(200000 + k)
            ps = []
            for i in range(n):
                th = 2 * math.pi * i / n
                rr0 = R0 + rk.gauss(0, SIG)
                ps.append((XC + rr0 * math.cos(th), YC + rr0 * math.sin(th)))
            rs2.append(2 * ajuste_circulo(ps)[2])
        m2 = sum(rs2) / len(rs2)
        sd2 = math.sqrt(sum((x - m2) ** 2 for x in rs2) / (len(rs2) - 1))
        print(f"  n = {n:3d}: sigma_D = {sd2 * 1e3:6.3f} um ; teorica = {2 * SIG / math.sqrt(n) * 1e3:6.3f} um")
    assert abs(2 * r - 50.0) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
