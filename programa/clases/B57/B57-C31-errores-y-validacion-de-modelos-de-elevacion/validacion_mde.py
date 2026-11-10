#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C31: errores y validacion de modelos de elevacion: RMSE, NMAD, LE90 y robustez frente a valores atipicos.

Datos: la exactitud vertical absoluta del Copernicus DEM es inferior a 4 m (90 % de error lineal, LE90) segun la pagina consultada el 2026-11-09. SINTETICOS: errores de un MDE
frente a 400 puntos de control, gaussianos de media 0.5 m y desviacion 2.0 m, mas un 3 % de valores atipicos de +-20 m; semilla fija 57.
Modelo: ME = media del error ; RMSE = raiz de la media del cuadrado ; MAE ; NMAD = 1.4826 mediana(|e - mediana(e)|) ; LE90 = percentil 90 de |e - sesgo| (aqui |e|, sin quitar el sesgo) ;
para gaussianas sin sesgo LE90 = 1.6449 sigma ; intervalo de confianza del RMSE por remuestreo (bootstrap, 2000).
Validez: errores independientes de los puntos de control, que se suponen sin error. Tolerancia: sin valores atipicos NMAD ~ sigma (3 %) y LE90 ~ 1.645 sigma (4 %) para un MDE sin sesgo.
Requiere numpy.
"""
import math, platform
import numpy as np


def metricas(e):
    me = float(e.mean())
    rmse = float(np.sqrt(np.mean(e**2)))
    mae = float(np.mean(np.abs(e)))
    nmad = float(1.4826 * np.median(np.abs(e - np.median(e))))
    le90 = float(np.percentile(np.abs(e), 90))
    return dict(me=me, rmse=rmse, mae=mae, nmad=nmad, le90=le90)


def calcular():
    r = {}
    rng = np.random.default_rng(57)
    n = 400
    gauss0 = 2.0 * rng.standard_normal(200000)
    r["m0"] = metricas(gauss0)
    r["le90_teo"] = 1.6449 * 2.0
    e = 0.5 + 2.0 * rng.standard_normal(n)
    r["m1"] = metricas(e)
    e2 = e.copy()
    idx = rng.choice(n, int(0.03 * n), replace=False)
    e2[idx] = rng.choice([-20.0, 20.0], idx.size)
    r["m2"] = metricas(e2)
    boot = [np.sqrt(np.mean(rng.choice(e, n) ** 2)) for _ in range(2000)]
    r["rmse_ic"] = (float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5)))
    r["rmse_ana_se"] = 2.0 / math.sqrt(2 * n)
    r["rmse_boot_se"] = float(np.std(boot))
    r["cumple_4m_1"] = r["m1"]["le90"] < 4.0
    r["cumple_4m_2"] = r["m2"]["le90"] < 4.0
    r["rmse_ic0"], r["rmse_ic1"] = r["rmse_ic"]
    r["cumple2_txt"] = "cumple" if r["cumple_4m_2"] else "no cumple"
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    m0, m1, m2 = r["m0"], r["m1"], r["m2"]
    print(f"Gaussiana sin sesgo (sigma = 2 m, 200000 puntos): RMSE = {m0['rmse']:.3f} ; NMAD = {m0['nmad']:.3f} ; LE90 = {m0['le90']:.3f} (teoria 1.645 sigma = {r['le90_teo']:.3f})")
    print(f"400 puntos, sesgo 0.5 m, sin atipicos: ME = {m1['me']:.3f} ; RMSE = {m1['rmse']:.3f} ; MAE = {m1['mae']:.3f} ; NMAD = {m1['nmad']:.3f} ; LE90 = {m1['le90']:.3f}")
    print(f"400 puntos con 3 % de atipicos de +-20 m: ME = {m2['me']:.3f} ; RMSE = {m2['rmse']:.3f} ; MAE = {m2['mae']:.3f} ; NMAD = {m2['nmad']:.3f} ; LE90 = {m2['le90']:.3f}")
    print(f"IC 95 % del RMSE (bootstrap) sin atipicos = [{r['rmse_ic'][0]:.3f}, {r['rmse_ic'][1]:.3f}] ; error estandar bootstrap = {r['rmse_boot_se']:.3f} ; analitico sigma/sqrt(2n) = {r['rmse_ana_se']:.3f}")
    print(f"Cumple LE90 < 4 m: sin atipicos = {r['cumple_4m_1']} ; con atipicos = {r['cumple_4m_2']}")
    assert abs(m0["nmad"] / 2.0 - 1) < 0.03
    assert abs(m0["le90"] / r["le90_teo"] - 1) < 0.04
    assert m2["rmse"] > 1.5 * m2["nmad"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
