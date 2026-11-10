#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C14: jardineria por impactos y mezcla de componentes en un regolito SINTETICO.

Datos: SINTETICOS / ILUSTRATIVOS. Tasa de remocion de una capa de 1 cm lambda = 1 por 1.0e8 anos por celda (ilustrativa); composicion de tres componentes (basaltico, de tierras altas, enriquecido
en elementos incompatibles) en % de oxidos MgO, FeO, Al2O3, inventada; suma de oxidos 100. Ningun valor es una medicion lunar.
Modelo: (A) cada celda de 1 cm se voltea con eventos de Poisson de tasa lambda; fraccion sin voltear tras t: exp(-lambda t); Monte Carlo con semilla fija sobre 20000 celdas.
(B) El suelo es una mezcla lineal de tres componentes; fracciones por resolucion del sistema 3x3 (MgO, FeO, Al2O3) con eliminacion gaussiana, con y sin ruido gaussiano.
Supuestos: eventos independientes; sin profundidad mixta variable; mezcla lineal en masa. Validez: ilustrativa.
Tolerancia: fraccion sin voltear MC vs analitica a 1 % absoluto; recuperacion de fracciones sin ruido a 1e-10.
"""
from __future__ import annotations
import math, platform, random

LAM = 1.0 / 1.0e8      # eventos por celda y por ano

COMP = {  # % masa de oxidos (SINTETICO)
    "basaltico": (8.0, 20.0, 10.0),
    "tierras altas": (6.0, 5.0, 26.0),
    "enriquecido": (11.0, 12.0, 15.0),
}

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

def fracciones(suelo):
    nombres = list(COMP)
    A = [[COMP[k][i] for k in nombres] for i in range(3)]
    return dict(zip(nombres, resolver(A, list(suelo))))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Jardineria: fraccion de una capa de 1 cm que sigue sin voltear (lambda = 1/1e8 anos, ILUSTRATIVA)")
    print("t [anos]     analitica exp(-lambda t)   Monte Carlo (20000 celdas)")
    rng = random.Random(99)
    N = 20000
    for t in (1.0e7, 5.0e7, 1.0e8, 3.0e8, 1.0e9):
        # tiempo hasta el primer evento ~ exponencial
        sin = sum(1 for _ in range(N) if rng.expovariate(LAM) > t)
        an = math.exp(-LAM * t)
        print(f"{t:9.1e}   {an:14.5f}            {sin / N:12.5f}")
        assert abs(sin / N - an) < 0.01, (t, sin / N, an)
    t_med = math.log(2.0) / LAM
    print(f"   tiempo en que la mitad de la capa se ha volteado al menos una vez = ln2 / lambda = {t_med:.4e} anos")
    # numero medio de volteos
    print(f"   volteos medios en 1e9 anos = {LAM * 1e9:.1f}")
    print("B. Mezcla de tres componentes SINTETICOS (% masa de MgO, FeO, Al2O3)")
    for k, v in COMP.items():
        print(f"   {k:14s} {v}")
    verdad = {"basaltico": 0.50, "tierras altas": 0.30, "enriquecido": 0.20}
    suelo = tuple(sum(verdad[k] * COMP[k][i] for k in COMP) for i in range(3))
    rec = fracciones(suelo)
    err = max(abs(rec[k] - verdad[k]) for k in verdad)
    print(f"   suelo = ({suelo[0]:.4f}, {suelo[1]:.4f}, {suelo[2]:.4f}) ; fracciones recuperadas: " + ", ".join(f"{k} {rec[k]:.6f}" for k in rec) + f" ; error maximo = {err:.2e}")
    assert err < 1e-10
    print("C. Ruido gaussiano de 0.2 % absoluto en cada oxido (200 repeticiones, semilla 5)")
    rng2 = random.Random(5)
    lst = {k: [] for k in COMP}
    for _ in range(200):
        s = tuple(x + rng2.gauss(0, 0.2) for x in suelo)
        f = fracciones(s)
        for k in COMP:
            lst[k].append(f[k])
    for k in COMP:
        m = sum(lst[k]) / 200
        sd = math.sqrt(sum((x - m) ** 2 for x in lst[k]) / 199)
        print(f"   {k:14s} media = {m:.4f} ; desviacion = {sd:.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
