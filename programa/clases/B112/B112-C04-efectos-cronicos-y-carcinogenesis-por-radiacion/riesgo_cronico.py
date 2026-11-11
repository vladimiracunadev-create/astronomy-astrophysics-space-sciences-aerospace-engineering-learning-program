#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C04: riesgo de exceso lineal sin umbral con incertidumbre, y por que no se mide directamente.

Valores consultados (2026-11-10): ICRP 103 (extracto): detrimento combinado por cancer y efectos hereditables de alrededor del 5 % por Sv
con respuesta lineal a dosis bajas y DDREF de 2 para canceres solidos; Cucinotta, Kim y Ren (NASA NTRS): la incertidumbre del riesgo
(cociente entre el nivel del 95 % y la estimacion puntual) es de unas 4 veces para misiones lunares y a Marte; las incertidumbres entran
por los coeficientes epidemiologicos, el DDREF, los factores de calidad y la fisica. Lo propio del laboratorio es SINTETICO (semilla 115):
las desviaciones geometricas de cada factor, la incidencia basal de 20 % y el tamano de cohorte. NO reproduce el modelo de NASA ni el de la
ICRP. Riesgo de exceso = r * E, con r = 0.05 / Sv. Unidades: Sv, probabilidad. Verificacion: la potencia estadistica simulada concuerda con
la formula normal dentro de 0.05; la mediana del producto lognormal coincide con el producto de medianas dentro del 2 %.
Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

R_NOMINAL = 0.05   # por Sv (ICRP 103, detrimento nominal, extracto consultado)
BASAL = 0.20       # incidencia basal inventada
Z_A = 1.959964     # cuantil normal bilateral 5 %
Z_B = 0.841621     # cuantil normal de potencia 80 %


def n_por_grupo(p0, p1):
    pm = (p0 + p1) / 2
    return ((Z_A * np.sqrt(2 * pm * (1 - pm)) + Z_B * np.sqrt(p0 * (1 - p0) + p1 * (1 - p1))) ** 2) / (p1 - p0) ** 2


def potencia_sim(rng, p0, p1, n, reps=4000):
    a = rng.binomial(n, p0, reps) / n
    b = rng.binomial(n, p1, reps) / n
    pm = (a + b) / 2
    se = np.sqrt(2 * pm * (1 - pm) / n)
    z = (b - a) / np.where(se == 0, 1, se)
    return float(np.mean(z > Z_A))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 115); coeficiente nominal de 5 %/Sv de ICRP 103 (extracto); incertidumbres inventadas")
    print("Riesgo de exceso nominal r*E con r = 0.05/Sv (lineal sin umbral):")
    for e_msv in (10, 100, 250, 600, 1000):
        print(f"  E = {e_msv:5d} mSv -> exceso {R_NOMINAL*e_msv/1e3*100:6.3f} %  ({R_NOMINAL*e_msv/1e3/BASAL*100:6.2f} % de la incidencia basal inventada)")
    rng = np.random.default_rng(115)
    # potencia: cuantas personas hacen falta para ver el exceso
    print("Personas por grupo para detectar el exceso (alfa 5 %, potencia 80 %, incidencia basal inventada 20 %):")
    for e_msv in (100, 600, 1000, 4000):
        p1 = BASAL + R_NOMINAL * e_msv / 1e3
        n = n_por_grupo(BASAL, p1)
        print(f"  E = {e_msv:5d} mSv -> {n:12.0f} por grupo")
    p1 = BASAL + R_NOMINAL * 1.0
    n = int(np.ceil(n_por_grupo(BASAL, p1)))
    pot = potencia_sim(rng, BASAL, p1, n)
    print(f"Comprobacion por simulacion (E = 1000 mSv, n = {n}): potencia {pot:.3f} (objetivo 0.80)")
    assert abs(pot - 0.80) < 0.05
    # incertidumbre multiplicativa lognormal de la estimacion
    print("Incertidumbre multiplicativa (factores lognormales inventados; desviacion geometrica de cada uno):")
    factores = {"coeficiente epidemiologico": 1.5, "DDREF (efecto de la tasa de dosis)": 1.5, "factor de calidad (iones pesados)": 1.9, "fisica del campo de radiacion": 1.2}
    for k, v in factores.items():
        print(f"  {k:36s} GSD {v:.2f}")
    n_mc = 400000
    logs = sum(rng.normal(0, np.log(g), n_mc) for g in factores.values())
    mult = np.exp(logs)
    r_sim = R_NOMINAL * mult
    e = 0.6
    ex = r_sim * e
    p50, p975, p025 = np.percentile(ex, [50, 97.5, 2.5])
    print(f"Exceso de riesgo para E = 600 mSv: mediana {p50*100:.2f} %, media {ex.mean()*100:.2f} %, 2.5 % = {p025*100:.2f} %, 97.5 % = {p975*100:.2f} %")
    print(f"Cociente nivel 97.5 % / media = {p975/ex.mean():.2f} ; nivel 97.5 % / mediana = {p975/p50:.2f}")
    sg = np.sqrt(sum(np.log(g) ** 2 for g in factores.values()))
    print(f"GSD combinada analitica = {np.exp(sg):.2f}; 97.5 %/mediana analitico = {np.exp(1.959964*sg):.2f}")
    assert abs(p50 / (R_NOMINAL * e) - 1) < 0.02
    assert abs(p975 / p50 / np.exp(1.959964 * sg) - 1) < 0.03
    # efecto del DDREF: dividir por 2 (valor de la ICRP) frente a no dividir
    print("Efecto del DDREF sobre el exceso nominal a 600 mSv: con DDREF = 1 el exceso seria el doble que con DDREF = 2 (el 5 %/Sv ya lo incorpora).")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
