#!/usr/bin/env python3
"""B104-C16: modelo ILUSTRATIVO de tension en una tripulacion y comparacion de estrategias de resolucion.
DATOS SINTETICOS (semilla 104). No describe ni predice a ninguna tripulacion real."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO (semilla 104): 4 personas, 180 dias; tension AR(1) con choques; umbrales inventados")
RHO, SIG = 0.90, 0.35         # persistencia diaria y choque diario
U_CONF, U_MED = 2.0, 1.2      # umbral de conflicto abierto y de mediacion temprana (ILUSTRATIVOS)
DIAS, TRIPS, N = 180, 4, 1500


def simular(estrategia, seed=104):
    rng = np.random.default_rng(seed)
    T = np.zeros((N, TRIPS))
    conf = np.zeros(N, dtype=int)
    for d in range(DIAS):
        T = RHO * T + SIG * rng.standard_normal((N, TRIPS))
        if estrategia == "reunion semanal" and d % 7 == 6:
            T *= 0.5
        if estrategia == "mediacion temprana":
            T = np.where(T > U_MED, T * 0.8, T)
        abierto = T > U_CONF
        conf += abierto.any(axis=1)
        T = np.where(abierto, 0.2 * T, T)          # tras un conflicto abierto la tension baja (alivio)
    return conf


print("\nestrategia | episodios medios por tripulacion | P(>= 1 episodio) | P(>= 5 episodios)")
res = {}
for e in ("ninguna", "reunion semanal", "mediacion temprana"):
    c = simular(e)
    res[e] = c
    print(f"{e:22s} {c.mean():20.2f} {(c >= 1).mean():18.3f} {(c >= 5).mean():16.3f}")

# prueba de la varianza estacionaria del AR(1) (sin eventos ni estrategia)
rng = np.random.default_rng(7)
x = np.zeros(200_000)
for t in range(1, 2000):
    x = RHO * x + SIG * rng.standard_normal(x.size)
var_teo = SIG**2 / (1 - RHO**2)
print(f"\nVarianza estacionaria AR(1): simulada {x.var():.4f}; teorica {var_teo:.4f}")
print(f"Umbral de conflicto = {U_CONF/np.sqrt(var_teo):.2f} desviaciones estandar de la tension estacionaria")

assert abs(x.var() - var_teo) / var_teo < 0.02
assert res["mediacion temprana"].mean() < res["reunion semanal"].mean() < res["ninguna"].mean()
print("Pruebas superadas.")
