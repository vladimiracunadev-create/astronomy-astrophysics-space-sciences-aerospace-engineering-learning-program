#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B107-C01: dosis de entrenamiento y respuesta con un modelo de impulso-respuesta (fitness-fatigue).

TODO es SINTETICO/ILUSTRATIVO: parametros inventados para ensenar, no de astronautas ni de ninguna fuente.
Modelo: rendimiento p(t) = p0 + k1 * sum w(s) exp(-(t-s)/tau1) - k2 * sum w(s) exp(-(t-s)/tau2), t en dias, w en unidades
arbitrarias de carga (u.a.). Parametros ilustrativos: p0 = 100 (indice), k1 = 0.10, k2 = 0.30, tau1 = 42 d, tau2 = 7 d.
Verificacion: (1) respuesta a un impulso unico frente a la forma cerrada y al instante del maximo
t* = tau1 tau2/(tau1 - tau2) * ln(k2 tau1/(k1 tau2)); (2) dos planes con la MISMA carga semanal total.
Tolerancias: |t* numerico - t* analitico| <= 1 dia; diferencia de forma cerrada < 1e-9. Numpy.
"""
from __future__ import annotations
import platform
import numpy as np

P0, K1, K2, T1, T2 = 100.0, 0.10, 0.30, 42.0, 7.0


def respuesta(w):
    n = len(w)
    t = np.arange(n)
    p = np.zeros(n)
    for i in range(n):
        s = t[: i + 1]
        dt = i - s
        p[i] = P0 + K1 * np.sum(w[: i + 1] * np.exp(-dt / T1)) - K2 * np.sum(w[: i + 1] * np.exp(-dt / T2))
    return p


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS E ILUSTRATIVOS (semilla 107): parametros inventados; no son de astronautas")
    # (1) impulso unico de 100 u.a. el dia 0
    w = np.zeros(200)
    w[0] = 100.0
    p = respuesta(w)
    t = np.arange(200)
    cerrada = P0 + 100 * (K1 * np.exp(-t / T1) - K2 * np.exp(-t / T2))
    err = float(np.max(np.abs(p - cerrada)))
    tstar = T1 * T2 / (T1 - T2) * np.log(K2 * T1 / (K1 * T2))
    tnum = int(np.argmax(p))
    print(f"Impulso unico: error maximo frente a forma cerrada = {err:.2e}; minimo = {p.min():.2f} (dia {int(np.argmin(p))})")
    print(f"Instante del maximo: analitico t* = {tstar:.2f} d; numerico = {tnum} d")
    assert err < 1e-9 and abs(tnum - tstar) <= 1.0
    # (2) dos planes con la misma carga semanal (420 u.a./semana), 12 semanas, y 14 dias de afinado
    dias = 84
    plan_a = np.zeros(dias + 14)  # 6 sesiones iguales por semana (descanso el dia 7)
    plan_b = np.zeros(dias + 14)  # 3 sesiones largas por semana
    for d in range(dias):
        if d % 7 != 6:
            plan_a[d] = 70.0
        if d % 7 in (0, 2, 4):
            plan_b[d] = 140.0
    for nombre, plan in (("A: 6 x 70 u.a./sem", plan_a), ("B: 3 x 140 u.a./sem", plan_b)):
        assert abs(plan[:dias].sum() / 12 - 420) < 1e-9
        q = respuesta(plan)
        print(f"Plan {nombre}: carga total = {plan[:dias].sum():.0f} u.a.; p(dia 83) = {q[83]:.2f}; max en afinado = {q[dias:].max():.2f} (dia {dias + int(np.argmax(q[dias:]))})")
    # (3) sin carga nueva (desentrenamiento): la aptitud decae con tau1
    q = respuesta(plan_a)
    g = K1 * np.sum(plan_a[:dias] * np.exp(-(dias + 13 - np.arange(dias)) / T1))
    print(f"Componente de aptitud (fitness) al dia 97 = {g:.2f} u.a.; vida media de la aptitud = {T1*np.log(2):.1f} d; de la fatiga = {T2*np.log(2):.1f} d")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
