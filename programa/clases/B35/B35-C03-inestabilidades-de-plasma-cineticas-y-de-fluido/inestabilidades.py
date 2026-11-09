#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C03: tasas de crecimiento de la inestabilidad de dos haces frios y de Kelvin-Helmholtz con campo paralelo.

Datos: ninguna constante fisica ni dato observado. Todo se expresa en unidades normalizadas (omega_p = 1; v_A = 1) y los parametros (k v0, U/v_A) son ILUSTRATIVOS (sinteticos).
Modelo: (1) dos haces frios simetricos de velocidades +-v0 y densidad total n0: 1 = (wp^2/2)[1/(w-k v0)^2 + 1/(w+k v0)^2], es decir el polinomio de cuarto grado
(w^2-a^2)^2 - wp^2 (w^2+a^2) = 0 con a = k v0; (2) lamina de vorticidad incompresible con densidades iguales y campo B paralelo al flujo: w^2 = k^2 (vA^2 - U^2/4) (U = salto de velocidad).
Dos vias independientes: la solucion cerrada de la ecuacion cuadratica en w^2 y las raices numericas del polinomio por el metodo de Durand-Kerner; ademas el maximo analitico gamma = wp/(2 sqrt 2)
en k v0 = sqrt(3/8) wp.
Supuestos: haces frios, no colisionales, sin campo magnetico en el caso de dos haces; fluido incompresible en Kelvin-Helmholtz. Validez: lineal.
Tolerancia: raices numericas frente a la forma cerrada con error < 1e-9; maximo de crecimiento con error < 1e-4.
"""
from __future__ import annotations
import cmath, math, platform, sys

def durand_kerner(coef, it=500):
    """Raices de un polinomio con coeficientes (de mayor a menor grado); el primero debe ser 1."""
    n = len(coef) - 1
    r = [(0.4 + 0.9j) ** k for k in range(n)]
    for _ in range(it):
        nuevo = []
        for i in range(n):
            p = 0
            for c in coef:
                p = p * r[i] + c
            q = 1
            for j in range(n):
                if j != i:
                    q *= (r[i] - r[j])
            nuevo.append(r[i] - p / q)
        r = nuevo
    return r

def gamma_dos_haces(a):
    """Tasa de crecimiento (unidades de wp) por la forma cerrada para a = k v0 / wp."""
    x = ((2 * a * a + 1) - math.sqrt(1 + 8 * a * a)) / 2  # w^2 (raiz menos), wp = 1
    return math.sqrt(-x) if x < 0 else 0.0

def gamma_numerica(a):
    # (w^2 - a^2)^2 - (w^2 + a^2) = w^4 - (2a^2 + 1) w^2 + a^4 - a^2
    raices = durand_kerner([1, 0, -(2 * a * a + 1), 0, a ** 4 - a * a])
    return max(r.imag for r in raices)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'k v0/wp':>8} {'gamma cerrada':>14} {'gamma Durand-Kerner':>20}")
    for a in (0.2, 0.4, 0.6124, 0.8, 0.95, 1.0, 1.2):
        gc, gn = gamma_dos_haces(a), gamma_numerica(a)
        print(f"{a:8.4f} {gc:14.6f} {gn:20.6f}")
        assert abs(gc - gn) < 1e-9
    amax = math.sqrt(3 / 8)
    g_an = 1 / (2 * math.sqrt(2))
    # barrido fino para localizar el maximo
    mejor = max((gamma_dos_haces(0.001 * i), 0.001 * i) for i in range(1, 1000))
    print(f"maximo analitico: k v0 = {amax:.5f} wp, gamma = {g_an:.6f} wp ; maximo del barrido: k v0 = {mejor[1]:.3f}, gamma = {mejor[0]:.6f}")
    assert abs(gamma_dos_haces(amax) - g_an) < 1e-4 and abs(mejor[0] - g_an) < 1e-4 and abs(mejor[1] - amax) < 2e-3
    # estable para k v0 >= wp (la raiz menos deja de ser negativa)
    assert gamma_dos_haces(1.0) == 0.0 and gamma_dos_haces(1.2) == 0.0
    # Kelvin-Helmholtz con B paralelo: w^2 = k^2 (vA^2 - U^2/4); polinomio en w con k = 1, vA = 1
    print(f"{'U/vA':>6} {'gamma/(k vA) cerrada':>21} {'gamma Durand-Kerner':>20}")
    for U in (0.0, 1.0, 1.9, 2.0, 2.1, 3.0, 4.0):
        g_c = math.sqrt(max(U * U / 4 - 1, 0.0))
        # (w - U/2)^2 + (w + U/2)^2 = 2  ->  w^2 + U^2/4 - 1 = 0 -> w^2 + (U^2/4 - 1) = 0
        raices = durand_kerner([1, 0, U * U / 4 - 1])
        g_n = max(r.imag for r in raices)
        g_n = max(g_n, 0.0)
        print(f"{U:6.2f} {g_c:21.6f} {g_n:20.6f}")
        assert abs(g_c - g_n) < 1e-6
    # umbral de estabilidad: U = 2 vA
    assert math.sqrt(max(1.99 ** 2 / 4 - 1, 0.0)) == 0.0 and math.sqrt(max(2.01 ** 2 / 4 - 1, 0.0)) > 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
