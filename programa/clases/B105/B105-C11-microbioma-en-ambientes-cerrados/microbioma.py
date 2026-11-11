#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C11: diversidad de un microbioma en un ambiente cerrado (comunidades SINTETICAS).

Comunidades de S = 40 taxones con abundancias relativas generadas con una distribucion log-normal normalizada (semilla 105):
A = piel de la tripulacion; B = superficies de la cabina, que reciben una fraccion m de la comunidad A mas una comunidad propia C.
Metricas: riqueza observada, Shannon H = -sum p ln p, Simpson 1 - sum p^2 y disimilitud de Bray-Curtis BC = 1 - 2 sum min(p,q)/(sum p + sum q).
Muestreo por secuenciacion simulado como multinomial con profundidad n; rarefaccion: media de 200 submuestras. Todo SINTETICO; ninguna comunidad
es una medicion. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

S = 40


def comunidad(rng, sigma):
    x = np.exp(rng.normal(0, sigma, S))
    return x / x.sum()


def shannon(p):
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def simpson(p):
    return float(1 - (p ** 2).sum())


def bray(p, q):
    return float(1 - 2 * np.minimum(p, q).sum() / (p.sum() + q.sum()))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): 40 taxones; comunidades log-normales; sin datos de secuenciacion reales")
    rng = np.random.default_rng(105)
    a = comunidad(rng, 1.2)
    c = comunidad(rng, 1.2)
    print(f"Maximos teoricos: Shannon ln(40) = {np.log(S):.3f}; Simpson 1 - 1/40 = {1 - 1 / S:.3f}")
    for m in (0.0, 0.25, 0.5, 0.75):
        b = m * a + (1 - m) * c
        print(f"fraccion de A en B m = {m:4.2f}: Shannon A {shannon(a):.3f}, B {shannon(b):.3f}; Simpson B {simpson(b):.3f}; Bray-Curtis A-B = {bray(a, b):.3f}")
    # propiedades
    assert abs(bray(a, a)) < 1e-12 and 0 <= bray(a, c) <= 1
    print("Rarefaccion de la riqueza y de Shannon de la comunidad A (200 submuestras por profundidad):")
    ref_r, ref_h = int((a > 0).sum()), shannon(a)
    prev = -1
    for n in (50, 200, 1000, 10000):
        rs, hs = [], []
        for _ in range(200):
            cnt = rng.multinomial(n, a)
            rs.append((cnt > 0).sum()); hs.append(shannon(cnt / n))
        print(f"  profundidad {n:6d}: riqueza observada {np.mean(rs):5.1f} / {ref_r}; Shannon {np.mean(hs):.3f} (verdad {ref_h:.3f}); DE {np.std(hs):.3f}")
        assert np.mean(rs) >= prev
        prev = np.mean(rs)
    # un ambiente cerrado pierde diversidad: dominancia creciente (alpha) y su efecto en H y BC
    print("Dominancia creciente (la comunidad se concentra en pocos taxones): exponente g sobre las abundancias p^g")
    hs_prev = 99
    for g in (1.0, 1.5, 2.0, 3.0):
        p = a ** g; p = p / p.sum()
        print(f"  g = {g:3.1f}: Shannon {shannon(p):.3f}; Simpson {simpson(p):.3f}; Bray-Curtis frente a g = 1: {bray(a, p):.3f}")
        assert shannon(p) <= hs_prev + 1e-12
        hs_prev = shannon(p)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
