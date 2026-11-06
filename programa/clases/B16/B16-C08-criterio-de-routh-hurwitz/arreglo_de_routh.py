#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C08: arreglo de Routh y número de polos en el semiplano derecho.

Datos: SINTÉTICOS. Planta con retardo de actuador, L(s) = K / (s (s + 1)(s + 2)),
con K en N m/rad (escala arbitraria). Polinomio característico
  s^3 + 3 s^2 + 2 s + K.
Modelo: arreglo de Routh (primera columna). Número de cambios de signo =
número de raíces con parte real positiva (caso regular: sin ceros en la
primera columna).
Referencia independiente: np.roots sobre 2000 polinomios aleatorios de grado 2
a 7, y la ganancia crítica analítica del cúbico s^3 + a1 s^2 + a2 s + K:
Kcrit = a1 a2 = 6, con raíces imaginarias +-j sqrt(a2) = +-j 1.4142.
Supuestos: coeficientes reales, caso regular. Tolerancia: coincidencia
exacta del conteo en todos los polinomios regulares.
"""
from __future__ import annotations
import platform, sys
import numpy as np


def routh_primera_columna(coef):
    """Primera columna del arreglo de Routh (None si aparece un cero: caso especial)."""
    c = [float(x) for x in coef]
    n = len(c) - 1
    f1, f2 = c[0::2], c[1::2]
    f2 = f2 + [0.0] * (len(f1) - len(f2))
    col = [f1[0], f2[0]]
    filas = [f1, f2]
    for _ in range(n - 1):
        a, b = filas[-2], filas[-1]
        if b[0] == 0.0:
            return None
        nueva = [(b[0] * a[j + 1] - a[0] * b[j + 1]) / b[0] if j + 1 < len(a) else 0.0
                 for j in range(len(a) - 1)]
        nueva += [0.0] * (len(a) - len(nueva))
        filas.append(nueva)
        col.append(nueva[0])
    return col


def semiplano_derecho_routh(coef):
    col = routh_primera_columna(coef)
    if col is None or any(x == 0.0 for x in col):
        return None
    return sum(1 for x, y in zip(col, col[1:]) if x * y < 0)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    for K in (2.0, 5.9, 6.1, 10.0):
        col = routh_primera_columna([1, 3, 2, K])
        print(f"K = {K:4.1f}: primera columna {np.round(col, 4)}; cambios de signo "
              f"{semiplano_derecho_routh([1,3,2,K])}; raíces {np.round(np.roots([1,3,2,K]), 4)}")
    prueba(semiplano_derecho_routh([1, 3, 2, 2.0]) == 0, "K=2 estable")
    prueba(semiplano_derecho_routh([1, 3, 2, 10.0]) == 2, "K=10 inestable")
    r = np.roots([1, 3, 2, 6.0])
    print(f"K crítico = 6: raíces imaginarias {np.round(r[np.abs(r.real) < 1e-9], 6)}; sqrt(2) = {np.sqrt(2):.6f}")
    prueba(np.allclose(sorted(np.abs(r.imag))[-1], np.sqrt(2), atol=1e-6), "cruce en j sqrt 2")

    rng = np.random.default_rng(16)
    n_ok = n_omit = 0
    for _ in range(2000):
        grado = int(rng.integers(2, 8))
        coef = rng.normal(size=grado + 1)
        coef[0] = abs(coef[0]) + 0.1
        cnt = semiplano_derecho_routh(coef)
        if cnt is None:
            n_omit += 1
            continue
        ref = int(np.sum(np.roots(coef).real > 0))
        prueba(cnt == ref, f"conteo distinto en {coef}")
        n_ok += 1
    print(f"aleatorios: {n_ok} coincidencias exactas con np.roots; {n_omit} casos especiales omitidos")
    prueba(n_ok > 1900, "casi todos regulares")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
