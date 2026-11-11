#!/usr/bin/env python3
"""B104-C20: mision tripulada simulada (analoga) de 30 dias: Monte Carlo que integra consumibles, fallas y carga de trabajo.
DATOS SINTETICOS (semilla 104); todos los parametros ILUSTRATIVOS. No es la evaluacion de ninguna mision real."""
import sys
import numpy as np

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("DATOS SINTETICOS (semilla 104): mision analoga de 30 dias, 4 tripulantes; parametros ilustrativos")
DIAS, TRIP, N = 30, 4, 50_000
TAREAS = 60                    # tareas de ciencia programadas
HORAS_TAREA = 2.0
HORAS_DIA = 6.5                # horas de trabajo utiles por persona y dia (ILUSTRATIVO)
CARGA_AGUA = 330.0 * 1.0       # kg cargados de agua (4 x 30 x 2,5 + 10 %); ILUSTRATIVO
TASA_AGUA = 2.5


def simular(lam_falla, seed=104):
    rng = np.random.default_rng(seed)
    # consumo de agua con variacion diaria
    consumo = (TRIP * TASA_AGUA * (1 + 0.08 * rng.standard_normal((N, DIAS)))).sum(axis=1)
    # fallas: Poisson por mision; cada una exige horas de reparacion log-normal (mediana 6 h) y puede costar agua (perdida 5 kg)
    nf = rng.poisson(lam_falla * DIAS, size=N)
    horas_rep = np.array([np.exp(np.log(6.0) + 0.7 * rng.standard_normal(k)).sum() for k in nf])
    perdida = 5.0 * nf
    horas_disp = DIAS * TRIP * HORAS_DIA
    horas_cs = TAREAS * HORAS_TAREA
    # horas de otras obligaciones (mantenimiento, ejercicio, etc.) ILUSTRATIVO: 70 % del tiempo util
    horas_libres = horas_disp * 0.30 - horas_rep
    tareas_hechas = np.clip(horas_libres / HORAS_TAREA, 0, TAREAS)
    ok_agua = (consumo + perdida) <= CARGA_AGUA
    ok_ciencia = tareas_hechas >= 0.9 * TAREAS
    exito = ok_agua & ok_ciencia
    return exito, ok_agua, ok_ciencia, nf, tareas_hechas, CARGA_AGUA - (consumo + perdida)


print("\ntasa de fallas [1/d] | P(exito) | P(agua suficiente) | P(>= 90 % de tareas) | fallas medias | margen medio de agua [kg]")
res = {}
for lam in (0.0, 0.05, 0.10, 0.20):
    ex, a, c, nf, th, marg = simular(lam)
    res[lam] = (ex.mean(), a.mean(), c.mean(), nf.mean(), marg.mean(), nf)
    print(f"{lam:18.2f} {ex.mean():10.3f} {a.mean():18.3f} {c.mean():20.3f} {nf.mean():14.2f} {marg.mean():22.1f}")

p0_teo = np.exp(-0.10 * DIAS)
p0_mc = (res[0.10][5] == 0).mean()
print(f"\nP(ninguna falla) con 0,10/d: simulada {p0_mc:.4f}; teorica exp(-lambda T) = {p0_teo:.4f}")
horas_libres_max = DIAS * TRIP * HORAS_DIA * 0.30
print(f"Horas libres sin fallas: {horas_libres_max:.0f} h para {TAREAS*HORAS_TAREA:.0f} h de tareas (holgura {horas_libres_max-TAREAS*HORAS_TAREA:.0f} h)")

assert abs(p0_mc - p0_teo) < 0.005
assert res[0.0][0] > res[0.05][0] > res[0.10][0] > res[0.20][0]
print("Pruebas superadas.")
