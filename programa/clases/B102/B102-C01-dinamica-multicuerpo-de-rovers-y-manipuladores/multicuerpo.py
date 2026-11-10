#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B102-C01: dinamica de un brazo plano de dos eslabones en Tierra, Marte y la Luna.

Datos consultados (2026-11-10): gravedad media de Marte 3.73 m/s2 y de la Luna 1.62 m/s2 (fichas NASA/NSSDC);
Tierra: g_n = 9.80665 m/s2 (NIST, CODATA 2022). ILUSTRATIVOS (sinteticos): barras uniformes l1 = 1.0 m, l2 = 0.8 m,
m1 = 4 kg, m2 = 3 kg; contacto de penalizacion k = 2.0e4 N/m, c = 60 N s/m, masa de 5 kg.
Modelo: Lagrange, M(q) qdd + C(q,qd) qd + G(q) = tau; plano vertical, q medido desde la horizontal, sistema inercial local
(eje x horizontal, eje y hacia arriba), sin rozamiento articular. Integracion RK4 con paso fijo.
Tolerancias: deriva de energia < 1e-6 relativa; escalado temporal exacto con sqrt(g) < 1e-9; G = grad V frente a
diferencias finitas centrales < 1e-6; penetracion estatica frente a m g / k < 1e-3 relativa (caida desde 0.02 m, 12 s).
"""
from __future__ import annotations
import math, platform

L1, L2, M1, M2 = 1.0, 0.8, 4.0, 3.0
LC1, LC2 = L1 / 2, L2 / 2
I1, I2 = M1 * L1**2 / 12, M2 * L2**2 / 12
GRAV = {"Tierra": 9.80665, "Marte": 3.73, "Luna": 1.62}


def matriz_masa(q2):
    a = I1 + I2 + M1 * LC1**2 + M2 * (L1**2 + LC2**2)
    b = M2 * L1 * LC2
    d = I2 + M2 * LC2**2
    c = math.cos(q2)
    return [[a + 2 * b * c, d + b * c], [d + b * c, d]]


def coriolis(q2, w1, w2):
    b = M2 * L1 * LC2
    s = math.sin(q2)
    return [-b * s * (2 * w1 * w2 + w2**2), b * s * w1**2]


def gravedad(q1, q2, g):
    return [(M1 * LC1 + M2 * L1) * g * math.cos(q1) + M2 * LC2 * g * math.cos(q1 + q2),
            M2 * LC2 * g * math.cos(q1 + q2)]


def energia(q1, q2, w1, w2, g):
    m = matriz_masa(q2)
    t = 0.5 * (m[0][0] * w1 * w1 + 2 * m[0][1] * w1 * w2 + m[1][1] * w2 * w2)
    v = M1 * g * LC1 * math.sin(q1) + M2 * g * (L1 * math.sin(q1) + LC2 * math.sin(q1 + q2))
    return t + v


def deriv(x, g):
    q1, q2, w1, w2 = x
    m = matriz_masa(q2)
    c = coriolis(q2, w1, w2)
    gv = gravedad(q1, q2, g)
    r1, r2 = -c[0] - gv[0], -c[1] - gv[1]
    det = m[0][0] * m[1][1] - m[0][1] ** 2
    a1 = (m[1][1] * r1 - m[0][1] * r2) / det
    a2 = (-m[0][1] * r1 + m[0][0] * r2) / det
    return [w1, w2, a1, a2]


def rk4(x, dt, g):
    k1 = deriv(x, g)
    k2 = deriv([x[i] + 0.5 * dt * k1[i] for i in range(4)], g)
    k3 = deriv([x[i] + 0.5 * dt * k2[i] for i in range(4)], g)
    k4 = deriv([x[i] + dt * k3[i] for i in range(4)], g)
    return [x[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)]


def trayectoria(g, dt, n):
    x = [0.5, 0.3, 0.0, 0.0]
    e0 = energia(*x, g)
    deriva = 0.0
    traza = [x]
    for _ in range(n):
        x = rk4(x, dt, g)
        traza.append(x)
        deriva = max(deriva, abs(energia(*x, g) - e0) / abs(e0))
    return traza, deriva


def rebote(g, m=5.0, k=2.0e4, c=60.0, dt=1e-4, t=12.0):
    y, v = 0.02, 0.0
    for _ in range(int(t / dt)):
        f = -m * g
        if y < 0:
            f += -k * y - c * v
        v += f / m * dt
        y += v * dt
    return y


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Brazo ILUSTRATIVO: l1 = {L1} m, l2 = {L2} m, m1 = {M1} kg, m2 = {M2} kg (barras uniformes)")
    mm = matriz_masa(0.0)
    print(f"M(q2=0) = [[{mm[0][0]:.4f}, {mm[0][1]:.4f}], [{mm[1][0]:.4f}, {mm[1][1]:.4f}]] kg m2")
    mm2 = matriz_masa(math.pi / 2)
    print(f"M(q2=90 deg) = [[{mm2[0][0]:.4f}, {mm2[0][1]:.4f}], [{mm2[1][0]:.4f}, {mm2[1][1]:.4f}]] kg m2")
    print("Par de gravedad con el brazo extendido en horizontal (q1 = q2 = 0):")
    print(" cuerpo   g [m/s2]  tau1 [N m]  tau2 [N m]")
    tau = {}
    for nom, g in GRAV.items():
        gv = gravedad(0.0, 0.0, g)
        tau[nom] = gv
        print(f"{nom:7s} {g:9.5f} {gv[0]:11.4f} {gv[1]:11.4f}")
    # G = grad V por diferencias finitas
    q1, q2, h = 0.7, -0.4, 1e-6
    g = 3.73
    v = lambda a, b: energia(a, b, 0.0, 0.0, g)
    gfd = [(v(q1 + h, q2) - v(q1 - h, q2)) / (2 * h), (v(q1, q2 + h) - v(q1, q2 - h)) / (2 * h)]
    ga = gravedad(q1, q2, g)
    err_g = max(abs(gfd[0] - ga[0]), abs(gfd[1] - ga[1]))
    print(f"G analitico frente a grad V (diferencias finitas): error maximo = {err_g:.2e} N m")
    # energia y escalado temporal
    dt, n = 1e-3, 5000
    tr_t, dr_t = trayectoria(GRAV["Tierra"], dt, n)
    tr_m, dr_m = trayectoria(GRAV["Marte"], dt * math.sqrt(GRAV["Tierra"] / GRAV["Marte"]), n)
    dif = max(abs(tr_t[i][j] - tr_m[i][j]) for i in range(len(tr_t)) for j in range(2))
    print(f"Deriva de energia en 5 s (Tierra, dt = 1 ms): {dr_t:.2e}")
    print(f"Escalado temporal Tierra/Marte (t ~ 1/sqrt(g)): diferencia maxima de angulos = {dif:.2e} rad")
    # primer instante en que q1 cambia de signo de la velocidad
    def t_giro(g, dt):
        x = [0.5, 0.3, 0.0, 0.0]
        w_prev = 0.0
        for i in range(1, 20000):
            x = rk4(x, dt, g)
            if i > 5 and x[2] * w_prev < 0:
                return i * dt
            w_prev = x[2]
        return float("nan")
    tt = t_giro(GRAV["Tierra"], 1e-3)
    tm = t_giro(GRAV["Marte"], 1e-3)
    print(f"Tiempo hasta la 1a inversion de q1: Tierra {tt:.3f} s, Marte {tm:.3f} s; cociente {tm / tt:.4f}; sqrt(gT/gM) = {math.sqrt(GRAV['Tierra'] / GRAV['Marte']):.4f}")
    print("Contacto de penalizacion (masa 5 kg, k = 2.0e4 N/m): penetracion estatica")
    ok = True
    for nom, g in GRAV.items():
        y = rebote(g)
        est = -5.0 * g / 2.0e4
        rel = abs(y - est) / abs(est)
        ok = ok and rel < 1e-3
        print(f"  {nom:7s} y = {y * 1000:8.4f} mm ; m g / k = {est * 1000:8.4f} mm ; error relativo = {rel:.1e}")
    assert err_g < 1e-6
    assert dr_t < 1e-6 and dif < 1e-9
    assert abs(tm / tt - math.sqrt(GRAV["Tierra"] / GRAV["Marte"])) < 5e-3
    assert abs(tau["Marte"][0] / tau["Tierra"][0] - GRAV["Marte"] / GRAV["Tierra"]) < 1e-12
    assert ok
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
