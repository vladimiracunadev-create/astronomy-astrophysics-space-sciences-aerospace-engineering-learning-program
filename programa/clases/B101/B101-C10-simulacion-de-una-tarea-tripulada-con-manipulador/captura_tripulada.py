#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C10: captura simulada con un operador humano modelado (retardo + ganancia) y una carga de objetivo en una dimension.

Modelo SINTETICO: x' = v_cmd(t - tau) con v_cmd = clip(K (x_obj - x_visto)) ; limite de velocidad de 0.1 m/s ; temblor de velocidad
gaussiano de 2 mm/s (semilla 110). Exito: |x - x_obj| <= 0.05 m y |v| <= 0.02 m/s al final de 120 s. Los umbrales son ILUSTRATIVOS.
Comprobacion independiente: x' = -K x(t - tau) es estable si y solo si K tau < pi/2. Unidades: m, s.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: operador como retardo + ganancia ; umbrales de captura ilustrativos")
dt = 0.02


def lazo(K, tau, T=120.0, x0=0.0, obj=5.0, vmax=0.1, ruido=0.0, rng=None, saturar=True):
    n = int(T / dt)
    d = int(round(tau / dt))
    x = np.zeros(n + 1)
    v = np.zeros(n + 1)
    x[0] = x0
    cmd = np.zeros(n + 1)
    for k in range(n):
        cmd[k] = K * (obj - x[k])
        if saturar:
            cmd[k] = np.clip(cmd[k], -vmax, vmax)
        vk = cmd[k - d] if k >= d else 0.0
        if ruido and rng is not None:
            vk += rng.normal(0, ruido)
        v[k] = vk
        x[k + 1] = x[k] + vk * dt
    return x, v, cmd


# 1) criterio K tau < pi/2 sin saturacion: x' = -K x(t - tau), x0 = 1
print("Estabilidad de x' = -K x(t - tau) (sin saturacion, x0 = 1): crece o decae segun K tau frente a pi/2 = 1.571")
for K, tau in ((0.5, 2.0), (0.5, 3.0), (0.5, 3.4), (1.0, 1.0)):
    x, _, _ = lazo(K, tau, T=300.0, x0=1.0, obj=0.0, saturar=False)
    amp0 = np.abs(x[:int(60 / dt)]).max()
    amp1 = np.abs(x[-int(60 / dt):]).max()
    estable = amp1 < amp0
    print(f"  K = {K:3.1f} /s, tau = {tau:3.1f} s: K tau = {K * tau:4.2f} -> amplitud final / inicial = {amp1 / amp0:9.2e} ({'estable' if estable else 'inestable'})")
    comprobar(estable == (K * tau < np.pi / 2), "el limite de estabilidad es K tau = pi/2")

# 2) Monte Carlo de captura segun el retardo total
rng = np.random.default_rng(110)
print("Captura simulada (100 ensayos por fila, objetivo a 5 m, K = 0.4 /s, vmax = 0.1 m/s):")
print("  retardo [s]   K tau   exito [%]   tiempo a +-0.05 m [s]   inversiones de orden")
exitos, TMED = {}, {}
for tau in (0.3, 0.8, 1.5, 2.5, 4.0):
    ok, tiempos, inv = 0, [], []
    for _ in range(100):
        x, v, cmd = lazo(0.4, tau, ruido=2e-3, rng=rng)
        dentro = np.abs(x - 5.0) <= 0.05
        ok += bool(dentro[-1] and abs(v[-1]) <= 0.02)
        idx = np.argmax(dentro) if dentro.any() else -1
        if idx > 0:
            tiempos.append(idx * dt)
        inv.append(int(np.sum(np.diff(np.sign(cmd[:-1][np.abs(cmd[:-1]) > 1e-3])) != 0)))
    exitos[tau] = ok / 100
    TMED[tau] = np.mean(tiempos) if tiempos else float('nan')
    t_med = np.mean(tiempos) if tiempos else float('nan')
    print(f"  {tau:10.1f}   {0.4 * tau:5.2f}   {100 * ok / 100:8.1f}   {t_med:19.1f}   {np.mean(inv):10.1f}")
comprobar(exitos[0.3] > 0.95 and exitos[4.0] < exitos[0.3], "el exito decrece con el retardo")
comprobar(exitos[4.0] < 0.2, "con K tau > pi/2 la captura falla")

# 3) mover y esperar frente a control continuo
print("Estrategia 'mover y esperar': 10 pasos de 0.5 m a 0.1 m/s (5 s) y espera tau + 1 s de observacion, frente al control continuo")
for tau in (0.3, 1.5, 4.0):
    t_mw = 10 * (5.0 + tau + 1.0)
    cont = TMED[tau] if exitos[tau] > 0.5 else float('nan')
    txt = f"{cont:5.1f} s" if cont == cont else "falla (K tau > 1.57 con saturacion)"
    print(f"  retardo {tau:3.1f} s: mover y esperar = {t_mw:6.1f} s ; control continuo = {txt}")
comprobar(10 * (5.0 + 4.0 + 1.0) > 10 * (5.0 + 0.3 + 1.0), "mover y esperar crece con el retardo")
comprobar(exitos[4.0] < 0.5 and exitos[1.5] > 0.9, "con retardo grande solo funciona mover y esperar")

# 4) ley de Fitts: MT = a + b log2(2 D / W), con a y b SINTETICOS
a_f, b_f = 0.2, 0.15
print("Ley de Fitts (forma consultada en la literatura: NO consultada aqui; a = 0.2 s, b = 0.15 s/bit SINTETICOS):")
for D, W in ((0.5, 0.1), (2.0, 0.1), (2.0, 0.05), (5.0, 0.05)):
    ID = np.log2(2 * D / W)
    print(f"  D = {D:3.1f} m, W = {W:4.2f} m: ID = {ID:5.2f} bits ; MT = {a_f + b_f * ID:5.2f} s")
comprobar(abs(np.log2(2 * 2.0 / 0.05) - np.log2(2 * 2.0 / 0.1) - 1.0) < 1e-12, "reducir W a la mitad suma un bit")
fin()
