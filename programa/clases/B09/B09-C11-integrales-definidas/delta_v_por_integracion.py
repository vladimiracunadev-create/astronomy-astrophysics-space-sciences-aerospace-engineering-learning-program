#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C11: integral definida y cuadratura numérica.

Datos: pulso de aceleración propia SINTÉTICO a(t) = A sin(pi t / T), A = 30 m/s2,
T = 60 s (sin gravedad ni arrastre). Muestras con ruido SIMULADAS:
random.Random(2026).gauss(0, 0.3 m/s2) a 10 Hz. g_n = 9.80665 m/s2 (CODATA 2022).
Modelo: Delta v = int_0^T a dt = 2 A T / pi (exacto, por antiderivada).
Métodos: Riemann izquierda/derecha, punto medio, trapecio y Simpson compuestos.
Supuestos: a(t) integrable y continua; Simpson requiere n par. Validez: pulso
suave. Tolerancias: errores teóricos O(h) para Riemann, O(h^2) para
punto medio/trapecio y O(h^4) para Simpson (órdenes observados entre 0.9 y 4.2).
"""
from __future__ import annotations
import math, platform, random, sys

A, T = 30.0, 60.0
EXACTO = 2 * A * T / math.pi


def a(t):
    return A * math.sin(math.pi * t / T)


def izq(f, lo, hi, n):
    h = (hi - lo) / n
    return h * sum(f(lo + i * h) for i in range(n))


def der(f, lo, hi, n):
    h = (hi - lo) / n
    return h * sum(f(lo + (i + 1) * h) for i in range(n))


def medio(f, lo, hi, n):
    h = (hi - lo) / n
    return h * sum(f(lo + (i + 0.5) * h) for i in range(n))


def trap(f, lo, hi, n):
    h = (hi - lo) / n
    return h * (0.5 * (f(lo) + f(hi)) + sum(f(lo + i * h) for i in range(1, n)))


def simpson(f, lo, hi, n):
    assert n % 2 == 0
    h = (hi - lo) / n
    s = f(lo) + f(hi)
    s += 4 * sum(f(lo + i * h) for i in range(1, n, 2))
    s += 2 * sum(f(lo + i * h) for i in range(2, n, 2))
    return s * h / 3


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    print(f"Delta v exacto = 2 A T / pi = {EXACTO:.6f} m/s")
    metodos = {"izquierda": izq, "derecha": der, "punto medio": medio, "trapecio": trap, "simpson": simpson}
    TAU = 20.0
    b = lambda t: A * math.exp(-t / TAU)                 # empuje decreciente SINTÉTICO
    exb = A * TAU * (1 - math.exp(-T / TAU))
    casos = (("pulso seno (extremos en 0)", a, EXACTO), ("decaimiento exponencial tau = 20 s", b, exb))
    ords_todos = {}
    for nombre, f, ex in casos:
        print(f"\n{nombre}: exacto = {ex:.6f} m/s")
        print("  n   " + "  ".join(f"{k:>13s}" for k in metodos))
        previo, ords = {}, {}
        for n in (4, 8, 16, 32, 64):
            fila = []
            for k, m in metodos.items():
                err = abs(m(f, 0.0, T, n) - ex)
                if k in previo and err > 1e-12:
                    ords[k] = math.log2(previo[k] / err)
                previo[k] = err
                fila.append(f"{err:13.3e}")
            print(f"{n:4d}  " + "  ".join(fila))
        print("órdenes observados (último paso): " + ", ".join(f"{k} {v:.2f}" for k, v in ords.items()))
        ords_todos[nombre] = ords
    o = ords_todos["decaimiento exponencial tau = 20 s"]
    prueba(0.9 < o["izquierda"] < 1.2 and 1.8 < o["trapecio"] < 2.2 and 1.8 < o["punto medio"] < 2.2 and 3.5 < o["simpson"] < 4.3,
           "órdenes de convergencia")
    prueba(abs(simpson(a, 0, T, 64) - EXACTO) < 1e-6 * EXACTO, "Simpson n = 64")
    # propiedades
    prueba(abs(simpson(a, 0, 20, 64) + simpson(a, 20, T, 64) - EXACTO) < 1e-6 * EXACTO, "aditividad")
    prueba(abs(simpson(a, T, 0, 64) + EXACTO) < 1e-6 * EXACTO, "inversión de límites")
    print(f"Aceleración media = Delta v / T = {EXACTO/T:.4f} m/s2 (= 2A/pi = {2*A/math.pi:.4f})")
    print(f"En unidades g: A = {A/9.80665:.4f} g; integral = {EXACTO/9.80665:.3f} g s")
    # 8 muestras a 1 s: trapecio y Simpson
    f8 = lambda t: 30.0 * math.sin(math.pi * t / 8.0)
    ex8 = 2 * 30.0 * 8.0 / math.pi
    t8, s8 = trap(f8, 0, 8, 8), simpson(f8, 0, 8, 8)
    print(f"\nPulso de 8 s muestreado a 1 s: exacto {ex8:.4f}; trapecio {t8:.4f} ({t8/ex8-1:+.2%}); Simpson {s8:.4f} ({s8/ex8-1:+.3%})")
    # ruido simulado
    rng = random.Random(2026)
    sigma, dt = 0.3, 0.1
    n = int(T / dt)
    muestras = [a(i * dt) + rng.gauss(0, sigma) for i in range(n + 1)]
    dv_ruido = dt * (0.5 * (muestras[0] + muestras[-1]) + sum(muestras[1:-1]))
    esperado = sigma * dt * math.sqrt(n)
    print(f"Trapecio con ruido simulado (sigma = 0.3 m/s2 a 10 Hz): {dv_ruido:.4f} m/s; error = {dv_ruido-EXACTO:+.4f} m/s; sigma esperada del error = {esperado:.4f} m/s")
    prueba(abs(dv_ruido - EXACTO) < 5 * esperado, "error por ruido compatible")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
