#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B12-C24: metricas de habilidad (Brier, TSS, HSS) de un pronostico.

Datos: SINTETICOS (no son datos solares reales). 3000 dias: riesgo latente
r ~ Beta(2, 18) (media 0.10); suceso o ~ Bernoulli(r); pronostico
f = clip(r + N(0, 0.05^2), 0.01, 0.99) (pronosticador con informacion parcial).
Modelo: puntaje de Brier BS = mean((f - o)^2); referencia climatologica
(frecuencia base constante): BS_ref = base (1 - base); BSS = 1 - BS/BS_ref.
Tabla de contingencia con umbral f >= 0.2: a (aciertos), b (falsas alarmas),
c (omisiones), d (rechazos correctos); POD = a/(a+c); POFD = b/(b+d);
TSS = POD - POFD; HSS = 2(ad - bc)/((a+c)(c+d) + (a+b)(b+d)).
Supuestos: eventos independientes entre dias; base rate estacionaria.
Validez: la habilidad depende de la referencia y de la muestra (incertidumbre
por remuestreo).
Tolerancia: pruebas exactas con aritmetica de fracciones para casos
analiticos (pronostico perfecto, climatologia, tabla 30/20/10/140, invarianza
de TSS); intervalo bootstrap con 1 000 remuestras. Detienen la ejecucion.
"""
import platform
from fractions import Fraction

import numpy as np

print(f"Python {platform.python_version()} - NumPy {np.__version__}")


def brier(f, o):
    return float(np.mean((f - o) ** 2))


def bss(f, o, ref=None):
    base = float(np.mean(o))
    b_ref = base * (1 - base) if ref is None else brier(ref, o)
    return 1 - brier(f, o) / b_ref


def table(f, o, thr):
    p = f >= thr
    a = int(np.sum(p & (o == 1)))
    b = int(np.sum(p & (o == 0)))
    c = int(np.sum(~p & (o == 1)))
    d = int(np.sum(~p & (o == 0)))
    return a, b, c, d


def tss_hss(a, b, c, d):
    pod, pofd = Fraction(a, a + c), Fraction(b, b + d)
    hss = Fraction(2 * (a * d - b * c), (a + c) * (c + d) + (a + b) * (b + d))
    return pod, pofd, pod - pofd, hss


# --- casos analiticos
o = np.array([0, 1, 0, 0, 1, 0, 0, 0, 0, 0])
assert brier(o.astype(float), o) == 0.0 and bss(o.astype(float), o) == 1.0
base = float(o.mean())
clim = np.full(len(o), base)
assert abs(bss(clim, o)) < 1e-12  # la climatologia tiene BSS = 0 exactamente
print(f"pronostico perfecto: BS = 0, BSS = 1;  climatologia (base {base}): BS = {brier(clim, o):.3f}, BSS = 0")

pod, pofd, tss, hss = tss_hss(30, 20, 10, 140)
print(f"tabla (a,b,c,d)=(30,20,10,140): POD = {pod}, POFD = {pofd}, TSS = {tss} = {float(tss):.4f}, HSS = {hss} = {float(hss):.4f}")
assert tss == Fraction(5, 8) and hss == Fraction(4, 7)
# TSS no cambia si se multiplican por k los no-eventos (b, d); HSS si cambia
_, _, tss2, hss2 = tss_hss(30, 200, 10, 1400)
print(f"con 10 veces mas no-eventos: TSS = {float(tss2):.4f} (igual), HSS = {float(hss2):.4f} (cambia)")
assert tss2 == tss and hss2 != hss

# --- pronostico sintetico
rng = np.random.default_rng(2424)
N = 3000
r = rng.beta(2, 18, N)
ev = (rng.random(N) < r).astype(int)
f = np.clip(r + rng.normal(0, 0.05, N), 0.01, 0.99)
base = ev.mean()
print(f"dias = {N}; frecuencia base = {base:.4f}; Brier del pronostico = {brier(f, ev):.4f}; Brier de la climatologia = {base*(1-base):.4f}")
bs_skill = bss(f, ev)
print(f"BSS frente a climatologia = {bs_skill:.4f}")
assert 0 < bs_skill < 0.5
a, b, c, d = table(f, ev, 0.2)
pod, pofd, tss, hss = tss_hss(a, b, c, d)
print(f"umbral 0.2: a={a} b={b} c={c} d={d}; POD = {float(pod):.3f}; POFD = {float(pofd):.3f}; TSS = {float(tss):.3f}; HSS = {float(hss):.3f}")
assert float(tss) > 0
# pronostico "siempre no": TSS = 0
a0, b0, c0, d0 = table(np.zeros(N), ev, 0.2)
assert tss_hss(a0, b0, c0, d0)[2] == 0
print(f"pronostico 'siempre no': TSS = {float(tss_hss(a0, b0, c0, d0)[2]):.3f}; exactitud = {(a0+d0)/N:.3f}  (alta exactitud, habilidad nula)")
# bootstrap
idx = rng.integers(0, N, (1000, N))
bss_bs = np.array([bss(f[i], ev[i]) for i in idx])
lo, hi = np.percentile(bss_bs, [2.5, 97.5])
print(f"BSS bootstrap (1000): IC 95 % = [{lo:.3f}, {hi:.3f}]")
assert lo < bs_skill < hi
# BSS frente a otra referencia: pronostico de persistencia de ayer
persist = np.concatenate([[base], ev[:-1].astype(float)])
print(f"BSS frente a persistencia = {bss(f, ev, persist):.3f}  (la referencia cambia el valor)")
print("Pruebas superadas.")
