#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C04: presupuesto de deposito molecular por desgasificacion (datos SINTETICOS).

TML = 100 (m_i - m_f)/m_i ; CVCM = 100 m_col/m_i (definiciones de la prueba de desgasificacion; los umbrales 1.0 % y 0.10 %
usados aqui son un limite DE EJEMPLO, no consultado). Deposito: m_dep = m_cond F, con F el factor de vista
F = int cos(te) cos(tr) /(pi r^2) dA_r de una fuente puntual lambertiana a un receptor plano; espesor = m_dep / (rho A).
Comprobacion: integral numerica sobre el receptor frente a la aproximacion puntual. Unidades SI (mg, g, m, nm).
Tolerancia: integral numerica frente a aproximacion puntual < 3 %.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: adhesivo de 50 g, receptor optico de 50 mm x 50 mm a 0.3 m")
mi, mf, mcol = 200.0, 198.2, 0.10            # mg
TML = 100 * (mi - mf) / mi
CVCM = 100 * mcol / mi
lim_TML, lim_CVCM = 1.0, 0.10                # limites DE EJEMPLO
print(f"Muestra: TML = {TML:.2f} % (limite de ejemplo {lim_TML}) ; CVCM = {CVCM:.3f} % (limite de ejemplo {lim_CVCM})")
comprobar(TML <= lim_TML and CVCM <= lim_CVCM, "el material de ejemplo debe cumplir el limite de ejemplo")

m_mat = 50.0                                  # g de adhesivo en el equipo
m_cond = m_mat * CVCM / 100 * 1e-3            # kg de condensables
print(f"Condensables de {m_mat:.0f} g de material: {m_cond * 1e6:.1f} mg")

# Receptor: cuadrado de 50 mm, plano paralelo a la emision, centro en (0.1, 0, 0.3) m
L, zc, xc = 0.05, 0.30, 0.10
A = L * L
n = 400
xs = xc + (np.arange(n) + 0.5) / n * L - L / 2
ys = (np.arange(n) + 0.5) / n * L - L / 2
X, Y = np.meshgrid(xs, ys)
r2 = X**2 + Y**2 + zc**2
cos2 = zc**2 / r2                              # cos(te) cos(tr), planos paralelos
F_num = np.sum(cos2 / (math.pi * r2)) * (L / n) ** 2
r2c = xc**2 + zc**2
F_pto = (zc**2 / r2c) * A / (math.pi * r2c)
err = abs(F_num - F_pto) / F_pto
print(f"Factor de vista: numerico = {F_num:.6e} ; puntual = {F_pto:.6e} ; diferencia = {err * 100:.2f} %")
comprobar(err < 0.03, "la aproximacion puntual debe estar a menos de 3 % de la integral")

rho = 1000.0                                    # kg/m3 (densidad de la pelicula, sintetica)
def espesor_nm(m_dep_kg):
    return m_dep_kg / (rho * A) * 1e9

m_dep = m_cond * F_num
esp = espesor_nm(m_dep)
limite_nm = 10.0                                # limite de espesor DE EJEMPLO
print(f"Deposito sin mitigar: {m_dep * 1e9:.1f} ug = {m_dep * 1e12:.0f} ng ; espesor = {esp:.1f} nm (limite de ejemplo {limite_nm} nm)")
print("Mitigacion (bakeout): eficiencia -> espesor [nm] -> cumple?")
for eta in (0.0, 0.5, 0.9, 0.95):
    e = esp * (1 - eta)
    print(f"   {eta:4.2f} -> {e:6.2f} nm -> {'SI' if e <= limite_nm else 'NO'}")
need = 1 - limite_nm / esp
print(f"Eficiencia minima de eliminacion = {need * 100:.1f} %")
comprobar(abs(esp * (1 - need) - limite_nm) < 1e-9, "con la eficiencia minima se llega justo al limite")
print("Distancia r [m] -> espesor [nm] (cos(te) cos(tr) = 0.9 fijo)")
for r in (0.15, 0.3, 0.6):
    F = 0.9 * A / (math.pi * r * r)
    print(f"   {r:4.2f} -> {espesor_nm(m_cond * F):8.2f}")
fin()
