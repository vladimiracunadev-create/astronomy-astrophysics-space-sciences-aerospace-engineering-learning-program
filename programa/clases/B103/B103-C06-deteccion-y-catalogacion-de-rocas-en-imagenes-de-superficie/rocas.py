#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C06: deteccion y catalogo de rocas en una imagen SINTETICA de superficie.

Todo es sintetico (semilla 103): imagen cenital de 600 x 600 px con escala en el terreno de 0.010 m/px (6 m x 6 m),
arena de 150 niveles de gris con textura, 400 rocas de diametro D con distribucion acumulada N(>D) ~ D^-b, b = 2.0 (verdad),
entre 0.05 y 1.0 m, brillo 185 (+35 sobre la arena) con un gradiente de iluminacion y una sombra oscura hacia +x de longitud
(0.5 D)/tan(30 grados). Valores ILUSTRATIVOS; la forma de la distribucion es una eleccion de ensenanza, no un dato medido.
Metodo: suavizado 3x3, umbral (arena + 15 niveles), componentes conexos 4-vecinos (pila, sin scipy), area minima 12 px,
D = 2 sqrt(A/pi) * escala. Emparejado con la verdad por distancia de centros < 0.6 D verdadero. Ajuste de la ley de potencias por maxima
verosimilitud sobre D >= D_min: b = n / sum ln(D_i / D_min) con incertidumbre b / sqrt(n) y remuestreo bootstrap.
Verificacion: recall por clase de tamano; ajuste frente a la verdad b = 2.0; ajuste ingenuo con todas las detecciones.
Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

S, ESC, B_VERDAD, DMIN, DMAX, NR = 600, 0.010, 2.0, 0.05, 1.0, 400
ELEV = np.radians(30.0)


def caja(a, n):
    r = n // 2
    p = np.pad(a, r, mode="reflect")
    c = np.cumsum(np.cumsum(np.pad(p, ((1, 0), (1, 0))), axis=0), axis=1)
    return (c[n:, n:] - c[:-n, n:] - c[n:, :-n] + c[:-n, :-n]) / (n * n)


def generar(rng):
    u = rng.uniform(0, 1, NR)
    d = DMIN * (1 - u * (1 - (DMAX / DMIN) ** -B_VERDAD)) ** (-1 / B_VERDAD)  # inversa de la acumulada truncada
    d = np.sort(d)[::-1]
    base = rng.normal(0, 1, (S, S))
    for _ in range(2):
        base = caja(base, 5)
    img = 150 + base / base.std() * 5
    yy, xx = np.mgrid[0:S, 0:S]
    centros = []
    for di in d:
        r = di / ESC / 2
        cx, cy = rng.uniform(r + 2, S - r - 2), rng.uniform(r + 2, S - r - 2)
        sl = 0.5 * di / np.tan(ELEV) / ESC  # longitud de la sombra en px
        sombra = (np.abs(yy - cy) < 0.8 * r) & (xx > cx) & (xx < cx + r + sl) & ((xx - cx - r * 0.3) ** 2 / (r + sl) ** 2 + (yy - cy) ** 2 / (0.85 * r) ** 2 < 1)
        img = np.where(sombra, 105 + (img - 150) * 0.3, img)
        disco = (xx - cx) ** 2 + (yy - cy) ** 2 < r * r
        grad = 185 + 10 * (cy - yy) / r * 0.5
        img = np.where(disco, grad, img)
        centros.append((cx, cy))
    img += rng.normal(0, 4.0, img.shape)
    return np.clip(img, 0, 255), d, np.array(centros)


def componentes(mascara):
    etiquetas = np.zeros(mascara.shape, int)
    n = 0
    ys, xs = np.nonzero(mascara)
    for y0, x0 in zip(ys, xs):
        if etiquetas[y0, x0]:
            continue
        n += 1
        pila = [(y0, x0)]
        etiquetas[y0, x0] = n
        while pila:
            y, x = pila.pop()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                yy, xx = y + dy, x + dx
                if 0 <= yy < S and 0 <= xx < S and mascara[yy, xx] and not etiquetas[yy, xx]:
                    etiquetas[yy, xx] = n
                    pila.append((yy, xx))
    return etiquetas, n


