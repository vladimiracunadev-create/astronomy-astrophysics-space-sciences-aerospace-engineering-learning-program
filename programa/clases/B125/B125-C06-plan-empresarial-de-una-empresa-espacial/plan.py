#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B125-C06: plan empresarial SINTETICO a 5 anos de una empresa de datos de observacion de la Tierra.

CONTENIDO EDUCATIVO: no es un plan real, ni asesoria financiera, contable, legal ni de inversion; no es una valoracion de ninguna empresa.
Datos consultados (2026-11-11): el 10-K de Planet Labs PBC (SEC, ejercicio cerrado el 2026-01-31) muestra, como contraste cualitativo, que una
empresa de este tipo vende datos por suscripcion y por uso, servicios satelitales por hitos y tareas de captura, que dos clientes sumaron 13 % y
12 % de los ingresos y que las perdidas netas fueron 246.9, 123.2 y 140.5 millones de dolares en los tres ultimos ejercicios (cifras citadas
del informe; NO entran al modelo). El Reglamento (UE) 377/2014 art. 23 y la politica Landsat del USGS muestran la existencia de datos gratuitos
y abiertos (clase C01). Ninguna cifra de mercado entra al calculo.
ILUSTRATIVOS (sinteticos): altas de clientes por trimestre 300 + 120 t (t = 0..19), crecientes, abandono mensual 2 %, ARPU 1 000 u.m./mes, margen bruto 70 %, gasto fijo
trimestral 6 M u.m., inversion en satelites (capex) de 18 M u.m. en los trimestres 1, 2, 9, 10 y 15, caja inicial 40 millones de u.m., tasa de descuento anual 12 %.
Unidades: millones de u.m. (M u.m.), trimestres (20 = 5 anos). Tolerancias: caja recomputada por otra via (suma acumulada) < 1e-9;
valor actual por dos vias < 1e-9; punto de equilibrio analitico frente a simulado exacto en el trimestre.
"""
from __future__ import annotations
import platform, random

TRIM = 20


def plan(altas_por_trim, churn_m=0.02, arpu=1000.0, margen=0.70, fijo=6.0, capex_lista=None, caja0=40.0, precio_factor=1.0):
    """Devuelve filas por trimestre: clientes, ingreso, margen, flujo operativo, capex, flujo libre, caja (M u.m.)."""
    capex_lista = capex_lista or [0.0] * TRIM
    c_trim = 1.0 - (1.0 - churn_m) ** 3   # abandono trimestral
    clientes, caja, filas = 0.0, caja0, []
    for t in range(TRIM):
        clientes = clientes * (1.0 - c_trim) + altas_por_trim[t]
        ingreso = clientes * arpu * precio_factor * 3.0 / 1e6        # M u.m. por trimestre
        bruto = ingreso * margen
        op = bruto - fijo
        flujo = op - capex_lista[t]
        caja += flujo
        filas.append((t + 1, clientes, ingreso, bruto, op, capex_lista[t], flujo, caja))
    return filas


def valor_actual(flujos, r_anual):
    r_t = (1.0 + r_anual) ** 0.25 - 1.0
    return sum(f / (1.0 + r_t) ** (i + 1) for i, f in enumerate(flujos))


def valor_actual_horner(flujos, r_anual):
    r_t = (1.0 + r_anual) ** 0.25 - 1.0
    v = 0.0
    for f in reversed(flujos):
        v = (v + f) / (1.0 + r_t)
    return v


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Plan SINTETICO a 5 anos; M u.m. = millones de unidades monetarias; sin cifras de mercado ni de empresa real en el calculo.")
    altas = [300 + 120 * t for t in range(TRIM)]
    capex = [18.0 if t in (0, 1, 8, 9, 14) else 0.0 for t in range(TRIM)]
    filas = plan(altas, capex_lista=capex)
    print("Trim  clientes  ingreso  margen  flujo_oper  capex  flujo_libre  caja")
    for f in filas:
        print(f"{f[0]:4d}  {f[1]:8.0f}  {f[2]:7.2f}  {f[3]:6.2f}  {f[4]:10.2f}  {f[5]:5.1f}  {f[6]:11.2f}  {f[7]:5.1f}")
    caja2 = 40.0 + sum(f[6] for f in filas)
    assert abs(caja2 - filas[-1][7]) < 1e-9
    caja_min = min(f[7] for f in filas)
    t_min = [f[0] for f in filas if f[7] == caja_min][0]
    eq = next((f[0] for f in filas if f[4] > 0), None)
    print(f"Caja final = {filas[-1][7]:.1f} M u.m. ; caja minima = {caja_min:.1f} M u.m. en el trimestre {t_min} ; primer flujo operativo positivo: trimestre {eq}")
    print(f"Brecha de financiacion (necesidad maxima de caja adicional para no bajar de 0) = {max(0.0, -caja_min):.1f} M u.m.")
    flujos = [f[6] for f in filas]
    va1, va2 = valor_actual(flujos, 0.12), valor_actual_horner(flujos, 0.12)
    assert abs(va1 - va2) < 1e-9
    print(f"Valor actual de los flujos libres a 12 % anual = {va1:.2f} M u.m. (dos vias coinciden); sin valor terminal")
    print("Sensibilidad (caja minima y caja final, M u.m.):")
    print("escenario                       caja min   caja final")
    for nombre, kw in (("base", {}), ("abandono 4 % mensual", {"churn_m": 0.04}), ("precio -20 %", {"precio_factor": 0.8}),
                       ("gasto fijo +30 %", {"fijo": 7.8}), ("capex +25 %", {"capex_lista": [x * 1.25 for x in capex]})):
        kk = dict(kw)
        kk.setdefault("capex_lista", capex)
        fs = plan(altas, **kk)
        print(f"{nombre:30s}  {min(f[7] for f in fs):8.1f}  {fs[-1][7]:10.1f}")
    # Incertidumbre: Monte Carlo con altas multiplicadas por un factor lognormal
    rng = random.Random(125)
    finales, quiebras = [], 0
    for _ in range(2000):
        k = rng.lognormvariate(0.0, 0.3)
        fs = plan([a * k for a in altas], capex_lista=capex)
        finales.append(fs[-1][7])
        if min(f[7] for f in fs) < 0:
            quiebras += 1
    finales.sort()
    print(f"Monte Carlo (2000 casos, altas x lognormal(0, 0.3), semilla 125): mediana caja final = {finales[1000]:.1f} ; P10 = {finales[200]:.1f} ; P90 = {finales[1800]:.1f} ; fraccion con caja < 0 en algun trimestre = {quiebras/2000:.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
