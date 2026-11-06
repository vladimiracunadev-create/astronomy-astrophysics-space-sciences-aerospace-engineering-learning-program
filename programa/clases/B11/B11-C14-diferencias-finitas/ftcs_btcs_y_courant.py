#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C14: diferencias finitas para el calor y la advección.

Datos SINTÉTICOS: placa de L = 0.05 m, difusividad alpha = 1.0e-6 m2/s,
condición inicial u(x,0) = sin(pi x / L), u(0,t) = u(L,t) = 0, instante final
100 s; advección con velocidad c = 2.0 m/s (adimensionalizada: x en [0,1)).
Modelo: u_t = alpha u_xx con solución exacta
u = sin(pi x/L) exp(-alpha pi^2 t / L^2); u_t + c u_x = 0 periódica.
Métodos: FTCS (explícito), BTCS (implícito, sistema tridiagonal por Thomas);
contracorriente (upwind) para la advección; derivada segunda central
(DLMF 3.4.6 / 3.4.22) con error O(h^2).
Supuestos: coeficientes constantes. Validez: FTCS exige r = alpha dt/dx^2 <= 1/2;
upwind exige Courant nu = c dt/dx <= 1.
Tolerancia: orden espacial 2 (razón de errores en [3.5, 4.5] con dt proporcional a
dx^2); FTCS con r = 0.6 debe amplificar una perturbación de 1e-3 hasta superar 1; BTCS con r = 5
debe seguir acotado por 1.0; upwind estable con nu = 0.8 e inestable con nu = 1.2.
"""
import math, platform

alpha, L, tf = 1.0e-6, 0.05, 100.0
exacta = lambda x, t: math.sin(math.pi * x / L) * math.exp(-alpha * math.pi**2 * t / L**2)


def ftcs(N, r, pert=0.0):
    dx = L / N
    dt = r * dx * dx / alpha
    steps = int(round(tf / dt))
    dt = tf / steps
    r = alpha * dt / dx**2
    u = [math.sin(math.pi * i * dx / L) + (pert * (-1) ** i if 0 < i < N else 0.0) for i in range(N + 1)]
    for _ in range(steps):
        v = u[:]
        for i in range(1, N):
            v[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
        u = v
    return u, dx, steps, r


def btcs(N, steps):
    dx = L / N
    dt = tf / steps
    r = alpha * dt / dx**2
    u = [math.sin(math.pi * i * dx / L) for i in range(N + 1)]
    n = N - 1
    for _ in range(steps):
        a = [-r] * n; b = [1 + 2 * r] * n; c = [-r] * n; d = u[1:N]
        for i in range(1, n):
            w = a[i] / b[i - 1]
            b[i] -= w * c[i - 1]
            d[i] -= w * d[i - 1]
        x = [0.0] * n
        x[-1] = d[-1] / b[-1]
        for i in range(n - 2, -1, -1):
            x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
        u = [0.0] + x + [0.0]
    return u, dx, steps, r


def error_max(u, dx):
    return max(abs(u[i] - exacta(i * dx, tf)) for i in range(len(u)))


print(f"Python {platform.python_version()}")
print(f"u(L/2, 100 s) exacto = {exacta(L/2, tf):.6f}")
errs = []
for N in (10, 20, 40):
    u, dx, steps, r = ftcs(N, 0.4)
    errs.append(error_max(u, dx))
    print(f"FTCS N={N:3d} r={r:.3f} pasos={steps:6d}: error máx = {errs[-1]:.4e} ; u(L/2) = {u[N//2]:.6f}")
razones = [errs[i] / errs[i + 1] for i in range(2)]
print("  razones de error:", " ".join(f"{q:.3f}" for q in razones))
assert all(3.5 < q < 4.5 for q in razones)

for rr in (0.4, 0.6):
    u, dx, steps, r = ftcs(20, rr, pert=1e-3)           # perturbación alternante de 1e-3
    amp = max(abs(u[i] - exacta(i * dx, tf)) for i in range(len(u)))
    print(f"FTCS N=20 r={r:.3f} con perturbación 1e-3: error máx tras {steps} pasos = {amp:.3e}")
    if rr == 0.4:
        assert amp < 1e-2
    else:
        assert amp > 1.0 and r > 0.5

u, dx, steps, r = btcs(20, 3)
print(f"BTCS N=20 pasos={steps} r={r:.2f}: error máx = {error_max(u, dx):.4e} ; máx|u| = {max(abs(v) for v in u):.4f}")
assert max(abs(v) for v in u) <= 1.0 and error_max(u, dx) < 0.1
u2, dx2, steps2, r2 = btcs(20, 2000)
print(f"BTCS N=20 pasos={steps2} r={r2:.3f}: error máx = {error_max(u2, dx2):.4e}")

# advección contracorriente
def upwind(nu, N=100, pasos=None):
    pasos = pasos or int(round(1.0 / nu * N / 2))
    u = [math.exp(-200 * ((i / N) - 0.3) ** 2) + 1e-3 * (-1) ** i for i in range(N)]   # pulso + perturbación alternante
    for _ in range(pasos):
        u = [u[i] - nu * (u[i] - u[i - 1]) for i in range(N)]
    return max(abs(v) for v in u)

m08, m12 = upwind(0.8, pasos=60), upwind(1.2, pasos=60)
print(f"upwind: máx|u| tras 60 pasos con nu=0.8: {m08:.4f} ; con nu=1.2: {m12:.3e}")
assert m08 <= 1.0 and m12 > 10
print("Pruebas superadas.")
