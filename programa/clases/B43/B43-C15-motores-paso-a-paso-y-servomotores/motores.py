#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C15: motores paso a paso y servomotores: resolucion por micropaso, error bajo carga y respuesta de un servo con control PD.

Datos: ILUSTRATIVOS (motor de 200 pasos por vuelta, es decir 50 pares de polos; 16 micropasos; par de retencion 1 N m normalizado; carga del 10 %; relacion total 720:1 de C14;
servo con inercia J = 0,01 kg m^2, Kp = 1 N m/rad, amortiguamiento total 0,1 N m s/rad). Valores de orden de magnitud, sin datos de fabricantes.
Modelo: par del motor T = -T_h sin(N_pp (theta - theta_cmd)); en equilibrio con carga T_L, error mecanico = arcsin(T_L/T_h)/N_pp. Servo: J theta'' = Kp (r - theta) - c theta' con c = b + Kd;
omega_n = sqrt(Kp/J), zeta = c/(2 sqrt(Kp J)), sobreimpulso exp(-pi zeta/sqrt(1 - zeta^2)), tiempo de pico pi/(omega_n sqrt(1 - zeta^2)).
Verificacion independiente: error bajo carga por biseccion numerica del equilibrio; sobreimpulso y tiempo de pico por integracion Runge-Kutta de cuarto orden (dt = 1e-4 s).
Supuestos: motor lineal en el par, sin resonancias de media velocidad, servo ideal sin saturacion ni retardo. Validez: pequenas cargas.
Tolerancia: error bajo carga 1e-9 relativo; sobreimpulso 1e-3 absoluto, tiempo de pico 2e-3 relativo.
"""
from __future__ import annotations
import math, platform

NPP = 50; MICRO = 16; RATIO = 720.0
J = 0.01; KP = 1.0; C = 0.1

def error_cerrado(x):
    return math.asin(x) / NPP

def error_biseccion(x):
    lo, hi = 0.0, math.pi / (2 * NPP)
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.sin(NPP * mid) < x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def servo():
    dt = 1e-4; th = 0.0; w = 0.0; t = 0.0
    f = lambda th, w: (w, (KP * (1.0 - th) - C * w) / J)
    pico = 0.0; tp = 0.0
    while t < 2.0:
        k1 = f(th, w)
        k2 = f(th + 0.5 * dt * k1[0], w + 0.5 * dt * k1[1])
        k3 = f(th + 0.5 * dt * k2[0], w + 0.5 * dt * k2[1])
        k4 = f(th + dt * k3[0], w + dt * k3[1])
        th += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); w += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]); t += dt
        if th > pico:
            pico = th; tp = t
    return pico - 1.0, tp

def calc():
    r = {}
    r["pasos_vuelta"] = 200 * MICRO
    r["arcsec_micropaso_motor"] = 1296000.0 / (200 * MICRO)
    r["arcsec_micropaso_cielo"] = r["arcsec_micropaso_motor"] / RATIO
    for x in (0.05, 0.10, 0.25, 0.5):
        pass
    filas = []
    for x in (0.05, 0.10, 0.25, 0.50):
        ec = error_cerrado(x); eb = error_biseccion(x)
        filas.append((x, math.degrees(ec) * 3600, math.degrees(eb) * 3600, math.degrees(ec) * 3600 / RATIO))
    r["carga"] = filas
    wn = math.sqrt(KP / J); z = C / (2 * math.sqrt(KP * J))
    r["omega_n"] = wn; r["zeta"] = z
    r["sobreimpulso_teorico"] = math.exp(-math.pi * z / math.sqrt(1 - z * z))
    r["t_pico_teorico"] = math.pi / (wn * math.sqrt(1 - z * z))
    so, tp = servo()
    r["sobreimpulso_sim"] = so; r["t_pico_sim"] = tp
    r["t_asentamiento_2pct"] = 4 / (z * wn)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k in ("pasos_vuelta", "arcsec_micropaso_motor", "arcsec_micropaso_cielo", "omega_n", "zeta", "sobreimpulso_teorico", "sobreimpulso_sim", "t_pico_teorico", "t_pico_sim", "t_asentamiento_2pct"):
        print(f"{k} = {r[k]:.6g}")
    print("T_L/T_h | error en el motor (arcsec, cerrado) | (biseccion) | en el cielo (arcsec)")
    for x, a, b, c in r["carga"]:
        print(f"{x:.2f} | {a:.3f} | {b:.3f} | {c:.4f}")
    for x, a, b, c in r["carga"]:
        assert abs(a - b) / a < 1e-9
    assert abs(r["sobreimpulso_sim"] - r["sobreimpulso_teorico"]) < 1e-3
    assert abs(r["t_pico_sim"] - r["t_pico_teorico"]) / r["t_pico_teorico"] < 2e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
