#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B93-C03: reflexiones en una linea sin perdidas, acoplamiento entre pistas y margen de temporizacion.

Datos consultados (2026-11-10): notas de curso UCSB ECE 145A (Long, 2007): coeficiente de reflexion Gamma = (RL - Z0)/(RL + Z0),
Z0 = sqrt(L/C), v = 1/sqrt(LC) y el retardo de una linea de longitud l como l/v; para microtira W = h sobre epoxi-vidrio er_eff = 3.4.
NO CONSULTADOS (relaciones estandar): modelo de acoplamiento de dos lineas Kb = (Cm/C + Lm/L)/4 (referido a la onda incidente) y su forma exacta con impedancias de modo par e impar, Kb = (Zoe - Zoo)/(2(Zoe + Zoo));
longitud de saturacion = tr v / 2.
SINTETICOS / ILUSTRATIVOS: linea de 50 ohm y 150 mm con er_eff = 3.587 (microtira de la clase C01), fuente de 3.3 V con Rs = 20 ohm o 50 ohm,
carga casi abierta (1 Mohm), tiempo de subida 0.5 ns, razones de acoplamiento Cm/C = 0.08 y Lm/L = 0.15, reloj de 100 MHz con tco, tsu y banda de +-10 %.
Segunda via: simulacion temporal de la linea con diferencias finitas (FDTD, paso magico dt = dx/v, 200 celdas) frente al diagrama de rebotes analitico.
Tolerancias: valor final frente a Vs*RL/(Rs+RL) con 1e-6 relativa en el diagrama de rebotes; FDTD frente al diagrama dentro de 0.04 V en las mesetas;
Kb aproximado frente al exacto dentro de 3 % relativo.
"""
from __future__ import annotations
import math, platform

C = 299792458.0
Z0, LONG, EEFF = 50.0, 0.150, 3.587
VS, RL, TR = 3.3, 1e6, 0.5e-9
V = C / math.sqrt(EEFF)
T = LONG / V


def rebotes(rs, rl, nmax=60):
    gs, gl = (rs - Z0) / (rs + Z0), (rl - Z0) / (rl + Z0)
    vp = VS * Z0 / (rs + Z0)
    vl, out = 0.0, []
    for k in range(nmax):
        vl += vp * (gs * gl) ** k * (1 + gl)
        out.append(((2 * k + 1) * T, vl))
    return out


def fdtd(rs, rl, n=200, tfin=12 * T):
    lp = Z0 / V              # H/m
    cp = 1.0 / (Z0 * V)      # F/m
    dx = LONG / n
    dt = dx / V
    v = [0.0] * (n + 1)
    i = [0.0] * n
    t, serie = 0.0, []
    while t < tfin:
        for k in range(n):
            i[k] -= dt / (lp * dx) * (v[k + 1] - v[k])
        for k in range(1, n):
            v[k] -= dt / (cp * dx) * (i[k] - i[k - 1])
        a = 2.0 * dt / (cp * dx)                      # = 2 Z0 en ohm
        v[0] = (v[0] + a * (VS / rs - i[0])) / (1.0 + a / rs)
        v[n] = (v[n] + a * i[n - 1]) / (1.0 + a / rl)
        t += dt
        serie.append((t, v[n]))
    return serie


def muestra(serie, t):
    mejor = min(serie, key=lambda p: abs(p[0] - t))
    return mejor[1]


def establecimiento(rs, rl, banda=0.10):
    s = rebotes(rs, rl)
    vf = VS * rl / (rs + rl)
    ts = T  # primera llegada: si ya esta dentro de la banda, se establece en T
    for (t, v) in s:
        if abs(v - vf) > banda * VS:
            ts = t + 2 * T  # la llegada siguiente es la primera que podria estar dentro
    return ts, s


def kb_aprox(cm, lm):
    return (cm + lm) / 4.0


def kb_exacto(cm, lm):
    zoe = math.sqrt((1 + lm) / (1 - cm))
    zoo = math.sqrt((1 - lm) / (1 + cm))
    return 0.5 * (zoe - zoo) / (zoe + zoo)  # referido a la onda incidente en la linea agresora


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Linea SINTETICA: Z0 = {Z0:.0f} ohm, {LONG*1e3:.0f} mm, er_eff = {EEFF}; v = {V/C:.3f} c; retardo T = {T*1e9:.3f} ns; Vs = {VS} V")
    for nombre, rs in (("Rs = 20 ohm (sin adaptar)", 20.0), ("Rs = 50 ohm (terminacion serie)", 50.0)):
        gs, gl = (rs - Z0) / (rs + Z0), (RL - Z0) / (RL + Z0)
        ts, s = establecimiento(rs, RL)
        vmax = max(v for _, v in s)
        vf = VS * RL / (rs + RL)
        assert abs(s[-1][1] / vf - 1) < 1e-6
        print(f"{nombre}: Gamma_fuente = {gs:+.4f}, Gamma_carga = {gl:+.5f}; 1a llegada = {s[0][1]:.3f} V; pico = {vmax:.3f} V ({(vmax/VS-1)*100:+.1f} %); final = {s[-1][1]:.4f} V; establecimiento (+-10 %) = {ts*1e9:.2f} ns")
    # segunda via: FDTD frente a rebotes
    serie = fdtd(20.0, RL)
    s20 = rebotes(20.0, RL)
    print("Meseta de la carga, Rs = 20 ohm: diagrama de rebotes frente a FDTD")
    pe = 0.0
    for k in range(4):
        tm = (2 * k + 2) * T
        va = s20[k][1]
        vf_ = muestra(serie, tm)
        pe = max(pe, abs(va - vf_))
        print(f"  t = {tm*1e9:5.2f} ns   rebotes {va:6.3f} V   FDTD {vf_:6.3f} V")
    print(f"Diferencia maxima en las mesetas = {pe:.4f} V")
    assert pe < 0.04
    # acoplamiento
    cm, lm = 0.08, 0.15
    ka, ke = kb_aprox(cm, lm), kb_exacto(cm, lm)
    assert abs(ka / ke - 1) < 0.03
    lsat = TR * V / 2
    print(f"Acoplamiento ILUSTRATIVO Cm/C = {cm}, Lm/L = {lm}: Kb aproximado = {ka:.4f}, exacto = {ke:.4f} (dif. {abs(ka/ke-1)*100:.2f} %)")
    vinc = VS * Z0 / (50.0 + Z0)  # onda incidente con fuente adaptada de 50 ohm
    print(f"Longitud de saturacion = tr v / 2 = {lsat*1e3:.1f} mm; onda incidente = {vinc:.2f} V; diafonia cercana saturada = {ke*vinc*1e3:.0f} mV")
    for lc in (0.020, 0.040, 0.150):
        ne = ke * vinc * min(1.0, 2 * lc / (V * TR))
        print(f"  longitud acoplada {lc*1e3:5.0f} mm -> NE = {ne*1e3:6.1f} mV")
    # temporizacion
    tper, tco, tsu = 10e-9, 3e-9, 2e-9
    for nombre, rs in (("Rs = 20 ohm", 20.0), ("Rs = 50 ohm", 50.0)):
        ts, _ = establecimiento(rs, RL)
        margen = tper - tco - ts - tsu
        print(f"Margen de preparacion (reloj 100 MHz, tco 3 ns, tsu 2 ns) con {nombre}: {margen*1e9:.2f} ns")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
