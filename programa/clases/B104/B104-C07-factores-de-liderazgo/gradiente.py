#!/usr/bin/env python3
"""B104-C07: gradiente de autoridad y probabilidad de que un error sea senalado y corregido.
MODELO ILUSTRATIVO con DATOS SINTETICOS (semilla 104). No describe a ninguna tripulacion real."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO (semilla 104): tripulacion de 4 (lider + 3), un error del lider por prueba; parametros inventados")
Q_SELF, Q_OBS, M = 0.50, 0.60, 3     # el lider ve su error (0,5); cada integrante lo ve (0,6)


def habla(g):      # probabilidad de que quien lo ve lo diga (baja con el gradiente g)
    return 0.90 - 0.70 * g


def acepta(g):     # probabilidad de que el lider acepte la observacion
    return 0.95 - 0.45 * g


def analitico(g):
    p_obs = Q_OBS * habla(g) * acepta(g)
    return 1 - (1 - Q_SELF) * (1 - p_obs) ** M


def mc(g, n=200_000, seed=104):
    rng = np.random.default_rng(seed)
    propio = rng.random(n) < Q_SELF
    obs = (rng.random((n, M)) < Q_OBS) & (rng.random((n, M)) < habla(g)) & (rng.random((n, M)) < acepta(g))
    return float((propio | obs.any(axis=1)).mean())


print("\ngradiente g | P(habla) | P(acepta) | P(corregido) analitico | P(corregido) Monte Carlo | errores no corregidos por 1000")
filas = {}
for g in (0.0, 0.25, 0.5, 0.75, 1.0):
    a, m = analitico(g), mc(g)
    filas[g] = (a, m)
    print(f"{g:9.2f} {habla(g):10.2f} {acepta(g):9.2f} {a:20.4f} {m:24.4f} {1000*(1-m):26.0f}")

# Efecto de agregar un cuarto integrante con g = 0,5
p_obs = Q_OBS * habla(0.5) * acepta(0.5)
a4 = 1 - (1 - Q_SELF) * (1 - p_obs) ** 4
print(f"\nCon 4 observadores y g = 0,5: P(corregido) = {a4:.4f} (con 3: {filas[0.5][0]:.4f})")
# Cuantos observadores hacen falta con g = 1 para igualar g = 0 con 3
n_eq = np.log((1 - filas[0.0][0]) / (1 - Q_SELF)) / np.log(1 - Q_OBS * habla(1.0) * acepta(1.0))
print(f"Observadores con g = 1 para igualar el caso g = 0 con 3 observadores: {n_eq:.1f}")

assert all(abs(a - m) < 0.005 for a, m in filas.values()), "Monte Carlo debe coincidir con la formula"
vals = [filas[g][0] for g in sorted(filas)]
assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), "mas gradiente, menos correccion"
assert vals[0] > 0.9
print("Pruebas superadas.")
