#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C09: altimetria satelital: distancia por tiempo de ida y vuelta y reajuste del frente del eco.

Datos: SINTETICOS e ILUSTRATIVOS: altitud del satelite 1 336 km, compuertas de 3.125 ns (320 MHz), 128 compuertas, forma de la subida
del eco 0.5 (1 + erf((t - t0)/(sqrt(2) sigma))) con sigma = 2.5 ns, moteado de potencia exponencial promediado sobre N pulsos. No hay datos
observados ni se modela una mision concreta (no se consultaron paginas de altimetria).
Modelo: R = c t / 2; reajuste (retracking) del tiempo t0 por minimos cuadrados con amplitud libre sobre una malla de 0.01 ns; altura de la
superficie SSH = H - R. Semilla fija 57, 400 ensayos por caso.
Validez: sin correcciones atmosfericas ni de estado del mar; amplitud y sigma conocidas. Tolerancia: sesgo compatible con cero a 4 errores estandar de la media (rms/sqrt(400)); el error rms debe
bajar como 1/sqrt(N) (razon entre N = 25 y N = 100 entre 1.6 y 2.4).
Requiere numpy.
"""
import math, platform
import numpy as np
from math import erf

C = 299792458.0
DT = 3.125e-9
NG = 128
SIG = 2.5e-9
H = 1336e3


def modelo(t, t0):
    return 0.5 * (1 + np.vectorize(erf)((t - t0) / (math.sqrt(2) * SIG)))


def ensayo(nlooks, rng, ensayos=400):
    t = np.arange(NG) * DT
    mallas = np.arange(-3e-9, 3e-9 + 1e-12, 0.01e-9)
    base = 64 * DT
    plantillas = np.array([modelo(t, base + d) for d in mallas])
    pm = np.sum(plantillas**2, axis=1)
    err = []
    for _ in range(ensayos):
        verd = rng.uniform(-1.5e-9, 1.5e-9)
        m = modelo(t, base + verd)
        w = np.mean(rng.exponential(1.0, (nlooks, NG)) * m, axis=0)
        a = plantillas @ w / pm  # amplitud optima por plantilla
        costo = np.sum(w**2) - 2 * a * (plantillas @ w) + a**2 * pm
        est = mallas[int(np.argmin(costo))]
        err.append(est - verd)
    err = np.array(err)
    return float(err.mean()), float(err.std())


def calcular():
    r = {}
    r["dt_1cm_ps"] = 2 * 0.01 / C * 1e12
    r["cm_por_ns"] = C * 1e-9 / 2 * 100
    rng = np.random.default_rng(57)
    for n in (25, 100):
        b, s = ensayo(n, rng)
        r[f"sesgo_{n}"] = b * 1e9
        r[f"rms_{n}_ns"] = s * 1e9
        r[f"rms_{n}_cm"] = s * C / 2 * 100
    r["razon"] = r["rms_25_ns"] / r["rms_100_ns"]
    # inversion exacta de R = c t / 2
    t = 2 * (H - 0.42) / C
    r["ssh_rec"] = H - C * t / 2
    r["t_ms"] = t * 1e3
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"1 cm de distancia = {r['dt_1cm_ps']:.1f} ps de tiempo de ida y vuelta ; 1 ns = {r['cm_por_ns']:.2f} cm")
    print(f"Tiempo de ida y vuelta para H - SSH = 1336 km - 0.42 m: {r['t_ms']:.6f} ms ; SSH recuperada = {r['ssh_rec']:.4f} m")
    for n in (25, 100):
        print(f"N = {n:3d} pulsos: sesgo = {r['sesgo_'+str(n)]:+.4f} ns ; error rms de t0 = {r['rms_'+str(n)+'_ns']:.4f} ns = {r['rms_'+str(n)+'_cm']:.2f} cm")
    print(f"Razon de errores rms (N = 25 / N = 100) = {r['razon']:.2f} (teoria 2)")
    assert abs(r["ssh_rec"] - 0.42) < 1e-6
    for n in (25, 100):
        assert abs(r[f"sesgo_{n}"]) < 4 * r[f"rms_{n}_ns"] / math.sqrt(400)  # compatible con cero a 4 errores estandar
    assert 1.6 < r["razon"] < 2.4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
