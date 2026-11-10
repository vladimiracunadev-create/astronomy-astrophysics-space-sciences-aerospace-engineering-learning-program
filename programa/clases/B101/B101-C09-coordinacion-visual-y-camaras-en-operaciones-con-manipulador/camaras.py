#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B101-C09: cobertura de camaras, puntos ciegos, oclusion y resolucion espacial en una operacion con manipulador.

Escena SINTETICA: zona de trabajo (caja de 2 x 2 x 1 m centrada en el origen), una carga esferica de radio 0.4 m en el origen que ocluye,
tres camaras de campo de vision circular de 60 grados (2 theta = 60) y alcance 0.3 a 12 m, resolucion de 1920 pixeles. Unidades: m, grados.
Comprobaciones independientes: angulo por arccos frente a producto escalar; oclusion esfera-segmento exacta frente a muestreo denso.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b101_comun import *

cabecera("Datos SINTETICOS: caja de trabajo 2x2x1 m, carga esferica de 0.4 m, camaras de 60 grados, 1920 pixeles")
rng = np.random.default_rng(109)
CENTRO, RADIO = np.zeros(3), 0.4
FOV, RMIN, RMAX, NPIX = 60.0, 0.3, 12.0, 1920


def unit(v):
    return v / np.linalg.norm(v)


CAMS = {
    "base": (np.array([-3.0, 0.0, 1.5]), unit(np.array([3.0, 0.0, -1.0]))),
    "codo": (np.array([0.0, -3.5, 2.0]), unit(np.array([0.0, 3.5, -2.0]))),
    "mano": (np.array([0.0, 0.0, 2.2]), unit(np.array([0.0, 0.0, -1.0]))),
}


def segmento_toca_esfera(a, b, c=CENTRO, r=RADIO):
    """Distancia minima de c al segmento ab menor que r (ignora los extremos que esten dentro de la esfera)."""
    d = b - a
    t = np.clip((c - a) @ d / (d @ d), 0, 1)
    return np.linalg.norm(a + t * d - c) < r


def segmento_toca_esfera_muestreo(a, b, c=CENTRO, r=RADIO, n=4000):
    t = np.linspace(0, 1, n)[:, None]
    return bool((np.linalg.norm(a + t * (b - a) - c, axis=1) < r).any())


def visible(cam, p):
    pos, eje = CAMS[cam] if isinstance(cam, str) else cam
    rayo = p - pos
    dist = np.linalg.norm(rayo)
    if dist < RMIN or dist > RMAX:
        return False
    if np.degrees(np.arccos(np.clip(eje @ rayo / dist, -1, 1))) > FOV / 2:
        return False
    if np.linalg.norm(p - CENTRO) < RADIO:
        return False
    return not segmento_toca_esfera(pos, p)


# comprobaciones de la geometria
d_ang = 0.0
for _ in range(500):
    v, w = rng.normal(size=3), rng.normal(size=3)
    a1 = np.arccos(np.clip(unit(v) @ unit(w), -1, 1))
    a2 = np.arctan2(np.linalg.norm(np.cross(v, w)), v @ w)
    d_ang = max(d_ang, abs(a1 - a2))
print(f"Angulo por arccos del producto escalar frente a atan2 de |v x w| (500 pares): diferencia max = {np.degrees(d_ang):.2e} grados")
comprobar(d_ang < 1e-6, "angulos")
desacuerdo = 0
for _ in range(500):
    a, b = rng.uniform(-3, 3, 3), rng.uniform(-3, 3, 3)
    desacuerdo += segmento_toca_esfera(a, b) != segmento_toca_esfera_muestreo(a, b)
print(f"Oclusion esfera-segmento exacta frente a muestreo de 4000 puntos (500 segmentos): desacuerdos = {desacuerdo}")
comprobar(desacuerdo <= 1, "oclusion")

# malla de puntos de la caja de trabajo (paso 0.1 m): 21 x 21 x 11
xs, ys, zs = np.linspace(-1, 1, 21), np.linspace(-1, 1, 21), np.linspace(-0.5, 0.5, 11)
puntos = np.array([[x, y, z] for x in xs for y in ys for z in zs])
fuera = np.linalg.norm(puntos - CENTRO, axis=1) >= RADIO
print(f"Puntos de la malla: {len(puntos)} ; fuera de la carga: {fuera.sum()}")
vis = {c: np.array([visible(c, p) for p in puntos]) for c in CAMS}
print("Cobertura de la zona de trabajo (puntos fuera de la carga):")
for c in CAMS:
    print(f"  camara {c:5s}: {100 * vis[c][fuera].mean():5.1f} %")
import itertools
cobs = {}
for k in (1, 2, 3):
    mejor = max(itertools.combinations(CAMS, k), key=lambda s: np.logical_or.reduce([vis[c] for c in s])[fuera].mean())
    cobs[k] = np.logical_or.reduce([vis[c] for c in mejor])[fuera].mean()
    print(f"  mejor combinacion de {k}: {', '.join(mejor):17s} -> {100 * cobs[k]:5.1f} %")
comprobar(cobs[1] < cobs[2] <= cobs[3], "mas camaras, mas cobertura")
n_vis = sum(vis[c] for c in CAMS)
ciegos = fuera & (n_vis == 0)
dobles = fuera & (n_vis >= 2)
print(f"Puntos ciegos con las 3 camaras: {ciegos.sum()} ({100 * ciegos.sum() / fuera.sum():.1f} %) ; vistos por al menos 2: {dobles.sum()} ({100 * dobles.sum() / fuera.sum():.1f} %)")
sombra = np.array([p for p, c in zip(puntos, ciegos) if c])
if len(sombra):
    print(f"  los puntos ciegos se extienden de x = {sombra[:, 0].min():.1f} a {sombra[:, 0].max():.1f} m, z = {sombra[:, 2].min():.1f} a {sombra[:, 2].max():.1f} m")

# resolucion espacial: tamano de pixel en el objeto
print("Tamano de pixel en el objeto = 2 d tan(theta) / N (theta = 30 grados, N = 1920):")
for d in (1.0, 2.0, 5.0, 10.0):
    gsd = 2 * d * np.tan(np.radians(FOV / 2)) / NPIX
    print(f"  d = {d:4.1f} m: {gsd * 1000:6.3f} mm/pixel")
comprobar(abs(2 * 5.0 * np.tan(np.radians(30)) / NPIX * 1000 - 3.007) < 0.01, "tamano de pixel a 5 m")
# angulo entre dos camaras para triangular
pb = CAMS["base"][0] - CENTRO
pc = CAMS["codo"][0] - CENTRO
ang = np.degrees(np.arccos(unit(pb) @ unit(pc)))
print(f"Angulo entre las lineas de vista de 'base' y 'codo' hacia el origen = {ang:.1f} grados (criterio ilustrativo de triangulacion: >= 30)")
comprobar(ang > 30, "angulo de triangulacion")
fin()
