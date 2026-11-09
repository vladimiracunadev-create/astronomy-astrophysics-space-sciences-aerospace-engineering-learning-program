#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C17: fotometria diferencial con transito sintetico y transparencia atmosferica comun.

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): 300 exposiciones, un objetivo de 2e5 cuentas y tres estrellas de comparacion de 1e5, 2e5 y 4e5 cuentas por exposicion,
una transparencia comun (tendencia lenta de 3 % mas una oscilacion de 4 %), un transito rectangular de profundidad 1 % en las exposiciones 130 a 169 y ruido de fotones gaussiano. No es una curva de luz real.
Modelo: curva diferencial = flujo del objetivo / suma de los flujos de comparacion; ruido previsto sqrt(1/N_obj + 1/N_comp); profundidad = 1 - media_en_transito / media_fuera.
Supuestos: la atmosfera afecta igual a todas las estrellas (sin termino de color ni de masa de aire), sin variabilidad de las comparaciones. Validez: la hipotesis falla en campos amplios o con estrellas de color distinto.
Tolerancia: RMS fuera de transito frente al previsto a 10 %; profundidad recuperada dentro de 3 errores previstos.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
N = 300
IN0, IN1 = 130, 170
PROF = 0.01
N_OBJ = 2e5
N_COMP = [1e5, 2e5, 4e5]


def rms(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1))


def calcular():
    rnd = random.Random(SEMILLA)
    trans = [1 + 0.03 * (1 - 2 * i / (N - 1)) + 0.04 * math.sin(2 * math.pi * i / 90) for i in range(N)]
    obj, comps = [], [[] for _ in N_COMP]
    for i in range(N):
        f = 1 - PROF if IN0 <= i < IN1 else 1.0
        m = N_OBJ * trans[i] * f
        obj.append(rnd.gauss(m, math.sqrt(m)))
        for k, nc in enumerate(N_COMP):
            mc = nc * trans[i]
            comps[k].append(rnd.gauss(mc, math.sqrt(mc)))
    fuera = [i for i in range(N) if not (IN0 <= i < IN1)]
    dentro = list(range(IN0, IN1))
    r = {"N": N, "n_in": len(dentro), "n_out": len(fuera)}

    def analizar(curva):
        med_out = sum(curva[i] for i in fuera) / len(fuera)
        norm = [c / med_out for c in curva]
        sd = rms([norm[i] for i in fuera])
        prof = 1 - sum(norm[i] for i in dentro) / len(dentro)
        return sd, prof
    r["raw"] = analizar(obj)
    r["trans_rms"] = rms([trans[i] for i in fuera])
    for k, nc in enumerate(N_COMP):
        r[f"c{k}"] = analizar([o / c for o, c in zip(obj, comps[k])])
    suma = [sum(c[i] for c in comps) for i in range(N)]
    r["ens"] = analizar([o / s for o, s in zip(obj, suma)])
    r["pred_ens"] = math.sqrt(1 / N_OBJ + 1 / sum(N_COMP))
    r["pred_c0"] = math.sqrt(1 / N_OBJ + 1 / N_COMP[0])
    r["pred_c2"] = math.sqrt(1 / N_OBJ + 1 / N_COMP[2])
    r["sig_prof"] = r["pred_ens"] * math.sqrt(1 / len(dentro) + 1 / len(fuera))
    r["pred_obj"] = math.sqrt(1 / N_OBJ)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{r['N']} exposiciones ({r['n_out']} fuera y {r['n_in']} dentro del transito) ; profundidad verdadera 1,000 %")
    print(f"transparencia comun: variacion RMS fuera de transito = {r['trans_rms']*100:.3f} %")
    print(f"{'curva':>22} {'RMS fuera (%)':>14} {'profundidad (%)':>16}")
    print(f"{'objetivo sin dividir':>22} {r['raw'][0]*100:14.3f} {r['raw'][1]*100:16.3f}")
    for k, nc in enumerate(N_COMP):
        print(f"{'comparacion ' + format(nc, '.0e'):>22} {r[f'c{k}'][0]*100:14.3f} {r[f'c{k}'][1]*100:16.3f}")
    print(f"{'conjunto de 3':>22} {r['ens'][0]*100:14.3f} {r['ens'][1]*100:16.3f}")
    print(f"previsto: ruido de fotones del conjunto {r['pred_ens']*100:.3f} % ; con la comparacion de 1e5 {r['pred_c0']*100:.3f} % ; con la de 4e5 {r['pred_c2']*100:.3f} % ; solo objetivo {r['pred_obj']*100:.3f} %")
    print(f"error previsto de la profundidad = {r['sig_prof']*100:.4f} % ; recuperada {r['ens'][1]*100:.4f} %")
    assert abs(r["ens"][0] / r["pred_ens"] - 1) < 0.10
    assert abs(r["ens"][1] - PROF) < 3 * r["sig_prof"]
    assert r["raw"][0] > 5 * r["ens"][0]
    assert r["ens"][0] < r["c0"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
