#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C04: combinacion de barreras independientes en un retorno de muestras (modelo didactico).

Datos: SINTETICOS e ILUSTRATIVOS. Las probabilidades de fallo por barrera son valores propuestos para el ejemplo.
NO son requisitos regulatorios, no proceden de ninguna mision y no representan la arquitectura de ninguna nave:
la politica consultada (COSPAR, 2021) no fija aqui ningun numero de este tipo.
Modelo: una muestra llega sin contencion al exterior solo si fallan TODAS las barreras en serie (sellado
primario, sellado secundario, esterilizacion de superficie de lo externo, verificacion de cierre). Con fallos
independientes, P_fuga = prod(p_i). Se contrasta con Monte Carlo (semilla fija) y se calcula el numero minimo de
barreras iguales para alcanzar una meta. Tambien se muestra el efecto de un fallo de causa comun (beta).
Sistema de referencia: probabilidades por mision, adimensionales.
Validez: didactica; supone independencia (salvo el bloque de causa comun) y un solo modo de fallo.
Tolerancias: producto analitico < 1e-15 relativo; Monte Carlo dentro de 3 sigma binomiales.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import math, platform, random

BARRERAS = {"sellado primario": 1e-2, "sellado secundario": 2e-2, "esterilizacion externa": 5e-2, "verificacion de cierre": 1e-1}


def p_fuga(ps) -> float:
    r = 1.0
    for p in ps:
        r *= p
    return r


def n_barreras(p: float, meta: float) -> int:
    return math.ceil(math.log(meta) / math.log(p) - 1e-9)


def p_fuga_causa_comun(ps, beta: float) -> float:
    """Modelo beta-factor: una fraccion beta del fallo de cada barrera es de causa comun (todas fallan a la vez)."""
    p_comun = beta * min(ps)
    indep = p_fuga([(1 - beta) * p for p in ps])
    return p_comun + indep - p_comun * indep


def montecarlo(ps, n: int = 2_000_000, semilla: int = 63):
    rng = random.Random(semilla)
    k = 0
    for _ in range(n):
        if all(rng.random() < p for p in ps):
            k += 1
    return k / n, n


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ps = list(BARRERAS.values())
    print("Barreras sinteticas (probabilidad de fallo):")
    for k, v in BARRERAS.items():
        print(f"  {k:24s} {v:g}")
    pf = p_fuga(ps)
    assert abs(pf - 1e-2 * 2e-2 * 5e-2 * 1e-1) / pf < 1e-15
    print(f"P_fuga analitica (independientes) = {pf:.3e}")
    # prueba Monte Carlo sobre un subconjunto de dos barreras (la de cuatro es demasiado rara para muestrear)
    sub = [1e-1, 2e-1]
    pm, n = montecarlo(sub)
    pa = p_fuga(sub)
    sigma = math.sqrt(pa * (1 - pa) / n)
    print(f"Subconjunto {sub}: analitica = {pa:.5f}, Monte Carlo = {pm:.5f}, 3 sigma = {3 * sigma:.5f}")
    assert abs(pm - pa) < 3 * sigma
    print("Monte Carlo dentro de 3 sigma.")
    for meta in (1e-4, 1e-6):
        n_b = n_barreras(1e-1, meta)
        print(f"Barreras iguales de p = 0.1 para P_fuga <= {meta:g}: {n_b}")
        assert n_b - 1 < math.log(meta) / math.log(0.1) <= n_b + 1e-9
    print("Efecto de causa comun (beta-factor) sobre las cuatro barreras:")
    print("  beta    P_fuga")
    prev = pf
    for beta in (0.0, 0.01, 0.1):
        v = p_fuga_causa_comun(ps, beta)
        print(f"  {beta:4.2f}   {v:.3e}")
        assert v >= prev * (1 - 1e-12) or beta == 0.0
        prev = v if beta else prev
    assert abs(p_fuga_causa_comun(ps, 0.0) - pf) / pf < 1e-12
    print("Con beta = 0 se recupera el producto independiente. Pruebas superadas.")


if __name__ == "__main__":
    main()
