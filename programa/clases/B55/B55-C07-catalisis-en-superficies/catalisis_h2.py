#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C07: salto, desorcion y ventana de temperatura para la formacion de H2 sobre un grano (modelo SINTETICO).

Datos: ILUSTRATIVOS. Frecuencia de vibracion 1e12 s-1, barrera de difusion E_b = 300 K, energia de desorcion E_d = 500 K, N_s = 1e6 sitios por grano,
tiempo entre llegadas de atomos t_llegada = 1e8 s. Ningun valor procede de una medicion consultada; Zhao et al. (2022) se consulto solo por su resumen,
que indica que la eficiencia de formacion de H2 depende de las barreras de difusion.
Modelo: tasas de Arrhenius k = nu exp(-E/T); tiempo de escaneo del grano t_esc ~ N_s ln(N_s) / k_salto (estimacion heuristica de orden de magnitud);
un atomo forma H2 con otro si t_esc < t_des y t_esc < t_llegada. Camino aleatorio 2D en red para verificar <r^2> = n (Monte Carlo con semilla fija).
Supuestos: red cuadrada, un solo tipo de sitio, sin tunelamiento. Validez: ilustrativa.
Tolerancia: <r^2> vs n a 3 %; ventana de T con ambas condiciones coherentes (T_min < T_max).
"""
from __future__ import annotations
import math, platform, random

NU = 1.0e12
EB, ED = 300.0, 500.0
NS = 1.0e6
T_LLEG = 1.0e8

def k(E, T):
    return NU * math.exp(-E / T)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Parametros ILUSTRATIVOS: nu = 1e12 s-1 ; E_b = 300 K ; E_d = 500 K ; N_s = 1e6 sitios ; t_llegada = 1e8 s")
    print("T [K]   k_salto [s-1]   k_des [s-1]    t_escaneo [s]   t_des [s]   forma H2?")
    for T in (6.0, 8.0, 10.0, 11.0, 12.0, 13.0, 15.0, 20.0):
        ks, kd = k(EB, T), k(ED, T)
        t_esc = NS * math.log(NS) / ks
        t_des = 1.0 / kd
        ok = (t_esc < t_des) and (t_esc < T_LLEG)
        print(f"{T:5.1f}   {ks:.3e}    {kd:.3e}   {t_esc:.3e}    {t_des:.3e}   {'si' if ok else 'no'}")
    n_ln = NS * math.log(NS)
    T_max = (ED - EB) / math.log(n_ln)
    T_min = EB / math.log(T_LLEG * NU / n_ln)
    print(f"B. Ventana analitica: T_min = E_b / ln(t_llegada nu / (N ln N)) = {T_min:.2f} K ; T_max = (E_d - E_b) / ln(N ln N) = {T_max:.2f} K")
    assert T_min < T_max
    # comprobacion de la ventana
    for T in (T_min + 0.2, (T_min + T_max) / 2, T_max - 0.2):
        ks, kd = k(EB, T), k(ED, T)
        t_esc = NS * math.log(NS) / ks
        assert t_esc < 1.0 / kd and t_esc < T_LLEG, T
    for T in (T_min - 0.5, T_max + 0.5):
        ks, kd = k(EB, T), k(ED, T)
        t_esc = NS * math.log(NS) / ks
        assert not (t_esc < 1.0 / kd and t_esc < T_LLEG), T
    print("C. Dentro de la ventana se cumplen ambas condiciones y fuera de ella al menos una falla: superado")
    # camino aleatorio
    rng = random.Random(2024)
    print("D. Camino aleatorio 2D (Monte Carlo, 4000 caminantes, semilla 2024): <r^2> frente a n saltos")
    print("n saltos   <r^2> MC   n (analitico)")
    pasos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for n in (10, 100, 1000):
        s = 0.0
        for _ in range(4000):
            x = y = 0
            for _ in range(n):
                dx, dy = pasos[rng.randrange(4)]
                x += dx; y += dy
            s += x * x + y * y
        m = s / 4000.0
        print(f"{n:8d}   {m:9.2f}   {n:9d}")
        assert abs(m - n) / n < 0.03, (n, m)
    print(f"E. Tiempo de salto a 10 K = {1.0 / k(EB, 10.0):.3e} s ; a 20 K = {1.0 / k(EB, 20.0):.3e} s ; cociente = {k(EB, 20.0) / k(EB, 10.0):.1f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
