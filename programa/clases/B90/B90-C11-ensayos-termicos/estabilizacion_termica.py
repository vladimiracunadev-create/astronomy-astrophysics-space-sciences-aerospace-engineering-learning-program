#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C11: respuesta termica de un nodo concentrado en una camara de ensayo (SINTETICO).

m c dT/dt = G (T_s(t) - T) + P, con T_s(t) rampa de r K/min hasta T_hot y luego meseta. Constante de tiempo tau = m c / G.
Solucion exacta para rampa y meseta; se contrasta con RK4. Criterio de estabilizacion (DE EJEMPLO, no de una norma): |dT/dt| < 3 K/h
y T dentro de 1 K de T_s + P/G. Unidades: s, K (o C), W. Tolerancia: RK4 frente a exacto < 1e-3 K.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: unidad de 2.0 kg (c = 900 J/kg/K), G = 2.0 W/K, disipacion 5 W, rampa de 1 K/min de 20 C a 65 C")
m, c, G, P = 2.0, 900.0, 2.0, 5.0
tau = m * c / G
r = 1.0 / 60.0                       # K/s
T0, T_hot = 20.0, 65.0
t_ramp = (T_hot - T0) / r
print(f"tau = m c / G = {tau:.0f} s = {tau / 60:.1f} min ; tiempo de rampa = {t_ramp / 60:.0f} min ; offset de regimen P/G = {P / G:.2f} K")

def Ts(t):
    return min(T0 + r * t, T_hot)

def exacta(t):
    # durante la rampa: T = T0 + P/G + r (t - tau) + r tau exp(-t/tau) con T(0) = T0 + P/G + ... (parte del regimen en T0)
    base = T0 + P / G
    if t <= t_ramp:
        return base + r * (t - tau) + r * tau * math.exp(-t / tau)
    Tr = base + r * (t_ramp - tau) + r * tau * math.exp(-t_ramp / tau)
    return T_hot + P / G + (Tr - (T_hot + P / G)) * math.exp(-(t - t_ramp) / tau)

def rk4(t_fin, h=1.0):
    T = T0 + P / G
    t = 0.0
    f = lambda t, T: (G * (Ts(t) - T) + P) / (m * c)
    while t < t_fin - 1e-9:
        k1 = f(t, T); k2 = f(t + h / 2, T + h * k1 / 2); k3 = f(t + h / 2, T + h * k2 / 2); k4 = f(t + h, T + h * k3)
        T += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return T

for t in (1800, t_ramp, t_ramp + 1800, t_ramp + 3600):
    e, n = exacta(t), rk4(t)
    print(f"t = {t / 60:6.1f} min: T_s = {Ts(t):5.1f} C ; T exacta = {e:7.3f} C ; RK4 = {n:7.3f} C ; |dif| = {abs(e - n):.1e} K")
    comprobar(abs(e - n) < 1e-3, "RK4 debe coincidir con la solucion exacta")
lag = r * tau
print(f"Retraso en regimen de rampa = r tau = {lag:.1f} K ; la unidad queda {lag:.1f} K por debajo de la camara al final de la rampa (aprox.)")

# Tiempo de estabilizacion tras el fin de la rampa: |T - (T_hot + P/G)| < 1 K y |dT/dt| < 3 K/h
obj = T_hot + P / G
t = t_ramp
while True:
    d = exacta(t) - obj
    dTdt = (exacta(t + 1) - exacta(t)) * 3600
    if abs(d) < 1.0 and abs(dTdt) < 3.0:
        break
    t += 1.0
t_est = t - t_ramp
print(f"Tiempo de estabilizacion tras la rampa = {t_est:.0f} s = {t_est / 60:.1f} min (criterio de ejemplo: dentro de 1 K y menos de 3 K/h)")
Tr = exacta(t_ramp) - obj
analitico = tau * math.log(abs(Tr) / (3.0 / 3600 * tau)) if abs(Tr) > 0 else 0.0
print(f"Desfase al fin de la rampa = {Tr:.2f} K ; tiempo para |dT/dt| < 3 K/h (analitico) = {analitico:.0f} s")
comprobar(abs(t_est - analitico) < 2.0, "el tiempo numerico debe coincidir con el analitico")

print("Margen de ensayo: T_max predicha 55 C + margen de ejemplo 10 K ->", 55 + 10, "C (igual a T_hot)")
print("Tiempo total para llegar a T_hot y estabilizar = %.1f min" % ((t_ramp + t_est) / 60))
fin()
