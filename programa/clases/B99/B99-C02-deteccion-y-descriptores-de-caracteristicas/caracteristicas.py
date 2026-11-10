#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B99-C02: esquinas de Harris, descriptor de parche normalizado y prueba de razon de distancias en imagenes SINTETICAS.

Imagen sintetica de 200x200 (rectangulos y manchas con intensidades 0-255). La imagen A es un recorte; la B es el mismo
mundo recortado con un desplazamiento conocido (verdad exacta) mas ruido gaussiano. Detector de Harris (tensor de estructura
con ventana gaussiana), descriptor = parche 11x11 con media cero y norma uno (insensible a ganancia y sesgo de brillo),
emparejamiento por vecino mas cercano con la prueba de razon distancia1/distancia2 (Lowe, 2004, usa 0.8).
Unidades: pixeles e intensidad (0-255). Un emparejamiento es correcto si cae a <= 2 px de la posicion verdadera.
Tolerancias: sin ruido la repetibilidad debe ser 100 %. Semilla fija. Todo SINTETICO; no es SIFT ni ORB.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b99_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: imagen de 200x200 px, recorte A y recorte B desplazado (fila -5, columna +7), semilla 5")
rng = np.random.default_rng(5)
M = 200
mundo = np.full((M, M), 90.0)
for _ in range(45):
    r0, c0 = rng.integers(0, M - 25, 2)
    h, w = rng.integers(8, 25, 2)
    mundo[r0:r0 + h, c0:c0 + w] = rng.uniform(20, 235)
yy, xx = np.mgrid[0:M, 0:M]
for _ in range(25):
    cy, cx = rng.uniform(0, M, 2)
    mundo += rng.uniform(-60, 60) * np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * rng.uniform(2, 5) ** 2))
mundo = np.clip(mundo, 0, 255)
S = 160
FILA_B, COL_B = 5, -7     # B(r', c') = mundo(r' + 20 + 5, c' + 20 - 7): el punto A(r, c) aparece en B(r - 5, c + 7)


def recortes(sigma, gain=1.0, bias=0.0, semilla=0):
    r = np.random.default_rng(semilla)
    A = mundo[20:20 + S, 20:20 + S] + r.normal(0, sigma, (S, S))
    B = mundo[20 + FILA_B:20 + FILA_B + S, 20 + COL_B:20 + COL_B + S] * gain + bias + r.normal(0, sigma, (S, S))
    return A, B


def gauss1d(s):
    k = np.arange(-int(3 * s), int(3 * s) + 1)
    g = np.exp(-k**2 / (2 * s**2))
    return g / g.sum()


def suavizar(I, s):
    g = gauss1d(s)
    I = np.apply_along_axis(lambda v: np.convolve(v, g, mode="same"), 0, I)
    return np.apply_along_axis(lambda v: np.convolve(v, g, mode="same"), 1, I)


def harris(I, k=0.05, s=1.5, rel=0.01, n_max=150, borde=8):
    Iy, Ix = np.gradient(suavizar(I, 1.0))
    Sxx, Syy, Sxy = suavizar(Ix * Ix, s), suavizar(Iy * Iy, s), suavizar(Ix * Iy, s)
    R = Sxx * Syy - Sxy**2 - k * (Sxx + Syy) ** 2
    R[:borde, :] = R[-borde:, :] = 0
    R[:, :borde] = R[:, -borde:] = 0
    umbral = rel * R.max()
    maximos = (R > umbral)
    for dr in (-2, -1, 0, 1, 2):
        for dc in (-2, -1, 0, 1, 2):
            if dr or dc:
                maximos &= R >= np.roll(np.roll(R, dr, 0), dc, 1)
    pts = np.argwhere(maximos)
    orden = np.argsort(-R[maximos])[:n_max]
    return pts[orden]


def descriptores(I, pts, h=5):
    D = []
    for r, c in pts:
        p = I[r - h:r + h + 1, c - h:c + h + 1].ravel()
        p = p - p.mean()
        D.append(p / (np.linalg.norm(p) + 1e-12))
    return np.array(D)


def emparejar(DA, DB, razon):
    d = np.linalg.norm(DA[:, None, :] - DB[None, :, :], axis=2)
    orden = np.argsort(d, axis=1)
    i = np.arange(len(DA))
    d1, d2 = d[i, orden[:, 0]], d[i, orden[:, 1]]
    ok = d1 / (d2 + 1e-12) < razon
    return [(a, orden[a, 0]) for a in np.where(ok)[0]]


