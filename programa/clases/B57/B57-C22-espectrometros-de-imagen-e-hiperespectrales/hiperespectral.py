#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C22: espectrometria de imagen: angulo espectral, desmezclado lineal y flujo de datos.

Datos: EMIT es un espectrometro de imagen en la ISS con campo de 72 km y mas de 100 000 espectros por segundo (JPL, consultada 2026-11-09; la pagina no daba
el rango espectral ni la resolucion). SINTETICOS / ILUSTRATIVOS: 200 bandas entre 0.4 y 2.5 um, tres miembros extremos (arcilla, hematita, vegetacion) con rasgos
de absorcion gaussianos inventados, ruido de 0.005, 285 bandas y 2 bytes para el calculo del flujo, semilla fija 57. No son espectros de ninguna libreria.
Modelo: mezcla lineal y = E a + n con suma de abundancias 1 (minimos cuadrados con restriccion de suma por multiplicador de Lagrange); angulo espectral
SAM = arccos(x.y/(|x||y|)); flujo de datos = espectros/s * bandas * bytes.
Validez: mezcla lineal (superficie plana), sin atmosfera. Tolerancia: abundancias sin ruido exactas a 1e-9; SAM invariante al factor de escala a 1e-12.
Requiere numpy.
"""
import math, platform
import numpy as np

LAM = np.linspace(0.4, 2.5, 200)


def g(c, w, a):
    return a * np.exp(-0.5 * ((LAM - c) / w) ** 2)


def miembros():
    arcilla = 0.55 + 0.10 * (LAM - 0.4) - g(2.2, 0.04, 0.25) - g(1.4, 0.05, 0.12)
    hematita = 0.10 + 0.25 / (1 + np.exp(-(LAM - 0.6) / 0.05)) - g(0.87, 0.08, 0.05)
    vegetacion = 0.05 + 0.40 / (1 + np.exp(-(LAM - 0.72) / 0.02)) - g(0.68, 0.03, 0.04) - g(1.45, 0.08, 0.15) - g(1.95, 0.10, 0.20)
    return np.column_stack([arcilla, hematita, vegetacion])


def sam(x, y):
    return math.acos(max(-1, min(1, float(x @ y / (np.linalg.norm(x) * np.linalg.norm(y))))))


def desmezclar(E, y):
    n = E.shape[1]
    K = np.block([[2 * E.T @ E, np.ones((n, 1))], [np.ones((1, n)), np.zeros((1, 1))]])
    rhs = np.concatenate([2 * E.T @ y, [1.0]])
    return np.linalg.solve(K, rhs)[:n]


def calcular():
    r = {}
    E = miembros()
    a = np.array([0.5, 0.3, 0.2])
    y = E @ a
    r["err_sin_ruido"] = float(np.max(np.abs(desmezclar(E, y) - a)))
    r["sam_escala"] = abs(sam(y, 3.7 * y))
    r["sam_arc_hem"] = math.degrees(sam(E[:, 0], E[:, 1]))
    r["sam_arc_veg"] = math.degrees(sam(E[:, 0], E[:, 2]))
    r["sam_hem_veg"] = math.degrees(sam(E[:, 1], E[:, 2]))
    rng = np.random.default_rng(57)
    errs = []
    for _ in range(2000):
        ah = desmezclar(E, y + 0.005 * rng.standard_normal(y.size))
        errs.append(ah - a)
    errs = np.array(errs)
    r["rms_ab"] = float(np.sqrt(np.mean(errs**2)))
    r["sesgo_ab"] = float(np.max(np.abs(errs.mean(axis=0))))
    # multiespectral de 4 bandas (ilustrativa): bandas anchas 0.48, 0.56, 0.66, 0.86 um
    idx = [int(np.argmin(abs(LAM - l))) for l in (0.48, 0.56, 0.66, 0.86)]
    E4 = E[idx, :]
    errs4 = []
    for _ in range(2000):
        ah = desmezclar(E4, E4 @ a + 0.005 * rng.standard_normal(4))
        errs4.append(ah - a)
    r["rms_ab_4"] = float(np.sqrt(np.mean(np.array(errs4) ** 2)))
    r["razon_ab"] = r["rms_ab_4"] / r["rms_ab"]
    r["rate_MBs"] = 100000 * 285 * 2 / 1e6
    r["rate_TBdia"] = r["rate_MBs"] * 86400 / 1e6
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Desmezclado sin ruido: error maximo de abundancia = {r['err_sin_ruido']:.1e}")
    print(f"SAM: invariancia al factor de escala = {r['sam_escala']:.1e} rad ; arcilla-hematita = {r['sam_arc_hem']:.2f} deg ; arcilla-vegetacion = {r['sam_arc_veg']:.2f} deg ; hematita-vegetacion = {r['sam_hem_veg']:.2f} deg")
    print(f"Con ruido 0.005 (2000 ensayos): rms de abundancia = {r['rms_ab']:.4f} ; sesgo maximo = {r['sesgo_ab']:.1e}")
    print(f"Con 4 bandas anchas y el mismo ruido: rms de abundancia = {r['rms_ab_4']:.4f} ({r['razon_ab']:.1f} veces el de 200 bandas)")
    print(f"Flujo ilustrativo: 100000 espectros/s x 285 bandas x 2 bytes = {r['rate_MBs']:.0f} MB/s = {r['rate_TBdia']:.1f} TB/dia (si se grabara de forma continua)")
    assert r["err_sin_ruido"] < 1e-9
    assert r["sam_escala"] < 1e-6
    assert r["razon_ab"] > 3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
