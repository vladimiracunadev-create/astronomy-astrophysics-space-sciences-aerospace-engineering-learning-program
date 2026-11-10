#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C20: red astroquimica minima de carbono (C+, CO, HCO+, CO helado) con conservacion de carbono y estado estacionario.

Datos: SINTETICOS / ILUSTRATIVOS (tasas en s-1, sin base de datos): C+ -> CO con k1 = 2e-10 ; CO -> C+ (fotodisociacion mas ionizacion efectiva) k2 = 5e-12 ;
CO + H3+ -> HCO+ con k3 = 1.7e-9 * n(H3+) con n(H3+) = 5.3e-5 cm-3 (valor de B55-C04) ; HCO+ + e- -> CO con k4 = 2e-7 * n(e), n(e) = 1e-3 cm-3 ;
congelacion CO -> hielo con k5 = 1e-11 ; desorcion hielo -> CO con k6 = 2e-12. Ninguno procede de una base de datos; McElroy et al. (2013) se consulto solo por su resumen
(6173 reacciones y 467 especies en la base UMIST 2012).
Modelo: dy/dt = M y (lineal); integracion con Euler implicito (conserva invariantes lineales) y estado estacionario resolviendo M y = 0 con la restriccion de carbono total = 1.
Supuestos: abundancias de H3+ y e- fijas; red lineal en las especies de carbono. Validez: ilustrativa; no es un modelo de nube.
Tolerancia: carbono total conservado a 1e-9 (redondeo acumulado de 10^6 pasos); estacionario por integracion larga vs algebraico a 1e-6 relativo; balance detallado de flujos en el estacionario a 1e-9.
"""
from __future__ import annotations
import platform

ESP = ["C+", "CO", "HCO+", "CO(hielo)"]
YR = 3.15576e7
K1, K2 = 2.0e-10, 5.0e-12
NH3P, NE = 5.3e-5, 1.0e-3
K3 = 1.7e-9 * NH3P
K4 = 2.0e-7 * NE
K5, K6 = 1.0e-11, 2.0e-12

def construir(k5):
    """matriz M (dy/dt = M y); columnas = especie que reacciona"""
    M = [[0.0] * 4 for _ in range(4)]
    def reaccion(origen, destino, k):
        M[origen][origen] -= k
        M[destino][origen] += k
    reaccion(0, 1, K1)   # C+ -> CO
    reaccion(1, 0, K2)   # CO -> C+
    reaccion(1, 2, K3)   # CO -> HCO+
    reaccion(2, 1, K4)   # HCO+ -> CO
    reaccion(1, 3, k5)   # CO -> hielo
    reaccion(3, 1, K6)   # hielo -> CO
    return M

M = construir(K5)

def resolver(A, b):
    n = len(b)
    A = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[p] = A[p], A[i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n + 1):
                A[r][c] -= f * A[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (A[i][n] - sum(A[i][c] * x[c] for c in range(i + 1, n))) / A[i][i]
    return x

def euler_implicito(y, dt):
    A = [[(1.0 if i == j else 0.0) - dt * M[i][j] for j in range(4)] for i in range(4)]
    return resolver(A, y)

def estacionario(M=M):
    A = [fila[:] for fila in M]
    A[3] = [1.0, 1.0, 1.0, 1.0]       # sustituye una ecuacion por la conservacion
    b = [0.0, 0.0, 0.0, 1.0]
    return resolver(A, b)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Red SINTETICA de carbono: C+ <-> CO <-> HCO+ ; CO <-> hielo (tasas en s-1, ILUSTRATIVAS)")
    print(f"   k(C+->CO) = {K1:.1e} ; k(CO->C+) = {K2:.1e} ; k(CO->HCO+) = {K3:.3e} ; k(HCO+->CO) = {K4:.1e} ; k(CO->hielo) = {K5:.1e} ; k(hielo->CO) = {K6:.1e}")
    # conservacion: la suma de cada columna de M es cero
    for j in range(4):
        assert abs(sum(M[i][j] for i in range(4))) < 1e-25
    ss = estacionario()
    print("B. Estado estacionario algebraico (fracciones del carbono total)")
    for e, v in zip(ESP, ss):
        print(f"   {e:10s} {v:.6f}")
    assert abs(sum(ss) - 1.0) < 1e-12
    # integracion
    y = [1.0, 0.0, 0.0, 0.0]
    t = 0.0
    dt = 1.0e8      # s (pasos grandes y estables)
    print("C. Integracion (Euler implicito, paso 1e8 s) desde C+ = 1")
    print("t [anos]      " + "  ".join(f"{e:>10s}" for e in ESP) + "   suma")
    marcas = {1: 3.2e0, 10: 3.2e1, 100: 3.2e3}
    pasos_imp = [10, 100, 1000, 10000, 100000, 1000000]
    paso = 0
    siguientes = set(pasos_imp)
    while paso < 1000000:
        y = euler_implicito(y, dt)
        paso += 1
        t += dt
        if paso in siguientes:
            print(f"{t / YR:10.3e}   " + "  ".join(f"{v:10.6f}" for v in y) + f"   {sum(y):.12f}")
            assert abs(sum(y) - 1.0) < 1e-9
    err = max(abs(a - b) / b for a, b in zip(y, ss))
    print(f"   error relativo respecto del estacionario algebraico = {err:.2e}")
    assert err < 1e-6
    # balance detallado de flujos
    print("D. Flujos en el estacionario [por atomo de C y por segundo]: debe haber balance neto cero por especie")
    pares = [("C+ -> CO", K1 * ss[0], "CO -> C+", K2 * ss[1]), ("CO -> HCO+", K3 * ss[1], "HCO+ -> CO", K4 * ss[2]), ("CO -> hielo", K5 * ss[1], "hielo -> CO", K6 * ss[3])]
    for a, fa, b, fb in pares:
        print(f"   {a:12s} {fa:.4e}   {b:12s} {fb:.4e}   diferencia {abs(fa - fb):.2e}")
        assert abs(fa - fb) < 1e-9 * max(fa, fb) + 1e-20
    print("E. Sensibilidad: duplicar k(CO->hielo) cambia el CO helado de", f"{ss[3]:.4f}", "a", end=" ")
    ss2 = estacionario(construir(2 * K5))
    print(f"{ss2[3]:.4f}")
    assert ss2[3] > ss[3]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
