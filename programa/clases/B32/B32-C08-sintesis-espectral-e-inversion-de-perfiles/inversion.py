#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B32-C08: sintesis de una linea con el modelo de Milne-Eddington e inversion por minimos cuadrados.

Datos: ninguna constante fisica. Los parametros de la linea (B0 = 1.0, B1 = 0.6, eta0 = 2.0, ancho 0.05, centro 0.0 en unidades arbitrarias), el ruido (sigma = 0.005) y la semilla fija
son ILUSTRATIVOS (sinteticos); no se invierte ningun espectro real.
Modelo: intensidad emergente en mu = 1 I(x) = B0 + B1/(1 + eta0 phi(x)) con phi gaussiano de ancho w y centro x0; sintesis con ruido gaussiano; inversion de (eta0, w, x0) con
busqueda de Nelder-Mead propia (sin bibliotecas) sobre la suma de cuadrados; comparacion con los parametros verdaderos y con el error esperado.
Supuestos: B0 y B1 conocidos, perfil gaussiano. Validez: ilustrativa.
Tolerancia: parametros recuperados dentro de 4 errores estandar de bootstrap de 30 repeticiones; chi^2 reducido entre 0.8 y 1.2.
"""
from __future__ import annotations
import math, platform, random, sys
B0, B1 = 1.0, 0.6
XS = [-0.3 + 0.01 * i for i in range(61)]

def modelo(p, x):
    eta, w, x0 = p
    return B0 + B1 / (1 + eta * math.exp(-0.5 * ((x - x0) / w) ** 2))

def chi2(p, dat, s):
    if p[0] < 0 or p[1] <= 0.005:
        return 1e18
    return sum(((modelo(p, x) - d) / s) ** 2 for x, d in zip(XS, dat))

def nelder(f, x0, paso, it=600):
    n = len(x0)
    sim = [list(x0)] + [[x0[j] + (paso[j] if j == i else 0) for j in range(n)] for i in range(n)]
    for _ in range(it):
        sim.sort(key=f)
        c = [sum(s[j] for s in sim[:-1]) / n for j in range(n)]
        r = [c[j] + (c[j] - sim[-1][j]) for j in range(n)]
        if f(r) < f(sim[0]):
            e = [c[j] + 2 * (c[j] - sim[-1][j]) for j in range(n)]
            sim[-1] = e if f(e) < f(r) else r
        elif f(r) < f(sim[-2]):
            sim[-1] = r
        else:
            k = [c[j] + 0.5 * (sim[-1][j] - c[j]) for j in range(n)]
            if f(k) < f(sim[-1]):
                sim[-1] = k
            else:
                sim = [sim[0]] + [[sim[0][j] + 0.5 * (s[j] - sim[0][j]) for j in range(n)] for s in sim[1:]]
    sim.sort(key=f)
    return sim[0]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ver = [2.0, 0.05, 0.0]
    s = 0.005
    rng = random.Random(20261109)
    dat = [modelo(ver, x) + rng.gauss(0, s) for x in XS]
    est = nelder(lambda p: chi2(p, dat, s), [1.0, 0.08, 0.02], [0.5, 0.02, 0.02])
    c2 = chi2(est, dat, s)
    gl = len(XS) - 3
    print(f"verdaderos: eta0 = {ver[0]}, w = {ver[1]}, x0 = {ver[2]} ; recuperados: eta0 = {est[0]:.4f}, w = {est[1]:.5f}, x0 = {est[2]:.5f} ; chi2 = {c2:.2f} con {gl} gl ; chi2 reducido = {c2 / gl:.3f}")
    assert 0.8 < c2 / gl < 1.2
    reps = []
    for _ in range(30):
        d2 = [modelo(ver, x) + rng.gauss(0, s) for x in XS]
        reps.append(nelder(lambda p: chi2(p, d2, s), est, [0.2, 0.01, 0.01]))
    print(f"{'parametro':<8} {'verdadero':>10} {'recuperado':>11} {'sigma (30 repeticiones)':>25} {'desviacion [sigma]':>20}")
    for j, nombre in enumerate(("eta0", "w", "x0")):
        m = sum(r[j] for r in reps) / len(reps)
        sd = math.sqrt(sum((r[j] - m) ** 2 for r in reps) / (len(reps) - 1))
        print(f"{nombre:<8} {ver[j]:10.4f} {est[j]:11.5f} {sd:25.5f} {abs(est[j] - ver[j]) / sd:20.2f}")
        assert abs(est[j] - ver[j]) < 4 * sd
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
