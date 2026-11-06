#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C15: elementos finitos lineales en una dimensión.

Datos SINTÉTICOS: placa de espesor L = 0.1 m con generación interna uniforme
q = 1.0e4 W/m3, conductividad k = 2.0 W/(m K) y temperatura de pared
T_w = 300 K en ambos lados (valores de ejemplo, no de un material real).
Modelo: -k T'' = q en (0, L), T(0) = T(L) = T_w. Solución exacta
T = T_w + q x (L - x) / (2 k). Segundo caso adimensional: -u'' = pi^2 sin(pi x),
u(0) = u(1) = 0, con solución exacta sin(pi x).
Método: forma débil, funciones de base lineales a trozos ("sombrero"), malla uniforme
de N elementos, ensamblaje de la matriz de rigidez K_ij = ∫ phi_i' phi_j' dx y del
vector de carga b_i = ∫ f phi_i dx (cuadratura de Gauss de 3 puntos por elemento),
solución con eliminación tridiagonal.
Supuestos: coeficientes constantes. Validez: soluciones suaves.
Tolerancia: para f constante los valores nodales son exactos (< 1e-12 relativo);
para f = pi^2 sin(pi x) el error en norma L2 baja con orden 2 (razón de errores
en [3.5, 4.5]) y el error en la seminorma H1 con orden 1 (razón en [1.8, 2.2]).
"""
import math, platform
import numpy as np

GP = np.array([-math.sqrt(3 / 5), 0.0, math.sqrt(3 / 5)])
GW = np.array([5 / 9, 8 / 9, 5 / 9])


def resolver(N, f, a=0.0, b=1.0):
    h = (b - a) / N
    x = a + h * np.arange(N + 1)
    n = N - 1                                   # incógnitas interiores
    diag = np.full(n, 2.0 / h)
    off = np.full(n - 1, -1.0 / h)
    # carga: el nodo i (1..N-1) recibe del elemento i-1 (sombrero que sube) y del elemento i (sombrero que baja)
    rhs = np.zeros(n)
    for e in range(N):
        xl, xr = x[e], x[e + 1]
        xm, hw = 0.5 * (xl + xr), 0.5 * h
        for g, w in zip(GP, GW):
            xx = xm + hw * g
            fx = f(xx)
            if e + 1 <= N - 1:                  # nodo derecho e+1 es interior
                rhs[e] += w * hw * fx * (xx - xl) / h
            if e >= 1:                          # nodo izquierdo e es interior
                rhs[e - 1] += w * hw * fx * (xr - xx) / h
    # eliminación tridiagonal (Thomas)
    c = off.copy(); d = rhs.copy(); bb = diag.copy()
    for i in range(1, n):
        wgt = off[i - 1] / bb[i - 1]
        bb[i] -= wgt * c[i - 1]
        d[i] -= wgt * d[i - 1]
    u = np.zeros(n)
    u[-1] = d[-1] / bb[-1]
    for i in range(n - 2, -1, -1):
        u[i] = (d[i] - c[i] * u[i + 1]) / bb[i]
    return x, np.concatenate(([0.0], u, [0.0]))


def errores(x, u, exacta, dexacta):
    N = len(x) - 1
    h = x[1] - x[0]
    e2 = 0.0
    e1 = 0.0
    for e in range(N):
        xm, hw = 0.5 * (x[e] + x[e + 1]), 0.5 * h
        for g, w in zip(GP, GW):
            xx = xm + hw * g
            uh = u[e] + (u[e + 1] - u[e]) * (xx - x[e]) / h
            duh = (u[e + 1] - u[e]) / h
            e2 += w * hw * (uh - exacta(xx)) ** 2
            e1 += w * hw * (duh - dexacta(xx)) ** 2
    return math.sqrt(e2), math.sqrt(e1)


print(f"Python {platform.python_version()}; NumPy {np.__version__}")

# placa con generación interna (valores nodales exactos)
Lp, q, k, Tw = 0.1, 1.0e4, 2.0, 300.0
# escalado: -k T'' = q  -> T = Tw + (q/k) * v, con -v'' = 1 en (0, L)
x, v = resolver(4, lambda s: 1.0, 0.0, Lp)
T = Tw + (q / k) * v
Tex = Tw + q * x * (Lp - x) / (2 * k)
print("placa, N=4: x (m) =", np.round(x, 4), "\n            T (K) =", np.round(T, 4), "\n          exacto  =", np.round(Tex, 4))
print(f"  temperatura máxima = {T.max():.4f} K (exacta {Tw + q*Lp**2/(8*k):.4f} K)")
assert np.max(np.abs(T - Tex)) / 300.0 < 1e-12

# convergencia con f = pi^2 sin(pi x)
f = lambda s: math.pi**2 * math.sin(math.pi * s)
ex = lambda s: math.sin(math.pi * s)
dex = lambda s: math.pi * math.cos(math.pi * s)
E2, E1, En = [], [], []
for N in (4, 8, 16, 32, 64):
    x, u = resolver(N, f)
    e2, e1 = errores(x, u, ex, dex)
    en = float(np.max(np.abs(u - np.sin(np.pi * x))))
    E2.append(e2); E1.append(e1); En.append(en)
    print(f"N={N:3d} h={1/N:.5f}: error L2 = {e2:.4e}  error H1 (seminorma) = {e1:.4e}  error nodal máx = {en:.4e}")
r2 = [E2[i] / E2[i + 1] for i in range(4)]
r1 = [E1[i] / E1[i + 1] for i in range(4)]
print("  razones L2:", " ".join(f"{q_:.3f}" for q_ in r2), "| razones H1:", " ".join(f"{q_:.3f}" for q_ in r1))
assert all(3.5 < q_ < 4.5 for q_ in r2) and all(1.8 < q_ < 2.2 for q_ in r1)
print("Pruebas superadas.")
