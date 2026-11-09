#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C18: extraccion de un espectro, suma de apertura frente a extraccion optima ponderada por el perfil.

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): columna espectral con 41 pixeles espaciales, perfil gaussiano de sigma 2,0 pixeles, flujo de 400 e-, cielo de 60 e-/pixel y ruido de lectura
de 6 e-; los conteos se muestrean con ruido gaussiano de varianza igual a la media mas el ruido de lectura. La extraccion optima es el metodo de ponderacion por el perfil de Horne (1986), citado de memoria
y NO consultado en esta sesion.
Modelo: suma simple en +-6 pixeles con correccion por la fraccion encerrada; extraccion optima F = sum(P D / V) / sum(P^2 / V) con V = P F + B + RN^2; varianza 1 / sum(P^2 / V).
Supuestos: perfil conocido, cielo conocido, ruido independiente por pixel. Validez: en la practica el perfil se ajusta y el cielo se mide.
Tolerancia: desviaciones Monte Carlo frente a la prediccion analitica a 5 %; la extraccion optima tiene menor varianza que la suma; el rechazo de rayos cosmicos restaura la estimacion.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
NY = 41
C0 = 20
SIG = 2.0
FLUJO = 400.0
CIELO = 60.0
RN = 6.0
AP = 6


def perfil():
    p = [math.exp(-0.5 * ((y - C0) / SIG) ** 2) for y in range(NY)]
    s = sum(p)
    return [v / s for v in p]


def desv(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)), m


def optima(D, P, F_est, rechazar=False):
    V = [p * F_est + CIELO + RN ** 2 for p in P]
    mask = [1.0] * NY
    F = None
    for _ in range(3 if rechazar else 1):
        num = sum(m * p * (d - CIELO) / v for m, p, d, v in zip(mask, P, D, V))
        den = sum(m * p * p / v for m, p, v in zip(mask, P, V))
        F = num / den
        if rechazar:
            for i in range(NY):
                res = (D[i] - CIELO - F * P[i]) / math.sqrt(V[i])
                mask[i] = 0.0 if abs(res) > 5 else 1.0
    return F


def calcular():
    rnd = random.Random(SEMILLA)
    P = perfil()
    r = {}
    ap = range(C0 - AP, C0 + AP + 1)
    frac = sum(P[i] for i in ap)
    r["frac"] = frac
    V = [p * FLUJO + CIELO + RN ** 2 for p in P]
    r["pred_simple"] = math.sqrt(sum(V[i] for i in ap)) / frac
    r["pred_opt"] = math.sqrt(1 / sum(p * p / v for p, v in zip(P, V)))
    simple, opt = [], []
    for _ in range(5000):
        D = [rnd.gauss(p * FLUJO + CIELO, math.sqrt(p * FLUJO + CIELO + RN ** 2)) for p in P]
        simple.append(sum(D[i] - CIELO for i in ap) / frac)
        opt.append(optima(D, P, FLUJO))
    r["sd_simple"], r["m_simple"] = desv(simple)
    r["sd_opt"], r["m_opt"] = desv(opt)
    # rayo cosmico de 3000 e- en un pixel del perfil (a +1)
    cr_simple, cr_opt, cr_rej = [], [], []
    for _ in range(2000):
        D = [rnd.gauss(p * FLUJO + CIELO, math.sqrt(p * FLUJO + CIELO + RN ** 2)) for p in P]
        D[C0 + 4] += 3000.0
        cr_simple.append(sum(D[i] - CIELO for i in ap) / frac)
        cr_opt.append(optima(D, P, FLUJO))
        cr_rej.append(optima(D, P, FLUJO, rechazar=True))
    r["cr_simple"] = sum(cr_simple) / len(cr_simple)
    r["cr_opt"] = sum(cr_opt) / len(cr_opt)
    r["cr_rej"] = sum(cr_rej) / len(cr_rej)
    r["cr_rej_sd"] = desv(cr_rej)[0]
    r["mejora"] = r["sd_simple"] / r["sd_opt"]
    r["mejora_pred"] = r["pred_simple"] / r["pred_opt"]
    r["snr_simple"] = FLUJO / r["sd_simple"]
    r["snr_opt"] = FLUJO / r["sd_opt"]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"fraccion del perfil dentro de +-{AP} pixeles = {r['frac']:.5f}")
    print(f"{'metodo':>16} {'media':>9} {'sigma MC':>9} {'sigma prevista':>15} {'S/N':>7}")
    print(f"{'suma simple':>16} {r['m_simple']:9.2f} {r['sd_simple']:9.3f} {r['pred_simple']:15.3f} {r['snr_simple']:7.2f}")
    print(f"{'optima (Horne)':>16} {r['m_opt']:9.2f} {r['sd_opt']:9.3f} {r['pred_opt']:15.3f} {r['snr_opt']:7.2f}")
    print(f"mejora de la desviacion: {r['mejora']:.3f} (prevista {r['mejora_pred']:.3f})")
    print(f"con rayo cosmico de 3000 e- a +4 pixeles (verdadero 400): suma {r['cr_simple']:.1f} ; optima sin rechazo {r['cr_opt']:.1f} ; optima con rechazo a 5 sigma {r['cr_rej']:.1f} (sigma {r['cr_rej_sd']:.2f})")
    assert abs(r["sd_simple"] / r["pred_simple"] - 1) < 0.05
    assert abs(r["sd_opt"] / r["pred_opt"] - 1) < 0.05
    assert r["sd_opt"] < r["sd_simple"]
    assert abs(r["m_simple"] - FLUJO) < 4 * r["sd_simple"] / math.sqrt(5000) and abs(r["m_opt"] - FLUJO) < 4 * r["sd_opt"] / math.sqrt(5000)
    assert r["cr_simple"] - FLUJO > 1000 and abs(r["cr_rej"] - FLUJO) < 10
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
