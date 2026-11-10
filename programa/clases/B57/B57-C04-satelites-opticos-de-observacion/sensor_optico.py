#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C04: sensor optico espacial: difraccion, fotones y SNR.

Datos: altitud 705 km, GSD 30 m y barrido 185 km de Landsat 8 (USGS, consultada 2026-11-09). Todo lo demas es ILUSTRATIVO:
apertura 0.10 m, transmision 0.7, eficiencia cuantica 0.8, ancho de banda 0.03 um, radiancia 50 W m^-2 sr^-1 um^-1 (no es la
de ninguna escena observada). GM = 3.986004418e14 m^3 s^-2 y R = 6378.137 km (valores de referencia WGS84, no consultados en la sesion).
Modelo: orbita circular; velocidad sobre el suelo = v_orb R/(R+H); tiempo de integracion = GSD / v_suelo (barredor); fotones =
L dlambda A Omega tau t / (h c / lambda); Poisson con semilla fija 57; criterio de Rayleigh para el limite de difraccion.
Validez: ilustrativa, sin ruido de lectura ni corriente oscura. Tolerancia: SNR simulada frente a sqrt(N) < 2 %.
Requiere numpy.
"""
import math, platform
import numpy as np

H_PL, C_LUZ = 6.62607015e-34, 299792458.0
GM, R_T = 3.986004418e14, 6378137.0
H, GSD = 705e3, 30.0
D, TAU, QE = 0.10, 0.7, 0.8
LAM, DLAM, L_UM = 0.865e-6, 0.03, 50.0  # DLAM en um; L en W m^-2 sr^-1 um^-1


def calcular():
    r = {}
    v_orb = math.sqrt(GM / (R_T + H))
    v_suelo = v_orb * R_T / (R_T + H)
    r["v_orb"], r["v_suelo"] = v_orb / 1e3, v_suelo / 1e3
    r["t_int_ms"] = GSD / v_suelo * 1e3
    ifov = GSD / H
    area = math.pi * (D / 2) ** 2
    omega = ifov**2
    r["etendue"] = area * omega
    potencia = L_UM * DLAM * area * omega * TAU
    foton = H_PL * C_LUZ / LAM
    n_fot = potencia / foton * (r["t_int_ms"] * 1e-3)
    n_e = n_fot * QE
    r["n_electrones"] = n_e
    r["snr_teo"] = math.sqrt(n_e)
    rng = np.random.default_rng(57)
    muestras = rng.poisson(n_e, 200000)
    r["snr_sim"] = float(muestras.mean() / muestras.std())
    r["gsd_difrac"] = 1.22 * LAM * H / D
    r["d_min_30m"] = 1.22 * LAM * H / GSD * 1e3
    r["F_numero_30"] = 1.0
    r["razon_sim_snr"] = r["snr_sim"] / r["snr_teo"]
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Velocidad orbital = {r['v_orb']:.3f} km/s ; velocidad sobre el suelo = {r['v_suelo']:.3f} km/s ; tiempo de integracion por pixel = {r['t_int_ms']:.3f} ms")
    print(f"Etendue A*Omega = {r['etendue']:.3e} m^2 sr")
    print(f"Electrones por pixel = {r['n_electrones']:.3e} ; SNR de fotones teorica = {r['snr_teo']:.1f} ; simulada = {r['snr_sim']:.1f}")
    print(f"Limite de difraccion (Rayleigh, D = 0.10 m, 0.865 um) = {r['gsd_difrac']:.3f} m en el suelo ; apertura minima para 30 m = {r['d_min_30m']:.1f} mm")
    assert abs(r["razon_sim_snr"] - 1) < 0.02
    assert r["gsd_difrac"] < GSD
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
