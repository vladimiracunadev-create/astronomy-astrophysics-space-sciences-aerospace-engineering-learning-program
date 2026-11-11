#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C22: eje del estres con retroalimentacion negativa: cortisol circadiano y respuesta a un estresor (modelo DIDACTICO, SINTETICO).

Modelo de una variable C (cortisol relativo, sin unidades) con entrada circadiana y retroalimentacion: dC/dt = a u(t) / (1 + g C) - C / tau, donde
u(t) = 1 + A cos(2 pi (t - t0)/24) + S(t); A = 0.8 (amplitud), t0 = 8 h (pico matutino), tau = 1.5 h (semivida ~ 1 h, ILUSTRATIVA), g = 1.0 (ganancia de retroalimentacion),
a = escala elegida para que el promedio de C sea ~ 1. S(t) = 1.0 entre las 14 y las 16 h (estresor agudo) o 0.5 durante 7 dias (estres cronico). Integracion de Euler con dt = 0.01 h.
Todo es SINTETICO/ILUSTRATIVO: no hay mediciones de cortisol. Contenido educativo; no es una prueba diagnostica. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

A, T0, TAU = 0.8, 8.0, 1.5


def simular(g, dias=3, estres=None, a=None, dt=0.01):
    n = int(dias * 24 / dt)
    t = np.arange(n) * dt
    s = np.zeros(n) if estres is None else estres(t)
    u = 1 + A * np.cos(2 * np.pi * (t - T0) / 24) + s
    c = np.zeros(n)
    c[0] = 1.0
    for i in range(1, n):
        c[i] = c[i - 1] + dt * (a * u[i - 1] / (1 + g * c[i - 1]) - c[i - 1] / TAU)
    return t, c


def calibrar(g):
    a = 1.0
    for _ in range(40):
        t, c = simular(g, 3, None, a)
        m = c[len(c) // 3:].mean()
        a *= 1.0 / m
    return a


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: sin mediciones de cortisol; no es una prueba diagnostica")
    res = {}
    for g in (0.0, 1.0, 3.0):
        a = calibrar(g)
        t, c = simular(g, 3, None, a)
        d3 = c[2 * 2400:]
        tt = t[2 * 2400:] - 48
        pico_h = tt[np.argmax(d3)]
        print(f"g = {g:3.1f}: a = {a:6.3f}; dia 3: media {d3.mean():.3f}, maximo {d3.max():.3f} a las {pico_h:5.2f} h, minimo {d3.min():.3f} (amplitud pico-valle {d3.max() - d3.min():.3f})")
        agudo = lambda tt_, : np.where((tt_ % 24 >= 14) & (tt_ % 24 < 16) & (tt_ >= 24) & (tt_ < 48), 1.0, 0.0)
        t2, c2 = simular(g, 3, agudo, a)
        base = c[2400:4800]; con = c2[2400:4800]
        auc_b, auc_c = np.trapezoid(base, dx=0.01), np.trapezoid(con, dx=0.01)
        pico = (con - base).max()
        print(f"        estresor agudo (u + 1,0 de 14 a 16 h del dia 2): aumento maximo {pico:.3f}; AUC diaria {auc_b:.2f} -> {auc_c:.2f} ({100 * (auc_c / auc_b - 1):+.1f} %)")
        res[g] = (pico, auc_c / auc_b - 1)
    # retraso de la recuperacion: tiempo en que la diferencia cae a 10 % del maximo
    g = 1.0
    a = calibrar(g)
    agudo = lambda tt_: np.where((tt_ >= 38) & (tt_ < 40), 1.0, 0.0)
    t, c = simular(g, 3, None, a); t2, c2 = simular(g, 3, agudo, a)
    dif = c2 - c
    imax = np.argmax(dif)
    despues = np.where(dif[imax:] < 0.1 * dif[imax])[0][0] * 0.01
    print(f"g = 1.0: tras un estresor de 2 h (t = 38-40 h), el aumento maximo es {dif[imax]:.3f} a las {t[imax]:.2f} h y cae al 10 % en {despues:.2f} h")
    # estres cronico: u + 0.5 durante 7 dias
    cron = lambda tt_: np.full_like(tt_, 0.5)
    t, cb = simular(g, 7, None, a); t, cc = simular(g, 7, cron, a)
    print(f"Estres cronico (+0.5 durante 7 dias, g = 1): media diaria del dia 7: {cb[-2400:].mean():.3f} -> {cc[-2400:].mean():.3f} ({100 * (cc[-2400:].mean() / cb[-2400:].mean() - 1):+.1f} %); amplitud pico-valle {cb[-2400:].max() - cb[-2400:].min():.3f} -> {cc[-2400:].max() - cc[-2400:].min():.3f}")
    # desfase del pico matutino por un salto de fase de 6 h
    print("Pico matutino: si el reloj se retrasa 6 h (t0 = 14 h), el maximo se desplaza ~6 h (por construccion).")
    assert res[3.0][0] < res[0.0][0]
    assert res[1.0][0] < res[0.0][0]
    assert all(v[1] > 0 for v in res.values())
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
