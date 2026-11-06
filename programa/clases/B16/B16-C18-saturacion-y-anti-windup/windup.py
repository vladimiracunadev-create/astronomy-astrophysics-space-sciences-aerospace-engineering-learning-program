#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C18: saturación del par y anti-windup por recálculo hacia atrás.

Datos: SINTÉTICOS. Eje J = 50 kg m^2; PID con derivada sobre la medida
(Kp = 4 N m/rad, Ki = 0.2 N m/(rad s), Kd = 30 N m s/rad); escalón de
referencia r = 0.5 rad; par máximo del actuador u_max = 0.2 N m.
Modelo: J omega' = sat(v), v = Kp e + Ki xi - Kd omega, e = r - theta.
  - sin anti-windup:  xi' = e
  - con recálculo hacia atrás: xi' = e + Kaw (sat(v) - v), con Kaw = 5 (en
    rad s por N m; es un parámetro de diseño y su valor es sintético).
Integración: RK4 de paso fijo h = 0.01 s propio (la saturación es continua
pero no diferenciable; se declara el paso).
Referencias independientes:
  (1) sin saturación (u_max enorme) los tres lazos son idénticos y coinciden con
      el polinomio J s^3 + Kd s^2 + Kp s + Ki (polos por np.roots);
  (2) con saturación: el par saturado entrega un límite de aceleración
      u_max/J, de modo que el primer tramo es un movimiento uniformemente
      acelerado (fórmula cerrada);
  (3) el anti-windup nunca empeora el sobreimpulso en este caso.
Supuestos: sin ruido, estado completo. Tolerancia: 1e-12 en (1) y 1e-9 en (2).
"""
from __future__ import annotations
import platform, sys
import numpy as np

J, Kp, Ki, Kd = 50.0, 4.0, 0.2, 30.0
r, umax, h, T = 0.5, 0.2, 0.01, 600.0
Kaw = 5.0


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def sat(v, lim):
    return min(max(v, -lim), lim)


def simula(lim, aw):
    n = int(T / h)
    x = np.zeros(3)                         # theta, omega, xi
    out = np.empty((n + 1, 4)); out[0] = [0, 0, 0, 0]
    def f(x):
        th, w, xi = x
        e = r - th
        v = Kp * e + Ki * xi - Kd * w
        u = sat(v, lim)
        dxi = e + (Kaw * (u - v) if aw else 0.0)
        return np.array([w, u / J, dxi]), u
    for k in range(n):
        k1, u = f(x)
        k2, _ = f(x + h / 2 * k1)
        k3, _ = f(x + h / 2 * k2)
        k4, _ = f(x + h * k3)
        x = x + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        out[k + 1] = [x[0], x[1], x[2], u]
    return out


def metricas(o):
    th = o[:, 0]
    mp = max(0.0, th.max() - r) / r
    fuera = np.nonzero(np.abs(th - r) > 0.02 * r)[0]
    ts = (fuera[-1] + 1) * h if len(fuera) else 0.0
    return mp, ts, o[:, 2].max()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    big = 1e9
    a, b = simula(big, False), simula(big, True)
    prueba(np.max(np.abs(a - b)) < 1e-12, "sin saturación el anti-windup no actúa")
    print(f"sin saturación: con y sin anti-windup idénticos (diferencia máx {np.max(np.abs(a-b)):.1e})")
    polos = np.roots([J, Kd, Kp, Ki])
    print("polos lineales:", np.round(polos, 4))
    prueba(np.all(polos.real < 0), "lazo lineal estable")

    s0, s1 = simula(umax, False), simula(umax, True)
    # (2) primer tramo: par saturado constante hasta que v baja de u_max
    t_sat = (np.nonzero(s0[1:, 3] < umax - 1e-12)[0][0] + 1) * h
    k = int(round(t_sat / h)) - 1
    th_ex = 0.5 * (umax / J) * (k * h) ** 2
    print(f"par saturado (0.2 N m) durante {t_sat:.2f} s; theta(t) = (u_max/2J) t^2: simulado {s0[k,0]:.9f}, cerrado {th_ex:.9f}")
    prueba(abs(s0[k, 0] - th_ex) < 1e-9, "tramo saturado uniformemente acelerado")

    print("                      sobreimpulso   asentamiento 2 % (s)   xi máx (rad s)")
    nombres = ("lineal ideal (sin límite)", "con saturación, sin AW", "con saturación, con AW")
    res = []
    for nombre, o in zip(nombres, (a, s0, s1)):
        m = metricas(o); res.append(m)
        print(f"{nombre:26s} {100*m[0]:7.1f} %      {m[1]:9.1f}            {m[2]:8.3f}")
    prueba(res[2][0] <= res[1][0] + 1e-12, "el anti-windup no empeora el sobreimpulso")
    prueba(res[1][2] > res[2][2], "la integral crece menos con anti-windup")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
