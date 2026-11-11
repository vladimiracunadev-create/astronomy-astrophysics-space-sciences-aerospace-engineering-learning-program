#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C24: intervalos de referencia, linea base personal, valor de cambio de referencia y desempeno de un umbral (datos SINTETICOS).

Biomarcador SINTETICO X (unidades arbitrarias, u.a.): poblacion sana ~ N(100, 15) con variacion intraindividual CVi = 5 % y analitica CVa = 3 %. Individuo afectado (cambio real)
= +25 u.a. Intervalo de referencia poblacional: percentiles 2.5-97.5. Valor de cambio de referencia RCV = sqrt(2) z sqrt(CVa^2 + CVi^2) (formula estandar, no consultada aqui; se verifica
por simulacion); z = 1.96. Indice de individualidad = CVi/CVg. Desempeno de un umbral: sensibilidad, especificidad y VPP con prevalencia 2 %; AUC por rangos. Semilla 105. Contenido educativo:
no es un criterio clinico. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

MU, SD_G, CVI, CVA = 100.0, 15.0, 0.05, 0.03


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): biomarcador X en u.a.; poblacion N(100, 15); CVi 5 %, CVa 3 %; no es un criterio clinico")
    rng = np.random.default_rng(105)
    n = 200000
    pers = rng.normal(MU, SD_G, n)  # punto de ajuste individual
    obs = pers * (1 + rng.normal(0, np.hypot(CVI, CVA), n))
    lo, hi = np.percentile(obs, [2.5, 97.5])
    print(f"Intervalo de referencia poblacional (2.5-97.5 %) = {lo:.1f} - {hi:.1f} u.a.")
    cvg = SD_G / MU
    ii = CVI / cvg
    print(f"CVg = {100 * cvg:.1f} %; indice de individualidad CVi/CVg = {ii:.2f} (< 0.6 sugiere que el intervalo poblacional es poco sensible a cambios personales)")
    rcv = np.sqrt(2) * 1.96 * np.hypot(CVA, CVI)
    print(f"Valor de cambio de referencia RCV = {100 * rcv:.1f} % ({rcv * MU:.1f} u.a. sobre 100)")
    # simulacion del RCV: dos mediciones del mismo individuo sin cambio real
    a = pers * (1 + rng.normal(0, CVI, n)) * (1 + rng.normal(0, CVA, n))
    b = pers * (1 + rng.normal(0, CVI, n)) * (1 + rng.normal(0, CVA, n))
    cambio = np.abs(b / a - 1)
    print(f"Simulacion: fraccion de individuos sin cambio real que superan el RCV = {np.mean(cambio > rcv):.4f} (esperado ~ 0.05 bilateral)")
    # un cambio real de +25 u.a. sobre 100 (25 %): deteccion
    c = pers * (1 + rng.normal(0, CVI, n)) * (1 + rng.normal(0, CVA, n))
    d = (pers + 25.0) * (1 + rng.normal(0, CVI, n)) * (1 + rng.normal(0, CVA, n))
    det_rcv = np.mean(np.abs(d / c - 1) > rcv)
    fuera = np.mean((d < lo) | (d > hi))
    print(f"Cambio real de +25 u.a.: detectado por RCV personal = {det_rcv:.3f}; detectado por salir del intervalo poblacional = {fuera:.3f}")
    # umbral: sensibilidad/especificidad frente a un umbral T para 'afectado' ~ N(125, 20), sano ~ N(100, 15); prevalencia 2 %
    san = rng.normal(100, 15, 100000); afe = rng.normal(125, 20, 100000)
    print("umbral  sensibilidad  especificidad   VPP (prevalencia 2 %)   VPN")
    prev = 0.02
    ppv = {}
    for t in (110, 120, 130, 140, 150):
        se = np.mean(afe > t); sp = np.mean(san <= t)
        v = prev * se / (prev * se + (1 - prev) * (1 - sp))
        vn = (1 - prev) * sp / ((1 - prev) * sp + prev * (1 - se))
        ppv[t] = v
        print(f"  {t:4d}    {se:.3f}        {sp:.3f}          {v:.3f}                 {vn:.4f}")
    # AUC por rangos
    todos = np.concatenate([san[:5000], afe[:5000]])
    rangos = todos.argsort().argsort() + 1
    auc = (rangos[5000:].sum() - 5000 * 5001 / 2) / (5000 * 5000)
    print(f"AUC (probabilidad de que un afectado supere a un sano) = {auc:.3f}")
    assert abs(np.mean(cambio > rcv) - 0.05) < 0.01
    assert ppv[150] > ppv[110]
    assert 0.5 < auc < 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
