#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C09: ondas de Alfven en diferencias finitas y comparacion con la velocidad de Alfven y el tiempo de viaje WKB.

Datos: mu_0 y m_p (NIST CODATA 2022), consultados 2026-11-09. El campo (1e-3 T), la densidad (n = 1e15 m^-3 en la base y escala de altura de 5e7 m), el tamano del dominio (4e8 m)
y la forma del pulso son ILUSTRATIVOS (sinteticos).
Modelo: onda de Alfven transversal en un campo uniforme B a lo largo de x con densidad rho(x): d^2 xi/dt^2 = v_A^2(x) d^2 xi/dx^2, v_A = B/sqrt(mu_0 rho(x)); esquema explicito de tres
niveles (salto de rana) con condicion CFL dt = 0.5 dx/max v_A; pulso gaussiano que se propaga hacia +x. Comparacion con: (a) medio uniforme v = B/sqrt(mu_0 rho); (b) tiempo de viaje
Int dx/v_A(x) en un medio con rho = rho_0 exp(-x/H) (aproximacion WKB: la forma del pulso se conserva en el tiempo de viaje).
Supuestos: onda lineal, campo uniforme, sin disipacion. Validez: longitudes de onda mucho menores que la escala de variacion de v_A.
Tolerancia: velocidad numerica frente a la analitica dentro de 1 % (medio uniforme); tiempo de viaje numerico frente al WKB dentro de 3 % (medio estratificado).
"""
from __future__ import annotations
import math
import platform
import sys

MU0, MP = 1.25663706127e-6, 1.67262192595e-27
B = 1e-3
N0, H = 1e15, 5e7
L = 4e8


def va(x, estratificado):
    rho = (N0 * MP * (math.exp(-x / H) if estratificado else 1.0))
    return B / math.sqrt(MU0 * rho)


def simular(estratificado, nx=4000, x_ini=0.4e8, ancho=0.12e8, destino=3.0e8):
    dx = L / nx
    xs = [i * dx for i in range(nx + 1)]
    v = [va(x, estratificado) for x in xs]
    vmax = max(v)
    dt = 0.5 * dx / vmax
    # pulso que viaja hacia +x: xi(x, 0) = f(x), xi(x, -dt) = f(x + c dt) con c = v local (aproximacion para una onda hacia +x)
    f = lambda x: math.exp(-0.5 * ((x - x_ini) / ancho) ** 2)
    prev = [f(x + v[i] * dt) for i, x in enumerate(xs)]
    act = [f(x) for x in xs]
    t = 0.0
    i_dest = int(destino / dx)
    mejor_t, mejor_a = 0.0, 0.0
    pasos = 0
    while t < 20 * L / vmin_globalizado(v) and pasos < 200000:
        nuevo = act[:]
        for i in range(1, nx):
            nuevo[i] = 2 * act[i] - prev[i] + (v[i] * dt / dx) ** 2 * (act[i + 1] - 2 * act[i] + act[i - 1])
        nuevo[0] = nuevo[1]
        nuevo[nx] = nuevo[nx - 1]
        prev, act = act, nuevo
        t += dt
        pasos += 1
        a = act[i_dest]
        if a > mejor_a:
            mejor_a, mejor_t = a, t
        elif a < 0.5 * mejor_a and mejor_a > 0.5:
            break
    return mejor_t, mejor_a, xs, v, dx


def vmin_globalizado(v):
    return min(v)


def tiempo_wkb(x0, x1, estratificado, n=20000):
    h = (x1 - x0) / n
    s = 1 / va(x0, estratificado) + 1 / va(x1, estratificado)
    for i in range(1, n):
        s += (4 if i % 2 else 2) / va(x0 + i * h, estratificado)
    return s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    v0 = va(0.0, False)
    print(f"velocidad de Alfven en la base (B = {B * 1e3:g} mT, n = {N0:.0e} m-3): v_A = B/sqrt(mu_0 n m_p) = {v0 / 1e3:.1f} km/s")
    # (a) medio uniforme
    t_num, amp, xs, v, dx = simular(False)
    x_ini, destino = 0.4e8, 3.0e8
    v_num = (destino - x_ini) / t_num
    print(f"medio uniforme: tiempo de viaje numerico = {t_num:.3f} s para {(destino - x_ini) / 1e6:.0f} Mm -> v = {v_num / 1e3:.1f} km/s ; analitica = {v0 / 1e3:.1f} km/s ; cociente = {v_num / v0:.4f} ; amplitud del pulso = {amp:.3f}")
    assert abs(v_num / v0 - 1) < 0.01, "velocidad de Alfven numerica"
    # (b) medio estratificado
    t_num2, amp2, xs, v, dx = simular(True)
    t_wkb = tiempo_wkb(x_ini, destino, True)
    print(f"medio estratificado (rho ~ exp(-x/H), H = {H / 1e6:.0f} Mm): v_A de {va(x_ini, True) / 1e3:.1f} a {va(destino, True) / 1e3:.1f} km/s ; tiempo numerico = {t_num2:.3f} s ; WKB Int dx/v_A = {t_wkb:.3f} s ; cociente = {t_num2 / t_wkb:.4f} ; amplitud = {amp2:.3f}")
    assert abs(t_num2 / t_wkb - 1) < 0.03, "tiempo de viaje WKB"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
