#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C03: ecuaciones de primer orden con solución exacta.

Datos SINTÉTICOS (ilustrativos, no de una misión): masa m = 100 kg, coeficiente
de arrastre lineal c = 5 kg/s, g = 9.80665 m/s2 (valor convencional de g_n, SI);
componente térmico con constante de tiempo tau = 600 s, T_amb = 250 K, T0 = 300 K.
Modelos: (a) v' = g - (c/m) v  (velocidad con arrastre lineal);
(b) T' = -(T - T_amb)/tau (enfriamiento de Newton);
(c) y' = -2 t y (separable), y(0) = 1, con solución exp(-t^2).
Método de verificación: la solución exacta se sustituye en la ecuación (residuo
con diferencia central, DLMF 3.4.6) y se compara con la regla de integración
del factor integrante calculada por cuadratura trapezoidal.
Supuestos: coeficientes constantes. Validez: modelo de arrastre lineal solo
para velocidades bajas. Tolerancia: residuo relativo < 1e-6; cuadratura 1e-6.
"""
import math, platform

g, m, c = 9.80665, 100.0, 5.0
kk = c / m
vt = g / kk                                    # velocidad terminal
v_exact = lambda t: vt * (1 - math.exp(-kk * t))
tau, Ta, T0 = 600.0, 250.0, 300.0
T_exact = lambda t: Ta + (T0 - Ta) * math.exp(-t / tau)
y_exact = lambda t: math.exp(-t * t)


def residuo(F, rhs, t, h):
    return (F(t + h) - F(t - h)) / (2 * h) - rhs(t, F(t))


r_v = residuo(v_exact, lambda t, v: g - kk * v, 30.0, 1e-3)
r_T = residuo(T_exact, lambda t, T: -(T - Ta) / tau, 400.0, 1e-2)
r_y = residuo(y_exact, lambda t, y: -2 * t * y, 0.7, 1e-4)
for nombre, r, esc in (("velocidad", r_v, g), ("temperatura", r_T, 50 / tau), ("separable", r_y, 1.0)):
    print(f"residuo {nombre:12s}: {r: .2e}")
    assert abs(r) / esc < 1e-6

# factor integrante: v(t) = e^{-kk t} * integral_0^t g e^{kk s} ds, por trapecios
N = 20000
t = 30.0
s = [t * i / N for i in range(N + 1)]
integ = sum(0.5 * (g * math.exp(kk * s[i]) + g * math.exp(kk * s[i + 1])) * (s[i + 1] - s[i]) for i in range(N))
v_fi = math.exp(-kk * t) * integ
print(f"v(30 s): exacta {v_exact(t):.9f}  factor integrante {v_fi:.9f} m/s")
assert abs(v_fi - v_exact(t)) < 1e-6

print(f"v terminal = {vt:.2f} m/s; v(30 s) = {v_exact(30):.3f} m/s; tiempo característico m/c = {1/kk:.1f} s")
print(f"T(tau) = {T_exact(tau):.3f} K (esperado {Ta + (T0-Ta)/math.e:.3f}); tiempo para llegar a 1 K sobre T_amb: {tau*math.log(T0-Ta):.1f} s")
print(f"Python {platform.python_version()}")
print("Pruebas superadas.")
