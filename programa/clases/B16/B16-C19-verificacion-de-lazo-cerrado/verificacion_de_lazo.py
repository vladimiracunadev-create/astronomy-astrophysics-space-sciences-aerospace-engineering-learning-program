#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C19: matriz de verificación de un lazo cerrado.

Datos: SINTÉTICOS. Eje J = 50 kg m^2, PD con derivada sobre la medida
(Kp = 20 N m/rad, Kd = 40 N m s/rad), perturbación de par d = 0.5 N m,
escalón de referencia de 0.1 rad.
Los requisitos son INVENTADOS para la clase. El diseño inicial incumple R5
(hallazgo de la verificación) y se rediseña con Kd = 48. Requisitos:
  R1 estabilidad asintótica (polos continuos y, en la versión muestreada, radio
     espectral < 1 con T = 0.1 s);
  R2 sobreimpulso <= 10 %;  R3 asentamiento (2 %) <= 15 s;
  R4 error estacionario ante d <= 30 mrad;
  R5 sobreimpulso <= 10 % para toda inercia en [0.7, 1.3] J (Monte Carlo + barrido);
  R6 la implementación muestreada (T = 0.1 s) difiere de la continua <= 5 % en
     sobreimpulso.
Métodos independientes para cada requisito:
  analítico (fórmulas cerradas) / simulación continua RK4 / lazo muestreado
  exacto (retenedor de orden cero) / barrido de parámetros.
Además: orden de convergencia del integrador RK4 al reducir el paso (debe ser al menos 4).
Tolerancia: 1e-3 relativa entre analítico y simulación continua para Mp.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
from scipy.linalg import expm

Kp = 20.0
KD = [40.0]          # ganancia derivativa vigente (se rediseña en la última parte)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def rhs(x, J, d=0.0, r=0.1):
    th, w = x
    return np.array([w, (Kp * (r - th) - KD[0] * w + d) / J])


def rk4(J, h, T, d=0.0, r=0.1):
    n = int(round(T / h))
    x = np.zeros(2); th = np.empty(n + 1); th[0] = 0.0
    for k in range(n):
        k1 = rhs(x, J, d, r); k2 = rhs(x + h / 2 * k1, J, d, r)
        k3 = rhs(x + h / 2 * k2, J, d, r); k4 = rhs(x + h * k3, J, d, r)
        x = x + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        th[k + 1] = x[0]
    return th


def muestreado(J, T, Tf=60.0, d=0.0, r=0.1):
    A = np.array([[0, 1.0], [0, 0]]); B = np.array([[0], [1.0 / J]])
    M = np.zeros((3, 3)); M[:2, :2], M[:2, 2:] = A, B
    E = expm(M * T); Ad, Bd = E[:2, :2], E[:2, 2:]
    x = np.zeros((2, 1)); out = [0.0]
    for _ in range(int(round(Tf / T))):
        u = Kp * (r - x[0, 0]) - KD[0] * x[1, 0] + d
        x = Ad @ x + Bd * u
        out.append(x[0, 0])
    rho = max(abs(np.linalg.eigvals(Ad - Bd @ np.array([[Kp, KD[0]]]))))
    return np.array(out), rho


def mp_ts(th, dt, r=0.1):
    mp = max(0.0, th.max() - r) / r
    fuera = np.nonzero(np.abs(th - r) > 0.02 * r)[0]
    return mp, (fuera[-1] + 1) * dt if len(fuera) else 0.0


