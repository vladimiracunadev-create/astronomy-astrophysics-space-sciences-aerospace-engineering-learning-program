#!/usr/bin/env python3
"""B104-C21: inventario de consumibles con punto de reorden y estiba por empaquetado en volumen.
DATOS SINTETICOS (semilla 104); parametros ILUSTRATIVOS. No es el inventario de ninguna nave."""
import sys
import math
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): consumo diario de un consumible con variacion; abastecimiento con plazo de 14 dias; parametros ilustrativos")
MU, SIG, LT, DIAS, N = 12.0, 3.0, 14, 365, 4000     # kg/d media, desviacion diaria, plazo de entrega, dias, repeticiones
Q = 300.0                                          # tamano del pedido (kg)


def simular(s_reorden, seed=104):
    rng = np.random.default_rng(seed)
    stock = np.full(N, s_reorden + Q)
    pendiente = np.zeros((N, LT + 1))                # llegadas programadas
    faltante_dias = np.zeros(N)
    en_camino = np.zeros(N, dtype=bool)
    for d in range(DIAS):
        stock += pendiente[:, 0]
        pendiente = np.concatenate([pendiente[:, 1:], np.zeros((N, 1))], axis=1)
        en_camino &= pendiente.sum(axis=1) > 0
        cons = np.maximum(0, MU + SIG * rng.standard_normal(N))
        faltante_dias += (cons > stock)
        stock = np.maximum(0, stock - cons)
        pedir = (stock <= s_reorden) & ~en_camino
        pendiente[pedir, LT] += Q
        en_camino |= pedir
    return (faltante_dias > 0).mean(), faltante_dias.mean()


z95 = 1.645
s_teo = MU * LT + z95 * SIG * math.sqrt(LT)
print(f"\nPunto de reorden teorico para ~95 % sin faltante en el plazo: s = mu L + z sigma sqrt(L) = {MU*LT:.0f} + {z95*SIG*math.sqrt(LT):.1f} = {s_teo:.1f} kg")
print("punto de reorden [kg] | P(algun faltante en 365 d) | dias con faltante (media)")
res = {}
for s in (MU * LT, s_teo, MU * LT + 2.5 * SIG * math.sqrt(LT)):
    res[s] = simular(s)
    print(f"{s:20.1f} {res[s][0]:28.3f} {res[s][1]:26.3f}")

# Estiba: empaquetado de objetos en bolsas de 0,05 m3 (primero el mayor que cabe, FFD)
rng = np.random.default_rng(104)
vol = np.round(rng.uniform(0.004, 0.030, 60), 4)
CAP = 0.05
orden = sorted(vol, reverse=True)
bolsas = []
for v in orden:
    for i in range(len(bolsas)):
        if bolsas[i] + v <= CAP + 1e-12:
            bolsas[i] += v
            break
    else:
        bolsas.append(v)
lb = math.ceil(vol.sum() / CAP - 1e-12)
print(f"\nEstiba: 60 objetos, volumen total {vol.sum():.3f} m3; cota inferior {lb} bolsas; empaquetado FFD usa {len(bolsas)} bolsas; llenado medio {vol.sum()/(len(bolsas)*CAP):.1%}")

assert res[s_teo][0] < res[MU * LT][0], "mas stock de seguridad, menos faltantes"
assert len(bolsas) >= lb and len(bolsas) <= math.ceil(11 / 9 * lb) + 1, "FFD dentro de su garantia"
assert max(bolsas) <= CAP + 1e-9
print("Pruebas superadas.")
