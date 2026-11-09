#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B60-C03: integracion de una red quimica rigida con Euler explicito e implicito.

Datos: SINTETICOS. La red es la de tres especies y tres reacciones del problema rigido clasico de Robertson,
con constantes 0.04, 1e4 y 3e7 (unidades adimensionales de ejemplo: tiempo en unidades arbitrarias, abundancias
que suman 1). Los coeficientes se escribieron de memoria como problema de prueba: NO se consultaron en una fuente
y NO representan una red astroquimica. La referencia independiente es el metodo implicito Radau de SciPy
(rtol = 1e-10, atol = 1e-12) si SciPy esta instalado; la documentacion de solve_ivp se consulto el 2026-11-09.
Modelo: Euler explicito de paso fijo; Euler implicito con Newton (Jacobiano analitico) y control de paso por
doble paso con extrapolacion de Richardson (orden 2).
Supuestos: sin estiramiento de la red por temperatura; la rigidez es el cociente entre escalas de tiempo.
Tolerancias: Euler implicito adaptativo (rtol = 1e-4, atol = 1e-9 por paso) frente a la referencia: error relativo < 1e-3
en y1, y3 al final; conservacion de la suma < 1e-9.
"""
from __future__ import annotations
import math, platform

K1, K2, K3 = 0.04, 1.0e4, 3.0e7


def f(y):
    y1, y2, y3 = y
    return [-K1 * y1 + K2 * y2 * y3, K1 * y1 - K2 * y2 * y3 - K3 * y2 * y2, K3 * y2 * y2]


def jac(y):
    y1, y2, y3 = y
    return [[-K1, K2 * y3, K2 * y2],
            [K1, -K2 * y3 - 2 * K3 * y2, -K2 * y2],
            [0.0, 2 * K3 * y2, 0.0]]


def resolver(A, b):
    n = len(b)
    M = [fila[:] + [b[i]] for i, fila in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            fac = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= fac * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][c] * x[c] for c in range(i + 1, n))) / M[i][i]
    return x


def euler_implicito(y, h):
    """Un paso: resuelve z - y - h f(z) = 0 con Newton."""
    z = y[:]
    for _ in range(50):
        F = [z[i] - y[i] - h * f(z)[i] for i in range(3)]
        J = jac(z)
        A = [[(1.0 if i == j else 0.0) - h * J[i][j] for j in range(3)] for i in range(3)]
        dz = resolver(A, [-v for v in F])
        z = [z[i] + dz[i] for i in range(3)]
        if max(abs(v) for v in dz) < 1e-14 + 1e-12 * max(abs(v) for v in z):
            return z
    raise RuntimeError("Newton no convergio")


def integrar_implicito(y0, t_fin, rtol=1e-4, atol=1e-9, h0=1e-6):
    t, y, h, pasos, rechazos = 0.0, y0[:], h0, 0, 0
    while t < t_fin:
        h = min(h, t_fin - t)
        completo = euler_implicito(y, h)
        medio = euler_implicito(euler_implicito(y, h / 2), h / 2)
        err = max(abs(medio[i] - completo[i]) / (atol + rtol * abs(medio[i])) for i in range(3))
        if err <= 1.0:
            y = [2 * medio[i] - completo[i] for i in range(3)]   # Richardson
            t += h
            pasos += 1
        else:
            rechazos += 1
        h *= min(4.0, max(0.2, 0.9 / math.sqrt(max(err, 1e-10))))
    return y, pasos, rechazos


def euler_explicito(y0, t_fin, h):
    y, n = y0[:], int(round(t_fin / h))
    for _ in range(n):
        d = f(y)
        y = [y[i] + h * d[i] for i in range(3)]
        if not all(math.isfinite(v) and abs(v) < 1e12 for v in y):
            return y, False
    return y, True


def main():
    print(f"Python {platform.python_version()}")
    y0 = [1.0, 0.0, 0.0]
    print("Red SINTETICA de tres especies (problema de prueba, no astroquimico); suma de abundancias = 1")
    J = jac([0.7158, 9.186e-6, 0.2842])
    lam_max = abs(J[1][1])
    print(f"Escalas en el estado y(40) (pendiente diagonal de y2): tiempo lento ~ 1/{K1} = {1 / K1:.0f} ; tiempo rapido ~ 1/{lam_max:.2e} = {1 / lam_max:.2e} ; cociente ~ {lam_max / K1:.1e}")
    print(f"Limite de estabilidad de Euler explicito: h < 2/|lambda| = {2 / lam_max:.1e}")
    print("\nEuler explicito hasta t = 0.1 (h por debajo y por encima del limite):")
    for h in (1e-4, 1e-3, 4e-3, 1e-2):
        y, ok = euler_explicito(y0, 0.1, h)
        print(f"  h = {h:.0e}: {'estable' if ok else 'DIVERGE'} ; y = " + (", ".join(f"{v:.5f}" for v in y) if ok else "fuera de rango"))
    t_fin = 40.0
    y, pasos, rech = integrar_implicito(y0, t_fin)
    print(f"\nEuler implicito adaptativo hasta t = {t_fin:g}: {pasos} pasos aceptados, {rech} rechazados")
    print(f"  y1 = {y[0]:.6f}  y2 = {y[1]:.4e}  y3 = {y[2]:.6f}  suma - 1 = {sum(y) - 1:.1e}")
    print(f"  pasos que necesitaria un Euler explicito estable: {t_fin / (2 / lam_max):.1e} (h = {2 / lam_max:.0e})")
    ok = True
    try:
        import scipy
        from scipy.integrate import solve_ivp
        sol = solve_ivp(lambda t, v: f(v), (0, t_fin), y0, method="Radau", jac=lambda t, v: jac(v), rtol=1e-10, atol=1e-12)
        ref = sol.y[:, -1]
        e1 = abs(y[0] / ref[0] - 1)
        e3 = abs(y[2] / ref[2] - 1)
        print(f"\nReferencia SciPy {scipy.__version__} Radau (rtol 1e-10, atol 1e-12): y1 = {ref[0]:.6f}  y2 = {ref[1]:.4e}  y3 = {ref[2]:.6f} ; {sol.t.size - 1} pasos")
        print(f"  error relativo del Euler implicito: y1 {e1:.1e} ; y3 {e3:.1e}")
        ok = e1 < 1e-3 and e3 < 1e-3
    except ImportError:
        print("\nSciPy no instalado: se omite la referencia (SIN contraste independiente).")
    assert ok and abs(sum(y) - 1) < 1e-9
    assert not euler_explicito(y0, 0.1, 1e-2)[1]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
