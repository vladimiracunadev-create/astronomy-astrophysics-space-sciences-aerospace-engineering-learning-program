#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C12: sintonía de un PID por ganancia última y por colocación de polos.

Datos: SINTÉTICOS. (a) Planta térmica normalizada G(s) = 1/(s + 1)^3 (tres
inercias térmicas en cascada, tiempo en unidades de la constante de tiempo);
(b) eje J = 50 kg m^2 (doble integrador) para la colocación de polos.
Modelo y referencias independientes:
  - ganancia última: 1 + K G = 0 en s = j w -> (s+1)^3 + K = 0 tiene raíces
    imaginarias para K_u = 8 y w_u = sqrt(3); periodo P_u = 2 pi / sqrt(3);
  - regla clásica de Ziegler-Nichols de lazo cerrado (REGLA EMPÍRICA, no se
    verifica contra la literatura aquí): Kp = 0.6 K_u, Ti = P_u/2, Td = P_u/8;
  - colocación de polos en el doble integrador: Kp = J wn^2, Kd = 2 zeta wn J,
    con polos exactamente en -zeta wn +- j wn sqrt(1-zeta^2).
Supuestos: LTI, sin saturación, derivador con filtro N = 10 (Td s/(1+Td s/N)).
Tolerancia: 1e-9 para K_u, w_u y polos; las métricas del escalón se informan.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy import signal
from scipy.optimize import brentq


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def ultima():
    """K_u y w_u por el cruce de fase -180 grados de G(jw) = 1/(jw+1)^3."""
    fase = lambda w: np.imag(1.0 / (1j * w + 1) ** 3)
    wu = brentq(fase, 0.5, 5.0)
    return 1.0 / abs(1.0 / (1j * wu + 1) ** 3), wu


def cerrado_pid(Kp, Ti, Td, N=10.0):
    # C = Kp (1 + 1/(Ti s) + Td s/(1 + Td s/N))
    # términos sobre el denominador común  Ti s (1 + Td s/N)
    den_c = np.polymul([Ti, 0.0], [Td / N, 1.0])
    num_p = np.polymul([Ti, 0.0], [Td / N, 1.0])               # 1 * den_c
    num_i = np.array([Td / N, 1.0])                            # 1/(Ti s) * den_c
    num_d = np.polymul([Td, 0.0], [Ti, 0.0])                   # Td s/(1+Td s/N) * den_c
    num_c = Kp * np.polyadd(np.polyadd(num_p, num_i), num_d)
    nG, dG = [1.0], np.polymul(np.polymul([1, 1], [1, 1]), [1, 1])
    num_l, den_l = np.polymul(num_c, nG), np.polymul(den_c, dG)
    den_t = np.polyadd(den_l, num_l)
    return num_l, den_t


def metricas(num, den, T=60.0):
    t = np.linspace(0, T, 60001)
    _, y = signal.step(signal.TransferFunction(num, den), T=t)
    mp = max(0.0, y.max() - 1.0)
    fuera = np.nonzero(np.abs(y - 1) > 0.02)[0]
    ts = t[fuera[-1]] if len(fuera) else 0.0
    iae = np.trapezoid(np.abs(1 - y), t)
    return mp, ts, iae


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    Ku, wu = ultima()
    Pu = 2 * math.pi / wu
    print(f"ganancia última: K_u = {Ku:.9f}, w_u = {wu:.9f} rad, P_u = {Pu:.6f}")
    prueba(abs(Ku - 8.0) < 1e-9 and abs(wu - math.sqrt(3)) < 1e-9, "K_u = 8, w_u = sqrt 3")
    r = np.roots([1, 3, 3, 1 + Ku])
    prueba(np.sum(np.abs(r.real) < 1e-7) == 2, "polos imaginarios en K_u")

    print("controlador              Kp     Ti      Td     Mp(%)   ts(2%)   IAE")
    casos = {
        "ZN lazo cerrado": (0.6 * Ku, Pu / 2, Pu / 8),
        "ZN, Kp a la mitad": (0.3 * Ku, Pu / 2, Pu / 8),
        "PI conservador": (0.4 * Ku / 2, Pu / 1.2, 0.0),
    }
    res = {}
    for nombre, (Kp, Ti, Td) in casos.items():
        if Td == 0.0:
            num_l = np.polymul([Kp * Ti, Kp], [1.0])
            den_l = np.polymul([Ti, 0.0], [1, 3, 3, 1])
            num, den = num_l, np.polyadd(den_l, num_l)
        else:
            num, den = cerrado_pid(Kp, Ti, Td)
        est = bool(np.all(np.roots(den).real < 0))
        mp, ts, iae = metricas(num, den)
        res[nombre] = (mp, ts, iae, est)
        print(f"{nombre:22s} {Kp:6.3f} {Ti:6.3f} {Td:6.3f}  {100*mp:6.1f}  {ts:7.2f}  {iae:6.3f}   estable={est}")
        prueba(est, f"estable: {nombre}")
    prueba(res["ZN lazo cerrado"][0] > res["ZN, Kp a la mitad"][0], "reducir Kp reduce el sobreimpulso")

    # colocación de polos en el eje
    J = 50.0
    for wn, z in ((0.3, 0.7), (0.6, 0.9), (1.0, 0.7)):
        Kp, Kd = J * wn**2, 2 * z * wn * J
        p = np.roots([J, Kd, Kp])
        ex = complex(-z * wn, wn * math.sqrt(1 - z * z))
        prueba(abs(max(p, key=lambda c: c.imag) - ex) < 1e-9, "polos colocados")
        print(f"colocación wn = {wn}, zeta = {z}: Kp = {Kp:.3f}, Kd = {Kd:.3f}; polos {np.round(p, 5)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
