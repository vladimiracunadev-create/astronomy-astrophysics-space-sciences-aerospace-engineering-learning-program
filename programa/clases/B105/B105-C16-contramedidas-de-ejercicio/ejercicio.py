#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C16: energia del ejercicio y dosis-respuesta SINTETICA de una contramedida (modelo DIDACTICO).

Energia: kcal = MET x masa [kg] x horas (aproximacion de 1 MET ~ 1 kcal/kg/h; no consultada aqui). Presupuesto de tiempo: 2 h/dia de ejercicio en
6 dias por semana. Carga mecanica: fuerza de reaccion F = m a para un dispositivo de resistencia HIPOTETICO. Dosis-respuesta sintetica de tipo Hill:
reduccion relativa de la perdida osea R(L) = Rmax L/(L + L50), con L la carga semanal en unidades arbitrarias, Rmax = 0.8, L50 = 100 (ILUSTRATIVOS).
Perdida sin contramedida: 1.25 %/mes (tasa del bloque, B105-C02); con contramedida, perdida = 1.25 %(1 - R). Datos SINTETICOS con ruido, ajuste de Rmax y L50
por busqueda en rejilla de minimos cuadrados, semilla 105. Contenido educativo: NO es una prescripcion de ejercicio. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

RMAX, L50 = 0.8, 100.0


def hill(l, rmax, l50):
    return rmax * l / (l + l50)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): MET, tiempos, cargas y dosis-respuesta ilustrativos; NO es una prescripcion")
    for nombre, met in (("caminata ligera", 3.5), ("carrera moderada", 8.0), ("resistencia", 6.0)):
        print(f"  {nombre:18s} MET {met:4.1f}: 75 kg y 2 h = {met * 75 * 2:6.0f} kcal; 62 kg y 2 h = {met * 62 * 2:6.0f} kcal")
    dia = 6.0 * 75 * 2
    sem = dia * 6
    print(f"Con resistencia a 6 MET, 2 h/dia: {dia:.0f} kcal/dia; semana de 6 dias = {sem:.0f} kcal; ingesta adicional equivalente = {dia / 2668 * 100:.1f} % del gasto de 2668 kcal/dia (B105-C12)")
    m, a = 75.0, 3.0
    print(f"Fuerza de reaccion F = m a para m = {m:.0f} kg y a = {a:.0f} m/s2: {m * a:.0f} N = {m * a / (m * 9.81):.2f} veces el peso terrestre")
    rng = np.random.default_rng(105)
    cargas = np.array([0, 25, 50, 100, 200, 400, 800.0])
    y = hill(cargas, RMAX, L50) + rng.normal(0, 0.03, cargas.size)
    mejor = (1e9, 0, 0)
    for rm in np.linspace(0.5, 1.0, 101):
        for l5 in np.linspace(20, 300, 281):
            e = np.sum((y - hill(cargas, rm, l5)) ** 2)
            if e < mejor[0]:
                mejor = (e, rm, l5)
    print(f"Reduccion observada (sintetica) por carga semanal L: " + ", ".join(f"{l:.0f}->{v:.2f}" for l, v in zip(cargas, y)))
    print(f"Ajuste Hill por rejilla: Rmax = {mejor[1]:.2f} (verdad {RMAX}), L50 = {mejor[2]:.0f} (verdad {L50:.0f}); suma de cuadrados = {mejor[0]:.5f}")
    print("Perdida osea a 6 meses con la tasa de 1.25 %/mes segun la carga (modelo con la reduccion R ajustada):")
    for l in (0, 50, 100, 200, 400, 800):
        r = hill(l, mejor[1], mejor[2])
        tasa = 0.0125 * (1 - r)
        perd = 100 * (1 - (1 - tasa) ** 6)
        print(f"  L = {l:4d}: R = {r:.3f}; tasa {100 * tasa:.3f} %/mes; perdida a 6 meses = {perd:5.2f} %")
    l_obj = L50 * 0.5 / (RMAX - 0.5)
    print(f"Carga para R = 0.5 con los parametros verdaderos: L = {l_obj:.0f}")
    assert abs(hill(L50, RMAX, L50) - RMAX / 2) < 1e-12
    assert abs(6.0 * 75 * 2 - 900) < 1e-9
    assert abs(mejor[1] - RMAX) < 0.2 and abs(mejor[2] - L50) < 60
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
