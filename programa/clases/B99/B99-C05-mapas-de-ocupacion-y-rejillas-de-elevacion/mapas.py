#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C05: rejilla de ocupacion con log-odds y rejilla de elevacion con pendiente y rugosidad, en entornos SINTETICOS.

Ocupacion: sala de 20 x 20 m con rejilla de 0.25 m (80 x 80 celdas); un sensor de 360 rayos y 10 m de alcance (ruido de
rango 0.05 m) desde 8 poses; cada rayo marca libres las celdas atravesadas (Bresenham) y ocupada la celda final, con la
actualizacion aditiva en log-odds L = ln(p/(1-p)) y limites [lmin, lmax] (politica de recorte descrita en OctoMap).
Elevacion: nube de 40 000 puntos 3D (ruido vertical 0.03 m) sobre un plano de 8 grados con una roca gaussiana; rejilla de 0.5 m
con media por celda, pendiente por gradiente y rugosidad por residuo. Unidades: m, rad y grados. Semillas fijas.
Probabilidades del modelo de sensor (p_ocupado = 0.7, p_libre = 0.4) y umbrales de traversabilidad: SINTETICOS.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: sala de 20 x 20 m, celdas de 0.25 m, 8 poses de sensor; terreno de 10 x 10 m con 40 000 puntos")
rng = np.random.default_rng(31)
RES, N = 0.25, 80

# ---- verdad: muros perimetrales, dos bloques rectangulares y un pilar circular
verdad = np.zeros((N, N), bool)
verdad[0, :] = verdad[-1, :] = verdad[:, 0] = verdad[:, -1] = True
verdad[20:32, 24:30] = True
verdad[50:56, 40:66] = True
yy, xx = np.mgrid[0:N, 0:N]
verdad |= (yy - 30) ** 2 + (xx - 58) ** 2 <= 16


