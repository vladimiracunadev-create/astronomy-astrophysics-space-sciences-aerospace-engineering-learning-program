#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C18: enlace de bajada de un instrumento cientifico, presupuesto de enlace, BER de BPSK, limite de Shannon y duracion de un paso.

Datos: k_B = 1,380649e-23 J/K y c = 299792458 m/s de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09); GM_Tierra = 3,986004e14 m3/s2 y R_ecuatorial = 6,3781e6 m de la UAI B3 de 2015
(consultada el 2026-11-09). ILUSTRATIVOS (no son los de ninguna mision ni estacion): orbita circular a 600 km, mascara de elevacion 10 grados, 8,2 GHz, transmisor de 5 W, ganancia de antena de
a bordo 6 dBi, ganancia de la estacion 35 dBi, temperatura de sistema 150 K, perdidas varias 3 dB, BPSK sin codificacion, velocidad de 1 Mbit/s.
Modelo: (1) distancia oblicua d = sqrt((R+h)^2 - (R cos e)^2) - R sin e; perdida de espacio libre (4 pi d / lambda)^2; C/N0 = EIRP + G/T - L_fs - L_otras - 10 log k;
(2) BER teorica de BPSK Q(sqrt(2 Eb/N0)) = erfc(sqrt(Eb/N0))/2 frente a un Monte Carlo de 400000 bits (semilla 20261109); (3) limite de Shannon Eb/N0 >= (2^(R/B) - 1)/(R/B) y su limite ln 2;
(4) duracion del paso cenital: 2 lambda_c/(2 pi) T con lambda_c = acos(R cos e/(R+h)) - e, frente a una simulacion vectorial del paso.
Supuestos: orbita circular, Tierra esferica sin atmosfera ni lluvia, sin efecto Doppler ni errores de apuntamiento de la antena. Validez: ilustrativa.
Tolerancia: BER simulada a 5 % de la teorica; duracion de paso de dos vias, 1e-3 relativo; limite de Shannon, 1e-4.
"""
from __future__ import annotations
import math, platform, random

KB = 1.380649e-23
C = 299792458.0
GM = 3.986004e14
RE = 6.3781e6
H = 600e3
A = RE + H
EL = math.radians(10)
F = 8.2e9
LAM = C / F
PT, GT, GR, TS, LOT = 5.0, 6.0, 35.0, 150.0, 3.0
PER = 2 * math.pi * math.sqrt(A ** 3 / GM)


def q_func(x):
    return 0.5 * math.erfc(x / math.sqrt(2))


def ber_bpsk(ebn0_db):
    return 0.5 * math.erfc(math.sqrt(10 ** (ebn0_db / 10)))


def duracion_formula():
    lc = math.acos(RE * math.cos(EL) / A) - EL
    return 2 * lc / (2 * math.pi) * PER


def duracion_sim(dt=0.05):
    w = 2 * math.pi / PER
    est = (RE, 0.0)
    t = -PER / 4
    dentro = False
    t_ini = t_fin = None
    while t < PER / 4:
        x, y = A * math.cos(w * t), A * math.sin(w * t)
        dx, dy = x - est[0], y - est[1]
        d = math.hypot(dx, dy)
        sen = (dx * est[0] + dy * est[1]) / (d * RE)
        el = math.asin(sen)
        if el >= EL and not dentro:
            dentro, t_ini = True, t
        if el < EL and dentro:
            t_fin = t
            break
        t += dt
    return t_fin - t_ini


def calc():
    r = {}
    d = math.sqrt(A ** 2 - (RE * math.cos(EL)) ** 2) - RE * math.sin(EL)
    r["d"] = d
    fs = 20 * math.log10(4 * math.pi * d / LAM)
    r["fspl"] = fs
    r["eirp"] = 10 * math.log10(PT) + GT
    r["gt"] = GR - 10 * math.log10(TS)
    r["cn0"] = r["eirp"] + r["gt"] - fs - LOT - 10 * math.log10(KB)
    rb = 1e6
    r["ebn0"] = r["cn0"] - 10 * math.log10(rb)
    # Eb/N0 requerida para BER 1e-5 por biseccion
    lo, hi = 0.0, 20.0
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if ber_bpsk(m) > 1e-5:
            lo = m
        else:
            hi = m
    r["req"] = 0.5 * (lo + hi)
    r["margen"] = r["ebn0"] - r["req"]
    r["rb_max"] = 10 ** ((r["cn0"] - r["req"]) / 10)
    rng = random.Random(20261109)
    eb = 4.3
    sigma = math.sqrt(1 / (2 * 10 ** (eb / 10)))
    n = 400000
    err = sum(1 for _ in range(n) if 1 + rng.gauss(0, sigma) < 0)
    r["ber"] = (ber_bpsk(eb), err / n, eb)
    r["shannon"] = {}
    for eta in (0.1, 1.0, 2.0, 4.0):
        r["shannon"][eta] = 10 * math.log10((2 ** eta - 1) / eta)
    r["shannon_lim"] = 10 * math.log10(math.log(2))
    r["t_formula"], r["t_sim"] = duracion_formula(), duracion_sim()
    r["volumen_MB"] = rb * r["t_formula"] / 8 / 1e6
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"distancia oblicua a 10 grados = {r['d']/1e3:.2f} km ; perdida de espacio libre = {r['fspl']:.2f} dB")
    print(f"EIRP = {r['eirp']:.2f} dBW ; G/T = {r['gt']:.2f} dB/K ; C/N0 = {r['cn0']:.2f} dB-Hz")
    print(f"a 1 Mbit/s: Eb/N0 = {r['ebn0']:.2f} dB ; requerida para BER 1e-5 = {r['req']:.3f} dB ; margen = {r['margen']:.2f} dB ; velocidad maxima = {r['rb_max']/1e6:.2f} Mbit/s")
    teo, sim, eb = r["ber"]
    print(f"BER de BPSK a Eb/N0 = {eb} dB: teorica = {teo:.5f} ; simulada = {sim:.5f}")
    for eta, v in r["shannon"].items():
        print(f"Shannon: R/B = {eta:3.1f} -> Eb/N0 minima = {v:7.3f} dB")
    print(f"limite R/B -> 0: {r['shannon_lim']:.4f} dB")
    print(f"duracion del paso cenital: formula = {r['t_formula']:.3f} s ; simulacion = {r['t_sim']:.3f} s ; volumen a 1 Mbit/s = {r['volumen_MB']:.1f} MB")
    assert abs(sim - teo) / teo < 0.05
    assert abs(r["t_formula"] - r["t_sim"]) / r["t_formula"] < 1e-3
    assert abs(r["shannon_lim"] + 1.5917) < 1e-3
    assert r["margen"] > 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
