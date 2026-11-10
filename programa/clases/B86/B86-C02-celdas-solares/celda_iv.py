#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C02: curva I-V de una celda solar SINTETICA (modelo de diodo unico con resistencia en serie).

Datos consultados (2026-11-10): constante de Boltzmann k = 1.380649e-23 J/K (NIST, CODATA 2022); irradiancia solar 1361.0 W/m2
(NASA/NSSDC); eficiencias BOL de celdas multiunion de 29.5 % a 32.2 % (tabla del estado del arte de la NASA, solo como orden de magnitud).
La carga elemental e = 1.602176634e-19 C es un valor exacto del SI; NO se consulto en esta clase.
ILUSTRATIVOS (sinteticos, no medidos): area 30 cm2, Iph = 0.5200 A, I0 = 5e-11 A, n = 4.5 (equivalente de tres uniones), Rs = 0.05 ohm,
Eg efectiva 4.0 eV para I0(T), coeficiente de Iph 6e-4 /K, temperatura de referencia 301.15 K.
Modelo: I = Iph - I0 (exp(q (V + I Rs)/(n k T)) - 1), con I resuelta por Newton.
Segunda via: Voc en forma cerrada (Rs no interviene con I = 0) y maximo de P(V) por busqueda en rejilla fina.
Tolerancia: Voc numerico frente al cerrado < 1e-9 V; Pmax de seccion aurea frente a rejilla < 1e-6 W.
"""
from __future__ import annotations
import math, platform

K, Q = 1.380649e-23, 1.602176634e-19
G, AREA = 1361.0, 30.0e-4
IPH, I0, N, RS, EG, ALFA, TREF = 0.5200, 5.0e-11, 4.5, 0.05, 4.0, 6.0e-4, 301.15


def params(T):
    iph = IPH * (1.0 + ALFA * (T - TREF))
    i0 = I0 * (T / TREF) ** 3 * math.exp(EG * Q / (N * K) * (1.0 / TREF - 1.0 / T))
    return iph, i0


def corriente(v, T=TREF):
    iph, i0 = params(T)
    nvt = N * K * T / Q
    i = iph
    for _ in range(100):
        e = math.exp((v + i * RS) / nvt)
        f = iph - i0 * (e - 1.0) - i
        df = -i0 * e * RS / nvt - 1.0
        d = f / df
        i -= d
        if abs(d) < 1e-14:
            break
    return i


def voc_numerico(T=TREF):
    lo, hi = 0.0, 4.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if corriente(m, T) > 0.0:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def voc_cerrado(T=TREF):
    iph, i0 = params(T)
    return N * K * T / Q * math.log(iph / i0 + 1.0)


def pmax_aurea(T=TREF):
    voc = voc_numerico(T)
    a, b = 0.0, voc
    g = (math.sqrt(5.0) - 1.0) / 2.0
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(200):
        if corriente(c, T) * c > corriente(d, T) * d:
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    v = 0.5 * (a + b)
    return v, corriente(v, T), v * corriente(v, T)


def pmax_rejilla(T=TREF, paso=1.0e-5):
    voc = voc_numerico(T)
    mejor = (0.0, 0.0)
    v = 0.0
    while v < voc:
        p = v * corriente(v, T)
        if p > mejor[1]:
            mejor = (v, p)
        v += paso
    return mejor


def resultados():
    isc = corriente(0.0)
    voc = voc_numerico()
    vmp, imp, pmax = pmax_aurea()
    vg, pg = pmax_rejilla()
    eta = pmax / (G * AREA)
    pt = {T: pmax_aurea(T)[2] for T in (233.15, 301.15, 353.15)}
    voct = {T: voc_numerico(T) for T in (233.15, 301.15, 353.15)}
    coef = (pt[353.15] - pt[233.15]) / pt[301.15] / (353.15 - 233.15) * 100.0
    return dict(Isc=isc, Voc=voc, Voc_cerr=voc_cerrado(), dVoc=abs(voc - voc_cerrado()), Vmp=vmp, Imp=imp, Pmax=pmax,
                FF=pmax / (voc * isc), eta=eta, eta_pct=eta * 100.0, Pgrid=pg, Vgrid=vg, dP=abs(pmax - pg),
                P233=pt[233.15], P301=pt[301.15], P353=pt[353.15], Voc233=voct[233.15], Voc353=voct[353.15],
                coef=coef, n_serie=28.0 / vmp, n_serie_ent=math.ceil(28.0 / vmp), Pala=G * 1.2 * 0.85 * eta, Pinc=G * AREA, Vt=N * K * TREF / Q, Pcarga=1.0 * corriente(1.0))


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Celda SINTETICA: area = {AREA*1e4:.0f} cm2, G = {G} W/m2, T = {TREF-273.15:.1f} C; potencia incidente = {r['Pinc']:.4f} W")
    print(f"Isc = {r['Isc']:.5f} A ; Voc = {r['Voc']:.5f} V (cerrado {r['Voc_cerr']:.5f} V; diferencia {r['dVoc']:.1e} V)")
    print(f"Punto de maxima potencia: Vmp = {r['Vmp']:.4f} V ; Imp = {r['Imp']:.5f} A ; Pmax = {r['Pmax']:.5f} W")
    print(f"Pmax por rejilla = {r['Pgrid']:.5f} W en V = {r['Vgrid']:.4f} V ; diferencia = {r['dP']:.1e} W")
    print(f"Factor de llenado FF = {r['FF']:.4f} ; eficiencia = {r['eta_pct']:.2f} %")
    print(" T [K]   Voc [V]   Pmax [W]")
    for T, v, p in ((233.15, r["Voc233"], r["P233"]), (301.15, r["Voc"], r["P301"]), (353.15, r["Voc353"], r["P353"])):
        print(f" {T:6.2f}  {v:7.4f}   {p:7.4f}")
    print(f"Coeficiente de temperatura de Pmax = {r['coef']:.3f} %/K")
    assert r["dVoc"] < 1e-9
    assert r["dP"] < 1e-6
    assert r["Isc"] > r["Imp"] and r["Voc"] > r["Vmp"]
    assert 0.5 < r["FF"] < 0.95
    assert r["P233"] > r["P301"] > r["P353"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
