#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B98-C03: tiempo de una tarea de conduccion con 'mover y esperar' frente a control supervisado.

Datos CONSULTADOS (2026-11-10): distancia minima y maxima Tierra-Marte, 54.6e6 km y 401.4e6 km (ficha de Marte, NASA/NSSDC);
c = 299 792 458 m/s exacta (CODATA 2022, NIST). El tiempo de luz de una vía se CALCULA aqui: t = d/c.
ILUSTRATIVOS (sinteticos, no medidos): distancia de la tarea 100 m; velocidad de oruga 0.04 m/s en modo manual y 0.02 m/s en
modo autonomo (sobrecoste de comprobar peligros); paso por orden 1 m (mover y esperar) o 10 m (supervisado); tiempo de
decision del operador 30 s por orden manual y 120 s por meta supervisada; procesamiento en tierra y a bordo despreciado.
Sistema de referencia: tiempo de operaciones en segundos, desde el envio de la primera orden.
Modelo: T_mover_y_esperar = N (s/v + 2 t + d_op); T_supervisado = M (S/v_a + 2 t + D_op). Comprobacion: con t -> 0 el
resultado coincide con la formula cerrada N (s/v + d_op) (tolerancia 1e-9). Solo biblioteca estandar.
"""
from __future__ import annotations
import math, platform

C = 299_792_458.0  # m/s, exacto (CODATA 2022)
D_MIN, D_MAX = 54.6e9, 401.4e9  # m (ficha NASA/NSSDC de Marte: 54.6 y 401.4 millones de km)
DIST, V_MAN, V_AUT = 100.0, 0.04, 0.02
S_MAN, S_SUP = 1.0, 10.0
OP_MAN, OP_SUP = 30.0, 120.0


def t_mover_y_esperar(t_uni):
    n = math.ceil(DIST / S_MAN)
    return n * (S_MAN / V_MAN + 2.0 * t_uni + OP_MAN)


def t_supervisado(t_uni):
    m = math.ceil(DIST / S_SUP)
    return m * (S_SUP / V_AUT + 2.0 * t_uni + OP_SUP)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Distancias (ficha de Marte, NASA/NSSDC, consultada 2026-11-10); c exacta (CODATA 2022, NIST)")
    casos = [("sin retardo (referencia)", 0.0), ("Marte, distancia minima", D_MIN / C), ("Marte, distancia maxima", D_MAX / C)]
    print(f"Tarea SINTETICA: {DIST:.0f} m; manual {V_MAN} m/s en pasos de {S_MAN:.0f} m; supervisado {V_AUT} m/s en metas de {S_SUP:.0f} m")
    print(f"{'caso':26s} {'t 1 via [s]':>11s} {'t 1 via [min]':>13s} {'mover y esperar [h]':>20s} {'supervisado [h]':>16s} {'razon':>7s}")
    res = {}
    for nombre, t in casos:
        a, b = t_mover_y_esperar(t), t_supervisado(t)
        res[nombre] = (t, a, b)
        print(f"{nombre:26s} {t:11.1f} {t / 60:13.2f} {a / 3600:20.2f} {b / 3600:16.2f} {a / b:7.2f}")
    # Comprobaciones
    t0, a0, b0 = res["sin retardo (referencia)"]
    cerrada = math.ceil(DIST / S_MAN) * (S_MAN / V_MAN + OP_MAN)
    assert abs(a0 - cerrada) < 1e-9
    assert abs(res["Marte, distancia minima"][0] - 54.6e9 / C) < 1e-9
    assert res["Marte, distancia maxima"][1] > res["Marte, distancia minima"][1] > a0
    assert res["Marte, distancia maxima"][2] < res["Marte, distancia maxima"][1]
    # Fraccion del tiempo que se pasa esperando la luz
    for nombre in ("Marte, distancia minima", "Marte, distancia maxima"):
        t, a, b = res[nombre]
        espera_a = math.ceil(DIST / S_MAN) * 2 * t / a
        espera_b = math.ceil(DIST / S_SUP) * 2 * t / b
        print(f"{nombre}: fraccion del tiempo esperando la luz: manual {espera_a:.1%}, supervisado {espera_b:.1%}")
    # Numero de ciclos de orden-respuesta por tarea
    print(f"Ciclos orden-respuesta: manual {math.ceil(DIST / S_MAN)}, supervisado {math.ceil(DIST / S_SUP)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
