#!/usr/bin/env python3
"""B72-C15 — Aproximaciones perturbativas.

(1) Oscilador de Duffing x'' + x + eps x^3 = 0: frecuencia de Lindstedt-Poincare de primer y segundo orden
    frente a RK4 (el error de cada orden escala como eps^2 y eps^3).
(2) Tasa de nodo de primer orden en J2 frente a una integracion RK4 con J2 multiplicado por k,
    muestreada en cada cruce del nodo ascendente (el error relativo escala con k J2).
Sistemas SINTETICOS. Unidades adimensionales en (1); SI en (2). Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6
DIA = 86400.0
RAD = 180.0 / math.pi


def frecuencia_numerica(eps, dt=2e-4):
    x, v, t = 1.0, 0.0, 0.0
    f = lambda x, v: (v, -x - eps * x ** 3)
    while True:
        k1 = f(x, v); k2 = f(x + dt / 2 * k1[0], v + dt / 2 * k1[1])
        k3 = f(x + dt / 2 * k2[0], v + dt / 2 * k2[1]); k4 = f(x + dt * k3[0], v + dt * k3[1])
        nx = x + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        nv = v + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if x > 0 >= nx:
            tc = t + dt * x / (x - nx)
            return 2 * math.pi / (4 * tc)
        x, v, t = nx, nv, t + dt


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
print("Parte 1: oscilador de Duffing x'' + x + eps x^3 = 0, x(0) = 1, x'(0) = 0 (sistema SINTETICO, adimensional)")
print(f"{'eps':>7}{'omega RK4':>12}{'orden 1':>11}{'err1':>10}{'orden 2':>11}{'err2':>10}{'err1/eps^2':>12}{'err2/eps^3':>12}")
for eps in (0.01, 0.05, 0.1, 0.3, 1.0):
    w = frecuencia_numerica(eps)
    w1 = 1 + 3 * eps / 8
    w2 = w1 - 21 * eps ** 2 / 256
    e1, e2 = abs(w - w1), abs(w - w2)
    print(f"{eps:>7.2f}{w:>12.6f}{w1:>11.6f}{e1:>10.2e}{w2:>11.6f}{e2:>10.2e}{e1 / eps ** 2:>12.4f}{e2 / eps ** 3:>12.4f}")
    if eps <= 0.1:
        assert e2 < e1


def nodo(r, v):
    h = [r[1] * v[2] - r[2] * v[1], r[2] * v[0] - r[0] * v[2], r[0] * v[1] - r[1] * v[0]]
    return math.atan2(h[0], -h[1])


def pendiente_nodo(k, a, inc, norb=25, dt=10.0):
    j2 = k * J2
    n = math.sqrt(MU / a ** 3)
    r = [a, 0.0, 0.0]; v = [0.0, n * a * math.cos(inc), n * a * math.sin(inc)]

    def acel(r):
        x, y, z = r
        d = math.sqrt(x * x + y * y + z * z)
        c = -1.5 * j2 * MU * RE ** 2 / d ** 5
        zz = 5 * z * z / (d * d)
        return [-MU * x / d ** 3 + c * x * (1 - zz), -MU * y / d ** 3 + c * y * (1 - zz), -MU * z / d ** 3 + c * z * (3 - zz)]

    def paso(r, v):
        a1 = acel(r); r2 = [r[i] + .5 * dt * v[i] for i in range(3)]; v2 = [v[i] + .5 * dt * a1[i] for i in range(3)]
        a2 = acel(r2); r3 = [r[i] + .5 * dt * v2[i] for i in range(3)]; v3 = [v[i] + .5 * dt * a2[i] for i in range(3)]
        a3 = acel(r3); r4 = [r[i] + dt * v3[i] for i in range(3)]; v4 = [v[i] + dt * a3[i] for i in range(3)]
        a4 = acel(r4)
        return ([r[i] + dt / 6 * (v[i] + 2 * v2[i] + 2 * v3[i] + v4[i]) for i in range(3)],
                [v[i] + dt / 6 * (a1[i] + 2 * a2[i] + 2 * a3[i] + a4[i]) for i in range(3)])

    T = 2 * math.pi * math.sqrt(a ** 3 / MU)
    ts, os_, t = [], [], 0.0
    acc, prev = 0.0, nodo(r, v)
    zprev, oprev_acc = r[2], 0.0
    for _ in range(int(norb * T / dt)):
        r, v = paso(r, v)
        t += dt
        o = nodo(r, v)
        d = o - prev; d -= 2 * math.pi * round(d / (2 * math.pi)); acc += d; prev = o
        if zprev < 0 <= r[2]:
            f = -zprev / (r[2] - zprev)
            ts.append(t - dt + f * dt); os_.append(oprev_acc + f * (acc - oprev_acc))
        zprev, oprev_acc = r[2], acc
    tm = sum(ts) / len(ts); om = sum(os_) / len(os_)
    return sum((ts[i] - tm) * (os_[i] - om) for i in range(len(ts))) / sum((x - tm) ** 2 for x in ts)


print("\nParte 2: tasa del nodo, orbita circular SINTETICA a = 7078.137 km, i = 60 deg, J2 multiplicado por k")
a, inc = 7078137.0, math.radians(60.0)
n = math.sqrt(MU / a ** 3)
print(f"{'k':>5}{'primer orden [deg/dia]':>24}{'RK4 estroboscopico [deg/dia]':>31}{'dif. relativa':>15}{'dif./(k J2)':>13}")
for k in (1.0, 10.0, 30.0):
    teo = -1.5 * n * k * J2 * (RE / a) ** 2 * math.cos(inc) * DIA * RAD
    num = pendiente_nodo(k, a, inc) * DIA * RAD
    rel = abs(num - teo) / abs(teo)
    print(f"{k:>5.0f}{teo:>24.5f}{num:>31.5f}{rel:>15.2e}{rel / (k * J2):>13.3f}")
    assert rel < 0.5
print("El cociente dif./(k J2) casi constante indica error relativo proporcional al parametro pequeno k J2.")
print("Pruebas superadas.")
