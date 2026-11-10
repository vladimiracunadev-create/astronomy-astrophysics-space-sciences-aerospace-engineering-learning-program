#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B69-C03: ruido speckle y filtrado en imagenes SAR (escena SINTETICA).

Datos: ningun dato observado. Escena sintetica de 256 x 256 pixeles con dos regiones homogeneas (reflectividad media sigma0 de 1.0 y 4.0, unidades arbitrarias de intensidad
lineal; borde vertical en la columna 128). Speckle totalmente desarrollado simulado como suma de fasores con fase uniforme: amplitud compleja gaussiana circular. Semilla 20261109.
Sistema de referencia: pixeles (fila, columna) de la imagen; intensidad I = |z|^2 (lineal, sin dB salvo que se indique).
Modelo: I = sigma0 * u, con u ~ Exponencial(1) en una vista y u ~ Gamma(L, 1/L) tras promediar L vistas independientes. Contraste CV = desv. tipica / media = 1/sqrt(L).
Numero equivalente de vistas ENL = media^2 / varianza. Filtro de Lee: x = m + k (I - m), k = 1 - Cu^2 / Ci^2 (acotado a [0, 1]), con medias y varianzas en ventana 7x7 y Cu = 1/sqrt(L).
Supuestos: speckle multiplicativo, independiente entre pixeles, sin correlacion espacial por sobremuestreo. Validez: regiones homogeneas amplias.
Tolerancias: CV de una vista 1 +- 2 %; CV de L vistas = 1/sqrt(L) +- 3 %; ENL tras el filtro de Lee mayor que 4 veces el original en la zona homogenea; sesgo de la media del filtro < 3 %.
"""
from __future__ import annotations
import platform
import numpy as np

rng = np.random.default_rng(20261109)

def check(cond, msg):
    if not cond:
        raise SystemExit("FALLA: " + msg)

def enl(x):
    return x.mean() ** 2 / x.var()

print(f"Python {platform.python_version()} ; numpy {np.__version__}")
# 1) Estadistica del speckle de una vista
N = 400_000
z = (rng.standard_normal(N) + 1j * rng.standard_normal(N)) / np.sqrt(2)
I1 = np.abs(z) ** 2
cv1 = I1.std() / I1.mean()
print(f"Una vista: media = {I1.mean():.4f} ; CV = {cv1:.4f} (teorico 1) ; ENL = {enl(I1):.3f}")
check(abs(cv1 - 1) < 0.02, "CV de una vista")
# amplitud: Rayleigh con CV = sqrt(4/pi - 1)
A = np.abs(z)
print(f"Amplitud: CV = {A.std()/A.mean():.4f} (Rayleigh teorico {np.sqrt(4/np.pi-1):.4f})")
check(abs(A.std() / A.mean() / np.sqrt(4 / np.pi - 1) - 1) < 0.02, "CV Rayleigh")

# 2) Multilook
print("Multilook (promedio de L vistas independientes):")
for L in (1, 4, 9, 16):
    zz = (rng.standard_normal((N // 4, L)) + 1j * rng.standard_normal((N // 4, L))) / np.sqrt(2)
    IL = (np.abs(zz) ** 2).mean(axis=1)
    cv = IL.std() / IL.mean()
    print(f"  L = {L:2d}: CV = {cv:.4f} (1/sqrt(L) = {1/np.sqrt(L):.4f}) ; ENL = {enl(IL):.2f}")
    check(abs(cv * np.sqrt(L) - 1) < 0.03, f"CV multilook L={L}")

# 3) Escena sintetica y filtro de Lee
Nf = 256
sigma = np.ones((Nf, Nf)); sigma[:, Nf // 2:] = 4.0
zi = (rng.standard_normal((Nf, Nf)) + 1j * rng.standard_normal((Nf, Nf))) / np.sqrt(2)
I = sigma * np.abs(zi) ** 2

def ventana_media(x, w):
    r = w // 2
    xp = np.pad(x, r, mode="reflect")
    S = np.cumsum(np.cumsum(np.pad(xp, ((1, 0), (1, 0))), axis=0), axis=1)
    return (S[w:, w:] - S[:-w, w:] - S[w:, :-w] + S[:-w, :-w]) / (w * w)

def lee(I, w=7, L=1):
    m = ventana_media(I, w)
    v = np.maximum(ventana_media(I * I, w) - m * m, 0)
    Cu2 = 1.0 / L
    Ci2 = v / np.maximum(m * m, 1e-12)
    k = np.clip(1 - Cu2 / np.maximum(Ci2, 1e-12), 0, 1)
    return m + k * (I - m)

F = lee(I)
zona1 = (slice(20, 100), slice(20, 100))      # lejos del borde, sigma0 = 1
zona2 = (slice(20, 100), slice(156, 236))     # sigma0 = 4
e_ant1, e_post1 = enl(I[zona1]), enl(F[zona1])
e_ant2, e_post2 = enl(I[zona2]), enl(F[zona2])
print(f"Zona homogenea sigma0 = 1: ENL {e_ant1:.2f} -> {e_post1:.2f} ; media {I[zona1].mean():.3f} -> {F[zona1].mean():.3f}")
print(f"Zona homogenea sigma0 = 4: ENL {e_ant2:.2f} -> {e_post2:.2f} ; media {I[zona2].mean():.3f} -> {F[zona2].mean():.3f}")
check(e_post1 > 4 * e_ant1 and e_post2 > 4 * e_ant2, "ENL tras Lee")
check(abs(F[zona1].mean() / I[zona1].mean() - 1) < 0.03 and abs(F[zona2].mean() / I[zona2].mean() - 1) < 0.03, "sesgo de Lee")

# Borde: pendiente del salto de media a ambos lados (preservacion del borde)
def salto(x):
    a = x[:, Nf // 2 - 4:Nf // 2].mean(); b = x[:, Nf // 2:Nf // 2 + 4].mean()
    return b / a
Mb = ventana_media(I, 7)
print(f"Cociente de medias a ambos lados del borde (4 columnas): crudo {salto(I):.2f} ; Lee {salto(F):.2f} ; media 7x7 {salto(Mb):.2f} ; verdad 4.00")
check(abs(salto(F) - 4) < abs(salto(Mb) - 4), "Lee conserva el borde mejor que la media")
print("Pruebas superadas.")
