#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C05: coherencia interferometrica y decorrelacion (pares de imagenes complejas SINTETICAS).

Datos: ningun dato observado. Pares de pixeles complejos gaussianos circulares (speckle completamente desarrollado) con correlacion rho impuesta; semilla 20261109.
Longitud de onda ilustrativa lambda = 0.0555 m (banda C). Magnitudes: coherencia |gamma| (adimensional, 0 a 1); fase en rad; desplazamientos en m.
Sistema de referencia: pixeles de dos adquisiciones coregistradas s1 y s2; gamma = <s1 s2*> / sqrt(<|s1|^2> <|s2|^2>). Estimador con N vistas independientes.
Modelo: s2 = rho s1 + sqrt(1 - rho^2) n con n independiente. Decorrelacion: de relacion senal-ruido gamma_snr = 1/(1 + 1/SNR); temporal por movimiento aleatorio de los dispersores con
desviacion tipica sigma_d en la linea de vision gamma_t = exp(-(4 pi sigma_d / lambda)^2 / 2); geometrica: n ciclos de franja a traves de la celda gamma_g = |sinc(n)| (n = 1: linea de base critica).
Compuesta: gamma = gamma_snr * gamma_t * gamma_g.
Supuestos: dispersores sin correlacion entre si, estimador sin ventana de pesos, sin pendiente del terreno. Validez: ilustrar los modelos; no se calibra ningun sensor.
Tolerancias (modelos de decorrelacion solo donde el modelo supera 0.3, por el suelo de sesgo del estimador): |gamma| estimado frente al verdadero en alto rho 0.01 (N=1000); sesgo a rho=0 frente a Gamma(3/2)Gamma(N)/Gamma(N+1/2) dentro de 3 errores tipicos; modelos de decorrelacion 0.01.
"""
from __future__ import annotations
import math
import platform
import numpy as np

rng = np.random.default_rng(20261109)
lam = 0.0555

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

def cgauss(*shape):
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / np.sqrt(2)

def gamma_est(s1, s2):
    return np.abs((s1 * np.conj(s2)).mean(axis=-1)) / np.sqrt((np.abs(s1) ** 2).mean(axis=-1) * (np.abs(s2) ** 2).mean(axis=-1))

def par(rho, M, N):
    s1 = cgauss(M, N)
    s2 = rho * s1 + math.sqrt(1 - rho**2) * cgauss(M, N)
    return s1, s2

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
# 1) Sesgo del estimador
print("Estimador de |gamma| con N vistas (M = 20000 pixeles por celda):")
print(f"{'rho':>5s} {'N':>5s} {'media estimada':>15s} {'error tipico':>13s}")
for rho, N in ((0.9, 1000), (0.5, 20), (0.0, 9), (0.0, 25)):
    s1, s2 = par(rho, 20000, N)
    g = gamma_est(s1, s2)
    print(f"{rho:5.2f} {N:5d} {g.mean():15.4f} {g.std()/math.sqrt(len(g)):13.4f}")
    if rho == 0.9:
        check(abs(g.mean() - 0.9) < 0.01, "alto rho")
    if rho == 0.0:
        teo = math.gamma(1.5) * math.gamma(N) / math.gamma(N + 0.5)
        print(f"        teorico para rho = 0: {teo:.4f}")
        check(abs(g.mean() - teo) < 3 * g.std() / math.sqrt(len(g)), f"sesgo rho=0 N={N}")

# 2) Decorrelacion por SNR
print("Decorrelacion por ruido termico (SNR en potencia lineal):")
for snr in (1.0, 3.0, 10.0, 100.0):
    N = 2000
    x = cgauss(10000, N)
    s1 = x + cgauss(10000, N) / math.sqrt(snr)
    s2 = x + cgauss(10000, N) / math.sqrt(snr)
    g = gamma_est(s1, s2).mean()
    teo = 1 / (1 + 1 / snr)
    print(f"  SNR = {snr:6.1f} ({10*math.log10(snr):5.1f} dB): medido {g:.4f} ; modelo {teo:.4f}")
    check(abs(g - teo) < 0.01, f"gamma_snr SNR={snr}")

# 3) Decorrelacion temporal: dispersores que se mueven en la linea de vision
print("Decorrelacion temporal (sigma_d: movimiento aleatorio rms en la linea de vision):")
for sd in (0.002, 0.005, 0.01, 0.02):
    Ns = 400
    a = cgauss(5000, Ns)
    d = sd * rng.standard_normal((5000, Ns))
    s1 = a
    s2 = a * np.exp(-1j * 4 * math.pi * d / lam)
    g = gamma_est(s1, s2).mean()
    teo = math.exp(-0.5 * (4 * math.pi * sd / lam) ** 2)
    print(f"  sigma_d = {sd*1000:5.1f} mm: medido {g:.4f} ; modelo {teo:.4f}")
    if teo > 0.3:
        check(abs(g - teo) < 0.01, f"gamma_t sd={sd}")
    else:
        print("        (coherencia baja: el estimador con N = 400 vistas tiene un suelo de sesgo ~0.04-0.09; no se compara)")
        check(g > teo, "el estimador no puede quedar por debajo del modelo")

# 4) Decorrelacion geometrica: n ciclos de franja a traves de la celda
print("Decorrelacion geometrica (n ciclos de franja a traves de la celda de resolucion):")
for n in (0.25, 0.5, 1.0, 1.5):
    Ns = 400
    a = cgauss(5000, Ns)
    pos = rng.uniform(-0.5, 0.5, size=(5000, Ns))      # posicion en la celda, en fracciones de celda
    s1 = a
    s2 = a * np.exp(1j * 2 * math.pi * n * pos)
    g = gamma_est(s1, s2).mean()
    teo = abs(np.sinc(n))
    print(f"  n = {n:4.2f}: medido {g:.4f} ; |sinc(n)| = {teo:.4f}")
    if teo > 0.3:
        check(abs(g - teo) < 0.01, f"gamma_g n={n}")
    else:
        print("        (coherencia baja: dominada por el suelo de sesgo del estimador; no se compara)")

# 5) Composicion
snr, sd, n = 10.0, 0.005, 0.25
comp = 1 / (1 + 1 / snr) * math.exp(-0.5 * (4 * math.pi * sd / lam) ** 2) * abs(np.sinc(n))
Ns = 400
a = cgauss(5000, Ns); d = sd * rng.standard_normal((5000, Ns)); pos = rng.uniform(-0.5, 0.5, size=(5000, Ns))
s1 = a + cgauss(5000, Ns) / math.sqrt(snr)
s2 = a * np.exp(-1j * 4 * math.pi * d / lam) * np.exp(1j * 2 * math.pi * n * pos) + cgauss(5000, Ns) / math.sqrt(snr)
g = gamma_est(s1, s2).mean()
print(f"Compuesta (SNR 10, sigma_d 5 mm, n 0.25): medida {g:.4f} ; producto de modelos {comp:.4f}")
check(abs(g - comp) < 0.015, "composicion")
print("Pruebas superadas.")
