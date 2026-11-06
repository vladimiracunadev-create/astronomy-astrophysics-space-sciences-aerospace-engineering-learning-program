#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B21-C03: ecuación de Poisson 2D, relajación y multigrid.

Datos: SINTETICOS y adimensionales. Una nube con densidad 4*pi*G*rho = 2 pi^2 sin(pi x) sin(pi y)
en el cuadrado unidad con potencial nulo en la frontera (Dirichlet): el problema
es  -lap(Phi) = f  con  f = -2 pi^2 sin(pi x) sin(pi y)  y solución continua
Phi = -sin(pi x) sin(pi y).
Modelo: ecuación de Poisson discretizada con el estencil de 5 puntos,
(4 u_ij - u_{i+1,j} - u_{i-1,j} - u_{i,j+1} - u_{i,j-1}) / h^2 = f_ij, h = 1/N.
Métodos: Jacobi, Gauss-Seidel rojo-negro y multigrid en ciclo V (2 preajustes y
1 postajuste de Jacobi ponderado con omega = 4/5, restricción de ponderación
completa, prolongación bilineal, malla más gruesa N = 2).
Supuestos: malla uniforme cuadrada, frontera Dirichlet homogénea, doble precisión.
Validez: problema lineal con solución suave; no incluye condiciones de frontera mixtas.
Tolerancias (las pruebas detienen la ejecución si fallan): el multigrid reproduce
la solución discreta exacta (modo a modo) a 1e-10; el error de discretización
tiene orden observado en [1.95, 2.05]; el factor de reducción de Jacobi por
iteración coincide con cos(pi h) a 1e-9; el factor por ciclo V es < 0.30 (variación < 0.05 entre N=16 y 256) y casi
independiente de N.
"""
import math
import platform

import numpy as np

print(f"Python {platform.python_version()}  NumPy {np.__version__}")


def aplicar_A(u, h):
    """Operador discreto (con u de tamaño (N+1)x(N+1), bordes en 0)."""
    r = np.zeros_like(u)
    r[1:-1, 1:-1] = (4 * u[1:-1, 1:-1] - u[2:, 1:-1] - u[:-2, 1:-1]
                     - u[1:-1, 2:] - u[1:-1, :-2]) / h**2
    return r


def residuo(u, f, h):
    r = np.zeros_like(u)
    r[1:-1, 1:-1] = f[1:-1, 1:-1] - aplicar_A(u, h)[1:-1, 1:-1]
    return r


def jacobi(u, f, h, omega=1.0):
    v = u.copy()
    v[1:-1, 1:-1] = (1 - omega) * u[1:-1, 1:-1] + omega * 0.25 * (
        u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] + h**2 * f[1:-1, 1:-1])
    return v


def gs_rojo_negro(u, f, h):
    v = u.copy()
    I, J = np.meshgrid(np.arange(v.shape[0]), np.arange(v.shape[1]), indexing="ij")
    for color in (0, 1):
        m = ((I + J) % 2 == color)
        m[0, :] = m[-1, :] = m[:, 0] = m[:, -1] = False
        nb = np.zeros_like(v)
        nb[1:-1, 1:-1] = v[2:, 1:-1] + v[:-2, 1:-1] + v[1:-1, 2:] + v[1:-1, :-2]
        v[m] = 0.25 * (nb[m] + h**2 * f[m])
    return v


def restringir(r):
    """Ponderación completa (1/16 [1 2 1; 2 4 2; 1 2 1]) sobre los nodos interiores."""
    n = (r.shape[0] - 1) // 2
    rc = np.zeros((n + 1, n + 1))
    s = slice(2, 2 * n - 1, 2)
    rc[1:-1, 1:-1] = (4 * r[s, s]
                      + 2 * (r[3:2 * n:2, s] + r[1:2 * n - 2:2, s] + r[s, 3:2 * n:2] + r[s, 1:2 * n - 2:2])
                      + r[3:2 * n:2, 3:2 * n:2] + r[3:2 * n:2, 1:2 * n - 2:2]
                      + r[1:2 * n - 2:2, 3:2 * n:2] + r[1:2 * n - 2:2, 1:2 * n - 2:2]) / 16
    return rc


def prolongar(ec):
    n = ec.shape[0] - 1
    e = np.zeros((2 * n + 1, 2 * n + 1))
    e[::2, ::2] = ec
    e[1::2, ::2] = 0.5 * (ec[:-1, :] + ec[1:, :])
    e[::2, 1::2] = 0.5 * (ec[:, :-1] + ec[:, 1:])
    e[1::2, 1::2] = 0.25 * (ec[:-1, :-1] + ec[1:, :-1] + ec[:-1, 1:] + ec[1:, 1:])
    return e


def ciclo_v(u, f, h, nu1=2, nu2=1):
    N = u.shape[0] - 1
    if N == 2:
        v = np.zeros_like(u)
        v[1, 1] = h**2 * f[1, 1] / 4
        return v
    for _ in range(nu1):
        u = jacobi(u, f, h, 0.8)
    r = residuo(u, f, h)
    rc = restringir(r)
    ec = ciclo_v(np.zeros_like(rc), rc, 2 * h, nu1, nu2)
    u = u + prolongar(ec)
    for _ in range(nu2):
        u = jacobi(u, f, h, 0.8)
    return u


def norma(r):
    return float(np.sqrt(np.sum(r**2)) * (1.0 / (r.shape[0] - 1)))


def malla(N):
    h = 1.0 / N
    x = np.arange(N + 1) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    return h, X, Y


def lam(p, q, h):
    return 4 / h**2 * (math.sin(p * math.pi * h / 2) ** 2 + math.sin(q * math.pi * h / 2) ** 2)


# (a) solución discreta exacta (modo a modo) y error de discretización
print("(a) error de discretización max|u_h - Phi|, solución del multigrid hasta 1e-13")
errs = []
for N in (16, 32, 64, 128):
    h, X, Y = malla(N)
    f = -2 * math.pi**2 * np.sin(math.pi * X) * np.sin(math.pi * Y)
    # modo adicional de alta frecuencia: solución discreta exacta conocida
    p, q = 5, 7
    f2 = f + np.sin(p * math.pi * X) * np.sin(q * math.pi * Y)
    exacta_disc = f / lam(1, 1, h) + (f2 - f) / lam(p, q, h)
    u = np.zeros_like(f2)
    for _ in range(40):
        u = ciclo_v(u, f2, h)
        if norma(residuo(u, f2, h)) < 1e-13:
            break
    assert np.max(np.abs(u - exacta_disc)) < 1e-10, "solución discreta"
    u1 = np.zeros_like(f)
    for _ in range(40):
        u1 = ciclo_v(u1, f, h)
    err = float(np.max(np.abs(u1 - (-np.sin(math.pi * X) * np.sin(math.pi * Y)))))
    errs.append(err)
    print(f"    N={N:4d}  h={h:.5f}  error = {err:.4e}")
ords = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
print("    orden observado:", " ".join(f"{o:.3f}" for o in ords))
assert all(1.95 <= o <= 2.05 for o in ords)

# (b) relajación: Jacobi y factor de reducción del modo suave
print("(b) Jacobi: error inicial = modo (1,1); razón por iteración frente a cos(pi h)")
for N in (16, 32, 64):
    h, X, Y = malla(N)
    f = -2 * math.pi**2 * np.sin(math.pi * X) * np.sin(math.pi * Y)
    ex = f / lam(1, 1, h)
    u = np.zeros_like(f)
    e_prev = float(np.max(np.abs(u - ex)))
    for _ in range(50):
        u = jacobi(u, f, h)
        e = float(np.max(np.abs(u - ex)))
        razon = e / e_prev
        e_prev = e
    assert abs(razon - math.cos(math.pi * h)) < 1e-9, "razón de Jacobi"
    print(f"    N={N:3d}  razón medida = {razon:.8f}  cos(pi h) = {math.cos(math.pi*h):.8f}")

# (c) suavizado: Jacobi ponderado amortigua lo oscilante, no lo suave
print("(c) una pasada de Jacobi ponderado (omega=0.8) sobre un modo (p,p), N = 32")
N = 32
h, X, Y = malla(N)
for p in (1, 4, 16, 28):
    e0 = np.sin(p * math.pi * X) * np.sin(p * math.pi * Y)
    e1 = jacobi(e0, np.zeros_like(e0), h, 0.8)
    medida = float(np.max(np.abs(e1)) / np.max(np.abs(e0)))
    simbolo = abs(1 - 0.8 + 0.8 * math.cos(p * math.pi * h))
    assert abs(medida - simbolo) < 1e-12
    print(f"    p={p:2d}  factor medido = {medida:.6f}  símbolo = {simbolo:.6f}")

# (d) iteraciones para reducir el residuo en 1e6
print("(d) iteraciones/ciclos para reducir el residuo en un factor 1e6 (cero como estimación inicial)")
for N in (16, 32, 64):
    h, X, Y = malla(N)
    f = -2 * math.pi**2 * np.sin(math.pi * X) * np.sin(math.pi * Y) \
        + np.sin(5 * math.pi * X) * np.sin(7 * math.pi * Y)
    r0 = norma(residuo(np.zeros_like(f), f, h))
    res = {}
    for nombre in ("Jacobi", "GS rojo-negro", "V(2,1)"):
        u = np.zeros_like(f)
        it = 0
        while norma(residuo(u, f, h)) > 1e-6 * r0 and it < 20000:
            u = {"Jacobi": lambda: jacobi(u, f, h),
                 "GS rojo-negro": lambda: gs_rojo_negro(u, f, h),
                 "V(2,1)": lambda: ciclo_v(u, f, h)}[nombre]()
            it += 1
        res[nombre] = it
    print(f"    N={N:3d}  Jacobi = {res['Jacobi']:5d}  GS rojo-negro = {res['GS rojo-negro']:5d}  ciclos V = {res['V(2,1)']:3d}")
    assert res["V(2,1)"] <= 12 and res["Jacobi"] > 8 * res["V(2,1)"]

# (e) factor asintótico por ciclo V
print("(e) factor de reducción del residuo por ciclo V")
facs = []
for N in (16, 32, 64, 128, 256):
    h, X, Y = malla(N)
    f = -2 * math.pi**2 * np.sin(math.pi * X) * np.sin(math.pi * Y) \
        + np.sin(5 * math.pi * X) * np.sin(7 * math.pi * Y)
    u = np.zeros_like(f)
    rs = [norma(residuo(u, f, h))]
    for _ in range(6):
        u = ciclo_v(u, f, h)
        rs.append(norma(residuo(u, f, h)))
    fac = (rs[-1] / rs[-3]) ** 0.5
    facs.append(fac)
    print(f"    N={N:4d}  factor por ciclo = {fac:.4f}")
assert max(facs) < 0.30 and max(facs) - min(facs) < 0.05
print("Pruebas superadas.")
