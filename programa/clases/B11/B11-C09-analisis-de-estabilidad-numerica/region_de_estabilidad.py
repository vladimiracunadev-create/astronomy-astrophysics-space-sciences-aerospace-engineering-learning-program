#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C09: estabilidad numérica con la ecuación de prueba y' = lambda y.

Datos: SINTÉTICOS. Constante de relajación lambda = -50 1/s (sistema de una sola
escala); sistema rígido x' = -k (x - cos t), k = 1000 1/s, x(0) = 0 (un
componente que sigue una excitación lenta con una relajación muy rápida).
Modelo: factor de amplificación por paso R(z), z = h lambda:
  Euler: 1 + z; Heun: 1 + z + z^2/2; RK4: 1 + z + z^2/2 + z^3/6 + z^4/24;
  Euler implícito: 1/(1 - z). Estable si |R| <= 1.
Solución exacta del sistema rígido: x = (k^2 cos t + k sin t)/(k^2+1) - k^2/(k^2+1) e^(-k t).
Supuestos: ecuación lineal de coeficientes constantes; aritmética de doble
precisión. Validez: los límites son para la ecuación de prueba.
Tolerancia: los límites de estabilidad calculados por bisección deben coincidir
con 2 (Euler, Heun) y 2.785 (RK4) a 1e-3; sobre el eje imaginario RK4 llega a
2*sqrt(2); las predicciones de crecimiento o decaimiento deben coincidir con las
iteraciones.
"""
import math, platform

R_euler = lambda z: 1 + z
R_heun = lambda z: 1 + z + z * z / 2
R_rk4 = lambda z: 1 + z + z**2 / 2 + z**3 / 6 + z**4 / 24
R_imp = lambda z: 1 / (1 - z)


def limite_real(R):
    lo, hi = 0.0, 10.0                     # |R(-lo)| <= 1; se busca el mayor x con |R(-x)| <= 1
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if all(abs(R(-x)) <= 1 + 1e-14 for x in [mid * j / 50 for j in range(1, 51)]):
            lo = mid
        else:
            hi = mid
    return lo


def limite_imag(R):
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if all(abs(R(complex(0, mid * j / 50))) <= 1 + 1e-14 for j in range(1, 51)):
            lo = mid
        else:
            hi = mid
    return lo


print(f"Python {platform.python_version()}")
lim = {n: limite_real(R) for n, R in (("Euler", R_euler), ("Heun", R_heun), ("RK4", R_rk4))}
for n, v in lim.items():
    print(f"limite real de estabilidad {n:6s}: h|lambda| <= {v:.4f}")
assert abs(lim["Euler"] - 2) < 1e-3 and abs(lim["Heun"] - 2) < 1e-3 and abs(lim["RK4"] - 2.7853) < 1e-3
li = limite_imag(R_rk4)
print(f"limite sobre el eje imaginario RK4: {li:.4f} (2*sqrt(2) = {2*math.sqrt(2):.4f}); Euler: {limite_imag(R_euler):.4f}")
assert abs(li - 2 * math.sqrt(2)) < 1e-3
print("modulo de R sobre el eje imaginario, y = 0.1:",
      " ".join(f"{n}={abs(R(complex(0, 0.1))):.10f}" for n, R in (("Euler", R_euler), ("Heun", R_heun), ("RK4", R_rk4))))
assert abs(R_euler(0.1j)) > 1 and abs(R_heun(0.1j)) > 1 and abs(R_rk4(0.1j)) < 1

# iteraciones sobre y' = -50 y, y(0) = 1, hasta t = 2
lam = -50.0
print("y' = -50 y hasta t = 2 (exacto e^-100 = 3.7e-44):")
for h in (0.03, 0.05):
    z = h * lam
    N = int(round(2 / h))
    fila = []
    for n, R in (("Euler", R_euler), ("Heun", R_heun), ("RK4", R_rk4)):
        y = 1.0
        for _ in range(N):
            y *= R(z)
        pred = "estable" if abs(R(z)) <= 1 else "inestable"
        fila.append(f"{n}: |R|={abs(R(z)):.3f} y_final={y:.3e} ({pred})")
        assert (abs(y) < 1e-3) == (abs(R(z)) < 1), "la predicción de estabilidad no coincide"
    print(f"  h={h}  z={z}: " + " | ".join(fila))

# sistema rígido
k = 1000.0
ex = lambda t: (k * k * math.cos(t) + k * math.sin(t)) / (k * k + 1) - k * k / (k * k + 1) * math.exp(-k * t)
print("sistema rígido x' = -k (x - cos t), x(1) exacto = %.9f" % ex(1.0))
res = {}
for h in (0.0005, 0.01, 0.1):
    N = int(round(1.0 / h))
    xe, xi, t = 0.0, 0.0, 0.0
    for _ in range(N):
        xe = xe + h * (-k * (xe - math.cos(t)))                 # Euler explícito
        t += h
        xi = (xi + h * k * math.cos(t)) / (1 + h * k)           # Euler implícito (lineal: se despeja)
    res[h] = (xe, xi)
    print(f"  h={h:<7} h*k={h*k:6.1f}: Euler explícito x(1) = {xe: .4e} | Euler implícito x(1) = {xi: .9f}")
assert abs(res[0.0005][0] - ex(1.0)) < 1e-3                      # h k = 0.5: estable y razonable
assert abs(res[0.01][0]) > 1e3                                   # h k = 10: explota
assert abs(res[0.1][1] - ex(1.0)) < 0.1                          # implícito, h k = 100: estable
assert abs(res[0.0005][1] - ex(1.0)) < 1e-3
print("Pruebas superadas.")
