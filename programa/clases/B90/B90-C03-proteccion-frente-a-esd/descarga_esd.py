#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C03: descarga electrostatica con un modelo de circuito RC (cuerpo humano) y su control por resistencia.

Modelo: capacitor C cargado a V descarga por R: i(t) = (V/R) exp(-t/(R C)); energia E = C V^2 / 2; carga Q = C V.
Los valores C = 100 pF y R = 1500 ohm son los parametros CONVENCIONALES de un modelo de cuerpo humano
(no consultados en el texto de la norma; ver CLASE). Umbrales de sensibilidad de componentes: SINTETICOS.
Unidades SI. Tolerancia: integracion numerica frente a formula cerrada < 1e-4 relativo.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: parametros convencionales C = 100 pF, R = 1.5 kohm; tensiones de ejemplo")
C, R = 100e-12, 1500.0
tau = R * C
print(f"tau = R C = {tau * 1e9:.1f} ns")
print("V [V]   Q [nC]   E [uJ]   I_pico [A]")
for V in (250, 500, 1000, 2000, 4000, 8000):
    print(f"{V:6d} {C * V * 1e9:8.1f} {0.5 * C * V**2 * 1e6:8.1f} {V / R:10.3f}")

# Integracion numerica de i(t) y comparacion con formula cerrada para V = 2000 V
V = 2000.0
t = np.linspace(0, 12 * tau, 200001)
i = (V / R) * np.exp(-t / tau)
Q_num = np.trapezoid(i, t)
E_num = np.trapezoid(i**2 * R, t)
print(f"V = 2000 V: Q numerica = {Q_num * 1e9:.4f} nC (formula {C * V * 1e9:.4f}) ; "
      f"E numerica = {E_num * 1e6:.4f} uJ (formula {0.5 * C * V**2 * 1e6:.4f})")
comprobar(abs(Q_num - C * V) / (C * V) < 1e-4, "la carga numerica debe coincidir con C V")
comprobar(abs(E_num - 0.5 * C * V**2) / (0.5 * C * V**2) < 1e-4, "la energia disipada debe ser C V^2 / 2")

# Clasificacion de un componente con umbral sintetico de 500 V
umbral = 500.0
print(f"Componente con umbral SINTETICO de {umbral:.0f} V: una descarga de 2000 V supera el umbral por factor {2000 / umbral:.1f}")

# Carga por movimiento y control por disipacion: capacitancia del cuerpo C_b = 150 pF, carga Q0 = 0.1 uC
Cb, Q0 = 150e-12, 0.1e-6
Vb = Q0 / Cb
print(f"Tension del cuerpo con Q0 = 0.1 uC y C_b = 150 pF: {Vb:.0f} V")
print("R de fuga [ohm]    tau [s]    t hasta 100 V [s]   I_pico [A]")
for Rf in (1e6, 1e9, 1e11):
    tauf = Rf * Cb
    tt = tauf * math.log(Vb / 100.0)
    print(f"  {Rf:9.0e}  {tauf:10.3e}  {tt:14.3e}   {Vb / Rf:10.3e}")
    comprobar(Vb / Rf < Vb / R, "una resistencia mayor limita la corriente pico")
# Comparacion por paso de tiempo explicito: Euler con paso pequeno frente a exacto para 1 Mohm
Rf = 1e6
v, h, tau1 = Vb, 1e-7, Rf * Cb
for _ in range(int(round(tau1 / h))):
    v += -h * v / tau1
print(f"Euler (h = 0.1 us) tras un tau (150 us): {v:.2f} V ; exacto = {Vb * math.exp(-1):.2f} V")
comprobar(abs(v - Vb * math.exp(-1)) / (Vb * math.exp(-1)) < 1e-3, "Euler debe concordar con la exponencial")
fin()
