#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C20: clasificacion de un registro diario en las escalas G, S y R de NOAA y evaluacion de una regla de alerta.

Datos: umbrales de las escalas de NOAA (spaceweather.gov, pagina de escalas, consultada 2026-11-09): G1-G5 = Kp 5, 6, 7, 8 (incluido 9-) y 9; S1-S5 = flujo de protones de energia >= 10 MeV de
10, 1e2, 1e3, 1e4 y 1e5 unidades de flujo de particulas (pfu); R1-R5 = flujo de rayos X de 0.1-0.8 nm de 1e-5, 5e-5, 1e-4, 1e-3 y 2e-3 W/m2 (M1, M5, X1, X10, X20). El registro de un anio
(Kp maximo diario, flujo maximo de protones y de rayos X, con persistencia de rayos X rho = 0.7) y la regla de alerta son SINTETICOS (ilustrativos, semilla fija); no es un registro real.
Modelo: clasificacion por umbral; regla de alerta: pronosticar R1 o mayor manana si hoy el flujo de rayos X >= C5; tabla de contingencia (aciertos a, falsas alarmas b, fallos c, negativos
correctos d) y puntuaciones POD = a/(a + c), FAR = b/(a + b), CSI = a/(a + b + c), y la puntuacion de habilidad de Heidke por dos formulas.
Supuestos: eventos diarios, persistencia gaussiana en log de los rayos X. Validez: ilustrativa; los umbrales son los publicados por NOAA.
Tolerancia: las dos formulas de Heidke coinciden a 1e-12; los conteos suman el numero de pares de dias.
"""
from __future__ import annotations
import math
import platform
import random
import sys

UMBRAL_G = ((9, "o", 5), (8, "-", 4), (7, "-", 3), (6, "-", 2), (5, "-", 1))
UMBRAL_S = (1e5, 1e4, 1e3, 1e2, 10.0)
UMBRAL_R = (2e-3, 1e-3, 1e-4, 5e-5, 1e-5)
ETIQ = ["0o", "0+"]
for k in range(1, 9):
    ETIQ += [f"{k}-", f"{k}o", f"{k}+"]
ETIQ += ["9-", "9o"]


def g_de_kp(etiqueta):
    dig = int(etiqueta[0])
    if dig == 9 and etiqueta[1] == "-":
        return 4
    return max(0, dig - 4) if dig >= 5 else 0


def escala(valor, umbrales):
    n = len(umbrales)
    for i, u in enumerate(umbrales):
        if valor >= u:
            return n - i
    return 0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    assert len(ETIQ) == 28
    print(f"escala de Kp de 28 valores: {len(ETIQ)} etiquetas, de {ETIQ[0]} a {ETIQ[-1]}")
    print("umbrales: G " + " ".join(f"G{i + 1}=Kp{k}" for i, k in enumerate((5, 6, 7, 8, 9))) + " ; S " + " ".join(f"S{i + 1}>={u:g}" for i, u in enumerate(sorted(UMBRAL_S))) + " pfu ; R " + " ".join(f"R{i + 1}>={u:g}" for i, u in enumerate(sorted(UMBRAL_R))) + " W/m2")
    assert [escala(f, UMBRAL_R) for f in (9e-6, 1e-5, 5e-5, 1e-4, 1e-3, 2e-3)] == [0, 1, 2, 3, 4, 5]
    assert [escala(f, UMBRAL_S) for f in (9.9, 10, 100, 1e3, 1e4, 1e5)] == [0, 1, 2, 3, 4, 5]
    # registro sintetico de 365 dias
    rng = random.Random(20261109)
    dias = 365
    rho = 0.7
    y = 0.0
    xray, kp, prot = [], [], []
    for _ in range(dias):
        y = rho * y + math.sqrt(1 - rho ** 2) * rng.gauss(0, 1)
        xray.append(10 ** (-6.0 + 0.55 * y))
        t = min(27, max(0, int(round(6 + 3.3 * rng.expovariate(1.0) * 1.0))))   # tercios de Kp
        kp.append(ETIQ[t])
        prot.append(0.2 * (1 - rng.random()) ** -1.0)
    cuentas = {"G": [0] * 6, "S": [0] * 6, "R": [0] * 6}
    for i in range(dias):
        cuentas["G"][g_de_kp(kp[i])] += 1
        cuentas["S"][escala(prot[i], UMBRAL_S)] += 1
        cuentas["R"][escala(xray[i], UMBRAL_R)] += 1
    print(f"{'escala':<8}" + "".join(f"{x:>6}" for x in ("0", "1", "2", "3", "4", "5")))
    for k in "GSR":
        print(f"{k:<8}" + "".join(f"{v:6d}" for v in cuentas[k]))
        assert sum(cuentas[k]) == dias
    # regla de alerta de rayos X
    a = b = c = d = 0
    for i in range(dias - 1):
        pred = xray[i] >= 5e-6
        obs = xray[i + 1] >= 1e-5
        if pred and obs:
            a += 1
        elif pred:
            b += 1
        elif obs:
            c += 1
        else:
            d += 1
    n = a + b + c + d
    assert n == dias - 1
    pod, far, csi = a / (a + c), b / (a + b), a / (a + b + c)
    hss1 = 2 * (a * d - b * c) / ((a + c) * (c + d) + (a + b) * (b + d))
    pc = (a + d) / n
    e = ((a + b) * (a + c) + (c + d) * (b + d)) / n ** 2
    hss2 = (pc - e) / (1 - e)
    assert abs(hss1 - hss2) < 1e-12
    base = (a + c) / n
    print(f"pares de dias: {n} ; aciertos a = {a}, falsas alarmas b = {b}, fallos c = {c}, negativos correctos d = {d}")
    print(f"tasa base de R1 o mayor = {base:.3f} ; POD = {pod:.3f} ; FAR = {far:.3f} ; CSI = {csi:.3f} ; Heidke = {hss1:.3f} (dos formulas: {hss2:.3f})")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
