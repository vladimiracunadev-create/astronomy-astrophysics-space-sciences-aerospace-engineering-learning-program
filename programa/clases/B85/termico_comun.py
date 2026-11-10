# SPDX-License-Identifier: Apache-2.0
"""Biblioteca común de los laboratorios del bloque B85 (solo biblioteca estándar).

Constantes consultadas (2026-11-10):
  SIGMA  constante de Stefan-Boltzmann, NIST CODATA 2022 (valor exacto).
  S0     irradiancia solar a 1 UA, NASA/NSSDC Earth Fact Sheet.
  ALBEDO albedo de Bond de la Tierra, NASA/NSSDC Earth Fact Sheet.
  T_BB_E temperatura de cuerpo negro de la Tierra, NASA/NSSDC Earth Fact Sheet.
  R_E, G_E radio medio y gravedad media de la Tierra, NASA/NSSDC Earth Fact Sheet.
Todo lo demás (propiedades de materiales, flujos, coeficientes) es ILUSTRATIVO y lo rotula cada script.
"""
import math
import sys

SIGMA = 5.670374419e-8      # W m^-2 K^-4
S0 = 1361.0                 # W m^-2
ALBEDO = 0.294              # adimensional
T_BB_E = 254.0              # K
R_E = 6371.0e3              # m
G_E = 9.820                 # m s^-2
K_B = 1.380649e-23          # J/K (SI exacto)
H_P = 6.62607015e-34        # J s (SI exacto)
C_L = 299792458.0           # m/s (SI exacto)
E_Q = 1.602176634e-19       # C (SI exacto)
YEAR = 365.25 * 86400.0     # s
CERO_C = 273.15             # K


def cabecera():
    v = sys.version_info
    print(f"Python {v.major}.{v.minor}.{v.micro} (biblioteca estandar)")


def comprobar(condicion, mensaje):
    if not condicion:
        raise AssertionError(mensaje)


def fin():
    print("Pruebas superadas.")


def biseccion(f, a, b, tol=1e-12, it=300):
    fa, fb = f(a), f(b)
    comprobar(fa * fb <= 0, "la biseccion necesita un cambio de signo")
    for _ in range(it):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
        if abs(b - a) < tol * max(1.0, abs(m)):
            break
    return 0.5 * (a + b)


def newton(f, df, x0, tol=1e-12, it=100):
    x = x0
    for _ in range(it):
        dx = f(x) / df(x)
        x -= dx
        if abs(dx) < tol * max(1.0, abs(x)):
            return x
    raise RuntimeError("Newton no converge")


def resolver_lineal(A, b):
    """Gauss con pivote parcial; A es lista de listas, b lista."""
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][c] * x[c] for c in range(i + 1, n))) / M[i][i]
    return x


def factor_forma_esfera_tierra(h):
    """Factor de forma de una esfera a la Tierra (esfera) a la altura h [m]."""
    rho = R_E / (R_E + h)
    return 0.5 * (1.0 - math.sqrt(1.0 - rho * rho))
