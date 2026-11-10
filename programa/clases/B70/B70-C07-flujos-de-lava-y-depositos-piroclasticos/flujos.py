#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C07: caudal de un flujo de lava (newtoniano y de Bingham) y alcance de clastos piroclásticos.

Datos: gravedades NASA/NSSDC (consultada 2026-11-09): Luna 1,62, Marte 3,73, Venus 8,87; Tierra 9,80665 m/s^2 (valor normal).
Densidad de la lava (2600 kg/m^3), viscosidad (1000 Pa s), resistencia a la fluencia (2000 Pa), espesor (3 m), pendiente (3 grados), velocidad de
eyeccion (100 m/s), angulo (45 grados), diametro y densidad del clasto, coeficiente de arrastre (1) y densidad del aire: ILUSTRATIVOS (sinteticos).
Modelo: (1) capa sobre una pendiente theta: esfuerzo tau(y) = rho g sin(theta) (h - y). Newtoniano: q = G h^3 /(3 eta), G = rho g sin(theta).
Bingham: h_c = tau_y/G; zona deformada 0 <= y <= h - h_c; q = (G h^3/(3 eta)) (1 - 1,5 xi + 0,5 xi^3), xi = h_c/h (derivado en la clase; el flujo
se detiene si h <= h_c). Ambos se comparan con la integral numerica del perfil de velocidad. (2) Alcance balistico en el vacio R = v^2 sin(2 alpha)/g
frente a RK4; con resistencia cuadratica m dv/dt = -0,5 rho_a Cd A |v| v, que se reduce al caso del vacio cuando rho_a -> 0.
Supuestos: flujo laminar estacionario uniforme, isotermo, sin cambios de reologia; clasto esferico, suelo plano, sin viento. Validez: ilustrativa.
Tolerancia: 1e-9 relativo en el caudal; 1e-4 en el alcance; 1e-6 al tender rho_a a 0.
"""
from __future__ import annotations
import math, platform

RHO, ETA, TAUY = 2600.0, 1000.0, 2000.0
H, THETA = 3.0, math.radians(3.0)
G_TAB = {"Luna": 1.62, "Marte": 3.73, "Venus": 8.87, "Tierra": 9.80665}

def simpson(f, a, b, n=4000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

def caudal_newtoniano(g, h=H):
    G = RHO * g * math.sin(THETA)
    q = G * h**3 / (3 * ETA)
    # perfil u(y) = G (h y - y^2/2)/eta
    qn = simpson(lambda y: G * (h * y - y * y / 2) / ETA, 0.0, h)
    return q, qn

def caudal_bingham(g, h=H):
    G = RHO * g * math.sin(THETA)
    hc = TAUY / G
    if h <= hc:
        return 0.0, 0.0, hc
    xi = hc / h
    q = G * h**3 / (3 * ETA) * (1 - 1.5 * xi + 0.5 * xi**3)
    yd = h - hc   # espesor de la zona deformada
    def u(y):
        y = min(y, yd)
        return (G * (h * y - y * y / 2) - TAUY * y) / ETA
    qn = simpson(u, 0.0, h, n=8000)
    return q, qn, hc

def alcance_rk4(v0, ang, g, rho_a=0.0, d=0.2, rho_p=2500.0, cd=1.0, dt=1e-3):
    m = rho_p * math.pi * d**3 / 6
    A = math.pi * d**2 / 4
    k = 0.5 * rho_a * cd * A / m
    x, y = 0.0, 0.0
    vx, vy = v0 * math.cos(ang), v0 * math.sin(ang)
    def der(vx, vy):
        v = math.hypot(vx, vy)
        return -k * v * vx, -g - k * v * vy
    while True:
        a1x, a1y = der(vx, vy)
        a2x, a2y = der(vx + dt * a1x / 2, vy + dt * a1y / 2)
        a3x, a3y = der(vx + dt * a2x / 2, vy + dt * a2y / 2)
        a4x, a4y = der(vx + dt * a3x, vy + dt * a3y)
        nvx = vx + dt * (a1x + 2 * a2x + 2 * a3x + a4x) / 6
        nvy = vy + dt * (a1y + 2 * a2y + 2 * a3y + a4y) / 6
        nx = x + dt * (vx + nvx) / 2
        ny = y + dt * (vy + nvy) / 2
        if ny < 0:
            return x + (nx - x) * y / (y - ny)
        x, y, vx, vy = nx, ny, nvx, nvy

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    print(f"Capa de {H} m en {math.degrees(THETA):.0f} grados (rho = {RHO:.0f}, eta = {ETA:.0f} Pa s, tau_y = {TAUY:.0f} Pa; ilustrativos)")
    for nombre, g in G_TAB.items():
        q, qn = caudal_newtoniano(g)
        assert abs(q - qn) / q < 1e-9
        qb, qbn, hc = caudal_bingham(g)
        assert abs(qb - qbn) / max(qb, 1e-30) < 1e-6, "caudal Bingham no coincide"
        print(f"  {nombre:7s} g = {g:7.5f}: newtoniano q = {q:7.3f} m^2/s (u media {q/H:6.3f} m/s) ; Bingham h_c = {hc:5.2f} m, q = {qb:7.3f} m^2/s")
    # a caudal fijo el espesor newtoniano escala como g^(-1/3)
    q0 = caudal_newtoniano(9.80665)[0]
    print("A caudal por unidad de ancho fijo (el de la Tierra), espesor newtoniano h = (3 eta q/(rho g sin))^(1/3):")
    for nombre, g in G_TAB.items():
        h = (3 * ETA * q0 / (RHO * g * math.sin(THETA))) ** (1 / 3)
        assert abs(h / H - (9.80665 / g) ** (1 / 3)) < 1e-9
        print(f"  {nombre:7s}: h = {h:5.2f} m ; velocidad media = {q0/h:6.3f} m/s")
    v0, ang = 100.0, math.radians(45.0)
    print(f"Alcance balistico de clastos (v0 = {v0:.0f} m/s, 45 grados, d = 0,2 m, rho_p = 2500; ilustrativos)")
    for nombre, g in G_TAB.items():
        ra = v0**2 * math.sin(2 * ang) / g
        rn = alcance_rk4(v0, ang, g)
        assert abs(ra - rn) / ra < 1e-4, "alcance RK4 no coincide"
        rd = alcance_rk4(v0, ang, g, rho_a=0.0165 if nombre == "Marte" else 0.0)
        print(f"  {nombre:7s}: vacio {ra:8.1f} m (RK4 {rn:8.1f}) ; Marte con aire ilustrativo 0,0165 kg/m^3: {rd:8.1f} m" if nombre == "Marte"
              else f"  {nombre:7s}: vacio {ra:8.1f} m (RK4 {rn:8.1f})")
    r0 = alcance_rk4(v0, ang, 9.80665, rho_a=1e-12)
    assert abs(r0 - v0**2 / 9.80665) / (v0**2 / 9.80665) < 1e-4
    print("Limite rho_a -> 0 (Tierra) superado.")
    r_aire = alcance_rk4(v0, ang, 9.80665, rho_a=1.2)
    print(f"Tierra con aire (rho_a = 1,2 kg/m^3, ilustrativo): alcance = {r_aire:.1f} m frente a {v0**2/9.80665:.1f} m en el vacio")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