def evaluar(sigma, razon, gain=1.0, bias=0.0, semilla=0, rotar=False):
    A, B = recortes(sigma, gain, bias, semilla)
    pA, pB = harris(A), harris(B)
    esperado = pA - np.array([FILA_B, COL_B])          # posicion verdadera en B de cada punto de A
    if rotar:
        B = np.rot90(B)
        pB = harris(B)
        esperado = np.column_stack([S - 1 - esperado[:, 1], esperado[:, 0]])  # punto de B en B rotada 90 grados
    dentro = (esperado[:, 0] >= 8) & (esperado[:, 0] < S - 8) & (esperado[:, 1] >= 8) & (esperado[:, 1] < S - 8)
    # repetibilidad: puntos de A cuya posicion verdadera tiene un punto de Harris de B a <= 2 px
    dist = np.linalg.norm(pB[None, :, :] - esperado[:, None, :], axis=2).min(axis=1)
    repetidos = dentro & (dist <= 2.0)
    rep = repetidos.sum() / max(dentro.sum(), 1)
    DA, DB = descriptores(A, pA), descriptores(B, pB)
    pares = emparejar(DA, DB, razon)
    buenos = sum(np.linalg.norm(pB[b] - esperado[a]) <= 2.0 for a, b in pares)
    prec = buenos / len(pares) if pares else float("nan")
    exh = buenos / max(repetidos.sum(), 1)
    return len(pA), len(pB), rep, len(pares), prec, exh


# 1) Sin ruido: la deteccion debe ser repetible y el emparejamiento casi perfecto
nA, nB, rep0, n0, prec0, exh0 = evaluar(0.0, 0.8)
print(f"Sin ruido: puntos A = {nA}, B = {nB}, repetibilidad = {rep0:.0%}, emparejamientos = {n0}, precision = {prec0:.0%}, exhaustividad = {exh0:.0%}")
comprobar(rep0 > 0.999, "sin ruido, la repetibilidad debe ser 100 %")
comprobar(prec0 > 0.95, "sin ruido, la precision del emparejamiento debe ser alta")

# 2) Efecto del ruido y de la razon (media de 5 semillas)
print("sigma[niv]  razon   n_pares  precision  exhaustividad  repetibilidad")
tabla = {}
for sigma in (2.0, 6.0, 12.0):
    for razon in (0.6, 0.8, 1.01):
        vals = np.array([evaluar(sigma, razon, semilla=s) for s in range(5)])
        m = np.nanmean(vals, axis=0)
        tabla[(sigma, razon)] = m
        etiqueta = "sin prueba" if razon > 1 else f"{razon:.2f}"
        print(f"{sigma:9.1f}  {etiqueta:>10}  {m[3]:7.1f}  {m[4]:9.2%}  {m[5]:13.2%}  {m[2]:13.2%}")
comprobar(tabla[(6.0, 0.8)][4] > tabla[(6.0, 1.01)][4], "la prueba de razon debe subir la precision")
comprobar(tabla[(6.0, 0.6)][4] >= tabla[(6.0, 0.8)][4] - 1e-9, "una razon mas estricta no debe bajar la precision")
comprobar(tabla[(6.0, 0.6)][3] <= tabla[(6.0, 0.8)][3], "una razon mas estricta no debe aceptar mas pares")
comprobar(tabla[(12.0, 0.8)][4] <= tabla[(2.0, 0.8)][4] + 1e-9, "mas ruido no debe mejorar la precision")

# 3) Insensibilidad a ganancia y sesgo de brillo (descriptor de media cero y norma uno)
g = evaluar(2.0, 0.8, gain=1.4, bias=-30.0)
b = evaluar(2.0, 0.8)
print(f"Cambio de brillo (ganancia 1.4, sesgo -30): precision = {g[4]:.0%} frente a {b[4]:.0%} sin cambio")
comprobar(g[4] > 0.8 * b[4], "el descriptor normalizado debe tolerar cambios de ganancia y sesgo")

# 4) Limite: el descriptor de parche no es invariante a la rotacion
r = evaluar(2.0, 0.8, rotar=True)
print(f"Imagen B girada 90 grados: repetibilidad = {r[2]:.0%}, pares = {r[3]}, precision = {r[4]:.0%} (el parche no es invariante a la rotacion)")
comprobar(r[2] > 0.5, "el detector de Harris debe seguir encontrando las esquinas tras girar")
comprobar(not (r[4] > 0.5), "el descriptor de parche debe fallar tras una rotacion de 90 grados")
fin()
