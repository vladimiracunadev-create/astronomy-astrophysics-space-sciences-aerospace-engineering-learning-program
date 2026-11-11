#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C25: calibracion, deriva y votacion 2 de 3 de sensores de CO2, y principio de absorcion (Beer-Lambert).

Consultado (OCHMO-TB-002): el resumen lista los requisitos de registro y visualizacion de datos atmosfericos (V2 6020 y 6021), de parametros de monitoreo y alerta (V2 6022) y de monitoreo de trazas
(V2 6023), y el criterio de ppCO2 < 3 mmHg (OCHMO-TB-004). Todo lo numerico es SINTETICO o ILUSTRATIVO: tres sensores de ganancia y desplazamiento inventados con ruido de 0.15 mmHg, deriva de
0.02 mmHg/dia en uno de ellos, patrones de calibracion de 0, 1, 2 y 4 mmHg, k L de Beer-Lambert de 0.2 por mmHg. Monte Carlo con semilla 106.
Verificacion: la calibracion por minimos cuadrados recupera ganancia y desplazamiento; la votacion 2 de 3 reduce las falsas alarmas segun 3p^2 - 2p^3 (verificado por Monte Carlo); la deriva se detecta por residuo.
"""
from __future__ import annotations
import math
import platform
import numpy as np

SIG, UMBRAL = 0.15, 3.0


def q(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: sensores SINTETICOS (semilla 106) con parametros ILUSTRATIVOS; sin datos de sensores reales")
    R = {}
    rng = np.random.default_rng(106)
    g_true, o_true = 1.07, -0.12
    patron = np.array([0.0, 1.0, 2.0, 4.0])
    lec = g_true * np.repeat(patron, 25) + o_true + rng.normal(0, SIG, 100)
    A = np.vstack([np.repeat(patron, 25), np.ones(100)]).T
    sol, *_ = np.linalg.lstsq(A, lec, rcond=None)
    g_hat, o_hat = sol
    R["g_hat"], R["o_hat"] = g_hat, o_hat
    print(f"Calibracion con patrones {patron.tolist()} mmHg (25 lecturas cada uno): ganancia {g_hat:.4f} (verdadera {g_true}), desplazamiento {o_hat:.4f} (verdadero {o_true})")
    assert abs(g_hat - g_true) < 0.02 and abs(o_hat - o_true) < 0.06
    x = 2.5
    print(f"Lectura sin calibrar a {x} mmHg: {g_true*x+o_true:.3f} (error {g_true*x+o_true-x:+.3f}); calibrada: {(g_true*x+o_true-o_hat)/g_hat:.3f}")
    kL = 0.20
    print("Absorcion (Beer-Lambert) I/I0 = exp(-kL c): sensibilidad dI/dc = -kL I")
    for c in (0.0, 1.0, 3.0, 4.5):
        print(f"   c = {c:3.1f} mmHg: I/I0 = {math.exp(-kL*c):.4f}; dI/dc = {-kL*math.exp(-kL*c):.4f} por mmHg")
    R["i3"] = math.exp(-kL * 3.0)
    # falsas alarmas
    N = 400000
    R["fa"] = {}
    for mu in (2.5, 2.8):
        p = q((UMBRAL - mu) / SIG)
        p3 = 3 * p ** 2 - 2 * p ** 3
        lect = mu + rng.normal(0, SIG, (N, 3))
        mc1 = np.mean(lect[:, 0] > UMBRAL)
        mc3 = np.mean((lect > UMBRAL).sum(1) >= 2)
        R["fa"][mu] = (p, p3, mc1, mc3)
        print(f"Falsas alarmas por lectura con la verdad en {mu} mmHg y umbral {UMBRAL}: un sensor {p:.5f} (MC {mc1:.5f}); votacion 2 de 3 {p3:.2e} (MC {mc3:.2e})")
        assert abs(mc1 - p) < 4 * math.sqrt(p * (1 - p) / N) + 1e-5 and abs(mc3 - p3) < 4 * math.sqrt(p3 * (1 - p3) / N) + 1e-5 and p3 < p
    # deriva
    dias = np.arange(0, 91)
    s = np.vstack([2.5 + rng.normal(0, SIG, 91), 2.5 + rng.normal(0, SIG, 91), 2.5 + 0.02 * dias + rng.normal(0, SIG, 91)])
    med = np.median(s, axis=0)
    res = np.abs(s[2] - med)
    res7 = np.convolve(res, np.ones(7) / 7, mode='valid')
    disp = np.where(res7 > 0.3)[0] + 6
    d_det = int(disp[0]) if len(disp) else -1
    R["d_det"] = d_det
    print(f"Deriva de 0.02 mmHg/dia en el sensor 3: la media movil de 7 dias del residuo contra la mediana supera 0.3 mmHg el dia {d_det} (sesgo acumulado {0.02*d_det:.2f} mmHg)")
    print(f"Con votacion por mediana, la lectura a 90 dias vale {med[-1]:.2f} frente a {s[2][-1]:.2f} del sensor con deriva")
    assert 10 <= d_det <= 30 and abs(med[-1] - 2.5) < 0.3
    R["med90"], R["s90"] = med[-1], s[2][-1]
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
