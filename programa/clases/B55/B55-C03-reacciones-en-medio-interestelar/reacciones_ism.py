#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C03: coeficientes de velocidad de tipo Arrhenius modificado y escalas de tiempo de reacciones en el medio interestelar.

Datos: SINTETICOS / ILUSTRATIVOS. La forma k(T) = alfa (T/300)^beta exp(-gamma/T) es la parametrizacion habitual de las bases de datos de reacciones
(el resumen de McElroy et al. 2013 describe una base de 6173 reacciones y 467 especies, consultado el 2026-11-09, pero NO se uso ningun coeficiente suyo).
Los coeficientes de las dos reacciones de ejemplo son inventados para la clase. Constante de Boltzmann no necesaria.
Modelo: A + B -> productos con B en gran exceso (pseudo-primer orden) y A + A -> productos (segundo orden). Integracion RK4 de dn/dt.
Supuestos: temperatura y densidad constantes; reaccion irreversible; sin otras fuentes ni sumideros. Validez: ilustrativa.
Tolerancia: error relativo de la integracion numerica frente a la solucion analitica < 1e-8.
"""
from __future__ import annotations
import math, platform

def k_arr(T, alfa, beta, gamma):
    """cm3 s-1 (segundo orden); T en K."""
    return alfa * (T / 300.0) ** beta * math.exp(-gamma / T)

def rk4(f, y0, t_fin, pasos):
    h = t_fin / pasos
    y = y0
    for _ in range(pasos):
        k1 = f(y); k2 = f(y + 0.5 * h * k1); k3 = f(y + 0.5 * h * k2); k4 = f(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return y

YR = 3.15576e7   # s por ano juliano

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # reacciones ILUSTRATIVAS
    R1 = ("ion-molecula (ILUSTRATIVA, sin barrera)", 1.0e-9, 0.0, 0.0)
    R2 = ("neutro-neutro con barrera (ILUSTRATIVA)", 1.0e-10, 0.0, 1500.0)
    print("A. Coeficientes k(T) en cm3 s-1 de dos reacciones ILUSTRATIVAS")
    print("T [K]   k_ion-molecula   k_neutro-neutro(barrera 1500 K)")
    for T in (10.0, 30.0, 100.0, 300.0):
        print(f"{T:5.0f}   {k_arr(T, *R1[1:]):.4e}     {k_arr(T, *R2[1:]):.4e}")
    k10 = k_arr(10.0, *R2[1:]); k300 = k_arr(300.0, *R2[1:])
    print(f"Cociente k(300 K)/k(10 K) con barrera: {k300 / k10:.4e} ; sin barrera: {k_arr(300, *R1[1:]) / k_arr(10, *R1[1:]):.4f}")
    # escalas de tiempo
    print("B. Escala de tiempo t = 1/(k n_B) [anos] para consumir A, con B en exceso")
    print("n_B [cm-3]    ion-molecula (T=10 K)   neutro-neutro (T=300 K)")
    for nb in (1.0e2, 1.0e4, 1.0e6):
        t1 = 1.0 / (k_arr(10.0, *R1[1:]) * nb) / YR
        t2 = 1.0 / (k_arr(300.0, *R2[1:]) * nb) / YR
        print(f"{nb:9.0e}     {t1:.4e}              {t2:.4e}")
    # integracion: pseudo-primer orden
    nB = 1.0e4; T = 10.0
    kk = k_arr(T, *R1[1:]) * nB
    A0 = 1.0
    t_fin = 3.0 / kk
    A_num = rk4(lambda a: -kk * a, A0, t_fin, 2000)
    A_ana = A0 * math.exp(-kk * t_fin)
    err1 = abs(A_num - A_ana) / A_ana
    print(f"C. Pseudo-primer orden (n_B = 1e4 cm-3, T = 10 K): A(3 tau) numerico = {A_num:.10e} ; analitico = {A_ana:.10e} ; error relativo = {err1:.2e}")
    assert err1 < 1e-8
    # segundo orden: dn/dt = -k n^2  => 1/n = 1/n0 + k t
    n0 = 1.0e3; kc = k_arr(100.0, *R1[1:])
    t2 = 5.0 / (kc * n0)
    n_num = rk4(lambda n: -kc * n * n, n0, t2, 4000)
    n_ana = 1.0 / (1.0 / n0 + kc * t2)
    err2 = abs(n_num - n_ana) / n_ana
    print(f"D. Segundo orden A + A (n0 = 1e3 cm-3, T = 100 K): n(t) numerico = {n_num:.8e} ; analitico = {n_ana:.8e} ; error relativo = {err2:.2e}")
    assert err2 < 1e-8
    assert abs(k_arr(300.0, 1.0, 0.7, 0.0) - 1.0) < 1e-12      # alfa = k(300 K) cuando gamma = 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
