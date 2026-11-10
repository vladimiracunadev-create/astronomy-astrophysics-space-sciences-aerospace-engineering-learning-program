#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C07: distribucion de potencia por un arnes de cobre en un bus regulado SINTETICO.

Datos consultados (2026-11-10): tensiones de bus de 12, 28 y 50 V citadas como habituales con convertidores GaN, y bus de bateria de 8.2 V con salidas de 5.0 y 3.3 V,
en el capitulo de potencia del estado del arte de naves pequenas de la NASA (solo como contexto de tensiones).
ILUSTRATIVOS (sinteticos, no medidos): cinco cargas de potencia constante (12, 20, 18, 30 y 4 W; resultado de B86-C01 en luz), longitudes de arnes (0.6, 1.2, 1.5, 2.0, 0.8 m),
resistividad del cobre 1.72e-8 ohm m y densidad 8960 kg/m3 (valores de manual NO consultados en esta clase), secciones normalizadas ilustrativas
(0.05 a 3.3 mm2), criterio de caida maxima del 2 % de la tension del bus.
Modelo: ida y vuelta (2 L); carga de potencia constante P = (V - R I) I  ->  I = (V - sqrt(V^2 - 4 R P)) / (2 R), con R la resistencia de ida y vuelta; perdida = 2 R I^2.
Segunda via: aproximacion I = P/V frente a la solucion exacta de la cuadratica; balance de potencia en el bus (fuente = cargas + perdidas).
Tolerancia: balance de potencia con residuo < 1e-9 W; la aproximacion I = P/V debe diferir de la exacta menos del 2 % en el diseno.
"""
from __future__ import annotations
import math, platform

CARGAS = [("Ordenador", 12.0, 0.6), ("Actitud", 20.0, 1.2), ("Radio", 18.0, 1.5), ("Carga util", 30.0, 2.0), ("Calefactores", 4.0, 0.8)]
SECCIONES = [0.05, 0.08, 0.13, 0.2, 0.32, 0.5, 0.82, 1.3, 2.1, 3.3]       # mm2
RHO, DENS, CAIDA = 1.72e-8, 8960.0, 0.02


def corriente_exacta(v, p, r):
    disc = v * v - 4.0 * r * p
    if disc < 0.0:
        raise ValueError("la carga de potencia constante no tiene solucion (colapso de tension)")
    return (v - math.sqrt(disc)) / (2.0 * r)


def resistencia(l, a_mm2):
    return 2.0 * RHO * l / (a_mm2 * 1e-6)


def dimensionar(v):
    filas = []
    for n, p, l in CARGAS:
        for a in SECCIONES:
            r = resistencia(l, a)
            try:
                i = corriente_exacta(v, p, r)
            except ValueError:                      # colapso de tension: la seccion es demasiado fina
                continue
            caida = r * i / v                      # caida de tension del arnes (ida y vuelta) como fraccion de v
            if caida <= CAIDA:
                break
        filas.append((n, p, l, a, r, i, caida, r * i * i, 2.0 * l * a * 1e-6 * DENS * 1000.0))
    return filas


def evaluar(v, secciones):
    out = []
    for (n, p, l), a in zip(CARGAS, secciones):
        r = resistencia(l, a)
        i = corriente_exacta(v, p, r)
        out.append((i, r * i / v, r * i * i))
    return out


def resultados():
    r = {}
    for v in (12, 28, 50):
        f = dimensionar(float(v))
        r[f"sec{v}"] = [x[3] for x in f]
        r[f"perd{v}"] = sum(x[7] for x in f)
        r[f"masa{v}"] = sum(x[8] for x in f)
        r[f"caida{v}"] = max(x[6] for x in f) * 100.0
        r[f"carga{v}"] = sum(x[1] for x in f)
        r[f"Ibus{v}"] = sum(x[5] for x in f)
    for v in (12, 28, 50):
        f = dimensionar(float(v))
        pfuente = sum(float(v) * x[5] for x in f)
        pcargas = sum(x[1] for x in f)
        r[f"resbal{v}"] = abs(pfuente - pcargas - sum(x[4] * x[5] ** 2 for x in f))   # V I_bus = suma P + suma R I^2
        r[f"sec{v}_txt"] = "; ".join(str(x) for x in r[f"sec{v}"])
    # aproximacion I = P/V frente a la exacta, a 28 V
    f28 = dimensionar(28.0)
    r["dif_aprox"] = max(abs(x[1] / 28.0 - x[5]) / x[5] for x in f28) * 100.0
    # secciones de 28 V usadas en 12 V
    ev = evaluar(12.0, r["sec28"])
    r["caida12_con28"] = max(e[1] for e in ev) * 100.0
    r["perd12_con28"] = sum(e[2] for e in ev)
    # colapso de tension: potencia maxima de una carga de potencia constante
    rr = resistencia(2.0, 0.05)
    r["Pmax_colapso"] = 28.0 ** 2 / (4.0 * rr)
    r["R_colapso"] = rr
    r["perd28_pct"] = r["perd28"] / r["carga28"] * 100.0
    r["perd12_pct"] = r["perd12"] / r["carga12"] * 100.0
    r["perd50_pct"] = r["perd50"] / r["carga50"] * 100.0
    r["r1228"] = r["perd12"] / r["perd28"]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print("Cargas SINTETICAS de potencia constante; criterio de caida maxima = 2 % ; cobre rho = 1.72e-8 ohm m (ilustrativo)")
    for v in (12, 28, 50):
        f = dimensionar(float(v))
        print(f"Bus de {v} V:")
        print("  carga          P [W]  L [m]  A [mm2]   R [ohm]   I [A]   caida [%]  perdida [W]  Cu [g]")
        for n, p, l, a, rr, i, c, pl, m in f:
            print(f"  {n:<12} {p:7.1f}  {l:5.1f}  {a:7.2f}  {rr:9.4f}  {i:6.3f}  {c*100:9.3f}  {pl:11.4f}  {m:6.2f}")
        print(f"  Total: perdida = {r[f'perd{v}']:.4f} W ({r[f'perd{v}']/r[f'carga{v}']*100:.3f} % de {r[f'carga{v}']:.0f} W) ; cobre = {r[f'masa{v}']:.1f} g ; caida maxima = {r[f'caida{v}']:.3f} %")
        print(f"  Balance de potencia en el bus: residuo = {r[f'resbal{v}']:.2e} W")
    print(f"Aproximacion I = P/V frente a la exacta (28 V): diferencia maxima = {r['dif_aprox']:.3f} %")
    print(f"Secciones de 28 V usadas en un bus de 12 V: caida maxima = {r['caida12_con28']:.2f} % ; perdida = {r['perd12_con28']:.3f} W")
    print(f"Colapso de tension: con R = {r['R_colapso']:.3f} ohm (2.0 m, 0.05 mm2) a 28 V la potencia maxima de una carga de potencia constante es {r['Pmax_colapso']:.1f} W")
    for v in (12, 28, 50):
        assert r[f"resbal{v}"] < 1e-9
        assert r[f"caida{v}"] <= CAIDA * 100.0 + 1e-9
    assert r["dif_aprox"] < 2.0
    assert r["masa12"] > r["masa28"] > r["masa50"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
