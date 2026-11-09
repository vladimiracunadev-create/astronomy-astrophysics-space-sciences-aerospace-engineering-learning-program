#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C17: factor de Lorentz, colimacion y retardo de llegada de una explosion de rayos gamma.

Datos: c (NIST CODATA 2022), 1 au (IERS TN36, Tabla 1.1), consultados 2026-11-09. GW170817/GRB 170817A: retardo de
1.74 +/- 0.05 s entre la onda gravitacional y los rayos gamma (LIGO/Virgo/Fermi/INTEGRAL, arXiv:1710.05834, resumen) y
distancia de 40 Mpc (arXiv:1710.05832, resumen). Los factores de Lorentz, el radio de emision, la energia isotropica
y el semiangulo del chorro son ILUSTRATIVOS (sinteticos).
Modelo: capa que emite a un radio R con factor de Lorentz Gamma. Retardo de llegada frente a un foton emitido
en el centro: dt = R (1 - beta)/(beta c), con 1 - beta = 1/(Gamma^2 (1 + beta)); aproximacion R/(2 Gamma^2 c).
Colimacion: E_gamma = f_b E_iso, f_b = 1 - cos(theta_j). Cota de velocidad: |v_g - c|/c < dt/(d/c) si la emision
no se retrasa (cota superior sencilla; no se toma como medicion).
Supuestos: capa esferica fina, emision instantanea, sin cosmologia. Validez: Gamma >> 1.
Tolerancia: 1e-3 entre el retardo exacto y la aproximacion para Gamma >= 100.
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
AU = 1.49597870700e11
PC = 648000 / math.pi * AU
MPC = 1e6 * PC


def retardo_exacto(r, gamma):
    beta = math.sqrt(1 - 1 / gamma ** 2)
    um = 1 / (gamma ** 2 * (1 + beta))
    return r * um / (beta * C)


def retardo_aprox(r, gamma):
    return r / (2 * gamma ** 2 * C)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = 1e15
    print(f"1 pc = {PC:.6e} m ; 1 Mpc = {MPC:.6e} m")
    print(f"{'Gamma':>7} {'retardo exacto [s]':>20} {'aproximacion [s]':>18} {'cociente':>10}")
    for g in (100.0, 300.0, 1000.0):
        e, a = retardo_exacto(r, g), retardo_aprox(r, g)
        assert abs(e / a - 1) < 1e-3, "aproximacion del retardo"
        print(f"{g:7.0f} {e:20.6f} {a:18.6f} {e / a:10.6f}")
    # inversion: dado un retardo, el radio de emision
    g, dt = 300.0, 1.0
    r_dt = dt * 2 * g ** 2 * C
    print(f"retardo de {dt} s con Gamma = {g:.0f}: R = {r_dt:.4e} m = {r_dt / AU:.1f} au")
    assert abs(retardo_exacto(r_dt, g) / dt - 1) < 1e-3
    # colimacion
    e_iso = 1e47
    print(f"{'theta_j [rad]':>14} {'f_b':>10} {'E_gamma [J]':>13}")
    for th in (0.02, 0.05, 0.1, 0.3):
        fb = 1 - math.cos(th)
        print(f"{th:14.2f} {fb:10.3e} {e_iso * fb:13.3e}")
    assert abs((1 - math.cos(0.1)) - 4.99583e-3) < 1e-8
    # GW170817 / GRB 170817A
    d = 40 * MPC
    t_viaje = d / C
    dt_obs = 1.74
    print(f"40 Mpc = {d:.4e} m ; tiempo de viaje de la luz = {t_viaje:.4e} s = {t_viaje / (365.25 * 86400) / 1e6:.1f} Ma")
    print(f"cota |v_g - c|/c < {dt_obs / t_viaje:.2e} (retardo 1.74 s entre {t_viaje:.3e} s)")
    print(f"con la incertidumbre de 0.05 s: {(dt_obs - 0.05) / t_viaje:.2e} .. {(dt_obs + 0.05) / t_viaje:.2e}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
