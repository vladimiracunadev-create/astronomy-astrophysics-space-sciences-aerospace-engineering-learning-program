#!/usr/bin/env python3
"""B72-C18 — Integracion numerica perturbada.

Metodo de Cowell con J2: Euler explicito, RK4 de paso fijo y Dormand-Prince 5(4) de paso adaptativo.
Comprueba el orden de convergencia, el coste frente a la tolerancia y la conservacion de la energia
(con el potencial J2) y de la componente z del momento angular, que son integrales exactas del
problema axisimetrico. Orbita SINTETICA. Unidades SI; marco: ecuador de la fecha, inercial.
Solo biblioteca estandar.
"""
import math
import sys

MU = 3.986004e14
RE = 6378137.0
J2 = 1082.63e-6


def acel(r):
    x, y, z = r
    d = math.sqrt(x * x + y * y + z * z)
    k = -1.5 * J2 * MU * RE ** 2 / d ** 5
    zz = 5 * z * z / (d * d)
    return [-MU * x / d ** 3 + k * x * (1 - zz), -MU * y / d ** 3 + k * y * (1 - zz), -MU * z / d ** 3 + k * z * (3 - zz)]


def f(s):
    a = acel(s[:3])
    return [s[3], s[4], s[5], a[0], a[1], a[2]]


def energia(s):
    x, y, z, vx, vy, vz = s
    d = math.sqrt(x * x + y * y + z * z)
    p2 = 0.5 * (3 * (z / d) ** 2 - 1)
    U = MU / d * (1 - J2 * (RE / d) ** 2 * p2)
    return 0.5 * (vx * vx + vy * vy + vz * vz) - U


def hz(s):
    return s[0] * s[4] - s[1] * s[3]


def suma(s, k, h):
    return [s[i] + h * k[i] for i in range(6)]


def euler(s, h):
    k = f(s)
    return suma(s, k, h)


def rk4(s, h):
    k1 = f(s); k2 = f(suma(s, k1, h / 2)); k3 = f(suma(s, k2, h / 2)); k4 = f(suma(s, k3, h))
    return [s[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(6)]


A = [[], [1 / 5], [3 / 40, 9 / 40], [44 / 45, -56 / 15, 32 / 9],
     [19372 / 6561, -25360 / 2187, 64448 / 6561, -212 / 729],
     [9017 / 3168, -355 / 33, 46732 / 5247, 49 / 176, -5103 / 18656],
     [35 / 384, 0.0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84]]
B5 = [35 / 384, 0.0, 500 / 1113, 125 / 192, -2187 / 6784, 11 / 84, 0.0]
B4 = [5179 / 57600, 0.0, 7571 / 16695, 393 / 640, -92097 / 339200, 187 / 2100, 1 / 40]


def dp45(s, h):
    ks = [f(s)]
    for fila in A[1:]:
        ks.append(f([s[i] + h * sum(fila[j] * ks[j][i] for j in range(len(fila))) for i in range(6)]))
    n5 = [s[i] + h * sum(B5[j] * ks[j][i] for j in range(7)) for i in range(6)]
    n4 = [s[i] + h * sum(B4[j] * ks[j][i] for j in range(7)) for i in range(6)]
    return n5, n4


def integra_fijo(metodo, s, T, h):
    n = int(round(T / h))
    for _ in range(n):
        s = metodo(s, h)
    return s


def integra_adaptativo(s, T, rtol, atol_r=1.0, atol_v=1e-3):
    t, h, pasos = 0.0, 30.0, 0
    while t < T - 1e-9:
        h = min(h, T - t)
        n5, n4 = dp45(s, h)
        err = 0.0
        for i in range(6):
            sc = (atol_r if i < 3 else atol_v) * rtol + rtol * max(abs(s[i]), abs(n5[i])) * 0
            sc = (atol_r if i < 3 else atol_v) * rtol + rtol * max(abs(s[i]), abs(n5[i]))
            err = max(err, abs(n5[i] - n4[i]) / sc)
        if err <= 1.0:
            t += h; s = n5; pasos += 1
        h *= min(5.0, max(0.2, 0.9 * (err + 1e-16) ** -0.2))
    return s, pasos


def estado_inicial():
    a, e, inc = 7500e3, 0.1, math.radians(55.0)
    rp = a * (1 - e)
    vp = math.sqrt(MU * (1 + e) / rp)
    return [rp, 0.0, 0.0, 0.0, vp * math.cos(inc), vp * math.sin(inc)], 2 * math.pi * math.sqrt(a ** 3 / MU)


print(f"Python {sys.version.split()[0]} (biblioteca estandar)")
s0, T = estado_inicial()
norb = 5
Tt = 32400.0     # s, multiplo de todos los pasos usados (aprox. 5 vueltas)
print(f"Orbita SINTETICA a = 7500 km, e = 0.1, i = 55 deg, solo J2 ; periodo kepleriano = {T:.1f} s ; {Tt / T:.2f} vueltas ({Tt / 3600:.2f} h)")
E0, H0 = energia(s0), hz(s0)

# Referencia: RK4 con paso pequeno
ref = integra_fijo(rk4, s0, Tt, 1.25)
print(f"Referencia: RK4 con h = 1.25 s ; |E - E0|/|E0| = {abs(energia(ref) - E0) / abs(E0):.2e} ; |h_z - h_z0|/|h_z0| = {abs(hz(ref) - H0) / abs(H0):.2e}")

print("\nEuler explicito (NO usar): h = 1 s")
se = integra_fijo(euler, s0, Tt, 1.0)
print(f"  error de posicion = {math.dist(se[:3], ref[:3]) / 1e3:.1f} km ; deriva de energia = {abs(energia(se) - E0) / abs(E0):.2e}")

print("\nRK4 de paso fijo: error de posicion frente a la referencia")
print(f"{'h [s]':>8}{'pasos':>8}{'error [m]':>14}{'orden':>8}{'dE/E0':>12}{'dhz/hz0':>12}")
prev = None
for h in (60.0, 30.0, 15.0, 7.5):
    s = integra_fijo(rk4, s0, Tt, h)
    err = math.dist(s[:3], ref[:3])
    orden = f"{math.log(prev / err, 2):.2f}" if prev else "-"
    print(f"{h:>8.1f}{int(round(Tt / h)):>8}{err:>14.4e}{orden:>8}{abs(energia(s) - E0) / abs(E0):>12.2e}{abs(hz(s) - H0) / abs(H0):>12.2e}")
    if prev and h <= 30:
        assert 3.5 < math.log(prev / err, 2) < 5.0
    prev = err

print("\nDormand-Prince 5(4) adaptativo: coste y error frente a la tolerancia relativa")
print(f"{'rtol':>9}{'pasos aceptados':>17}{'error [m]':>14}{'dE/E0':>12}")
for rtol in (1e-5, 1e-7, 1e-9, 1e-11):
    s, p = integra_adaptativo(s0, Tt, rtol)
    print(f"{rtol:>9.0e}{p:>17}{math.dist(s[:3], ref[:3]):>14.4e}{abs(energia(s) - E0) / abs(E0):>12.2e}")
print("(la referencia RK4 con h = 1.25 s tiene un error estimado de ~1e-5 m, extrapolando el orden 4 de la tabla anterior)")
assert math.dist(s[:3], ref[:3]) < 0.1
print("Pruebas superadas.")
