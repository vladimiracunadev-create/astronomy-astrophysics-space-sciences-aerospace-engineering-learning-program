#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C09: calibración de una imagen sintética (bias, oscuro, plano).

Datos: SINTÉTICOS, semilla fija. Imagen de 64 x 64 píxeles, ganancia 1 e-/ADU.
Modelo (el de la guía de reducción CCD consultada):
    crudo = oscuro_con_bias + plano * (cielo + estrella) + ruido
    calibrado = (crudo - oscuro_maestro) / plano
con bias 100 ADU, corriente de oscuridad 3 ADU en la exposición, cielo 50 ADU,
estrella gaussiana (sigma 1,5 px) de flujo 2000 ADU, plano suave 0,80-1,00,
ruido de lectura 5 ADU y ruido de Poisson de la señal.
Supuestos: respuesta lineal, sin saturación, ganancia conocida.
Validez: señales por debajo de saturación. Tolerancias: 1e-9 sin ruido;
5 % en la desviación del cielo calibrado.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15009)
Ny = Nx = 64
yy, xx = np.mgrid[0:Ny, 0:Nx]

# Componentes verdaderas
bias, dark, sky, flujo, sig = 100.0, 3.0, 50.0, 2000.0, 1.5
plano = 1.0 - 0.2 * ((xx - 32) ** 2 + (yy - 32) ** 2) / (2 * 32**2)     # viñeteo suave
psf = np.exp(-0.5 * ((xx - 40.0) ** 2 + (yy - 24.0) ** 2) / sig**2)
psf /= psf.sum()
estrella = flujo * psf
print(f"plano: mín {plano.min():.3f}, máx {plano.max():.3f}")

# --- Prueba 1: sin ruido, la calibración recupera cielo + estrella exactamente
crudo0 = bias + dark + plano * (sky + estrella)
cal0 = (crudo0 - (bias + dark)) / plano
d = np.max(np.abs(cal0 - (sky + estrella)))
print(f"(1) sin ruido: error máximo de la calibración = {d:.1e} ADU")
prueba(d < 1e-9, "calibración exacta sin ruido")
sin_plano = crudo0 - (bias + dark)
print(f"    sin dividir por el plano, el cielo varía de {sin_plano[0,0]:.2f} a {sin_plano[32,0]:.2f} ADU (real 50)")

# --- Prueba 2: tipos de dato (uint16 da la vuelta)
a = np.array([100], dtype=np.uint16)
b = np.array([150], dtype=np.uint16)
print(f"(2) uint16: 100 - 150 = {(a - b)[0]} ; en float: {float(a[0]) - float(b[0])}")
prueba((a - b)[0] == 65486, "desbordamiento uint16")


def exposicion(con_estrella=True):
    senal = plano * (sky + (estrella if con_estrella else 0))
    return bias + dark + rng.poisson(senal) + rng.normal(0, 5.0, (Ny, Nx))


def oscuro(K):
    return np.mean([bias + rng.poisson(dark, (Ny, Nx)) + rng.normal(0, 5.0, (Ny, Nx)) for _ in range(K)], axis=0)


# --- Prueba 3: ruido del cielo calibrado frente a la teoría (plano = 1 en la zona de prueba)
def cielo_calibrado(K, reps=40):
    out = []
    for _ in range(reps):
        osc = oscuro(K)
        raw = bias + rng.poisson(dark + sky, (Ny, Nx)) + rng.normal(0, 5.0, (Ny, Nx))
        out.append((raw - osc)[:, :20])
    v = np.array(out)
    return v.mean(), v.std()


print("(3) cielo calibrado (plano uniforme = 1): media, desviación observada y teórica")
for K in (1, 10, 100):
    m, s = cielo_calibrado(K)
    teo = np.sqrt(25 + sky + dark + (25 + dark) / K)
    print(f"    K = {K:3d} oscuros: media {m:6.2f} ADU (real 50); sigma {s:.3f} (teoría {teo:.3f})")
    prueba(abs(m - 50) < 0.5 and abs(s - teo) < 0.05 * teo, f"ruido con K={K}")

# --- Flujo de la estrella en una apertura
osc = oscuro(50)
raw = exposicion()
cal = (raw - osc) / plano
ap = (xx - 40) ** 2 + (yy - 24) ** 2 <= 5**2
anillo = ((xx - 40) ** 2 + (yy - 24) ** 2 > 8**2) & ((xx - 40) ** 2 + (yy - 24) ** 2 <= 12**2)
fondo = np.median(cal[anillo])
F = (cal[ap] - fondo).sum()
print(f"(4) flujo en apertura de radio 5 px: {F:.0f} ADU (real {flujo * psf[ap].sum():.0f} dentro de la apertura, "
      f"{flujo:.0f} total); fondo {fondo:.2f} ADU")
prueba(abs(F - flujo * psf[ap].sum()) < 5 * np.sqrt(ap.sum() * 80 + flujo), "flujo recuperado dentro de 5 sigma")
print("Pruebas superadas.")
