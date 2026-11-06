#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C14: angulos de Euler 3-2-1 y bloqueo de cardan.

Datos: SINTETICOS (angulos inventados).
Modelo: R = Rz(psi) Ry(theta) Rx(phi) (activa; cuerpo -> inercial), con
phi = alabeo (x), theta = cabeceo (y), psi = guinada (z). Extraccion:
theta = -asin(R[2,0]), phi = atan2(R[2,1], R[2,2]), psi = atan2(R[1,0], R[0,0]).
Relacion con la velocidad angular del cuerpo w (formulas estandar):
phi' = wx + (wy sin phi + wz cos phi) tan theta; theta' = wy cos phi - wz sin phi;
psi' = (wy sin phi + wz cos phi)/cos theta.
Supuestos: secuencia 3-2-1 fija. Validez: |theta| < 90 grados.
Tolerancia: 1e-12 en la ida y vuelta lejos de la singularidad.
"""
from __future__ import annotations
import platform
import numpy as np


def Rx(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def Ry(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def desde_euler(phi, theta, psi):
    return Rz(psi) @ Ry(theta) @ Rx(phi)


def a_euler(R):
    theta = -np.arcsin(np.clip(R[2, 0], -1, 1))
    phi = np.arctan2(R[2, 1], R[2, 2])
    psi = np.arctan2(R[1, 0], R[0, 0])
    return phi, theta, psi


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    d = np.radians
    phi, theta, psi = d(20), d(30), d(40)
    R = desde_euler(phi, theta, psi)
    print("R(20,30,40) =\n", R.round(6))
    p2 = a_euler(R)
    print("ida y vuelta (grados):", np.degrees(p2).round(9))
    assert np.allclose(p2, (phi, theta, psi), atol=1e-12)

    # 1. bloqueo de cardan: theta = 90 grados
    th = d(90)
    R1 = desde_euler(d(10), th, d(50))      # psi - phi = 40
    R2 = desde_euler(d(30), th, d(70))      # psi - phi = 40
    R3 = desde_euler(d(10), th, d(60))      # psi - phi = 50
    print("(10,90,50) y (30,90,70) dan la misma R?", np.allclose(R1, R2, atol=1e-12))
    print("(10,90,50) y (10,90,60) dan la misma R?", np.allclose(R1, R3, atol=1e-12))
    assert np.allclose(R1, R2, atol=1e-12) and not np.allclose(R1, R3, atol=1e-6)

    # 2. error de extraccion al acercarse a la singularidad
    rng = np.random.default_rng(14)
    E = 1e-8 * rng.normal(size=(3, 3))
    print("theta (deg)   1/cos(theta)   error angular maximo tras perturbar R en 1e-8")
    for tdeg in (0, 60, 80, 89, 89.9, 89.99):
        Rt = desde_euler(d(25), d(tdeg), d(35))
        ang0 = np.array(a_euler(Rt))
        ang1 = np.array(a_euler(Rt + E))
        dif = np.abs(np.angle(np.exp(1j * (ang1 - ang0)))).max()
        print(f"{tdeg:8.2f}   {1 / np.cos(d(tdeg)):12.2f}   {dif:.3e} rad")

    # 3. velocidad angular del cuerpo frente a las tasas de Euler
    ph, th, ps = d(20), d(30), d(40)
    rates = np.array([0.02, -0.01, 0.03])      # phi', theta', psi' en rad/s
    h = 1e-6
    f = lambda s: desde_euler(ph + s * rates[0], th + s * rates[1], ps + s * rates[2])
    Rdot = (f(h) - f(-h)) / (2 * h)
    W = desde_euler(ph, th, ps).T @ Rdot       # antisimetrica: omega en ejes del cuerpo
    w = np.array([W[2, 1], W[0, 2], W[1, 0]])
    print("omega cuerpo (rad/s) =", w.round(8))
    phid = w[0] + (w[1] * np.sin(ph) + w[2] * np.cos(ph)) * np.tan(th)
    thed = w[1] * np.cos(ph) - w[2] * np.sin(ph)
    psid = (w[1] * np.sin(ph) + w[2] * np.cos(ph)) / np.cos(th)
    print("tasas de Euler recuperadas:", np.array([phid, thed, psid]).round(8))
    assert np.allclose([phid, thed, psid], rates, atol=1e-8)
    # tasas necesarias cerca de la singularidad para el mismo w
    for tdeg in (60, 85, 89, 89.9):
        t_ = d(tdeg)
        psid_ = (w[1] * np.sin(ph) + w[2] * np.cos(ph)) / np.cos(t_)
        print(f"theta = {tdeg:5.1f} deg: psi' necesaria = {psid_: .4f} rad/s (misma omega del cuerpo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
