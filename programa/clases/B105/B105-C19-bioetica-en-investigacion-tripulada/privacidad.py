#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C19: riesgo de reidentificacion en cohortes pequenas y privacidad diferencial (datos SINTETICOS).

Pool SINTETICO de 150 personas con cuasi-identificadores: edad (30-60), sexo (2 valores), profesion (4 valores) y mision (5 valores); una cohorte de 6 se
extrae al azar (semilla 105). k-anonimato de una tabla = tamano minimo de grupo con los mismos cuasi-identificadores; fraccion de registros unicos.
Generalizacion: edad en bandas de 5 o de 10 anios. Privacidad diferencial: mecanismo de Laplace para una media con rango [a, b]: escala = (b - a)/(n eps);
error absoluto medio esperado = escala. El informe Belmont (HHS, 1979) plantea respeto por las personas, beneficencia y justicia: en esta clase se consulta SOLO la
lista de los tres principios a traves de un resumen de busqueda web (2026-11-10), no el texto. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np


def k_anon(filas):
    cuentas = {}
    for f in filas:
        cuentas[f] = cuentas.get(f, 0) + 1
    return min(cuentas.values()), sum(1 for f in filas if cuentas[f] == 1) / len(filas)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): pool de 150 personas y cohortes extraidas al azar; ninguna persona real")
    rng = np.random.default_rng(105)
    n_pool = 150
    edad = rng.integers(30, 61, n_pool); sexo = rng.integers(0, 2, n_pool); prof = rng.integers(0, 4, n_pool); mision = rng.integers(0, 5, n_pool)
    cohorte = rng.choice(n_pool, 6, replace=False)
    print("Cohorte de 6 personas: k-anonimato y fraccion de registros unicos segun los cuasi-identificadores:")
    esquemas = {
        "edad exacta, sexo, profesion, mision": lambda i: (edad[i], sexo[i], prof[i], mision[i]),
        "banda de edad 5 anios, sexo, profesion, mision": lambda i: (edad[i] // 5, sexo[i], prof[i], mision[i]),
        "banda de 10 anios, sexo, mision": lambda i: (edad[i] // 10, sexo[i], mision[i]),
        "solo banda de 10 anios": lambda i: (edad[i] // 10,),
        "solo mision": lambda i: (mision[i],),
    }
    res = {}
    for nombre, f in esquemas.items():
        k, u = k_anon([f(i) for i in cohorte])
        res[nombre] = (k, u)
        print(f"  {nombre:50s} k = {k}; unicos = {u:.2f}")
    # probabilidad de unicidad al repetir miles de cohortes
    print("Fraccion media de registros unicos en 5000 cohortes de 6 (aleatorias del pool):")
    for nombre, f in esquemas.items():
        us = []
        for _ in range(5000):
            idx = rng.choice(n_pool, 6, replace=False)
            us.append(k_anon([f(i) for i in idx])[1])
        print(f"  {nombre:50s} {np.mean(us):.3f}")
    print("Privacidad diferencial (Laplace) para la media de una medida en [0, 100] con n = 6: error absoluto medio esperado = (b-a)/(n eps)")
    for eps in (0.1, 0.5, 1.0, 5.0):
        esc = 100 / (6 * eps)
        sim = np.mean(np.abs(rng.laplace(0, esc, 100000)))
        print(f"  eps = {eps:4.1f}: escala {esc:7.2f}; error medio simulado {sim:7.2f} (sobre una media de rango 100)")
    print(f"Con n = 6 y eps = 1 el ruido esperado es {100 / 6:.1f} puntos sobre 100: la utilidad se destruye; con n = 600 seria {100 / 600:.2f}")
    assert res["edad exacta, sexo, profesion, mision"][1] >= res["solo mision"][1]
    assert res["solo mision"][0] >= 1
    assert abs(np.mean(np.abs(rng.laplace(0, 16.67, 200000))) - 16.67) < 0.3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
