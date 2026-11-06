#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C06: álgebra de bloques y comprobación con el lazo simulado.

Datos: SINTÉTICOS. Planta G(s) = 1/(J s^2), J = 50 kg m^2; controlador PD
C(s) = Kp + Kd s con Kp = 20 N m/rad, Kd = 40 N m s/rad; sensor ideal H = 1.
Modelo: bloques como cocientes de polinomios en s; reglas
  serie: G1 G2;  paralelo: G1 + G2;  realimentación negativa: G/(1 + G H).
Referencia independiente: se integra el lazo en espacio de estados con la
derivada sobre la medida, J theta'' = Kp (r - theta) - Kd theta'
(solve_ivp, rtol 1e-11), y se compara con su bloque equivalente
Kp/(J s^2 + Kd s + Kp); el PD sobre el error T(s) tiene un cero adicional.
Identidades verificadas: S + T = 1 con S = 1/(1+L), T = L/(1+L).
Tolerancia: 1e-8 en la respuesta; 1e-12 en las identidades.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy import signal
from scipy.integrate import solve_ivp


class Tf:
    """Cociente de polinomios en s (coeficientes en potencias decrecientes)."""
    def __init__(self, num, den):
        self.n = np.atleast_1d(np.array(num, float))
        self.d = np.atleast_1d(np.array(den, float))
    def __mul__(self, o):
        return Tf(np.polymul(self.n, o.n), np.polymul(self.d, o.d))
    def __add__(self, o):
        return Tf(np.polyadd(np.polymul(self.n, o.d), np.polymul(o.n, self.d)), np.polymul(self.d, o.d))
    def feedback(self, H=None):
        H = H or Tf([1.0], [1.0])
        # G/(1+GH) = nG dH / (dG dH + nG nH)
        return Tf(np.polymul(self.n, H.d), np.polyadd(np.polymul(self.d, H.d), np.polymul(self.n, H.n)))
    def ev(self, s):
        return np.polyval(self.n, s) / np.polyval(self.d, s)


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    J, Kp, Kd = 50.0, 20.0, 40.0
    G = Tf([1.0], [J, 0.0, 0.0])
    C = Tf([Kd, Kp], [1.0])
    L = C * G
    T = L.feedback()
    # simplificación: el cociente ya viene expresado con grado 3 sobre 3; se normaliza
    print("L(s): num", L.n, " den", L.d)
    print("T(s): num", T.n, " den", T.d)

    s = 0.4 + 1.3j
    Ls = L.ev(s)
    S_, T_ = 1 / (1 + Ls), Ls / (1 + Ls)
    prueba(abs(S_ + T_ - 1) < 1e-12, "S + T = 1")
    prueba(abs(T.ev(s) - T_) < 1e-12, "T reducido = L/(1+L)")
    print(f"identidad S + T = 1 en s = {s}: {abs(S_+T_-1):.1e}")

    polos = np.roots(T.d)
    print("polos de T:", np.round(np.sort_complex(polos), 4))
    prueba(abs(T.ev(s) - np.polyval([Kd, Kp], s) / np.polyval([J, Kd, Kp], s)) < 1e-12, "T = (Kd s+Kp)/(J s^2+Kd s+Kp)")

    # lazo simulado con la derivada sobre la MEDIDA: u = Kp (r - theta) - Kd omega.
    # Su bloque equivalente es Kp/(J s^2 + Kd s + Kp): sin el cero de T(s).
    def f(t, x):
        th, w = x
        return [w, (Kp * (1.0 - th) - Kd * w) / J]
    t = np.linspace(0, 30, 3001)
    sol = solve_ivp(f, [0, 30], [0, 0], t_eval=t, rtol=1e-11, atol=1e-13)
    Tm = signal.TransferFunction([Kp], [J, Kd, Kp])
    _, ym = signal.step(Tm, T=t)
    err = np.max(np.abs(sol.y[0] - ym))
    print(f"derivada sobre la medida: simulación vs Kp/(Js^2+Kds+Kp), error máx = {err:.2e} rad")
    prueba(err < 1e-8, "simulación vs bloque equivalente")

    # el PD sobre el error (con cero en -Kp/Kd) sobrepasa más
    _, ye = signal.step(signal.TransferFunction([Kd, Kp], [J, Kd, Kp]), T=t)
    print(f"sobreimpulso: derivada sobre la medida {100*(ym.max()-1):.2f} %, PD sobre el error {100*(ye.max()-1):.2f} %")
    prueba(ye.max() > ym.max(), "el cero aumenta el sobreimpulso")

    # perturbación: del par perturbador d a theta es G/(1+GC)
    Td = (G).feedback(C)
    ss = np.polyval(Td.n, 0.0) / np.polyval(Td.d, 0.0)
    print(f"ganancia estática perturbación->ángulo = {ss:.4f} rad/(N m) = 1/Kp = {1/Kp:.4f}")
    prueba(abs(ss - 1 / Kp) < 1e-12, "1/Kp")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
