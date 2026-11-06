#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C16: picos de sensibilidad, ganancia pequeña e incertidumbre de inercia.

Datos: SINTÉTICOS. Planta nominal G(s) = 1/(J s^2 (tau_a s + 1)) con J = 50 kg m^2
y un actuador de primer orden tau_a = 0.5 s; controlador PD sobre el error
C(s) = Kp + Kd s con Kp = 20 N m/rad, Kd = 40 N m s/rad.
Incertidumbre: la inercia real es J_real = kappa J, kappa en [0.2, 1.6]; además
se varía el retardo del actuador tau_a.
Para la planta real, G_real = G / kappa: incertidumbre multiplicativa
constante Delta = 1/kappa - 1.
Referencias independientes:
  (1) pico de T para un sistema estándar de segundo orden:
      ||T||_inf = 1 / (2 zeta sqrt(1 - zeta^2)) si zeta < 1/sqrt 2 (exacto);
  (2) estabilidad real: raíces del polinomio característico para cada kappa;
  (3) teorema de ganancia pequeña: si |Delta| ||T||_inf < 1 el lazo es estable
      (condición suficiente, por tanto conservadora);
  (4) Routh: el lazo es estable si y solo si Kd > tau_a Kp (exacto).
Supuestos: LTI, incertidumbre solo en la inercia, sin ruido ni saturación.
Tolerancia: 1e-4 relativa para el pico de T (rejilla fina de frecuencias).
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy import signal

J, tau_a, Kp, Kd = 50.0, 0.5, 20.0, 40.0
W = np.logspace(-3, 2, 200001)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def L(s, kappa=1.0):
    return (Kp + Kd * s) / (kappa * J * s**2 * (tau_a * s + 1))


def picos(kappa=1.0):
    Ls = L(1j * W, kappa)
    S, T = 1 / (1 + Ls), Ls / (1 + Ls)
    return np.abs(S).max(), np.abs(T).max(), W[np.abs(T).argmax()]


def estable(kappa):
    # tau_a kappa J s^3 + kappa J s^2 + Kd s + Kp
    r = np.roots([tau_a * kappa * J, kappa * J, Kd, Kp])
    return bool(np.all(r.real < 0)), r.real.max()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    # (1) prueba analítica del pico de T
    for z in (0.2, 0.4, 0.6):
        wn = 0.7
        T2 = ((wn**2) / (-W**2 + 2j * z * wn * W + wn**2))
        pico = np.abs(T2).max()
        ex = 1 / (2 * z * math.sqrt(1 - z * z))
        prueba(abs(pico - ex) < 1e-4 * ex, f"pico de T zeta={z}")
        print(f"zeta = {z}: ||T||inf = {pico:.5f} (cerrada {ex:.5f})")

    Ms, Mt, wp = picos()
    print(f"lazo nominal: Ms = {Ms:.3f}, Mt = {Mt:.3f} (en {wp:.3f} rad/s); "
          f"cota de ganancia pequeña |Delta| < {1/Mt:.3f}")
    ok, a = estable(1.0)
    prueba(ok, "nominal estable")

    # (2) y (3): barrido de kappa
    print("  kappa   Delta    estable (raíces)  parte real máx   garantizado por ganancia pequeña")
    for kappa in (1.6, 1.3, 1.0, 0.7, 0.5, 0.4, 0.3, 0.2):
        d = 1 / kappa - 1
        est, a = estable(kappa)
        garantizado = abs(d) * Mt < 1
        print(f"  {kappa:4.1f}  {d:+6.2f}    {str(est):5s}           {a:+.4f}          {garantizado}")
        prueba(not garantizado or est, "la ganancia pequeña no puede garantizar un caso inestable")
    # la estabilidad (Routh) del cúbico kappa J tau s^3 + kappa J s^2 + Kd s + Kp
    # exige Kd > tau_a Kp, independiente de kappa: la inercia no puede desestabilizar
    # este lazo, pero un actuador más lento sí.
    print(f"condición exacta de Routh: Kd > tau_a Kp -> tau_a < {Kd/Kp:.3f} s para cualquier kappa")
    for ta in (0.5, 1.9, 1.99, 2.01, 3.0):
        r = np.roots([ta * J, J, Kd, Kp])
        print(f"  tau_a = {ta:5.2f} s: parte real máx = {r.real.max():+.5f} -> {'estable' if r.real.max() < 0 else 'inestable'}")
    prueba(np.roots([1.99 * J, J, Kd, Kp]).real.max() < 0 < np.roots([2.01 * J, J, Kd, Kp]).real.max(),
           "frontera tau_a = Kd/Kp")
    for kappa in (0.1, 0.5, 2.0, 5.0):
        prueba(estable(kappa)[0], "estable para cualquier kappa")

    # Monte Carlo de la inercia
    rng = np.random.default_rng(16)
    kap = rng.uniform(0.7, 1.3, 400)
    mp = []
    for k in kap:
        num, den = [Kd, Kp], np.polyadd(np.polymul([tau_a * k * J, k * J, 0, 0], [1.0]), [Kd, Kp])
        t = np.linspace(0, 80, 4001)
        _, y = signal.step(signal.TransferFunction(num, den), T=t)
        mp.append(max(0.0, y.max() - 1.0))
    mp = np.array(mp)
    print(f"Monte Carlo (400 inercias en ±30 %): sobreimpulso medio {100*mp.mean():.1f} %, "
          f"mínimo {100*mp.min():.1f} %, máximo {100*mp.max():.1f} %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
