#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B07-C18: búsqueda y ordenamiento, con conteo de comparaciones.

Datos PUBLICADOS: semieje mayor de los ocho planetas (NASA NSSDC, fichas individuales,
consultadas el 2026-11-05), convertido a unidades de la distancia de la Tierra (149,598e6
km). Datos SINTÉTICOS: listas de números pseudoaleatorios generadas con
random.Random(2026) para medir el costo (la semilla las hace reproducibles).
Modelo: el costo de un algoritmo se mide contando comparaciones, que no depende del
computador (a diferencia del tiempo).
Supuestos: los elementos son comparables con `<`; la búsqueda binaria exige lista ordenada.
Dominio de validez: listas en memoria. Tolerancia: las listas ordenadas deben coincidir
exactamente con sorted(); los recuentos teóricos se verifican como cotas.
"""

from __future__ import annotations

import bisect
import math
import random
import sys

SEMIEJES_1E6KM = [("Mercurio", 57.909), ("Venus", 108.210), ("Tierra", 149.598), ("Marte", 227.956),
                  ("Júpiter", 778.479), ("Saturno", 1432.041), ("Urano", 2867.043), ("Neptuno", 4514.953)]
TIERRA = 149.598


def busqueda_lineal(lista, objetivo):
    """Devuelve (índice o -1, comparaciones) recorriendo la lista de izquierda a derecha."""
    comparaciones = 0
    for i, x in enumerate(lista):
        comparaciones += 1
        if x == objetivo:
            return i, comparaciones
    return -1, comparaciones


def busqueda_binaria(lista_ordenada, objetivo):
    """Devuelve (índice o -1, comparaciones) en una lista ORDENADA, dividiendo a la mitad."""
    bajo, alto, comparaciones = 0, len(lista_ordenada) - 1, 0
    while bajo <= alto:
        medio = (bajo + alto) // 2
        comparaciones += 1
        if lista_ordenada[medio] == objetivo:
            return medio, comparaciones
        comparaciones += 1
        if lista_ordenada[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1, comparaciones


def ordenar_insercion(lista):
    """Devuelve (lista nueva ordenada, comparaciones) por inserción; no modifica la original."""
    a = list(lista)
    comparaciones = 0
    for i in range(1, len(a)):
        valor = a[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if a[j] > valor:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = valor
    return a, comparaciones


def ordenar_mezcla(lista):
    """Devuelve (lista nueva ordenada, comparaciones) por mezcla; es estable."""
    if len(lista) <= 1:
        return list(lista), 0
    medio = len(lista) // 2
    izq, c1 = ordenar_mezcla(lista[:medio])
    der, c2 = ordenar_mezcla(lista[medio:])
    resultado, i, j, c = [], 0, 0, 0
    while i < len(izq) and j < len(der):
        c += 1
        if der[j] < izq[i]:
            resultado.append(der[j])
            j += 1
        else:
            resultado.append(izq[i])
            i += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado, c1 + c2 + c


def pruebas() -> None:
    azar = random.Random(2026)
    for _ in range(300):                                                # listas de tamaños 0..40 con repetidos
        datos = [azar.randint(0, 20) for _ in range(azar.randint(0, 40))]
        assert ordenar_insercion(datos)[0] == sorted(datos)
        assert ordenar_mezcla(datos)[0] == sorted(datos)
    assert ordenar_insercion([])[0] == [] and ordenar_mezcla([5])[0] == [5]          # bordes
    asc, desc = list(range(50)), list(range(49, -1, -1))
    assert ordenar_insercion(asc)[1] == 49                                            # ya ordenada: n-1
    assert ordenar_insercion(desc)[1] == 50 * 49 // 2                                 # inversa: n(n-1)/2
    pares = [(2, "a"), (1, "b"), (2, "c"), (1, "d")]
    ordenados, _ = ordenar_mezcla([p[0] for p in pares])
    assert ordenados == [1, 1, 2, 2]
    por_clave = sorted(pares, key=lambda p: p[0])
    assert [p[1] for p in por_clave] == ["b", "d", "a", "c"]                          # sorted es estable
    lista = sorted(azar.sample(range(10_000), 500))
    for objetivo in (lista[0], lista[-1], lista[250], -1, 10_001):
        idx, c = busqueda_binaria(lista, objetivo)
        esperado = bisect.bisect_left(lista, objetivo)
        assert (idx == esperado) if idx != -1 else (esperado == len(lista) or lista[esperado] != objetivo)
        assert c <= 2 * (math.floor(math.log2(len(lista))) + 1)                       # cota logarítmica
    assert busqueda_lineal([3, 1, 2], 2) == (2, 3) and busqueda_lineal([], 1) == (-1, 0)
    assert busqueda_binaria([], 1) == (-1, 0)
    ordenados_a = [s for _, s in sorted(SEMIEJES_1E6KM, key=lambda p: p[1])]
    assert ordenados_a == [s for _, s in SEMIEJES_1E6KM]                              # ya vienen ordenados


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK")
    semiejes_au = [s / TIERRA for _, s in SEMIEJES_1E6KM]
    nombres = [n for n, _ in SEMIEJES_1E6KM]
    objetivo = 2.7                                                     # distancia de ejemplo (en distancias terrestres)
    pos = bisect.bisect_left(semiejes_au, objetivo)
    print(f"Una órbita a {objetivo} distancias terrestres queda entre {nombres[pos - 1]} y {nombres[pos]}"
          f" (semiejes {semiejes_au[pos - 1]:.3f} y {semiejes_au[pos]:.3f})")
    print(f"{'n':>7}{'lineal (peor)':>15}{'binaria':>9}{'inserción':>12}{'mezcla':>9}{'sorted':>8}")
    for n in (8, 100, 1000, 5000):
        azar = random.Random(2026)
        datos = [azar.random() for _ in range(n)]
        ordenada, c_mez = ordenar_mezcla(datos)
        _, c_ins = ordenar_insercion(datos)
        _, c_bin = busqueda_binaria(ordenada, -1.0)
        _, c_lin = busqueda_lineal(datos, -1.0)
        print(f"{n:>7}{c_lin:>15}{c_bin:>9}{c_ins:>12}{c_mez:>9}{'  ok' if ordenada == sorted(datos) else ' MAL':>8}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
