#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C23: paso de integracion, error y determinismo del nucleo de un simulador de misión robotica.

Dato consultado (2026-11-10): masa de Perseverance 1025 kg (NASA). ILUSTRATIVOS (sinteticos, no medidos): empuje constante de 200 N, amortiguamiento viscoso de 80 N s/m,
oscilador de comprobacion de 1025 kg con rigidez 100 N/m y sin amortiguamiento, tiempo simulado de 60 s (y de 2000 s para el oscilador), pasos de 5 s a 0.1 s, semilla fija.
Modelo: m v' = F - c v con solucion analitica v(t) = (F/c)(1 - exp(-c t/m)); integradores Euler explicito y RK4 de paso fijo; oscilador m x'' = -k x con energia conservada.
Segunda via: la solucion analitica; orden de convergencia observado (razon de errores al dividir el paso por 2: 2 para Euler, 16 para RK4); estabilidad de Euler para dt < 2 m/c;
determinismo: dos ejecuciones con la misma semilla dan la misma huella.
Unidades SI. Un solo grado de libertad, sin contacto ni saturacion; no es un simulador completo.
"""
from __future__ import annotations
import hashlib, math, platform, random, struct

M, F, C = 1025.0, 200.0, 80.0           # M consultado; F y C ILUSTRATIVOS
K_OSC, T_FIN, T_OSC, SEMILLA = 100.0, 60.0, 2000.0, 20261110


def v_exacta(t):
    return (F / C) * (1 - math.exp(-C * t / M))


def deriv(v):
    return (F - C * v) / M


def euler(dt, t_fin=T_FIN):
    v, n = 0.0, int(round(t_fin / dt))
    for _ in range(n):
        v += dt * deriv(v)
    return v


def rk4(dt, t_fin=T_FIN):
    v, n = 0.0, int(round(t_fin / dt))
    for _ in range(n):
        k1 = deriv(v); k2 = deriv(v + 0.5 * dt * k1); k3 = deriv(v + 0.5 * dt * k2); k4 = deriv(v + dt * k3)
        v += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return v


def energia_osc(metodo, dt):
    x, v, n = 1.0, 0.0, int(round(T_OSC / dt))
    acel = lambda x_: -K_OSC / M * x_
    for _ in range(n):
        if metodo == "euler":
            x, v = x + dt * v, v + dt * acel(x)
        else:
            k1x, k1v = v, acel(x)
            k2x, k2v = v + 0.5 * dt * k1v, acel(x + 0.5 * dt * k1x)
            k3x, k3v = v + 0.5 * dt * k2v, acel(x + 0.5 * dt * k2x)
            k4x, k4v = v + dt * k3v, acel(x + dt * k3x)
            x += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
            v += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
    return 0.5 * M * v * v + 0.5 * K_OSC * x * x


def huella(semilla):
    rng = random.Random(semilla)
    datos = [rng.gauss(0, 1) for _ in range(1000)]
    return hashlib.sha256(struct.pack("1000d", *datos)).hexdigest()[:16]


def calc():
    ex = v_exacta(T_FIN)
    filas = []
    for dt in (5.0, 2.5, 1.0, 0.5, 0.1):
        filas.append((dt, abs(euler(dt) - ex) / ex, abs(rk4(dt) - ex) / ex))
    ord_e = filas[0][1] / filas[1][1]
    ord_r = filas[0][2] / filas[1][2]
    dt_lim = 2 * M / C
    inestable = abs(1 - C / M * 30.0) > 1                 # Euler con dt = 30 s (> 2 m/c = 25.6 s)
    e0 = 0.5 * K_OSC * 1.0 ** 2
    deriva_e = abs(energia_osc("euler", 1.0) - e0) / e0
    deriva_r = abs(energia_osc("rk4", 1.0) - e0) / e0
    dt_ok = next(dt for dt, ee, er in reversed(filas) if er < 1e-6) if any(er < 1e-6 for _, _, er in filas) else None
    return dict(ex=ex, filas=filas, ord_e=ord_e, ord_r=ord_r, dt_lim=dt_lim, inestable=inestable, deriva_e=deriva_e, deriva_r=deriva_r, dt_ok=dt_ok,
                h1=huella(SEMILLA), h2=huella(SEMILLA), h3=huella(SEMILLA + 1), tau=M / C, vterm=F / C, e_5=filas[0][1], r_5=filas[0][2], e_01=filas[-1][1], r_01=filas[-1][2],
                e_1=filas[2][1], r_1=filas[2][2])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Modelo ILUSTRATIVO: m = {M:.0f} kg (consultada), F = {F:.0f} N, c = {C:.0f} N s/m; v(60 s) exacta = {r['ex']:.6f} m/s; tau = {r['tau']:.2f} s; v terminal = {r['vterm']:.2f} m/s")
    print(" dt [s]   error relativo Euler   error relativo RK4")
    for dt, ee, er in r["filas"]:
        print(f"{dt:6.1f} {ee:20.3e} {er:20.3e}")
    print(f"Razon de errores al dividir dt por 2 (5 -> 2.5): Euler = {r['ord_e']:.2f} (orden 1 -> 2); RK4 = {r['ord_r']:.2f} (orden 4 -> 16)")
    print(f"Limite de estabilidad de Euler: dt < 2 m/c = {r['dt_lim']:.2f} s; con dt = 30 s, inestable = {r['inestable']}")
    print(f"Deriva de energia del oscilador en 2000 s con dt = 1 s: Euler = {r['deriva_e']:.3e}; RK4 = {r['deriva_r']:.3e}")
    print(f"Huellas de 1000 numeros: semilla {SEMILLA}: {r['h1']} y {r['h2']} (iguales: {r['h1'] == r['h2']}); semilla {SEMILLA+1}: {r['h3']}")
    assert 1.5 < r["ord_e"] < 2.5 and 10 < r["ord_r"] < 20 and r["inestable"] and r["h1"] == r["h2"] != r["h3"] and r["deriva_r"] < r["deriva_e"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
