#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C02: modelos de ingresos por suscripcion y por servicio (modelo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria financiera, contable, legal ni de inversion.
Datos consultados (2026-11-11): en el Formulario 10-K de Planet Labs PBC (ejercicio cerrado el 2026-01-31, SEC) se lee que los servicios de
imagenes se venden en general como suscripciones de precio fijo, que el ingreso se reconoce linealmente en el plazo del contrato (o segun uso)
y, en menor medida, de una vez al transferir el acceso, y que los contratos de servicios satelitales son a largo plazo y por hitos.
NO se usa ninguna cifra de esa empresa en el calculo (las cifras de ingresos de ese informe no estaban en los extractos leidos).
ILUSTRATIVOS (sinteticos): contrato anual de suscripcion de 120 000 u.m. pagado por adelantado al inicio; contrato de servicio de 600 000 u.m.
con cuatro hitos (30 %, 20 %, 30 %, 20 %) en los meses 3, 6, 9 y 12, con cobro en los hitos; altas 100 clientes/mes; abandono mensual c = 2 %;
ingreso mensual por cliente ARPU = 1 000 u.m.; margen bruto 70 %; costo de adquisicion CAC = 6 000 u.m. por cliente.
Unidades: u.m. (unidades monetarias), meses. Tolerancias: suma reconocida = valor del contrato (1e-9 relativa);
valor de vida simulado frente a la serie geometrica dentro de 0.5 %.
"""
from __future__ import annotations
import platform


def reconocer_ratable(valor, meses):
    return [valor / meses] * meses


def reconocer_hitos(valor, hitos, meses):
    """hitos: lista de (mes, fraccion). El ingreso se reconoce en el mes del hito."""
    salida = [0.0] * meses
    for mes, f in hitos:
        salida[mes - 1] += valor * f
    return salida


def valor_vida(arpu, margen, c):
    """LTV = ARPU * margen / c (serie geometrica con abandono mensual c, sin descuento)."""
    return arpu * margen / c


def valor_vida_simulado(arpu, margen, c, meses=2000):
    vivos, total = 1.0, 0.0
    for _ in range(meses):
        total += vivos * arpu * margen
        vivos *= (1.0 - c)
    return total


def clientes_estado_estable(altas, c):
    return altas / c


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Modelo SINTETICO; ninguna cifra de ingresos de empresa real entra al calculo.")
    # Suscripcion anual prepagada frente a servicio por hitos
    rat = reconocer_ratable(120000.0, 12)
    hit = reconocer_hitos(600000.0, [(3, .3), (6, .2), (9, .3), (12, .2)], 12)
    caja_sub = [120000.0] + [0.0] * 11
    caja_hit = hit[:]
    assert abs(sum(rat) - 120000.0) < 1e-6 and abs(sum(hit) - 600000.0) < 1e-6
    print("Mes  ingreso suscripcion  caja suscripcion  deferido(fin de mes)  ingreso servicio(hitos)")
    acum = 0.0
    for m in range(12):
        acum += rat[m]
        diferido = 120000.0 - acum
        print(f"{m+1:3d}  {rat[m]:18.0f}  {caja_sub[m]:16.0f}  {diferido:20.0f}  {hit[m]:22.0f}")
    print(f"Suma reconocida suscripcion = {sum(rat):.0f} ; servicio = {sum(hit):.0f} (igual al valor del contrato)")
    # Valor de vida
    arpu, margen, c, cac = 1000.0, 0.70, 0.02, 6000.0
    ltv = valor_vida(arpu, margen, c)
    ltv_sim = valor_vida_simulado(arpu, margen, c)
    assert abs(ltv - ltv_sim) / ltv < 0.005
    payback = cac / (arpu * margen)
    print(f"LTV analitico = {ltv:.0f} u.m. ; simulado = {ltv_sim:.0f} u.m. ; LTV/CAC = {ltv/cac:.2f} ; recuperacion del CAC = {payback:.1f} meses")
    # Sensibilidad al abandono
    print("Abandono mensual c   vida media (meses)   LTV (u.m.)   LTV/CAC")
    for cc in (0.01, 0.02, 0.04, 0.08):
        l = valor_vida(arpu, margen, cc)
        print(f"{cc:19.2f}  {1/cc:18.1f}  {l:11.0f}  {l/cac:7.2f}")
    # Clientes en estado estable con 100 altas/mes
    n = clientes_estado_estable(100.0, c)
    sim, N = 0.0, 0.0
    for _ in range(3000):
        N = N * (1 - c) + 100.0
    assert abs(N - n) / n < 1e-6
    print(f"Clientes en estado estable = altas/c = {n:.0f} (simulado {N:.0f}) ; ingreso mensual = {n*arpu:.0f} u.m.")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
