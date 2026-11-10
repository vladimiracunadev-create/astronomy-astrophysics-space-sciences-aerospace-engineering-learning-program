#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C12: elementos finitos de una barra: ensamblaje, restricciones, solucion exacta y prueba del parche.

DATOS ILUSTRATIVOS (no consultados): barra de aluminio E = 69 GPa, longitud L = 1,0 m, area A(x) = A0 (1 - 0,5 x/L) con A0 = 4,0e-4 m2
(afilada), empotrada en x = 0 y con carga axial P = 10 kN en x = L.
Modelo: elementos de barra de 2 nodos con area constante igual al valor en el punto medio; k_e = E A_e / l_e [[1,-1],[-1,1]].
Solucion exacta: u(L) = (P L/(E A0 c)) (-ln(1 - c)) con c = 0,5, es decir u(L) = P L/(E A0) ln(2)/0,5.
Segunda via: la energia de deformacion U = 1/2 u^T K u debe igualar 1/2 P u(L) (equilibrio) y la reaccion en el apoyo debe ser -P.
Prueba del parche: en una barra de area constante con malla irregular y carga en el extremo la solucion nodal es exacta (error < 1e-12).
Unidades: N, m, Pa. Tolerancias: reaccion = -P a 1e-9 (relativa); energia = 1/2 P u a 1e-12 (relativa); orden de convergencia observado entre 1,9 y 2,1.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import solve, zeros, matvec

E, L, A0, P, C = 69e9, 1.0, 4.0e-4, 10e3, 0.5


def area(x):
    return A0 * (1 - C * x / L)


def ensamblar(nodos, area_fn):
    n = len(nodos)
    K = zeros(n)
    for e in range(n - 1):
        le = nodos[e + 1] - nodos[e]
        ae = area_fn(0.5 * (nodos[e] + nodos[e + 1]))
        k = E * ae / le
        K[e][e] += k
        K[e + 1][e + 1] += k
        K[e][e + 1] -= k
        K[e + 1][e] -= k
    return K


def resolver(nodos, area_fn, carga):
    K = ensamblar(nodos, area_fn)
    n = len(nodos)
    libres = list(range(1, n))
    f = [0.0] * n
    f[-1] = carga
    Kff = [[K[i][j] for j in libres] for i in libres]
    uf = solve(Kff, [f[i] for i in libres])
    u = [0.0] + uf
    Ku = matvec(K, u)
    reaccion = Ku[0] - f[0]  # R = (K u)_0 - f_0
    return K, u, reaccion


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ue = P * L / (E * A0 * C) * (-math.log(1 - C))
    print(f"Barra ILUSTRATIVA afilada: E = 69 GPa, L = 1 m, A0 = 4e-4 m2, c = 0,5, P = 10 kN; u(L) exacta = {ue * 1e3:.6f} mm")
    print(" ne   u(L) [mm]   error rel.   orden obs.   reaccion [N]   U [J]    1/2 P u [J]")
    prev = None
    ordenes = []
    for ne in (1, 2, 4, 8, 16, 32):
        nodos = [L * i / ne for i in range(ne + 1)]
        K, u, R = resolver(nodos, area, P)
        err = abs(u[-1] - ue) / ue
        U = 0.5 * sum(u[i] * v for i, v in enumerate(matvec(K, u)))
        ord_ = "" if prev is None else f"{math.log(prev / err) / math.log(2):10.3f}"
        if prev is not None:
            ordenes.append(float(ord_))
        print(f"{ne:3d} {u[-1] * 1e3:11.6f} {err:12.3e} {ord_:>11s} {R:14.6f} {U:9.5f} {0.5 * P * u[-1]:12.5f}")
        assert abs(R + P) / P < 1e-9
        assert abs(U - 0.5 * P * u[-1]) / U < 1e-12
        prev = err
    print(f"Orden observado en las dos mallas mas finas = {ordenes[-1]:.3f} (teorico 2)")
    # Prueba del parche: area constante, malla irregular
    nodos = [0.0, 0.13, 0.31, 0.32, 0.77, 1.0]
    K, u, R = resolver(nodos, lambda x: A0, P)
    dif = max(abs(u[i] - P * nodos[i] / (E * A0)) for i in range(len(nodos)))
    print(f"Prueba del parche (area constante, malla irregular): error nodal maximo = {dif:.2e} m")
    assert dif < 1e-12
    assert 1.9 < ordenes[-1] < 2.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
