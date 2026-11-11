#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B108-C04: persona sujeta por una restriccion de pies modelada como oscilador torsional (SINTETICO).

CONSULTADOS (2026-11-10, solo resumen del registro): NASA TP-3433 (NTRS 19940017154): ensayo con plataforma de fuerza y restriccion de pies,
fuerzas de aprox. 400 a 750 N; NASA TP-3424 (NTRS 19940016133): sin restriccion de pies la persona transmite cargas a la estructura y trabaja
mejor hacia el cuerpo. La rigidez de ninguna restriccion real (p. ej. el APFR) se consulto.
ILUSTRATIVOS (sinteticos, no medidos): inercia respecto al punto de sujecion I = 60 kg m2, altura de la fuerza sobre el pivote h = 0.5 m,
fuerza 100 N (y 400 N como extremo inferior del rango consultado), rigidez k = 800 N m/rad, razon de amortiguamiento 0.3.
Modelo: I theta'' + c theta' + k theta = F h (escalon), lineal (pequenos angulos). Analitico subamortiguado:
theta(t) = ts [1 - e^{-z wn t}(cos wd t + z/sqrt(1-z^2) sin wd t)], ts = F h / k. Sin restriccion: k = c = 0 -> theta = F h t^2/(2 I).
Segunda via: Runge-Kutta 4 con dt = 1e-3 s. Tolerancia: 1e-6 rad en el escalon. Unidades SI; ejes del cuerpo, pivote en el tobillo.
"""
from __future__ import annotations
import math, platform

I, H, K, Z = 60.0, 0.5, 800.0, 0.3


def analitico(t, f, k, z, i=I):
    ts = f * H / k
    wn = math.sqrt(k / i)
    wd = wn * math.sqrt(1 - z * z)
    return ts * (1 - math.exp(-z * wn * t) * (math.cos(wd * t) + z / math.sqrt(1 - z * z) * math.sin(wd * t)))


def rk4(t_fin, f, k, z, i=I, dt=1e-3):
    c = 2 * z * math.sqrt(k * i)
    def d(y):
        th, w = y
        return (w, (f * H - c * w - k * th) / i)
    y, t, pico = (0.0, 0.0), 0.0, 0.0
    for _ in range(int(round(t_fin / dt))):
        k1 = d(y)
        k2 = d((y[0] + dt / 2 * k1[0], y[1] + dt / 2 * k1[1]))
        k3 = d((y[0] + dt / 2 * k2[0], y[1] + dt / 2 * k2[1]))
        k4 = d((y[0] + dt * k3[0], y[1] + dt * k3[1]))
        y = (y[0] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
             y[1] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
        pico = max(pico, y[0])
    return y[0], pico


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    F = 100.0
    ts = F * H / K
    wn = math.sqrt(K / I)
    wd = wn * math.sqrt(1 - Z * Z)
    mp = math.exp(-math.pi * Z / math.sqrt(1 - Z * Z))
    print(f"Restriccion SINTETICA: I = {I} kg m2, h = {H} m, k = {K} N m/rad, zeta = {Z}; F = {F:.0f} N")
    print(f"  theta estatico = {ts:.4f} rad = {math.degrees(ts):.2f} grados; wn = {wn:.4f} rad/s ({wn/2/math.pi:.3f} Hz); wd = {wd:.4f} rad/s")
    print(f"  sobreimpulso teorico = {mp*100:.2f} %; instante del pico = {math.pi/wd:.4f} s; pico = {ts*(1+mp):.4f} rad")
    th_n, pico = rk4(5.0, F, K, Z)
    th_a = analitico(5.0, F, K, Z)
    print(f"  RK4: theta(5 s) = {th_n:.6f} rad; pico numerico = {pico:.4f} rad; analitico theta(5 s) = {th_a:.6f} rad; dif = {abs(th_n - th_a):.1e} rad")
    libre = F * H * 2.0 ** 2 / (2 * I)
    print(f"Sin restriccion (cuerpo libre): theta(2 s) = {libre:.4f} rad = {math.degrees(libre):.2f} grados (crece sin cota)")
    print(f"Con restriccion: theta(2 s) = {analitico(2.0, F, K, Z):.4f} rad = {math.degrees(analitico(2.0, F, K, Z)):.2f} grados")
    print("Barrido de rigidez (F = 100 N):")
    print("  k [N m/rad]  theta estatico [grados]  wn [rad/s]  pico [grados]")
    for k in (200.0, 800.0, 3200.0):
        t_ = F * H / k
        w_ = math.sqrt(k / I)
        print(f"  {k:10.0f}  {math.degrees(t_):22.2f}  {w_:10.3f}  {math.degrees(t_ * (1 + mp)):12.2f}")
    f2 = 400.0
    t2 = f2 * H / K
    print(f"Con F = {f2:.0f} N (extremo inferior del rango consultado): theta estatico = {t2:.3f} rad = {math.degrees(t2):.2f} grados"
          f" -> {'fuera' if t2 > 0.2 else 'dentro'} de la hipotesis de pequenos angulos (limite ilustrativo 0.2 rad)")
    assert abs(th_n - th_a) < 1e-6 and abs(pico - ts * (1 + mp)) < 2e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
