#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C13: edad y expansion de un universo plano LambdaCDM (Friedmann).

Datos: H0 = 67.4 km/s/Mpc y Omega_m = 0.315 (Planck 2018, arXiv:1807.06209, resumen, consultado
2026-11-09); G (NIST CODATA 2022); 1 au (IERS TN36, Tabla 1.1) para pasar Mpc a m. Se desprecia la radiacion
(Omega_r ~ 9e-5, calculada en B26-C14) y la curvatura.
Modelo: H(a)^2 = H0^2 (Om a^-3 + OL), OL = 1 - Om. Edad t0 = Int_0^1 da / (a H(a)); solucion cerrada
t0 = 2 asinh(sqrt(OL/Om)) / (3 H0 sqrt(OL)); factor de escala a(t) = (Om/OL)^(1/3) sinh(1.5 sqrt(OL) H0 t)^(2/3).
Densidad critica rho_c = 3 H0^2 / (8 pi G). Parametro de deceleracion q0 = Om/2 - OL; transicion a la
aceleracion en (1 + z_t)^3 = 2 OL / Om.
Supuestos: universo plano, homogeneo e isotropo, materia sin presion y constante cosmologica. Validez: z << 3000.
Tolerancia: 1e-9 entre la cuadratura y la forma cerrada de la edad; 1e-7 entre RK4 y a(t) analitico.
"""
from __future__ import annotations
import math
import platform
import sys

G = 6.67430e-11
AU = 1.49597870700e11
MPC_M = 1e6 * (648000 / math.pi) * AU
YR = 365.25 * 86400.0
MP = 1.67262192595e-27


def h0_si(h0_kms_mpc):
    return h0_kms_mpc * 1e3 / MPC_M


def edad_cerrada(h0, om):
    ol = 1 - om
    if ol == 0:
        return 2 / (3 * h0)
    return 2 * math.asinh(math.sqrt(ol / om)) / (3 * h0 * math.sqrt(ol))


def edad_cuadratura(h0, om, n=20000):
    ol = 1 - om
    # con a = s^2 el integrando 1/(a H) da = 2 s^2 / (H0 sqrt(om + ol s^6)) ds es suave en s = 0
    f = lambda s: 2 * s * s / (h0 * math.sqrt(om + ol * s ** 6))
    h = 1.0 / n
    s = f(0.0) + f(1.0)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return s * h / 3


def a_analitico(t, h0, om):
    ol = 1 - om
    return (om / ol) ** (1 / 3) * math.sinh(1.5 * math.sqrt(ol) * h0 * t) ** (2 / 3)


def a_rk4(t_fin, h0, om, a0=0.1, n=20000):
    """Integra da/dt = a H(a) desde a0 con RK4 en el tiempo; a0 se toma de la solucion en el tiempo inicial."""
    ol = 1 - om
    f = lambda a: a * h0 * math.sqrt(om / a ** 3 + ol)
    # tiempo inicial consistente con a0 (inversion de la forma cerrada)
    t0 = math.asinh((a0 / (om / ol) ** (1 / 3)) ** 1.5) / (1.5 * math.sqrt(ol) * h0)
    h, a = (t_fin - t0) / n, a0
    for _ in range(n):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h0, om = h0_si(67.4), 0.315
    ol = 1 - om
    t_cer, t_num = edad_cerrada(h0, om), edad_cuadratura(h0, om)
    assert abs(t_num / t_cer - 1) < 1e-9, "cuadratura != forma cerrada"
    assert abs(edad_cuadratura(h0, 1.0) / (2 / (3 * h0)) - 1) < 1e-9, "Einstein-de Sitter"
    print(f"H0 = {h0:.5e} s^-1 ; 1/H0 = {1 / h0 / YR / 1e9:.3f} Gyr")
    print(f"edad (LCDM plano, Om = 0.315): cerrada = {t_cer / YR / 1e9:.4f} Gyr ; cuadratura = {t_num / YR / 1e9:.4f} Gyr")
    print(f"edad (Einstein-de Sitter, Om = 1) = {2 / (3 * h0) / YR / 1e9:.4f} Gyr")
    t_obj = t_cer
    a1, a2 = a_rk4(t_obj, h0, om), a_analitico(t_obj, h0, om)
    assert abs(a1 / a2 - 1) < 1e-6, "RK4 != a(t) analitico"
    print(f"a(t0): RK4 = {a1:.8f} ; analitico = {a2:.8f}")
    rho_c = 3 * h0 ** 2 / (8 * math.pi * G)
    print(f"rho_c = {rho_c:.4e} kg/m3 = {rho_c / MP:.2f} masas de proton por m3")
    q0 = om / 2 - ol
    zt = (2 * ol / om) ** (1 / 3) - 1
    lo, hi = 0.0, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if om * (1 + mid) ** 3 / 2 > ol:         # (1+z)^3 Om / 2 = OL  <=>  addot = 0
            hi = mid
        else:
            lo = mid
    assert abs(0.5 * (lo + hi) - zt) < 1e-9
    print(f"q0 = {q0:.4f} ; transicion a la aceleracion en z = {zt:.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
