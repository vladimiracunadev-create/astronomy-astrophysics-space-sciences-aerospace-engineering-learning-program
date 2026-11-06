#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C21: integración de alta precisión (extrapolación de Gragg-Bulirsch-Stoer) y aritmética extendida.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m (valores
nominales IAU 2015, Res. B3). Órbita circular a 400 km de altitud: dato ILUSTRATIVO.
Oscilador y'' = -y para la prueba de redondeo: modelo SINTÉTICO.
Modelo: dos cuerpos en el plano; referencia exacta circular x = a cos(n t), y = a sin(n t).
Métodos: (a) punto medio modificado con extrapolación de Richardson en h^2
(tabla de Aitken-Neville; el orden de la columna j es 2j); se compara con RK4 al
MISMO número de evaluaciones de la fuerza; (b) RK4 en doble precisión y en
decimal de 40 dígitos (módulo decimal) para medir el redondeo acumulado.
Supuestos: sin perturbaciones; paso macro fijo. Validez: soluciones suaves.
Tolerancia: la extrapolación debe superar a RK4 a igual costo por al menos dos órdenes
de magnitud para (M=10, K=6) y (M=40, K=4); el orden observado de la extrapolación con K=3 en
[5, 7.5]; la diferencia float-decimal debe ser mayor que 1e-14 y menor que 1e-9.
"""
import math, platform
from decimal import Decimal, getcontext

GM, RE = 3.986004e14, 6.3781e6
a = RE + 400e3
n0 = math.sqrt(GM / a**3)
T = 2 * math.pi / n0


def F(s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -GM * x / r3, -GM * y / r3)


EV = [0]


def Fc(s):
    EV[0] += 1
    return F(s)


def rk4(s, h):
    c = lambda k, q: tuple(si + h * q * ki for si, ki in zip(s, k))
    k1 = Fc(s); k2 = Fc(c(k1, .5)); k3 = Fc(c(k2, .5)); k4 = Fc(c(k3, 1.))
    return tuple(si + h * (p + 2 * q + 2 * r + w) / 6 for si, p, q, r, w in zip(s, k1, k2, k3, k4))


def punto_medio(s, H, n):
    h = H / n
    z0 = s
    f0 = Fc(z0)
    z1 = tuple(u + h * d for u, d in zip(z0, f0))
    for _ in range(1, n):
        f1 = Fc(z1)
        z2 = tuple(u + 2 * h * d for u, d in zip(z0, f1))
        z0, z1 = z1, z2
    fn = Fc(z1)
    return tuple(0.5 * (u + v + h * d) for u, v, d in zip(z0, z1, fn))


def gbs(s, H, K):
    ns = [2 * (k + 1) for k in range(K)]
    Tab = []
    for k in range(K):
        fila = [punto_medio(s, H, ns[k])]
        for j in range(1, k + 1):
            r = (ns[k] / ns[k - j]) ** 2 - 1
            fila.append(tuple(u + (u - v) / r for u, v in zip(fila[j - 1], Tab[k - 1][j - 1])))
        Tab.append(fila)
    return Tab[-1][-1]


def una_vuelta(paso, M):
    s = (a, 0.0, 0.0, a * n0)
    EV[0] = 0
    for _ in range(M):
        s = paso(s, T / M)
    return s, EV[0]


err = lambda s: math.hypot(s[0] - a, s[1])

print(f"Python {platform.python_version()}")
print("(a) una vuelta de la órbita de 400 km: error de posición frente a la circular exacta")
res = {}
for M, K in ((10, 6), (20, 4), (40, 4), (40, 3), (80, 3)):
    s, ev = una_vuelta(lambda s, H: gbs(s, H, K), M)
    res[(M, K)] = (err(s), ev)
    sr, evr = una_vuelta(rk4, max(1, ev // 4))
    print(f"    extrapolación M={M:2d}, K={K} (orden {2*K}): error = {err(s):.3e} m con {ev:4d} evaluaciones | RK4 con {evr:4d}: {err(sr):.3e} m")
    if (M, K) in ((10, 6), (40, 4)):
        assert err(s) < err(sr) / 100
# orden observado con K = 3 duplicando M
p_obs = math.log2(res[(40, 3)][0] / res[(80, 3)][0])
print(f"    orden observado de K=3 (M=40 -> 80): {p_obs:.2f}")
assert 5 < p_obs < 7.5

# (b) redondeo: RK4 en float y en Decimal de 40 dígitos sobre y'' = -y
getcontext().prec = 40
N = 100000
h = 0.01
yf, vf = 1.0, 0.0
hD = Decimal("0.01")
yD, vD = Decimal(1), Decimal(0)
half, sixth = Decimal("0.5"), Decimal(1) / Decimal(6)
for _ in range(N):
    k1y, k1v = vf, -yf
    k2y, k2v = vf + 0.5 * h * k1v, -(yf + 0.5 * h * k1y)
    k3y, k3v = vf + 0.5 * h * k2v, -(yf + 0.5 * h * k2y)
    k4y, k4v = vf + h * k3v, -(yf + h * k3y)
    yf += h * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
    vf += h * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
    k1y, k1v = vD, -yD
    k2y, k2v = vD + half * hD * k1v, -(yD + half * hD * k1y)
    k3y, k3v = vD + half * hD * k2v, -(yD + half * hD * k2y)
    k4y, k4v = vD + hD * k3v, -(yD + hD * k3y)
    yD += hD * (k1y + 2 * k2y + 2 * k3y + k4y) * sixth
    vD += hD * (k1v + 2 * k2v + 2 * k3v + k4v) * sixth
dif = abs(Decimal(yf) - yD)
exacto = math.cos(N * h)
print(f"(b) RK4 sobre y''=-y, h=0.01, t={N*h:.0f}: y_float = {yf:.15f} ; y_decimal(40 dígitos) = {float(yD):.15f}")
print(f"    diferencia float-decimal (redondeo acumulado) = {float(dif):.3e} ; y exacta cos(t) = {exacto:.15f}")
print(f"    error de truncamiento (decimal frente a cos t) = {abs(float(yD)-exacto):.3e}")
assert 1e-14 < float(dif) < 1e-9
print("Pruebas superadas.")
