#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B10-C16: cadena de marcos terrestre-inercial simplificada.

Datos: IERS Conventions (2010), TN36: ec. 5.1 [GCRS] = Q(t) R(t) W(t) [ITRS];
ec. 5.14 ERA(Tu) = 2 pi (0.7790572732640 + 1.00273781191135448 Tu), con
Tu = (JD UT1 - 2451545.0); tabla 1.2 (GRS80): GM = 3.986005e14 m3/s2,
omega = 7.292115e-5 rad/s (nominal). Estaciones y satelites: SINTETICOS.
Modelo SIMPLIFICADO: Q = W = I (sin precesion, nutacion ni movimiento
polar), R = Rz(ERA). Esto NO es la transformacion oficial; es solo el giro.
Supuestos: UT1 conocido; Tierra rigida. Validez: solo ilustrativa; el error
por ignorar precesion, nutacion y movimiento polar NO se evalua aqui (IERS TN36, cap. 5,
describe las matrices Q y W que se omiten).
Tolerancia: 1e-12 en identidades; 1e-6 relativa en la orbita geoestacionaria.
"""
from __future__ import annotations
import platform
import numpy as np

GM = 3.986005e5            # km^3/s^2 (GRS80)
OMEGA = 7.292115e-5        # rad/s (GRS80, nominal)
DIA = 86400.0


def era(Tu):
    """Angulo de rotacion terrestre (rad), IERS TN36 ec. 5.14."""
    return 2 * np.pi * (0.7790572732640 + 1.00273781191135448 * Tu) % (2 * np.pi)


def Rz(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def main():
    print("Python", platform.python_version(), "| numpy", np.__version__)
    e0 = era(0.0)
    print(f"ERA(J2000.0, Tu = 0) = {np.degrees(e0):.6f} grados")
    assert abs(np.degrees(e0) - 0.7790572732640 * 360) < 1e-9
    # tasa de ERA frente a omega nominal
    w_era = 2 * np.pi * 1.00273781191135448 / DIA
    print(f"tasa de ERA = {w_era:.12e} rad/s | omega nominal GRS80 = {OMEGA:.12e} | dif. relativa = {abs(w_era - OMEGA) / OMEGA:.2e}")
    assert abs(w_era - OMEGA) / OMEGA < 2e-6
    T_sid = DIA / 1.00273781191135448
    print(f"dia sideral = {T_sid:.4f} s = {T_sid / 3600:.6f} h")
    print(f"grados por dia solar medio = {360 * 1.00273781191135448:.6f}")

    # estacion fija en el marco terrestre -> marco inercial en dos instantes
    lat, lon = np.radians(30.0), np.radians(0.0)
    a = 6378.137
    r_itrs = a * np.array([np.cos(lat) * np.cos(lon), np.cos(lat) * np.sin(lon), np.sin(lat)])
    for Tu in (0.0, 0.25, 0.5):
        r_ger = Rz(era(Tu)) @ r_itrs
        print(f"Tu = {Tu:4.2f} dias: ERA = {np.degrees(era(Tu)):9.4f} deg; r_GCRS = {r_ger.round(3)} km")
        assert np.allclose(Rz(era(Tu)).T @ r_ger, r_itrs, atol=1e-9)

    # orbita geoestacionaria: velocidad inercial y velocidad en el marco giratorio
    a_geo = (GM * (2 * np.pi / OMEGA) ** 2 / (4 * np.pi ** 2)) ** (1 / 3)
    v_c = np.sqrt(GM / a_geo)
    v_arrastre = OMEGA * a_geo
    print(f"radio geoestacionario = {a_geo:.3f} km; v circular = {v_c:.6f} km/s; omega*a = {v_arrastre:.6f} km/s")
    assert abs(v_c - v_arrastre) / v_c < 1e-9
    t = 1234.5
    ang = OMEGA * t + 0.3
    r_i = a_geo * np.array([np.cos(ang), np.sin(ang), 0.0])
    v_i = v_c * np.array([-np.sin(ang), np.cos(ang), 0.0])
    R = Rz(OMEGA * t)
    r_rot = R.T @ r_i
    wvec = np.array([0.0, 0.0, OMEGA])
    v_rot = R.T @ (v_i - np.cross(wvec, r_i))
    print("posicion en el marco giratorio:", r_rot.round(3), "km; velocidad relativa:", np.abs(v_rot).round(9), "km/s")
    assert np.linalg.norm(v_rot) < 1e-6

    # matriz de estado 6x6 y composicion de marcos
    S = np.block([[R.T, np.zeros((3, 3))], [-(R.T @ (np.array([[0, -OMEGA, 0], [OMEGA, 0, 0], [0, 0, 0]]))), R.T]])
    x_i = np.concatenate([r_i, v_i])
    x_r = S @ x_i
    assert np.allclose(x_r[:3], r_rot, atol=1e-9) and np.allclose(x_r[3:], v_rot, atol=1e-9)
    Rx = lambda b: np.array([[1, 0, 0], [0, np.cos(b), -np.sin(b)], [0, np.sin(b), np.cos(b)]])
    A, B = Rz(0.4), Rx(0.7)
    v0 = np.array([1.0, 2.0, 3.0])
    assert np.allclose(A @ (B @ v0), (A @ B) @ v0, atol=1e-12)
    assert not np.allclose(A @ B, B @ A)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
