#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C09: integracion de largo plazo; error de energia de leapfrog, Yoshida de orden 4 y Runge-Kutta 4 en el problema de Kepler.

Problema SINTETICO adimensional: GM = 1, semieje a = 1, excentricidad e = 0.2, inicio en el pericentro; periodo 2 pi.
Escala de ejemplo (datos consultados 2026-11-10, JPL SSD): si a = 421 800 km (semieje medio de Io) y GM = 126.687e6 + 5959.91547 km3/s2
(NASA/NSSDC, Jupiter Fact Sheet; JPL SSD), una unidad de tiempo son 24 340 s y 3000 orbitas son unos 14.5 anos terrestres (periodo de Io 1.762732 d en la tabla del JPL).
Metodos: leapfrog (orden 2, simplectico), Yoshida (orden 4, simplectico, composicion de 3 leapfrogs), RK4 (orden 4, no simplectico).
100 pasos por orbita. Segunda via: tras un numero entero de orbitas la solucion exacta vuelve al estado inicial: el error de posicion mide el desfase.
Tambien: reversibilidad (N orbitas adelante y N atras). Tolerancias: leapfrog y Yoshida con error de energia acotado (pendiente log-log < 0.3);
RK4 con deriva secular (pendiente log-log > 0.7).
"""
from __future__ import annotations
import json, math, platform, sys

E_EXC = 0.2
PASOS = 100
DT = 2 * math.pi / PASOS


def acc(x, y):
    r3 = (x * x + y * y) ** 1.5
    return -x / r3, -y / r3


def energia(s):
    x, y, vx, vy = s
    return 0.5 * (vx * vx + vy * vy) - 1.0 / math.hypot(x, y)


def leap(s, h):
    x, y, vx, vy = s
    ax, ay = acc(x, y)
    vx += 0.5 * h * ax
    vy += 0.5 * h * ay
    x += h * vx
    y += h * vy
    ax, ay = acc(x, y)
    vx += 0.5 * h * ax
    vy += 0.5 * h * ay
    return [x, y, vx, vy]


W1 = 1.0 / (2.0 - 2.0 ** (1.0 / 3.0))
W0 = -(2.0 ** (1.0 / 3.0)) * W1


def yoshida(s, h):
    return leap(leap(leap(s, W1 * h), W0 * h), W1 * h)


def deriv(s):
    ax, ay = acc(s[0], s[1])
    return [s[2], s[3], ax, ay]


def rk4(s, h):
    k1 = deriv(s)
    k2 = deriv([a + 0.5 * h * b for a, b in zip(s, k1)])
    k3 = deriv([a + 0.5 * h * b for a, b in zip(s, k2)])
    k4 = deriv([a + h * b for a, b in zip(s, k3)])
    return [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4)]


METODOS = {"leapfrog": (leap, 1), "yoshida4": (yoshida, 3), "rk4": (rk4, 4)}
INICIO = [1 - E_EXC, 0.0, 0.0, math.sqrt((1 + E_EXC) / (1 - E_EXC))]
CHECK = (100, 300, 1000, 3000)


def correr(paso):
    s = list(INICIO)
    e0 = energia(s)
    res = {}
    emax = 0.0
    for orb in range(1, CHECK[-1] + 1):
        for _ in range(PASOS):
            s = paso(s, DT)
            emax = max(emax, abs(energia(s) / e0 - 1)) if _ % 10 == 0 else emax
        if orb in CHECK:
            res[orb] = (abs(energia(s) / e0 - 1), math.hypot(s[0] - INICIO[0], s[1] - INICIO[1]), emax)
    return res, s


def pendiente(res):
    a, b = CHECK[0], CHECK[-1]
    return math.log(res[b][2] / res[a][2]) / math.log(b / a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Kepler e = {E_EXC}, {PASOS} pasos/orbita, hasta {CHECK[-1]} orbitas (equivalen a {CHECK[-1] * 1.762732 / 365.25:.1f} anos con la escala de Io)")
    out = {"python": platform.python_version(), "orb": CHECK[-1], "anios": CHECK[-1] * 1.762732 / 365.25}
    print(" metodo     evals/paso " + " ".join(f"E(N={n:>4})" for n in CHECK) + "   pend.log-log  |r-r0| (N=3000)")
    for nom, (paso, ev) in METODOS.items():
        res, sf = correr(paso)
        p = pendiente(res)
        print(f" {nom:9s} {ev:6d}     " + " ".join(f"{res[n][2]:.2e}" for n in CHECK) + f"      {p:6.2f}      {res[CHECK[-1]][1]:.2e}")
        out[f"{nom}_p"] = p
        out[f"{nom}_e"] = res[CHECK[-1]][2]
        out[f"{nom}_e100"] = res[CHECK[0]][2]
        out[f"{nom}_r"] = res[CHECK[-1]][1]
        out[f"{nom}_ev"] = ev
        # reversibilidad: N orbitas atras
        s = list(sf)
        for _ in range(CHECK[-1] * PASOS):
            s = paso(s, -DT)
        rev = math.hypot(s[0] - INICIO[0], s[1] - INICIO[1])
        out[f"{nom}_rev"] = rev
        print(f"   reversibilidad ({CHECK[-1]} orbitas adelante y atras): |r - r0| = {rev:.2e}")
    assert out["leapfrog_p"] < 0.3 and out["yoshida4_p"] < 0.3 and out["rk4_p"] > 0.7
    assert out["yoshida4_e"] < out["leapfrog_e"]
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
