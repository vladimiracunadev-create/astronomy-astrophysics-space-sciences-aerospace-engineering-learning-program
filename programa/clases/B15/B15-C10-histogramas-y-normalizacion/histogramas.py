#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C10: histogramas, límites de visualización y estiramientos.

Datos: SINTÉTICOS, semilla fija. Imagen de 128 x 128 ya calibrada: cielo
50 ADU con ruido gaussiano de 9 ADU, una estructura difusa tenue (gaussiana
de sigma 15 px y amplitud 15 ADU) y 12 estrellas de flujo entre 300 y 2e5 ADU.
Modelo de visualización: x_n = clip((x - lo)/(hi - lo), 0, 1) y luego un
estiramiento f en [0,1]:
  lineal f(t)=t; raíz f(t)=sqrt(t); log f(t)=log10(1+a t)/log10(1+a), a = 1000;
  asinh f(t)=asinh(t/b)/asinh(1/b), con b = 0.02 (idea de Lupton et al., 2004).
Referencias analíticas: f(0)=0, f(1)=1, f monótona; sqrt(0.25)=0.5; la
pendiente inicial del asinh es 1/(b asinh(1/b)); para t >> b, asinh ~ log;
la ecualización por CDF da un histograma casi plano.
Supuestos: la visualización NO modifica el dato (se aplica a una copia).
Tolerancias: 1e-12 en las propiedades de f; 0.02 en la ecualización.
"""
import platform
import sys

import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "|", platform.system())
rng = np.random.default_rng(15010)
N = 128
yy, xx = np.mgrid[0:N, 0:N]
img = 50.0 + 15.0 * np.exp(-0.5 * (((xx - 40) ** 2 + (yy - 90) ** 2) / 15.0**2))
fluj = np.exp(rng.uniform(np.log(300), np.log(2e5), 12))
pos = rng.uniform(8, N - 8, (12, 2))
for F, (px, py) in zip(fluj, pos):
    g = np.exp(-0.5 * ((xx - px) ** 2 + (yy - py) ** 2) / 1.8**2)
    img += F * g / g.sum()
img += 9.0 * rng.standard_normal((N, N))
copia = img.copy()

# --- Histograma
cuentas, bordes = np.histogram(img, bins=50)
prueba(cuentas.sum() == N * N, "el histograma cuenta todos los píxeles")
print(f"(1) mín {img.min():.1f}, mediana {np.median(img):.1f}, máx {img.max():.0f} ADU; "
      f"el {100*cuentas[0]/N/N:.1f} % de los píxeles cae en el primer intervalo (de 50)")

# --- Límites y estiramientos
estir = {
    "lineal": lambda t: t,
    "raíz": np.sqrt,
    "log": lambda t: np.log10(1 + 1000 * t) / np.log10(1 + 1000),
    "asinh": lambda t: np.arcsinh(t / 0.02) / np.arcsinh(1 / 0.02),
}
t = np.linspace(0, 1, 2001)
for nom, f in estir.items():
    y = f(t)
    prueba(abs(f(np.array([0.0]))[0]) < 1e-12 and abs(f(np.array([1.0]))[0] - 1) < 1e-12, f"{nom}: extremos")
    prueba(np.all(np.diff(y) > 0), f"{nom}: monótona")
prueba(abs(np.sqrt(0.25) - 0.5) < 1e-12, "sqrt(0.25) = 0.5")
b = 0.02
pend = (np.arcsinh(1e-6 / b) / np.arcsinh(1 / b)) / 1e-6
print(f"(2) asinh: pendiente inicial {pend:.4f} (teoría {1/(b*np.arcsinh(1/b)):.4f}); "
      f"f(0.5) = {estir['asinh'](np.array([0.5]))[0]:.4f}, log aprox. = {np.log(2*0.5/b)/np.arcsinh(1/b):.4f}")
prueba(abs(pend - 1 / (b * np.arcsinh(1 / b))) < 1e-4, "pendiente inicial del asinh")
prueba(abs(estir["asinh"](np.array([0.5]))[0] - np.log(2 * 0.5 / b) / np.arcsinh(1 / b)) < 1e-3, "asinh ~ log para t >> b")


def niveles(x, lo, hi, f):
    tn = np.clip((x - lo) / (hi - lo), 0, 1)
    return np.round(255 * f(tn))


lo_p, hi_p = np.percentile(img, [1, 99.5])
print(f"    límites percentil 1-99,5: {lo_p:.1f} a {hi_p:.1f} ADU")
print("(3) niveles de gris (0-255) del cielo (mediana y +1 sigma = +9 ADU) y de la estructura tenue (+15 ADU sobre el cielo):")
med = np.median(img)
for nom, lo, hi in (("min-max", img.min(), img.max()),
                    ("percentil 1-99,5", *np.percentile(img, [1, 99.5]))):
    for fn in ("lineal", "asinh"):
        n0, n1, n2 = (niveles(np.array([v]), lo, hi, estir[fn])[0] for v in (med, med + 9, med + 15))
        print(f"    {nom:17s} {fn:7s}: cielo {n0:3.0f}, +9 ADU {n1:3.0f}, +15 ADU {n2:3.0f}")
lo_mm, hi_mm = img.min(), img.max()
tn = (med + 9 - lo_mm) / (hi_mm - lo_mm)
prueba(255 * tn - 255 * (med - lo_mm) / (hi_mm - lo_mm) < 1.0, "con min-max lineal, 1 sigma de ruido es menos de 1 nivel de gris")

# --- Ecualización
orden = np.sort(img.ravel())
cdf = np.searchsorted(orden, img.ravel(), side="right") / orden.size
ecual = cdf.reshape(N, N)
h, _ = np.histogram(ecual, bins=20, range=(0, 1))
desv = np.abs(h / h.sum() - 1 / 20).max()
print(f"(4) ecualización por CDF: desviación máxima del histograma respecto a plano = {desv:.4f}")
prueba(desv < 0.02, "ecualización casi plana")

# --- La visualización no es el dato: razón de flujos
def razon(fn):
    """Suma de la estrella en la imagen mostrada (tras normalizar a [0,1] y estirar)."""
    r = []
    for F in (1000.0, 2000.0):
        g = np.exp(-0.5 * (((xx - 64) ** 2 + (yy - 64) ** 2) / 1.8**2))
        s = F * g / g.sum()
        r.append(fn(np.clip(s / 2500, 0, 1)).sum())
    return r[1] / r[0]


print(f"(5) razón entre las 'sumas' de dos estrellas de flujos 1000 y 2000 (real 2.000): "
      f"lineal {razon(estir['lineal']):.3f}, raíz {razon(estir['raíz']):.3f}, asinh {razon(estir['asinh']):.3f}")
prueba(abs(razon(estir["lineal"]) - 2) < 1e-9 and abs(razon(estir["asinh"]) - 2) > 0.1, "solo el lineal conserva proporciones")
prueba(np.array_equal(img, copia), "la visualización no modificó los datos")
print("Pruebas superadas.")
