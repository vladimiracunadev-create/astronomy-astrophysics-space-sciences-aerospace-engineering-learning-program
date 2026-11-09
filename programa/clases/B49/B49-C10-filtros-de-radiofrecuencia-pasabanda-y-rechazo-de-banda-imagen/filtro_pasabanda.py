#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C10: filtro pasabanda de Butterworth, rechazo de la banda imagen y perdida de insercion por resonadores con perdidas.

Datos: ninguna constante fisica. La frecuencia central de 1420 MHz (cercana a la banda de la linea del hidrogeno neutro, redondeada), el ancho de banda de 200 MHz, la frecuencia intermedia de 100 MHz, la
impedancia de 50 ohm y el factor de calidad sin carga de 200 son ILUSTRATIVOS; no describen ningun filtro real.
Modelo: prototipo pasabajos de Butterworth g_k = 2 sin((2k-1) pi/(2n)); transformacion a pasabanda con Omega = (f/f0 - f0/f)/Delta, Delta = BW/f0; respuesta teorica |S21|^2 = 1/(1 + Omega^(2n)). Segunda via
independiente: escalera LC pasabanda (resonadores serie y paralelo) evaluada con matrices ABCD, S21 = 2/(A + B/R0 + C R0 + D), con y sin resistencia de perdidas en las bobinas R = w0 L/Qu. Perdida de insercion
en el centro frente a la aproximacion de disipacion 4,343 (suma de g)/(Delta Qu). Banda imagen del receptor superheterodino con oscilador local bajo: f_im = f_RF - 2 f_FI.
Supuestos: elementos concentrados, resonadores aislados, sin acoplos parasitos; la aproximacion de disipacion vale para Delta Qu grande. Validez: banda estrecha (Delta pequeno).
Tolerancia: escalera sin perdidas frente a la formula de Butterworth a 1e-9 en |S21|^2; perdida de insercion de la escalera con perdidas frente a la aproximacion a 5 %.
"""
from __future__ import annotations
import cmath, math, platform

R0 = 50.0


def prototipo(n):
    return [2 * math.sin((2 * k - 1) * math.pi / (2 * n)) for k in range(1, n + 1)]


def omega_bp(f, f0, delta):
    return (f / f0 - f0 / f) / delta


def s21_teorico(f, f0, delta, n):
    return 1 / (1 + omega_bp(f, f0, delta) ** (2 * n))


def s21_escalera(f, f0, delta, g, qu=None):
    w0 = 2 * math.pi * f0
    w = 2 * math.pi * f
    m = [[1, 0], [0, 1]]
    def mul(a, b):
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]
    for k, gk in enumerate(g):
        if k % 2 == 0:   # serie: L = g R0/(w0 D), C = D/(w0 g R0)
            L = gk * R0 / (w0 * delta)
            C = delta / (w0 * gk * R0)
            rl = (w0 * L / qu) if qu else 0.0
            z = rl + 1j * w * L + 1 / (1j * w * C)
            m = mul(m, [[1, z], [0, 1]])
        else:            # paralelo: C = g/(R0 w0 D), L = R0 D/(w0 g)
            C = gk / (R0 * w0 * delta)
            L = R0 * delta / (w0 * gk)
            rl = (w0 * L / qu) if qu else 0.0
            y = 1j * w * C + 1 / (rl + 1j * w * L)
            m = mul(m, [[1, 0], [y, 1]])
    a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
    return abs(2 / (a + b / R0 + c * R0 + d)) ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    f0, bw, fi = 1420.0, 200.0, 100.0
    delta = bw / f0
    fim = f0 - 2 * fi
    print(f"f0 = {f0} MHz ; BW = {bw} MHz ; Delta = {delta:.5f} ; f_FI = {fi} MHz ; banda imagen en {fim} MHz ; Omega_im = {omega_bp(fim, f0, delta):.4f}")
    print(f"{'n':>2} {'suma g':>8} {'rechazo imagen (dB)':>20} {'escalera (dB)':>14} {'dif max |S21|^2':>16} {'IL centro Qu=200 (dB)':>22} {'aprox. (dB)':>12}")
    for n in (2, 3, 5, 7):
        g = prototipo(n)
        rech = -10 * math.log10(s21_teorico(fim, f0, delta, n))
        esc = -10 * math.log10(s21_escalera(fim, f0, delta, g))
        dmax = 0.0
        for k in range(1, 400):
            f = 1000 + k * 2.0
            dmax = max(dmax, abs(s21_teorico(f, f0, delta, n) - s21_escalera(f, f0, delta, g)))
        assert dmax < 1e-9
        il = -10 * math.log10(s21_escalera(f0, f0, delta, g, 200.0))
        ap = 4.343 * sum(g) / (delta * 200.0)
        assert abs(il / ap - 1) < 0.05
        print(f"{n:2d} {sum(g):8.4f} {rech:20.3f} {esc:14.3f} {dmax:16.2e} {il:22.4f} {ap:12.4f}")
    print("Puntos de -3 dB: f = f0 sqrt(1 + (Delta/2)^2) +- f0 Delta/2")
    f_hi = f0 * (math.sqrt(1 + (delta / 2) ** 2) + delta / 2)
    f_lo = f0 * (math.sqrt(1 + (delta / 2) ** 2) - delta / 2)
    print(f"  f_inf = {f_lo:.3f} MHz ; f_sup = {f_hi:.3f} MHz ; |S21|^2 en ambos (n = 5) = {s21_teorico(f_lo, f0, delta, 5):.5f} y {s21_teorico(f_hi, f0, delta, 5):.5f}")
    assert abs(s21_teorico(f_lo, f0, delta, 5) - 0.5) < 1e-9
    print("Efecto de la frecuencia intermedia en el rechazo de la imagen (n = 5, BW = 200 MHz):")
    for fi2 in (20.0, 50.0, 100.0, 200.0):
        print(f"  f_FI = {fi2:5.0f} MHz -> imagen en {f0 - 2 * fi2:6.0f} MHz ; rechazo = {-10 * math.log10(s21_teorico(f0 - 2 * fi2, f0, delta, 5)):8.3f} dB")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
