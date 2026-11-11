#!/usr/bin/env python3
"""B104-C17: modelo de dos procesos (homeostatico y circadiano) de sueno y alerta.
Parametros ILUSTRATIVOS (la literatura original no se consulto); horarios SINTETICOS. No es una pauta de sueno."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: tau_vigilia = 18,2 h; tau_sueno = 4,2 h; S entre 0,1 y 0,9; circadiano senoidal de 24 h; NO es una pauta de sueno")
TAU_V, TAU_S, S_MIN, S_MAX = 18.2, 4.2, 0.1, 0.9
A_C, FASE = 0.12, 16.8     # amplitud y hora del maximo circadiano (ILUSTRATIVOS)
DT = 1 / 60                # 1 minuto


def simular(inicio_sueno, horas_sueno, dias=14):
    t = np.arange(0, dias * 24, DT)
    S = np.zeros_like(t)
    S[0] = 0.4
    dormido = np.zeros(t.size, dtype=bool)
    for i in range(t.size):
        h = (t[i] % 24 - inicio_sueno) % 24
        dormido[i] = h < horas_sueno
    for i in range(1, t.size):
        if dormido[i]:
            S[i] = S_MIN + (S[i - 1] - S_MIN) * np.exp(-DT / TAU_S)
        else:
            S[i] = S_MAX - (S_MAX - S[i - 1]) * np.exp(-DT / TAU_V)
    C = A_C * np.cos(2 * np.pi * (t - FASE) / 24)
    alerta = C - S + 0.5
    return t, S, C, alerta, dormido


print("\nhorario | sueno [h] | S al despertar | alerta media 08-20 h | alerta minima 08-20 h | cambio dia 13 a 14 de S [1e-4]")
res = {}
for nombre, ini, hs in (("23:00-07:00", 23, 8), ("00:00-06:00", 0, 6), ("01:00-05:00", 1, 4)):
    t, S, C, a, dorm = simular(ini, hs)
    dia14 = (t >= 13 * 24) & (t < 14 * 24)
    laboral = dia14 & (t % 24 >= 8) & (t % 24 < 20) & ~dorm
    despertar_idx = np.where(dia14 & ~dorm)[0][0]
    ds = abs(S[(t >= 13 * 24) & (t < 13 * 24 + DT * 1.01)][0] - S[(t >= 12 * 24) & (t < 12 * 24 + DT * 1.01)][0])
    res[nombre] = (S[despertar_idx], a[laboral].mean(), a[laboral].min(), ds)
    print(f"{nombre:12s} {hs:9d} {S[despertar_idx]:15.3f} {a[laboral].mean():20.3f} {a[laboral].min():22.3f} {ds*1e4:26.2f}")

# prueba: solucion exacta de un tramo de vigilia
S0, t_v = 0.2, 16.0
exacta = S_MAX - (S_MAX - S0) * np.exp(-t_v / TAU_V)
num = S0
for _ in range(int(t_v / DT)):
    num = S_MAX - (S_MAX - num) * np.exp(-DT / TAU_V)
print(f"\nTramo de vigilia de 16 h desde S = 0,2: exacta {exacta:.5f}; numerica {num:.5f}")
print("Referencia consultada (NASA HRR): las tripulaciones duermen en promedio ~6 h por noche en Shuttle e ISS; ~19 % de los episodios de sueno en orbita estuvieron desalineados")

a8, a6, a4 = (res[k][1] for k in res)
assert abs(exacta - num) < 1e-9
assert a8 > a6 > a4
assert res["23:00-07:00"][0] < res["00:00-06:00"][0] < res["01:00-05:00"][0]
assert all(0.1 <= v[0] <= 0.9 for v in res.values())
print("Pruebas superadas.")
