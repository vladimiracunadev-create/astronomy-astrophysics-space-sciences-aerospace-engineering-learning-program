#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C33: deforestacion y cambio de uso del suelo: area de cambio estimada con muestreo estratificado.

Datos: SINTETICOS. Mapa de verdad de 400 x 400 celdas de 30 m (14.4 km2 por mil celdas de 0.0009 km2) con bosque en t1 y una perdida verdadera de 4.0 % de las celdas;
mapa clasificado con omision del 30 % de las perdidas y comision de 0.5 % sobre el bosque estable (errores ILUSTRATIVOS). Muestreo aleatorio estratificado por clase del mapa
(perdida, bosque estable, no bosque) con 100, 150 y 100 celdas; referencia = verdad; semilla fija 57. Los estimadores del tipo de Olofsson et al. (estratificado con pesos de area)
son conocimiento general NO CONSULTADO en esta sesion.
Modelo: p_perdida = sum_h W_h p_h con p_h la proporcion de perdida verdadera en la muestra del estrato h; varianza V = sum_h W_h^2 p_h (1-p_h)/(n_h - 1) ;
IC 95 % = 1.96 sqrt(V) ; area = p x area total. Se compara con el conteo directo del mapa y con la verdad. Se repite 1000 veces para estimar la cobertura del IC.
Validez: referencia sin error, muestreo aleatorio simple dentro de cada estrato. Tolerancia: la cobertura del IC debe estar entre 85 % y 99 % (algo menor que la nominal por la aproximacion normal); el conteo del mapa debe estar sesgado.
Requiere numpy.
"""
import math, platform
import numpy as np

N = 400
AREA_CELDA = 0.0009  # km2


def mundo(rng):
    forest = np.ones((N, N), bool)
    forest[:, :80] = False  # 20 % no bosque
    loss = np.zeros((N, N), bool)
    cand = np.argwhere(forest)
    k = int(0.04 * N * N)
    idx = rng.choice(len(cand), k, replace=False)
    loss[cand[idx, 0], cand[idx, 1]] = True
    mapa_loss = loss & (rng.uniform(size=(N, N)) > 0.30)
    falsa = forest & ~loss & (rng.uniform(size=(N, N)) < 0.005)
    mapa_loss = mapa_loss | falsa
    clase = np.where(mapa_loss, 0, np.where(forest, 1, 2))  # 0 perdida, 1 bosque estable, 2 no bosque
    return loss, clase


def estimar(loss, clase, rng, nh=(100, 150, 100)):
    W = np.array([(clase == h).mean() for h in range(3)])
    p = []
    v = 0.0
    for h in range(3):
        idx = np.flatnonzero(clase.ravel() == h)
        s = rng.choice(idx, nh[h], replace=False)
        ph = loss.ravel()[s].mean()
        p.append(ph)
        v += W[h] ** 2 * ph * (1 - ph) / (nh[h] - 1)
    p_est = float(np.dot(W, p))
    return p_est, 1.96 * math.sqrt(v), W


def calcular():
    r = {}
    rng = np.random.default_rng(57)
    loss, clase = mundo(rng)
    r["verdad_pct"] = loss.mean() * 100
    r["mapa_pct"] = (clase == 0).mean() * 100
    r["sesgo_mapa_pct"] = r["mapa_pct"] - r["verdad_pct"]
    r["area_total_km2"] = N * N * AREA_CELDA
    p, ic, W = estimar(loss, clase, rng)
    r["est_pct"], r["ic_pct"] = p * 100, ic * 100
    r["area_est_km2"] = p * r["area_total_km2"]
    r["area_ver_km2"] = loss.mean() * r["area_total_km2"]
    r["W"] = W
    r["W_txt"] = "; ".join(f"{w:.4f}".replace(".", ",") for w in W)
    cub = 0
    errs = []
    for _ in range(1000):
        pp, ii, _ = estimar(loss, clase, rng)
        cub += abs(pp - loss.mean()) <= ii
        errs.append(pp - loss.mean())
    r["cobertura"] = cub / 1000
    r["sd_est_pct"] = float(np.std(errs) * 100)
    r["sesgo_est_pct"] = float(np.mean(errs) * 100)
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Verdad: perdida = {r['verdad_pct']:.3f} % de las celdas ({r['area_ver_km2']:.3f} km2 de {r['area_total_km2']:.1f} km2)")
    print(f"Conteo directo del mapa: {r['mapa_pct']:.3f} % (sesgo {r['sesgo_mapa_pct']:+.3f} puntos porcentuales)")
    print(f"Pesos de los estratos (perdida, bosque estable, no bosque): {r['W'].round(4).tolist()}")
    print(f"Estimador estratificado (una muestra de 350 celdas): {r['est_pct']:.3f} % +- {r['ic_pct']:.3f} (IC 95 %) = {r['area_est_km2']:.3f} km2")
    print(f"1000 repeticiones: sesgo = {r['sesgo_est_pct']:+.4f} puntos ; desviacion = {r['sd_est_pct']:.3f} puntos ; cobertura del IC 95 % = {r['cobertura']*100:.1f} %")
    assert 0.85 <= r["cobertura"] <= 0.99
    assert abs(r["sesgo_mapa_pct"]) > 0.3
    assert abs(r["sesgo_est_pct"]) < 0.05
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
