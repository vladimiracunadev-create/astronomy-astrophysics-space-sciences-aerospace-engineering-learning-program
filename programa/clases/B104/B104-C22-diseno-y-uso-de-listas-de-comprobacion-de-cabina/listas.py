#!/usr/bin/env python3
"""B104-C22: probabilidad de omitir un paso con distintos formatos de lista de comprobacion y su costo en tiempo.
MODELO ILUSTRATIVO con DATOS SINTETICOS (semilla 104); probabilidades y tiempos inventados."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO (semilla 104): p de omitir un paso = 0,01 de memoria; 0,004 leer-y-hacer; 0,001 desafio-respuesta; tiempos por paso inventados")
P = {"de memoria": 0.01, "leer y hacer": 0.004, "desafio y respuesta": 0.001}
T_PASO = {"de memoria": 4.0, "leer y hacer": 7.0, "desafio y respuesta": 12.0}   # s por paso
P_INT, P_MAL = 0.05, 0.5      # probabilidad de interrupcion por lista y de retomar en un paso equivocado
rng = np.random.default_rng(104)
N = 400_000


def formula(p, n):
    return 1 - (1 - p) ** n


print("\nformato | pasos | P(al menos una omision) formula | Monte Carlo | tiempo de la lista [s]")
res = {}
for n in (10, 40):
    for f in P:
        e_mc = (rng.random((N, n)) < P[f]).any(axis=1).mean()
        res[(f, n)] = (formula(P[f], n), e_mc)
        print(f"{f:20s} {n:5d} {formula(P[f], n):28.4f} {e_mc:12.4f} {n * T_PASO[f]:18.0f}")

# Efecto de una interrupcion: con prob. P_INT la lista se retoma mal con prob. P_MAL y se omite al menos un paso
e_int = P_INT * P_MAL
print(f"\nInterrupcion (p = {P_INT}, retomar mal = {P_MAL}): P(omision por interrupcion) = {e_int:.4f}; comparable con la de leer-y-hacer con 10 pasos ({res[('leer y hacer', 10)][0]:.4f})")

# Lista corta de elementos criticos: de 40 pasos a 10 criticos
print(f"Lista de 40 pasos de memoria: {res[('de memoria', 40)][0]:.3f}; solo 10 criticos con desafio-respuesta: {res[('desafio y respuesta', 10)][0]:.4f}")

for (f, n), (a, m) in res.items():
    assert abs(a - m) < 0.004, (f, n)
assert res[("desafio y respuesta", 40)][0] < res[("leer y hacer", 40)][0] < res[("de memoria", 40)][0]
print("Pruebas superadas.")
