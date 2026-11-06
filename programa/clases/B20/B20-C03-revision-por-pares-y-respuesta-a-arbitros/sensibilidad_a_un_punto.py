#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B20-C03: ¿depende la conclusión de un solo punto? (jackknife).

Datos: SINTÉTICOS (10 pares (x, y) inventados para la clase: y = 2,00 x + 1,00
más una perturbación fija; el último punto es un valor atípico deliberado).
Modelo: recta de mínimos cuadrados y = a + b x. Un árbitro hipotético pide
repetir el ajuste quitando un punto a la vez (leave-one-out) y reportar el
rango de la pendiente. Supuestos: errores en y, sin ponderar. Validez:
ilustra una respuesta documentada a un árbitro; no es un método de rechazo
de datos. Tolerancia: 1e-12 en los casos analíticos (recta exacta).
"""

from __future__ import annotations

import sys

X = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
RUIDO = [0.2, -0.3, 0.1, 0.25, -0.2, 0.15, -0.1, -0.25, 0.3, 0.0]
Y = [2.0 * x + 1.0 + e for x, e in zip(X, RUIDO)]
Y[-1] += 6.0  # valor atípico deliberado en el último punto


def ajuste(xs, ys):
    """Mínimos cuadrados: devuelve (a, b) con y = a + b x."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    return my - b * mx, b


def jackknife(xs, ys):
    """Pendientes quitando un punto cada vez."""
    out = []
    for i in range(len(xs)):
        out.append(ajuste(xs[:i] + xs[i + 1:], ys[:i] + ys[i + 1:])[1])
    return out


def pruebas() -> None:
    xs = [0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [1.0 + 2.0 * x for x in xs]            # recta exacta
    a, b = ajuste(xs, ys)
    assert abs(a - 1.0) < 1e-12 and abs(b - 2.0) < 1e-12
    js = jackknife(xs, ys)
    assert max(js) - min(js) < 1e-12            # sin ruido, quitar un punto no cambia nada
    # caso de referencia a mano: (0,0),(1,1),(2,2),(3,6): b = 9,5/5 = 1,9 ; a = 2,25 - 1,9·1,5 = -0,6
    a, b = ajuste([0, 1, 2, 3], [0, 1, 2, 6])
    assert abs(b - 1.9) < 1e-12 and abs(a + 0.6) < 1e-12


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK | datos SINTÉTICOS")
    a, b = ajuste(X, Y)
    print(f"Ajuste con los 10 puntos: a = {a:.3f}, b = {b:.3f}")
    js = jackknife(X, Y)
    for i, pend in enumerate(js, start=1):
        print(f"  sin el punto {i:>2}: b = {pend:.3f}")
    print(f"Rango de la pendiente: {min(js):.3f} a {max(js):.3f}  (ancho {max(js) - min(js):.3f})")
    ib = max(range(len(js)), key=lambda i: abs(js[i] - b))
    print(f"Punto más influyente: {ib + 1}")
    a9, b9 = ajuste(X[:-1], Y[:-1])
    print(f"Ajuste sin el punto 10: a = {a9:.3f}, b = {b9:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
