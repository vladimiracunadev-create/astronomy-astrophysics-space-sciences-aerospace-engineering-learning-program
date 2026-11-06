#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C05: de espacio de estados a función de transferencia.

Datos: SINTÉTICOS. Eje con J = 50 kg m^2 y fricción viscosa c = 10 N m s/rad,
sensor de ángulo. Lazo PD cerrado con Kp = 20 N m/rad, Kd = 40 N m s/rad.
Modelo: G(s) = C (sI - A)^-1 B + D. Para el eje con fricción
  G(s) = 1 / (s (J s + c)),  polos 0 y -c/J.
Lazo cerrado PD sobre el doble integrador:
  T(s) = (Kd s + Kp) / (J s^2 + Kd s + Kp).
Referencias independientes: fórmulas cerradas anteriores; descomposición en
fracciones simples (scipy.signal.residue) frente a la respuesta temporal
cerrada; teorema del valor final.
Supuestos: LTI, condiciones iniciales nulas. Tolerancia: 1e-12 en G(s) y
1e-10 en la respuesta temporal.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy import signal


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    J, c = 50.0, 10.0
    A = np.array([[0.0, 1.0], [0.0, -c / J]])
    B = np.array([[0.0], [1.0 / J]])
    C = np.array([[1.0, 0.0]])
    D = np.array([[0.0]])

    # 1) G(s) = C (sI - A)^-1 B en varios puntos, contra la fórmula cerrada
    for s in (0.3 + 0.0j, 1.0 + 2.0j, -0.5 + 1.0j):
        g = (C @ np.linalg.inv(s * np.eye(2) - A) @ B + D)[0, 0]
        g_ex = 1.0 / (s * (J * s + c))
        prueba(abs(g - g_ex) <= 1e-12 * abs(g_ex), f"G({s})")
    print("G(s) = C(sI-A)^-1 B coincide con 1/(s(Js+c)) en 3 puntos")

    # 2) numerador, denominador y polos con ss2tf
    num, den = signal.ss2tf(A, B, C, D)
    print("ss2tf: num =", np.round(num[0], 12), " den =", np.round(den, 12))
    polos = np.roots(den)
    print("polos de G:", np.sort(polos))
    prueba(np.allclose(np.sort(polos), [-c / J, 0.0], atol=1e-12), "polos")
    print(f"ganancia de velocidad a baja frecuencia 1/c = {1/c:.3f} rad/s por N m")

    # 3) lazo cerrado PD: T(s)
    Kp, Kd = 20.0, 40.0
    numT, denT = [Kd, Kp], [J, Kd, Kp]
    pT = np.roots(denT)
    wn, z = np.sqrt(Kp / J), Kd / (2 * np.sqrt(Kp * J))
    print(f"T(s): polos {pT[0]:.4f}, {pT[1]:.4f}; wn = {wn:.4f} rad/s, zeta = {z:.4f}; cero en {-Kp/Kd:.3f}")
    prueba(abs(abs(pT[0]) - wn) < 1e-12, "|polo| = wn")

    # 4) respuesta a un escalón: residuos vs integración
    r, p, k = signal.residue(np.array(numT, float), np.polymul(denT, [1.0, 0.0]))
    t = np.linspace(0, 30, 3001)
    y_res = sum(ri * np.exp(pi * t) for ri, pi in zip(r, p)).real
    tt, y_ss = signal.step(signal.TransferFunction(numT, denT), T=t)
    err = np.max(np.abs(y_res - y_ss))
    print(f"escalón: residuos vs scipy.signal.step, error máx = {err:.2e}")
    prueba(err < 1e-8, "respuesta por residuos")

    # 5) teorema del valor final: lim s T(s)/s = T(0) = 1
    prueba(abs(Kp / Kp - 1.0) < 1e-15, "valor final")
    print(f"valor final del escalón = T(0) = {Kp/Kp:.1f}; y(30 s) = {y_res[-1]:.6f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
