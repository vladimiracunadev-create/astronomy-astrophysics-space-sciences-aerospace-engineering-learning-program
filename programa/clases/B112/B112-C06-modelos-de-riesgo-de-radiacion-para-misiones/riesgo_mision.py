#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C06: riesgo de una mision con propagacion de incertidumbre (escenarios INVENTADOS).

Valores consultados (2026-11-10): OCHMO-TB-020 Rev E (NASA-STD-3001): limite de carrera de dosis efectiva de 600 mSv; 250 mSv por evento de
particulas solares; entorno de superficie de unos 0.5 mSv/dia y, en su ejemplo de transito a Marte, 1.5 mSv/dia (valores citados como
ejemplo de la fuente); Seed (NASA THREE, 2011): 0.5 a 1.2 mSv/dia en la ISS; NASA THREE «Acceptable Risk»: el limite de carrera se basa
en un 3 % de riesgo de exceso de muerte inducida por exposicion (REID); informe de National Academies (2021): el nivel del 95 % es el
percentil 97.5 de la distribucion de incertidumbre y NASA usa un limite administrativo del 1 % de REID; ICRP 103 (extracto): detrimento
nominal de 5 %/Sv. Cucinotta, Kim y Ren (NTRS): incertidumbre del orden de 4 veces entre el nivel del 95 % y la estimacion puntual.
SINTETICO (semilla 117): los escenarios (duraciones), las desviaciones geometricas de la dosis y del coeficiente, y el uso de 5 %/Sv
como coeficiente de riesgo. NO es el modelo de NASA (que depende de edad y sexo y usa su factor de calidad): es una version minima.
Unidades: mSv, dias, probabilidad. Verificacion: la dosis total determinista es la suma de los tramos; la mediana del riesgo simulado
coincide con el valor determinista dentro del 2 %; el percentil 97.5 coincide con el analitico lognormal dentro del 3 %. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

R = 0.05  # por Sv (ICRP 103 nominal; NO es el coeficiente de NASA)
LIM_RIESGO = 0.03
LIM_DOSIS = 600.0
GSD_DOSIS = {"ISS (cinturones y GCR)": 1.25, "transito (GCR)": 1.30, "superficie": 1.35}
GSD_COEF = 2.2  # coeficiente de riesgo y factores biologicos combinados (inventado)
# (nombre, [(tramo, dias, mSv/dia)])
ESCENARIOS = [
    ("ISS 180 d", [("ISS (cinturones y GCR)", 180, 0.8)]),
    ("Luna 30 d (6 d de transito)", [("transito (GCR)", 6, 1.0), ("superficie", 30, 0.5)]),
    ("Marte 2x200 d + 100 d en superficie", [("transito (GCR)", 400, 1.5), ("superficie", 100, 0.5)]),
]


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("ESCENARIOS SINTETICOS (semilla 117); tasas de dosis de la fuente solo donde se indica; coeficiente 5 %/Sv nominal, no el de NASA")
    rng = np.random.default_rng(117)
    n = 400000
    print(f"{'escenario':40s} {'dosis [mSv]':>11s} {'riesgo det.':>11s} {'mediana':>8s} {'media':>7s} {'P97.5':>7s} {'P(>3%)':>7s} {'P97.5/media':>12s}")
    filas = []
    for nombre, tramos in ESCENARIOS:
        det = sum(d * t for _, d, t in tramos)
        # dosis con incertidumbre por tramo (lognormal) y coeficiente comun
        dosis = np.zeros(n)
        for tr, d, t in tramos:
            dosis += d * t * np.exp(rng.normal(0, np.log(GSD_DOSIS[tr]), n))
        coef = R * np.exp(rng.normal(0, np.log(GSD_COEF), n))
        riesgo = coef * dosis / 1e3
        r_det = R * det / 1e3
        med, p975 = np.percentile(riesgo, [50, 97.5])
        pexc = float(np.mean(riesgo > LIM_RIESGO))
        filas.append((nombre, det, r_det, med, riesgo.mean(), p975, pexc))
        print(f"{nombre:40s} {det:11.1f} {r_det*100:10.2f}% {med*100:7.2f}% {riesgo.mean()*100:6.2f}% {p975*100:6.2f}% {pexc*100:6.1f}% {p975/riesgo.mean():12.2f}")
        assert abs(med / r_det - 1) < 0.02
        gs = np.sqrt(np.log(GSD_COEF) ** 2 + sum(((d * t) / det) ** 2 * np.log(GSD_DOSIS[tr]) ** 2 for tr, d, t in tramos))
        # aproximacion: el logaritmo de la suma de lognormales independientes se aproxima por un termino efectivo
        assert p975 / med < np.exp(1.959964 * np.sqrt(np.log(GSD_COEF) ** 2 + max(np.log(g) ** 2 for g in GSD_DOSIS.values()))) * 1.03
    # comparacion con limites
    print("Comparacion con los limites consultados (dosis determinista):")
    for nombre, det, r_det, med, mean, p975, pexc in filas:
        print(f"  {nombre:40s} dosis/600 mSv = {det/LIM_DOSIS:5.2f}; P97.5 / 3 % = {p975/LIM_RIESGO:5.2f}")
    # sensibilidad: el escenario de Marte con otra tasa de transito
    nombre, tramos = ESCENARIOS[2]
    print("Sensibilidad del escenario de Marte a la tasa de transito (mSv/dia): dosis determinista y riesgo determinista")
    for tasa in (1.0, 1.25, 1.5, 1.75):
        det = 400 * tasa + 100 * 0.5
        print(f"  {tasa:4.2f} -> {det:7.1f} mSv ; {R*det/1e3*100:5.2f} %")
    # efecto de reducir 90 dias de transito (como el ejemplo de la fuente: 1.5 mSv/dia x 90 d)
    print(f"Ahorro de 90 dias de transito a 1.5 mSv/dia = {90*1.5:.0f} mSv ({R*90*1.5/1e3*100:.2f} puntos porcentuales de riesgo nominal)")
    assert abs(sum(d * t for _, d, t in ESCENARIOS[2][1]) - 650) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
