#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C02: dinamica de un asteroide de dos cuerpos (integrador leapfrog) y posicion de las resonancias de movimiento medio con Jupiter.

Datos: orbita SINTETICA a = 2.2 au, e = 0.3. GM del Sol = k^2 con la constante de Gauss k = 0.01720209895 au^1.5/dia (valor historico adoptado, no consultado en esta sesion). Semieje de
Jupiter 5.2044 au: valor aproximado del autor, no consultado. La posicion del hueco de Kirkwood 3:1 en ~2.5 au es conocimiento general no consultado.
Modelo: problema de dos cuerpos con integrador kick-drift-kick (orden 2, simplectico). Unidades: au, dia, radian. Marco: heliocentrico inercial.
Supuestos: sin perturbaciones planetarias; punto material. Validez: la resonancia se trata solo como cociente de periodos keplerianos, no como dinamica resonante.
Tolerancia: error de periodo < 1e-4 d con dt = 0.1 d; orden de convergencia entre 1.9 y 2.1 al reducir dt a la mitad (error ~ dt^2); cocientes de periodo resonantes con 1e-4 relativo.
"""
import math, platform

K = 0.01720209895
GM = K * K
AJ = 5.2044

def aceleracion(x, y):
    r3 = (x * x + y * y) ** 1.5
    return -GM * x / r3, -GM * y / r3

def periodo_integrado(a, e, dt):
    """Parte del perihelio y devuelve el tiempo en que el angulo acumulado alcanza 2 pi (interpolacion lineal)."""
    x, y = a * (1 - e), 0.0
    vx, vy = 0.0, math.sqrt(GM * (1 + e) / (a * (1 - e)))
    ax, ay = aceleracion(x, y)
    th, t = 0.0, 0.0
    while True:
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        ax, ay = aceleracion(x, y)
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        t += dt
        nuevo = math.atan2(y, x) % (2 * math.pi)
        d = (nuevo - (th % (2 * math.pi)) + math.pi) % (2 * math.pi) - math.pi
        th_prev = th
        th += d
        if th >= 2 * math.pi:
            return t - dt + dt * (2 * math.pi - th_prev) / (th - th_prev)

def energia(a, e):
    return -GM / (2 * a)

def calcular():
    a, e = 2.2, 0.3
    T = 2 * math.pi * a ** 1.5 / K
    p1 = periodo_integrado(a, e, 0.2)
    p2 = periodo_integrado(a, e, 0.1)
    p3 = periodo_integrado(a, e, 0.05)
    e1, e2, e3 = abs(p1 - T), abs(p2 - T), abs(p3 - T)
    TJ = 2 * math.pi * AJ ** 1.5 / K
    res = []
    for nombre, (p, q) in {"3:1": (3, 1), "5:2": (5, 2), "7:3": (7, 3), "2:1": (2, 1), "3:2": (3, 2)}.items():
        # el asteroide da p vueltas mientras Jupiter da q: P_ast / P_J = q / p
        ares = AJ * (q / p) ** (2.0 / 3.0)
        Pint = periodo_integrado(ares, 0.0, 0.5)
        res.append((nombre, ares, Pint / TJ, q / p))
    return {"T": T, "T_anios": T / 365.25, "p1": p1, "p2": p2, "p3": p3, "err1": e1, "err2": e2, "err3": e3,
            "orden": math.log(e1 / e2, 2), "orden2": math.log(e2 / e3, 2), "TJ_anios": TJ / 365.25, "res": res}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("Periodo analitico 2 pi a^1.5 / k = %.6f d (%.4f anios)" % (r["T"], r["T_anios"]))
    for dt, p, er in [(0.2, r["p1"], r["err1"]), (0.1, r["p2"], r["err2"]), (0.05, r["p3"], r["err3"])]:
        print("dt = %.2f d : periodo integrado = %.6f d ; error = %.3e d" % (dt, p, er))
    print("Orden de convergencia observado: %.2f ; %.2f" % (r["orden"], r["orden2"]))
    print("Periodo de Jupiter (a = 5.2044 au) = %.3f anios" % r["TJ_anios"])
    print("%5s %10s %16s %10s" % ("res", "a [au]", "P_ast/P_J medido", "q/p"))
    for n, a, m, c in r["res"]:
        print("%5s %10.4f %16.6f %10.6f" % (n, a, m, c))
    assert r["err3"] < 1e-4
    assert 1.9 < r["orden"] < 2.1 and 1.9 < r["orden2"] < 2.1
    for n, a, m, c in r["res"]:
        assert abs(m / c - 1) < 1e-4, n
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
