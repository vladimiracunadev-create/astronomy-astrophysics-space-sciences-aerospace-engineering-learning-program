#!/usr/bin/env python3
"""B104-C14: dispersion de aterrizaje y tiempo de rescate frente a la autonomia de provisiones.
DATOS SINTETICOS (semilla 104); dispersiones, velocidades y autonomia ILUSTRATIVAS. No es una guia de supervivencia."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): aterrizajes ficticios; dispersiones, velocidades y autonomia ilustrativas; no es una guia de supervivencia")
rng = np.random.default_rng(104)
N = 200_000
V_RESCATE = 250.0        # km/h de la fuerza de rescate (ILUSTRATIVO)
PREP = 1.5               # h de alistamiento
AUTONOMIA = 12.0         # h de provisiones y refugio (ILUSTRATIVO)


def simular(sig_dr, sig_cr, baliza, sesgo_dr=0.0):
    dr = sesgo_dr + sig_dr * rng.standard_normal(N)
    cr = sig_cr * rng.standard_normal(N)
    dist = np.hypot(dr, cr)                      # km desde el punto nominal donde espera el rescate
    t_loc = np.full(N, 0.5) if baliza else np.exp(np.log(6.0) + 0.8 * rng.standard_normal(N))
    t = PREP + t_loc + dist / V_RESCATE
    return dist, t


casos = [("nominal, con baliza", 25, 10, True, 0), ("nominal, sin baliza", 25, 10, False, 0),
         ("balistico (corto), con baliza", 120, 30, True, -300), ("balistico (corto), sin baliza", 120, 30, False, -300)]
print("\ncaso | distancia mediana [km] | tiempo mediano [h] | percentil 95 [h] | P(t > 12 h)")
res = {}
for n, sd, sc, b, sg in casos:
    dist, t = simular(sd, sc, b, sg)
    res[n] = (np.median(dist), np.median(t), np.percentile(t, 95), (t > AUTONOMIA).mean())
    r = res[n]
    print(f"{n:34s} {r[0]:10.1f} {r[1]:12.2f} {r[2]:14.2f} {r[3]:14.4f}")

# prueba: distancia media de una normal isotropica es sigma*sqrt(pi/2)
dist, _ = simular(25, 25, True, 0)
print(f"\nVerificacion (isotropica, sigma = 25 km): distancia media {dist.mean():.2f} km frente a teorica {25*np.sqrt(np.pi/2):.2f} km")
assert abs(dist.mean() - 25 * np.sqrt(np.pi / 2)) < 0.15
assert res["nominal, con baliza"][3] < res["nominal, sin baliza"][3]
assert res["balistico (corto), sin baliza"][3] > res["nominal, sin baliza"][3]
assert res["balistico (corto), con baliza"][1] > res["nominal, con baliza"][1]
print("Pruebas superadas.")
