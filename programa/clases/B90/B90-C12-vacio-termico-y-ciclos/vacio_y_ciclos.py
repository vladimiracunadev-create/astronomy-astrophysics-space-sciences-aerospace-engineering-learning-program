#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C12: evacuacion de una camara y equivalencia de ciclos termicos por fatiga (SINTETICO).

Evacuacion: V dP/dt = -S (P - P_f), P_f = Q_gas / S; dos etapas (bomba de desbaste y bomba de alto vacio): t = (V/S) ln((P0 - Pf)/(P - Pf)).
Ciclos: factor de aceleracion tipo Coffin-Manson con correccion de frecuencia y temperatura maxima (forma de Norris-Landzberg:
AF = (dT_ens/dT_op)^n (f_op/f_ens)^(1/3) exp[1414 (1/Tmax_op - 1/Tmax_ens)]; los coeficientes n = 1.9, 1/3 y 1414 K son valores de
la literatura NO consultados, usados aqui como ejemplo). Se recupera n de datos de vida sinteticos por regresion log-log.
Unidades: Pa, m3, m3/s, K, ciclos. Tolerancias: cociente exacto 1e-9; exponente ajustado 0.05.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: camara de 2 m3, dos bombas; ciclos de -40 a +60 C frente a orbita de -10 a +30 C")
V = 2.0
S1, S2 = 0.05, 0.50                   # m3/s de la bomba de desbaste y de la de alto vacio
Qg = 1.0e-4                           # Pa m3/s de gas liberado por la unidad y la camara (constante, sintetico)
P0, Pc, Pobj = 1.0e5, 10.0, 1.0e-3
Pf2 = Qg / S2
t1 = (V / S1) * math.log(P0 / Pc)
t2 = (V / S2) * math.log((Pc - Pf2) / (Pobj - Pf2))
print(f"Presion limite con S2 = {S2} m3/s: P_f = {Pf2:.1e} Pa")
print(f"Desbaste 1e5 -> 10 Pa: t1 = {t1:.0f} s ; alto vacio 10 -> 1e-3 Pa: t2 = {t2:.1f} s ; total = {(t1 + t2) / 60:.1f} min")
comprobar(Pf2 < Pobj, "el objetivo debe estar por encima de la presion limite")
# RK4 de la segunda etapa
P, t, h = Pc, 0.0, 0.01
f = lambda P: -(S2 / V) * (P - Pf2)
while P > Pobj:
    k1 = f(P); k2 = f(P + h * k1 / 2); k3 = f(P + h * k2 / 2); k4 = f(P + h * k3)
    P += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    t += h
print(f"RK4 de la etapa 2: t2 = {t:.2f} s ; formula = {t2:.2f} s ; diferencia = {abs(t - t2):.3f} s")
comprobar(abs(t - t2) < 0.05, "RK4 debe coincidir con la formula")

def af(dT_t, dT_o, f_t, f_o, Tmax_t, Tmax_o, n=1.9):
    return (dT_t / dT_o) ** n * (f_o / f_t) ** (1 / 3) * math.exp(1414 * (1 / Tmax_o - 1 / Tmax_t))

dTo, To_max, fo = 40.0, 303.15, 16 / 24.0            # ciclos/h en orbita baja: 16 por dia
dTt, Tt_max, ft = 100.0, 333.15, 1 / 4.0              # un ciclo cada 4 h en la camara
A_f = af(dTt, dTo, ft, fo, Tt_max, To_max)
print(f"AF (ensayo frente a orbita) = {A_f:.2f} ; con solo dT: {(dTt / dTo) ** 1.9:.2f}")
comprobar(abs(af(dTo, dTo, fo, fo, To_max, To_max) - 1) < 1e-12, "con las mismas condiciones el factor debe ser 1")
anios = 1.0
N_op = 16 * 365 * anios
N_t = N_op / A_f
print(f"Ciclos de orbita en {anios:.0f} ano = {N_op:.0f} ; ciclos de ensayo equivalentes = {N_t:.0f}")
ramp = 3.0                                              # K/min
dwell = 30.0                                            # min en cada extremo
t_ciclo = 2 * dTt / ramp + 2 * dwell
print(f"Duracion de un ciclo = {t_ciclo:.0f} min ; {N_t:.0f} ciclos = {N_t * t_ciclo / 60 / 24:.1f} dias")

# Recuperacion del exponente con datos sinteticos de vida: N = C dT^-n con ruido lognormal (semilla fija)
rng = np.random.default_rng(90)
dT = np.repeat([40, 60, 80, 100, 120], 20)
N = 1.0e7 * dT ** -1.9 * rng.lognormal(0, 0.15, size=dT.size)
b, a = np.polyfit(np.log(dT), np.log(N), 1)
print(f"Regresion log-log de vida frente a dT (100 datos sinteticos): pendiente = {b:.3f} (verdadera -1.9) ; C = {math.exp(a):.3e}")
comprobar(abs(b + 1.9) < 0.05, "la regresion debe recuperar el exponente")
print("dT del ensayo [K] (minimo fijo de -40 C) -> AF -> ciclos equivalentes de un ano en orbita")
for d in (60, 80, 100, 120):
    a_ = af(d, dTo, ft, fo, 233.15 + d, To_max)
    print(f"   {d:3d} -> {a_:6.2f} -> {N_op / a_:7.0f}")
fin()
