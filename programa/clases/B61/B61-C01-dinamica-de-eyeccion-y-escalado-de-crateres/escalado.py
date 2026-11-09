#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C01: escalado de cráteres en el régimen de gravedad y velocidades de eyección.

Datos: SINTETICOS/ILUSTRATIVOS. No se usa ningun crater real ni medida.
  mu = 0.55 (valor citado para roca blanda en un resumen de busqueda web de Holsapple 1993; original no consultado)
  K1 = 1.0 (constante de ajuste ILUSTRATIVA), g Luna = 1.62 m/s2, g Marte = 3.71 m/s2 (valores redondeados, no consultados en esta sesion)
Modelo (unidades SI, cuerpo plano sin atmosfera, sin curvatura):
  radio transitorio R = K1 * a * pi2**(-mu/(2+mu)),  pi2 = g*a/U**2   (regimen de gravedad)
  velocidad de eyeccion v = U * C * (x/a)**(-1/mu)  (ley de potencias, forma NO consultada en el original; C ilustrativo)
  alcance balistico sin arrastre en terreno plano: L = v**2 sin(2 theta)/g
Verificaciones: (1) exponentes dimensionales; (2) ajuste log-log de R frente a g; (3) fraccion de masa que supera v
  con pendiente -3 mu (Monte Carlo, semilla 20261109); (4) alcance RK4 frente a la formula (tolerancia 1e-6 relativo).
Tolerancias: exponentes 1e-12; pendiente de R(g) 1e-9; pendiente Monte Carlo 0.03 absoluto; RK4 1e-6.
"""
from __future__ import annotations
import math, platform, random

MU = 0.55
K1 = 1.0
G_MOON, G_MARS = 1.62, 3.71
U = 17000.0  # m/s, ilustrativo


def radio_transitorio(a, g, u=U, mu=MU, k1=K1):
    pi2 = g * a / u**2
    return k1 * a * pi2 ** (-mu / (2.0 + mu))


def exponentes():
    """R = k a^p g^q U^r. De R=a*(g a/U^2)^(-b) con b=mu/(2+mu): p=1-b, q=-b, r=2b."""
    b = MU / (2.0 + MU)
    return 1 - b, -b, 2 * b


def alcance_rk4(v, theta, g, dt=1e-3):
    x, y, vx, vy = 0.0, 0.0, v * math.cos(theta), v * math.sin(theta)
    def f(s):
        return (s[2], s[3], 0.0, -g)
    s = (x, y, vx, vy)
    while True:
        k1 = f(s)
        k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
        k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
        k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
        n = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))
        if n[1] < 0:
            # interpolacion lineal al impacto con y=0
            t = s[1] / (s[1] - n[1])
            return s[0] + t * (n[0] - s[0])
        s = n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    p, q, r = exponentes()
    print(f"Exponentes R ~ a^p g^q U^r: p={p:.6f} q={q:.6f} r={r:.6f}")
    # dimensiones: m^1 ; g: m s-2 ; U: m s-1  => longitud: p+q+r = 1 ; tiempo: -2q - r = 0
    assert abs(p + q + r - 1) < 1e-12 and abs(-2 * q - r) < 1e-12
    a = 500.0
    for nombre, g in (("Luna", G_MOON), ("Marte", G_MARS)):
        R = radio_transitorio(a, g)
        print(f"{nombre}: a={a:.0f} m, U={U/1000:.0f} km/s -> R_transitorio={R/1000:.2f} km (D={2*R/1000:.2f} km) [ilustrativo]")
    gs = [0.5 * 1.3**k for k in range(12)]
    xs = [math.log(g) for g in gs]
    ys = [math.log(radio_transitorio(a, g)) for g in gs]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    pend = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    print(f"Pendiente log-log de R frente a g = {pend:.9f} ; teorica = {q:.9f}")
    assert abs(pend - q) < 1e-9
    print(f"Cociente R(Luna)/R(Marte) = {radio_transitorio(a, G_MOON)/radio_transitorio(a, G_MARS):.4f}")
    # Monte Carlo: x/a uniforme en volumen (x^3 uniforme) entre 1 y 10 => masa dentro de x ~ x^3
    rng = random.Random(20261109)
    N = 200000
    C = 1.0e-3
    v = []
    for _ in range(N):
        x3 = rng.uniform(1.0, 1000.0)
        x = x3 ** (1 / 3)
        v.append(U * C * x ** (-1.0 / MU))
    v.sort()
    # pendiente de log M(>v) frente a log v en el tramo central
    pts = []
    for fr in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7):
        idx = int(fr * N)
        pts.append((math.log(v[idx]), math.log(1 - idx / N)))
    mx = sum(p_[0] for p_ in pts) / len(pts)
    my = sum(p_[1] for p_ in pts) / len(pts)
    sl = sum((p_[0] - mx) * (p_[1] - my) for p_ in pts) / sum((p_[0] - mx) ** 2 for p_ in pts)
    print(f"Pendiente de M(>v) en Monte Carlo = {sl:.4f} ; teorica -3*mu = {-3*MU:.4f}")
    assert abs(sl - (-3 * MU)) < 0.03
    # alcance
    vv, th = 300.0, math.radians(45.0)
    Lrk = alcance_rk4(vv, th, G_MOON)
    Lan = vv**2 * math.sin(2 * th) / G_MOON
    print(f"Alcance a v=300 m/s, 45 grados, Luna: RK4={Lrk:.4f} m ; analitico={Lan:.4f} m ; dif. relativa={abs(Lrk/Lan-1):.2e}")
    assert abs(Lrk / Lan - 1) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
