#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C29: escalada y desescalada como cadena de Markov con y sin medidas de fomento de la confianza (probabilidades SINTETICAS, escenario abstracto).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no modela ninguna crisis real ni a ningun Estado.
Texto consultado (2026-11-11, nota de legal.un.org): art. XI del tratado de 1967: informar en la mayor medida posible sobre las actividades espaciales, y art. IX: consultas y cooperacion.
NO consultado: documentos de medidas de transparencia y fomento de la confianza ni teoria de disuasion.
Modelo: estados transitorios 0 calma, 1 tension, 2 incidente, 3 crisis; absorbentes: R (resuelto) y C (conflicto). Cada paso (semana sintetica) pasa de un estado al siguiente
o a uno anterior con probabilidades inventadas. Las medidas de confianza (transparencia) multiplican por (1 - h) las probabilidades de subir de nivel y llevan ese peso a la desescalada.
Resultado analitico: probabilidades de absorcion = (I - Q)^-1 R (matriz fundamental). Verificacion: simulacion con semilla 119, N = 200000, a 3 sigma.
"""
import json, math, platform, random

NOMBRES = ["calma", "tension", "incidente", "crisis"]
BASE = [  # por estado: subir, bajar, a resuelto, a conflicto
    dict(up=0.10, down=0.00, R=0.00, C=0.00),
    dict(up=0.20, down=0.15, R=0.15, C=0.00),
    dict(up=0.25, down=0.30, R=0.00, C=0.00),
    dict(up=0.00, down=0.35, R=0.05, C=0.15),
]
def matriz(h):
    """Q (4x4) y R (4x2: resuelto, conflicto). La transparencia h reduce subir y pasar a conflicto en un factor (1 - h) y lo traslada a bajar de nivel."""
    Q, Rm = [], []
    for i, b in enumerate(BASE):
        up, toc = b["up"] * (1 - h), b["C"] * (1 - h)
        down = b["down"] + (h * (b["up"] + b["C"]) if i > 0 else 0.0)
        row = [0.0] * 4
        if i < 3: row[i + 1] = up
        if i > 0: row[i - 1] = down
        row[i] = 1.0 - sum(row) - b["R"] - toc
        Q.append(row); Rm.append([b["R"], toc])
    return Q, Rm
def resolver(A, B):
    """Gauss-Jordan para A X = B (A 4x4, B 4x2)."""
    n = len(A)
    M = [A[i][:] + B[i][:] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        d = M[i][i]; M[i] = [x / d for x in M[i]]
        for r in range(n):
            if r != i:
                f = M[r][i]; M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return [row[n:] for row in M]
def absorcion(h):
    Q, Rm = matriz(h)
    for i in range(4):
        assert abs(sum(Q[i]) + sum(Rm[i]) - 1) < 1e-12 and min(Q[i] + Rm[i]) >= -1e-12, (h, i, Q[i], Rm[i])
    A = [[(1.0 if i == j else 0.0) - Q[i][j] for j in range(4)] for i in range(4)]
    return resolver(A, Rm), Q, Rm
def simular(h, inicio, N, rng):
    Q, Rm = matriz(h); c = 0
    for _ in range(N):
        s = inicio
        while True:
            u = rng.random(); acc = 0.0; nuevo = None
            for j in range(4):
                acc += Q[s][j]
                if u < acc: nuevo = j; break
            if nuevo is None:
                acc2 = acc + Rm[s][0]
                if u < acc2: break        # resuelto
                c += 1; break              # conflicto
            s = nuevo
    return c / N
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Cadena de Markov ABSTRACTA con probabilidades SINTETICAS; art. XI y IX consultados 2026-11-11; textos de fomento de la confianza NO consultados.")
rng = random.Random(119)
N = 200000
res = {}
for h in (0.0, 0.3, 0.6):
    X, Q, Rm = absorcion(h)
    pC = [X[i][1] for i in range(4)]
    mc = simular(h, 1, N, rng)
    sg = math.sqrt(pC[1] * (1 - pC[1]) / N)
    assert abs(mc - pC[1]) < 3 * sg + 1e-4, (h, mc, pC[1])
    res[h] = pC
    print(f"transparencia h = {h:.1f}: P(conflicto) desde calma {pC[0]:.4f} ; tension {pC[1]:.4f} (simulado {mc:.4f}) ; incidente {pC[2]:.4f} ; crisis {pC[3]:.4f}")
red = 100 * (1 - res[0.6][1] / res[0.0][1])
print(f"Reduccion de P(conflicto) desde tension con h = 0.6: {red:.1f} %")
assert res[0.6][1] < res[0.3][1] < res[0.0][1]
print("CLAVES " + json.dumps({"c0": "%.4f" % res[0.0][1], "c3": "%.4f" % res[0.3][1], "c6": "%.4f" % res[0.6][1], "red": "%.1f" % red, "cris0": "%.4f" % res[0.0][3], "cris6": "%.4f" % res[0.6][3]}))
print("Pruebas superadas.")
