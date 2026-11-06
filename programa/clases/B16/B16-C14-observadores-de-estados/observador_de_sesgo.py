#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C14: observador de estados y estimación del sesgo de un giróscopo.

Datos: SINTÉTICOS (simulados). Ángulo verdadero theta(t) = 0.05 sin(0.1 t) rad
(en torno a una actitud), giróscopo con sesgo constante b = 2.0e-3 rad/s
(~ 413 segundos de arco por segundo, valor ficticio) y ruido blanco (muestreado a 200 Hz) en el
rastreador de estrellas de 1.0e-4 rad rms por muestra (~ 20.6 segundos de arco, ficticio).
Modelo del observador: theta' = w_m - b, b' = 0, medida y = theta.
  e' = (A - L C) e con A = [[0, -1], [0, 0]], C = [1, 0]; el polinomio es
  s^2 + L1 s - L2, de modo que L2 = -wo^2 para obtener s^2 + L1 s + wo^2.
Referencias independientes:
  - los polos de A - L C coinciden con los pedidos (exacto);
  - principio de separación: los autovalores del lazo completo (planta
    doble integrador con realimentación estimada) son la unión de los de
    A - B K y los de A - L C (exacto);
  - sin ruido, el error converge a cero (cota exponencial).
Supuestos: sesgo constante, ruido blanco gaussiano, sin saturación.
Tolerancia: 1e-12 en los autovalores; 1e-6 en el error sin ruido (Euler con h = 0.005 s).
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def ganancias(wo, zo):
    return np.array([[2 * zo * wo], [-wo**2]])        # L1, L2


def simula(wo, zo, b_true, sigma, T=300.0, h=0.005, semilla=14):
    rng = np.random.default_rng(semilla)
    A = np.array([[0.0, -1.0], [0.0, 0.0]]); C = np.array([[1.0, 0.0]])
    L = ganancias(wo, zo)
    n = int(T / h)
    th = lambda t: 0.05 * np.sin(0.1 * t)
    w_true = lambda t: 0.005 * np.cos(0.1 * t)
    xh = np.array([0.0, 0.0])
    errs = []
    t = 0.0
    for _ in range(n):
        y = th(t) + sigma * rng.normal()
        wm = w_true(t) + b_true
        # paso de Euler hacia adelante de h pequeño (wo h << 1)
        inov = y - xh[0]
        xh = xh + h * np.array([wm - xh[1] + L[0, 0] * inov, L[1, 0] * inov])
        t += h
        errs.append((th(t) - xh[0], b_true - xh[1]))
    return np.array(errs)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    A = np.array([[0.0, -1.0], [0.0, 0.0]]); C = np.array([[1.0, 0.0]])
    for wo, zo in ((0.2, 0.9), (0.5, 0.9), (1.0, 0.7)):
        L = ganancias(wo, zo)
        pol = np.sort_complex(np.linalg.eigvals(A - L @ C))
        pedido = np.sort_complex(np.roots([1, 2 * zo * wo, wo**2]))
        prueba(np.allclose(pol, pedido, atol=1e-12), "polos del observador")
        print(f"wo = {wo}, zeta = {zo}: L = [{L[0,0]:.4f}, {L[1,0]:.4f}], polos {np.round(pol, 4)}")

    # sin ruido: el error converge y el sesgo se estima
    e = simula(0.5, 0.9, 2.0e-3, 0.0, T=100.0)
    print(f"sin ruido, t = 100 s: error de ángulo {e[-1,0]:+.3e} rad, error de sesgo {e[-1,1]:+.3e} rad/s")
    prueba(abs(e[-1, 1]) < 1e-6 and abs(e[-1, 0]) < 1e-6, "convergencia sin ruido")

    # con ruido: compromiso ancho de banda - ruido
    print("con ruido de 1e-4 rad rms (t = 100..300 s):")
    print("   wo     rms error ángulo (rad)   rms error sesgo (rad/s)")
    res = {}
    for wo in (0.1, 0.3, 1.0):
        e = simula(wo, 0.9, 2.0e-3, 1.0e-4)[20000:]
        res[wo] = (np.sqrt(np.mean(e[:, 0]**2)), np.sqrt(np.mean(e[:, 1]**2)))
        print(f"  {wo:4.1f}     {res[wo][0]:.3e}              {res[wo][1]:.3e}")
    prueba(res[0.1][1] < res[1.0][1], "más ancho de banda, más ruido en el sesgo")

    # principio de separación
    J = 50.0
    Ap = np.array([[0.0, 1.0], [0.0, 0.0]]); Bp = np.array([[0.0], [1.0 / J]]); Cp = np.array([[1.0, 0.0]])
    K = np.array([[20.0, 40.0]])
    Lo = np.array([[1.2], [0.36]])                      # polos de Ap - Lo Cp en -0.6 (doble)
    Acl = np.block([[Ap, -Bp @ K], [Lo @ Cp, Ap - Bp @ K - Lo @ Cp]])
    ev = np.sort_complex(np.linalg.eigvals(Acl))
    union = np.sort_complex(np.concatenate([np.linalg.eigvals(Ap - Bp @ K), np.linalg.eigvals(Ap - Lo @ Cp)]))
    print("lazo completo:", np.round(ev, 4))
    print("unión de A-BK y A-LC:", np.round(union, 4))
    prueba(np.allclose(ev, union, atol=1e-6), "separación")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
