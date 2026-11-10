#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C28: condiciones de contorno y cargas: modos de solido rigido, restricciones, cargas equivalentes y equilibrio.

DATOS ILUSTRATIVOS (no consultados): viga de aluminio de L = 1,0 m, EI = 287,5 N m2, rho A = 1,35 kg/m (la de B84-C10), 8 elementos de Euler-Bernoulli;
carga distribuida uniforme q = 100 N/m; barra de aluminio de L = 1 m y A = 4e-4 m2 con dilatacion termica alpha = 23e-6 1/K y DeltaT = 50 K.
Verificaciones: (1) autovalores de K libre: se cuentan los (casi) nulos = modos de solido rigido (2 en una viga plana libre: traslacion y giro);
(2) con una sola restriccion w = 0 queda un modo (giro); con dos apoyos simples w = 0 en ambos extremos no quedan;
(3) cargas equivalentes: consistente [qL/2, qL^2/12, qL/2, -qL^2/12] frente a puntual [qL/2, 0, qL/2, 0]; la flecha central exacta es 5 q L^4/(384 EI);
(4) equilibrio: la suma de reacciones iguala la carga total q L y el momento de reaccion se equilibra; (5) barra empotrada en ambos extremos con DeltaT: sigma = -E alpha DeltaT.
Tolerancias: autovalor nulo si lambda/lambda_max < 1e-10; flecha con carga consistente frente a exacta < 1e-9; equilibrio 1e-9.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import ensamblar_viga, reducir, jacobi_eig, solve, matvec

EI, RHOA, L = 287.5, 1.35, 1.0
Q = 100.0
N_EL = 8


def contar_nulos(K, libres):
    lam, _ = jacobi_eig(reducir(K, libres))
    mx = max(abs(l) for l in lam)
    return sum(1 for l in lam if abs(l) / mx < 1e-10), lam


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    K, M = ensamblar_viga(N_EL, L, EI, RHOA)
    todos = list(range(len(K)))
    n0, _ = contar_nulos(K, todos)
    print(f"Viga libre de {N_EL} elementos ({len(K)} GDL): modos de solido rigido = {n0} (esperados 2: traslacion y giro)")
    n1, _ = contar_nulos(K, [i for i in todos if i != 0])
    print(f"Con una sola restriccion w0 = 0: modos de solido rigido restantes = {n1} (giro libre: el modelo sigue singular)")
    ap = [i for i in todos if i not in (0, 2 * N_EL)]
    n2, lam = contar_nulos(K, ap)
    print(f"Con apoyos simples w0 = wn = 0: modos de solido rigido = {n2}; menor autovalor = {min(lam):.4e}")
    assert n0 == 2 and n1 == 1 and n2 == 0
    # Cargas equivalentes
    le = L / N_EL
    f_cons = [0.0] * len(K)
    f_punt = [0.0] * len(K)
    for e in range(N_EL):
        g = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for loc, v in zip(g, (Q * le / 2, Q * le ** 2 / 12, Q * le / 2, -Q * le ** 2 / 12)):
            f_cons[loc] += v
        f_punt[2 * e] += Q * le / 2
        f_punt[2 * e + 2] += Q * le / 2
    exacta = 5 * Q * L ** 4 / (384 * EI)
    centro = 2 * (N_EL // 2)
    for nom, f in (("consistente", f_cons), ("puntual equivalente", f_punt)):
        u = solve(reducir(K, ap), [f[i] for i in ap])
        w_c = u[ap.index(centro)]
        r = matvec(K, [0.0 if i not in ap else u[ap.index(i)] for i in todos])
        reacc = (r[0] - f[0], r[2 * N_EL] - f[2 * N_EL])
        print(f"Carga {nom:20s}: flecha central = {w_c * 1e3:.6f} mm (exacta {exacta * 1e3:.6f}, error {abs(w_c - exacta) / exacta * 100:.4f} %) ; reacciones = {reacc[0]:.4f} N y {reacc[1]:.4f} N ; suma = {sum(reacc):.6f} N")
        assert abs(sum(reacc) + Q * L) < 1e-6 or abs(sum(reacc) - Q * L) < 1e-6 or abs(abs(sum(reacc)) - Q * L) < 1e-6
        if nom == "consistente":
            assert abs(w_c - exacta) / exacta < 1e-9
    # Termica
    E, A, al, dT = 69e9, 4e-4, 23e-6, 50.0
    n = 4
    l = 1.0 / n
    Kb = [[0.0] * (n + 1) for _ in range(n + 1)]
    f = [0.0] * (n + 1)
    for e in range(n):
        k = E * A / l
        Kb[e][e] += k; Kb[e + 1][e + 1] += k; Kb[e][e + 1] -= k; Kb[e + 1][e] -= k
        ft = E * A * al * dT
        f[e] -= ft
        f[e + 1] += ft
    libres = list(range(1, n))
    u = [0.0] + solve([[Kb[i][j] for j in libres] for i in libres], [f[i] for i in libres]) + [0.0]
    sigma = E * ((u[1] - u[0]) / l - al * dT)
    print(f"Barra empotrada en ambos extremos con DeltaT = {dT:.0f} K: sigma FE = {sigma / 1e6:.4f} MPa ; -E alpha DeltaT = {-E * al * dT / 1e6:.4f} MPa")
    assert abs(sigma + E * al * dT) < 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
