#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C01: conversion de un SAFE SINTETICO y dilucion de fundadores.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion; no reemplaza a un abogado ni a un contador.
Consultado (2026-11-11): la pagina de documentos SAFE de Y Combinator (tipos con tope de valoracion, con descuento y MFN;
el tope post-money cuenta el dinero de los SAFE; la conversion es automatica en una ronda con acciones preferentes;
el precio de conversion lo fija el tope o el descuento). El texto legal completo del SAFE NO se leyo.
ILUSTRATIVOS (sinteticos): la empresa, 9 000 000 acciones previas, el SAFE de 500 000 USD con tope post-money de 5 000 000 USD
y descuento de 20 %, la ronda de 3 000 000 USD y las tres valoraciones pre-money (4, 8 y 20 millones de USD).
Modelo simplificado: un solo SAFE, sin aumento del fondo de opciones en la ronda, sin intereses ni costos legales.
Formulas: acciones por tope  s_cap = C*inv/(cap - inv); acciones por descuento  s_desc = inv*C/((1-d)*V - inv)
(V = pre-money que incluye las acciones del SAFE); el SAFE recibe max(s_cap, s_desc).
Unidades: acciones, USD. Tolerancias: segunda via por iteracion de punto fijo (error < 1e-6 acciones); suma de porcentajes = 100 % (1e-9).
"""
from __future__ import annotations
import platform

C = 9_000_000          # acciones previas (fundadores + opciones), sinteticas
INV, CAP, DESC = 500_000.0, 5_000_000.0, 0.20
RONDA = 3_000_000.0
FUND, POOL = 8_000_000, 1_000_000


def convierte(V):
    s_cap = C * INV / (CAP - INV)
    s_desc = INV * C / ((1 - DESC) * V - INV)
    s = max(s_cap, s_desc)
    precio = V / (C + s)                       # precio de la ronda
    return s_cap, s_desc, s, precio


def punto_fijo(V):
    """Segunda via: itera s -> INV/(min(precio_cap, precio_desc)) con precio = V/(C+s)."""
    s = 1.0
    for _ in range(2000):
        precio = V / (C + s)
        p_conv = min(CAP / (C + s), (1 - DESC) * precio)
        s_nuevo = INV / p_conv
        if abs(s_nuevo - s) < 1e-9:
            break
        s = s_nuevo
    return s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); solo la mecanica general del SAFE esta consultada (pagina de Y Combinator, 2026-11-11).")
    print(f"SAFE {INV:,.0f} USD, tope post-money {CAP:,.0f} USD, descuento {DESC:.0%}; ronda {RONDA:,.0f} USD; acciones previas {C:,}")
    print(f"Propiedad del SAFE al tope (antes de la ronda) = INV/CAP = {INV/CAP:.2%}")
    print(" pre-money   usa      acc_SAFE    precio_ronda  acc_nuevas   fund_%   SAFE_%   nuevos_%   pool_%")
    maxerr = 0.0
    for V in (4_000_000.0, 8_000_000.0, 20_000_000.0):
        s_cap, s_desc, s, precio = convierte(V)
        s2 = punto_fijo(V)
        maxerr = max(maxerr, abs(s - s2))
        nuevas = RONDA / precio
        total = C + s + nuevas
        pct = [FUND / total, s / total, nuevas / total, POOL / total]
        assert abs(sum(pct) - 1) < 1e-9
        usa = "tope" if s_cap >= s_desc else "descuento"
        print(f" {V/1e6:6.1f} M   {usa:<9} {s:10,.0f}   {precio:8.4f}   {nuevas:10,.0f}   {pct[0]*100:6.2f}   {pct[1]*100:6.2f}   {pct[2]*100:7.2f}   {pct[3]*100:6.2f}")
    s_cap = C * INV / (CAP - INV)
    assert abs(s_cap / (C + s_cap) - INV / CAP) < 1e-12
    print(f"Comprobacion: s_cap/(C+s_cap) = {s_cap/(C+s_cap):.6f} = INV/CAP = {INV/CAP:.6f}")
    print(f"Error maximo entre formula cerrada y punto fijo = {maxerr:.2e} acciones")
    assert maxerr < 1e-6
    # valoracion de cruce: tope y descuento convierten igual
    # s_desc = s_cap  ->  V* = (INV*C/s_cap + INV)/(1-DESC)
    Vx = (INV * C / s_cap + INV) / (1 - DESC)
    print(f"Valoracion pre-money de cruce (tope = descuento) = {Vx:,.0f} USD")
    _, a, b, _ = convierte(Vx)
    assert abs(a - b) < 1e-6 * a
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
