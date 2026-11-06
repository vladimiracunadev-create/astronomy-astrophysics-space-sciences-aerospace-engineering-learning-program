#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C17: ecuaciones de Euler, inestabilidad del eje intermedio y Lyapunov.

Datos: SINTÉTICOS. Cuerpo rígido con inercias principales J = (50, 40, 30) kg m^2.
Modelo: J w' = -w x (J w) + u  (ecuaciones de Euler, sistema del cuerpo).
Referencias independientes:
  (1) sin par: se conservan la energía T = (1/2) w.J w y el módulo del momento
      angular |J w| (invariantes exactos);
  (2) giro alrededor del eje intermedio (J2 = 40) con velocidad Omega: la
      linealización da una perturbación que crece con la tasa
      lambda = Omega sqrt((J2-J3)(J1-J2)/(J1 J3)); se contrasta con el ajuste
      del crecimiento en la simulación no lineal;
  (3) cuerpo isótropo J = 40 I con u = -k w: solución exacta w(t) = w0 exp(-k t/J);
  (4) Lyapunov: V = (1/2) w.J w cumple V' = -k |w|^2 <= 0 con u = -k w.
Supuestos: cuerpo rígido, par exacto, sin saturación. Tolerancia: 1e-9 relativa
en los invariantes (DOP853, rtol 1e-12); 3 % en la tasa de crecimiento.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp

J = np.diag([50.0, 40.0, 30.0])


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def euler(t, w, Jm, k):
    return np.linalg.solve(Jm, -np.cross(w, Jm @ w) - k * w)


def integra(w0, T, Jm=J, k=0.0, n=4001):
    t = np.linspace(0, T, n)
    s = solve_ivp(euler, [0, T], w0, args=(Jm, k), t_eval=t, method="DOP853", rtol=1e-12, atol=1e-14)
    return t, s.y


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}  scipy {scipy.__version__}")
    # (1) invariantes sin par
    w0 = np.array([0.10, 0.05, -0.08])
    t, w = integra(w0, 200.0)
    E = 0.5 * np.einsum("it,ij,jt->t", w, J, w)
    H = np.linalg.norm(J @ w, axis=0)
    dE, dH = np.ptp(E) / E[0], np.ptp(H) / H[0]
    print(f"sin par, 200 s: variación relativa de la energía {dE:.2e}, del |H| {dH:.2e}")
    prueba(dE < 1e-9 and dH < 1e-9, "invariantes")

    # (2) eje intermedio
    Om, eps = 0.2, 1e-6
    lam = Om * math.sqrt((40 - 30) * (50 - 40) / (50 * 30))
    t, w = integra(np.array([eps, Om, eps]), 300.0, n=12001)
    amp = np.hypot(w[0], w[2])
    mask = (t > 20) & (t < 150)
    pend = np.polyfit(t[mask], np.log(amp[mask]), 1)[0]
    print(f"eje intermedio: tasa linealizada {lam:.5f} s^-1; tasa ajustada {pend:.5f} s^-1 "
          f"({100*abs(pend-lam)/lam:.2f} % de diferencia)")
    prueba(abs(pend - lam) < 0.03 * lam, "tasa de crecimiento")
    print(f"   amplitud transversal: {amp[0]:.1e} rad/s al inicio, máx {amp.max():.3f} rad/s en 300 s (el modelo lineal deja de valer)")
    # ejes extremos: estables
    for eje, nombre in ((0, "mayor (J=50)"), (2, "menor (J=30)")):
        w00 = np.full(3, eps); w00[eje] = Om
        t, w = integra(w00, 100.0, n=2001)
        otros = [i for i in range(3) if i != eje]
        print(f"   giro estable alrededor del eje {nombre}: |w_perp| máx = {np.abs(w[otros]).max():.2e} rad/s")
        prueba(np.abs(w[otros]).max() < 1e-4, "ejes extremos estables")

    # (3) isótropo
    Jiso = 40.0 * np.eye(3); k = 8.0
    t, w = integra(w0, 60.0, Jm=Jiso, k=k)
    ex = np.outer(w0, np.exp(-k * t / 40.0))
    err = np.max(np.abs(w - ex))
    print(f"cuerpo isótropo con u = -k w: error máx frente a w0 exp(-k t/J) = {err:.2e} rad/s")
    prueba(err < 1e-10, "solución exacta isótropa")

    # (4) Lyapunov en el cuerpo con inercias distintas
    k = 8.0
    t, w = integra(w0, 120.0, k=k, n=12001)
    V = 0.5 * np.einsum("it,ij,jt->t", w, J, w)
    Vdot_num = np.gradient(V, t)
    Vdot_teo = -k * np.sum(w**2, axis=0)
    err = np.max(np.abs(Vdot_num[2:-2] - Vdot_teo[2:-2]))
    mono = np.all(np.diff(V) <= 1e-18)
    print(f"Lyapunov: V monótona decreciente = {mono}; max|dV/dt numérica - (-k|w|^2)| = {err:.2e}")
    print(f"   V(0) = {V[0]:.5f} J, V(120 s) = {V[-1]:.3e} J; |w| final = {np.linalg.norm(w[:, -1]):.2e} rad/s")
    prueba(mono and err < 5e-7, "Lyapunov")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
