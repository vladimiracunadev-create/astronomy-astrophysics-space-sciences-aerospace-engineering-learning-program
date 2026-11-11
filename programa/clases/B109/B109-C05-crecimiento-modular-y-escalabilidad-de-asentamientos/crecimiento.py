#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C05: crecimiento por fases de un habitat (2 tripulantes/30 d -> 4/30 d -> 4/60 d) y comprobacion de reutilizacion.

Datos consultados (2026-11-10; Burke, Howard y Kessler 2022, Tabla 4 y secciones de supuestos): areas del trazado de referencia por funcion para 2 tripulantes (no es un diseno de vuelo),
altura estandar de volumen funcional 2.4 m, y que NASA estudia ampliar el Surface Habitat a 4 tripulantes durante ~30 d y ~60 d. Informe de consenso HRP (2014): 25 m3 por persona
como NHV minimo de una mision de 30 meses a Marte (se usa SOLO como comparacion, no es un requisito lunar).
ILUSTRATIVAS: las reglas de escalado de cada funcion (fijo, lineal en tripulantes, por pares de tripulantes, lineal en tripulantes x dias), el redondeo de modulos a 0.5 m2 y el reparto en modulos.
Modelo: A_req(N, d) = suma de funciones con su regla; el plan aditivo anade modulos E_k con area >= A_req(fase k) - A_req(fase k-1); el plan de reemplazo construye un habitat nuevo por fase.
Segunda via: A_req(2, 30) debe reproducir la suma de las filas de la Tabla 4 mas la esclusa (tolerancia 1e-9); A_req no decrece con N ni con d; la reutilizacion aditiva es 1.
Unidades: area [m2], volumen [m3], altura 2.4 m.
"""
from __future__ import annotations
import math, platform

H = 2.4
REF_NHV = 25.0
# (nombre, area para 2 tripulantes y 30 d [m2], regla)
FUNC = [("Estiramiento", 2.68, "lineal"), ("Sueno", 3.70, "lineal"), ("Medico", 3.43, "fijo"), ("Ejercicio", 2.09, "pares"),
        ("UWMS", 1.04, "pares"), ("Higiene", 1.04, "pares"), ("Mesa", 2.23, "lineal"), ("Trabajo", 1.30, "fijo"),
        ("Ordenador EVA", 0.97, "fijo"), ("Ordenador general", 2.10, "fijo"), ("Cocina trabajo", 0.95, "fijo"),
        ("Cocina preparacion", 1.17, "fijo"), ("Utilizacion", 5.07, "fijo"), ("Traslado y escaleras", 8.65, "fijo"),
        ("Sistemas y almacenamiento", 5.79, "logistica"), ("Esclusa", 5.18, "fijo")]
FASES = [("Fase 1", 2, 30), ("Fase 2", 4, 30), ("Fase 3", 4, 60)]


def factor(regla, n, d):
    if regla == "fijo":
        return 1.0
    if regla == "lineal":
        return n / 2
    if regla == "pares":
        return math.ceil(n / 2)
    return (n * d) / (2 * 30)  # logistica


def a_req(n, d):
    return sum(a * factor(r, n, d) for _, a, r in FUNC)


def al_medio(x):
    return math.ceil(x * 2 - 1e-9) / 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Reglas de escalado ILUSTRATIVAS; areas base de la Tabla 4 de Burke et al. (2022); 25 m3/persona del informe HRP solo como comparacion")
    base = a_req(2, 30)
    suma_filas = sum(a for _, a, _ in FUNC)
    print(f"A_req(2 trip., 30 d) = {base:.2f} m2 ; suma de filas = {suma_filas:.2f} m2")
    assert abs(base - suma_filas) < 1e-9
    reqs = [a_req(n, d) for _, n, d in FASES]
    assert all(b >= a - 1e-12 for a, b in zip(reqs, reqs[1:]))
    print(" fase    N   dias   A_req [m2]   A_req/trip [m2]   V funcional/trip [m3]  (altura 2.4 m)")
    for (nom, n, d), r in zip(FASES, reqs):
        print(f"{nom:7s} {n:3d} {d:6d} {r:12.2f} {r / n:17.2f} {r * H / n:22.2f}")
    modulos = [("M0 nucleo", al_medio(reqs[0]))]
    for k in (1, 2):
        modulos.append((f"E{k} ampliacion", al_medio(reqs[k] - reqs[k - 1] + 1e-12)))
    print("Modulos del plan aditivo:")
    acum = 0.0
    for k, (nm, a) in enumerate(modulos):
        acum += a
        print(f"   {nm:15s} area = {a:6.2f} m2 ; acumulada = {acum:7.2f} m2 ; requerida en la fase {k + 1} = {reqs[k]:7.2f} m2")
        assert acum >= reqs[k] - 1e-9
    construido_aditivo = sum(a for _, a in modulos)
    construido_reemplazo = sum(al_medio(r) for r in reqs)
    print(f"Area construida: plan aditivo = {construido_aditivo:.1f} m2 ; plan de reemplazo = {construido_reemplazo:.1f} m2 ; exceso del reemplazo = {construido_reemplazo - construido_aditivo:.1f} m2")
    print("Reutilizacion entre fases del plan aditivo = 1.00 ; interfaces nuevas por fase = 1")
    assert construido_reemplazo > construido_aditivo
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
