#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C17: crecimiento lineal de perturbaciones de densidad y escala angular de las BAO.

Datos: H0 = 67.4 km/s/Mpc, Omega_m = 0.315 (Planck 2018, arXiv:1807.06209, resumen, consultado
2026-11-09); escala de las oscilaciones acusticas de bariones ~ 100 h^-1 Mpc (Eisenstein et al.,
astro-ph/0501171, resumen, consultado 2026-11-09); c exacta (NIST CODATA 2022). Las perturbaciones iniciales
(delta = a, delta' = 1 en a = 1e-3) son una condicion ILUSTRATIVA.
Modelo: crecimiento lineal de materia sin presion en un universo plano LambdaCDM:
delta'' + (3/a + E'/E) delta' - (3/2) Om / (a^5 E^2) delta = 0 (derivadas respecto de a), con
E^2 = Om a^-3 + OL. Solucion integral: D(a) = (5 Om/2) E(a) Int_0^a da' / (a' E(a'))^3 (normalizada a D ~ a
en epocas tempranas). Distancia comovil D_C = (c/H0) Int dz/E; EdS: D_C = (2c/H0)(1 - 1/sqrt(1+z)).
Supuestos: perturbaciones lineales, sin radiacion, sin neutrinos masivos. Validez: a >= 1e-3.
Tolerancia: 1e-8 en EdS (D = a); 1e-5 entre ODE e integral en LCDM; 1e-9 en D_C de EdS.
"""
from __future__ import annotations
import math
import platform
import sys

C_KMS = 299792.458
H0, OM = 67.4, 0.315


def E2(a, om):
    return om / a ** 3 + (1 - om)


def crecimiento_ode(om, a_fin=1.0, a0=1e-3, n=40000):
    """RK4 en ln a de delta(a) con delta=a, delta'=1 inicial."""
    def f(x, y):
        a = math.exp(x)
        d, dd = y                      # d = delta, dd = d delta / dx  (x = ln a)
        e2 = E2(a, om)
        dlnE_dlna = -1.5 * om / a ** 3 / e2        # d ln E / d ln a
        # delta_xx + (2 + dlnE/dlna) delta_x - 1.5 om / (a^3 E^2) delta = 0
        return dd, -(2 + dlnE_dlna) * dd + 1.5 * om / (a ** 3 * e2) * d
    x0, x1 = math.log(a0), math.log(a_fin)
    h = (x1 - x0) / n
    y = (a0, a0)                       # delta = a, delta_x = a delta' = a
    x = x0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, (y[0] + h / 2 * k1[0], y[1] + h / 2 * k1[1]))
        k3 = f(x + h / 2, (y[0] + h / 2 * k2[0], y[1] + h / 2 * k2[1]))
        k4 = f(x + h, (y[0] + h * k3[0], y[1] + h * k3[1]))
        y = (y[0] + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6,
             y[1] + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)
        x += h
    return y[0]


def crecimiento_integral(om, a, n=20000):
    def f(s):                           # a' = s^2: da' = 2 s ds ; integrand 1/(a' E)^3
        ap = s * s
        return 2 * s / (ap * math.sqrt(E2(ap, om))) ** 3 if ap > 0 else 0.0
    s1 = math.sqrt(a)
    s0 = 1e-4
    h = (s1 - s0) / n
    tot = f(s0) + f(s1)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(s0 + i * h)
    # contribucion de [0, s0]: E^2 ~ om/a^3 -> integrando ~ a'^(3/2)/om^(3/2) -> Int = (2/5) a^(5/2) / om^(3/2)
    cola = 0.4 * (s0 * s0) ** 2.5 / om ** 1.5
    return 2.5 * om * math.sqrt(E2(a, om)) * (tot * h / 3 + cola)


def dc_mpc(z, om, n=4000):
    h = z / n
    f = lambda zz: 1 / math.sqrt(om * (1 + zz) ** 3 + (1 - om))
    s = f(0) + f(z)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return C_KMS / H0 * s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    d_eds = crecimiento_ode(1.0)
    assert abs(d_eds / 1.0 - 1) < 1e-8, "EdS: delta debe seguir a"
    print(f"Einstein-de Sitter: delta(a=1)/a = {d_eds:.10f} (esperado 1)")
    ode, integral = crecimiento_ode(OM), crecimiento_integral(OM, 1.0)
    assert abs(ode / integral - 1) < 1e-5, "ODE != integral"
    print(f"LCDM (Om = {OM}): D(1) por ODE = {ode:.6f} ; por integral = {integral:.6f}")
    print(f"supresion del crecimiento: D(1)/a = {ode:.4f} (EdS: 1)")
    d05 = crecimiento_integral(OM, 0.5) / integral
    print(f"D(a = 0.5)/D(1) = {d05:.4f} (EdS: 0.5)")
    z = 0.35
    assert abs(dc_mpc(z, 1.0) / (2 * C_KMS / H0 * (1 - 1 / math.sqrt(1 + z))) - 1) < 1e-9
    h = H0 / 100
    r_bao = 100 / h
    dc = dc_mpc(z, OM)
    print(f"escala BAO ~ 100/h = {r_bao:.1f} Mpc comovil ; D_C(z = {z}) = {dc:.1f} Mpc ; angulo = {math.degrees(r_bao / dc):.2f} grados")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
