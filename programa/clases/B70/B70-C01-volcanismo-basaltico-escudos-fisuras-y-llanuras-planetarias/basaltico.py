#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C01: volumen de un escudo y flujo en una fisura basaltica.

Datos: gravedades superficiales medias de la hoja de datos NASA/NSSDC (consultada 2026-11-09): Luna 1,62, Marte 3,73, Venus 8,87 m/s^2;
Tierra 9,80665 m/s^2 (gravedad normal, valor definido). Dimensiones del escudo, viscosidad, contraste de densidad y ancho de fisura:
ILUSTRATIVOS (sinteticos); no representan ningun volcan real.
Modelo: (1) escudo axisimetrico con perfil h(r) = H (1 - r/R)^p; volumen analitico V = 2 pi H R^2 / ((p+1)(p+2)) frente a integral numerica
(regla de Simpson). (2) Fisura como rendija de ancho w con gradiente de presion G = drho*g; flujo por unidad de longitud q = G w^3/(12 eta)
frente a integral numerica del perfil parabolico u(y) = G (w^2/4 - y^2)/(2 eta).
Supuestos: fluido newtoniano, laminar, isotermo, rendija infinita; escudo con simetria perfecta. Validez: ilustrativa.
Tolerancia: 1e-6 relativo en volumen y 1e-9 relativo en el caudal de la rendija.
"""
from __future__ import annotations
import math, platform

H, R = 8.0e3, 150.0e3          # m (ilustrativos)
ETA, DRHO, W = 100.0, 200.0, 1.0   # Pa s, kg/m^3, m (ilustrativos)
G_TAB = {"Luna": 1.62, "Marte": 3.73, "Venus": 8.87, "Tierra": 9.80665}

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def volumen_escudo(p):
    analitico = 2 * math.pi * H * R**2 / ((p + 1) * (p + 2))
    numerico = simpson(lambda r: 2 * math.pi * r * H * (1 - r / R) ** p, 0.0, R)
    return analitico, numerico

def q_rendija(g):
    G = DRHO * g
    analitico = G * W**3 / (12 * ETA)
    u = lambda y: G * (W**2 / 4 - y * y) / (2 * ETA)
    numerico = simpson(u, -W / 2, W / 2)
    return analitico, numerico

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print("Escudo (H = 8 km, R = 150 km, ilustrativos): volumen por exponente del perfil")
    for p in (1.0, 2.0, 3.0):
        a, n = volumen_escudo(p)
        assert abs(a - n) / a < 1e-6, "volumen numerico no coincide"
        print(f"  p = {p:.0f}: V analitico = {a/1e9:10.1f} km^3 ; numerico = {n/1e9:10.1f} km^3 ; V/V(cono) = {a/(math.pi*H*R*R/3):.3f}")
    print("Fisura (w = 1 m, eta = 100 Pa s, drho = 200 kg/m^3, ilustrativos): flujo por metro de fisura")
    q_t = None
    for nombre, g in G_TAB.items():
        a, n = q_rendija(g)
        assert abs(a - n) / a < 1e-9, "caudal de rendija no coincide"
        if nombre == "Tierra":
            q_t = a
        print(f"  {nombre:7s} g = {g:7.5f} m/s^2: q = {a*1e3:8.3f} L/s por metro ; numerico = {n*1e3:8.3f}")
    # a caudal fijo, el ancho escala como g^(-1/3)
    q0 = q_t
    print("Ancho necesario para el caudal terrestre (q fijo): w = (12 eta q / (drho g))^(1/3)")
    for nombre, g in G_TAB.items():
        w = (12 * ETA * q0 / (DRHO * g)) ** (1 / 3)
        print(f"  {nombre:7s}: w = {w:.3f} m ; w/w(Tierra) = {w/W:.3f} ; (g_T/g)^(1/3) = {(9.80665/g)**(1/3):.3f}")
        assert abs(w / W - (9.80665 / g) ** (1 / 3)) < 1e-9
    # tiempo para emitir 1 km^3 por una fisura de 10 km
    V, L = 1e9, 10e3
    print("Tiempo para emitir 1 km^3 por una fisura de 10 km con w = 1 m (flujo de rendija):")
    for nombre, g in G_TAB.items():
        a, _ = q_rendija(g)
        t = V / (a * L)
        print(f"  {nombre:7s}: {t/86400:8.2f} dias")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
