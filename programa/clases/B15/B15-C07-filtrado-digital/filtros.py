#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B15-C07: filtros de media móvil (FIR) y de un polo (IIR).

Datos: SINTÉTICOS, semilla fija. Cadencia 120 s (nominal de TESS, MAST).
Modelos y referencias analíticas:
 (1) media móvil de M puntos: h[n] = 1/M para n = 0..M-1; su respuesta en
     frecuencia es H(f) = sen(pi f M) / (M sen(pi f)) * exp(-i pi f (M-1)),
     con f en ciclos por muestra (se compara con la DFT de h);
 (2) filtro de un polo y[n] = a x[n] + (1-a) y[n-1]: respuesta al escalón
     y[n] = 1 - (1-a)^(n+1) y ganancia en continua 1; contraste con
     scipy.signal.lfilter;
 (3) ruido blanco filtrado con M puntos: desviación sigma/sqrt(M);
 (4) retardo del FIR causal simétrico: (M-1)/2 muestras;
 (5) detrend con media móvil centrada de W muestras: un tránsito de d muestras
     y profundidad D conserva D (1 - d/W) en su centro (sin modulación).
Supuestos: sistemas lineales e invariantes; ruido blanco gaussiano.
Validez: lejos de los bordes. Tolerancias: 1e-9 en (1),(2),(4),(5); 3 % en (3).
"""
import platform
import sys

import numpy as np
import scipy
from scipy.signal import lfilter


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


print("Python", sys.version.split()[0], "| numpy", np.__version__, "| scipy", scipy.__version__, "|", platform.system())
rng = np.random.default_rng(15007)

# (1) Respuesta en frecuencia de la media móvil
M = 5
h = np.ones(M) / M
Nf = 64
H = np.fft.fft(h, Nf)
f = np.arange(Nf) / Nf
teo = np.where(f == 0, 1.0, np.sin(np.pi * f * M) / (M * np.sin(np.pi * np.where(f == 0, 1, f)))) * np.exp(-1j * np.pi * f * (M - 1))
d = np.max(np.abs(H - teo))
print(f"(1) media móvil M=5: |H(0)| = {abs(H[0]):.4f}; |H(0,2 c/muestra)| = {abs(H[int(0.2*Nf+0.5)]):.4f} "
      f"(teoría 0 en f = 1/M = 0,2); diferencia máx. con la fórmula = {d:.1e}")
prueba(d < 1e-12, "respuesta en frecuencia de la media móvil")

# (2) Filtro de un polo
a = 0.1
paso = np.ones(50)
y = np.zeros(50)
acc = 0.0
for n in range(50):
    acc = a * paso[n] + (1 - a) * acc
    y[n] = acc
teo_y = 1 - (1 - a) ** (np.arange(50) + 1)
yref = lfilter([a], [1, -(1 - a)], paso)
print(f"(2) un polo a=0,1: y[0] = {y[0]:.4f}; y[9] = {y[9]:.4f} (1-0,9^10 = {1-0.9**10:.4f}); "
      f"y[49] = {y[49]:.4f}; constante de tiempo 1/a = {1/a:.0f} muestras")
prueba(np.allclose(y, teo_y, atol=1e-12) and np.allclose(y, yref, atol=1e-12), "escalón del filtro de un polo")

# (3) Reducción de ruido
Mm = 25
w = rng.standard_normal(400000)
v = np.convolve(w, np.ones(Mm) / Mm, mode="valid")
print(f"(3) ruido blanco con media móvil de {Mm} puntos: sigma = {v.std():.4f} (teoría {1/np.sqrt(Mm):.4f})")
prueba(abs(v.std() * np.sqrt(Mm) - 1) < 0.03, "reducción de ruido 1/sqrt(M)")

# (4) Retardo
n = np.arange(400)
pulso = np.exp(-0.5 * ((n - 150) / 6.0) ** 2)
Mr = 31
sal = np.convolve(pulso, np.ones(Mr) / Mr, mode="full")[:400]
cen = lambda s: np.sum(np.arange(len(s)) * s) / np.sum(s)
print(f"(4) retardo del FIR causal (M={Mr}): centroide de {cen(pulso):.3f} a {cen(sal):.3f} (retardo {cen(sal)-cen(pulso):.3f}; teoría {(Mr-1)/2})")
prueba(abs(cen(sal) - cen(pulso) - (Mr - 1) / 2) < 1e-9, "retardo (M-1)/2")

# (5) Detrend y tránsito
N = 7 * 720                     # 7 d a 120 s
t = np.arange(N) * 120.0 / 86400.0
W, dtr, D = 361, 91, 1000e-6
tr = np.zeros(N)
i0 = 2500
tr[i0:i0 + dtr] = -D
base = np.convolve(tr, np.ones(W) / W, mode="same")
centro = i0 + dtr // 2
ret = (tr - base)[centro]
print(f"(5) tránsito sin ruido: profundidad en el centro tras quitar la media móvil de {W} muestras = "
      f"{-ret*1e6:.1f} ppm (teoría D(1-d/W) = {D*(1-dtr/W)*1e6:.1f} ppm)")
prueba(abs(-ret - D * (1 - dtr / W)) < 1e-12, "profundidad retenida")
# con modulación y ruido
modul = 2000e-6 * np.sin(2 * np.pi * t / 2.5)
x = modul + tr + 300e-6 * rng.standard_normal(N)
base = np.convolve(x, np.ones(W) / W, mode="same")
res = x - base
fm = 1 / 2.5
hma = np.sin(np.pi * fm * (W * 120 / 86400)) / (np.pi * fm * (W * 120 / 86400))
sl = slice(W, N - W)

print(f"    modulación 2000 ppm (P=2,5 d): factor de la media móvil |H| = {hma:.4f}; "
      f"residuo teórico {2000*(1-hma):.0f} ppm; desviación del residuo (incl. ruido) ≈ {np.std(res[sl][np.arange(N)[sl] < i0 - W])*1e6:.0f} ppm")
print(f"    profundidad media en tránsito con ruido y modulación: {-res[i0+10:i0+dtr-10].mean()*1e6:.0f} ppm (centro esperado ≈ {D*(1-dtr/W)*1e6:.0f})")
print("Pruebas superadas.")
