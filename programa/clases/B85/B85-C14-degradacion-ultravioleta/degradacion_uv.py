# SPDX-License-Identifier: Apache-2.0
"""B85-C14: degradación ultravioleta de un recubrimiento: α(ESH) saturante, ajuste a datos sintéticos y efecto en T.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC); NASA SST-SoA Thermal Control: los coatings se oscurecen en órbita y se usan valores
de fin de vida en el caso caliente. ILUSTRATIVO y SINTÉTICO: ley α(ESH) = α0 + Δα_max (1 - exp(-ESH/E0)), parámetros verdaderos,
ruido (semilla fija) y horas de sol equivalente por año.
Segunda vía: ajuste por mínimos cuadrados (búsqueda en E0 + solución lineal en Δα_max) frente a los parámetros verdaderos.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

ALFA0, DA_VERD, E0_VERD = 0.20, 0.18, 1500.0      # sintético
EPS = 0.90
ESH_ANIO = 5000.0                                 # horas de sol equivalente por año (ilustrativo)
SEMILLA = 20261110


def alfa(esh, a0=ALFA0, da=DA_VERD, e0=E0_VERD):
    return a0 + da * (1 - math.exp(-esh / e0))


def datos_sinteticos(n=14, ruido=0.004):
    rng = random.Random(SEMILLA)
    esh = [i * 4000.0 / (n - 1) for i in range(n)]
    return esh, [alfa(e) + rng.gauss(0.0, ruido) for e in esh]


def ajustar(esh, a):
    mejor = None
    for e0 in [200.0 + 5.0 * k for k in range(1, 800)]:
        g = [1 - math.exp(-x / e0) for x in esh]
        y = [ai - ALFA0 for ai in a]
        da = sum(gi * yi for gi, yi in zip(g, y)) / sum(gi * gi for gi in g)
        sse = sum((yi - da * gi) ** 2 for gi, yi in zip(g, y))
        if mejor is None or sse < mejor[0]:
            mejor = (sse, e0, da)
    sse, e0, da = mejor
    return da, e0, math.sqrt(sse / len(esh))


def t_placa(al):
    return (al * S0 / (EPS * SIGMA)) ** 0.25


def calcular():
    r = {}
    esh, a = datos_sinteticos()
    r["esh"], r["a"] = esh, a
    r["da_aj"], r["e0_aj"], r["rms"] = ajustar(esh, a)
    r["alfa_5"] = alfa(5 * ESH_ANIO, ALFA0, r["da_aj"], r["e0_aj"])
    r["alfa_5_verd"] = alfa(5 * ESH_ANIO)
    r["alfa_sat"] = ALFA0 + r["da_aj"]
    r["t_bol"] = t_placa(ALFA0)
    r["t_eol5"] = t_placa(r["alfa_5"])
    r["t_sat"] = t_placa(r["alfa_sat"])
    r["esh_90"] = -r["e0_aj"] * math.log(0.1)
    r["anios_90"] = r["esh_90"] / ESH_ANIO
    r["alfa_a_1500"] = alfa(1500.0)
    r["dt_5"] = r["t_eol5"] - r["t_bol"]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Ley ILUSTRATIVA: alfa = {ALFA0} + {DA_VERD} (1 - exp(-ESH/{E0_VERD:.0f})) ; datos SINTETICOS con ruido gaussiano 0.004 (semilla {SEMILLA})")
    print("ESH [h]   alfa medida")
    for e, ai in zip(r["esh"], r["a"]):
        print(f"{e:8.0f}   {ai:.4f}")
    print(f"Ajuste: delta_alfa_max = {r['da_aj']:.4f} (verdadero {DA_VERD}) ; E0 = {r['e0_aj']:.0f} h (verdadero {E0_VERD:.0f}) ; RMS = {r['rms']:.4f}")
    print(f"alfa tras 5 anios ({5*ESH_ANIO:.0f} ESH): ajustada {r['alfa_5']:.4f} ; verdadera {r['alfa_5_verd']:.4f} ; saturacion {r['alfa_sat']:.4f}")
    print(f"Placa al Sol (eps = {EPS}): BOL {r['t_bol']:.2f} K ; 5 anios {r['t_eol5']:.2f} K (+{r['dt_5']:.2f} K) ; saturada {r['t_sat']:.2f} K")
    print(f"Horas de sol equivalente para el 90 % del cambio: {r['esh_90']:.0f} h = {r['anios_90']:.2f} anios")
    comprobar(abs(r["da_aj"] - DA_VERD) < 0.01, "delta alfa")
    comprobar(abs(r["e0_aj"] - E0_VERD) / E0_VERD < 0.15, "E0")
    comprobar(r["rms"] < 0.008, "RMS del ajuste")
    fin()


if __name__ == "__main__":
    main()
