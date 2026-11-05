#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B04-C03: sistemas lineales, calibración y sensibilidad.

Datos: SINTÉTICOS (inventados para enseñar, no son mediciones): dos estrellas de
referencia con flujo conocido y cuentas medidas de un detector; dos estaciones y
dos rumbos hacia un objeto. Modelo: cuentas = a·F + b (respuesta lineal) y
rectas de visión en el plano. Supuestos: respuesta lineal sin saturación; ángulos
exactos salvo la perturbación estudiada; plano euclídeo.
Validez: sistemas 2x2 y 3x3 no singulares. Tolerancia: exacta con Fraction en las
pruebas; 1e-9 en las demás.
"""
from __future__ import annotations
import math, platform, sys
from fractions import Fraction


def resolver(A, b):
    """Eliminación gaussiana con pivoteo parcial. Devuelve x; ValueError si singular."""
    n = len(A)
    M = [list(map(lambda v: v, fila)) + [b[i]] for i, fila in enumerate(A)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        if M[p][k] == 0:
            raise ValueError("sistema singular")
        M[k], M[p] = M[p], M[k]
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= f * M[k][j]
    x = [0] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def pruebas():
    # Exacto con fracciones: x + y = 3 ; x - y = 1  ->  (2, 1)
    A = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(-1)]]
    assert resolver(A, [Fraction(3), Fraction(1)]) == [2, 1]
    # 3x3 exacto: solución conocida (1, 2, 3)
    A3 = [[Fraction(v) for v in f] for f in ([2, 1, -1], [-3, -1, 2], [-2, 1, 2])]
    xs = [1, 2, 3]
    b3 = [sum(a * x for a, x in zip(f, xs)) for f in A3]
    assert resolver(A3, b3) == xs
    # Singular: filas proporcionales
    try:
        resolver([[1.0, 2.0], [2.0, 4.0]], [1.0, 2.0])
        raise AssertionError("debía fallar")
    except ValueError:
        pass
    # Residuo pequeño en coma flotante
    A2 = [[3.0, 2.0], [1.0, -4.0]]
    x = resolver(A2, [7.0, -5.0])
    r = [sum(a * v for a, v in zip(f, x)) - bi for f, bi in zip(A2, [7.0, -5.0])]
    assert max(abs(v) for v in r) < 1e-12


def interseccion(est1, rumbo1, est2, rumbo2):
    """Intersección de dos rectas de visión. Rumbo = ángulo desde el eje x (grados).
    Recta i: sin(th) x - cos(th) y = sin(th) x_i - cos(th) y_i."""
    A, b = [], []
    for (xi, yi), th in ((est1, rumbo1), (est2, rumbo2)):
        s, c = math.sin(math.radians(th)), math.cos(math.radians(th))
        A.append([s, -c]); b.append(s * xi - c * yi)
    return resolver(A, b)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"Python {platform.python_version()} (solo biblioteca estándar)")
    print("Pruebas: OK (2x2 y 3x3 exactos con Fraction; singular detectado; residuo < 1e-12)")
    # Calibración (datos SINTÉTICOS): cuentas = a F + b
    (F1, N1), (F2, N2) = (100.0, 2150.0), (400.0, 8450.0)
    a, b = resolver([[F1, 1.0], [F2, 1.0]], [N1, N2])
    print(f"\nCalibración (sintética): a = {a:.4f} cuentas/unidad, b = {b:.4f} cuentas")
    print(f"Fuente con 5000 cuentas -> flujo F = (N - b)/a = {(5000 - b) / a:.2f} unidades")
    # Sensibilidad: estaciones a 0 y 10 km de distancia, objeto cerca de (4, 6)
    est1, est2 = (0.0, 0.0), (10.0, 0.0)
    for th1, th2, etiqueta in ((56.31, 123.69, "rumbos bien separados"),
                               (56.31, 56.31 + 1.0, "rumbos casi paralelos")):
        x0, y0 = interseccion(est1, th1, est2, th2)
        x1, y1 = interseccion(est1, th1 + 0.1, est2, th2)
        print(f"\n{etiqueta}: ({x0:.3f}, {y0:.3f}) km;  con +0,1° en el primer rumbo: "
              f"({x1:.3f}, {y1:.3f}) km;  desplazamiento {math.hypot(x1-x0, y1-y0):.3f} km")


if __name__ == "__main__":
    main()
