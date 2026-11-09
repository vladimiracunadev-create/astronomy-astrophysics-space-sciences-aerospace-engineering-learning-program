#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C24: instrumentos de plasma y campos in situ, analizador electrostatico, momentos de la distribucion, longitud de Debye y magnetometro fluxgate.

Datos: k_B, e, masa del proton, masa del electron y permitividad del vacio (8,8541878188e-12 F/m) de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09). ILUSTRATIVOS (no son medidas ni el diseno
de ningun instrumento): viento solar de protones con densidad 5 cm-3, velocidad 400 km/s y temperatura 1e5 K; 200 canales de energia por carga entre 200 eV y 5 keV; 300000 deteccion simuladas;
nucleo fluxgate con B = 1e5 tanh(H/1e4) en unidades arbitrarias de nT, excitacion de 5e4 nT.
Modelo: (1) energia por carga de un proton de velocidad v: E/q = m v^2/(2 e); (2) muestras (semilla 20261109) de una maxwelliana unidimensional desplazada, ponderadas por el flujo (aceptacion
proporcional a v) y agrupadas en canales logaritmicos; (3) densidad, velocidad y temperatura recuperadas con pesos 1/v y correccion de Sheppard por la anchura del canal; (4) longitud de Debye
sqrt(eps0 k T/(n e^2)) y frecuencia de plasma sqrt(n e^2/(eps0 m_e))/(2 pi); (5) magnetometro fluxgate: segundo armonico de la tension de captacion V = d phi/dt con phi = B tanh((H_exc sin wt + B0)/H_s).
Supuestos: haz alineado con el analizador, sin potencial de la nave, un solo especie, sin perdida de angulo de aceptacion. Validez: ilustrativa.
Tolerancia: velocidad recuperada 1 %, temperatura 10 %; fluxgate lineal a 1e-3 relativo para campos debiles.
"""
from __future__ import annotations
import math, platform, random

KB = 1.380649e-23
E = 1.602176634e-19
MP = 1.67262192595e-27
ME = 9.1093837139e-31
EPS0 = 8.8541878188e-12
U0, T0, N0 = 400e3, 1e5, 5e6
W = math.sqrt(KB * T0 / MP)


def e_por_q(v):
    return MP * v * v / (2 * E)


def v_de_eq(eq):
    return math.sqrt(2 * E * eq / MP)


def fluxgate(b0, n=4096):
    hs, bsat, hexc = 1e4, 1e5, 5e4
    ph = [bsat * math.tanh((hexc * math.sin(2 * math.pi * k / n) + b0) / hs) for k in range(n)]
    v = [(ph[(k + 1) % n] - ph[k - 1]) / 2 * n / (2 * math.pi) for k in range(n)]   # d phi/d(omega t), derivada centrada
    a2 = sum(v[k] * math.sin(2 * 2 * math.pi * k / n) for k in range(n)) * 2 / n
    return a2


def calc():
    r = {"eq_400": e_por_q(U0), "w_kms": W / 1e3, "w_u": W / U0}
    emin, emax, nb = 200.0, 5000.0, 200
    ln0, ln1 = math.log(emin), math.log(emax)
    rng = random.Random(20261109)
    cuentas = [0] * nb
    total = 0
    vmax = U0 + 6 * W
    while total < 300000:
        v = rng.gauss(U0, W)
        if v <= 0:
            continue
        if rng.random() * vmax > v:
            continue
        eq = e_por_q(v)
        if emin <= eq < emax:
            b = int((math.log(eq) - ln0) / (ln1 - ln0) * nb)
            cuentas[b] += 1
            total += 1
    dln = (ln1 - ln0) / nb
    vc = [v_de_eq(math.exp(ln0 + (i + 0.5) * dln)) for i in range(nb)]
    wts = [c / v for c, v in zip(cuentas, vc)]
    sw = sum(wts)
    um = sum(w * v for w, v in zip(wts, vc)) / sw
    var = sum(w * (v - um) ** 2 for w, v in zip(wts, vc)) / sw
    dv = [v * dln / 2 for v in vc]                       # dv/dlnE = v/2
    sheppard = sum(w * d * d / 12 * 4 for w, d in zip(wts, dv)) / sw   # anchura de canal en v = v dln/2
    r["u_est"] = um
    r["T_sin"] = MP * var / KB
    r["T_con"] = MP * (var - sheppard) / KB
    r["pico_eV"] = vc[max(range(nb), key=lambda i: cuentas[i])]
    r["pico_eq"] = e_por_q(r["pico_eV"])
    r["debye"] = math.sqrt(EPS0 * KB * T0 / (N0 * E * E))
    r["fp_kHz"] = math.sqrt(N0 * E * E / (EPS0 * ME)) / (2 * math.pi) / 1e3
    r["fg"] = {b: fluxgate(b) for b in (10.0, 50.0, 100.0, 5000.0)}
    r["fg_sens"] = r["fg"][10.0] / 10.0
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"E/q de un proton a 400 km/s = {r['eq_400']:.2f} eV ; velocidad termica = {r['w_kms']:.3f} km/s ({r['w_u']*100:.2f} % de la deriva)")
    print(f"canal del maximo: E/q = {r['pico_eq']:.1f} eV")
    print(f"velocidad recuperada = {r['u_est']/1e3:.3f} km/s (verdadera 400) ; temperatura sin correccion = {r['T_sin']:.0f} K ; con Sheppard = {r['T_con']:.0f} K (verdadera {T0:.0f})")
    print(f"longitud de Debye = {r['debye']:.3f} m ; frecuencia de plasma electronica = {r['fp_kHz']:.3f} kHz")
    for b, a in r["fg"].items():
        print(f"fluxgate B0 = {b:7.1f} nT : 2.o armonico = {a:.6e} ; por nT = {a/b:.6e}")
    assert abs(r["u_est"] - U0) / U0 < 0.01
    assert abs(r["T_con"] - T0) / T0 < 0.10
    assert abs(r["fg"][100.0] / 100.0 - r["fg_sens"]) / abs(r["fg_sens"]) < 1e-3
    assert abs(r["fg"][5000.0] / 5000.0 - r["fg_sens"]) / abs(r["fg_sens"]) > 1e-3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
