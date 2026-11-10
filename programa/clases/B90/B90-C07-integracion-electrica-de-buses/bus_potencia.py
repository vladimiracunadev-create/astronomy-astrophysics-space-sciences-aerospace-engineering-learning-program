#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C07: caida en el arnes, presupuesto de potencia y corriente de arranque de un bus SINTETICO.

Cargas de potencia constante P_i: I = P/V_c con V_c = V_s - I R (cuadratica). Se resuelve en forma cerrada y por iteracion de punto fijo.
Arranque: capacitor C_in cargado a traves de R_tot: i(t) = (V/R) exp(-t/(R C)); se compara con integracion explicita.
Resistividad del cobre a 20 C: 1.72e-8 ohm m (valor de uso general, NO consultado). Unidades SI. Tolerancia: 1e-9 relativo (cuadratica
frente a iteracion) y 1e-3 (Euler frente a exponencial).
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: bateria 8.4 V, arnes de cobre AWG24 de 0.5 m (ida) + 0.5 m (retorno), 4 cargas")
rho = 1.72e-8
d_cond = 0.511e-3                      # diametro de un conductor AWG24 [m]
A = math.pi * d_cond**2 / 4
Rm = rho / A
L = 1.0                                # m (ida + retorno)
R_arn = Rm * L
R_fuente = 0.05                        # resistencia interna de la bateria [ohm] (sintetica)
R = R_arn + R_fuente
Vs = 8.4
print(f"Seccion = {A * 1e6:.4f} mm2 ; R por metro = {Rm * 1000:.2f} mohm/m ; R arnes = {R_arn * 1000:.1f} mohm ; R total = {R * 1000:.1f} mohm")
cargas = {"OBC": 1.0, "COM (transmision)": 6.0, "ADCS": 2.0, "Carga util": 3.0}
P = sum(cargas.values())
# V_c = V_s - (P/V_c) R  ->  V_c^2 - V_s V_c + P R = 0
disc = Vs**2 - 4 * P * R
Vc = (Vs + math.sqrt(disc)) / 2
I = P / Vc
print(f"Potencia total = {P:.1f} W ; V en la carga = {Vc:.4f} V ; I = {I:.4f} A ; caida = {(Vs - Vc) * 1000:.1f} mV ; perdida I2R = {I * I * R:.4f} W")
v = Vs
for _ in range(200):
    v = Vs - (P / v) * R
print(f"Iteracion de punto fijo: V = {v:.9f} V (diferencia con la cuadratica = {abs(v - Vc):.2e} V)")
comprobar(abs(v - Vc) / Vc < 1e-9, "la iteracion debe coincidir con la solucion cuadratica")
Vmin = 6.0                              # tension minima de operacion de las cargas [V] (sintetica)
print(f"Tension minima de operacion = {Vmin} V -> {'CUMPLE' if Vc >= Vmin else 'NO CUMPLE'} ; margen = {(Vc - Vmin):.3f} V")
comprobar(Vc >= Vmin, "el bus de ejemplo debe cumplir la tension minima")
eta = (Vc * I) / (Vs * I)
print(f"Eficiencia del arnes = {eta * 100:.2f} %")
print("Longitud de arnes [m] -> caida [mV] a P total")
for Lx in (0.5, 1.0, 2.0, 4.0):
    Rx = Rm * Lx + R_fuente
    Vx = (Vs + math.sqrt(Vs**2 - 4 * P * Rx)) / 2
    print(f"   {Lx:3.1f} -> {(Vs - Vx) * 1000:7.1f}")

# Corriente de arranque al cerrar el interruptor con un capacitor de entrada de 470 uF
C = 470e-6
pico_directo = Vs / R
print(f"Arranque directo: I pico = {pico_directo:.1f} A ; tau = {R * C * 1e6:.1f} us")
Rlim = 2.0
pico_lim = Vs / (R + Rlim)
print(f"Con limitador de {Rlim} ohm: I pico = {pico_lim:.2f} A ; tau = {(R + Rlim) * C * 1e6:.1f} us")
E = 0.5 * C * Vs**2
print(f"Energia almacenada = {E * 1e3:.2f} mJ")
# Euler explicito del arranque directo (comprobacion)
h, q, t = 1e-8, 0.0, 0.0
imax = 0.0
tau = R * C
while t < 5 * tau:
    i = (Vs - q / C) / R
    imax = max(imax, i)
    q += i * h
    t += h
print(f"Euler: I pico = {imax:.2f} A ; V del capacitor tras 5 tau = {q / C:.4f} V")
comprobar(abs(imax - pico_directo) / pico_directo < 1e-3, "el pico numerico debe coincidir con V/R")
comprobar(abs(q / C - Vs * (1 - math.exp(-5))) < 5e-3, "la carga numerica debe seguir 1 - exp(-t/tau)")
fin()
