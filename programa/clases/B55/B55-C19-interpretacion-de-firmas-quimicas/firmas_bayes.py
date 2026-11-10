#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C19: razonamiento bayesiano sobre una firma quimica SINTETICA con dos procesos hipoteticos A y B.

Datos: SINTETICOS. Un indicador x (por ejemplo, una razon medida entre dos familias de compuestos) se distribuye de forma normal con media mu_A = 1.0 y sigma_A = 0.30 bajo el proceso A
y mu_B = 1.8 y sigma_B = 0.30 bajo el proceso B; la medicion es x = 1.5 +- 0.20 (suma en cuadratura con sigma). Todo es inventado: los procesos A y B no representan ningun proceso real
y la clase NO infiere vida ni ningun origen real.
Modelo: P(H|x) = P(x|H) P(H) / sum P(x|H') P(H'). Verosimilitud normal con varianza total sigma_H^2 + sigma_med^2. Factor de Bayes BF = P(x|B)/P(x|A).
Comprobacion independiente: integracion numerica del marginal sobre la media (rejilla) y comparacion con la formula cerrada.
Supuestos: hipotesis exhaustivas y excluyentes (A o B), modelos de verosimilitud correctos. Validez: ilustrativa.
Tolerancia: posterior cerrado vs integracion numerica a 1e-6; suma de posteriores igual a 1 a 1e-12.
"""
from __future__ import annotations
import math, platform

MU = {"A": 1.0, "B": 1.8}
SIG = {"A": 0.30, "B": 0.30}
X, SM = 1.5, 0.20

def normal(x, mu, s):
    return math.exp(-0.5 * ((x - mu) / s) ** 2) / (s * math.sqrt(2 * math.pi))

def like_cerrada(h, x=X, sm=SM):
    return normal(x, MU[h], math.sqrt(SIG[h] ** 2 + sm ** 2))

def like_numerica(h, x=X, sm=SM, n=20000):
    """int N(x | m, sm) N(m | mu_h, sig_h) dm por trapecio."""
    lo, hi = MU[h] - 8 * SIG[h], MU[h] + 8 * SIG[h]
    d = (hi - lo) / n
    s = 0.0
    for i in range(n + 1):
        m = lo + i * d
        w = 0.5 if i in (0, n) else 1.0
        s += w * normal(x, m, sm) * normal(m, MU[h], SIG[h])
    return s * d

def posterior(prior_a, like):
    num_a = like("A") * prior_a
    num_b = like("B") * (1 - prior_a)
    z = num_a + num_b
    return num_a / z, num_b / z

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("A. Dos procesos hipoteticos SINTETICOS: A (mu 1.0, sigma 0.30) y B (mu 1.8, sigma 0.30); medicion x = 1.5 +- 0.20")
    la, lb = like_cerrada("A"), like_cerrada("B")
    na, nb = like_numerica("A"), like_numerica("B")
    print(f"B. Verosimilitud cerrada: P(x|A) = {la:.6f} ; P(x|B) = {lb:.6f} ; numerica: {na:.6f} ; {nb:.6f}")
    assert abs(la - na) / la < 1e-6 and abs(lb - nb) / lb < 1e-6
    bf = lb / la
    print(f"   Factor de Bayes BF = P(x|B)/P(x|A) = {bf:.4f}")
    print("C. Posterior segun el prior P(A)")
    print("P(A) prior   P(A|x)    P(B|x)")
    prev = None
    for pa in (0.1, 0.3, 0.5, 0.7, 0.9, 0.99):
        a, b = posterior(pa, like_cerrada)
        assert abs(a + b - 1.0) < 1e-12
        a2, b2 = posterior(pa, like_numerica)
        assert abs(a - a2) < 1e-6
        print(f"{pa:9.2f}    {a:.4f}    {b:.4f}")
        if prev is not None:
            assert a > prev
        prev = a
    # barrido de la medicion
    print("D. Efecto de la medicion (prior 50/50)")
    print("x       P(A|x)    P(B|x)")
    for x in (0.8, 1.2, 1.4, 1.5, 1.6, 1.9, 2.3):
        a, b = posterior(0.5, lambda h: like_cerrada(h, x))
        print(f"{x:4.1f}    {a:.4f}    {b:.4f}")
    # punto de indiferencia
    lo, hi = 1.0, 1.8
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        a, b = posterior(0.5, lambda h: like_cerrada(h, mid))
        if a > b:
            lo = mid
        else:
            hi = mid
    print(f"E. Punto de indiferencia (prior 50/50): x = {0.5 * (lo + hi):.4f} (punto medio de las medias = {(MU['A'] + MU['B']) / 2:.4f})")
    assert abs(0.5 * (lo + hi) - 1.4) < 1e-9
    # prior necesario para P(B|x)=0.99
    odds = 99.0 / bf
    pb = odds / (1 + odds)
    print(f"F. Prior P(B) minimo para que P(B|x) >= 0.99: {pb:.4f} (es decir P(A) <= {1 - pb:.4f})")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