def verifica(J, etiqueta):
    """Ejecuta R1..R6 y devuelve {requisito: (cumple, valor)}."""
    Kd = KD[0]
    res = {}
    z = Kd / (2 * math.sqrt(Kp * J))
    polos = np.roots([J, Kd, Kp])
    _, rho = muestreado(J, 0.1)
    res["R1"] = (bool(np.all(polos.real < 0) and rho < 1), f"radio espectral {rho:.4f}")
    h = 0.01
    th = rk4(J, h, 60.0)
    mp, ts = mp_ts(th, h)
    res["R2"] = (mp <= 0.10, f"Mp = {100*mp:.2f} %")
    res["R3"] = (ts <= 15.0, f"ts = {ts:.2f} s")
    th_d = rk4(J, h, 600.0, d=0.5, r=0.0)
    res["R4"] = (th_d[-1] <= 0.030, f"e_ss = {th_d[-1]*1e3:.2f} mrad")
    peor = max(mp_ts(rk4(J * k, h, 60.0), h)[0] for k in np.linspace(0.7, 1.3, 25))
    rng = np.random.default_rng(19)
    mc = max(mp_ts(rk4(J * k, 0.02, 60.0), 0.02)[0] for k in rng.uniform(0.7, 1.3, 60))
    res["R5"] = (max(peor, mc) <= 0.10, f"peor Mp barrido {100*peor:.2f} %, Monte Carlo {100*mc:.2f} %")
    thm, _ = muestreado(J, 0.1, Tf=120.0)
    mpm, _ = mp_ts(thm, 0.1)
    dif = abs(mpm - mp) / mp
    res["R6"] = (dif <= 0.05, f"Mp muestreado {100*mpm:.2f} % ({100*dif:.1f} % de diferencia)")
    print(f"--- {etiqueta}: Kp = {Kp}, Kd = {Kd} ---")
    for k, (ok, v) in res.items():
        print(f"  {k}: {'CUMPLE ' if ok else 'NO CUMPLE'}  {v}")
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    J = 50.0
    # comprobaciones de la maquinaria (deben pasar siempre)
    z = KD[0] / (2 * math.sqrt(Kp * J))
    mp_an = math.exp(-math.pi * z / math.sqrt(1 - z * z))
    mp, _ = mp_ts(rk4(J, 0.01, 60.0), 0.01)
    print(f"maquinaria: Mp analítico {100*mp_an:.4f} % vs RK4 {100*mp:.4f} %")
    prueba(abs(mp - mp_an) < 1e-3 * mp_an, "Mp analítico vs RK4")
    th_d = rk4(J, 0.01, 600.0, d=0.5, r=0.0)
    prueba(abs(th_d[-1] - 0.5 / Kp) < 1e-6, "e_ss = d/Kp")
    ref = rk4(J, 0.0025, 20.0)[-1]
    e = [abs(rk4(J, hh, 20.0)[-1] - ref) for hh in (0.4, 0.2, 0.1)]
    orden = [math.log2(e[i] / e[i + 1]) for i in range(2)]
    print(f"convergencia RK4 (error a t = 20 s con h = 0.4, 0.2, 0.1): {e[0]:.2e}, {e[1]:.2e}, {e[2]:.2e}; órdenes {orden[0]:.2f}, {orden[1]:.2f}")
    prueba(all(o > 3.8 for o in orden), "orden al menos 4")
    print("efecto del periodo de muestreo T (lazo muestreado exacto, Kd = 40):")
    print("      T (s)   radio espectral   sobreimpulso")
    for T in (0.1, 0.5, 1.0, 2.0, 2.4, 2.6):
        thm, rho = muestreado(J, T, Tf=120.0)
        if rho < 1:
            print(f"    {T:5.1f}      {rho:8.4f}      {100*mp_ts(thm, T)[0]:7.2f} %")
        else:
            print(f"    {T:5.1f}      {rho:8.4f}      inestable")
    prueba(muestreado(J, 2.6)[1] > 1 > muestreado(J, 0.1)[1], "T grande desestabiliza")

    # matriz de verificación del diseño inicial: R5 NO se cumple (hallazgo)
    r1 = verifica(J, "diseño inicial")
    prueba(not r1["R5"][0] and all(r1[k][0] for k in ("R1", "R2", "R3", "R4", "R6")), "hallazgo esperado: falla R5")
    # rediseño: más amortiguamiento
    KD[0] = 48.0
    r2 = verifica(J, "rediseño")
    prueba(all(v[0] for v in r2.values()), "el rediseño cumple todo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
