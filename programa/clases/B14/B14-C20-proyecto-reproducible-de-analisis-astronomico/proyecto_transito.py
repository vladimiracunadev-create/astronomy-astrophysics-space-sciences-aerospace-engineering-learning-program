#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Proyecto B14-C20: análisis reproducible de un tránsito sintético, de punta a punta.

Datos: SINTÉTICOS. Curva de luz de 20 000 muestras (cadencia 10 s) de una
fuente ficticia: tránsito trapezoidal de profundidad 0.010, centro en
t = 100 000 s, duración total 8 000 s, ingreso/egreso 1 000 s, ruido
gaussiano 0.002 (semilla 20261105). No es una observación real.
Modelo: flujo = 1 - profundidad * clip((D/2 - |t - t0|)/ingreso, 0, 1), con
parámetros libres (profundidad, t0, D) y el ingreso fijo en 1 000 s;
ajuste por mínimos cuadrados con scipy.optimize.curve_fit; la incertidumbre
sale de la matriz de covarianza.
Etapas (cada una con su verificación): 1 generar, 2 huella de los datos, 3 ajuste,
4 comprobación contra la verdad conocida, 5 repetición idéntica,
6 registro de procedencia y entorno.
Supuestos: ruido gaussiano independiente; modelo correcto (datos generados con él).
Validez: demostración; en datos reales el modelo y el ruido hay que justificarlos.
Tolerancia: |estimado - verdadero| < 3 sigma para cada parámetro; dos ejecuciones
idénticas dan la misma huella de resultados; las cifras impresas no cambian con
la semilla fija en este entorno.
"""
from __future__ import annotations
import hashlib, json, platform, sys
import numpy as np
import scipy
from scipy.optimize import curve_fit

VERDAD = {"profundidad": 0.010, "t0_s": 100_000.0, "duracion_s": 8_000.0}
INGRESO = 1_000.0
SIGMA = 0.002


def modelo(t, profundidad, t0, dur):
    return 1.0 - profundidad * np.clip((dur / 2 - np.abs(t - t0)) / INGRESO, 0.0, 1.0)


def generar():
    rng = np.random.default_rng(20261105)
    t = np.arange(20_000) * 10.0
    f = modelo(t, VERDAD["profundidad"], VERDAD["t0_s"], VERDAD["duracion_s"]) + rng.normal(0, SIGMA, t.size)
    return t, f


def analizar():
    t, f = generar()
    huella_datos = hashlib.sha256(t.tobytes() + f.tobytes()).hexdigest()
    p0 = [0.005, 99_000.0, 7_000.0]
    popt, pcov = curve_fit(modelo, t, f, p0=p0, sigma=np.full(t.size, SIGMA), absolute_sigma=True)
    err = np.sqrt(np.diag(pcov))
    res = {"profundidad": float(popt[0]), "t0_s": float(popt[1]), "duracion_s": float(popt[2])}
    inc = {"profundidad": float(err[0]), "t0_s": float(err[1]), "duracion_s": float(err[2])}
    chi2 = float(np.sum(((f - modelo(t, *popt)) / SIGMA) ** 2))
    return huella_datos, res, inc, chi2, t.size


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  SciPy {scipy.__version__}")
    h, res, inc, chi2, n = analizar()
    print(f"1-2. datos sintéticos: n = {n}; huella sha256 = {h[:16]}...")
    print("3. ajuste:")
    for k in VERDAD:
        z = (res[k] - VERDAD[k]) / inc[k]
        print(f"   {k:12s}: estimado = {res[k]:.6g} +- {inc[k]:.2g}  (verdadero {VERDAD[k]:g}; desviación = {z:+.2f} sigma)")
        prueba(abs(z) < 3.0, f"{k} dentro de 3 sigma")
    gl = n - 3
    print(f"   chi2 = {chi2:.1f} con {gl} grados de libertad (chi2/gl = {chi2/gl:.3f}; esperado ~ 1)")
    prueba(0.9 < chi2 / gl < 1.1, "chi2 reducido cercano a 1")
    # 5. repetición idéntica
    h2, res2, inc2, chi22, _ = analizar()
    salida1 = json.dumps({"res": res, "inc": inc}, sort_keys=True)
    salida2 = json.dumps({"res": res2, "inc": inc2}, sort_keys=True)
    hs1, hs2 = hashlib.sha256(salida1.encode()).hexdigest(), hashlib.sha256(salida2.encode()).hexdigest()
    print(f"5. repetición: huella de resultados idéntica = {hs1 == hs2}")
    prueba(h == h2 and hs1 == hs2, "repetición idéntica")
    # 4b. regresión: valores de referencia con tolerancias
    ref = {"profundidad": 0.010, "t0_s": 100_000.0, "duracion_s": 8_000.0}
    for k in ref:
        prueba(abs(res[k] - ref[k]) < 3 * inc[k], f"regresión {k}")
    # 6. procedencia
    proc = {"datos_sha256": h, "modelo": "trapecio, ingreso fijo 1000 s", "semilla": 20261105,
            "versiones": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
            "resultados": res, "incertidumbres": inc}
    print("6. procedencia (claves):", sorted(proc.keys()))
    # 7. una verificación negativa: un modelo equivocado (sin ingreso) debe empeorar chi2
    t, f = generar()
    sin_ingreso = lambda t, d, t0, dur: 1.0 - d * (np.abs(t - t0) < dur / 2)
    popt2, _ = curve_fit(sin_ingreso, t, f, p0=[0.005, 99_000.0, 7_000.0], sigma=np.full(t.size, SIGMA), absolute_sigma=True,
                         maxfev=20000)
    chi2_mal = float(np.sum(((f - sin_ingreso(t, *popt2)) / SIGMA) ** 2))
    print(f"7. modelo equivocado (sin ingreso): chi2/gl = {chi2_mal/gl:.3f} frente a {chi2/gl:.3f}")
    prueba(chi2_mal > chi2, "el modelo equivocado debe ajustar peor")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
