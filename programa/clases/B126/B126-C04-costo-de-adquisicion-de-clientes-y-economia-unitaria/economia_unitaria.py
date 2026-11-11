#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C04: economia unitaria de un servicio SINTETICO de datos de observacion de la Tierra por suscripcion.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion.
Consultado: nada de este laboratorio viene de una fuente. Las definiciones de CAC, LTV y plazo de recuperacion NO se consultaron en una
fuente primaria; se verifican por dos vias de calculo (serie geometrica y simulacion de cohortes).
ILUSTRATIVOS (sinteticos): gasto de captacion de 240 000 USD por trimestre con 60 clientes nuevos; ingreso mensual por cliente (ARPA)
900 USD; margen bruto 70 %; abandono mensual 2 %; tasa de descuento 10 % anual (compuesta mensualmente).
Modelo: abandono constante, sin expansion de ingresos, CAC mezclado (todo el gasto entre todos los clientes nuevos), ARPA constante.
Formulas: CAC = gasto/clientes nuevos; LTV = ARPA*g/c; plazo = CAC/(ARPA*g) (meses, sin abandono);
LTV descontado = sum_{t>=0} ARPA*g*(1-c)^t/(1+r)^(t+1) con r mensual.
Tolerancias: serie truncada a 5000 meses frente a formula cerrada 1e-6 relativa; Monte Carlo (20000 clientes, semilla 126) frente a 1/c dentro de 1 mes.
"""
from __future__ import annotations
import platform, random

GASTO, NUEVOS = 240_000.0, 60
ARPA, G, C = 900.0, 0.70, 0.02
R_ANUAL = 0.10
R = (1 + R_ANUAL) ** (1 / 12) - 1


def ltv(arpa, g, c):
    return arpa * g / c


def ltv_serie(arpa, g, c, r=0.0, n=5000):
    return sum(arpa * g * (1 - c) ** t / (1 + r) ** t for t in range(n))


def ltv_desc_cerrada(arpa, g, c, r):
    # sum_{t>=0} m q^t/(1+r)^t con q=(1-c) -> m / (1 - (1-c)/(1+r))
    return arpa * g / (1 - (1 - c) / (1 + r))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); ninguna cifra viene de una fuente consultada.")
    cac = GASTO / NUEVOS
    margen = ARPA * G
    v = ltv(ARPA, G, C)
    print(f"CAC = {GASTO:,.0f} / {NUEVOS} = {cac:,.0f} USD ; margen bruto mensual por cliente = {margen:,.0f} USD")
    print(f"LTV (formula cerrada) = {v:,.0f} USD ; LTV (serie, 5000 meses) = {ltv_serie(ARPA, G, C):,.2f} USD")
    assert abs(ltv_serie(ARPA, G, C) - v) / v < 1e-6
    print(f"LTV/CAC = {v/cac:.2f} ; plazo de recuperacion = {cac/margen:.2f} meses")
    vd = ltv_desc_cerrada(ARPA, G, C, R)
    print(f"LTV descontado (10 % anual) = {vd:,.0f} USD (cerrada) ; serie = {ltv_serie(ARPA, G, C, R):,.0f} USD ; LTV/CAC desc = {vd/cac:.2f}")
    assert abs(vd - ltv_serie(ARPA, G, C, R)) / vd < 1e-6
    rnd = random.Random(126)
    vidas = []
    for _ in range(20000):
        t = 1
        while rnd.random() > C:
            t += 1
        vidas.append(t)
    media = sum(vidas) / len(vidas)
    print(f"Vida media del cliente: 1/c = {1/C:.1f} meses ; Monte Carlo = {media:.1f} meses")
    assert abs(media - 1 / C) < 1.0
    print("Sensibilidad de LTV/CAC (filas: abandono mensual; columnas: CAC en USD)")
    cacs = [2000, 4000, 6000, 8000]
    print("   churn   " + "".join(f"{x:>9d}" for x in cacs))
    for c in (0.01, 0.02, 0.03, 0.05, 0.08):
        print(f"   {c:5.0%}  " + "".join(f"{ltv(ARPA, G, c)/x:9.2f}" for x in cacs))
    print("Plazo de recuperacion y razon por margen bruto (CAC = 4000, abandono 2 %)")
    for g in (0.4, 0.55, 0.7, 0.85):
        print(f"   g = {g:.2f}: plazo = {cac/(ARPA*g):5.2f} meses ; LTV/CAC = {ltv(ARPA, g, C)/cac:5.2f}")
    # punto de equilibrio del abandono para LTV/CAC = 3
    c3 = ARPA * G / (3 * cac)
    print(f"Abandono mensual maximo para LTV/CAC = 3: {c3:.4f} ({c3:.2%})")
    assert abs(ltv(ARPA, G, c3) / cac - 3) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
