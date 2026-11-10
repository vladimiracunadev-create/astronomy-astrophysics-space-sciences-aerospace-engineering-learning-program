# SPDX-License-Identifier: Apache-2.0
"""B85-C24: daño por radiación ionizante: pérdida de potencia de una celda solar por fluencia equivalente y umbrales de dosis en materiales.

Todo SINTÉTICO e ILUSTRATIVO (semilla fija): P/P0 = 1 - C log10(1 + Φ/Φx), NIEL relativo, umbrales de dosis. Consultado: nada.
Segunda vía: ajuste (búsqueda de Φx + mínimos cuadrados lineales en C) frente a los parámetros verdaderos, y la inversa analítica.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

C_V, FX_V = 0.19, 1.0e12          # sintetico (fluencia equivalente en cm-2)
SEMILLA = 20261110
UMBRALES = [("polimero A (sintetico)", 2.0e3), ("polimero B (sintetico)", 2.0e4), ("elastomero (sintetico)", 4.0e3)]   # Gy


def p_rel(fl, c=C_V, fx=FX_V):
    return 1.0 - c * math.log10(1.0 + fl / fx)


def datos(n=10, ruido=0.004):
    rng = random.Random(SEMILLA)
    fl = [10 ** (11 + 4.0 * i / (n - 1)) for i in range(n)]
    return fl, [p_rel(f) + rng.gauss(0, ruido) for f in fl]


def ajustar(fl, p):
    mejor = None
    for k in range(1, 400):
        fx = 10 ** (10.0 + 0.01 * k)
        g = [math.log10(1.0 + f / fx) for f in fl]
        y = [1.0 - pi for pi in p]
        c = sum(a * b for a, b in zip(g, y)) / sum(a * a for a in g)
        sse = sum((yi - c * gi) ** 2 for gi, yi in zip(g, y))
        if mejor is None or sse < mejor[0]:
            mejor = (sse, c, fx)
    sse, c, fx = mejor
    return c, fx, math.sqrt(sse / len(fl))


def fluencia_para(p_obj, c, fx):
    return fx * (10 ** ((1.0 - p_obj) / c) - 1.0)


def calcular():
    r = {}
    fl, p = datos()
    r["fl"], r["p"] = fl, p
    r["c"], r["fx"], r["rms"] = ajustar(fl, p)
    tasa = 2.0e11                           # cm-2 por anio equivalentes (SINTETICO)
    r["tasa"] = tasa
    r["p_5"] = p_rel(5 * tasa, r["c"], r["fx"])
    r["p_5_verd"] = p_rel(5 * tasa)
    r["p_15"] = p_rel(15 * tasa, r["c"], r["fx"])
    r["fl_80"] = fluencia_para(0.80, r["c"], r["fx"])
    r["anios_80"] = r["fl_80"] / tasa
    r["inv_resid"] = abs(p_rel(r["fl_80"], r["c"], r["fx"]) - 0.80)
    r["p_coverglass"] = p_rel(2.5 * tasa, r["c"], r["fx"])       # blindaje que reduce la fluencia a la mitad
    r["niel"] = [(e, k) for e, k in ((1.0, 4.0), (10.0, 1.0), (50.0, 0.4))]   # MeV, NIEL relativo SINTETICO
    r["dosis_anual"] = 400.0                 # Gy/anio SINTETICO sin blindaje adicional
    r["vida_materiales"] = [(n, u / r["dosis_anual"]) for n, u in UMBRALES]
    r["potencia_eol_w"] = 100.0 * r["p_5"]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Celda SINTETICA: P/P0 = 1 - {C_V} log10(1 + F/{FX_V:.0e}) ; ruido 0.004 ; semilla {SEMILLA}")
    print("Fluencia [cm-2]   P/P0")
    for f, p in zip(r["fl"], r["p"]):
        print(f"{f:12.3e}   {p:.4f}")
    print(f"Ajuste: C = {r['c']:.4f} (verdadero {C_V}) ; Fx = {r['fx']:.3e} (verdadero {FX_V:.0e}) ; RMS = {r['rms']:.4f}")
    print(f"Tasa SINTETICA {r['tasa']:.1e} cm-2/anio: P/P0 a 5 anios = {r['p_5']:.4f} (verdadera {r['p_5_verd']:.4f}) ; a 15 anios = {r['p_15']:.4f}")
    print(f"Fluencia para P/P0 = 0.80: {r['fl_80']:.3e} cm-2 = {r['anios_80']:.1f} anios ; residuo de la inversa = {r['inv_resid']:.1e}")
    print(f"Con un blindaje que reduce la fluencia a la mitad, P/P0 a 5 anios = {r['p_coverglass']:.4f} ; potencia EOL de una matriz de 100 W = {r['potencia_eol_w']:.1f} W")
    print("Vida por umbral de dosis (dosis anual SINTETICA 400 Gy): " + "; ".join(f"{n}: {v:.0f} anios" for n, v in r["vida_materiales"]))
    comprobar(abs(r["c"] - C_V) < 0.02, "C")
    comprobar(r["inv_resid"] < 1e-9, "inversa")
    comprobar(abs(r["p_5"] - r["p_5_verd"]) < 0.01, "extrapolacion")
    fin()


if __name__ == "__main__":
    main()
