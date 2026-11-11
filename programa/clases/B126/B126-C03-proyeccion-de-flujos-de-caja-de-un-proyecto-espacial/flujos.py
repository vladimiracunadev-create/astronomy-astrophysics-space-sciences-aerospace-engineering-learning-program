#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C03: flujos de caja de un proyecto espacial SINTETICO (constelacion de observacion de la Tierra, 10 anos).

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion.
Consultado (2026-11-11): el informe de la NASA sobre COTS (NASA SP-2014-617): los pagos por hitos de precio fijo hacen que los
sobrecostos recaigan en la empresa y no en la agencia; esos hitos son una fuente de caja a programar. Ninguna cifra de este laboratorio
viene de ahi.
ILUSTRATIVOS (sinteticos): toda la serie de inversiones, clientes, precios y costos (millones de USD constantes, anos 0 a 9).
Modelo: flujos anuales deterministas, sin impuestos, sin capital de trabajo, sin deuda; ingresos = clientes x precio anual;
costo variable = 25 % de los ingresos; costo fijo anual dado.
Pruebas: (1) caja acumulada por itertools.accumulate frente a suma directa (1e-9); (2) caja minima = financiamiento necesario;
(3) el escenario con retraso de 1 ano se calcula desplazando los ingresos y por recalculo con clientes a cero en el ano 3 (igualdad).
"""
from __future__ import annotations
import itertools, platform

ANOS = list(range(10))
CAPEX = [20.0, 15.0, 10.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0]       # M USD
CLIENTES = [0, 0, 20, 60, 110, 150, 180, 200, 210, 215]
PRECIO = 0.35                                                       # M USD por cliente por ano
FIJO = [1.0, 2.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
VAR = 0.25


def flujos(clientes, capex=CAPEX, precio=PRECIO):
    out = []
    for t in ANOS:
        ing = clientes[t] * precio
        out.append(ing - VAR * ing - FIJO[t] - capex[t])
    return out


def resumen(nombre, f):
    acum = list(itertools.accumulate(f))
    for t in ANOS:
        assert abs(acum[t] - sum(f[: t + 1])) < 1e-9
    minimo = min(acum)
    t_min = acum.index(minimo)
    be = next((t for t in ANOS if acum[t] >= 0), None)
    print(f" {nombre:<18} caja minima {minimo:8.2f} M (ano {t_min})   financiamiento con 15 % de margen {max(0,-minimo)*1.15:7.2f} M   acumulada ano 9 {acum[-1]:8.2f} M   caja >= 0: {'ano '+str(be) if be is not None else 'no ocurre'}")
    return acum, minimo


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); de COTS solo se consulto el esquema de hitos de precio fijo (NASA SP-2014-617, 2026-11-11).")
    print("Unidades: millones de USD constantes por ano; anos 0 a 9")
    base = flujos(CLIENTES)
    print(" ano  clientes  ingreso   flujo_neto   caja_acumulada")
    acum0 = list(itertools.accumulate(base))
    for t in ANOS:
        print(f" {t:3d}  {CLIENTES[t]:8d}  {CLIENTES[t]*PRECIO:7.2f}  {base[t]:11.2f}  {acum0[t]:14.2f}")
    print("Escenarios:")
    b_acum, b_min = resumen("base", base)
    menos = flujos([int(c * 0.8) for c in CLIENTES])
    resumen("clientes -20 %", menos)
    caro = flujos(CLIENTES, capex=[x * 1.3 for x in CAPEX])
    resumen("capex +30 %", caro)
    # retraso de 1 ano: ingresos desplazados
    retr_clientes = [0] + CLIENTES[:-1]
    retr = flujos(retr_clientes)
    resumen("retraso 1 ano", retr)
    # via 2: el retraso equivale a clientes[t-1]; comprobar el ano 3 (clientes pasan de 60 a 20)
    assert retr_clientes[3] == CLIENTES[2] == 20
    assert abs(retr[3] - (20 * PRECIO * (1 - VAR) - FIJO[3] - CAPEX[3])) < 1e-9
    # el costo del retraso en caja minima
    _, r_min = resumen("(verif.) base", base)
    assert abs(r_min - b_min) < 1e-12
    print(f"Costo del retraso en financiamiento adicional = {(-min(itertools.accumulate(retr)) - (-b_min)):.2f} M USD")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