def detectar(img):
    suav = caja(img, 3)
    mascara = suav > 150 + 15 + 5  # arena nominal 150 mas 20 niveles
    et, n = componentes(mascara)
    cat = []
    for k in range(1, n + 1):
        yy, xx = np.nonzero(et == k)
        if len(yy) < 12:
            continue
        cat.append((xx.mean(), yy.mean(), 2 * np.sqrt(len(yy) / np.pi) * ESC))
    return np.array(cat)


def mle(dd, dmin):
    x = dd[dd >= dmin]
    b = len(x) / np.sum(np.log(x / dmin))
    return b, b / np.sqrt(len(x)), len(x)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    rng = np.random.default_rng(103)
    img, d_ver, c_ver = generar(rng)
    print(f"DATOS SINTETICOS (semilla 103): imagen {S}x{S} px, escala {ESC} m/px, {NR} rocas, b verdadero = {B_VERDAD}, D entre {DMIN} y {DMAX} m")
    cat = detectar(img)
    print(f"Detecciones: {len(cat)} componentes (area >= 12 px)")
    # emparejado
    usado = set()
    hallada = np.zeros(NR, bool)
    d_est = np.full(NR, np.nan)
    for i in range(NR):
        dist = np.hypot(cat[:, 0] * 1.0 - c_ver[i, 0], cat[:, 1] - c_ver[i, 1]) * ESC
        for j in np.argsort(dist):
            if dist[j] < 0.6 * d_ver[i] and j not in usado:
                usado.add(j)
                hallada[i] = True
                d_est[i] = cat[j, 2]
                break
            if dist[j] >= 0.6 * d_ver[i]:
                break
    fp = len(cat) - len(usado)
    print(f"Verdaderos positivos = {int(hallada.sum())}, falsos negativos = {int((~hallada).sum())}, falsos positivos = {fp}")
    print(f"Precision = {hallada.sum()/len(cat):.3f}; exhaustividad global = {hallada.mean():.3f}")
    print("Clase de tamano D [m]    verdaderas   halladas   exhaustividad   D estimado / D verdadero (mediana)")
    for lo, hi in ((0.05, 0.10), (0.10, 0.20), (0.20, 0.50), (0.50, 1.01)):
        m = (d_ver >= lo) & (d_ver < hi)
        h = m & hallada
        rat = np.median(d_est[h] / d_ver[h]) if h.any() else float("nan")
        print(f"  {lo:4.2f} - {hi:4.2f}          {m.sum():6d}   {h.sum():8d}   {h.sum()/max(m.sum(),1):13.3f}   {rat:10.3f}")
    # ajustes
    dd = cat[:, 2]
    b_all, s_all, n_all = mle(dd, dd.min())
    b_ver, s_ver, n_ver = mle(d_ver, DMIN)
    print(f"Verdad (todas las rocas, D >= {DMIN} m): b = {b_ver:.3f} +- {s_ver:.3f} (n = {n_ver}); parametro del generador = {B_VERDAD}")
    print(f"Ajuste ingenuo (todas las detecciones, D >= {dd.min():.3f} m): b = {b_all:.3f} +- {s_all:.3f} (n = {n_all})")
    for dmin in (0.10, 0.15, 0.20):
        b, s, n = mle(dd, dmin)
        bs = [mle(rng.choice(dd[dd >= dmin], n), dmin)[0] for _ in range(1000)]
        lo, hi = np.percentile(bs, [2.5, 97.5])
        print(f"Ajuste con D_min = {dmin:.2f} m: b = {b:.3f} +- {s:.3f} (n = {n}); bootstrap 95 %: [{lo:.3f}, {hi:.3f}]")
    # peligro: rocas grandes
    h_ver = 0.5 * d_ver
    print(f"Rocas con altura verdadera >= 0.25 m (D >= 0.5 m): verdad = {int(np.sum(d_ver >= 0.5))}, detectadas = {int(np.sum(hallada & (d_ver >= 0.5)))}")
    cob_ver = np.sum(np.pi * (d_ver / 2) ** 2) / (S * ESC) ** 2
    cob_est = np.sum(np.pi * (dd / 2) ** 2) / (S * ESC) ** 2
    print(f"Suma de areas de discos / area de la imagen (sin descontar solapes): verdad {cob_ver*100:.2f} %, detectada {cob_est*100:.2f} %")
    b_ok, s_ok, _ = mle(dd, 0.15)
    assert abs(b_ok - B_VERDAD) < 3 * s_ok + 0.2
    assert b_all < b_ok
    assert hallada[d_ver >= 0.2].mean() > 0.8
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
