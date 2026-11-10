#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C07: control de impedancia en una dimension frente a una pared elastica.

Datos SINTETICOS: masa efectiva del extremo m = 20 kg; pared de rigidez k_e = 5000 N/m en x = 0; objetivo x_d = +0.02 m (dentro de la pared).
Impedancia deseada: M_d x'' + B_d x' + K_d (x - x_d) = F_ext, con F_ext = -k_e x para x > 0 (fuerza de la pared sobre el extremo).
Ley de control: u = m a_des - F_ext, con a_des = (-B_d x' - K_d (x - x_d) + F_ext) / M_d (sensor de fuerza ideal, sin retardo).
Euler semi-implicito, dt = 1 ms. Unidades: m, s, N, kg. Comprobacion: fuerza en regimen permanente y factor de amortiguamiento analiticos.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: m = 20 kg, k_e = 5000 N/m, x_d = +0.02 m, sensor de fuerza ideal")
m, ke, xd, Md = 20.0, 5000.0, 0.02, 20.0
dt = 1e-3


def simular(Kd, zeta_libre=1.0, x0=-0.05, v0=0.05, T=6.0, ke_=ke):
    Bd = 2 * zeta_libre * np.sqrt(Kd * Md)
    global VC
    x, v = x0, v0
    VC = None
    xs, Fs = [], []
    for _ in range(int(T / dt)):
        Fext = -ke_ * x if x > 0 else 0.0
        a = (-Bd * v - Kd * (x - xd) + Fext) / Md
        u = m * a - Fext          # lo que ordena el actuador
        v += (u + Fext) / m * dt  # m x'' = u + F_ext
        x += v * dt
        xs.append(x)
        Fs.append(-Fext)
        if VC is None and x > 0:
            VC = v
    return np.array(xs), np.array(Fs), Bd


print("Kd [N/m]  Bd [N s/m]  F_perm [N]  F_formula [N]  F_pico [N]  x_final [mm]")
res = {}
for Kd in (200.0, 1000.0, 5000.0):
    xs, Fs, Bd = simular(Kd)
    Ff = Kd * ke / (Kd + ke) * xd
    res[Kd] = (xs, Fs)
    print(f"{Kd:8.0f}  {Bd:10.2f}  {Fs[-1]:10.3f}  {Ff:13.3f}  {Fs.max():10.3f}  {xs[-1] * 1000:11.3f}")
    comprobar(abs(Fs[-1] - Ff) < 1e-3 * Ff + 1e-6, "la fuerza permanente debe coincidir con Kd ke xd / (Kd + ke)")
comprobar(res[200.0][1][-1] < res[1000.0][1][-1] < res[5000.0][1][-1], "mas rigidez deseada, mas fuerza permanente")

# amortiguamiento critico en espacio libre: sin sobreimpulso
xs, Fs, Bd = simular(1000.0, zeta_libre=1.0, x0=-0.05, v0=0.0, ke_=0.0)
sobre = xs.max() - xd
print(f"Espacio libre con zeta = 1: x_final = {xs[-1] * 1000:.4f} mm (objetivo 20 mm) ; sobreimpulso = {sobre * 1e6:.2f} micras")
comprobar(sobre < 1e-6 and abs(xs[-1] - xd) < 1e-5, "sin sobreimpulso")
xs2, _, _ = simular(1000.0, zeta_libre=0.3, x0=-0.05, v0=0.0, ke_=0.0)
so2 = (xs2.max() - xd) / (xd + 0.05)
teor = np.exp(-np.pi * 0.3 / np.sqrt(1 - 0.3**2))
print(f"Espacio libre con zeta = 0.3: sobreimpulso relativo = {so2:.4f} ; formula exp(-pi zeta / sqrt(1 - zeta^2)) = {teor:.4f}")
comprobar(abs(so2 - teor) < 0.01, "sobreimpulso de un sistema de segundo orden")

# impacto: fuerza pico frente a la cota sin amortiguamiento
print("Impacto a 0.05 m/s contra la pared (Kd = 1000):")
for z in (0.3, 1.0, 2.0):
    xs, Fs, Bd = simular(1000.0, zeta_libre=z, x0=-0.001, v0=0.05)
    Ke, xeq = 1000.0 + ke, 1000.0 * xd / (1000.0 + ke)
    cota = ke * (xeq + np.sqrt(xeq**2 + Md * VC**2 / Ke))   # amplitud sin amortiguamiento con Kd + ke y velocidad de contacto VC
    print(f"  zeta = {z:3.1f}: v_contacto = {VC:.4f} m/s ; F_pico = {Fs.max():8.2f} N ; cota sin amortiguamiento = {cota:8.2f} N")
    comprobar(Fs.max() <= cota * 1.001, "la fuerza pico no debe superar la cota sin amortiguamiento")
# estabilidad numerica: Euler semi-implicito con dt grande
dt_guardado = dt
for dt_t in (1e-3, 2e-2):
    dt = dt_t
    xs, Fs, Bd = simular(5000.0, T=2.0)
    print(f"Paso dt = {dt_t * 1000:4.0f} ms, Kd = 5000: |x| maximo = {np.abs(xs).max():.3f} m ({'estable' if np.abs(xs).max() < 1 else 'inestable'})")
    if dt_t == 1e-3:
        comprobar(np.abs(xs).max() < 1, "el paso de 1 ms es estable")
dt = dt_guardado
fin()
