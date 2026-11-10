#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B103-C05: segmentacion semantica de pixeles con regresion softmax sobre imagenes SINTETICAS.

Todo es sintetico (semilla 103): imagenes de 128 x 128 px en niveles de gris (0-255) con 4 clases: 0 arena, 1 lecho rocoso,
2 roca, 3 sombra. La verdad de cada pixel la fija el generador. Las texturas y los niveles medios son ILUSTRATIVOS y no
reproducen ninguna superficie real. 6 imagenes de entrenamiento, 4 de prueba del mismo dominio y 4 de prueba con un cambio de
iluminacion (ganancia 0.6 y desplazamiento -10 niveles, ILUSTRATIVO).
Caracteristicas por pixel (6): media 3x3, media 9x9, desviacion tipica local 5x5, modulo del gradiente, media 9x9 y un sesgo;
estandarizadas con las medias y desviaciones del entrenamiento. Modelo: regresion softmax multinomial con descenso de gradiente
(400 iteraciones, paso 0.5, L2 = 1e-3), sin bibliotecas de aprendizaje automatico. Metricas: exactitud, IoU por clase y mIoU,
matriz de confusion. Variante "normalizada": se resta la media 31 x 31 y se divide por la desviacion local 31 x 31 antes de extraer
las caracteristicas. Verificacion: el modelo supera la clase mayoritaria; el cambio de iluminacion degrada el mIoU; la
normalizacion lo recupera en parte. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

S = 128
CLASES = ["arena", "lecho", "roca", "sombra"]
MEDIAS = np.array([150.0, 110.0, 175.0, 45.0])
SIGMA_TEX = np.array([6.0, 22.0, 12.0, 5.0])
SUAVE = np.array([3, 1, 2, 3])  # radio de suavizado de la textura por clase


def caja(a, n):
    r = n // 2
    p = np.pad(a, r, mode="reflect")
    c = np.cumsum(np.cumsum(np.pad(p, ((1, 0), (1, 0))), axis=0), axis=1)
    s = c[n:, n:] - c[:-n, n:] - c[n:, :-n] + c[:-n, :-n]
    return s / (n * n)


def suave(a, n):
    return caja(a, n) if n > 1 else a


def generar(rng):
    campo = rng.normal(0, 1, (S, S))
    for _ in range(4):
        campo = suave(campo, 15)
    etiqueta = (campo > np.median(campo)).astype(int)  # 0 arena, 1 lecho
    yy, xx = np.mgrid[0:S, 0:S]
    roca = np.zeros((S, S), bool)
    sombra = np.zeros((S, S), bool)
    for _ in range(14):
        cx, cy, r = rng.uniform(10, S - 10), rng.uniform(10, S - 10), rng.uniform(3, 8)
        roca |= (xx - cx) ** 2 + (yy - cy) ** 2 < r * r
        sombra |= (xx - cx - 0.9 * r) ** 2 + (yy - cy) ** 2 < (0.9 * r) ** 2
    etiqueta[sombra & ~roca] = 3
    etiqueta[roca] = 2
    img = np.zeros((S, S))
    for k in range(4):
        tex = rng.normal(0, 1, (S, S))
        for _ in range(2):
            tex = suave(tex, 2 * SUAVE[k] + 1)
        tex = tex / tex.std() * SIGMA_TEX[k]
        img = np.where(etiqueta == k, MEDIAS[k] + tex, img)
    img = suave(img, 3) * 0.5 + img * 0.5 + rng.normal(0, 2.0, (S, S))
    return np.clip(img, 0, 255), etiqueta


def caracteristicas(img, normalizar=False):
    if normalizar:
        m = caja(img, 31)
        sd = np.sqrt(np.maximum(caja(img ** 2, 31) - m ** 2, 1.0))
        img = (img - m) / sd * 40 + 128
    m3, m9 = caja(img, 3), caja(img, 9)
    sd5 = np.sqrt(np.maximum(caja(img ** 2, 5) - caja(img, 5) ** 2, 0))
    gy, gx = np.gradient(m3)
    f = np.stack([m3, m9, sd5, np.hypot(gx, gy), caja(img, 21), np.ones_like(img)], axis=-1)
    return f.reshape(-1, f.shape[-1])


