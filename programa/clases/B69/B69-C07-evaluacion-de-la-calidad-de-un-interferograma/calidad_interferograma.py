#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C07: evaluacion de la calidad de un interferograma (interferogramas SINTETICOS).

Datos: ningun dato observado. Escena de 128 x 128 pixeles (pixel de 20 m); lambda = 0.0555 m (ilustrativa); semilla 20261109. Fase en rad; coherencia adimensional.
Sistema de referencia: pixeles (fila, columna); fase interferometrica envuelta en (-pi, pi]; convencion dphi = +4 pi d_LOS / lambda como en B69-C06.
Modelo: (1) desviacion tipica de la fase de un pixel con coherencia gamma y N vistas independientes, sigma_phi ~ sqrt(1 - gamma^2) / (gamma sqrt(2 N)) (cota de Cramer-Rao,
valida para N grande y gamma no pequena), contrastada con simulacion. (2) Residuos de la fase envuelta: suma de las diferencias envueltas alrededor de cada lazo de 2 x 2 pixeles;
distinto de cero = inconsistencia que impide desenvolver sin ambiguedad. Densidad de residuos frente a la coherencia. (3) Cierre de fase de un triplete de fechas: phi12 + phi23 - phi13
debe ser 0 (mod 2 pi) si los tres interferogramas son consistentes; un sesgo en uno de ellos aparece en el cierre.
Supuestos: speckle completamente desarrollado, coherencia uniforme por escena, sin atmosfera ni topografia residual. Validez: ilustrar los criterios; no hay umbrales universales.
Tolerancias: sigma_phi simulado frente a la cota 5 % (gamma 0.8, N 100); residuos en fase sin ruido = 0; cierre exacto del triplete consistente 1e-9 rad; sesgo detectado a 0.1 rad.
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

def envolver(p):
    return (p + math.pi) % (2 * math.pi) - math.pi

def cgauss(*shape):
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) / math.sqrt(2)

def par(gamma, shape, N):
    s1 = cgauss(*shape, N)
    s2 = gamma * s1 + math.sqrt(1 - gamma**2) * cgauss(*shape, N)
    return s1, s2

def fase_multilook(s1, s2):
    return np.angle((s1 * np.conj(s2)).mean(axis=-1))

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
# 1) Cota de Cramer-Rao
print(f"{'gamma':>6s} {'N':>5s} {'sigma simulada (rad)':>22s} {'cota CR (rad)':>15s}")
for g, N in ((0.8, 100), (0.9, 100), (0.6, 100)):
    s1, s2 = par(g, (40000,), N)
    sim = fase_multilook(s1, s2).std()
    cr = math.sqrt(1 - g**2) / (g * math.sqrt(2 * N))
    print(f"{g:6.2f} {N:5d} {sim:22.4f} {cr:15.4f}")
    if g == 0.8:
        check(abs(sim / cr - 1) < 0.05, "cota de Cramer-Rao")
print(f"Equivalencia: 0.1 rad de fase = {0.1*lam/(4*math.pi)*1000:.3f} mm en la linea de vision")

# 2) Residuos
n = 128
yy, xx = np.mgrid[0:n, 0:n]
def residuos(phi_w):
    d1 = envolver(phi_w[:-1, 1:] - phi_w[:-1, :-1])
    d2 = envolver(phi_w[1:, 1:] - phi_w[:-1, 1:])
    d3 = envolver(phi_w[1:, :-1] - phi_w[1:, 1:])
    d4 = envolver(phi_w[:-1, :-1] - phi_w[1:, :-1])
    return np.rint((d1 + d2 + d3 + d4) / (2 * math.pi)).astype(int)

# Fase verdadera suave: tazon de subsidencia + rampa orbital
phi_v = 2.5 * np.exp(-((xx - 64) ** 2 + (yy - 64) ** 2) / (2 * 20.0**2)) + 0.02 * xx + 0.01 * yy
r0 = residuos(envolver(phi_v))
print(f"Fase sin ruido: residuos = {np.abs(r0).sum()}")
check(np.abs(r0).sum() == 0, "residuos en fase sin ruido")
print(f"{'coherencia':>11s} {'vistas':>7s} {'residuos por 1000 pix':>22s} {'desv. fase pix (rad)':>22s}")
dens = {}
for g in (0.95, 0.8, 0.6, 0.4, 0.2):
    s1, s2 = par(g, (n, n), 4)
    ph = envolver(phi_v + fase_multilook(s1, s2))
    r = residuos(ph)
    dens[g] = np.abs(r).sum() / (n * n) * 1000
    print(f"{g:11.2f} {4:7d} {dens[g]:22.1f} {envolver(ph - phi_v).std():22.3f}")
check(dens[0.95] < dens[0.8] < dens[0.6] < dens[0.4], "los residuos deben crecer al bajar la coherencia")

# 3) Cierre de fase de un triplete
phi12 = envolver(phi_v)
phi23 = envolver(0.7 * phi_v + 0.3)
phi13 = envolver(phi_v + 0.7 * phi_v + 0.3)
cierre = envolver(phi12 + phi23 - phi13)
print(f"Triplete consistente: cierre maximo = {np.abs(cierre).max():.2e} rad")
check(np.abs(cierre).max() < 1e-9, "cierre exacto")
sesgo = 0.25                                    # rad: sesgo sintetico en phi13 (p. ej. por humedad del suelo)
phi13s = envolver(phi13 + sesgo)
cierre_s = envolver(phi12 + phi23 - phi13s)
print(f"Triplete con sesgo de {sesgo} rad en el interferograma 13: cierre medio = {cierre_s.mean():+.3f} rad ({cierre_s.mean()*lam/(4*math.pi)*1000:+.2f} mm)")
check(abs(abs(cierre_s.mean()) - sesgo) < 0.1, "el cierre debe delatar el sesgo")
# Con ruido: el cierre tiene dispersion y no revela sesgos pequenos
s1, s2 = par(0.7, (n, n), 4)
rn = [fase_multilook(*par(0.7, (n, n), 4)) for _ in range(3)]
cierre_n = envolver(rn[0] + rn[1] - rn[2])
print(f"Tres interferogramas con ruido (gamma 0.7, 4 vistas): dispersion del cierre = {cierre_n.std():.3f} rad")
print("Pruebas superadas.")
