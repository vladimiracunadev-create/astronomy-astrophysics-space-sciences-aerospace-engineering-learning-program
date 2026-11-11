#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C28: muestreo microbiologico: probabilidad de detectar una contaminacion segun el volumen y la recuperacion, y crecimiento logistico.

Consultado (OCHMO-TB-002): el resumen lista requisitos de calidad del agua potable (V2 6026), de control de contaminacion del agua (V2 6051), de monitoreo y alerta de la calidad del agua (V2 6046)
y de contaminacion microbiana del aire (V2 6059), y exige agua microbiologicamente segura y aceptable; NO da limites microbiologicos. Todo lo numerico es ILUSTRATIVO o SINTETICO (semilla 106):
concentracion verdadera de 0.01 UFC/mL, recuperacion del metodo de 0.7, capacidad de carga de 1e6 UFC/mL, tasa de crecimiento de 0.05 1/h, umbral de accion de 100 UFC/mL.
Modelo: los organismos en una muestra siguen Poisson con media c v eps; P(detectar) = 1 - exp(-c v eps); el volumen para confianza P es -ln(1 - P)/(c eps) (3/(c eps) para 95 %).
Crecimiento logistico N(t) = K/(1 + ((K - N0)/N0) exp(-r t)).
Verificacion: el Monte Carlo coincide con 1 - exp(-mu); el volumen de 95 % da P = 0.95; el tiempo logistico cumple N(t) = umbral.
"""
from __future__ import annotations
import math
import platform
import numpy as np

C, EPS, K_CAP, RT, UMBRAL = 0.01, 0.7, 1e6, 0.05, 100.0


def p_det(c, v, eps):
    return 1 - math.exp(-c * v * eps)


def v_conf(c, eps, p):
    return -math.log(1 - p) / (c * eps)


def logistico(t, n0):
    return K_CAP / (1 + ((K_CAP - n0) / n0) * math.exp(-RT * t))


def t_umbral(n0, nu):
    return math.log(((K_CAP - n0) / n0) / ((K_CAP - nu) / nu)) / RT


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: concentraciones, recuperacion y crecimiento ILUSTRATIVOS; Monte Carlo SINTETICO (semilla 106); sin limites microbiologicos consultados")
    R = {}
    print(f"Contaminacion verdadera de {C} UFC/mL (1 UFC por 100 mL), recuperacion del metodo {EPS}:")
    print("   volumen [mL]   P(detectar)   Monte Carlo")
    rng = np.random.default_rng(106)
    N = 200000
    mc_list = []
    for v in (10.0, 100.0, 300.0, 1000.0):
        p = p_det(C, v, EPS)
        mc = float(np.mean(rng.poisson(C * v * EPS, N) > 0))
        sd = math.sqrt(p * (1 - p) / N)
        mc_list.append((v, p, mc))
        print(f"   {v:12.0f}   {p:11.4f}   {mc:11.4f}")
        assert abs(mc - p) < 4 * sd + 1e-6
    R["p100"], R["p1000"] = mc_list[1][1], mc_list[3][1]
    v95, v99 = v_conf(C, EPS, 0.95), v_conf(C, EPS, 0.99)
    R["v95"], R["v99"], R["v95_eps1"] = v95, v99, v_conf(C, 1.0, 0.95)
    print(f"Volumen para detectar con 95 % de confianza: {v95:.0f} mL (con recuperacion 1.0: {R['v95_eps1']:.0f} mL); para 99 %: {v99:.0f} mL")
    assert abs(p_det(C, v95, EPS) - 0.95) < 1e-12
    print(f"Concentracion minima detectable con 100 mL al 95 %: {-math.log(0.05)/(100*EPS):.4f} UFC/mL")
    R["cmin100"] = -math.log(0.05) / (100 * EPS)
    n0 = 1.0
    t100 = t_umbral(n0, UMBRAL)
    R["t100"] = t100
    print(f"Crecimiento logistico desde {n0} UFC/mL: llega a {UMBRAL:.0f} UFC/mL en {t100:.1f} h ({t100/24:.1f} dias); a 1e5 UFC/mL en {t_umbral(n0,1e5):.1f} h; control N(t100) = {logistico(t100, n0):.3f}")
    assert abs(logistico(t100, n0) - UMBRAL) < 1e-6
    for dt_h in (24.0, 72.0, 168.0):
        n_final = logistico(dt_h, n0)
        print(f"   si el muestreo es cada {dt_h:5.0f} h, una contaminacion de {n0} UFC/mL llega a {n_final:10.1f} UFC/mL antes del siguiente muestreo ({'supera' if n_final > UMBRAL else 'no supera'} el umbral de accion)")
    R["n24"], R["n72"] = logistico(24.0, n0), logistico(72.0, n0)
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
