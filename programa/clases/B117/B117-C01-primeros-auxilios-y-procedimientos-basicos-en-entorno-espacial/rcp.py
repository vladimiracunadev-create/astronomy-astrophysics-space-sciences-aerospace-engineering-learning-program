#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B117-C01: fatiga del reanimador y plan de relevo en una RCP SIMULADA (microgravedad).

CONTENIDO EDUCATIVO: no es una pauta de reanimacion ni consejo medico; no sustituye formacion ni supervision profesional.
Datos consultados (2026-11-10): comunicado de la Sociedad Europea de Cardiologia (2025-08-27) sobre un estudio en maniqui en vuelo
parabolico: profundidad mediana 34.5 mm (metodo manual 'handstand'), 53.0 mm (piston mecanico estandar), 29 mm (otros dos dispositivos);
el rango 50-60 mm que cita el comunicado se atribuye alli al Consejo Europeo de Resucitacion (no consultado directamente).
ILUSTRATIVOS (sinteticos, no medidos): decaimiento exponencial de la profundidad manual con la fatiga: d(t) = d_inf + (d0 - d_inf) exp(-t/tau),
d0 = 36 mm, d_inf = 22 mm, tau = 2.0 min; ruido por compresion sigma = 3 mm; frecuencia 110 compresiones/min; criterio de calidad
'profundidad media >= 80 % de d0'; recuperacion completa tras 4 min de reposo. El dispositivo se modela sin fatiga a 53.0 mm.
Sistema de referencia: tiempo desde el inicio de la RCP [min]; profundidades [mm]. No hay marco espacial.
Tolerancias: media simulada frente a analitica < 0.3 mm (2000 repeticiones, semilla fija); t* numerico frente a analitico < 0.01 min.
"""
from __future__ import annotations
import math, platform, random

D0, DINF, TAU, SIGMA = 36.0, 22.0, 2.0, 3.0
RATE = 110.0          # compresiones por minuto (ilustrativo)
FRAC = 0.80           # criterio de calidad (ilustrativo)
REPOSO = 4.0          # min de reposo para recuperarse (ilustrativo)
DEVICE = 53.0         # mm, mediana consultada del piston mecanico
UMBRAL_REF = 50.0     # mm, limite inferior citado en el comunicado


def profundidad_media(t):
    return DINF + (D0 - DINF) * math.exp(-t / TAU)


def t_estrella():
    """Tiempo hasta que la profundidad media cae al 80 % de d0 (analitico)."""
    return -TAU * math.log((FRAC * D0 - DINF) / (D0 - DINF))


def simular(seed, minutos):
    rng = random.Random(seed)
    n = int(minutos * RATE)
    return [profundidad_media(i / RATE) + rng.gauss(0.0, SIGMA) for i in range(n)]


def media_empirica(t, reps=2000, seed=117):
    rng = random.Random(seed)
    s = sum(profundidad_media(t) + rng.gauss(0.0, SIGMA) for _ in range(reps))
    return s / reps


def t_estrella_numerico(paso=0.001):
    t = 0.0
    while profundidad_media(t) >= FRAC * D0:
        t += paso
    return t


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("RCP SIMULADA, parametros ILUSTRATIVOS; solo las medianas de 34.5 y 53.0 mm son datos consultados (maniqui).")
    print(f"Modelo manual: d(t) = {DINF} + ({D0}-{DINF}) exp(-t/{TAU}) mm; dispositivo: {DEVICE} mm constante")
    print(" t [min]  d manual [mm]  d dispositivo [mm]")
    for t in (0, 1, 2, 4, 8, 16):
        print(f"{t:7d}  {profundidad_media(t):13.2f}  {DEVICE:18.1f}")
    ts = t_estrella()
    tsn = t_estrella_numerico()
    print(f"t* (profundidad media = {FRAC:.0%} de d0): analitico = {ts:.3f} min ; numerico = {tsn:.3f} min")
    err = max(abs(media_empirica(t) - profundidad_media(t)) for t in (0, 2, 8))
    print(f"Error maximo media simulada - analitica = {err:.3f} mm")
    # fraccion de compresiones >= 50 mm en una ventana de 2 min
    v = simular(1, 2.0)
    fm = sum(1 for x in v if x >= UMBRAL_REF) / len(v)
    rng = random.Random(2)
    fd = sum(1 for _ in range(len(v)) if DEVICE + rng.gauss(0.0, SIGMA) >= UMBRAL_REF) / len(v)
    print(f"Fraccion de compresiones >= {UMBRAL_REF} mm en 2 min: manual = {fm:.3f} ; dispositivo = {fd:.3f}")
    # plan de relevo: cada reanimador trabaja t* y descansa REPOSO
    for total in (10, 20, 30):
        turnos = math.ceil(total / ts)
        n_reanimadores = math.ceil((ts + REPOSO) / ts)
        print(f"Esfuerzo de {total} min: {turnos} turnos de {ts:.2f} min; reanimadores minimos con {REPOSO:.0f} min de reposo = {n_reanimadores}")
    assert abs(ts - tsn) < 0.01
    assert err < 0.3
    assert fm < 0.05 < 0.5 < fd
    assert math.isclose(profundidad_media(0), D0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
