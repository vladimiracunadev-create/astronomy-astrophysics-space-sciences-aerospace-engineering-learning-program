#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B30-C02: gravedad solar, alturas de escala de las capas y radio sonico de Parker.

Datos: G, k_B, u (NIST CODATA 2022); GM_sol y R_sol (IAU 2015 B3), consultados 2026-11-09. Las temperaturas (5772 K en la fotosfera nominal; 1e4 K y 1.5e6 K
ilustrativas para la cromosfera y la corona) y las masas moleculares medias (1.3, 1.2 y 0.6) son ILUSTRATIVAS.
Modelo: g(r) = GM/r^2; altura de escala H = k_B T/(mu u g); equilibrio hidrostatico isotermo con gravedad variable P(r)/P(R) = exp[-(GM mu u/(k_B T))(1/R - 1/r)]
comparado con la integracion numerica de dP/dr = -rho g; presion en el infinito de una corona hidrostatica P(inf)/P(R) = exp(-GM mu u/(k_B T R)) (argumento de Parker);
velocidad del sonido isotermo c_s = sqrt(k_B T/(mu u)); radio sonico r_c = GM/(2 c_s^2).
Supuestos: capas isotermas y esfericas. Validez: orden de magnitud.
Tolerancia: integracion numerica de la presion frente a la forma cerrada con 1e-6 relativo.
"""
from __future__ import annotations
import math
import platform
import sys

G, KB, U = 6.67430e-11, 1.380649e-23, 1.66053906892e-27
GM_SOL, R_SOL = 1.3271244e20, 6.957e8


def altura_escala(t, mu, g):
    return KB * t / (mu * U * g)


def presion_numerica(r0, r1, t, mu, n=20000):
    """ln(P(r1)/P(r0)) = -(mu u/(k T)) Int g dr con g = GM/r^2, por Simpson."""
    h = (r1 - r0) / n
    f = lambda r: GM_SOL / r ** 2
    s = f(r0) + f(r1)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(r0 + i * h)
    return -(mu * U / (KB * t)) * s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    g = GM_SOL / R_SOL ** 2
    print(f"gravedad en la superficie nominal g = GM/R^2 = {g:.3f} m/s2 (la de la Tierra es 9.80)")
    print(f"{'capa (ilustrativa)':<22} {'T [K]':>10} {'mu':>5} {'H [km]':>10} {'c_s [km/s]':>11} {'r_c [R_sol]':>12}")
    capas = (("fotosfera", 5772.0, 1.3), ("cromosfera", 1.0e4, 1.2), ("corona", 1.5e6, 0.6))
    for nombre, t, mu in capas:
        h = altura_escala(t, mu, g)
        cs = math.sqrt(KB * t / (mu * U))
        rc = GM_SOL / (2 * cs ** 2)
        print(f"{nombre:<22} {t:10.4g} {mu:5.1f} {h / 1e3:10.1f} {cs / 1e3:11.2f} {rc / R_SOL:12.3f}")
    # equilibrio hidrostatico con gravedad variable
    t, mu = 1.5e6, 0.6
    print(f"{'r [R_sol]':>10} {'P/P_0 (cerrada)':>16} {'P/P_0 (numerica)':>17}")
    for x in (1.0, 1.5, 2.0, 5.0, 20.0):
        r = x * R_SOL
        cerrada = math.exp(-(GM_SOL * mu * U / (KB * t)) * (1 / R_SOL - 1 / r))
        numerica = math.exp(presion_numerica(R_SOL, r, t, mu)) if x > 1 else 1.0
        if x > 1:
            assert abs(numerica / cerrada - 1) < 1e-6, f"presion en r={x}"
        print(f"{x:10.1f} {cerrada:16.5e} {numerica:17.5e}")
    p_inf = math.exp(-GM_SOL * mu * U / (KB * t * R_SOL))
    print(f"corona hidrostatica de 1.5e6 K: P(infinito)/P(R_sol) = {p_inf:.4e} (no se anula: una corona estatica no puede conectar con un medio de presion ~0)")
    # masa de columna por encima de la fotosfera
    h = altura_escala(5772.0, 1.3, g)
    n, zmax = 4000, 20 * h
    s = 1 + math.exp(-zmax / h)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * math.exp(-i * zmax / n / h)
    col = s * zmax / n / 3
    print(f"columna de densidad exponencial: Int exp(-z/H) dz / H = {col / h:.6f} (esperado 1 - e^-20 = {1 - math.exp(-20):.6f})")
    assert abs(col / h - (1 - math.exp(-20))) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
