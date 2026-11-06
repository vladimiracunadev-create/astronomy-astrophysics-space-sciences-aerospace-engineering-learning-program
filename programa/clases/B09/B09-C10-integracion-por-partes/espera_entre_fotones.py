#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B09-C10: integración por partes y tiempo de espera entre fotones.

Datos: SIMULADOS. Tasa de conteo lambda = 100 s^-1 (sintética). Los tiempos de
espera se generan con random.Random(12345).expovariate(lambda), 200 000 muestras.
Modelo: densidad exponencial f(t) = lambda exp(-lambda t), t >= 0 (la forma
con mu = 0 y beta = 1/lambda de la distribución exponencial del NIST/SEMATECH
e-Handbook de métodos estadísticos, sección 1.3.6.6.7).
Media: int t f dt = 1/lambda ; segundo momento: int t^2 f dt = 2/lambda^2,
ambos por partes. Varianza = 1/lambda^2.
Supuestos: llegadas independientes (proceso de Poisson), tasa constante, sin
tiempo muerto. Validez: fuentes estables y detector lineal.
Tolerancias: antiderivadas a 1e-6 relativa; media simulada dentro de 4 sigma
estadísticos (sigma = (1/lambda)/sqrt(N)).
"""
from __future__ import annotations
import math, platform, random, sys

LAM, N = 100.0, 200_000


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def central(F, x, h=1e-5):
    return (F(x + h) - F(x - h)) / (2 * h)


def trapecio(f, a, b, n=400_000):
    h = (b - a) / n
    return h * (0.5 * (f(a) + f(b)) + sum(f(a + i * h) for i in range(1, n)))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}")
    # antiderivadas por partes, comprobadas derivando
    pares = {
        "x sin x": (lambda x: x * math.sin(x), lambda x: -x * math.cos(x) + math.sin(x)),
        "ln x": (math.log, lambda x: x * math.log(x) - x),
        "x^2 e^x": (lambda x: x * x * math.exp(x), lambda x: (x * x - 2 * x + 2) * math.exp(x)),
        "t e^(-lam t)": (lambda t: t * math.exp(-LAM * t),
                         lambda t: -(t / LAM + 1 / LAM**2) * math.exp(-LAM * t)),
    }
    for nombre, (f, F) in pares.items():
        for x in (0.5, 1.3, 2.7) if nombre != "t e^(-lam t)" else (0.003, 0.01, 0.05):
            prueba(abs(central(F, x, 1e-6 if nombre != "t e^(-lam t)" else 1e-8) - f(x)) <= 1e-5 * max(1, abs(f(x))) + 1e-9,
                   f"F' = f en {nombre}")
        print(f"int {nombre} dx: antiderivada comprobada derivando")
    # momentos analíticos y numéricos
    T = 1.0                                   # 100 / lambda de sobra
    f = lambda t: LAM * math.exp(-LAM * t)
    m1 = trapecio(lambda t: t * f(t), 0.0, T)
    m2 = trapecio(lambda t: t * t * f(t), 0.0, T)
    var = m2 - m1 * m1
    print(f"\nmedia  : analítica {1/LAM:.8f} s  trapecio {m1:.8f} s")
    print(f"var    : analítica {1/LAM**2:.8e} s2  trapecio {var:.8e} s2")
    prueba(abs(m1 - 1 / LAM) < 1e-8 and abs(var - 1 / LAM**2) < 1e-10, "momentos")
    # simulación
    rng = random.Random(12345)
    xs = [rng.expovariate(LAM) for _ in range(N)]
    media = sum(xs) / N
    sigma = (1 / LAM) / math.sqrt(N)
    dev = (media - 1 / LAM) / sigma
    print(f"\nSimulación (N = {N}): media = {media:.6e} s (esperada {1/LAM:.6e}); desviación = {dev:+.2f} sigma")
    prueba(abs(dev) < 4, "media simulada compatible")
    frac = sum(1 for x in xs if x > 0.03) / N
    print(f"P(espera > 30 ms): simulada {frac:.4f}, analítica exp(-3) = {math.exp(-3):.4f}")
    prueba(abs(frac - math.exp(-3)) < 4 * math.sqrt(math.exp(-3) * (1 - math.exp(-3)) / N), "cola")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
