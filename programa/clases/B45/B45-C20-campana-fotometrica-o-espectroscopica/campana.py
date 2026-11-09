#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C20: plan de una campana fotometrica, masa de aire, tiempo de exposicion y presupuesto de S/N.

Datos: todo ILUSTRATIVO: sitio a latitud -30 grados, objetivo con declinacion -10 grados y magnitud V = 14,0, punto cero instrumental de 21,0 mag para 1 e-/s, extincion de 0,15 mag por masa de aire,
cielo de 20 e-/s/pixel, apertura de 80 pixeles, ruido de lectura de 5 e-, objetivo S/N = 100 por exposicion y 20 s de sobrecarga por exposicion. La formula de masa de aire de Kasten y Young (1989)
se leyo en la pagina Air mass (astronomy) de Wikipedia el 2026-11-09: X = 1/[cos z + 0,50572 (96,07995 - z)^-1,6364] con z en grados. Semilla 20261109.
Modelo: cos z = sin(lat) sin(dec) + cos(lat) cos(dec) cos(H); flujo S = 10^(-0,4 (V - ZP + k X)); tiempo t de la ecuacion cuadratica de S/N; ventana donde X <= 1,5.
Supuestos: extincion constante, sin Luna, cielo constante, objetivo S/N por exposicion sin considerar la variabilidad de la transparencia. Validez: planificacion de primer orden.
Tolerancia: la solucion del tiempo reproduce S/N = 100 a 1e-9; Monte Carlo de S/N a 3 % de 100; masa de aire de Kasten-Young frente a sec z a 1e-3 en el cenit.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
LAT = math.radians(-30.0)
DEC = math.radians(-10.0)
V = 14.0
ZP = 21.0
K = 0.15
SKY = 20.0
NPIX = 80
RN = 5.0
SNR = 100.0
OVERHEAD = 20.0


def cos_z(Hh):
    H = math.radians(15.0 * Hh)
    return math.sin(LAT) * math.sin(DEC) + math.cos(LAT) * math.cos(DEC) * math.cos(H)


def masa_aire_ky(zdeg):
    return 1 / (math.cos(math.radians(zdeg)) + 0.50572 * (96.07995 - zdeg) ** -1.6364)


def X_de(Hh):
    z = math.degrees(math.acos(cos_z(Hh)))
    return masa_aire_ky(z), 1 / cos_z(Hh), z


def flujo(X):
    return 10 ** (-0.4 * (V - ZP + K * X))


def tiempo(S, snr=SNR):
    a = S ** 2
    b = -snr ** 2 * (S + NPIX * SKY)
    c = -snr ** 2 * NPIX * RN ** 2
    return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)


def sn(S, t):
    return S * t / math.sqrt(S * t + NPIX * (SKY * t + RN ** 2))


def calcular():
    r = {}
    r["filas"] = []
    for Hh in (0.0, 1.0, 2.0, 3.0, 4.0, 5.0):
        X, Xs, z = X_de(Hh)
        S = flujo(X)
        t = tiempo(S)
        r["filas"].append((Hh, z, X, Xs, S, t, sn(S, t)))
    # ventana X <= 1.5
    ventana = []
    h = 0.0
    while True:
        X, _, z = X_de(h)
        if X > 1.5:
            break
        h += 0.01
    r["H_lim"] = h
    r["ventana_h"] = 2 * h
    S_med = flujo(1.25)
    t_med = tiempo(S_med)
    r["t_med"] = t_med
    r["n_exp"] = int(r["ventana_h"] * 3600 / (t_med + OVERHEAD))
    r["eficiencia"] = t_med / (t_med + OVERHEAD)
    r["tiempo_util_h"] = r["n_exp"] * t_med / 3600
    # Monte Carlo del S/N a X = 1.25 con t_med
    rnd = random.Random(SEMILLA)
    npix_mu = S_med * t_med
    est = []
    for _ in range(20000):
        s = rnd.gauss(npix_mu, math.sqrt(npix_mu))
        # el ruido del fondo ya se incluye en la varianza total: simulamos el estimador (senal - fondo medido)
        ruido_total = math.sqrt(NPIX * (SKY * t_med + RN ** 2))
        est.append(s + rnd.gauss(0, ruido_total))
    m = sum(est) / len(est)
    sd = math.sqrt(sum((a - m) ** 2 for a in est) / (len(est) - 1))
    r["sn_mc"] = m / sd
    r["sn_formula"] = sn(S_med, t_med)
    # precision de la curva de luz resultante
    r["sigma_mag"] = 1.0857 / r["sn_formula"]
    # cenit
    r["X_cenit"] = masa_aire_ky(0.0)
    r["X_80"] = masa_aire_ky(80.0), 1 / math.cos(math.radians(80.0))
    r["delta_mag"] = K * (1.5 - 1.0)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"{'H (h)':>6} {'z (grados)':>11} {'X (K-Y)':>8} {'sec z':>7} {'S (e-/s)':>9} {'t (s)':>8} {'S/N':>7}")
    for Hh, z, X, Xs, S, t, s in r["filas"]:
        print(f"{Hh:6.1f} {z:11.2f} {X:8.4f} {Xs:7.4f} {S:9.3f} {t:8.1f} {s:7.3f}")
    print(f"masa de aire en el cenit (K-Y) = {r['X_cenit']:.5f} ; a z = 80 grados: K-Y {r['X_80'][0]:.3f} frente a sec z {r['X_80'][1]:.3f}")
    print(f"ventana X <= 1,5: |H| <= {r['H_lim']:.2f} h, es decir {r['ventana_h']:.2f} h ; exposicion a X = 1,25: {r['t_med']:.1f} s ; eficiencia {r['eficiencia']*100:.1f} %")
    print(f"numero de exposiciones en la ventana = {r['n_exp']} ; tiempo de obturador = {r['tiempo_util_h']:.2f} h ; sigma por punto = {r['sigma_mag']*1000:.2f} mmag")
    print(f"S/N a X = 1,25: formula {r['sn_formula']:.3f} ; Monte Carlo {r['sn_mc']:.3f} ; perdida de {r['delta_mag']:.3f} mag entre X = 1,0 y 1,5")
    for Hh, z, X, Xs, S, t, s in r["filas"]:
        assert abs(s - SNR) < 1e-9
    assert abs(r["X_cenit"] - 1.0) < 1e-3
    assert abs(r["sn_mc"] / SNR - 1) < 0.03
    assert r["n_exp"] > 10
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
