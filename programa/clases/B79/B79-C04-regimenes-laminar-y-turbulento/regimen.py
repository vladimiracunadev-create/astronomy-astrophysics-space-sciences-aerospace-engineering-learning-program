#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C04: regimen laminar y turbulento - Reynolds en tubo y arrastre de una placa plana.

Consultado (2026-11-10): NASA Glenn, Re = rho V L / mu = V L / nu (la pagina no trata laminar/turbulento).
ILUSTRATIVOS (sinteticos, no medidos): aire con rho = 1.2 kg/m3 y mu = 1.8e-5 Pa s (valores de uso comun, no consultados);
agua rho = 1000, mu = 1.0e-3; tubo D = 0.05 m; placa de L = 1.0 m, ancho 1.0 m, velocidad 5 y 50 m/s.
Correlaciones ESTANDAR (no consultadas): tubo f = 64/Re (laminar), Blasius f = 0.316 Re^-0.25 (turbulento liso, Re < 1e5);
placa (Re_L < 5e5 laminar; si no, turbulenta de capa completa, sin correccion de transicion): Cf = 1.328/sqrt(Re_L) (laminar de Blasius), Cf = 0.074 Re_L^-0.2 (turbulento); transicion en Re_x = 5e5 (convencional).
Segunda via: integracion numerica de la tension local sobre la placa (Cf_x = 0.664/sqrt(Re_x)) frente a la formula cerrada.
Tolerancias: integral numerica frente a cerrada < 1e-4 relativa.
"""
import math, platform

RE_CRIT_TUBO, RE_CRIT_PLACA = 2300.0, 5e5


def re(rho, v, l, mu):
    return rho * v * l / mu


def f_tubo(r):
    return 64.0 / r if r < RE_CRIT_TUBO else 0.316 * r ** -0.25


def arrastre_laminar_numerico(rho, v, l, mu, w, n=20000):
    """Integra tau_x = 0.5 rho v^2 * 0.664 / sqrt(Re_x) sobre x en (0, L] por punto medio."""
    suma = 0.0
    ds = 1.0 / n  # cambio de variable x = L s^2 para tratar la singularidad en x = 0
    for i in range(n):
        s = (i + 0.5) * ds
        x = l * s * s
        rex = re(rho, v, x, mu)
        suma += 0.5 * rho * v * v * 0.664 / math.sqrt(rex) * 2.0 * l * s * ds
    return suma * w


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Tubo ILUSTRATIVO D = 0.05 m")
    print(" fluido   V [m/s]     Re      regimen     f (Darcy)")
    for nombre, rho, mu, v in (("agua", 1000.0, 1.0e-3, 0.02), ("agua", 1000.0, 1.0e-3, 1.0), ("aire", 1.2, 1.8e-5, 5.0), ("aire", 1.2, 1.8e-5, 0.5)):
        r = re(rho, v, 0.05, mu)
        reg = "laminar" if r < RE_CRIT_TUBO else "turbulento"
        print(f" {nombre:5s}  {v:7.3f}  {r:9.1f}  {reg:10s}  {f_tubo(r):.5f}")
    # continuidad de la formula en el cruce (no es continua: se muestra el salto)
    print(f" salto de f en Re = 2300: laminar {64 / 2300:.5f} ; Blasius {0.316 * 2300 ** -0.25:.5f}")
    print("Placa plana ILUSTRATIVA L = 1 m, ancho 1 m, aire")
    print("  V [m/s]    Re_L      regimen    Cf        arrastre D [N]")
    rho, mu, l, w = 1.2, 1.8e-5, 1.0, 1.0
    for v in (5.0, 50.0):
        rl = re(rho, v, l, mu)
        if rl < RE_CRIT_PLACA:
            cf, reg = 1.328 / math.sqrt(rl), "laminar"
        else:
            cf, reg = 0.074 * rl ** -0.2, "turbulento"
        d = 0.5 * rho * v * v * l * w * cf
        print(f"  {v:6.1f}  {rl:10.0f}   {reg:10s} {cf:.5f}   {d:.5f}")
    v = 5.0
    rl = re(rho, v, l, mu)
    d_cerr = 0.5 * rho * v * v * l * w * 1.328 / math.sqrt(rl)
    d_num = arrastre_laminar_numerico(rho, v, l, mu, w)
    dif = abs(d_num - d_cerr) / d_cerr
    print(f"Arrastre laminar a 5 m/s: cerrada = {d_cerr:.6f} N ; integral numerica = {d_num:.6f} N ; diferencia = {dif:.2e}")
    # longitud de transicion a 10 m/s
    xt = RE_CRIT_PLACA * mu / (rho * 5.0)
    print(f"Longitud de transicion (Re_x = 5e5) a 5 m/s: x = {xt:.3f} m ; a 50 m/s: x = {RE_CRIT_PLACA * mu / (rho * 50.0):.3f} m")
    # arrastre turbulento vs laminar al mismo Re (cociente)
    r2 = 2.0e6
    print(f"A Re_L = 2e6: Cf turbulento / Cf laminar = {0.074 * r2 ** -0.2 / (1.328 / math.sqrt(r2)):.2f}")
    assert dif < 1e-4
    assert abs(re(1000.0, 1.0, 0.05, 1.0e-3) - 50000.0) < 1e-9
    print("Pruebas superadas.")


main()
