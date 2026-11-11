#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C09: privacidad acustica de una cabina con tres divisiones (ley de masa) y margen frente al ruido de fondo.

Datos consultados (2026-11-10): Burke, Howard y Kessler (2022): areas de sueno recomendada 1.82 m2 y de trazado 3.70 m2 para 2 tripulantes (1.85 m2 por tripulante), cabinas individuales
«altamente recomendadas», habitabilidad: dormir y aseo privados; resumen tecnico OCHMO-TB-035 Rev C: NASA-STD-3001 Vol. 2 limita el ruido continuo de las areas de sueno a la curva NC-40
para misiones de mas de 30 dias (los valores por banda de la tabla 6.6-3 NO se consultaron).
ILUSTRATIVOS / NO CONSULTADOS: espectro de la voz a 1 m (125-4000 Hz: 50, 56, 60, 56, 50, 44 dB), densidades superficiales (0.3, 2 y 6 kg/m2), area de division 2.0 m2,
absorcion del recinto receptor 6 m2 (Sabine), ruido de fondo 45 dBA, criterio de privacidad (transmitido <= fondo - 5 dB), ley de masa TL = 20 log10(f m) - 47 dB,
ponderacion A por la formula analitica (constantes 20.6, 107.7, 737.9 y 12194 Hz; no consultadas).
Modelo: L_receptor(f) = L_voz(f) - TL(f) + 10 log10(S/A); suma energetica y ponderacion A. TL se acota a >= 0 dB (la ley de masa no vale para una cortina).
Segunda via: duplicar la masa sube TL exactamente 20 log10(2) dB (1e-9); la ponderacion A vale 0 dB a 1 kHz (0.01) y los valores tabulados conocidos a 125, 250, 500, 2000 y 4000 Hz coinciden con 0.1 dB.
Unidades: nivel [dB re 20 uPa; dBA], frecuencia [Hz], densidad superficial [kg/m2], area [m2].
"""
from __future__ import annotations
import math, platform

BANDAS = [125, 250, 500, 1000, 2000, 4000]
VOZ = dict(zip(BANDAS, [50.0, 56.0, 60.0, 56.0, 50.0, 44.0]))
S_DIV, A_REC, FONDO, MARGEN = 2.0, 6.0, 45.0, 5.0
DIVISIONES = {"cortina textil": 0.3, "panel ligero": 2.0, "panel pesado": 6.0}


def a_pond(f):
    f2 = f * f
    ra = (12194.0 ** 2 * f2 * f2) / ((f2 + 20.6 ** 2) * math.sqrt((f2 + 107.7 ** 2) * (f2 + 737.9 ** 2)) * (f2 + 12194.0 ** 2))
    return 20 * math.log10(ra) + 2.0


def suma_db(niveles):
    return 10 * math.log10(sum(10 ** (x / 10) for x in niveles))


def tl_ley(f, m):
    return 20 * math.log10(f * m) - 47.0


def tl(f, m):
    return max(0.0, tl_ley(f, m))  # la ley de masa no vale con TL negativo: se acota a 0 dB


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Voz, masas, areas, fondo y criterio ILUSTRATIVOS; areas de sueno de Burke et al. (2022); NC-40 (sueno > 30 d) del resumen OCHMO-TB-035, sin valores por banda")
    assert abs(a_pond(1000)) < 0.01
    for f, ref in ((125, -16.1), (250, -8.6), (500, -3.2), (2000, 1.2), (4000, 1.0)):
        assert abs(a_pond(f) - ref) < 0.1, (f, a_pond(f))
    voz_a = suma_db([VOZ[f] + a_pond(f) for f in BANDAS])
    print(f"Voz a 1 m = {suma_db(list(VOZ.values())):.1f} dB lineal ; {voz_a:.1f} dBA")
    print(f"Criterio: transmitido <= fondo - {MARGEN:.0f} dB = {FONDO - MARGEN:.0f} dBA ; fondo = {FONDO:.0f} dBA ; 10 log10(S/A) = {10 * math.log10(S_DIV / A_REC):.2f} dB")
    print(" division           m [kg/m2]   TL(500 Hz) [dB]   nivel transmitido [dBA]   margen vs fondo [dB]   privada")
    for nom, m in DIVISIONES.items():
        lr = [VOZ[f] - tl(f, m) + 10 * math.log10(S_DIV / A_REC) for f in BANDAS]
        la = suma_db([x + a_pond(f) for x, f in zip(lr, BANDAS)])
        marg = la - FONDO
        print(f"{nom:17s} {m:9.1f} {tl(500, m):17.1f} {la:25.1f} {marg:22.1f}   {'si' if la <= FONDO - MARGEN else 'no'}")
        assert abs(tl_ley(500, 2 * m) - tl_ley(500, m) - 20 * math.log10(2)) < 1e-9
    # masa necesaria para cumplir el criterio
    m = 0.1
    while True:
        lr = [VOZ[f] - tl(f, m) + 10 * math.log10(S_DIV / A_REC) for f in BANDAS]
        if suma_db([x + a_pond(f) for x, f in zip(lr, BANDAS)]) <= FONDO - MARGEN:
            break
        m += 0.01
    print(f"Densidad superficial minima para cumplir el criterio = {m:.2f} kg/m2 (por pasos de 0.01)")
    print(f"Area de sueno por tripulante: recomendada 1.82 m2 ; trazado de referencia {3.70 / 2:.2f} m2")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
