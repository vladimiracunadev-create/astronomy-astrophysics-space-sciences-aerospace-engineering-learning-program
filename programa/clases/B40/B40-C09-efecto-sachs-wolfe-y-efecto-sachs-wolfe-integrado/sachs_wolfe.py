#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C09: meseta de Sachs-Wolfe y factor de crecimiento para el efecto Sachs-Wolfe integrado.

Datos: de Planck 2018 VI (arXiv:1807.06209, solo resumen, consultado el 2026-11-09): Omega_m = 0,315. T_0 = 2,7255 K (Fixsen 2009, solo resumen). Es ILUSTRATIVA la amplitud
A_s = 2,1e-9 (del orden de lo publicado, no leida en una fuente consultada). El articulo original de Sachs y Wolfe (1967) no se consulto: las relaciones usadas son las de un
tratamiento de libro de texto, no verificado contra el original.
Modelo: meseta SW para un espectro invariante de escala: abs(Delta T/T) = abs(R)/5 (abs(Phi) = 3 abs(R)/5 y abs(Delta T/T) = abs(Phi)/3; el signo depende de la convencion), C_l = 4 pi (A_s/25) integral de j_l(x)^2 dx/x = 2 pi A_s / (25 l (l+1)).
La integral se evalua numericamente con la funcion de Bessel esferica por recurrencia. El factor de crecimiento g = D/a se obtiene de la ecuacion diferencial de las perturbaciones y de
la integral de Heath, para Omega_m = 0,315 y Lambda plana (sin radiacion).
Supuestos: materia + Lambda, potencial constante en la era de materia, modo unico (ISW instantaneo, cota para las escalas mas grandes). Validez: ilustrativa.
Tolerancia: integral de j_l^2/x frente a 1/(2 l (l+1)) a 1e-4 ; las dos vias de g a 1e-4 (la ecuacion diferencial parte de a = 1e-3 con D = a).
"""
from __future__ import annotations
import math, platform, sys

AS = 2.1e-9
T0_UK = 2.7255e6
OM = 0.315

def jl(l, x):
    if x < 1e-8:
        return 0.0
    if x >= l:
        a, b = math.sin(x) / x, (math.sin(x) / x - math.cos(x)) / x
        if l == 0:
            return a
        for k in range(1, l):
            a, b = b, (2 * k + 1) / x * b - a
        return b
    start = l + 30 + int(x)
    jp, jc = 0.0, 1e-300
    val = 0.0
    for k in range(start, 0, -1):
        jn = (2 * k + 1) / x * jc - jp
        jp, jc = jc, jn
        if abs(jc) > 1e250:
            jp *= 1e-250; jc *= 1e-250; val *= 1e-250
        if k - 1 == l:
            val = jc
    # jc corresponde a j_0 sin normalizar
    return val * (math.sin(x) / x) / jc

def integral(l, xmax=300.0, h=0.02):
    n = int(xmax / h)
    s = 0.0
    for i in range(1, n + 1):
        x = i * h
        f = jl(l, x) ** 2 / x
        s += f * (4 if i % 2 else 2)
    s -= (jl(l, xmax) ** 2 / xmax)         # el ultimo punto pesa 1, no 4/2
    s = s * h / 3
    return s + 1.0 / (4 * xmax ** 2)       # cola: j^2 ~ 1/(2 x^2)

def crecimiento_ode():
    # d2D/dN2 + (2 + dlnH/dN) dD/dN = 1.5 Om(a) D ; N = ln a ; Lambda plana, sin radiacion
    ol = 1 - OM
    def e2(a): return OM / a ** 3 + ol
    def f(N, D, Dp):
        a = math.exp(N)
        dlnh = -1.5 * OM / a ** 3 / e2(a)
        om_a = OM / a ** 3 / e2(a)
        return Dp, -(2 + dlnh) * Dp + 1.5 * om_a * D
    N = math.log(1e-3); D = 1e-3; Dp = 1e-3
    h = 1e-4
    while N < -h / 2:
        k1 = f(N, D, Dp)
        k2 = f(N + h / 2, D + h / 2 * k1[0], Dp + h / 2 * k1[1])
        k3 = f(N + h / 2, D + h / 2 * k2[0], Dp + h / 2 * k2[1])
        k4 = f(N + h, D + h * k3[0], Dp + h * k3[1])
        D += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); Dp += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        N += h
    return D

def crecimiento_heath():
    ol = 1 - OM
    def e(a): return math.sqrt(OM / a ** 3 + ol)
    n = 200000
    h = 1.0 / n
    s = 0.0
    for i in range(1, n):
        a = i * h
        s += (4 if i % 2 else 2) / (a * e(a)) ** 3 if a > 0 else 0
    s += 1.0 / e(1.0) ** 3
    s *= h / 3
    # el integrando ~ a^(3/2) cerca de 0: la regla de Simpson es suficiente
    return 2.5 * OM * e(1.0) * s

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'l':>3} {'integral numerica de j_l^2/x':>29} {'1/(2 l (l+1))':>15} {'dif. relativa':>14} {'l(l+1)C_l/2pi [uK^2]':>22}")
    for l in (2, 10, 30):
        i = integral(l)
        teo = 1 / (2 * l * (l + 1))
        cl = 4 * math.pi * AS / 25 * i
        dl = l * (l + 1) * cl / (2 * math.pi) * T0_UK ** 2
        print(f"{l:3d} {i:29.8e} {teo:15.8e} {(i / teo - 1):14.2e} {dl:22.2f}")
        assert abs(i / teo - 1) < 1e-4
    plateau = AS / 25 * T0_UK ** 2
    print(f"meseta A_s/25 * T_0^2 = {plateau:.2f} uK^2 (A_s ilustrativa)")
    g1 = crecimiento_ode(); g2 = crecimiento_heath()
    print(f"factor de crecimiento g = D/a hoy: ecuacion diferencial = {g1:.6f} ; integral de Heath = {g2:.6f} ; diferencia = {g1 - g2:+.1e}")
    assert abs(g1 - g2) < 1e-4
    print(f"cociente ISW/SW instantaneo (cota) = 6 (g - 1) = {6 * (g1 - 1):+.3f} (signo opuesto: el decaimiento calienta lo que SW enfria)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
