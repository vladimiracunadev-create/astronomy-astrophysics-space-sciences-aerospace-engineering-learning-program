#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C15: despliegue de un panel articulado con resorte de torsion y cronologia de inhibidores (SINTETICO).

I th'' = k (th_pre - th) - tau_arr - c th', de th = 0 a th = pi/2 (traba). Margen de par = min(tau_resorte)/tau_arr (criterio de
ejemplo >= 2, NO de una norma). Comprobacion independiente: sin arrastre ni amortiguador, 1/2 I w^2 = k (th_pre th - th^2/2).
Cronologia: el temporizador no cuenta como inhibidor independiente (regla de la CubeSat Design Specification Rev. 14.1, consultada).
Unidades: kg m2, N m, N m/rad, rad, s. Tolerancia: energia numerica frente a analitica < 1e-6 relativo.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: panel de I = 2.0e-4 kg m2, resorte k = 0.020 N m/rad con precarga angular de 126 grados")
I = 2.0e-4
k = 0.020
th_pre = math.radians(126.0)
th_f = math.pi / 2
tau_arr = 0.003
c = 1.0e-4

def integra(tau_arr, c, h=1e-5):
    th, w, t = 0.0, 0.0, 0.0
    def f(th, w):
        return w, (k * (th_pre - th) - tau_arr - c * w) / I
    while th < th_f:
        k1 = f(th, w); k2 = f(th + h / 2 * k1[0], w + h / 2 * k1[1]); k3 = f(th + h / 2 * k2[0], w + h / 2 * k2[1]); k4 = f(th + h * k3[0], w + h * k3[1])
        th_n = th + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        w_n = w + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if th_n >= th_f:
            a = (th_f - th) / (th_n - th)           # interpolacion lineal al angulo de traba
            return t + a * h, w + a * (w_n - w)
        th, w, t = th_n, w_n, t + h
        if t > 5:
            return float("inf"), 0.0
    return t, w

tau_ini = k * th_pre
tau_fin = k * (th_pre - th_f)
print(f"Par del resorte: inicial = {tau_ini * 1000:.2f} mN m ; en la traba = {tau_fin * 1000:.2f} mN m ; arrastre = {tau_arr * 1000:.2f} mN m")
mr = tau_fin / tau_arr
print(f"Margen de par (minimo, en la traba) = {mr:.2f} (criterio de ejemplo >= 2.0) -> {'CUMPLE' if mr >= 2.0 else 'NO CUMPLE'}")
comprobar(mr >= 2.0, "el margen de par de ejemplo debe cumplir")
t_d, w_d = integra(tau_arr, c)
E_traba = 0.5 * I * w_d**2
print(f"Con arrastre y amortiguador: t_despliegue = {t_d:.4f} s ; w_traba = {w_d:.3f} rad/s ; energia en la traba = {E_traba * 1000:.3f} mJ")
t0, w0 = integra(0.0, 0.0)
E_num = 0.5 * I * w0**2
E_ana = k * (th_pre * th_f - th_f**2 / 2)
print(f"Caso sin perdidas: t = {t0:.4f} s ; energia numerica = {E_num * 1000:.6f} mJ ; analitica = {E_ana * 1000:.6f} mJ ; dif = {abs(E_num - E_ana) / E_ana:.1e}")
comprobar(abs(E_num - E_ana) / E_ana < 1e-6, "la energia debe coincidir con la integral del par")
print("Arrastre [mN m] -> margen -> t_despliegue [s] -> w en la traba [rad/s]")
for ta in (0.003, 0.006, 0.0095, 0.0126, 0.0150):
    t_, w_ = integra(ta, c)
    est = "no despliega" if t_ == float("inf") else f"{t_:.4f} -> {w_:.3f}"
    print(f"   {ta * 1000:6.2f} -> {tau_fin / ta:5.2f} -> {est}")

# Cronologia de inhibidores (datos de ejemplo del ICD)
print("Cronologia de ejemplo (s desde la separacion):")
t_tim = 1800.0                                # minimo de ejemplo entre separacion y primera transmision / despliegue
ev = [(0.0, "Separacion detectada (interruptores liberados)"), (0.0, "Arranque del temporizador de 1800 s"),
      (1800.0, "Temporizador vence: habilita despliegue de antena"), (1805.0, "Antena desplegada"), (1830.0, "Primera transmision")]
for t_, d_ in ev:
    print(f"   t = {t_:7.1f} s  {d_}")
comprobar(ev[-1][0] - ev[0][0] >= t_tim, "la primera transmision debe ocurrir despues del minimo del ICD")
inh = [("interruptor de separacion", True), ("pasador RBF", True), ("temporizador", False)]
indep = sum(1 for _, i in inh if i)
print(f"Inhibidores independientes = {indep} de {len(inh)} (el temporizador no cuenta); requisito: al menos 3 -> {'CUMPLE' if indep >= 3 else 'NO CUMPLE'}")
comprobar(indep == 2, "el ejemplo debe mostrar dos inhibidores independientes")
for dr in (-0.005, 0.0, 0.005):
    print(f"Deriva del temporizador {dr * 100:+.1f} % -> vence en {t_tim * (1 + dr):.1f} s")
fin()