def entrenar(x, y, iteraciones=400, paso=0.5, l2=1e-3):
    w = np.zeros((x.shape[1], 4))
    onehot = np.eye(4)[y]
    for _ in range(iteraciones):
        z = x @ w
        z -= z.max(axis=1, keepdims=True)
        p = np.exp(z)
        p /= p.sum(axis=1, keepdims=True)
        w -= paso * (x.T @ (p - onehot) / len(x) + l2 * w)
    return w


def predecir(x, w):
    return np.argmax(x @ w, axis=1)


def metricas(y, p):
    conf = np.zeros((4, 4), int)
    np.add.at(conf, (y, p), 1)
    iou = np.array([conf[k, k] / (conf[k, :].sum() + conf[:, k].sum() - conf[k, k]) for k in range(4)])
    return conf, iou, np.trace(conf) / conf.sum()


def conjunto(rng, n, cambio=False):
    xs, ys = [], []
    for _ in range(n):
        img, et = generar(rng)
        if cambio:
            img = np.clip(img * 0.6 - 10, 0, 255)
        xs.append(img)
        ys.append(et.ravel())
    return xs, np.concatenate(ys)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 103): 4 clases, imagenes 128x128; texturas y niveles ILUSTRATIVOS")
    rng = np.random.default_rng(103)
    tr_i, tr_y = conjunto(rng, 6)
    te_i, te_y = conjunto(np.random.default_rng(203), 4)
    sh_i, sh_y = conjunto(np.random.default_rng(203), 4, cambio=True)  # mismas escenas, otra iluminacion
    frec = np.bincount(tr_y, minlength=4) / len(tr_y)
    print("Frecuencia de clases (entrenamiento): " + ", ".join(f"{n} {f*100:.1f} %" for n, f in zip(CLASES, frec)))
    print(f"Exactitud de predecir siempre la clase mayoritaria ({CLASES[int(np.argmax(frec))]}): {frec.max()*100:.1f} %")
    resultados = {}
    for nombre, norm in (("directa", False), ("normalizada", True)):
        xtr = np.vstack([caracteristicas(i, norm) for i in tr_i])
        mu, sd = xtr.mean(axis=0), xtr.std(axis=0)
        mu[-1], sd[-1] = 0.0, 1.0
        w = entrenar((xtr - mu) / sd, tr_y)
        for dom, imgs, y in (("entrenamiento", tr_i, tr_y), ("prueba", te_i, te_y), ("prueba con cambio de iluminacion", sh_i, sh_y)):
            x = np.vstack([caracteristicas(i, norm) for i in imgs])
            conf, iou, acc = metricas(y, predecir((x - mu) / sd, w))
            resultados[(nombre, dom)] = (conf, iou, acc)
        print(f"\nCaracteristicas {nombre}:")
        print(" dominio                              exactitud   IoU " + "  ".join(f"{c:>6s}" for c in CLASES) + "   mIoU")
        for dom in ("entrenamiento", "prueba", "prueba con cambio de iluminacion"):
            conf, iou, acc = resultados[(nombre, dom)]
            print(f" {dom:34s}  {acc*100:7.2f} %      " + "  ".join(f"{v:6.3f}" for v in iou) + f"  {iou.mean():6.3f}")
    conf = resultados[("directa", "prueba")][0]
    print("\nMatriz de confusion (prueba, directa; filas = verdad, columnas = prediccion):")
    print("         " + " ".join(f"{c:>7s}" for c in CLASES))
    for k, c in enumerate(CLASES):
        print(f" {c:7s} " + " ".join(f"{v:7d}" for v in conf[k]))
    m_prueba = resultados[("directa", "prueba")][1].mean()
    m_cambio = resultados[("directa", "prueba con cambio de iluminacion")][1].mean()
    m_norm = resultados[("normalizada", "prueba con cambio de iluminacion")][1].mean()
    print(f"\nmIoU directa: prueba {m_prueba:.3f} -> con cambio de iluminacion {m_cambio:.3f}; normalizada con cambio {m_norm:.3f}")
    assert resultados[("directa", "prueba")][2] > frec.max() + 0.05
    assert m_cambio < m_prueba - 0.05
    assert m_norm > m_cambio
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
