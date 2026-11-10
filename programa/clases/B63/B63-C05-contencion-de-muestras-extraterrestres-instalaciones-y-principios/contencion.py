#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C05: principios de contencion con un modelo de balance de aire (modelo didactico).

Datos: SINTETICOS e ILUSTRATIVOS. Volumen de la sala (60 m3), renovaciones por hora, eficiencia del filtro
(0.9997), area de fuga (1 cm2), diferencia de presion (25 Pa) y coeficiente de descarga (0.6) son valores
propuestos para el ejemplo; NO describen ninguna instalacion real ni son requisitos de norma alguna
(ninguna norma de bioseguridad fue consultada para esta clase).
Modelo: (1) sala bien mezclada con renovaciones ACH: C(t) = C0 exp(-ACH t), tiempo de limpieza a una reduccion
dada t = ln(R)/ACH, contrastado con integracion numerica de Euler; (2) filtro en serie: penetracion = (1 - E)^k,
reduccion logaritmica LRV = -log10(penetracion); (3) caudal de entrada por una fuga con la sala en depresion,
Q = Cd A sqrt(2 dP / rho), con rho = 1.2 kg/m3 (aire, valor ilustrativo): el aire entra, no sale.
Sistema de referencia: SI (m3, Pa, s); aire en reposo fuera de la sala; sin viento ni fluctuaciones.
Validez: didactica; mezcla perfecta, flujo estacionario, particulas que siguen al aire.
Tolerancias: Euler dentro del 0.1 % del analitico (paso 0.01 s); LRV < 1e-12.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import math, platform

V_M3, EFIC, A_M2, DP_PA, CD, RHO = 60.0, 0.9997, 1e-4, 25.0, 0.6, 1.2


def concentracion(c0: float, ach: float, t_h: float) -> float:
    return c0 * math.exp(-ach * t_h)


def tiempo_limpieza_h(reduccion: float, ach: float) -> float:
    return math.log(reduccion) / ach


def euler(c0: float, ach: float, t_h: float, dt_s: float = 0.01) -> float:
    c, t, k = c0, 0.0, ach / 3600.0
    n = int(round(t_h * 3600.0 / dt_s))
    for _ in range(n):
        c -= k * c * dt_s
    return c


def lrv(e: float, k: int = 1) -> float:
    return -math.log10((1.0 - e) ** k)


def caudal_fuga_m3s(area=A_M2, dp=DP_PA, cd=CD, rho=RHO) -> float:
    return cd * area * math.sqrt(2.0 * dp / rho)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Sala ilustrativa V = {V_M3} m3; filtro E = {EFIC}")
    print(" ACH [1/h]   t(reduccion 1e6) [min]   caudal de aire [m3/h]")
    for ach in (6.0, 12.0, 20.0):
        t = tiempo_limpieza_h(1e6, ach)
        print(f"{ach:9.1f}   {t * 60:20.2f}   {ach * V_M3:18.0f}")
    ach = 12.0
    t_h = tiempo_limpieza_h(1e6, ach)
    c_eu = euler(1.0, ach, 0.5)
    c_an = concentracion(1.0, ach, 0.5)
    rel = abs(c_eu / c_an - 1)
    print(f"Euler vs analitico a 0.5 h (ACH = 12): {c_eu:.6e} / {c_an:.6e}  dif relativa = {rel:.2e}")
    assert rel < 1e-3
    assert abs(concentracion(1.0, ach, t_h) - 1e-6) < 1e-18
    print(f"Concentracion tras t = ln(1e6)/ACH = {t_h * 60:.2f} min es 1e-6 (comprobado).")
    print(f"LRV de un filtro = {lrv(EFIC):.4f}; en serie (2 filtros) = {lrv(EFIC, 2):.4f}")
    assert abs(lrv(EFIC, 2) - 2 * lrv(EFIC)) < 1e-12
    q = caudal_fuga_m3s()
    print(f"Fuga de 1 cm2 con dP = {DP_PA} Pa: aire entrante = {q * 1000:.3f} L/s ({q * 3600:.2f} m3/h); velocidad de entrada = {q / A_M2 / CD:.2f} m/s")
    assert q > 0
    # comprobacion de la escala: cuadruplicar dP duplica el caudal
    assert abs(caudal_fuga_m3s(dp=4 * DP_PA) / q - 2.0) < 1e-12
    print("Escala Q ~ sqrt(dP) comprobada. Pruebas superadas.")


if __name__ == "__main__":
    main()
