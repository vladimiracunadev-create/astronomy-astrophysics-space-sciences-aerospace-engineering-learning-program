#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C11: PD frente a PID ante un par perturbador constante.

Datos: SINTÉTICOS. Eje J = 50 kg m^2, referencia r = 0, perturbación de par
constante d = 0.5 N m (p. ej. presión de radiación o gradiente de gravedad
idealizados), Kp = 20 N m/rad, Kd = 40 N m s/rad, Ki = 2 N m/(rad s).
Modelo: J omega' = Kp (r - theta) + Ki xi - Kd omega + d,  xi' = r - theta
(derivada sobre la medida). Polinomio característico del PID:
J s^3 + Kd s^2 + Kp s + Ki.
Referencias independientes:
  - PD: theta_ss = d / Kp = 25 mrad (balance de pares en equilibrio);
  - PID: theta_ss = 0 y xi_ss = -d / Ki (balance de pares con integral);
  - Routh del cúbico: estable si Ki < Kd Kp / J = 16 N m/(rad s); en ese valor
    aparecen polos en +-j sqrt(Kp/J).
Supuestos: LTI continuo, sin saturación. Tolerancia: 1e-9 en las fórmulas;
1e-6 rad para el valor final simulado.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp

J, Kp, Kd, d = 50.0, 20.0, 40.0, 0.5


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def simula(Ki, T=600.0):
    def f(t, x):
        th, w, xi = x
        e = 0.0 - th
        u = Kp * e + Ki * xi - Kd * w
        return [w, (u + d) / J, e]
    t = np.linspace(0, T, 6001)
    s = solve_ivp(f, [0, T], [0.1, 0.0, 0.0], t_eval=t, rtol=1e-11, atol=1e-13)
    return t, s.y


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    # PD (Ki = 0): el integrador xi no se usa
    t, y = simula(0.0)
    print(f"PD : theta(600 s) = {y[0,-1]*1e3:.6f} mrad; d/Kp = {d/Kp*1e3:.6f} mrad")
    prueba(abs(y[0, -1] - d / Kp) < 1e-6, "error estacionario del PD")

    Ki = 2.0
    t, y = simula(Ki)
    print(f"PID: theta(600 s) = {y[0,-1]*1e3:.6f} mrad; xi(600 s) = {y[2,-1]:.6f} rad s; -d/Ki = {-d/Ki:.6f}")
    prueba(abs(y[0, -1]) < 1e-6, "error estacionario del PID nulo")
    prueba(abs(y[2, -1] + d / Ki) < 1e-5, "integral compensa la perturbación")
    pico = np.max(np.abs(y[0]))
    print(f"    máximo |theta| = {pico*1e3:.2f} mrad (condición inicial 100 mrad)")

    # polos y frontera de Routh
    for Ki_ in (2.0, 8.0, 15.9, 16.1):
        p = np.roots([J, Kd, Kp, Ki_])
        print(f"Ki = {Ki_:5.1f}: polos {np.round(p, 4)}  parte real máx = {p.real.max():+.5f}")
    prueba(np.roots([J, Kd, Kp, 15.9]).real.max() < 0 < np.roots([J, Kd, Kp, 16.1]).real.max(), "Ki_crit = 16")
    pc = np.roots([J, Kd, Kp, 16.0])
    im = pc[np.abs(pc.real) < 1e-9]
    prueba(len(im) == 2 and abs(abs(im[0].imag) - np.sqrt(Kp / J)) < 1e-9, "polos en +-j sqrt(Kp/J)")
    print(f"Ki_crit = Kd Kp/J = {Kd*Kp/J}; polos en la frontera {np.round(pc, 6)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
