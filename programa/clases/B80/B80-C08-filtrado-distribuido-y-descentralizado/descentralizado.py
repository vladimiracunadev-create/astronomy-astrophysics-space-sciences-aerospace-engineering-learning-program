#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C08: fusion descentralizada con errores correlacionados: suma ingenua de informacion frente a interseccion de covarianzas (CI).

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80008). Dos nodos estiman el mismo estado 2D x = (posicion, velocidad) con errores e1, e2 de media cero.
Los errores son correlacionados porque ambos usaron la misma informacion previa (ruido de proceso comun): covarianza conjunta
 [[P1, P12], [P12^T, P2]] con P1 = diag(4, 1), P2 = diag(1, 4), P12 = rho * sqrt(diag(P1) diag(P2)) por componente, rho = 0.7 (ilustrativo).
Fusion ingenua (supone P12 = 0): P_i = (P1^-1 + P2^-1)^-1, x_f = P_i (P1^-1 x1 + P2^-1 x2).
Interseccion de covarianzas (Julier y Uhlmann, 1997; NO consultada, relacion estandar verificada aqui): P_ci^-1 = w P1^-1 + (1-w) P2^-1, x = P_ci (w P1^-1 x1 + (1-w) P2^-1 x2), w en [0,1] que minimiza la traza (busqueda en rejilla de paso 0.001).
Verificacion independiente: la covarianza REAL del error del fusionado se calcula en forma cerrada con la covarianza conjunta y por Monte Carlo (200000 muestras),
y se compara con la covarianza que el metodo DECLARA. Consistencia: P_declarada - P_real semidefinida positiva (o NEES medio <= dimension).
Sistema de referencia: estado generico en unidades arbitrarias de posicion y velocidad.
"""
from __future__ import annotations
import math, platform, random

RHO = 0.7
P1 = [[4.0, 0.0], [0.0, 1.0]]
P2 = [[1.0, 0.0], [0.0, 4.0]]
P12 = [[RHO * math.sqrt(4.0 * 1.0), 0.0], [0.0, RHO * math.sqrt(1.0 * 4.0)]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def add(A, B, a=1.0, b=1.0):
    return [[a * x + b * y for x, y in zip(r, s)] for r, s in zip(A, B)]


def inv2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def traza(M):
    return M[0][0] + M[1][1]


def real_cov(W1, W2):
    """Covarianza real de e_f = W1 e1 + W2 e2 con W1 + W2 = I (estimador insesgado)."""
    t = mm(mm(W1, P1), tr(W1))
    t = add(t, mm(mm(W2, P2), tr(W2)))
    c = mm(mm(W1, P12), tr(W2))
    return add(add(t, c), tr(c))


def chol_conjunta():
    S = [[P1[0][0], P1[0][1], P12[0][0], P12[0][1]],
         [P1[1][0], P1[1][1], P12[1][0], P12[1][1]],
         [P12[0][0], P12[1][0], P2[0][0], P2[0][1]],
         [P12[0][1], P12[1][1], P2[1][0], P2[1][1]]]
    n = 4
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(S[i][i] - s)
            else:
                L[i][j] = (S[i][j] - s) / L[j][j]
    return L


def min_eig_2x2(M):
    a, b, d = M[0][0], 0.5 * (M[0][1] + M[1][0]), M[1][1]
    return 0.5 * (a + d) - math.sqrt(0.25 * (a - d) ** 2 + b * b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS (semilla 80008): P1 = diag(4,1), P2 = diag(1,4), correlacion cruzada rho = {RHO} por componente")
    I1, I2 = inv2(P1), inv2(P2)
    # Ingenua
    Pi = inv2(add(I1, I2))
    W1i, W2i = mm(Pi, I1), mm(Pi, I2)
    Pi_real = real_cov(W1i, W2i)
    # CI
    mejor = (1e9, 0.0)
    for k in range(0, 1001):
        w = k / 1000.0
        Pw = inv2(add(I1, I2, w, 1.0 - w))
        if traza(Pw) < mejor[0]:
            mejor = (traza(Pw), w)
    w = mejor[1]
    Pc = inv2(add(I1, I2, w, 1.0 - w))
    W1c, W2c = mm(Pc, [[w * I1[i][j] for j in range(2)] for i in range(2)]), mm(Pc, [[(1 - w) * I2[i][j] for j in range(2)] for i in range(2)])
    Pc_real = real_cov(W1c, W2c)
    print(f"Peso optimo de CI w = {w:.3f}")
    print(" metodo      traza declarada   traza real (cerrada)   min autovalor (declarada - real)   consistente")
    cons = {}
    for nom, Pd, Pr in (("ingenua", Pi, Pi_real), ("CI", Pc, Pc_real)):
        dif = add(Pd, Pr, 1.0, -1.0)
        me = min_eig_2x2(dif)
        cons[nom] = me >= -1e-9
        print(f"{nom:9s} {traza(Pd):16.4f} {traza(Pr):21.4f} {me:34.4f} {'si' if cons[nom] else 'NO':>12s}")
    # Monte Carlo
    rnd = random.Random(80008)
    L = chol_conjunta()
    n = 200000
    acc = {"ingenua": 0.0, "CI": 0.0}
    for _ in range(n):
        zz = [rnd.gauss(0, 1) for _ in range(4)]
        e = [sum(L[i][k] * zz[k] for k in range(i + 1)) for i in range(4)]
        e1, e2 = e[:2], e[2:]
        for nom, W1, W2, Pd in (("ingenua", W1i, W2i, Pi), ("CI", W1c, W2c, Pc)):
            ef = [sum(W1[i][j] * e1[j] + W2[i][j] * e2[j] for j in range(2)) for i in range(2)]
            Pinv = inv2(Pd)
            acc[nom] += sum(ef[i] * Pinv[i][j] * ef[j] for i in range(2) for j in range(2))
    for nom in acc:
        print(f"NEES medio de {nom:8s} = {acc[nom] / n:.3f} (consistente si <= 2.000 = dimension)")
    assert not cons["ingenua"] and cons["CI"]
    assert acc["ingenua"] / n > 2.2
    assert acc["CI"] / n <= 2.02
    assert abs(traza(Pi_real) - traza(real_cov(W1i, W2i))) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
