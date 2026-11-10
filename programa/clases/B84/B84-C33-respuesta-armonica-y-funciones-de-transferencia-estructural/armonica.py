#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C33: respuesta armonica y funciones de transferencia de una estructura de 2 grados de libertad.

DATOS ILUSTRATIVOS (no consultados): m1 = 2,0 kg, m2 = 1,0 kg, k1 = 2,0e5 N/m (suelo-m1), k2 = 1,0e5 N/m (m1-m2); amortiguamiento de Rayleigh C = a M + b K elegido para dar
zeta = 0,02 en los dos modos. Fuerza armonica sobre la masa 1; respuesta medida en la masa 2.
H21(w) = [ (K - w^2 M + i w C)^-1 ]_21 (receptancia). Segunda via: superposicion modal H21 = sum_r phi_2r phi_1r/(w_r^2 - w^2 + 2 i zeta_r w_r w) con modos normalizados a masa unitaria.
Estimacion de amortiguamiento: metodo de potencia mitad: zeta ~ (f2 - f1)/(2 f_pico) donde |H|^2 cae a la mitad del pico. Barrido 1 a 200 Hz en pasos de 0,001 Hz.
Unidades: N, m, kg, s. Tolerancias: directa frente a modal < 1e-9 relativa; zeta por potencia mitad frente a 0,02 dentro de 5 %.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import gen_eig

M1, M2, K1, K2 = 2.0, 1.0, 2.0e5, 1.0e5
M = [[M1, 0.0], [0.0, M2]]
K = [[K1 + K2, -K2], [-K2, K2]]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lam, phi = gen_eig(K, M)
    w = [math.sqrt(l) for l in lam]
    f = [x / (2 * math.pi) for x in w]
    print(f"Estructura ILUSTRATIVA de 2 GDL: frecuencias naturales f1 = {f[0]:.4f} Hz, f2 = {f[1]:.4f} Hz")
    print(f"Modos (masa unitaria): modo 1 = [{phi[0][0]:.5f}, {phi[1][0]:.5f}], modo 2 = [{phi[0][1]:.5f}, {phi[1][1]:.5f}]")
    zeta = 0.02
    # Rayleigh: zeta_r = a/(2 w_r) + b w_r/2 = 0,02 en ambos modos
    a = 2 * zeta * w[0] * w[1] / (w[0] + w[1])
    b = 2 * zeta / (w[0] + w[1])
    C = [[a * M[i][j] + b * K[i][j] for j in range(2)] for i in range(2)]
    z = [a / (2 * w[r]) + b * w[r] / 2 for r in range(2)]
    print(f"Rayleigh: a = {a:.4f} 1/s, b = {b:.3e} s ; zeta modal = {z[0]:.5f}, {z[1]:.5f}")

    def directa(om):
        d = [[complex(K[i][j] - om * om * M[i][j], om * C[i][j]) for j in range(2)] for i in range(2)]
        det = d[0][0] * d[1][1] - d[0][1] * d[1][0]
        return -d[1][0] / det  # elemento (2,1) de la inversa

    def modal(om):
        s = 0j
        for r in range(2):
            s += phi[1][r] * phi[0][r] / (w[r] ** 2 - om * om + 2j * z[r] * w[r] * om)
        return s

    dmax = 0.0
    for fr in (5.0, 20.0, 40.0, 60.0, 100.0, 150.0):
        om = 2 * math.pi * fr
        h1, h2 = directa(om), modal(om)
        dmax = max(dmax, abs(h1 - h2) / abs(h1))
    print(f"Diferencia relativa maxima entre inversion directa y superposicion modal en 6 frecuencias = {dmax:.1e}")
    print("Receptancia |H21| [m/N] y fase en frecuencias seleccionadas:")
    for fr in (1.0, f[0] * 0.5, f[0], 0.5 * (f[0] + f[1]), f[1], 150.0):
        h = directa(2 * math.pi * fr)
        print(f"  f = {fr:8.3f} Hz  |H| = {abs(h):.4e}  fase = {math.degrees(math.atan2(h.imag, h.real)):8.2f} grados")
    print(f"Respuesta estatica |H21(0)| = {abs(directa(0.0)):.4e} m/N (= 1/k1: la fuerza sobre m1 la soporta el resorte k1)")
    # Barrido y potencia mitad
    paso = 0.001
    puntos = [(1.0 + i * paso, abs(directa(2 * math.pi * (1.0 + i * paso)))) for i in range(int((200 - 1.0) / paso) + 1)]
    for r in range(2):
        cerca = [(fr, h) for fr, h in puntos if abs(fr - f[r]) < 0.2 * f[r]]
        fp, hp = max(cerca, key=lambda t: t[1])
        mitad = hp / math.sqrt(2)
        f1 = next(fr for fr, h in reversed([t for t in cerca if t[0] < fp]) if h < mitad)
        f2 = next(fr for fr, h in [t for t in cerca if t[0] > fp] if h < mitad)
        zest = (f2 - f1) / (2 * fp)
        print(f"Modo {r + 1}: pico en {fp:.3f} Hz, |H| = {hp:.4e} ; puntos de potencia mitad {f1:.3f} y {f2:.3f} Hz -> zeta estimada = {zest:.5f} (modal {z[r]:.5f}, dif {abs(zest - z[r]) / z[r] * 100:.2f} %)")
        assert abs(zest - z[r]) / z[r] < 0.05
    assert dmax < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
