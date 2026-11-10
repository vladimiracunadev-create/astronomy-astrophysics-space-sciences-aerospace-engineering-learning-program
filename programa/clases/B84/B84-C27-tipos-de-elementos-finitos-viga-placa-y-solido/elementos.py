#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C27: tipos de elementos: viga de Euler-Bernoulli, viga de Timoshenko (cortante) y limite de validez segun la esbeltez.

DATOS ILUSTRATIVOS (no consultados): voladizo de aluminio, E = 69 GPa, nu = 0,33 (G = E/(2(1+nu))), seccion rectangular b = 20 mm x h variable, L = 0,50 m,
carga transversal en el extremo P = 100 N, factor de cortante kappa = 5/6.
Soluciones exactas: Euler delta_E = P L^3/(3 E I); Timoshenko delta_T = delta_E + P L/(kappa G A).
Elementos: (1) Euler Hermite cubico de 2 nodos (exacto en los nodos para carga puntual); (2) Timoshenko lineal de 2 nodos con integracion reducida del cortante (un punto) con 8 elementos:
k_flexion = E I/l [[0,0,0,0],[0,1,0,-1],[0,0,0,0],[0,-1,0,1]] y k_cortante = kappa G A l bT b con b = [-1/l, -1/2, 1/l, -1/2] (GDL w1, th1, w2, th2).
Segunda via: la fraccion de cortante delta_T/delta_E - 1 = 3 E I/(kappa G A L^2) debe coincidir con la calculada de los resultados.
Tolerancias: Euler FE frente a su exacta < 1e-9; Timoshenko FE (8 elementos) frente a su exacta < 2 %.
Los elementos de placa/lamina y solidos 3D NO se implementan aqui (limite declarado de la clase).
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import solve, zeros, viga_ke

E, NU = 69e9, 0.33
G = E / (2 * (1 + NU))
B, L, P, KAPPA = 0.020, 0.50, 100.0, 5.0 / 6.0


def euler_fe(I, n=8):
    le = L / n
    N = 2 * (n + 1)
    K = zeros(N)
    ke = viga_ke(E * I, le)
    for e in range(n):
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4):
                K[g[i]][g[j]] += ke[i][j]
    libres = list(range(2, N))
    f = [0.0] * N
    f[N - 2] = P
    u = solve([[K[i][j] for j in libres] for i in libres], [f[i] for i in libres])
    return u[N - 2 - 2]


def timoshenko_fe(I, A, n=8):
    le = L / n
    N = 2 * (n + 1)
    K = zeros(N)
    bvec = [-1 / le, -0.5, 1 / le, -0.5]
    for e in range(n):
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4):
                v = KAPPA * G * A * le * bvec[i] * bvec[j]
                if i in (1, 3) and j in (1, 3):
                    v += E * I / le * (1 if i == j else -1)
                K[g[i]][g[j]] += v
    libres = list(range(2, N))
    f = [0.0] * N
    f[N - 2] = P
    u = solve([[K[i][j] for j in libres] for i in libres], [f[i] for i in libres])
    return u[N - 2 - 2]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Voladizo de aluminio ILUSTRATIVO: L = 0,50 m, b = 20 mm, P = 100 N, kappa = 5/6")
    print(f"{'L/h':>5s} {'h [mm]':>7s} {'Euler [mm]':>11s} {'Timoshenko [mm]':>16s} {'cortante [%]':>13s} {'error de Euler [%]':>19s} {'FE Euler [mm]':>14s} {'FE Timo [mm]':>13s}")
    for lh in (40, 20, 10, 5, 3, 2):
        h = L / lh
        A = B * h
        I = B * h ** 3 / 12
        de = P * L ** 3 / (3 * E * I)
        dt = de + P * L / (KAPPA * G * A)
        fe_e = euler_fe(I)
        fe_t = timoshenko_fe(I, A)
        frac = dt / de - 1
        frac_teo = 3 * E * I / (KAPPA * G * A * L ** 2)
        assert abs(fe_e - de) / de < 1e-9
        assert abs(frac - frac_teo) < 1e-12
        assert abs(fe_t - dt) / dt < 0.02
        print(f"{lh:5d} {h * 1e3:7.1f} {de * 1e3:11.4f} {dt * 1e3:16.4f} {frac * 100:13.2f} {(de - dt) / dt * 100:19.2f} {fe_e * 1e3:14.4f} {fe_t * 1e3:13.4f}")
    print("Criterio practico ILUSTRATIVO: viga de Euler aceptable si el cortante aporta < 5 % -> L/h >= " + str(next(lh for lh in range(2, 200) if 3 * E / (12 * KAPPA * G) * (1 / lh) ** 2 < 0.05)) + " para seccion rectangular")
    print("Una barra (solo axial) no tiene rigidez transversal: una cadena de barras en voladizo con carga transversal es un mecanismo (matriz singular)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