def en_rejilla(p):
    return int(p[1] // RES), int(p[0] // RES)          # (fila, columna) = (y, x)


def rayo_verdad(origen, ang, alcance=10.0, paso=0.05):
    for r in np.arange(paso, alcance, paso):
        f, c = en_rejilla(origen + r * np.array([math.cos(ang), math.sin(ang)]))
        if not (0 <= f < N and 0 <= c < N):
            return None
        if verdad[f, c]:
            return r
    return None


def bresenham(f0, c0, f1, c1):
    celdas = []
    df, dc = abs(f1 - f0), abs(c1 - c0)
    sf, sc = (1 if f1 > f0 else -1), (1 if c1 > c0 else -1)
    err = dc - df
    f, c = f0, c0
    while True:
        celdas.append((f, c))
        if (f, c) == (f1, c1):
            break
        e2 = 2 * err
        if e2 > -df:
            err -= df
            c += sc
        if e2 < dc:
            err += dc
            f += sf
    return celdas


P_OCC, P_LIBRE = 0.7, 0.4
L_OCC, L_LIBRE = math.log(P_OCC / (1 - P_OCC)), math.log(P_LIBRE / (1 - P_LIBRE))
L_MIN, L_MAX = -2.0, 3.5
L = np.zeros((N, N))                 # log-odds 0 = p 0.5 = desconocido
visto = np.zeros((N, N), bool)
poses = [(3, 3), (3, 17), (10, 10), (17, 3), (17, 17), (10, 3), (3, 10), (10, 17)]
cobertura = []
for (px, py) in poses:
    o = np.array([px + 0.1, py + 0.1])
    f0, c0 = en_rejilla(o)
    for ang in np.linspace(0, 2 * math.pi, 360, endpoint=False):
        r = rayo_verdad(o, ang)
        golpe = r is not None
        rr = (r + rng.normal(0, 0.05)) if golpe else 10.0
        punta = o + rr * np.array([math.cos(ang), math.sin(ang)])
        f1, c1 = en_rejilla(punta)
        f1, c1 = min(max(f1, 0), N - 1), min(max(c1, 0), N - 1)
        celdas = bresenham(f0, c0, f1, c1)
        for k, (f, c) in enumerate(celdas):
            if k == len(celdas) - 1 and golpe:
                L[f, c] = min(max(L[f, c] + L_OCC, L_MIN), L_MAX)
            else:
                L[f, c] = min(max(L[f, c] + L_LIBRE, L_MIN), L_MAX)
            visto[f, c] = True
    cobertura.append(float(visto.mean()))
print("Cobertura de la rejilla tras cada pose: " + " ".join(f"{c:.0%}" for c in cobertura))
comprobar(all(cobertura[i + 1] >= cobertura[i] for i in range(len(cobertura) - 1)), "la cobertura no puede bajar")

# 1) Actualizacion en log-odds equivale al producto de Bayes en probabilidades
obs = [True, True, False, True, False, False, True, True]          # secuencia sintetica de golpes (True) y pasos (False)
p = 0.5
for o_ in obs:
    pm = P_OCC if o_ else P_LIBRE
    num = p * pm
    p = num / (num + (1 - p) * (1 - pm))
l = sum(L_OCC if o_ else L_LIBRE for o_ in obs)
p_log = 1 / (1 + math.exp(-l))
print(f"Bayes en probabilidad: {p:.12f} ; suma en log-odds: {p_log:.12f} ; diferencia = {abs(p - p_log):.1e}")
comprobar(abs(p - p_log) < 1e-12, "el log-odds debe equivaler al producto de Bayes")

# 2) Exactitud de la clasificacion de las celdas observadas
prob = 1 / (1 + np.exp(-L))
ocupada = prob > 0.5
libre = prob < 0.5
sel = visto & (ocupada | libre)
acc = float(((ocupada == verdad) & sel).sum() / sel.sum())
tp = int((ocupada & verdad & visto).sum())
fp = int((ocupada & ~verdad & visto).sum())
fn = int((~ocupada & verdad & visto).sum())
print(f"Celdas: {N * N}; observadas = {visto.sum()} ({visto.mean():.0%}); desconocidas = {int((~visto).sum())}")
print(f"Celdas observadas: exactitud = {acc:.1%}; ocupadas verdaderas halladas = {tp}; falsas ocupadas = {fp}; ocupadas perdidas = {fn}")
comprobar(acc > 0.93, "la exactitud de las celdas observadas debe ser alta")
comprobar(fn < 0.2 * verdad[visto].sum(), "no deben perderse muchas celdas ocupadas observadas")

# 3) Recorte (clamping): una celda ocupada que se libera tras pocos pasos
l_sin = 20 * L_OCC
l_con = min(l_sin, L_MAX)
pasos_sin = math.ceil((l_sin) / -L_LIBRE)
pasos_con = math.ceil((l_con) / -L_LIBRE)
print(f"Tras 20 golpes: sin recorte L = {l_sin:.1f}, necesita {pasos_sin} pasos libres para volver a 0; con recorte L = {l_con:.1f}, necesita {pasos_con}")
comprobar(pasos_con < pasos_sin, "el recorte debe acelerar la adaptacion a cambios")

# ---- rejilla de elevacion
M, RESE = 10.0, 0.5
NE = int(M / RESE)
n_pts = 40000
px_ = rng.uniform(0, M, n_pts)
py_ = rng.uniform(0, M, n_pts)
TAN = math.tan(math.radians(8.0))


def terreno(x, y, con_roca=True):
    z = TAN * x
    if con_roca:
        z = z + 0.4 * np.exp(-((x - 6.5) ** 2 + (y - 4.0) ** 2) / (2 * 0.6**2))
    return z


pz = terreno(px_, py_) + rng.normal(0, 0.03, n_pts)
fi = np.minimum((py_ // RESE).astype(int), NE - 1)
ci = np.minimum((px_ // RESE).astype(int), NE - 1)
cnt = np.zeros((NE, NE))
s1 = np.zeros((NE, NE))
np.add.at(cnt, (fi, ci), 1)
np.add.at(s1, (fi, ci), pz)
media = s1 / cnt
cx = (np.arange(NE) + 0.5) * RESE
CX, CY = np.meshgrid(cx, cx)
# error de la media por celda frente a la verdad en el centro (celdas planas, lejos de la roca; la pendiente promedia por simetria)
plano = (np.hypot(CX - 6.5, CY - 4.0) > 2.0)
err_media = media - terreno(CX, CY, con_roca=False)
rms = float(np.sqrt(np.mean(err_media[plano] ** 2)))
esperado = 0.03 / math.sqrt(cnt.mean())
print(f"Puntos por celda (media) = {cnt.mean():.0f}; error rms de la media en celdas planas = {rms * 100:.2f} cm (sigma/sqrt(n) = {esperado * 100:.2f} cm)")
comprobar(rms < 1.5 * esperado, "el error de la media debe seguir sigma/sqrt(n)")
gy, gx = np.gradient(media, RESE)
pend = np.degrees(np.arctan(np.hypot(gx, gy)))
plana_int = plano[2:-2, 2:-2]
pm = float(np.mean(pend[2:-2, 2:-2][plana_int]))
print(f"Pendiente media en terreno sin roca = {pm:.2f} grados (verdad: 8.00)")
comprobar(abs(pm - 8.0) < 0.5, "la pendiente debe recuperarse a 0.5 grados")
# rugosidad: desviacion tipica del residuo de la media respecto del plano ajustado en ventanas 3x3
rug = np.zeros_like(media)
for i in range(1, NE - 1):
    for j in range(1, NE - 1):
        v = media[i - 1:i + 2, j - 1:j + 2]
        A = np.column_stack([np.ones(9), CX[i - 1:i + 2, j - 1:j + 2].ravel(), CY[i - 1:i + 2, j - 1:j + 2].ravel()])
        coef, *_ = np.linalg.lstsq(A, v.ravel(), rcond=None)
        rug[i, j] = np.std(v.ravel() - A @ coef)
UMBRAL_PEND, UMBRAL_RUG = 15.0, 0.05
trav = (pend < UMBRAL_PEND) & (rug < UMBRAL_RUG)
roca = np.hypot(CX - 6.5, CY - 4.0) < 0.9
interior = np.zeros_like(trav)
interior[1:-1, 1:-1] = True
print(f"Traversables (pendiente < {UMBRAL_PEND:.0f} grados y rugosidad < {UMBRAL_RUG * 100:.0f} cm): {trav[interior].mean():.0%} del interior; "
      f"pendiente maxima = {pend[interior].max():.1f} grados; rugosidad maxima = {rug[interior].max() * 100:.1f} cm")
print(f"Celdas de la roca (radio 0.9 m) no traversables = {(~trav[roca & interior]).sum()} de {(roca & interior).sum()}; celdas lejanas no traversables = {(~trav[plano & interior]).sum()}")
comprobar((~trav[roca & interior]).sum() >= 0.5 * (roca & interior).sum(), "la roca debe quedar marcada como no traversable")
comprobar((~trav[plano & interior]).sum() <= 0.05 * (plano & interior).sum(), "el terreno liso no debe marcarse casi nunca")
fin()
