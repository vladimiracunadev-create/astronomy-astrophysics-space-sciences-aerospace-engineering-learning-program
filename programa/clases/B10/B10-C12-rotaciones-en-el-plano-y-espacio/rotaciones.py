#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C12: rotaciones en el plano y alrededor de un eje.

Datos: omega = 7.292115e-5 rad/s (IERS, TN36, tabla 1.2, GRS80, nominal);
radio ecuatorial 6378.137 km (NASA, ficha de la Tierra). La estacion esta en
latitud 30 grados (SINTETICA) sobre una esfera de ese radio.
Modelo: r(t) = Rz(omega t) r0 (rotacion activa del vector de posicion);
v = omega z x r. Supuestos: Tierra esferica y rigida, rotacion uniforme, sin
precesion ni movimiento polar. Validez: horas.
Tolerancia: 1e-12 en ortogonalidad; 1e-9 relativa en la velocidad.
"""
from __future__ import annotations
import platform
import numpy as np

OMEGA = 7.292115e-5
RE = 6378.137


def R2(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s], [s, c]])


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    # plano: propiedades
    a, b = 0.4, 1.1
    assert np.allclose(R2(a) @ R2(b), R2(a + b), atol=1e-12)
    assert np.allclose(R2(a).T @ R2(a), np.eye(2), atol=1e-12)
    assert abs(np.linalg.det(R2(a)) - 1.0) < 1e-12
    assert np.allclose(R2(a).T, R2(-a), atol=1e-12)           # inversa = giro opuesto
    # activa frente a pasiva en el plano
    v = np.array([1.0, 0.0])
    th = np.radians(30)
    print("activa  R(30) v :", (R2(th) @ v).round(6), "| pasiva (coordenadas en ejes girados 30):", (R2(th).T @ v).round(6))

    # estacion a latitud 30 grados
    lat = np.radians(30.0)
    r0 = RE * np.array([np.cos(lat), 0.0, np.sin(lat)])
    for horas in (0.0, 1.0, 6.0, 2 * np.pi / OMEGA / 3600.0):
        t = horas * 3600.0
        r = Rz(OMEGA * t) @ r0
        print(f"t = {horas:9.5f} h: r = {r.round(3)} km, |r| = {np.linalg.norm(r):.6f} km, giro = {np.degrees(OMEGA * t) % 360:.4f} deg")
        assert abs(np.linalg.norm(r) - RE) < 1e-9
    # velocidad por la formula omega z x r y por diferencia central
    t0, dt = 3600.0, 1.0
    r_t = lambda t: Rz(OMEGA * t) @ r0
    v_num = (r_t(t0 + dt) - r_t(t0 - dt)) / (2 * dt)
    v_formula = OMEGA * np.cross([0.0, 0.0, 1.0], r_t(t0))
    print("v (formula) =", (v_formula * 1000).round(6), "m/s |", "v (numerica) =", (v_num * 1000).round(6), "m/s")
    assert np.allclose(v_num, v_formula, rtol=1e-9, atol=1e-12)
    vmod = np.linalg.norm(v_formula) * 1000
    print(f"|v| = {vmod:.4f} m/s; en el ecuador = {OMEGA * RE * 1000:.4f} m/s; razon = {vmod / (OMEGA * RE * 1000):.6f} = cos(lat) = {np.cos(lat):.6f}")
    assert abs(vmod / (OMEGA * RE * 1000) - np.cos(lat)) < 1e-9
    # periodo sideral
    T = 2 * np.pi / OMEGA
    assert np.allclose(Rz(OMEGA * T), np.eye(3), atol=1e-12)
    print(f"periodo sideral = {T:.2f} s = {T / 3600:.5f} h")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
