#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C13: farmacocinetica de un compartimento con cambios de volumen y aclaramiento (FARMACO HIPOTETICO, datos SINTETICOS).

Farmaco hipotetico 'X' (no es ningun medicamento real; NO se da ninguna dosis ni pauta): bolo IV: C(t) = (D/V) exp(-k t), k = CL/V, t1/2 = ln2/k, AUC = D/CL.
Oral con absorcion de primer orden (Bateman): C(t) = F D ka / (V (ka - k)) (exp(-k t) - exp(-ka t)); tmax = ln(ka/k)/(ka - k).
Acumulacion en estado estacionario con dosis repetidas cada tau: R = 1/(1 - exp(-k tau)). Valores base ILUSTRATIVOS: V = 40 L, CL = 5 L/h, ka = 1.0 1/h, F = 1,
D = 100 unidades arbitrarias. Escenarios: V -10 % (menos liquido), CL -20 % (menos perfusion de higado/rinon): parametros hipoteticos. Poblacion SINTETICA de
5000 con variabilidad log-normal (CV 25 %), semilla 105. Integracion numerica de la curva oral con trapecios para comprobar el AUC. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

D, F, KA = 100.0, 1.0, 1.0


def iv(t, v, cl):
    return D / v * np.exp(-(cl / v) * t)


def oral(t, v, cl):
    k = cl / v
    return F * D * KA / (v * (KA - k)) * (np.exp(-k * t) - np.exp(-KA * t))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS (semilla 105): farmaco hipotetico X; no se da ninguna dosis real")
    t = np.linspace(0, 200, 200001)
    casos = {"base": (40.0, 5.0), "V -10 %": (36.0, 5.0), "CL -20 %": (40.0, 4.0), "V -10 % y CL -20 %": (36.0, 4.0)}
    print("caso                 k [1/h]  t1/2 [h]  AUC=D/CL   C0 [u/L]   Cmax oral   tmax [h]   AUC oral (trapecio)   R (tau = 12 h)")
    res = {}
    for nombre, (v, cl) in casos.items():
        k = cl / v
        c = oral(t, v, cl)
        auc = np.trapezoid(c, t)
        tmax = np.log(KA / k) / (KA - k)
        r = 1 / (1 - np.exp(-k * 12))
        res[nombre] = (np.log(2) / k, D / cl, c.max(), auc, r)
        print(f"{nombre:20s} {k:7.4f}  {np.log(2) / k:7.2f}   {D / cl:7.2f}   {D / v:7.3f}   {c.max():8.3f}   {tmax:6.2f}      {auc:8.2f}              {r:5.3f}")
    rng = np.random.default_rng(105)
    cv = 0.25
    s = np.sqrt(np.log(1 + cv ** 2))
    v = 40 * np.exp(rng.normal(-s * s / 2, s, 5000)); cl = 5 * np.exp(rng.normal(-s * s / 2, s, 5000))
    auc = D / cl
    print(f"Poblacion sintetica (CV 25 %): AUC mediana {np.median(auc):.2f}, p5-p95 = {np.percentile(auc, 5):.2f}-{np.percentile(auc, 95):.2f} (nominal {D / 5:.2f})")
    cl2 = cl * 0.8
    print(f"Con CL -20 % en toda la poblacion: razon media de AUC = {np.mean(D / cl2) / np.mean(auc):.3f} (= 1/0.8 = 1.250)")
    assert abs(res["base"][3] - res["base"][1]) / res["base"][1] < 1e-3
    assert abs(res["CL -20 %"][3] / res["base"][3] - 1.25) < 1e-3
    assert res["V -10 %"][1] == res["base"][1]
    assert res["CL -20 %"][0] > res["base"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
