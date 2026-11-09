#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C06: campo escalar oscilante en potenciales V = phi^n / n, ecuacion de estado media y dilucion.

Datos: ninguna constante fisica ni dato observado. Los potenciales, las amplitudes y el fondo de materia prescrito (a proporcional a t^(2/3)) son ILUSTRATIVOS. Unidades adimensionales (m = 1).
Modelo: phi'' + 3 H phi' + V'(phi) = 0 con V = phi^n / n ; w = (K - V)/(K + V), K = phi'^2/2. Sin expansion (H = 0) el promedio temporal cumple el teorema del virial:
<w> = (n - 2)/(n + 2). Con H = 2/(3t) prescrito (el campo es una prueba, no gravita) la energia en los maximos de |phi| decae como a^(-6n/(n+2)).
Supuestos: campo de prueba, sin interaccion ni fragmentacion. Validez: ilustrativa.
Tolerancia: <w> frente al virial 2e-3 sobre un numero entero de periodos; pendiente de dilucion 2 %.
"""
from __future__ import annotations
import math, platform, sys

def vp(p, n):
    return math.copysign(abs(p) ** (n - 1), p)

def rk4(p, v, t, dt, n, expand):
    def f(p, v, t):
        h = 2.0 / (3.0 * t) if expand else 0.0
        return v, -3 * h * v - vp(p, n)
    k1 = f(p, v, t)
    k2 = f(p + 0.5 * dt * k1[0], v + 0.5 * dt * k1[1], t + 0.5 * dt)
    k3 = f(p + 0.5 * dt * k2[0], v + 0.5 * dt * k2[1], t + 0.5 * dt)
    k4 = f(p + dt * k3[0], v + dt * k3[1], t + dt)
    return p + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), v + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])

def w_medio(n, phi0=1.0, dt=0.002):
    # media sobre un numero entero de periodos: 40 cruces por cero = 20 periodos
    p, v, t = phi0, 0.0, 1.0
    sk = sv = 0.0
    cruces = 0
    p_ant = p
    pasos = 0
    while cruces < 40:
        p, v = rk4(p, v, t, dt, n, False)
        t += dt
        sk += 0.5 * v * v; sv += abs(p) ** n / n
        pasos += 1
        if p_ant > 0 >= p or p_ant < 0 <= p:
            cruces += 1
        p_ant = p
    return (sk - sv) / (sk + sv)

def dilucion(n, phi0=1.0, dt=0.005):
    p, v, t = phi0, 0.0, 20.0
    pts = []
    v_ant = v
    p_ant = p
    while t < 3000.0:
        p, v = rk4(p, v, t, dt, n, True)
        t += dt
        if v_ant * v < 0:
            pts.append((t, abs(p) ** n / n))
        v_ant = v
    xs = [math.log(t ** (2 / 3)) for t, _ in pts]
    ys = [math.log(e) for _, e in pts]
    mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs), len(pts)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'n':>3} {'<w> numerico':>13} {'(n-2)/(n+2)':>12} {'pend. numerica':>15} {'-6n/(n+2)':>10} {'maximos':>8}")
    for n in (2, 4, 6):
        w = w_medio(n)
        teo = (n - 2) / (n + 2)
        s, k = dilucion(n)
        print(f"{n:3d} {w:13.5f} {teo:12.5f} {s:15.4f} {-6 * n / (n + 2):10.4f} {k:8d}")
        assert abs(w - teo) < 2e-3
        assert abs(s - (-6 * n / (n + 2))) < 0.02 * abs(6 * n / (n + 2))
    # ecuacion de estado instantanea para un campo casi congelado
    for k_sobre_v in (0.0, 0.01, 0.1, 1.0):
        w = (k_sobre_v - 1) / (k_sobre_v + 1)
        print(f"K/V = {k_sobre_v:5.2f} -> w = {w:+.4f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
