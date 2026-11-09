#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C16: lazo de control de optica adaptativa con integrador y retardo, rechazo de perturbaciones y propagacion de ruido.

Datos: frecuencia de muestreo de 1000 Hz, retardo de D = 2 trames, ganancias 0,3 / 0,5 / 0,9 y el ruido blanco unitario son ILUSTRATIVOS ; semilla 20261109. No es un lazo real.
Modelo: u[n] = u[n-1] + g e[n-D], e[n] = d[n] - u[n] (+ ruido de medicion). En z: funcion de rechazo H_r(z) = (1 - z^-1)/(1 - z^-1 + g z^-D) y de ruido H_n(z) = g z^-D/(1 - z^-1 + g z^-D)
(con signo ; el modulo importa). Vias independientes: (a) simulacion temporal con perturbacion senoidal y el modulo de H_r(exp(j w)) ; (b) varianza de salida por simulacion con ruido blanco frente a
la integral en frecuencia (1/pi) int_0^pi |H_n|^2 dw ; (c) estabilidad: polos de z^D - z^(D-1) + g = 0 por simulacion de crecimiento y por la regla |z| < 1 (para D = 2: g < 1).
Supuestos: sistema lineal e invariante, un modo (un actuador), sin saturacion ni cuantizacion. Validez: ilustrativa de los conceptos de ancho de banda y margen de ganancia.
Tolerancia: amplitud simulada frente a |H_r| a 1 % ; varianza simulada del ruido frente a la integral a 3 % ; estabilidad coherente con el criterio de polos.
"""
from __future__ import annotations
import cmath, math, platform, random

FS = 1000.0
D = 2

def hr(f, g, d=D):
    z = cmath.exp(2j * math.pi * f / FS)
    zi = 1 / z
    return (1 - zi) / (1 - zi + g * zi ** d)

def hn(f, g, d=D):
    z = cmath.exp(2j * math.pi * f / FS)
    zi = 1 / z
    return g * zi ** d / (1 - zi + g * zi ** d)

def simular(g, dist, ruido=None, d=D):
    n = len(dist)
    u = [0.0] * n
    e = [0.0] * n
    for k in range(n):
        up = u[k - 1] if k > 0 else 0.0
        ek = e[k - d] if k - d >= 0 else 0.0
        u[k] = up + g * ek
        e[k] = dist[k] - u[k]
        if ruido is not None:
            e[k] += ruido[k]    # el ruido entra en la medicion (lo que ve el controlador)
    return u, e

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    print(f"{'g':>4} {'f [Hz]':>7} {'|H_r| simulado':>15} {'|H_r| analitico':>16}")
    for g in (0.3, 0.5, 0.9):
        for f in (5.0, 20.0, 50.0, 100.0):
            n = 6000
            dist = [math.sin(2 * math.pi * f * k / FS) for k in range(n)]
            u, e = simular(g, dist)
            # amplitud del residuo real (sin ruido): e = d - u
            res = [dist[k] - u[k] for k in range(n)]
            tail = res[n // 2:]
            # amplitud por proyeccion
            a = 2 * math.sqrt((sum(r * math.sin(2 * math.pi * f * (k + n // 2) / FS) for k, r in enumerate(tail)) / len(tail)) ** 2 + (sum(r * math.cos(2 * math.pi * f * (k + n // 2) / FS) for k, r in enumerate(tail)) / len(tail)) ** 2)
            teo = abs(hr(f, g))
            print(f"{g:4.1f} {f:7.1f} {a:15.5f} {teo:16.5f}")
            assert abs(a - teo) < 0.01 * max(teo, 0.1), (g, f, a, teo)
    # ancho de banda de rechazo (|H_r| = 1)
    print(f"{'g':>4} {'f_0dB [Hz]':>11} {'ganancia de pico |H_r|':>23}")
    for g in (0.3, 0.5, 0.9):
        f0 = None
        pico = 0.0
        for k in range(1, 5000):
            f = k * 0.1
            m = abs(hr(f, g))
            pico = max(pico, m)
            if f0 is None and m >= 1.0:
                f0 = f
        print(f"{g:4.1f} {f0:11.1f} {pico:23.3f}")
        assert pico > 1.0       # el efecto cama de agua: por encima de f0 el lazo amplifica
    # ruido: varianza de salida por simulacion frente a la integral
    print(f"{'g':>4} {'var u simulada':>15} {'(1/pi) int |H_n|^2':>20}")
    for g in (0.3, 0.5, 0.9):
        n = 200000
        r = [rnd.gauss(0, 1) for _ in range(n)]
        u, e = simular(g, [0.0] * n, ruido=r)
        var = sum(x * x for x in u[1000:]) / (n - 1000)
        integ = sum(abs(hn(0.5 * FS * (k + 0.5) / 4000, g)) ** 2 for k in range(4000)) / 4000
        print(f"{g:4.1f} {var:15.5f} {integ:20.5f}")
        assert abs(var / integ - 1) < 0.03, (g, var, integ)
    # el caso D = 1 tiene forma cerrada g/(2-g)
    g = 0.5
    integ1 = sum(abs(hn(0.5 * FS * (k + 0.5) / 4000, g, 1)) ** 2 for k in range(4000)) / 4000
    print(f"D = 1, g = 0,5: integral = {integ1:.6f} ; forma cerrada g/(2-g) = {g / (2 - g):.6f}")
    assert abs(integ1 - g / (2 - g)) < 1e-4
    # estabilidad con D = 2
    print(f"{'g':>5} {'max |z| polos':>14} {'crecimiento simulado':>21}")
    for g in (0.9, 0.99, 1.05, 1.3):
        disc = cmath.sqrt(1 - 4 * g)
        polos = [(1 + disc) / 2, (1 - disc) / 2]
        mz = max(abs(p) for p in polos)
        dist = [1.0 if k == 100 else 0.0 for k in range(3000)]
        u, e = simular(g, dist)
        amp = max(abs(x) for x in u[2500:])
        print(f"{g:5.2f} {mz:14.4f} {amp:21.3e}")
        if g < 1:
            assert mz < 1 and amp < 1e-2
        else:
            assert mz >= 1 - 1e-12 and amp > 1e-2
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
