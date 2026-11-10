#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C02: limites de particulas por clase y balance de particulas de una sala limpia SINTETICA.

Modelo (mezcla perfecta): V dC/dt = Q (C_sum - C) + G. Solucion exacta C(t) = C_ss + (C0 - C_ss) exp(-Q t / V),
con C_ss = C_sum + G / Q. Se verifica con RK4. Relacion de clase: C_N(D) = 10^N (0.1/D)^2.08 [part/m3, D en micrometros]
(relacion conocida de la clasificacion ISO de salas limpias; NO consultada en el texto de la norma, ver CLASE).
Unidades: m, s, particulas/m3. Datos SINTETICOS. Tolerancia: RK4 frente a exacto < 1e-6 relativo.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin


def limite(N, D_um):
    return 10 ** N * (0.1 / D_um) ** 2.08


cabecera("Datos SINTETICOS: sala de 5 m x 4 m x 3 m, 2 personas; particulas >= 0.5 um")
print("clase ISO   limite a 0.5 um [part/m3]")
for N in (5, 6, 7, 8):
    print(f"  ISO {N}     {limite(N, 0.5):12.0f}")
comprobar(abs(limite(5, 0.5) - 3520) < 20, "ISO 5 a 0.5 um debe estar cerca de 3520")
comprobar(abs(limite(7, 0.5) / limite(5, 0.5) - 100) < 1e-9, "cada clase multiplica por 10")

V = 5 * 4 * 3.0                 # m3
Q = 0.60                         # m3/s de aire de suministro
eta = 0.99995                    # eficiencia del filtro de alta eficiencia (sintetica)
C_ext = 3.5e7                    # part/m3 afuera del filtro (sintetico)
C_sum = (1 - eta) * C_ext
G = 2 * 5.0e4                    # part/s generadas por 2 personas (sintetico)
ACH = Q * 3600 / V
C_ss = C_sum + G / Q
print(f"V = {V:.0f} m3 ; Q = {Q} m3/s ; renovaciones = {ACH:.1f} 1/h ; C_sum = {C_sum:.0f} ; C_ss = {C_ss:.0f} part/m3")
for N in (5, 7):
    lim = limite(N, 0.5)
    print(f"  ISO {N}: {'CUMPLE' if C_ss <= lim else 'NO CUMPLE'} en regimen (C_ss/limite = {C_ss / lim:.2f})")

# Recuperacion tras un evento: C0 = 10 x limite ISO 7
lim7 = limite(7, 0.5)
C0 = 10 * lim7
objetivo = 0.9 * lim7
t_rec = (V / Q) * math.log((C0 - C_ss) / (objetivo - C_ss))
print(f"Evento: C0 = {C0:.0f} ; objetivo = {objetivo:.0f} ; tiempo de recuperacion = {t_rec:.0f} s = {t_rec / 60:.1f} min")


def rk4(C, h, n):
    f = lambda c: (Q * (C_sum - c) + G) / V
    for _ in range(n):
        k1 = f(C); k2 = f(C + h * k1 / 2); k3 = f(C + h * k2 / 2); k4 = f(C + h * k3)
        C += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return C


h = 0.5
n = int(round(t_rec / h))
C_num = rk4(C0, h, n)
C_ex = C_ss + (C0 - C_ss) * math.exp(-Q * (n * h) / V)
err = abs(C_num - C_ex) / C_ex
print(f"RK4 en t = {n * h:.1f} s: {C_num:.1f} ; exacto = {C_ex:.1f} ; error relativo = {err:.2e}")
comprobar(err < 1e-6, "RK4 debe coincidir con la solucion exacta")
comprobar(abs(C_ex - objetivo) < 0.01 * objetivo, "al cabo de t_rec se alcanza el objetivo")

for pers in (0, 2, 4, 8):
    c = C_sum + pers * 5.0e4 / Q
    print(f"  {pers} personas: C_ss = {c:10.0f} part/m3  -> mejor clase cumplida a 0.5 um: ISO {math.ceil(math.log10(c / (0.1 / 0.5) ** 2.08))}")
fin()
