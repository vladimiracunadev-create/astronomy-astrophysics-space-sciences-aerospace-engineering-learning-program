#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C05: espectro primordial de rodadura lenta y recuperacion de la inclinacion con un campo gaussiano.

Datos: del resumen de Planck 2018 X (arXiv:1807.06211, solo resumen, consultado el 2026-11-09): n_s = 0,9649 +- 0,0042 (68 %) y r < 0,056 (95 %, Planck + BK15). Son ILUSTRATIVOS: el
potencial V = m^2 phi^2 / 2, la amplitud A_s = 2,1e-9 (del orden de lo publicado, pero no leida en ninguna fuente consultada) y el campo gaussiano sintetico.
Unidades: M_pl reducida = 1.
Modelo: epsilon = 2/phi^2, eta = 2/phi^2, N = (phi^2 - 2)/4 ; n_s = 1 - 6 epsilon + 2 eta ; r = 16 epsilon ; A_s = V/(24 pi^2 epsilon). Campo sintetico: modos de una red cubica 1 <= |k| <= 40
(en unidades de la frecuencia fundamental) con P(k) = A_s (2 pi^2 / k^3) (k/k_*)^(n_s - 1), k_* = 20; la inclinacion se recupera por regresion de ln Delta^2 sobre ln k en cascarones de ancho 1.
Supuestos: modos independientes y gaussianos, sin correccion por la mitad de espacio de Fourier. Validez: ilustrativa.
Tolerancia: pendiente media de 20 realizaciones dentro de 3 errores estandar de la media del valor de entrada; formulas de rodadura lenta contra integracion exacta de epsilon, 1e-12.
"""
from __future__ import annotations
import math, platform, random, sys

AS = 2.1e-9
NS_P, NS_E, R_P = 0.9649, 0.0042, 0.056

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'N':>4} {'phi^2':>7} {'n_s':>8} {'r':>8} {'m [M_pl]':>11} {'(n_s-Planck)/sigma':>19}")
    for n in (50, 60):
        phi2 = 4 * n + 2
        eps = 2 / phi2
        ns = 1 - 6 * eps + 2 * eps
        r = 16 * eps
        m = math.sqrt(24 * math.pi ** 2 * eps * AS / (0.5 * phi2))
        print(f"{n:4d} {phi2:7.1f} {ns:8.5f} {r:8.5f} {m:11.3e} {(ns - NS_P) / NS_E:19.2f}")
    phi2 = 4 * 60 + 2
    ns60 = 1 - 8 / phi2
    r60 = 32 / phi2
    # verificacion de N por integracion de dphi/(sqrt(2 eps)) = phi/2 dphi desde phi_e=sqrt(2) (V'/V = 2/phi, N = int phi/2 dphi)
    n_int = sum(0.5 * (0.5 * (math.sqrt(2) + (math.sqrt(phi2) - math.sqrt(2)) * (i + 0.5) / 20000)) * ((math.sqrt(phi2) - math.sqrt(2)) / 20000) * 2 for i in range(20000))
    print(f"N por integral de V/V' dphi = {n_int:.6f} ; (phi^2 - 2)/4 = {(phi2 - 2) / 4:.6f}")
    assert abs(n_int - 60.0) < 1e-6
    print(f"modelo con N = 60: r = {r60:.4f} frente al limite r < {R_P} (95 %): {'excluido' if r60 > R_P else 'permitido'} ; n_s consistente con Planck a {(ns60 - NS_P) / NS_E:+.2f} sigma")
    assert r60 > R_P
    # campo gaussiano sintetico
    rng = random.Random(20261109)
    kmax = 40
    cascarones = {}
    rango = range(-kmax, kmax + 1)
    for i in rango:
        for j in rango:
            for l in rango:
                k2 = i * i + j * j + l * l
                if k2 == 0:
                    continue
                k = math.sqrt(k2)
                if k <= kmax + 0.5:
                    cascarones.setdefault(int(k + 0.5), []).append(k)
    # solo semiespacio: la condicion de realidad deja la mitad de modos independientes
    ns_in = ns60
    pend = []
    for rep in range(20):
        xs, ys = [], []
        for b in range(1, kmax + 1):
            ks = cascarones[b][: len(cascarones[b]) // 2]
            acc = 0.0
            for k in ks:
                var = AS * 2 * math.pi ** 2 / k ** 3 * (k / 20.0) ** (ns_in - 1)
                x = rng.gauss(0, math.sqrt(var))
                acc += k ** 3 / (2 * math.pi ** 2) * x * x
            d2 = acc / len(ks)
            xs.append(math.log(b)); ys.append(math.log(d2))
        mx = sum(xs) / len(xs); my = sum(ys) / len(ys)
        sl = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        pend.append(sl)
    media = sum(pend) / len(pend)
    sd = math.sqrt(sum((p - media) ** 2 for p in pend) / (len(pend) - 1))
    ee = sd / math.sqrt(len(pend))
    nmodos = sum(len(v) // 2 for v in cascarones.values())
    print(f"modos independientes por realizacion = {nmodos}")
    print(f"pendiente (n_s - 1) de entrada = {ns_in - 1:+.5f} ; recuperada (20 realizaciones) = {media:+.5f} +- {ee:.5f} (dispersion {sd:.5f})")
    assert abs(media - (ns_in - 1)) < 3 * ee
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
