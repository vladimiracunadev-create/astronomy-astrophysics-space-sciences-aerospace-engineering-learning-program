#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B70-C06: criovulcanismo en un satélite tipo Encélado (sobrepresión y chorro de vapor).

Datos: masa de Encélado 1,08e20 kg y dimensiones 257 x 251 x 248 km (hoja de datos de satelites de Saturno NASA/NSSDC, consultada 2026-11-09);
la hoja NO lista gravedad ni velocidad de escape: se calculan aqui con G = 6,67430e-11 m^3 kg^-1 s^-2 (CODATA 2022, valor recordado, no consultado en linea).
R gas universal 8,314462618 J/(mol K) (SI definido). Densidad del agua liquida (1000 kg/m^3) y del hielo (917 kg/m^3), espesor de la capa (5 km),
temperatura del vapor (273,15 K) y exponente adiabatico (1,33): ILUSTRATIVOS. No se reproduce ninguna medida de la mision Cassini.
Modelo: (1) sobrepresion necesaria para que el agua suba por una fractura de altura h en hielo: DeltaP = (rho_w - rho_i) g h (con g media a la superficie).
(2) Velocidad de escape v_esc = sqrt(2 G M / R) frente a integracion numerica de la energia. (3) Velocidad de salida de un chorro de vapor estrangulado
(Mach 1): v* = sqrt(2 gamma/(gamma+1) R T0/M) frente a sqrt(gamma R T*/M) con T* = 2 T0/(gamma+1). (4) Altura maxima de un grano balistico sin
resistencia: r_max = 1/(1/R - v^2/(2 G M)) frente a integracion Runge-Kutta 4 de la trayectoria radial.
Supuestos: cuerpo esferico homogeneo (radio medio), gas ideal, flujo isentropico, sin resistencia, sin rotacion. Validez: ilustrativa.
Tolerancia: 1e-6 relativo en la escape y en la altura; 1e-12 en el chorro.
"""
from __future__ import annotations
import math, platform

G, RG = 6.67430e-11, 8.314462618
M = 1.08e20
R = (257e3 + 251e3 + 248e3) / 3.0
MH2O = 0.018015   # kg/mol

def rk4_radial(v0, t_max=4.0e5, dt=0.5):
    r, v, t, rmax = R, v0, 0.0, R
    acc = lambda r: -G * M / r**2
    while t < t_max and v > 0:
        k1r, k1v = v, acc(r)
        k2r, k2v = v + dt * k1v / 2, acc(r + dt * k1r / 2)
        k3r, k3v = v + dt * k2v / 2, acc(r + dt * k2r / 2)
        k4r, k4v = v + dt * k3v, acc(r + dt * k3r)
        r += dt * (k1r + 2 * k2r + 2 * k3r + k4r) / 6
        v += dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        t += dt
        rmax = max(rmax, r)
    return rmax

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    g = G * M / R**2
    vesc = math.sqrt(2 * G * M / R)
    # escape por integracion de la energia: int_R^inf G M / r^2 dr = G M / R (cambio u = R/r)
    # trabajo contra la gravedad de R a R e^30: r = R e^t, dr = r dt (Simpson)
    n = 6000
    hh = 30.0 / n
    f = lambda t: G * M / (R * math.exp(t))
    s = (f(0.0) + f(30.0) + sum((4 if i % 2 else 2) * f(i * hh) for i in range(1, n))) * hh / 3
    assert abs(math.sqrt(2 * s) - vesc) / vesc < 1e-6
    print(f"R medio = {R/1e3:.1f} km ; g = {g:.4f} m/s^2 ; v_esc = {vesc:.1f} m/s (calculados, no listados por la hoja)")
    rho_w, rho_i, h = 1000.0, 917.0, 5.0e3
    dp = (rho_w - rho_i) * g * h
    print(f"Sobrepresion para subir agua por {h/1e3:.0f} km de hielo: DeltaP = {dp/1e3:.1f} kPa (densidades ilustrativas)")
    print("   Con la gravedad de la Luna y h = 5 km: DeltaP = {:.1f} kPa (solo para comparar escalas)".format((rho_w - rho_i) * 1.62 * h / 1e3))
    gam, T0 = 1.33, 273.15
    v1 = math.sqrt(2 * gam / (gam + 1) * RG * T0 / MH2O)
    Tstar = 2 * T0 / (gam + 1)
    v2 = math.sqrt(gam * RG * Tstar / MH2O)
    assert abs(v1 - v2) / v1 < 1e-12
    print(f"Chorro de vapor estrangulado (T0 = {T0} K, gamma = {gam}): T* = {Tstar:.1f} K ; v* = {v1:.1f} m/s ; v*/v_esc = {v1/vesc:.2f}")
    print("Altura maxima de un grano (sin resistencia) segun la velocidad inicial:")
    for v0 in (60.0, 120.0, 200.0, 230.0):
        ra = 1.0 / (1.0 / R - v0**2 / (2 * G * M))
        rn = rk4_radial(v0)
        assert abs(ra - rn) / ra < 1e-6, "altura RK4 no coincide"
        print(f"  v0 = {v0:6.1f} m/s: altura = {(ra-R)/1e3:8.3f} km (RK4 {(rn-R)/1e3:8.3f}) ; v0^2/(2g) = {v0*v0/(2*g)/1e3:8.3f} km")
    print(f"El vapor estrangulado ({v1:.0f} m/s) supera v_esc ({vesc:.0f} m/s): el modelo ideal predice que un grano acoplado al gas puede escapar.")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
