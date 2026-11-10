#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C08: tasa de fotodisociacion con atenuacion por polvo (modelo SINTETICO).

Datos: ILUSTRATIVOS. Seccion eficaz en caja de 1.0e-17 cm2 entre 91.2 y 110.0 nm; flujo plano de 1.0e6 fotones cm-2 s-1 nm-1 en el exterior de la nube;
atenuacion exponencial exp(-gamma A_V) con gamma = 2.5 (ilustrativo); relacion A_V = N_H / 1e21 cm-2 (ILUSTRATIVA). Heays et al. (2017) se consulto solo por su resumen
(secciones eficaces y tasas de fotodisociacion en campos estandar, atenuadas por polvo y apantalladas); no se uso ninguna cifra suya.
Modelo: k0 = integral(sigma F d lambda) (regla del trapecio) ; k(A_V) = k0 exp(-gamma A_V) ; tiempo de vida 1/k.
Supuestos: campo plano unidireccional; sin apantallamiento molecular. Validez: ilustrativa.
Tolerancia: integral numerica vs analitica 1e-9 relativo; tasa atenuada vs formula 1e-12.
"""
from __future__ import annotations
import math, platform

SIG, L1, L2 = 1.0e-17, 91.2, 110.0
FLUJO = 1.0e6
GAMMA = 2.5
YR = 3.15576e7

def sigma(l):
    return SIG if L1 <= l <= L2 else 0.0

def k0_numerica(n=188000):
    h = (L2 - L1) / n
    s = 0.0
    for i in range(n + 1):
        w = 0.5 if i in (0, n) else 1.0
        s += w * sigma(L1 + i * h) * FLUJO
    return s * h

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    k0_ana = SIG * FLUJO * (L2 - L1)
    k0 = k0_numerica()
    err = abs(k0 - k0_ana) / k0_ana
    print("A. Seccion eficaz en caja ILUSTRATIVA 1e-17 cm2 (91.2-110.0 nm) ; flujo 1e6 fotones cm-2 s-1 nm-1")
    print(f"B. k0 (sin atenuar): numerica = {k0:.10e} s-1 ; analitica = {k0_ana:.10e} s-1 ; error relativo = {err:.2e} ; vida = {1 / k0_ana / YR:.3f} anos")
    assert err < 1e-9
    print("C. Atenuacion por polvo: k(A_V) = k0 exp(-gamma A_V), gamma = 2.5 (ILUSTRATIVO)")
    print("A_V   N_H [cm-2]     k [s-1]        vida [anos]")
    for av in (0.0, 0.5, 1.0, 2.0, 4.0, 8.0):
        k = k0_ana * math.exp(-GAMMA * av)
        assert abs(k - k0_ana * math.exp(-GAMMA * av)) < 1e-12 * k0_ana
        print(f"{av:4.1f}  {av * 1e21:.3e}   {k:.4e}    {1.0 / k / YR:.4e}")
    # profundidad a la que la vida alcanza 1e6 anos (tiempo de vida de una nube)
    t_nube = 1.0e6 * YR
    av_cr = math.log(k0_ana * t_nube) / GAMMA
    print(f"D. A_V critico para que la vida iguale 1e6 anos = ln(k0 t) / gamma = {av_cr:.3f} ; N_H = {av_cr * 1e21:.3e} cm-2")
    k_cr = k0_ana * math.exp(-GAMMA * av_cr)
    assert abs(1.0 / k_cr - t_nube) / t_nube < 1e-12
    # fraccion de molecula destruida en 1e6 anos con A_V = 1
    k1 = k0_ana * math.exp(-GAMMA * 3.0)
    f = 1.0 - math.exp(-k1 * t_nube)
    print(f"E. Con A_V = 3: fraccion fotodisociada en 1e6 anos sin reposicion = {f:.6f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
