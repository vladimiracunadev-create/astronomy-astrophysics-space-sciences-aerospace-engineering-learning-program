#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C07: realimentación, estabilidad y efecto de un retardo.

Datos: SINTÉTICOS. Eje de J = 50 kg m^2 (doble integrador), Kp = 20 N m/rad,
Kd = 40 N m s/rad, periodo de muestreo T = 0.1 s.
Modelo: (a) solo proporcional: polos +-j sqrt(Kp/J), oscilación sin
amortiguar; (b) PD: polos con parte real -Kd/(2J); (c) planta de primer orden
1/(s+1) con ganancia de lazo K: polo -(1+K), ganancia estática K/(1+K);
(d) lazo muestreado con retardo de d muestras en la medida: estabilidad por
radio espectral del sistema aumentado, confirmada con una simulación.
Referencias independientes: fórmulas cerradas (a)-(c); simulación (d).
Supuestos: LTI; discretización exacta con retenedor de orden cero.
Tolerancia: 1e-10 en (a)-(c); (d) se contrasta radio espectral vs crecimiento.
"""
from __future__ import annotations
import platform, sys
import numpy as np
import scipy
from scipy.linalg import expm


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


J, Kp, Kd, T = 50.0, 20.0, 40.0, 0.1
A = np.array([[0.0, 1.0], [0.0, 0.0]])
B = np.array([[0.0], [1.0 / J]])


def lazo_retardo(g, d):
    """Matriz del lazo muestreado, u[k] = -g (Kp theta[k-d] + Kd omega[k-d])."""
    M = np.zeros((3, 3))
    M[:2, :2], M[:2, 2:] = A, B
    E = expm(M * T)
    Ad, Bd = E[:2, :2], E[:2, 2:]
    K = g * np.array([[Kp, Kd]])
    n = 2 + 2 * d
    Z = np.zeros((n, n))
    Z[:2, :2] = Ad
    if d == 0:
        Z[:2, :2] = Ad - Bd @ K
        return Z
    Z[:2, 2 + 2 * (d - 1): 2 + 2 * d] = -Bd @ K       # usa x[k-d]
    Z[2:4, :2] = np.eye(2)                              # x[k-1] <- x[k]
    for i in range(1, d):
        Z[2 + 2 * i: 4 + 2 * i, 2 + 2 * (i - 1): 2 + 2 * i] = np.eye(2)
    return Z


def radio(g, d):
    return max(abs(np.linalg.eigvals(lazo_retardo(g, d))))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    # (a) proporcional puro
    Acl = A - B @ np.array([[Kp, 0.0]])
    lam = np.linalg.eigvals(Acl)
    w0 = np.sqrt(Kp / J)
    print(f"(a) solo P: polos {lam[0]:.6f}, {lam[1]:.6f}; esperado +-j{w0:.6f}")
    prueba(np.allclose(sorted(lam.imag), [-w0, w0], atol=1e-12) and np.allclose(lam.real, 0, atol=1e-12), "polos de P")
    x0 = np.array([0.1, 0.0])
    amp = [np.hypot(*(expm(Acl * t) @ x0 * np.array([1, 1 / w0]))) for t in (0.0, 50.0, 500.0)]
    print(f"    amplitud normalizada en t = 0, 50, 500 s: {amp[0]:.6f}, {amp[1]:.6f}, {amp[2]:.6f}")
    prueba(abs(amp[2] - amp[0]) < 1e-9, "amplitud constante")

    # (b) PD
    Acl = A - B @ np.array([[Kp, Kd]])
    lam = np.linalg.eigvals(Acl)
    print(f"(b) PD: polos {lam[0]:.4f}, {lam[1]:.4f}; -Kd/(2J) = {-Kd/(2*J):.4f}")
    prueba(np.allclose(lam.real, -Kd / (2 * J), atol=1e-12), "parte real PD")

    # (c) primer orden con realimentación
    for K in (1.0, 9.0):
        polo, T0 = -(1 + K), K / (1 + K)
        print(f"(c) K = {K}: polo {polo}, ganancia estática {T0:.4f}")
    S = 1 / (1 + 9.0)
    T_nom = 9 * 1 / (1 + 9 * 1)
    T_var = 9 * 1.2 / (1 + 9 * 1.2)
    dT = (T_var - T_nom) / T_nom
    print(f"    G0 +20 % -> T cambia {100*dT:.2f} % (primera aproximación S*20 % = {100*S*0.2:.2f} %)")
    prueba(abs(dT - 0.0169) < 5e-4 and dT < 0.2 * S * 1.0001, "desensibilización")

    # (d) retardo en la medida
    print("(d) ganancia máxima estable g_max (escala sobre Kp, Kd) según retardo:")
    gmax = {}
    for d in (0, 1, 2, 4):
        gs = np.linspace(0.05, 40, 4000)
        est = [g for g in gs if radio(g, d) < 1.0]
        gmax[d] = max(est)
        print(f"    retardo {d} muestras ({d*T:.1f} s): g_max ~ {gmax[d]:.2f}")
    prueba(gmax[0] > gmax[1] > gmax[2] > gmax[4], "más retardo, menos ganancia admisible")
    # confirmación por simulación del caso inestable
    g_ins = gmax[2] * 1.2 + 0.5
    Z = lazo_retardo(g_ins, 2)
    z = np.zeros(Z.shape[0]); z[0] = 1e-3
    for _ in range(600):
        z = Z @ z
    print(f"    con g = {g_ins:.2f} y retardo 2: |x| tras 60 s = {np.linalg.norm(z):.3e} (radio {radio(g_ins,2):.3f} > 1)")
    prueba(radio(g_ins, 2) > 1 and np.linalg.norm(z) > 1e-3, "crecimiento")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
