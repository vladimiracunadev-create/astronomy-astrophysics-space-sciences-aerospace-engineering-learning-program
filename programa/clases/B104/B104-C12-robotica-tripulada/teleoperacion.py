#!/usr/bin/env python3
"""B104-C12: teleoperacion con retardo: mover y esperar frente a autonomia supervisada.
Tiempos de tarea SINTETICOS (semilla 104); distancias estandar no consultadas."""
import sys
import numpy as np

C = 299_792.458
print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO (semilla 104): tarea de 12 movimientos de 10 s; 5 % necesitan correccion; distancias estandar no consultadas")
N_MOV, T_MOV, T_VER, P_ERR = 12, 10.0, 5.0, 0.05
T_AUTO_SEG, N_OBJ = 25.0, 3      # supervisada: 3 objetivos de alto nivel de 25 s cada uno

escenarios = [("brazo de la ISS desde la ISS (0 s)", 0.0), ("ISS a tierra (0,3 s ida, ilustrativo)", 0.3),
              ("Luna (1,28 s ida)", 384_400 / C), ("Marte, minimo (182 s ida)", 54.6e6 / C), ("Marte, maximo (1 338 s ida)", 401e6 / C)]


def t_mover_esperar(d, correccion=True):
    ciclo = T_MOV + T_VER + 2 * d
    base = N_MOV * ciclo
    extra = (N_MOV * P_ERR) * ciclo if correccion else 0.0   # valor esperado de movimientos repetidos
    return base + extra


def t_supervisada(d):
    return N_OBJ * (2 * d + T_AUTO_SEG)


print("\nescenario | ida [s] | mover y esperar [s] | supervisada [s] | cociente")
res = {}
for n, d in escenarios:
    a, b = t_mover_esperar(d), t_supervisada(d)
    res[n] = (a, b)
    print(f"{n:42s} {d:9.2f} {a:14.1f} {b:14.1f} {a/b:9.2f}")

# Monte Carlo del mover y esperar (movimientos con correccion aleatoria)
rng = np.random.default_rng(104)
d = 54.6e6 / C
n = 100_000
mov = N_MOV + rng.binomial(N_MOV, P_ERR, size=n)       # repeticiones aleatorias
tiempos = mov * (T_MOV + T_VER + 2 * d)
print(f"\nMarte (minimo), Monte Carlo ({n} corridas): media {tiempos.mean():.1f} s; percentil 95 {np.percentile(tiempos,95):.1f} s; formula {res[escenarios[3][0]][0]:.1f} s")

assert abs(tiempos.mean() - res[escenarios[3][0]][0]) / res[escenarios[3][0]][0] < 0.005
assert res[escenarios[0][0]][0] < res[escenarios[2][0]][0] < res[escenarios[4][0]][0]
assert res[escenarios[4][0]][1] < res[escenarios[4][0]][0] / 4
print("Pruebas superadas.")
