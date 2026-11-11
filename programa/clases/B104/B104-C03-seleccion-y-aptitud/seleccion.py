#!/usr/bin/env python3
"""B104-C03: embudo de seleccion con aptitud latente y pruebas ruidosas.
DATOS SINTETICOS (semilla 104). No describe el proceso real de ninguna agencia."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): 12000 postulantes ficticios; aptitud latente N(0,1); 'apto' = 2 % superior")
N, FRAC_APTO, PLAZAS = 12000, 0.02, 10
z_apto = 2.0537489   # cuantil 98 % de la normal estandar (verificado abajo)


def corrida(seed, sigma, tasa_paso=0.15):
    rng = np.random.default_rng(seed)
    theta = rng.standard_normal(N)
    apto = theta > z_apto
    puntaje = theta + sigma * rng.standard_normal(N)
    corte = np.quantile(puntaje, 1 - tasa_paso)
    pasa = puntaje >= corte
    ppv = (apto & pasa).sum() / pasa.sum()
    recall = (apto & pasa).sum() / apto.sum()
    # seleccion final: top PLAZAS por puntaje
    elegidos = np.argsort(puntaje)[-PLAZAS:]
    frac_aptos = apto[elegidos].mean()
    return ppv, recall, frac_aptos


print("\nsigma ruido | precision (apto entre los que pasan) | exhaustividad | aptos entre los 10 elegidos")
res = {}
for s in (0.0, 0.5, 1.0, 2.0):
    r = np.array([corrida(1000 + i, s) for i in range(200)])
    res[s] = r.mean(axis=0)
    print(f"{s:8.1f} {res[s][0]:20.3f} {res[s][1]:22.3f} {res[s][2]:22.3f}")

# tasa base: aptos esperados
rng = np.random.default_rng(104)
print(f"\nAptos esperados en {N}: {N*FRAC_APTO:.0f}; plazas: {PLAZAS}")
# Bayes con tasa de paso 15 %: P(apto|pasa) = P(pasa|apto) P(apto)/P(pasa)
p_pasa_dado_apto = res[1.0][1]
print(f"Bayes (sigma = 1): P(apto|pasa) = {p_pasa_dado_apto:.3f} x {FRAC_APTO} / 0.15 = {p_pasa_dado_apto*FRAC_APTO/0.15:.3f}")

# Pruebas
assert abs(np.mean(np.random.default_rng(5).standard_normal(2_000_000) > z_apto) - 0.02) < 0.001
assert res[0.0][0] > res[0.5][0] > res[1.0][0] > res[2.0][0], "mas ruido, menos precision"
assert res[0.0][2] == 1.0, "sin ruido los 10 elegidos son aptos"
assert abs(p_pasa_dado_apto * FRAC_APTO / 0.15 - res[1.0][0]) < 0.01, "Bayes debe coincidir con el Monte Carlo"
print("Pruebas superadas.")
