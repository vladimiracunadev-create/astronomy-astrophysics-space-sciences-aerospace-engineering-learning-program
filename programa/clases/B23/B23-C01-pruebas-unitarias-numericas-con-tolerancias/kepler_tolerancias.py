#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B23-C01: pruebas numéricas con tolerancias explícitas.

Datos: ninguno externo; los casos de prueba son SINTÉTICOS y se deducen a mano.
Modelo: ecuación de Kepler  M = E - e sin(E)  (M anomalía media, E anomalía
excéntrica, ambas en radianes, 0 <= e < 1), resuelta por Newton.
Supuestos: órbita elíptica de dos cuerpos; M se reduce al intervalo [0, 2π).
Validez: 0 <= e <= 0.9 en esta demostración; no se usa para e cercano a 1.
Tolerancias: residuo |E - e sin E - M| <= 4·(2π)·u (u = precisión de máquina; los
argumentos llegan a 2π); casos
exactos con error relativo <= 1e-12, con tolerancia absoluta explícita en 0.
Contraste de referencia independiente: bisección (sin derivadas) y casos
analíticos M=0, M=π, e=0.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np

U = np.finfo(float).eps  # 2.22e-16


def kepler_newton(M, e, tol=1e-14, itmax=50):
    """Resuelve E - e sin E = M. Devuelve E (rad)."""
    M = math.fmod(M, 2 * math.pi)
    E = M if e < 0.8 else math.pi
    for _ in range(itmax):
        f = E - e * math.sin(E) - M
        dE = f / (1.0 - e * math.cos(E))
        E -= dE
        if abs(dE) < tol:
            return E
    raise RuntimeError("Newton no convergió")


def kepler_biseccion(M, e):
    """Referencia independiente: bisección en [0, 2π] (f es creciente)."""
    M = math.fmod(M, 2 * math.pi)
    lo, hi = 0.0, 2 * math.pi
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid - e * math.sin(mid) < M:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --- versiones con defectos deliberados (mutantes) ---
def mutante_signo(M, e):      # signo equivocado en la derivada
    E = M
    for _ in range(50):
        E -= (E - e * math.sin(E) - M) / (1.0 + e * math.cos(E))
    return E


def _newton_fijo(M, e, n):  # n iteraciones de Newton, sin criterio de parada
    E = M
    for _ in range(n):
        E -= (E - e * math.sin(E) - M) / (1.0 - e * math.cos(E))
    return E


def mutante_3_iter(M, e):
    return _newton_fijo(M, e, 3)


def mutante_5_iter(M, e):
    return _newton_fijo(M, e, 5)


def mutante_primer_orden(M, e):  # aproximación E ≈ M + e sin M (truncada)
    return M + e * math.sin(M)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def cerca(a, b, rtol, atol):
    """Criterio de NumPy: |a-b| <= atol + rtol*|b|."""
    return abs(a - b) <= atol + rtol * abs(b)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  u={U:.3e}")

    # 1. Los valores por defecto engañan
    print("np.isclose(1e-9, 2e-9) =", bool(np.isclose(1e-9, 2e-9)),
          "(atol por defecto 1e-8 oculta un factor 2)")
    import math as m
    print("math.isclose(1e-10, 0) =", m.isclose(1e-10, 0),
          "| con abs_tol=1e-9:", m.isclose(1e-10, 0, abs_tol=1e-9))
    print("0.1+0.2 == 0.3:", 0.1 + 0.2 == 0.3, "| isclose:", m.isclose(0.1 + 0.2, 0.3))
    print(f"ulp(1.0)={m.ulp(1.0):.3e}  ulp(1e6)={m.ulp(1e6):.3e}  ulp(0.0)={m.ulp(0.0):.3e}")

    # 2. Casos exactos (deducidos a mano)
    prueba(kepler_newton(0.0, 0.5) == 0.0, "M=0 => E=0 exacto")
    prueba(cerca(kepler_newton(math.pi, 0.5), math.pi, 4 * U, 0.0), "M=π => E=π")
    for M in (0.3, 1.0, 2.5, 5.0):
        prueba(cerca(kepler_newton(M, 0.0), M, 4 * U, 0.0), "e=0 => E=M")
    print("casos exactos (M=0, M=π, e=0): correctos")

    # 3. Propiedad: residuo pequeño y acuerdo con la bisección
    peor_res, peor_dif = 0.0, 0.0
    for e in (0.0, 0.0167, 0.2, 0.5, 0.9):
        for M in np.linspace(0.01, 2 * math.pi - 0.01, 25):
            E = kepler_newton(M, e)
            res = abs(E - e * math.sin(E) - M)
            peor_res = max(peor_res, res)
            peor_dif = max(peor_dif, abs(E - kepler_biseccion(M, e)))
    print(f"peor residuo = {peor_res:.2e}   peor |Newton-bisección| = {peor_dif:.2e}")
    prueba(peor_res <= 4 * 2 * math.pi * U, "residuo dentro de la cota")
    prueba(peor_dif <= 1e-13, "Newton coincide con bisección")

    # 4. Sensibilidad de la tolerancia: cuáles mutantes detecta cada una
    casos = [(M, e) for e in (0.0167, 0.5, 0.9) for M in (0.5, 1.5, 3.0, 4.5)]
    candidatos = {"signo": mutante_signo, "3 iteraciones": mutante_3_iter,
                  "primer orden": mutante_primer_orden,
                  "5 iteraciones": mutante_5_iter}
    print("\ntolerancia relativa -> mutantes detectados (de 4)")
    detect = {}
    for rtol in (1e-1, 1e-3, 1e-6, 1e-9, 1e-12):
        vivos = []
        for nombre, f in candidatos.items():
            pasa = all(cerca(f(M, e), kepler_biseccion(M, e), rtol, 0.0) for M, e in casos)
            if pasa:
                vivos.append(nombre)
        detect[rtol] = len(candidatos) - len(vivos)
        print(f"  rtol={rtol:.0e}: detectados {len(candidatos) - len(vivos)}; sobreviven {vivos or '—'}")
    prueba(detect[1e-12] == 4, "con rtol=1e-12 caen los cuatro mutantes")
    prueba(detect[1e-1] < 4, "una tolerancia holgada deja vivo algún mutante")
    # La implementación correcta pasa incluso con la tolerancia más estricta
    prueba(all(cerca(kepler_newton(M, e), kepler_biseccion(M, e), 1e-12, 0.0)
               for M, e in casos), "la versión correcta pasa rtol=1e-12")
    print("\nPruebas superadas.")


if __name__ == "__main__":
    main()
