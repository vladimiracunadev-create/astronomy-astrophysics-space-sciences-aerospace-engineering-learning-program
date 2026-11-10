#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C26: convergencia de malla: orden observado, extrapolacion de Richardson e indice de convergencia de malla (GCI).

DATOS ILUSTRATIVOS (no consultados): barra de aluminio E = 69 GPa, longitud L = 1 m, area afilada A(x) = A0 (1 + 2x/L) con A0 = 4e-4 m2 (se ensancha),
empotrada en x = 0 y con carga distribuida axial uniforme q = 10 kN/m. Elementos de barra de dos nodos con area en el punto medio y carga consistente.
Magnitudes de interes: (a) desplazamiento del extremo; (b) tension del elemento de la raiz frente a la exacta en x = 0.
Exacta: N(x) = q (L - x); u'(x) = N/(E A); u(L) = int_0^L q (L - x)/(E A0 (1 + 2x/L)) dx (Simpson con 2 000 000 pasos); tension exacta en x = 0: q L/A0.
Mallas: n = 4, 8, 16, 32, 64 (razon de refinamiento r = 2). Orden observado p = ln((f2 - f1)/(f3 - f2))/ln 2 con tres mallas consecutivas f1 (gruesa), f2, f3 (fina);
Richardson: f_ext = f3 + (f3 - f2)/(2^p - 1); GCI fino = 1,25 |f3 - f2|/(f3 (2^p - 1)) (factor de seguridad 1,25 con tres mallas, de Roache; no consultado en esta sesion).
Tolerancias: orden observado del desplazamiento entre 1,8 y 2,2; extrapolado dentro de 1e-6 relativo de la exacta.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import solve, zeros

E, L, A0, Q = 69e9, 1.0, 4.0e-4, 10e3


def area(x):
    return A0 * (1 + 2 * x / L)


def resolver(n):
    xs = [L * i / n for i in range(n + 1)]
    K = zeros(n + 1)
    f = [0.0] * (n + 1)
    for e in range(n):
        le = xs[e + 1] - xs[e]
        k = E * area(0.5 * (xs[e] + xs[e + 1])) / le
        K[e][e] += k
        K[e + 1][e + 1] += k
        K[e][e + 1] -= k
        K[e + 1][e] -= k
        f[e] += Q * le / 2
        f[e + 1] += Q * le / 2
    libres = list(range(1, n + 1))
    u = [0.0] + solve([[K[i][j] for j in libres] for i in libres], [f[i] for i in libres])
    sig_raiz = E * (u[1] - u[0]) / (xs[1] - xs[0])
    return u[-1], sig_raiz


def exacta():
    N = 2_000_000
    h = L / N
    g = lambda x: Q * (L - x) / (E * area(x))
    s = g(0) + g(L)
    for i in range(1, N):
        s += (4 if i % 2 else 2) * g(i * h)
    return s * h / 3, Q * L / A0


def orden(f1, f2, f3):
    return math.log((f2 - f1) / (f3 - f2)) / math.log(2)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ue, se = exacta()
    print(f"Barra ILUSTRATIVA ensanchada: u(L) exacta = {ue * 1e3:.8f} mm ; sigma(0) exacta = {se / 1e6:.4f} MPa")
    ns = (4, 8, 16, 32, 64)
    res = [resolver(n) for n in ns]
    print(f"{'n':>4s} {'u(L) [mm]':>13s} {'err rel u':>11s} {'sigma raiz [MPa]':>17s} {'err rel s':>11s}")
    for n, (u, s) in zip(ns, res):
        print(f"{n:4d} {u * 1e3:13.8f} {abs(u - ue) / ue:11.3e} {s / 1e6:17.4f} {abs(s - se) / se:11.3e}")
    for nombre, idx, ref in (("desplazamiento del extremo", 0, ue), ("tension de la raiz", 1, se)):
        f = [r[idx] for r in res]
        p = orden(f[-3], f[-2], f[-1])
        ext = f[-1] + (f[-1] - f[-2]) / (2 ** p - 1)
        gci = 1.25 * abs(f[-1] - f[-2]) / (abs(f[-1]) * (2 ** p - 1))
        print(f"{nombre}: orden observado p = {p:.3f} ; Richardson = {ext:.8e} (exacta {ref:.8e}, dif rel {abs(ext - ref) / ref:.1e}) ; GCI(n = 64) = {gci * 100:.4f} %")
        if idx == 0:
            assert 1.8 < p < 2.2 and abs(ext - ref) / ref < 1e-6
    # Mallas de 4 a 64: se necesitaria para un error de 1e-4 en la tension de la raiz
    n_req = 4
    while abs(resolver(n_req)[1] - se) / se > 1e-4 and n_req < 4096:
        n_req *= 2
    print(f"Elementos necesarios (potencias de 2) para un error relativo de la tension de la raiz < 1e-4: {n_req}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
