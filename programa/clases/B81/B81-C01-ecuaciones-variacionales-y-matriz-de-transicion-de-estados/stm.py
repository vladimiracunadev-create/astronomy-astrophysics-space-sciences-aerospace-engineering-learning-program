#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C01: ecuaciones variacionales y matriz de transicion de estados (dos cuerpos heliocentrico).

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y unidad astronomica = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Estado inicial (ILUSTRATIVO, sintetico): r0 = (1 UA, 0, 0), v0 = (0, v_c*sqrt(1.1), 0) con v_c = sqrt(GM/r0) (excentricidad 0,1); propagacion de 100 d.
Sistema de referencia: inercial heliocentrico plano (x, y, z) con z = 0 en el estado nominal; unidades km, km/s, s.
Modelo: r'' = -GM r/|r|^3. Variacionales: Phi' = A(t) Phi, Phi(t0) = I, con A = [[0, I], [G, 0]] y G = GM (3 r r^T/|r|^5 - I/|r|^3).
Integrador: DOP853 (SciPy) con rtol = 1e-12 y atol = 1e-10 para el estado y 1e-12 para Phi.
Segunda via: diferencias finitas centrales sobre el flujo (perturbaciones de 1 km en posicion y 1e-5 km/s en velocidad).
Tolerancias: error relativo de Phi frente a diferencias finitas < 1e-5; |det Phi - 1| < 1e-8; error simplectico < 1e-8; composicion < 1e-9.
"""
from __future__ import annotations
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp

GM = 132712440041.279419   # km^3/s^2 (JPL SSD)
AU = 149597870.7           # km (JPL SSD)
DIA = 86400.0


def f_aug(t, y):
    r, v = y[:3], y[3:6]
    rn = np.linalg.norm(r)
    a = -GM * r / rn**3
    G = GM * (3.0 * np.outer(r, r) / rn**5 - np.eye(3) / rn**3)
    A = np.zeros((6, 6))
    A[:3, 3:] = np.eye(3)
    A[3:, :3] = G
    phi = y[6:].reshape(6, 6)
    return np.concatenate([v, a, (A @ phi).ravel()])


def f_state(t, y):
    r = y[:3]
    return np.concatenate([y[3:], -GM * r / np.linalg.norm(r)**3])


def flujo(x0, t0, t1):
    s = solve_ivp(f_state, (t0, t1), x0, method="DOP853", rtol=1e-12, atol=1e-10)
    return s.y[:, -1]


def stm(x0, t0, t1):
    y0 = np.concatenate([x0, np.eye(6).ravel()])
    s = solve_ivp(f_aug, (t0, t1), y0, method="DOP853", rtol=1e-12, atol=1e-12)
    y = s.y[:, -1]
    return y[:6], y[6:].reshape(6, 6)


def phi_fd(x0, t0, t1):
    P = np.zeros((6, 6))
    for j in range(6):
        h = 1.0 if j < 3 else 1e-5
        e = np.zeros(6)
        e[j] = h
        P[:, j] = (flujo(x0 + e, t0, t1) - flujo(x0 - e, t0, t1)) / (2 * h)
    return P


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    r0 = AU
    vc = np.sqrt(GM / r0)
    x0 = np.array([r0, 0, 0, 0, vc * np.sqrt(1.1), 0.0])
    T = 100 * DIA
    xf, P = stm(x0, 0.0, T)
    print(f"Estado inicial ILUSTRATIVO: r0 = 1 UA, v0 = {x0[4]:.6f} km/s (e = 0.1); tiempo = 100 d")
    print(f"Estado final: r = ({xf[0]:.1f}, {xf[1]:.1f}, {xf[2]:.1f}) km ; |v| = {np.linalg.norm(xf[3:]):.6f} km/s")
    # (1) diferencias finitas
    Pfd = phi_fd(x0, 0.0, T)
    esc = np.maximum(np.abs(P), 1e-3 * np.abs(P).max(axis=1, keepdims=True))
    err_fd = np.max(np.abs(P - Pfd) / esc)
    print(f"Error relativo maximo de Phi frente a diferencias finitas = {err_fd:.2e}")
    # (2) det y simplectica
    det = np.linalg.det(P)
    J = np.block([[np.zeros((3, 3)), np.eye(3)], [-np.eye(3), np.zeros((3, 3))]])
    simp = np.max(np.abs(P.T @ J @ P - J)) / np.max(np.abs(P)) ** 2
    print(f"det(Phi) - 1 = {det - 1:.2e} ; error simplectico (escalado) = {simp:.2e}")
    # (3) composicion
    tm = 40 * DIA
    xm, P1 = stm(x0, 0.0, tm)
    _, P2 = stm(xm, tm, T)
    comp = np.max(np.abs(P2 @ P1 - P)) / np.max(np.abs(P))
    print(f"Composicion Phi(T,tm) Phi(tm,0) frente a Phi(T,0): error relativo = {comp:.2e}")
    # (4) prediccion lineal de una dispersion
    dx = np.array([100.0, -50.0, 0.0, 1e-4, 2e-4, 0.0])  # 100 km, 50 km, 0.1 y 0.2 m/s
    lin = P @ dx
    real = flujo(x0 + dx, 0.0, T) - xf
    print(f"Dispersion inicial: 100 km, -50 km, 0.1 m/s, 0.2 m/s -> |dr_f| lineal = {np.linalg.norm(lin[:3]):.3f} km ; no lineal = {np.linalg.norm(real[:3]):.3f} km")
    print(f"Error de la prediccion lineal = {np.linalg.norm(lin[:3] - real[:3]):.3e} km")
    print(f"Bloque Phi_rv (km por km/s): sigma_min = {np.linalg.svd(P[:3, 3:], compute_uv=False)[-1]:.3e} ; sigma_max = {np.linalg.svd(P[:3, 3:], compute_uv=False)[0]:.3e}")
    assert err_fd < 1e-5 and abs(det - 1) < 1e-8 and simp < 1e-8 and comp < 1e-9
    assert np.linalg.norm(lin[:3] - real[:3]) < 1e-3 * np.linalg.norm(real[:3])
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
