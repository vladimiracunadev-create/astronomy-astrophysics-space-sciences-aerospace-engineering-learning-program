#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C19: SIG y analisis de riesgo: amenaza x exposicion x vulnerabilidad, pesos AHP y sensibilidad.

Datos: SINTETICOS. Tres capas de 60 x 60 celdas (amenaza, exposicion, vulnerabilidad) en [0, 1] generadas con funciones suaves y ruido (semilla 57);
cuatro zonas administrativas ficticias (cuadrantes). La matriz de comparacion pareada y el indice aleatorio de Saaty para n = 3 (0.58) son
conocimiento general NO CONSULTADO en esta sesion.
Modelo: riesgo multiplicativo R = H E V y riesgo aditivo ponderado R_w = w1 H + w2 E + w3 V con pesos AHP (vector propio principal por iteracion de potencias);
razon de consistencia CR = ((lambda_max - n)/(n - 1))/RI ; sensibilidad: perturbar pesos +-20 % y medir el solape del 10 % de celdas de mayor riesgo.
Validez: capas independientes y normalizadas; no hay datos reales ni se evalua ningun lugar. Tolerancia: para una matriz consistente los pesos
coinciden con la media geometrica a 1e-9 y CR = 0.
Requiere numpy.
"""
import platform
import numpy as np

N = 60


def capas(rng):
    y, x = np.mgrid[:N, :N] / (N - 1)
    h = np.exp(-((x - 0.3) ** 2 + (y - 0.6) ** 2) / 0.08) + 0.05 * rng.standard_normal((N, N))
    e = np.exp(-((x - 0.5) ** 2 + (y - 0.5) ** 2) / 0.12) + 0.05 * rng.standard_normal((N, N))
    v = 0.3 + 0.5 * x + 0.05 * rng.standard_normal((N, N))
    return [np.clip(a, 0, 1) for a in (h, e, v)]


def ahp(M):
    M = np.array(M, float)
    n = len(M)
    w = np.ones(n) / n
    for _ in range(500):
        w2 = M @ w
        w2 /= w2.sum()
        if np.max(np.abs(w2 - w)) < 1e-14:
            break
        w = w2
    lam = float((M @ w / w).mean())
    ri = {3: 0.58}[n]
    return w, lam, (lam - n) / (n - 1) / ri


def top(r, frac=0.10):
    k = int(r.size * frac)
    idx = np.argsort(r.ravel())[-k:]
    s = np.zeros(r.size, bool)
    s[idx] = True
    return s


def calcular():
    r = {}
    rng = np.random.default_rng(57)
    H, E, V = capas(rng)
    Mc = [[1, 2, 4], [0.5, 1, 2], [0.25, 0.5, 1]]
    w, lam, cr = ahp(Mc)
    gm = np.array([np.prod(row) ** (1 / 3) for row in Mc])
    gm /= gm.sum()
    r["w"], r["lam_c"], r["cr_c"] = w, lam, cr
    r["w_txt"] = " ; ".join(f"{x:.3f}".replace(".", ",") for x in w)
    r["err_gm"] = float(np.max(np.abs(w - gm)))
    Mi = [[1, 3, 0.5], [1 / 3, 1, 4], [2, 0.25, 1]]
    wi, lami, cri = ahp(Mi)
    r["lam_i"], r["cr_i"] = lami, cri
    R_mult = H * E * V
    R_add = w[0] * H + w[1] * E + w[2] * V
    t1, t2 = top(R_mult), top(R_add)
    r["solape_metodos"] = float((t1 & t2).sum() / t1.sum())
    pesos = []
    base = top(R_add)
    solapes = []
    for _ in range(200):
        p = w * (1 + 0.2 * rng.uniform(-1, 1, 3))
        p /= p.sum()
        solapes.append((top(p[0] * H + p[1] * E + p[2] * V) & base).sum() / base.sum())
    r["solape_sens_min"], r["solape_sens_media"] = float(min(solapes)), float(np.mean(solapes))
    zonas = {}
    m = N // 2
    for nom, (a, b) in {"NO": (slice(0, m), slice(0, m)), "NE": (slice(0, m), slice(m, N)), "SO": (slice(m, N), slice(0, m)), "SE": (slice(m, N), slice(m, N))}.items():
        zonas[nom] = float(R_add[a, b].mean())
    r["zonas"] = zonas
    r["zona_max"] = max(zonas, key=zonas.get)
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Matriz consistente: pesos = {r['w'].round(6).tolist()} ; lambda_max = {r['lam_c']:.6f} ; CR = {r['cr_c']:.2e} ; diferencia con media geometrica = {r['err_gm']:.1e}")
    print(f"Matriz inconsistente: lambda_max = {r['lam_i']:.3f} ; CR = {r['cr_i']:.2f} (se acepta CR < 0.10)")
    print(f"Solape del 10 % de mayor riesgo entre metodo multiplicativo y aditivo = {r['solape_metodos']*100:.1f} %")
    print(f"Perturbando los pesos +-20 %: solape minimo = {r['solape_sens_min']*100:.1f} % ; medio = {r['solape_sens_media']*100:.1f} %")
    print("Riesgo medio por zona (aditivo): " + " ; ".join(f"{k} = {v:.3f}" for k, v in r["zonas"].items()) + f" ; mayor: {r['zona_max']}")
    assert r["err_gm"] < 1e-9 and abs(r["cr_c"]) < 1e-9
    assert r["cr_i"] > 0.10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
